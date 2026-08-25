from __future__ import annotations

import base64
import hashlib
import os
import sys
import tempfile
import unittest
from pathlib import Path
from uuid import uuid4

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from fastapi.testclient import TestClient
from sqlalchemy import text

PROJECT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.adapters.postgres.uow import PostgresUnitOfWork, create_engine_and_factory
from orchestrator.api.app import ApiContext, create_app
from orchestrator.application.workflow_service import WorkflowService
from orchestrator.governance.policy import OpaPolicyClient
from orchestrator.identity import OperatorIdentityService, OperatorRegistry, SessionService
from orchestrator.observability import ComponentHealth, HealthService, OcpMetrics
from orchestrator.worker.service import OutboxPublisherService, WorkerService


DATABASE_URL = os.environ.get("OCP_W13_DATABASE_URL")
OPA_URL = os.environ.get("OCP_OPA_URL")


@unittest.skipUnless(DATABASE_URL and OPA_URL, "W13 database and OPA are not configured")
class ApiWorkerRealTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.engine, self.factory = create_engine_and_factory(DATABASE_URL, null_pool=True)
        self.tenant = f"w13-{uuid4().hex[:12]}"
        self.private = Ed25519PrivateKey.generate()
        public = self.private.public_key().public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw
        )
        registry = OperatorRegistry()
        registry.register_raw_public_key("owner", public, {"LOCAL_OWNER", "TOKEN_ISSUER"})
        identity = OperatorIdentityService(registry)

        async def up(): return ComponentHealth("integration", "UP", required=True)

        service = WorkflowService(
            lambda tenant: PostgresUnitOfWork(self.factory, tenant), self.tenant
        )
        self.client = TestClient(
            create_app(
                ApiContext(identity, SessionService(), service, HealthService([up]), OcpMetrics())
            )
        )
        policy_hash = "sha256:" + hashlib.sha256(
            (PROJECT / "policies/authorization.rego").read_bytes()
        ).hexdigest()
        self.policy = OpaPolicyClient(OPA_URL, policy_hash)
        self.temp = tempfile.TemporaryDirectory()
        self.artifacts = Path(self.temp.name) / "artifacts"

    async def asyncTearDown(self) -> None:
        await self.policy.close()
        await self.engine.dispose()
        self.temp.cleanup()

    def auth_token(self) -> str:
        challenge = self.client.post("/v1/auth/challenges/owner").json()
        signature = self.private.sign(base64.b64decode(challenge["message_b64"]))
        response = self.client.post(
            "/v1/auth/verify",
            json={
                "challenge_id": challenge["challenge_id"],
                "operator_id": "owner",
                "signature_b64": base64.b64encode(signature).decode(),
            },
        )
        return response.json()["session_token"]

    async def test_cancelled_workflow_is_not_claimed(self) -> None:
        token = self.auth_token()
        headers = {"Authorization": f"Bearer {token}", "Idempotency-Key": "w13-cancel-0001"}
        payload = {
            "workflow_type": "repository_adr",
            "goal": "Cancel before execution",
            "risk_hint": "R1",
            "skill_input": {"repository_files": ["src/app.py"], "artifact_path": "adr/cancelled.md"},
        }
        created = self.client.post("/v1/workflows", headers=headers, json=payload).json()
        cancelled = self.client.post(
            f"/v1/workflows/{created['workflow_id']}/cancel", headers=headers
        )
        self.assertEqual(202, cancelled.status_code)
        worker = WorkerService(
            root=PROJECT,
            tenant_id=self.tenant,
            worker_id="w13-cancel-worker",
            repository_root=PROJECT / "tests/fixtures/repository-01",
            artifact_root=self.artifacts,
            uow_factory=lambda tenant: PostgresUnitOfWork(self.factory, tenant),
            policy=self.policy,
        )
        self.assertFalse(await worker.run_once())
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            status = (
                await uow.session.execute(
                    text("SELECT status FROM tasks WHERE tenant_id=:tenant"),
                    {"tenant": self.tenant},
                )
            ).scalar_one()
            await uow.commit()
        self.assertEqual("CANCELLED", status)

    async def test_api_to_durable_worker_to_completed_audit(self) -> None:
        token = self.auth_token()
        headers = {"Authorization": f"Bearer {token}", "Idempotency-Key": "w13-request-0001"}
        payload = {
            "workflow_type": "repository_adr",
            "goal": "Create persistent ADR",
            "risk_hint": "R1",
            "constraints": {"max_tasks": 5, "deadline_seconds": 300, "max_tokens": 30000, "max_cost_usd": 2},
            "skill_input": {"repository_files": ["src/app.py", "README.md"], "artifact_path": "adr/w13.md"},
        }
        created = self.client.post("/v1/workflows", headers=headers, json=payload)
        self.assertEqual(202, created.status_code, created.text)
        workflow_id = created.json()["workflow_id"]

        replay = self.client.post("/v1/workflows", headers=headers, json=payload)
        self.assertEqual(202, replay.status_code)
        self.assertEqual(workflow_id, replay.json()["workflow_id"])
        self.assertTrue(replay.json()["idempotent_replay"])

        worker = WorkerService(
            root=PROJECT,
            tenant_id=self.tenant,
            worker_id="w13-worker",
            repository_root=PROJECT / "tests/fixtures/repository-01",
            artifact_root=self.artifacts,
            uow_factory=lambda tenant: PostgresUnitOfWork(self.factory, tenant),
            policy=self.policy,
        )
        self.assertTrue(await worker.run_once())
        self.assertTrue((self.artifacts / "adr/w13.md").is_file())

        state = self.client.get(f"/v1/workflows/{workflow_id}", headers=headers)
        self.assertEqual("COMPLETED", state.json()["status"])
        events = self.client.get(f"/v1/workflows/{workflow_id}/events", headers=headers).json()
        self.assertEqual(8, len(events))
        self.assertEqual(list(range(1, 9)), [event["sequence"] for event in events])

        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            task_count = (
                await uow.session.execute(
                    text("SELECT count(*) FROM tasks WHERE tenant_id=:tenant"),
                    {"tenant": self.tenant},
                )
            ).scalar_one()
            outbox_count = (
                await uow.session.execute(
                    text("SELECT count(*) FROM outbox_events WHERE tenant_id=:tenant"),
                    {"tenant": self.tenant},
                )
            ).scalar_one()
            await uow.commit()
        self.assertEqual(1, task_count)
        self.assertEqual(8, outbox_count)

        delivered = []
        async def sink(event):
            delivered.append(event)
        publisher = OutboxPublisherService(
            lambda tenant: PostgresUnitOfWork(self.factory, tenant), self.tenant, sink
        )
        self.assertEqual(8, await publisher.publish_once())
        self.assertEqual(8, len(delivered))
        async with PostgresUnitOfWork(self.factory, self.tenant) as uow:
            unpublished = (
                await uow.session.execute(
                    text("SELECT count(*) FROM outbox_events WHERE tenant_id=:tenant AND published_at IS NULL"),
                    {"tenant": self.tenant},
                )
            ).scalar_one()
            await uow.commit()
        self.assertEqual(0, unpublished)


if __name__ == "__main__":
    unittest.main()
