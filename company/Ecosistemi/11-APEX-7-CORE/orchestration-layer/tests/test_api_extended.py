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
    async def create(self, payload, auth, idempotency_key, trace_id):
        return {"workflow_id": "w1", "task_id": "t1", "status": "RECEIVED"}

    async def get(self, workflow_id):
        return {"workflow_id": workflow_id, "status": "RECEIVED"} if workflow_id == "w1" else None

    async def cancel(self, workflow_id, auth, trace_id):
        return {"workflow_id": workflow_id, "status": "CANCEL_REQUESTED"}

    async def events(self, workflow_id):
        return [{"sequence": 1, "event_type": "workflow.received"}]


class ApiExtendedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.private = Ed25519PrivateKey.generate()
        public = self.private.public_key().public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw
        )
        registry = OperatorRegistry()
        registry.register_raw_public_key("owner", public, {"LOCAL_OWNER", "TOKEN_ISSUER"})
        identity = OperatorIdentityService(registry)
        self.workflows = FakeWorkflowService()

        async def up():
            return ComponentHealth("test", "UP", required=True)

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

        ch = self.client.post("/v1/auth/challenges/owner").json()
        sig = self.private.sign(base64.b64decode(ch["message_b64"]))
        vr = self.client.post(
            "/v1/auth/verify",
            json={
                "challenge_id": ch["challenge_id"],
                "operator_id": "owner",
                "signature_b64": base64.b64encode(sig).decode(),
            },
        ).json()
        self.headers = {"Authorization": f"Bearer {vr['session_token']}"}

    def test_plan_memory_endpoints(self):
        res = self.client.get("/v1/plan-memory/manifest", headers=self.headers)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["levels_count"], 7)
        self.assertEqual(data["highest_approved_level"], "L7")

        q_res = self.client.get("/v1/plan-memory/query?q=stato canonico", headers=self.headers)
        self.assertEqual(q_res.status_code, 200)
        q_data = q_res.json()
        self.assertEqual(q_data["status"], "EVIDENCE_FOUND")
        self.assertGreaterEqual(len(q_data["results"]), 1)

    def test_status_endpoints(self):
        prr_res = self.client.get("/v1/status/prr", headers=self.headers)
        self.assertEqual(prr_res.status_code, 200)
        self.assertIn("verdict", prr_res.json())

        team_res = self.client.get("/v1/status/builder-team", headers=self.headers)
        self.assertEqual(team_res.status_code, 200)
        self.assertIn("agents", team_res.json())

        skills_res = self.client.get("/v1/status/skills", headers=self.headers)
        self.assertEqual(skills_res.status_code, 200)
        self.assertGreaterEqual(skills_res.json()["count"], 4)


if __name__ == "__main__":
    unittest.main()
