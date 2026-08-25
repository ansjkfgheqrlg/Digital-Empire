from __future__ import annotations

import asyncio
import hashlib
import json
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Protocol
from uuid import uuid4

from .models import WorkItem, WorkItemStatus
from .registry import BuilderTeamRegistry
from .sandbox import BuilderSandbox


@dataclass(frozen=True)
class StageResult:
    stage: str
    agent: str
    status: str
    evidence: tuple[dict[str, Any], ...] = ()
    detail: str = ""


@dataclass
class BuilderRun:
    run_id: str
    work_item_id: str
    status: str = "RUNNING"
    attempt: int = 1
    results: list[StageResult] = field(default_factory=list)
    artifact_manifest: dict[str, Any] | None = None


class BuilderHandlers(Protocol):
    async def scope(self, item: WorkItem, sandbox: BuilderSandbox) -> StageResult: ...
    async def architecture(self, item: WorkItem, sandbox: BuilderSandbox) -> StageResult: ...
    async def implementation(self, item: WorkItem, sandbox: BuilderSandbox) -> StageResult: ...
    async def testing(self, item: WorkItem, sandbox: BuilderSandbox) -> StageResult: ...
    async def security(self, item: WorkItem, sandbox: BuilderSandbox) -> StageResult: ...
    async def gate(self, item: WorkItem, sandbox: BuilderSandbox, evidence: list[StageResult], attempt: int) -> StageResult: ...
    async def release(self, item: WorkItem, sandbox: BuilderSandbox, evidence: list[StageResult]) -> StageResult: ...


