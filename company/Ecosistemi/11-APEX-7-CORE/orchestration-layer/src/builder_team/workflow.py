from __future__ import annotations

from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .models import RiskClass, WorkItem, WorkItemStatus
from .registry import BuilderTeamRegistry


class WorkItemPlanner:
    """Creates a governed build plan; it does not execute agent or tool calls."""

    STAGES: tuple[tuple[str, str, tuple[str, ...]], ...] = (
        ("scope", "BUILD-LEAD", ()),
        ("architecture", "ARCHITECT", ("scope",)),
        ("ruflo-certification", "RUFLO-SCOUT", ("architecture",)),
        ("implementation", "IMPLEMENTER", ("architecture",)),
        ("testing", "TESTER", ("implementation",)),
        ("security", "SECURITY", ("implementation",)),
        ("gate-review", "GATEKEEPER", ("testing", "security")),
        ("release-candidate", "RELEASE", ("gate-review",)),
    )

    def __init__(self, root: Path):
        self.root = root
        self.registry = BuilderTeamRegistry(root)

    def create(self, work_item_id: str, title: str, risk: str) -> WorkItem:
        team = self.registry.load_team()
        gates = self.registry.load_gates()
        parsed_risk = RiskClass(risk)
        item = WorkItem(work_item_id=work_item_id, title=title, risk=parsed_risk)
        item.required_gates = ["architecture", "implementation", "release"]
        item.stages = [
            {
                "stage": stage,
                "agent": agent,
                "depends_on": list(dependencies),
                "timeout_minutes": next(
                    a.timeout_minutes for a in team.agents if a.agent_id == agent
                ),
                "state": "BLOCKED" if dependencies else "READY",
            }
            for stage, agent, dependencies in self.STAGES
        ]
        if set(item.required_gates) - set(gates):
            raise ValueError("Work item references an unavailable gate")
        return item

    def checkpoint(self, item: WorkItem) -> dict[str, Any]:
        return {
            "checkpoint_version": "1.0",
            "created_at": datetime.now(UTC).isoformat(),
            "work_item": {
                **asdict(item),
                "risk": item.risk.value,
                "status": item.status.value,
            },
            "governance": {
                "author_cannot_approve": True,
                "failed_gate_attempts_before_freeze": 3,
                "production_credentials_allowed": False,
                "ruflo_execution_enabled": False,
            },
        }
