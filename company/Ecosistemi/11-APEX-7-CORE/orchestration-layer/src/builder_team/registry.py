from __future__ import annotations

import json
from pathlib import Path

from .models import AgentSpec, GateCriterion, GateSpec, ManifestError, TeamConfig


class BuilderTeamRegistry:
    """Loads and validates the Builder Swarm's immutable configuration."""

    REQUIRED_AGENTS = {
        "BUILD-LEAD",
        "ARCHITECT",
        "RUFLO-SCOUT",
        "IMPLEMENTER",
        "TESTER",
        "SECURITY",
        "GATEKEEPER",
        "RELEASE",
    }

    def __init__(self, root: Path):
        self.root = root
        self.swarm_dir = root / "builder_swarm"

    @staticmethod
    def _load_json_yaml(path: Path) -> dict:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise ManifestError(f"Missing manifest: {path}") from exc
        except json.JSONDecodeError as exc:
            raise ManifestError(f"Invalid JSON-subset YAML in {path}: {exc}") from exc

    def load_team(self) -> TeamConfig:
        raw = self._load_json_yaml(self.swarm_dir / "agents.yaml")
        governance = raw.get("governance", {})
        agents = tuple(
            AgentSpec(
                agent_id=item["id"],
                role=item["role"],
                responsibility=item["responsibility"],
                produces=tuple(item.get("produces", [])),
                reads=tuple(item.get("reads", [])),
                writes=tuple(item.get("writes", [])),
                denied=tuple(item.get("denied", [])),
                timeout_minutes=int(item["limits"]["timeout_minutes"]),
                max_retries=int(item["limits"]["max_retries"]),
                prompt_file=item["prompt_file"],
                can_approve=tuple(item.get("can_approve", [])),
            )
            for item in raw.get("agents", [])
        )
        team = TeamConfig(
            team_id=raw["team"]["id"],
            version=raw["team"]["version"],
            max_wip=int(governance["max_wip"]),
            max_concurrency=int(governance["max_concurrency"]),
            agents=agents,
        )
        self._validate_team(team)
        return team

    def load_gates(self) -> dict[str, GateSpec]:
        result: dict[str, GateSpec] = {}
        for path in sorted((self.swarm_dir / "gates").glob("*.yaml")):
            raw = self._load_json_yaml(path)
            gate = GateSpec(
                gate_id=raw["gate_id"],
                owner_agent=raw["owner_agent"],
                maximum_attempts=int(raw["maximum_attempts"]),
                criteria=tuple(
                    GateCriterion(
                        criterion_id=item["id"],
                        description=item["description"],
                        blocking=bool(item["blocking"]),
                        evidence_required=tuple(item.get("evidence_required", [])),
                    )
                    for item in raw["criteria"]
                ),
            )
            if gate.gate_id in result:
                raise ManifestError(f"Duplicate gate id: {gate.gate_id}")
            result[gate.gate_id] = gate
        if not result:
            raise ManifestError("No gates configured")
        return result

    def validate(self) -> list[str]:
        team = self.load_team()
        gates = self.load_gates()
        workflow = self._load_json_yaml(self.swarm_dir / "workflow.yaml")
        agent_ids = {agent.agent_id for agent in team.agents}

        for gate in gates.values():
            if gate.owner_agent not in agent_ids:
                raise ManifestError(
                    f"Gate {gate.gate_id} has unknown owner {gate.owner_agent}"
                )
            if gate.maximum_attempts != 3:
                raise ManifestError(
                    f"Gate {gate.gate_id} must freeze on the third failed attempt"
                )
            if not gate.criteria or not any(c.blocking for c in gate.criteria):
                raise ManifestError(f"Gate {gate.gate_id} has no blocking criterion")

        referenced_gates = set(workflow.get("required_gates", []))
        unknown = referenced_gates - set(gates)
        if unknown:
            raise ManifestError(f"Workflow references unknown gates: {sorted(unknown)}")

        return [
            f"team:{team.team_id}@{team.version}",
            f"agents:{len(team.agents)}",
            f"gates:{len(gates)}",
            f"max_wip:{team.max_wip}",
            f"max_concurrency:{team.max_concurrency}",
        ]

    def _validate_team(self, team: TeamConfig) -> None:
        ids = [agent.agent_id for agent in team.agents]
        if len(ids) != len(set(ids)):
            raise ManifestError("Agent ids must be unique")
        missing = self.REQUIRED_AGENTS - set(ids)
        if missing:
            raise ManifestError(f"Required agents missing: {sorted(missing)}")
        if team.max_wip != 3 or team.max_concurrency != 4:
            raise ManifestError("Governance requires max_wip=3 and max_concurrency=4")

        for agent in team.agents:
            if not agent.responsibility.strip():
                raise ManifestError(f"{agent.agent_id} needs one explicit responsibility")
            if not 1 <= agent.timeout_minutes <= 20:
                raise ManifestError(f"{agent.agent_id} timeout must be 1..20 minutes")
            if agent.max_retries not in (0, 1):
                raise ManifestError(f"{agent.agent_id} max_retries must be 0 or 1")
            prompt_path = self.swarm_dir / agent.prompt_file
            if not prompt_path.is_file():
                raise ManifestError(f"Missing prompt for {agent.agent_id}: {prompt_path}")
            if "approve_own_output" not in agent.denied:
                raise ManifestError(
                    f"{agent.agent_id} must explicitly deny approving its own output"
                )

        gatekeeper = next(a for a in team.agents if a.agent_id == "GATEKEEPER")
        if any(path != "builder_swarm/gates/**" for path in gatekeeper.writes):
            raise ManifestError("GATEKEEPER may write only gate artifacts")
