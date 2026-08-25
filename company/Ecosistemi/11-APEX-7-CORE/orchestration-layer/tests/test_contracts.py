from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.contracts import ContractError, ContractRegistry


class ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = ContractRegistry(PROJECT)

    def load_fixture(self, category: str, name: str) -> dict:
        path = PROJECT / "contracts" / "fixtures" / category / name
        return json.loads(path.read_text(encoding="utf-8"))

    def test_all_schemas_are_valid_draft_2020_12(self) -> None:
        names = self.registry.names()
        self.assertEqual(10, len(names))
        for name in names:
            schema = self.registry.schema(name)
            self.assertEqual("https://json-schema.org/draft/2020-12/schema", schema["$schema"])

    def test_valid_workflow_command(self) -> None:
        self.registry.validate(
            "workflow-command", self.load_fixture("valid", "workflow-command.json")
        )

    def test_workflow_rejects_unknown_property(self) -> None:
        with self.assertRaises(ContractError):
            self.registry.validate(
                "workflow-command",
                self.load_fixture("invalid", "workflow-command-extra-field.json"),
            )

    def test_valid_plan_and_relative_contract(self) -> None:
        self.registry.validate("plan", self.load_fixture("valid", "plan.json"))

    def test_plan_rejects_unbounded_task(self) -> None:
        with self.assertRaises(ContractError):
            self.registry.validate(
                "plan", self.load_fixture("invalid", "plan-unbounded-task.json")
            )


if __name__ == "__main__":
    unittest.main()
