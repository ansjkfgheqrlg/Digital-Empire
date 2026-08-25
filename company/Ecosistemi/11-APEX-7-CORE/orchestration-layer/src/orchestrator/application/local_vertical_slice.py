from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any, Protocol
from uuid import uuid4

from jsonschema import Draft202012Validator

from orchestrator.agents import CriticAgent, GateAgent, ImplementerAgent, PlannerAgent
from orchestrator.domain import ActorType, BudgetAmount, RiskClass, Workflow, WorkflowStatus
from orchestrator.domain.events import DomainEvent
from orchestrator.domain.transitions import TransitionContext
from orchestrator.governance.grants import CapabilityGrantService, GrantBinding
from orchestrator.governance.policy import PolicyDecision, PolicyEffect
from orchestrator.quality import QualityPipeline, compress_verified_output
from orchestrator.runtime import LocalAgentRuntime, TaskAssignment
from tool_gateway import ArtifactWriteTool, RepositoryReadTool, ToolGateway, ToolRequest


class PolicyEvaluator(Protocol):
    async def evaluate(self, policy_input: dict[str, Any]) -> PolicyDecision: ...


class VerticalSliceError(RuntimeError):
    pass


@dataclass(frozen=True)
class VerticalSliceResult:
    workflow_id: str
    status: str
    artifact_path: str
    artifact_sha256: str
    gate_verdict: str
    quality: dict[str, bool]
    final_response: str
    event_count: int
    event_stream: tuple[DomainEvent, ...] = ()
    ruflo_enabled: bool = False


