from __future__ import annotations

import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.domain import BudgetAmount, RiskClass, Workflow
from orchestrator.governance.policy import PolicyDecision, PolicyEffect
from orchestrator.worker.service import WorkerService


class AllowPolicy:
    async def evaluate(self, value):
        return PolicyDecision(PolicyEffect.ALLOW, ("TEST",), "sha256:test")


class FakeRepo:
    def __init__(self, row):
        self.row = row
        self.persisted = []

    async def get(self, workflow_id):
        return self.row

    async def load_aggregate(self, workflow_id):
        return Workflow.create(
            workflow_id=self.row["workflow_id"],
            tenant_id=self.row["tenant_id"],
            workflow_type=self.row["workflow_type"],
            goal=self.row["goal"],
            risk=RiskClass(self.row["risk"]),
            requested_by=self.row["requested_by"],
            idempotency_key=self.row["idempotency_key"],
            budget_limit=BudgetAmount(30000, Decimal("2"), 300000),
            constraints=self.row["constraints"],
        )

    async def persist_event_stream(self, workflow, previous_version, events, trace_id):
        self.persisted.extend(events)


class FakeUow:
    def __init__(self, repo):
        self.workflows = repo
        self.session = object()
        self.committed = False

    async def __aenter__(self): return self
    async def __aexit__(self, *args): return None
    async def commit(self): self.committed = True
    async def rollback(self): pass


class FakeQueue:
    task = None
    accepted = None

    def __init__(self, session, tenant): pass

    async def claim(self, worker_id, token_hash, lease_seconds):
        task, FakeQueue.task = FakeQueue.task, None
        return task

    async def accept_result(self, task_id, worker_id, token_hash, **kwargs):
        FakeQueue.accepted = {"task_id": task_id, **kwargs}


class WorkerServiceTests(unittest.IsolatedAsyncioTestCase):
    async def test_worker_claims_executes_persists_and_accepts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            repo_root = base / "repo"
            artifacts = base / "artifacts"
            (repo_root / "src").mkdir(parents=True)
            (repo_root / "src/app.py").write_text("x = 1\n")
            row = {
                "workflow_id": "00000000-0000-7000-8000-000000000101",
                "tenant_id": "local-pilot",
                "workflow_type": "repository_adr",
                "goal": "Create ADR",
                "risk": "R1",
                "requested_by": "owner",
                "idempotency_key": "idem-worker",
                "constraints": {"skill_input": {"repository_files": ["src/app.py"], "artifact_path": "adr/a.md"}},
            }
            repository = FakeRepo(row)
            FakeQueue.task = {
                "task_id": "00000000-0000-7000-8000-000000000102",
                "workflow_id": row["workflow_id"],
            }
            FakeQueue.accepted = None
            worker = WorkerService(
                root=PROJECT,
                tenant_id="local-pilot",
                worker_id="worker-test",
                repository_root=repo_root,
                artifact_root=artifacts,
                uow_factory=lambda tenant: FakeUow(repository),
                policy=AllowPolicy(),
            )
            with patch("orchestrator.worker.service.PostgresTaskQueue", FakeQueue):
                self.assertTrue(await worker.run_once())
            self.assertTrue((artifacts / "adr/a.md").is_file())
            self.assertEqual(7, len(repository.persisted))
            self.assertTrue(FakeQueue.accepted["succeeded"])
            self.assertIn("sha256:", FakeQueue.accepted["output_ref"])

    async def test_worker_returns_false_when_queue_empty(self) -> None:
        repository = FakeRepo({})
        FakeQueue.task = None
        worker = WorkerService(
            root=PROJECT,
            tenant_id="local-pilot",
            worker_id="worker-test",
            repository_root=PROJECT,
            artifact_root=PROJECT / "build-test-artifacts",
            uow_factory=lambda tenant: FakeUow(repository),
            policy=AllowPolicy(),
        )
        with patch("orchestrator.worker.service.PostgresTaskQueue", FakeQueue):
            self.assertFalse(await worker.run_once())


if __name__ == "__main__":
    unittest.main()
