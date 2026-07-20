"""Integration tests for repository governance tools."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillToolTests(unittest.TestCase):
    """Verify the executable governance controls."""

    def test_validator_returns_success(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_skill.py", "--root", "."],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 error(s), 0 warning(s)", result.stdout)

    def test_memory_manager_bootstraps_a_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/memory_manager.py"), "--init", "--target", str(target), "--vision", "test"],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue((target / "memory/MEMORY-INDEX.md").is_file())
            self.assertTrue(any((target / "memory/checkpoints").glob("CP-*.md")))

    def test_self_improvement_creates_a_plan(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/self_improve.py", "--root", "."],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((ROOT / "memory/self-improvement/PLAN-v1.md").is_file())


if __name__ == "__main__":
    unittest.main()

class QualityGateTests(unittest.TestCase):
    """Test enforcement beyond the happy-path repository state."""

    def test_at_least_twenty_five_complete_agents(self) -> None:
        complete = sum(
            len(list(directory.glob("*.md"))) >= 7
            for directory in (ROOT / "agents").glob("*/*")
            if directory.is_dir()
        )
        self.assertGreaterEqual(complete, 25)

    def test_credential_scanner_detects_a_token_like_value(self) -> None:
        import importlib.util
        import sys
        module_path = ROOT / "scripts/validate_skill.py"
        specification = importlib.util.spec_from_file_location("validate_skill_under_test", module_path)
        self.assertIsNotNone(specification)
        module = importlib.util.module_from_spec(specification)
        assert specification.loader is not None
        sys.modules[specification.name] = module
        specification.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temporary_directory:
            fixture = Path(temporary_directory) / "sample.md"
            fixture.write_text("token " + "gh" + "p_" + "abcdefghijklmnopqrstuvwxyz123456")
            findings = module.scan_credentials(Path(temporary_directory))
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].code, "SECRET-001")

class EvaluationRunnerTests(unittest.TestCase):
    """Verify that the structural acceptance suite is fully satisfied."""

    def test_structural_evaluations_score_five(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/run_evals.py"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("4/5", result.stdout)
        self.assertIn("5/5", result.stdout)

class GitHubConfigurationTests(unittest.TestCase):
    """Verify the committed GitHub Actions configuration is conservative and complete."""

    def test_ci_workflow_contains_required_quality_commands(self) -> None:
        workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        for required in (
            "actions/checkout@v4",
            "actions/setup-python@v5",
            "scripts/validate_skill.py --root .",
            "scripts/run_evals.py",
            "unittest discover -s tests -v",
        ):
            self.assertIn(required, workflow)