class RepositoryAdrVerticalSlice:
    """R1 local baseline: policy → four roles → tool gateway → quality → NERVE-SAVE."""

    def __init__(
        self,
        *,
        root: Path,
        repository_root: Path,
        artifact_root: Path,
        policy: PolicyEvaluator,
        grants: CapabilityGrantService,
    ):
        self.root = root
        self.repository_root = repository_root
        self.artifact_root = artifact_root
        self.policy = policy
        self.grants = grants
        self.runtime = LocalAgentRuntime()
        self.runtime.register("planner", PlannerAgent())
        self.runtime.register("implementer", ImplementerAgent())
        self.runtime.register("critic", CriticAgent())
        self.runtime.register("gate", GateAgent())
        self.tools = ToolGateway(grants)
        self.tools.register("repo.read", RepositoryReadTool(repository_root))
        self.tools.register("artifact.write", ArtifactWriteTool(artifact_root))

    async def run(
        self,
        *,
        tenant_id: str,
        requested_by: str,
        repository_files: list[str],
        artifact_path: str,
        workflow_id: str | None = None,
        idempotency_key: str | None = None,
    ) -> VerticalSliceResult:
        skill_input = {"repository_files": repository_files, "artifact_path": artifact_path}
        self._validate_json(self.root / "skills/repository-adr/schemas/input.json", skill_input)
        manifest = json.loads(
            (self.root / "skills/repository-adr/manifest.yaml").read_text(encoding="utf-8")
        )
        workflow = Workflow.create(
            workflow_id=workflow_id or str(uuid4()),
            tenant_id=tenant_id,
            workflow_type="repository_adr",
            goal="Analyze the scoped repository files and create an evidence-linked ADR.",
            risk=RiskClass.R1,
            requested_by=requested_by,
            idempotency_key=idempotency_key or f"local-{uuid4()}",
            budget_limit=BudgetAmount(30000, Decimal("2.00"), 300000),
            constraints={"skill_input": skill_input},
        )
        self._transition(workflow, WorkflowStatus.VALIDATING, ActorType.API, "request_persisted")
        self._transition(workflow, WorkflowStatus.PLANNING, ActorType.WORKER, "validation_passed")

        planner_id = str(uuid4())
        planner = await self.runtime.execute(
            TaskAssignment(
                workflow.workflow_id,
                planner_id,
                "planner",
                "Create the repository ADR execution plan.",
                (),
                skill_input,
                6000,
                60,
                0.40,
                "plan-v1",
            )
        )
        if planner.status != "SUCCEEDED":
            raise VerticalSliceError(f"Planner failed: {planner.failure}")
        self._transition(
            workflow,
            WorkflowStatus.PLAN_REVIEW,
            ActorType.WORKER,
            "plan_schema_valid",
            "dag_valid",
            "budget_valid",
        )

        policy_hash = "sha256:" + hashlib.sha256(
            (self.root / "policies/authorization.rego").read_bytes()
        ).hexdigest()
        decision = await self.policy.evaluate(
            {
                "tenant_id": tenant_id,
                "workflow_id": workflow.workflow_id,
                "task_id": planner_id,
                "risk": "R1",
                "requested_capabilities": list(manifest["spec"]["capabilities"]),
                "skill": {
                    "status": manifest["spec"]["status"],
                    "capabilities": list(manifest["spec"]["capabilities"]),
                },
                "budget": {"within_limit": True},
                "plan_hash": self._hash_json(planner.output),
                "policy_hash": policy_hash,
            }
        )
        if decision.effect is not PolicyEffect.ALLOW:
            raise VerticalSliceError(f"Policy did not allow workflow: {decision.reasons}")
        self._transition(workflow, WorkflowStatus.AUTHORIZED, ActorType.POLICY, "policy_allowed")
        self._transition(
            workflow,
            WorkflowStatus.RUNNING,
            ActorType.WORKER,
            "lease_valid",
            "budget_available",
            "grant_valid",
        )

        implementer_id = str(uuid4())
        binding = GrantBinding(tenant_id, workflow.workflow_id, implementer_id, "sha256:local-exec")
        sources: dict[str, dict] = {}
        for relative in repository_files:
            token, _ = await self.grants.issue(
                subject="local-implementer",
                binding=binding,
                capability_scope="repo.read",
                constraints={"path_prefix": "", "max_bytes": 1_048_576},
                ttl_seconds=60,
            )
            source = await self.tools.execute(
                ToolRequest("repo.read", "repo.read", token, binding, {"path": relative})
            )
            sources[relative] = source

        implementer = await self.runtime.execute(
            TaskAssignment(
                workflow.workflow_id,
                implementer_id,
                "implementer",
                "Create an evidence-linked ADR.",
                ("repo.read", "artifact.write:adr/**"),
                {"sources": sources},
                10000,
                120,
                0.75,
                "repository-adr-output-v1",
            )
        )
        if implementer.status != "SUCCEEDED":
            raise VerticalSliceError(f"Implementer failed: {implementer.failure}")

        output_schema = json.loads(
            (self.root / "skills/repository-adr/schemas/output.json").read_text(encoding="utf-8")
        )
        quality = QualityPipeline(output_schema).evaluate(implementer.output, sources)

        critic = await self.runtime.execute(
            TaskAssignment(
                workflow.workflow_id,
                str(uuid4()),
                "critic",
                "Falsify the ADR.",
                (),
                {"adr": implementer.output["adr"], "evidence": implementer.output["evidence"]},
                4000,
                45,
                0.30,
                "challenge-report-v1",
            )
        )

        write_token, _ = await self.grants.issue(
            subject="local-implementer",
            binding=binding,
            capability_scope="artifact.write:adr/**",
            constraints={"path_prefix": "adr/", "max_bytes": 1_048_576},
            ttl_seconds=60,
        )
        artifact = await self.tools.execute(
            ToolRequest(
                "artifact.write",
                f"artifact.write:{artifact_path}",
                write_token,
                binding,
                {"path": artifact_path, "content": implementer.output["adr"]},
            )
        )

        self._transition(
            workflow,
            WorkflowStatus.QUALITY_REVIEW,
            ActorType.WORKER,
            "required_tasks_complete",
        )
        gate = await self.runtime.execute(
            TaskAssignment(
                workflow.workflow_id,
                str(uuid4()),
                "gate",
                "Evaluate deterministic and critic evidence.",
                (),
                {
                    "issues": critic.output["issues"],
                    "deterministic_gates": quality.as_gate_map(),
                    "artifact_hash": "sha256:" + artifact["sha256"],
                },
                3000,
                30,
                0.20,
                "gate-report-v1",
            )
        )
        verdict = gate.output["verdict"]
        if verdict != "PASS" or not quality.passed:
            raise VerticalSliceError(
                f"Quality gate failed: {gate.output['blocking_failures']} {quality.failures}"
            )
        self._transition(
            workflow,
            WorkflowStatus.COMPLETED,
            ActorType.GATE,
            "all_blocking_gates_pass",
        )

        raw_response = (
            f"Workflow {workflow.workflow_id} completed. "
            f"Artifact `{artifact_path}` sha256:{artifact['sha256']}. "
            "Quality gates passed: schema, security, correctness, evidence. "
            "RuFlo non attivo; external side effects: 0."
        )
        compressed = compress_verified_output(raw_response)
        if not compressed.preservation_pass:
            raise VerticalSliceError("NERVE-SAVE protected-span preservation failed")
        return VerticalSliceResult(
            workflow_id=workflow.workflow_id,
            status=workflow.status.value,
            artifact_path=artifact_path,
            artifact_sha256=artifact["sha256"],
            gate_verdict=verdict,
            quality=quality.as_gate_map(),
            final_response=compressed.text,
            event_count=len(workflow.events),
            event_stream=tuple(workflow.events),
        )

    @staticmethod
    def _validate_json(schema_path: Path, payload: dict[str, Any]) -> None:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        errors = list(Draft202012Validator(schema).iter_errors(payload))
        if errors:
            raise VerticalSliceError("Input contract rejected: " + "; ".join(e.message for e in errors))

    @staticmethod
    def _hash_json(value: Any) -> str:
        encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
        return "sha256:" + hashlib.sha256(encoded).hexdigest()

    @staticmethod
    def _transition(
        workflow: Workflow,
        target: WorkflowStatus,
        actor: ActorType,
        *flags: str,
    ) -> None:
        workflow.transition(
            target,
            actor,
            TransitionContext(flags=frozenset(flags)),
            expected_version=workflow.version,
        )