class LocalBuilderHandlers:
    """Deterministic activation handler for one harmless capability report."""

    def __init__(self, root: Path):
        self.root = root
        self.registry = BuilderTeamRegistry(root)

    def prompt_hash(self, agent_id: str) -> str:
        agent = next(agent for agent in self.registry.load_team().agents if agent.agent_id == agent_id)
        data = (self.root / "builder_swarm" / agent.prompt_file).read_bytes()
        return hashlib.sha256(data).hexdigest()

    async def scope(self, item, sandbox):
        evidence = sandbox.write_immutable(
            "evidence/scope.json",
            json.dumps({"work_item": item.work_item_id, "title": item.title, "risk": item.risk.value, "non_scope": ["production", "external tools", "RuFlo execution"]}, indent=2),
        )
        return self._result("scope", "BUILD-LEAD", evidence)

    async def architecture(self, item, sandbox):
        team = self.registry.load_team()
        evidence = sandbox.write_immutable(
            "evidence/architecture.json",
            json.dumps({"artifact": "reports/builder-team-capabilities.md", "agents": len(team.agents), "max_wip": team.max_wip, "max_concurrency": team.max_concurrency, "writes_outside_sandbox": False}, indent=2),
        )
        return self._result("architecture", "ARCHITECT", evidence)

    async def implementation(self, item, sandbox):
        team = self.registry.load_team()
        lines = ["# Builder Team Capability Report", "", f"Work item: `{item.work_item_id}`", "", "| Agent | Role | Responsibility |", "|---|---|---|"]
        for agent in team.agents:
            lines.append(f"| {agent.agent_id} | {agent.role} | {agent.responsibility} |")
        lines.extend(["", f"WIP limit: {team.max_wip}. Concurrency limit: {team.max_concurrency}.", "", "RuFlo execution: disabled. Production credentials: forbidden."])
        evidence = sandbox.write_immutable("reports/builder-team-capabilities.md", "\n".join(lines) + "\n")
        return self._result("implementation", "IMPLEMENTER", evidence)

    async def testing(self, item, sandbox):
        report = sandbox.path("reports/builder-team-capabilities.md").read_text(encoding="utf-8")
        team = self.registry.load_team()
        missing = [agent.agent_id for agent in team.agents if agent.agent_id not in report]
        status = "PASS" if not missing and "RuFlo execution: disabled" in report else "FAIL"
        evidence = sandbox.write_immutable("evidence/test.json", json.dumps({"status": status, "missing_agents": missing}, indent=2))
        return self._result("testing", "TESTER", evidence, status)

    async def security(self, item, sandbox):
        report = sandbox.path("reports/builder-team-capabilities.md").read_text(encoding="utf-8")
        forbidden_markers = ("BEGIN PRIVATE KEY", "Bearer ", "password" + "=")
        forbidden = [value for value in forbidden_markers if value in report]
        status = "PASS" if not forbidden else "FAIL"
        evidence = sandbox.write_immutable("evidence/security.json", json.dumps({"status": status, "forbidden_patterns": forbidden, "outside_sandbox_writes": False}, indent=2))
        return self._result("security", "SECURITY", evidence, status)

    async def gate(self, item, sandbox, evidence, attempt):
        failures = [result.stage for result in evidence if result.status != "PASS"]
        status = "PASS" if not failures else "FAIL"
        record = sandbox.write_immutable(f"evidence/gate-attempt-{attempt}.json", json.dumps({"status": status, "attempt": attempt, "failures": failures, "artifact_hash": self._file_hash(sandbox.path("reports/builder-team-capabilities.md"))}, indent=2))
        return self._result("gate-review", "GATEKEEPER", record, status)

    async def release(self, item, sandbox, evidence):
        artifact = sandbox.path("reports/builder-team-capabilities.md")
        pack = {
            "work_item": item.work_item_id,
            "artifact": {"path": "reports/builder-team-capabilities.md", "sha256": self._file_hash(artifact)},
            "stages": [{"stage": result.stage, "agent": result.agent, "status": result.status} for result in evidence],
            "promotion": "SANDBOX_ONLY",
            "production_deployment": False,
        }
        record = sandbox.write_immutable("release/evidence-pack.json", json.dumps(pack, indent=2))
        return self._result("release-candidate", "RELEASE", record)

    def _result(self, stage: str, agent: str, evidence: dict, status: str = "PASS") -> StageResult:
        return StageResult(stage, agent, status, ({**evidence, "prompt_sha256": self.prompt_hash(agent)},))

    @staticmethod
    def _file_hash(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()


class BuilderSwarmExecutor:
    def __init__(self, root: Path, handlers: BuilderHandlers, sandbox_base: Path | None = None):
        self.root = root
        self.handlers = handlers
        self.registry = BuilderTeamRegistry(root)
        self.sandbox_base = sandbox_base or root / "builder_swarm" / "sandboxes"

    async def execute(self, item: WorkItem, *, touches_ruflo: bool = False) -> BuilderRun:
        self.registry.validate()
        run = BuilderRun(run_id=f"run-{uuid4().hex[:12]}", work_item_id=item.work_item_id)
        sandbox = BuilderSandbox(self.sandbox_base, run.run_id)
        run.results.append(await self.handlers.scope(item, sandbox))
        run.results.append(await self.handlers.architecture(item, sandbox))
        if touches_ruflo:
            run.results.append(StageResult("ruflo-certification", "RUFLO-SCOUT", "BLOCKED", detail="Generative RuFlo execution is not certified"))
            run.status = "FROZEN"
            return run
        else:
            run.results.append(StageResult("ruflo-certification", "RUFLO-SCOUT", "SKIPPED", detail="Work item does not touch RuFlo"))

        for attempt in range(1, 4):
            run.attempt = attempt
            implementation = await self.handlers.implementation(item, sandbox)
            testing, security = await asyncio.gather(
                self.handlers.testing(item, sandbox),
                self.handlers.security(item, sandbox),
            )
            run.results.extend((implementation, testing, security))
            gate = await self.handlers.gate(item, sandbox, [implementation, testing, security], attempt)
            run.results.append(gate)
            if gate.status == "PASS":
                release = await self.handlers.release(item, sandbox, run.results)
                run.results.append(release)
                run.status = "READY_TO_MERGE"
                run.artifact_manifest = release.evidence[0]
                return run
            if attempt < 3:
                run.results.append(StageResult("remediation", "IMPLEMENTER", "RETRY", detail=f"gate attempt {attempt} failed"))
        run.status = "FROZEN"
        return run

    def save_run(self, run: BuilderRun) -> Path:
        target = self.root / "memory_store" / "checkpoints" / f"{run.run_id}.json"
        payload = {
            "checkpoint_version": "1.0",
            "created_at": datetime.now(UTC).isoformat(),
            "run_id": run.run_id,
            "work_item_id": run.work_item_id,
            "status": run.status,
            "attempt": run.attempt,
            "results": [
                {"stage": result.stage, "agent": result.agent, "status": result.status, "evidence": list(result.evidence), "detail": result.detail}
                for result in run.results
            ],
            "artifact_manifest": run.artifact_manifest,
            "ruflo_execution": False,
            "production_credentials": False,
        }
        target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return target
