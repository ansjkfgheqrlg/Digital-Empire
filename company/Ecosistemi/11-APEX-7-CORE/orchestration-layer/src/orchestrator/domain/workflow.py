from __future__ import annotations

from dataclasses import dataclass, field

from .budget import BudgetAmount, BudgetLedger
from .errors import InvariantViolation, StaleVersion
from .events import DomainEvent
from .states import ActorType, RiskClass, WorkflowStatus
from .transitions import TransitionContext, validate_transition


@dataclass
class Workflow:
    workflow_id: str
    tenant_id: str
    workflow_type: str
    goal: str
    risk: RiskClass
    requested_by: str
    idempotency_key: str
    budget: BudgetLedger
    status: WorkflowStatus = WorkflowStatus.RECEIVED
    version: int = 0
    sequence: int = 0
    events: list[DomainEvent] = field(default_factory=list)
    constraints: dict = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        workflow_id: str,
        tenant_id: str,
        workflow_type: str,
        goal: str,
        risk: RiskClass,
        requested_by: str,
        idempotency_key: str,
        budget_limit: BudgetAmount,
        constraints: dict | None = None,
    ) -> "Workflow":
        values = {
            "workflow_id": workflow_id,
            "tenant_id": tenant_id,
            "workflow_type": workflow_type,
            "goal": goal,
            "requested_by": requested_by,
            "idempotency_key": idempotency_key,
        }
        missing = [name for name, value in values.items() if not value.strip()]
        if missing:
            raise InvariantViolation(f"Required workflow fields are empty: {missing}")
        if len(goal) > 20000:
            raise InvariantViolation("Workflow goal exceeds 20000 characters")
        workflow = cls(
            workflow_id=workflow_id,
            tenant_id=tenant_id,
            workflow_type=workflow_type,
            goal=goal,
            risk=risk,
            requested_by=requested_by,
            idempotency_key=idempotency_key,
            budget=BudgetLedger(budget_limit),
            constraints=dict(constraints or {}),
        )
        workflow._emit("workflow.received", {"risk": risk.value})
        return workflow

    def transition(
        self,
        target: WorkflowStatus,
        actor: ActorType,
        context: TransitionContext,
        expected_version: int,
    ) -> DomainEvent:
        if expected_version != self.version:
            raise StaleVersion(
                f"Expected version {expected_version}, current version {self.version}"
            )
        if self.status.terminal:
            raise InvariantViolation(f"Terminal workflow cannot transition from {self.status.value}")
        previous = self.status
        validate_transition(previous, target, actor, context)
        self.status = target
        self.version += 1
        return self._emit(
            "workflow.transitioned",
            {
                "from": previous.value,
                "to": target.value,
                "actor": actor.value,
                "evidence_refs": list(context.evidence_refs),
            },
        )

    def _emit(self, event_type: str, payload: dict) -> DomainEvent:
        self.sequence += 1
        event = DomainEvent.create(
            event_type=event_type,
            workflow_id=self.workflow_id,
            sequence=self.sequence,
            aggregate_version=self.version,
            payload=payload,
        )
        self.events.append(event)
        return event
