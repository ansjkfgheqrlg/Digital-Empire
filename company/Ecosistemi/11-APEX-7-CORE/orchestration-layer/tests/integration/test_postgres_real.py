from __future__ import annotations

import asyncio
import os
import subprocess
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path
from uuid import uuid4

PROJECT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT / "src"))

from sqlalchemy import text

from orchestrator.adapters.postgres.grants import PostgresCapabilityStore
from orchestrator.adapters.postgres.queue import LeaseLost, PostgresTaskQueue
from orchestrator.adapters.postgres.uow import PostgresUnitOfWork, create_engine_and_factory
from orchestrator.domain import ActorType, BudgetAmount, RiskClass, Workflow, WorkflowStatus
from orchestrator.governance.grants import CapabilityGrantService, GrantBinding, GrantDenied
from orchestrator.domain.transitions import TransitionContext


DATABASE_URL = os.environ.get("OCP_TEST_DATABASE_URL")


@unittest.skipUnless(DATABASE_URL, "OCP_TEST_DATABASE_URL is not configured")
class RealPostgresTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.engine, self.factory = create_engine_and_factory(
            DATABASE_URL, pool_size=2, max_overflow=0
        )
        # Runtime cannot bypass RLS; every test uses a fresh tenant namespace.
        self.tenant = f"test-{uuid4().hex[:12]}"

    async def asyncTearDown(self) -> None:
        await self.engine.dispose()

    def make_workflow(self, tenant: str | None = None) -> Workflow:
        return Workflow.create(
            workflow_id=str(uuid4()),
            tenant_id=tenant or self.tenant,
            workflow_type="repository_adr",
            goal="Create a test ADR",
            risk=RiskClass.R1,
            requested_by="integration-test",
            idempotency_key=f"idem-{uuid4()}",
            budget_limit=BudgetAmount(30000, Decimal("2.00"), 300000),
        )

    async def test_atomic_create_writes_state_audit_and_outbox(self) -> None:
        item = self.make_workflow()
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.workflows.add(item, "trace-integration-0001")
            await uow.commit()

        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            counts = {}
            for table in ("workflows", "audit_events", "outbox_events"):
                result = await uow.session.execute(
                    text(f"SELECT count(*) FROM {table} WHERE tenant_id=:tenant"),
                    {"tenant": self.tenant},
                )
                counts[table] = result.scalar_one()
            await uow.commit()
        self.assertEqual({"workflows": 1, "audit_events": 1, "outbox_events": 1}, counts)

    async def test_rollback_is_atomic(self) -> None:
        item = self.make_workflow()
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.workflows.add(item, "trace-integration-0002")
            # no commit

        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            result = await uow.session.execute(
                text("SELECT count(*) FROM workflows WHERE tenant_id=:tenant"),
                {"tenant": self.tenant},
            )
            self.assertEqual(0, result.scalar_one())
            await uow.commit()

    async def test_privacy_deletion_rls_hides_other_tenant(self) -> None:
        request_id = str(uuid4())
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.session.execute(
                text("""
                    INSERT INTO deletion_requests (
                      request_id, tenant_id, subject_ref_hashes, requested_by, state
                    ) VALUES (
                      CAST(:request_id AS uuid), :tenant, CAST(:subjects AS jsonb),
                      'privacy-test', 'REQUESTED'
                    )
                """),
                {"request_id": request_id, "tenant": self.tenant, "subjects": '["sha256:test"]'},
            )
            await uow.commit()
        other = f"other-{uuid4().hex[:12]}"
        async with PostgresUnitOfWork(self.factory, other) as uow:
            result = await uow.session.execute(
                text("SELECT count(*) FROM deletion_requests WHERE request_id=CAST(:id AS uuid)"),
                {"id": request_id},
            )
            self.assertEqual(0, result.scalar_one())
            await uow.commit()

    async def test_rls_hides_other_tenant(self) -> None:
        owner = self.make_workflow(self.tenant)
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.workflows.add(owner, "trace-integration-0003")
            await uow.commit()

        other_tenant = f"other-{uuid4().hex[:12]}"
        async with PostgresUnitOfWork(self.factory, other_tenant) as uow:
            result = await uow.session.execute(
                text("SELECT count(*) FROM workflows WHERE workflow_id=CAST(:id AS uuid)"),
                {"id": owner.workflow_id},
            )
            self.assertEqual(0, result.scalar_one())
            await uow.commit()

    async def test_optimistic_lock_rejects_second_writer(self) -> None:
        item = self.make_workflow()
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.workflows.add(item, "trace-integration-0004")
            await uow.commit()

        previous = item.version
        event = item.transition(
            WorkflowStatus.VALIDATING,
            ActorType.API,
            TransitionContext(flags=frozenset({"request_persisted"})),
            expected_version=previous,
        )
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.workflows.persist_transition(
                item, previous, event, "trace-integration-0004"
            )
            await uow.commit()

        from orchestrator.domain.errors import StaleVersion
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            with self.assertRaises(StaleVersion):
                await uow.workflows.persist_transition(
                    item, previous, event, "trace-integration-0004"
                )

    async def test_postgres_capability_is_single_use_and_task_bound(self) -> None:
        item = self.make_workflow()
        task_id = str(uuid4())
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.workflows.add(item, "trace-integration-grant")
            await uow.session.execute(
                text("""
                    INSERT INTO tasks (
                      task_id, tenant_id, workflow_id, ordinal, role, objective, status,
                      completion_criteria, capabilities, side_effect, budget_limit,
                      max_attempts, input_ref
                    ) VALUES (
                      CAST(:task_id AS uuid), :tenant, CAST(:workflow_id AS uuid), 0,
                      'implementer', 'grant-test', 'READY', '["done"]'::jsonb,
                      '["repo.read"]'::jsonb, CAST(:side_effect AS jsonb),
                      CAST(:budget AS jsonb), 1, 'artifact://input'
                    )
                """),
                {
                    "task_id": task_id,
                    "tenant": self.tenant,
                    "workflow_id": item.workflow_id,
                    "side_effect": '{"mode":"NONE"}',
                    "budget": '{"tokens":100,"cost_usd":"0.1","duration_ms":1000}',
                },
            )
            binding = GrantBinding(
                self.tenant, item.workflow_id, task_id, "sha256:execution"
            )
            service = CapabilityGrantService(PostgresCapabilityStore(uow.session))
            token, _ = await service.issue(
                subject="agent-a",
                binding=binding,
                capability_scope="repo.read",
                constraints={"path_prefix": "src/"},
                ttl_seconds=60,
            )
            await uow.commit()

        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            service = CapabilityGrantService(PostgresCapabilityStore(uow.session))
            record = await service.consume(token, binding, "repo.read")
            self.assertEqual("repo.read", record.capability_scope)
            await uow.commit()

        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            service = CapabilityGrantService(PostgresCapabilityStore(uow.session))
            with self.assertRaises(GrantDenied):
                await service.consume(token, binding, "repo.read")

    async def test_killed_worker_lease_expires_and_task_is_reclaimed(self) -> None:
        item = self.make_workflow()
        task_id = str(uuid4())
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.workflows.add(item, "trace-chaos-kill")
            await uow.session.execute(
                text("""
                    INSERT INTO tasks (
                      task_id, tenant_id, workflow_id, ordinal, role, objective, status,
                      completion_criteria, capabilities, side_effect, budget_limit,
                      max_attempts, input_ref
                    ) VALUES (
                      CAST(:task_id AS uuid), :tenant, CAST(:workflow_id AS uuid), 0,
                      'implementer', 'chaos-kill', 'READY', '["done"]'::jsonb,
                      '[]'::jsonb, CAST(:side_effect AS jsonb), CAST(:budget AS jsonb),
                      2, 'artifact://input'
                    )
                """),
                {
                    "task_id": task_id,
                    "tenant": self.tenant,
                    "workflow_id": item.workflow_id,
                    "side_effect": '{"mode":"NONE"}',
                    "budget": '{"tokens":100,"cost_usd":"0.1","duration_ms":1000}',
                },
            )
            await uow.commit()

        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "claimed"
            env = {**os.environ, "PYTHONPATH": str(PROJECT / "src")}
            process = await asyncio.create_subprocess_exec(
                sys.executable,
                str(PROJECT / "scripts" / "chaos_claim_and_die.py"),
                "--database-url", DATABASE_URL,
                "--tenant", self.tenant,
                "--lease-seconds", "5",
                "--marker", str(marker),
                env=env,
            )
            return_code = await process.wait()
            self.assertEqual(137, return_code)
            self.assertEqual(task_id, marker.read_text(encoding="utf-8"))

        await asyncio.sleep(5.2)
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            reclaimed = await PostgresTaskQueue(uow.session, self.tenant).claim(
                "replacement-worker", "sha256:replacement", 30
            )
            self.assertEqual(task_id, str(reclaimed["task_id"]))
            self.assertEqual(2, reclaimed["attempt"])
            await uow.commit()

    async def test_two_workers_cannot_claim_same_task_and_stale_token_fails(self) -> None:
        item = self.make_workflow()
        task_id = str(uuid4())
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            await uow.workflows.add(item, "trace-integration-0005")
            await uow.session.execute(
                text("""
                    INSERT INTO tasks (
                      task_id, tenant_id, workflow_id, ordinal, role, objective, status,
                      completion_criteria, capabilities, side_effect, budget_limit,
                      max_attempts, input_ref
                    ) VALUES (
                      CAST(:task_id AS uuid), :tenant, CAST(:workflow_id AS uuid), 0,
                      'implementer', 'test', 'READY', '["done"]'::jsonb, '[]'::jsonb,
                      CAST(:side_effect AS jsonb), CAST(:budget AS jsonb),
                      1, 'artifact://input'
                    )
                """),
                {
                    "task_id": task_id,
                    "tenant": self.tenant,
                    "workflow_id": item.workflow_id,
                    "side_effect": '{"mode":"NONE"}',
                    "budget": '{"tokens":100,"cost_usd":"0.1","duration_ms":1000}',
                },
            )
            await uow.commit()

        first_uow = PostgresUnitOfWork(self.factory, self.tenant)
        second_uow = PostgresUnitOfWork(self.factory, self.tenant)
        async with first_uow, second_uow:
            first = await PostgresTaskQueue(first_uow.session, self.tenant).claim(
                "worker-1", "sha256:token-1", 30
            )
            second = await PostgresTaskQueue(second_uow.session, self.tenant).claim(
                "worker-2", "sha256:token-2", 30
            )
            self.assertIsNotNone(first)
            self.assertIsNone(second)
            await first_uow.commit()
            await second_uow.commit()

        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            queue = PostgresTaskQueue(uow.session, self.tenant)
            with self.assertRaises(LeaseLost):
                await queue.accept_result(
                    task_id,
                    "worker-1",
                    "sha256:wrong-token",
                    succeeded=True,
                    output_ref="artifact://result",
                )


if __name__ == "__main__":
    unittest.main()
