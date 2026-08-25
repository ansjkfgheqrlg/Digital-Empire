from __future__ import annotations

import os
import subprocess
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
OPA_BIN = os.environ.get("OPA_BIN")


@unittest.skipUnless(OPA_BIN, "OPA_BIN is not configured")
class OpaPolicyTests(unittest.TestCase):
    def test_policy_format_strict_check_and_tests(self) -> None:
        commands = [
            [OPA_BIN, "fmt", "--fail", "policies/"],
            [OPA_BIN, "check", "--strict", "policies/"],
            [OPA_BIN, "test", "policies/", "-v"],
        ]
        for command in commands:
            result = subprocess.run(
                command,
                cwd=PROJECT,
                text=True,
                capture_output=True,
                timeout=30,
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
