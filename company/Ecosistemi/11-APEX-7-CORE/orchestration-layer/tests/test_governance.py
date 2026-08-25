from __future__ import annotations

import sys
import unittest
from datetime import UTC, datetime, timedelta
from pathlib import Path

import httpx

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.governance.grants import (
    CapabilityGrantService,
    GrantBinding,
    GrantDenied,
    InMemoryCapabilityStore,
    scope_allows,
)
from orchestrator.governance.policy import OpaPolicyClient, PolicyEffect


class PolicyAdapterTests(unittest.IsolatedAsyncioTestCase):
    async def test_valid_allow_response(self) -> None:
        async def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                200,
                json={"result": {"effect": "ALLOW", "reasons": ["POL_LOW_RISK_ALLOWED"]}},
            )

        client = OpaPolicyClient(
            "http://opa.local:8181",
            "sha256:policy",
            transport=httpx.MockTransport(handler),
        )
        decision = await client.evaluate({"risk": "R1"})
        await client.close()
        self.assertTrue(decision.allowed)
        self.assertEqual(PolicyEffect.ALLOW, decision.effect)

    async def test_malformed_response_fails_closed(self) -> None:
        async def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(200, json={"unexpected": True})

        client = OpaPolicyClient(
            "http://opa.local:8181",
            "sha256:policy",
            transport=httpx.MockTransport(handler),
        )
        decision = await client.evaluate({"risk": "R1"})
        await client.close()
        self.assertEqual(PolicyEffect.DENY, decision.effect)
        self.assertIn("POL_OPA_UNAVAILABLE_OR_INVALID", decision.reasons)

    async def test_http_error_fails_closed(self) -> None:
        async def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(500, json={"error": "down"})

        client = OpaPolicyClient(
            "http://opa.local:8181",
            "sha256:policy",
            transport=httpx.MockTransport(handler),
        )
        decision = await client.evaluate({"risk": "R1"})
        await client.close()
        self.assertEqual(PolicyEffect.DENY, decision.effect)


class CapabilityGrantTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.store = InMemoryCapabilityStore()
        self.service = CapabilityGrantService(self.store)
        self.binding = GrantBinding(
            tenant_id="tenant-a",
            workflow_id="workflow-a",
            task_id="task-a",
            execution_token_hash="sha256:execution",
        )
        self.now = datetime(2026, 8, 23, tzinfo=UTC)

    async def issue(self, scope: str = "repo.read", ttl: int = 60):
        return await self.service.issue(
            subject="implementer-1",
            binding=self.binding,
            capability_scope=scope,
            constraints={"path_prefix": "src/", "max_bytes": 1000},
            ttl_seconds=ttl,
            now=self.now,
        )

    async def test_single_use_token(self) -> None:
        token, _ = await self.issue()
        record = await self.service.consume(token, self.binding, "repo.read", now=self.now)
        self.assertEqual("repo.read", record.capability_scope)
        with self.assertRaises(GrantDenied):
            await self.service.consume(token, self.binding, "repo.read", now=self.now)

    async def test_wrong_binding_is_denied(self) -> None:
        token, _ = await self.issue()
        wrong = GrantBinding("tenant-b", "workflow-a", "task-a", "sha256:execution")
        with self.assertRaises(GrantDenied):
            await self.service.consume(token, wrong, "repo.read", now=self.now)

    async def test_expired_token_is_denied(self) -> None:
        token, _ = await self.issue(ttl=1)
        with self.assertRaises(GrantDenied):
            await self.service.consume(
                token, self.binding, "repo.read", now=self.now + timedelta(seconds=1)
            )

    async def test_revoked_token_is_denied(self) -> None:
        token, _ = await self.issue()
        self.assertEqual(1, await self.service.revoke_task("tenant-a", "task-a"))
        with self.assertRaises(GrantDenied):
            await self.service.consume(token, self.binding, "repo.read", now=self.now)

    async def test_scope_wildcard(self) -> None:
        self.assertTrue(scope_allows("artifact.write:adr/**", "artifact.write:adr/decision.md"))
        self.assertFalse(scope_allows("artifact.write:adr/**", "artifact.write:src/main.py"))

    async def test_invalid_ttl_is_denied(self) -> None:
        with self.assertRaises(GrantDenied):
            await self.issue(ttl=301)


if __name__ == "__main__":
    unittest.main()
