from __future__ import annotations

import base64
import sys
import unittest
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from fastapi.testclient import TestClient

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.api.app import ApiContext, create_app
from orchestrator.identity import OperatorIdentityService, OperatorRegistry, SessionService
from orchestrator.observability import ComponentHealth, HealthService, OcpMetrics


class FakeWorkflowService:
    def __init__(self):
        self.created = []

    async def create(self, payload, auth, idempotency_key, trace_id):
        self.created.append((payload, auth, idempotency_key, trace_id))
        return {"workflow_id": "w1", "task_id": "t1", "status": "RECEIVED"}

    async def get(self, workflow_id):
        return {"workflow_id": workflow_id, "status": "RECEIVED"} if workflow_id == "w1" else None

    async def cancel(self, workflow_id, auth, trace_id):
        if workflow_id != "w1": raise KeyError(workflow_id)
        return {"workflow_id": workflow_id, "status": "CANCEL_REQUESTED"}

    async def events(self, workflow_id):
        return [{"sequence": 1, "event_type": "workflow.received"}]


class ApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.private = Ed25519PrivateKey.generate()
        public = self.private.public_key().public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw
        )
        registry = OperatorRegistry()
        registry.register_raw_public_key("owner", public, {"LOCAL_OWNER", "TOKEN_ISSUER"})
        identity = OperatorIdentityService(registry)
        self.workflows = FakeWorkflowService()

        async def up(): return ComponentHealth("test", "UP", required=True)

        self.client = TestClient(
            create_app(
                ApiContext(
                    identity,
                    SessionService(),
                    self.workflows,
                    HealthService([up]),
                    OcpMetrics(),
                )
            )
        )

    def authenticate(self) -> str:
        challenge = self.client.post("/v1/auth/challenges/owner")
        self.assertEqual(200, challenge.status_code)
        body = challenge.json()
        signature = self.private.sign(base64.b64decode(body["message_b64"]))
        verified = self.client.post(
            "/v1/auth/verify",
            json={
                "challenge_id": body["challenge_id"],
                "operator_id": "owner",
                "signature_b64": base64.b64encode(signature).decode(),
            },
        )
        self.assertEqual(200, verified.status_code)
        return verified.json()["session_token"]

    def test_read_only_dashboard_is_visible(self) -> None:
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertIn("Local Secure Pilot", response.text)
        self.assertIn("Anonymous actions rejected", response.text)

    def test_anonymous_workflow_access_is_rejected(self) -> None:
        self.assertEqual(401, self.client.get("/v1/workflows/w1").status_code)

    def test_signed_operator_creates_and_queries_workflow(self) -> None:
        token = self.authenticate()
        headers = {"Authorization": f"Bearer {token}", "Idempotency-Key": "request-0001"}
        created = self.client.post(
            "/v1/workflows",
            headers=headers,
            json={
                "workflow_type": "repository_adr",
                "goal": "Create ADR",
                "risk_hint": "R1",
                "constraints": {"max_tasks": 5, "deadline_seconds": 300, "max_tokens": 30000, "max_cost_usd": 2},
                "skill_input": {"repository_files": ["src/app.py"], "artifact_path": "adr/0001.md"},
            },
        )
        self.assertEqual(202, created.status_code, created.text)
        self.assertEqual("request-0001", self.workflows.created[0][2])
        self.assertEqual(200, self.client.get("/v1/workflows/w1", headers=headers).status_code)
        self.assertEqual(202, self.client.post("/v1/workflows/w1/cancel", headers=headers).status_code)
        self.assertEqual(200, self.client.get("/v1/workflows/w1/events", headers=headers).status_code)

    def test_r2_and_approval_are_disabled(self) -> None:
        token = self.authenticate()
        headers = {"Authorization": f"Bearer {token}", "Idempotency-Key": "request-0002"}
        response = self.client.post(
            "/v1/workflows",
            headers=headers,
            json={
                "workflow_type": "repository_adr", "goal": "Unsafe", "risk_hint": "R2",
                "skill_input": {"repository_files": ["src/app.py"], "artifact_path": "adr/a.md"},
            },
        )
        self.assertEqual(422, response.status_code)
        self.assertEqual(403, self.client.post("/v1/workflows/w1/approve", headers=headers).status_code)

    def test_challenge_replay_is_rejected(self) -> None:
        challenge = self.client.post("/v1/auth/challenges/owner").json()
        signature = base64.b64encode(
            self.private.sign(base64.b64decode(challenge["message_b64"]))
        ).decode()
        payload = {"challenge_id": challenge["challenge_id"], "operator_id": "owner", "signature_b64": signature}
        self.assertEqual(200, self.client.post("/v1/auth/verify", json=payload).status_code)
        self.assertEqual(401, self.client.post("/v1/auth/verify", json=payload).status_code)

    def test_health_and_metrics(self) -> None:
        self.assertEqual(200, self.client.get("/health/live").status_code)
        self.assertEqual(200, self.client.get("/health/ready").status_code)
        token = self.authenticate()
        response = self.client.get("/metrics", headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(200, response.status_code)
        self.assertIn("text/plain", response.headers["content-type"])


if __name__ == "__main__":
    unittest.main()
