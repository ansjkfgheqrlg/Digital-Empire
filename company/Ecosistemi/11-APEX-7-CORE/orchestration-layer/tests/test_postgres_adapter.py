from __future__ import annotations

import asyncio
import importlib.util
import sys
import unittest
from decimal import Decimal
from pathlib import Path
from typing import Any

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.adapters.postgres.queue import LeaseLost, PostgresTaskQueue
from orchestrator.adapters.postgres.repositories import PostgresWorkflowRepository
from orchestrator.adapters.postgres.uow import PostgresUnitOfWork
from orchestrator.domain import ActorType, BudgetAmount, RiskClass, Workflow, WorkflowStatus
from orchestrator.domain.errors import StaleVersion
from orchestrator.domain.transitions import TransitionContext


class FakeMappings:
    def __init__(self, rows: list[dict]):
        self.rows = rows

    def one_or_none(self):
        return self.rows[0] if self.rows else None

    def all(self):
        return self.rows


class FakeResult:
    def __init__(self, scalar: Any = None, rows: list[dict] | None = None):
        self.scalar = scalar
        self.rows = rows or []

    def scalar_one_or_none(self):
        return self.scalar

    def scalar_one(self):
        if self.scalar is None:
            raise AssertionError("No scalar configured")
        return self.scalar

    def mappings(self):
        return FakeMappings(self.rows)


class FakeSession:
    def __init__(self, results: list[FakeResult] | None = None):
        self.results = list(results or [])
        self.calls: list[tuple[str, dict | None]] = []
        self.began = False
        self.committed = False
        self.rolled_back = False
        self.closed = False

    async def begin(self):
        self.began = True

    async def execute(self, statement, params=None):
        self.calls.append((str(statement), params))
        if self.results:
            return self.results.pop(0)
        return FakeResult()

    async def commit(self):
        self.committed = True

    async def rollback(self):
        self.rolled_back = True

    async def close(self):
        self.closed = True


class FakeFactory:
    def __init__(self, session: FakeSession):
        self.session = session

    def __call__(self):
        return self.session


def workflow() -> Workflow:
    return Workflow.create(
        workflow_id="018f4f62-7a6b-7d41-8ec8-8eb40f6bce31",
        tenant_id="tenant-a",
        workflow_type="repository_adr",
        goal="Create ADR",
        risk=RiskClass.R1,
        requested_by="user-a",
        idempotency_key="idem-0001",
        budget_limit=BudgetAmount(30000, Decimal("2.00"), 300000),
    )


class UnitOfWorkTests(unittest.IsolatedAsyncioTestCase):
    async def test_tenant_context_is_first_statement_and_commit_closes(self) -> None:
        session = FakeSession()
        uow = PostgresUnitOfWork(FakeFactory(session), "tenant-a")
        async with uow:
            self.assertTrue(session.began)
            self.assertIn("set_config('app.tenant_id'", session.calls[0][0])
            self.assertEqual("tenant-a", session.calls[0][1]["tenant_id"])
            await uow.commit()
        self.assertTrue(session.committed)
        self.assertFalse(session.rolled_back)
        self.assertTrue(session.closed)

    async def test_uncommitted_uow_rolls_back(self) -> None:
        session = FakeSession()
        async with PostgresUnitOfWork(FakeFactory(session), "tenant-a"):
            pass
        self.assertTrue(session.rolled_back)
        self.assertTrue(session.closed)


