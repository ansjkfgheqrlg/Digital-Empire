from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from builder_team.executor import BuilderSwarmExecutor, LocalBuilderHandlers, StageResult
from builder_team.sandbox import BuilderSandbox, SandboxViolation
from builder_team.workflow import WorkItemPlanner


class FailingHandlers(LocalBuilderHandlers):
    async def testing(self, item, sandbox):
        return StageResult("testing", "TESTER", "FAIL", detail="injected failure")


class BuilderActivationTests(unittest.IsolatedAsyncioTestCase):
    async def test_happy_path_runs_specialized_team_in_sandbox(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            item = WorkItemPlanner(PROJECT).create("WI-ACT", "Capability report", "R1")
            executor = BuilderSwarmExecutor(
                PROJECT, LocalBuilderHandlers(PROJECT), sandbox_base=base
            )
            run = await executor.execute(item)
            self.assertEqual("READY_TO_MERGE", run.status)
            self.assertEqual(1, run.attempt)
            statuses = {result.stage: result.status for result in run.results}
            self.assertEqual("PASS", statuses["testing"])
            self.assertEqual("PASS", statuses["security"])
            self.assertEqual("PASS", statuses["gate-review"])
            self.assertEqual("PASS", statuses["release-candidate"])
            self.assertEqual("SKIPPED", statuses["ruflo-certification"])
            artifact = base / run.run_id / "reports/builder-team-capabilities.md"
            self.assertTrue(artifact.is_file())
            self.assertIn("GATEKEEPER", artifact.read_text(encoding="utf-8"))
            self.assertTrue(run.artifact_manifest)

    async def test_ruflo_work_item_freezes_without_execution_certification(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            item = WorkItemPlanner(PROJECT).create("WI-RUFLO", "Unsafe activation", "R2")
            run = await BuilderSwarmExecutor(
                PROJECT, LocalBuilderHandlers(PROJECT), Path(directory)
            ).execute(item, touches_ruflo=True)
            self.assertEqual("FROZEN", run.status)
            self.assertEqual("BLOCKED", run.results[-1].status)
            self.assertFalse(any(result.stage == "implementation" for result in run.results))

    async def test_third_gate_failure_freezes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            item = WorkItemPlanner(PROJECT).create("WI-FAIL", "Injected failure", "R1")
            run = await BuilderSwarmExecutor(
                PROJECT, FailingHandlers(PROJECT), Path(directory)
            ).execute(item)
            self.assertEqual("FROZEN", run.status)
            self.assertEqual(3, run.attempt)
            gate_results = [result for result in run.results if result.stage == "gate-review"]
            self.assertEqual(3, len(gate_results))
            self.assertTrue(all(result.status == "FAIL" for result in gate_results))

    async def test_every_executed_agent_evidence_has_prompt_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            item = WorkItemPlanner(PROJECT).create("WI-HASH", "Prompt evidence", "R1")
            run = await BuilderSwarmExecutor(
                PROJECT, LocalBuilderHandlers(PROJECT), Path(directory)
            ).execute(item)
            for result in run.results:
                if result.evidence:
                    self.assertRegex(result.evidence[0]["prompt_sha256"], r"^[a-f0-9]{64}$")


class SandboxTests(unittest.TestCase):
    def test_path_escape_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            sandbox = BuilderSandbox(Path(directory), "run-safe")
            with self.assertRaises(SandboxViolation):
                sandbox.write_immutable("../outside.txt", "bad")

    def test_conflicting_overwrite_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            sandbox = BuilderSandbox(Path(directory), "run-safe")
            sandbox.write_immutable("artifact.txt", "first")
            with self.assertRaises(SandboxViolation):
                sandbox.write_immutable("artifact.txt", "second")


if __name__ == "__main__":
    unittest.main()
