from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.governance.grants import CapabilityGrantService, GrantBinding, InMemoryCapabilityStore
from tool_gateway.gateway import ToolGateway, ToolGatewayError, ToolRequest
from tool_gateway.tools import ArtifactWriteTool, RepositoryReadTool


class ToolGatewayTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.artifacts = self.root / "artifacts"
        (self.repo / "src").mkdir(parents=True)
        (self.repo / "src" / "main.py").write_text("print('safe')\n", encoding="utf-8")
        self.service = CapabilityGrantService(InMemoryCapabilityStore())
        self.binding = GrantBinding("tenant-a", "workflow-a", "task-a", "sha256:exec")
        self.gateway = ToolGateway(self.service)
        self.gateway.register("repo.read", RepositoryReadTool(self.repo))
        self.gateway.register("artifact.write", ArtifactWriteTool(self.artifacts))

    async def asyncTearDown(self) -> None:
        self.temp.cleanup()

    async def grant(self, scope: str, constraints: dict):
        return await self.service.issue(
            subject="agent-a",
            binding=self.binding,
            capability_scope=scope,
            constraints=constraints,
            ttl_seconds=60,
        )

    async def test_read_scoped_file(self) -> None:
        token, _ = await self.grant("repo.read", {"path_prefix": "src/", "max_bytes": 1000})
        result = await self.gateway.execute(
            ToolRequest("repo.read", "repo.read", token, self.binding, {"path": "src/main.py"})
        )
        self.assertEqual("print('safe')\n", result["content"])

    async def test_path_traversal_is_denied_and_token_consumed(self) -> None:
        outside = self.root / "secret.txt"
        outside.write_text("secret", encoding="utf-8")
        token, _ = await self.grant("repo.read", {"path_prefix": "src/"})
        request = ToolRequest("repo.read", "repo.read", token, self.binding, {"path": "../secret.txt"})
        with self.assertRaises(ToolGatewayError):
            await self.gateway.execute(request)
        with self.assertRaises(ToolGatewayError):
            await self.gateway.execute(request)

    async def test_unknown_tool_does_not_execute(self) -> None:
        token, _ = await self.grant("repo.read", {})
        with self.assertRaises(ToolGatewayError):
            await self.gateway.execute(
                ToolRequest("shell.exec", "repo.read", token, self.binding, {})
            )

    async def test_artifact_write_is_immutable_and_idempotent(self) -> None:
        token, _ = await self.grant(
            "artifact.write:adr/**", {"path_prefix": "adr/", "max_bytes": 1000}
        )
        request = ToolRequest(
            "artifact.write",
            "artifact.write:adr/decision.md",
            token,
            self.binding,
            {"path": "adr/decision.md", "content": "# Decision\n"},
        )
        first = await self.gateway.execute(request)
        self.assertFalse(first["idempotent"])

        token2, _ = await self.grant(
            "artifact.write:adr/**", {"path_prefix": "adr/", "max_bytes": 1000}
        )
        second = await self.gateway.execute(
            ToolRequest(
                "artifact.write",
                "artifact.write:adr/decision.md",
                token2,
                self.binding,
                {"path": "adr/decision.md", "content": "# Decision\n"},
            )
        )
        self.assertTrue(second["idempotent"])

        token3, _ = await self.grant(
            "artifact.write:adr/**", {"path_prefix": "adr/", "max_bytes": 1000}
        )
        with self.assertRaises(ToolGatewayError):
            await self.gateway.execute(
                ToolRequest(
                    "artifact.write",
                    "artifact.write:adr/decision.md",
                    token3,
                    self.binding,
                    {"path": "adr/decision.md", "content": "changed"},
                )
            )

    async def test_artifact_scope_mismatch_is_denied(self) -> None:
        token, _ = await self.grant("artifact.write:adr/**", {"path_prefix": "adr/"})
        with self.assertRaises(ToolGatewayError):
            await self.gateway.execute(
                ToolRequest(
                    "artifact.write",
                    "artifact.write:src/main.py",
                    token,
                    self.binding,
                    {"path": "src/main.py", "content": "unsafe"},
                )
            )


if __name__ == "__main__":
    unittest.main()