class RepositoryTests(unittest.IsolatedAsyncioTestCase):
    async def test_add_writes_workflow_audit_and_outbox(self) -> None:
        session = FakeSession([FakeResult(scalar="wf"), FakeResult(), FakeResult()])
        repo = PostgresWorkflowRepository(session, "tenant-a")
        await repo.add(workflow(), trace_id="trace-000000000001")
        sql = [call[0] for call in session.calls]
        self.assertIn("INSERT INTO workflows", sql[0])
        self.assertIn("INSERT INTO audit_events", sql[1])
        self.assertIn("INSERT INTO outbox_events", sql[2])
        self.assertEqual("tenant-a", session.calls[0][1]["tenant_id"])

    async def test_transition_rejects_stale_database_version(self) -> None:
        item = workflow()
        previous = item.version
        event = item.transition(
            WorkflowStatus.VALIDATING,
            ActorType.API,
            TransitionContext(flags=frozenset({"request_persisted"})),
            expected_version=previous,
        )
        session = FakeSession([FakeResult(scalar=None)])
        repo = PostgresWorkflowRepository(session, "tenant-a")
        with self.assertRaises(StaleVersion):
            await repo.persist_transition(item, previous, event, "trace-000000000001")
        self.assertIn("AND version = :previous_version", session.calls[0][0])

    async def test_repository_rejects_cross_tenant_object(self) -> None:
        session = FakeSession()
        repo = PostgresWorkflowRepository(session, "tenant-b")
        with self.assertRaises(ValueError):
            await repo.add(workflow(), trace_id="trace-000000000001")
        self.assertEqual([], session.calls)


class QueueTests(unittest.IsolatedAsyncioTestCase):
    async def test_claim_uses_skip_locked_and_returns_row(self) -> None:
        session = FakeSession([FakeResult(rows=[{"task_id": "task-1", "status": "LEASED"}])])
        queue = PostgresTaskQueue(session, "tenant-a")
        claimed = await queue.claim("worker-1", "sha256:token", 30)
        self.assertEqual("task-1", claimed["task_id"])
        self.assertIn("FOR UPDATE OF task SKIP LOCKED", session.calls[0][0])
        self.assertIn("tenant_id = :tenant_id", session.calls[0][0])

    async def test_stale_heartbeat_is_rejected(self) -> None:
        session = FakeSession([FakeResult(scalar=None)])
        queue = PostgresTaskQueue(session, "tenant-a")
        with self.assertRaises(LeaseLost):
            await queue.heartbeat("task-1", "worker-1", "old-token")

    async def test_stale_result_is_rejected(self) -> None:
        session = FakeSession([FakeResult(scalar=None)])
        queue = PostgresTaskQueue(session, "tenant-a")
        with self.assertRaises(LeaseLost):
            await queue.accept_result(
                "task-1", "worker-1", "old-token", succeeded=True, output_ref="artifact://x"
            )
        sql = session.calls[0][0]
        self.assertIn("execution_token_hash = :execution_token_hash", sql)
        self.assertIn("leased_until > now()", sql)


class MigrationStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sql = (PROJECT / "migrations" / "versions" / "0001_core.sql").read_text(
            encoding="utf-8"
        )

    def test_canonical_tables_exist(self) -> None:
        for table in (
            "workflows", "tasks", "task_runs", "approvals", "capability_grants",
            "gate_runs", "audit_events", "outbox_events", "memory_records",
        ):
            self.assertIn(f"CREATE TABLE {table}", self.sql)

    def test_rls_is_forced_for_all_tenant_tables(self) -> None:
        self.assertIn("ENABLE ROW LEVEL SECURITY", self.sql)
        self.assertIn("FORCE ROW LEVEL SECURITY", self.sql)
        self.assertIn("current_setting(''app.tenant_id'', true)", self.sql)

    def test_queue_and_outbox_indexes_exist(self) -> None:
        self.assertIn("ix_tasks_claim", self.sql)
        self.assertIn("ix_outbox_unpublished", self.sql)

    def test_migration_splitter_preserves_do_block(self) -> None:
        path = PROJECT / "migrations" / "versions" / "0001_core.py"
        spec = importlib.util.spec_from_file_location("migration_0001", path)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        statements = module._split_postgres_sql(self.sql)
        self.assertGreaterEqual(len(statements), 19)
        do_blocks = [statement for statement in statements if statement.lstrip().startswith("DO $$")]
        self.assertEqual(1, len(do_blocks))
        self.assertIn("FOREACH table_name", do_blocks[0])

    def test_down_migration_is_intentionally_blocked(self) -> None:
        migration = (PROJECT / "migrations" / "versions" / "0001_core.py").read_text(
            encoding="utf-8"
        )
        self.assertIn("Destructive down migration is intentionally unsupported", migration)


if __name__ == "__main__":
    unittest.main()
