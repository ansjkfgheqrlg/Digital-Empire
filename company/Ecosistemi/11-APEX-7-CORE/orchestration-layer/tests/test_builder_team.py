from __future__ import annotations

import json
import os
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
os.environ["PYTHONPATH"] = str(PROJECT / "src")

import sys
sys.path.insert(0, str(PROJECT / "src"))

from builder_team.models import RiskClass
from builder_team.registry import BuilderTeamRegistry
from builder_team.workflow import WorkItemPlanner


class BuilderTeamTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = BuilderTeamRegistry(PROJECT)

    def test_manifest_is_valid(self) -> None:
        evidence = self.registry.validate()
        self.assertIn("agents:8", evidence)
        self.assertIn("gates:3", evidence)

    def test_all_agents_forbid_self_approval(self) -> None:
        team = self.registry.load_team()
        for agent in team.agents:
            self.assertIn("approve_own_output", agent.denied)

    def test_gatekeeper_can_only_write_gate_artifacts(self) -> None:
        team = self.registry.load_team()
        gatekeeper = next(a for a in team.agents if a.agent_id == "GATEKEEPER")
        self.assertEqual(("builder_swarm/gates/**",), gatekeeper.writes)

    def test_work_item_dag_and_limits(self) -> None:
        item = WorkItemPlanner(PROJECT).create("WI-001", "Contracts", "R1")
        self.assertEqual(RiskClass.R1, item.risk)
        self.assertEqual(["architecture", "implementation", "release"], item.required_gates)
        self.assertEqual(8, len(item.stages))
        ready = [stage for stage in item.stages if stage["state"] == "READY"]
        self.assertEqual(["scope"], [stage["stage"] for stage in ready])
        self.assertTrue(all(stage["timeout_minutes"] <= 20 for stage in item.stages))

    def test_test_and_security_are_parallel_after_implementation(self) -> None:
        item = WorkItemPlanner(PROJECT).create("WI-002", "Core", "R1")
        stages = {stage["stage"]: stage for stage in item.stages}
        self.assertEqual(["implementation"], stages["testing"]["depends_on"])
        self.assertEqual(["implementation"], stages["security"]["depends_on"])
        self.assertEqual(
            ["testing", "security"], stages["gate-review"]["depends_on"]
        )

    def test_checkpoint_disables_ruflo_and_production_credentials(self) -> None:
        planner = WorkItemPlanner(PROJECT)
        checkpoint = planner.checkpoint(planner.create("WI-003", "Memory", "R0"))
        governance = checkpoint["governance"]
        self.assertFalse(governance["ruflo_execution_enabled"])
        self.assertFalse(governance["production_credentials_allowed"])
        self.assertEqual(3, governance["failed_gate_attempts_before_freeze"])


if __name__ == "__main__":
    unittest.main()
