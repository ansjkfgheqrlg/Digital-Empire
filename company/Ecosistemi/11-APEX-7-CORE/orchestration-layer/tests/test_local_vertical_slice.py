from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.application.local_vertical_slice import (
    RepositoryAdrVerticalSlice,
    VerticalSliceError,
)
from orchestrator.governance.grants import CapabilityGrantService, InMemoryCapabilityStore
from orchestrator.governance.policy import PolicyDecision, PolicyEffect
from orchestrator.quality import QualityPipeline, compress_verified_output
from orchestrator.runtime import LocalAgentRuntime, TaskAssignment


class AllowPolicy:
    async def evaluate(self, policy_input):
        return PolicyDecision(PolicyEffect.ALLOW, ("TEST_ALLOW",), "sha256:test")


class DenyPolicy:
    async def evaluate(self, policy_input):
        return PolicyDecision(PolicyEffect.DENY, ("TEST_DENY",), "sha256:test")


class LocalVerticalSliceTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.repo = self.base / "repo"
        self.artifacts = self.base / "artifacts"
        (self.repo / "src").mkdir(parents=True)
        (self.repo / "src" / "app.py").write_text(
            "def hello() -> str:\n    return 'hello'\n", encoding="utf-8"
        )
        (self.repo / "README.md").write_text("# Fixture\n", encoding="utf-8")

    async def asyncTearDown(self) -> None:
        self.temp.cleanup()

    def runner(self, policy=None):
        return RepositoryAdrVerticalSlice(
            root=PROJECT,
            repository_root=self.repo,
            artifact_root=self.artifacts,
            policy=policy or AllowPolicy(),
            grants=CapabilityGrantService(InMemoryCapabilityStore()),
        )

    async def test_complete_r1_vertical_slice(self) -> None:
        result = await self.runner().run(
            tenant_id="tenant-test",
            requested_by="tester",
            repository_files=["src/app.py", "README.md"],
            artifact_path="adr/0001-repository.md",
        )
        self.assertEqual("COMPLETED", result.status)
        self.assertEqual("PASS", result.gate_verdict)
        self.assertTrue(all(result.quality.values()))
        artifact = self.artifacts / result.artifact_path
        self.assertTrue(artifact.is_file())
        text = artifact.read_text(encoding="utf-8")
        self.assertIn("src/app.py", text)
        self.assertIn("## Evidence", text)
        self.assertIn(f"sha256:{result.artifact_sha256}", result.final_response)
        self.assertFalse(result.ruflo_enabled)

    async def test_input_path_traversal_rejected_before_execution(self) -> None:
        with self.assertRaises(VerticalSliceError):
            await self.runner().run(
                tenant_id="tenant-test",
                requested_by="tester",
                repository_files=["../secret"],
                artifact_path="adr/0001.md",
            )
        self.assertEqual([], list(self.artifacts.rglob("*")))

    async def test_policy_deny_produces_no_artifact(self) -> None:
        with self.assertRaises(VerticalSliceError):
            await self.runner(DenyPolicy()).run(
                tenant_id="tenant-test",
                requested_by="tester",
                repository_files=["src/app.py"],
                artifact_path="adr/0001.md",
            )
        self.assertFalse((self.artifacts / "adr/0001.md").exists())

    async def test_unknown_runtime_role_fails_explicitly(self) -> None:
        result = await LocalAgentRuntime().execute(
            TaskAssignment("w", "t", "unknown", "x", (), {}, 1, 1, 0, "none")
        )
        self.assertEqual("FAILED", result.status)
        self.assertEqual("RUN_ROLE_UNAVAILABLE", result.failure["code"])


class QualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(
            (PROJECT / "skills/repository-adr/schemas/output.json").read_text(encoding="utf-8")
        )

    def test_evidence_hash_mismatch_fails(self) -> None:
        output = {
            "adr": "# ADR\n\n## Status\nX\n## Context\nX\n## Decision\nX\n## Consequences\nX\n## Evidence\n`a.py` sha256:bad\n",
            "evidence": [{"path": "a.py", "sha256": "0" * 64}],
        }
        known = {"a.py": {"sha256": "1" * 64, "content": "x"}}
        report = QualityPipeline(self.schema).evaluate(output, known)
        self.assertFalse(report.evidence_pass)
        self.assertFalse(report.passed)

    def test_secret_pattern_fails(self) -> None:
        output = {
            "adr": "# ADR\n\n## Status\nX\n## Context\npassword=supersecretvalue\n## Decision\nX\n## Consequences\nX\n## Evidence\n`a.py` sha256:" + "1" * 64,
            "evidence": [{"path": "a.py", "sha256": "1" * 64}],
        }
        known = {"a.py": {"sha256": "1" * 64, "content": "x"}}
        self.assertFalse(QualityPipeline(self.schema).evaluate(output, known).security_pass)

    def test_nerve_save_preserves_numbers_negation_and_code(self) -> None:
        source = "È importante sottolineare che non usare `rm -rf /`. Limite 30%."
        result = compress_verified_output(source)
        self.assertTrue(result.preservation_pass)
        self.assertIn("non", result.text)
        self.assertIn("`rm -rf /`", result.text)
        self.assertIn("30%", result.text)
        self.assertLess(result.final_length, result.original_length)


if __name__ == "__main__":
    unittest.main()
