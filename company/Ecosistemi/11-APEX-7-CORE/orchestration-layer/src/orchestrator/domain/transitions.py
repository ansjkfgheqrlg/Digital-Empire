from __future__ import annotations

from dataclasses import dataclass, field

from .errors import IllegalTransition
from .states import ActorType, WorkflowStatus


@dataclass(frozen=True)
class TransitionContext:
    evidence_refs: tuple[str, ...] = ()
    flags: frozenset[str] = field(default_factory=frozenset)

    def require(self, *required: str) -> None:
        missing = set(required) - set(self.flags)
        if missing:
            raise IllegalTransition(f"Transition guard failed; missing flags: {sorted(missing)}")


@dataclass(frozen=True)
class TransitionRule:
    actor: ActorType
    required_flags: tuple[str, ...] = ()


RULES: dict[tuple[WorkflowStatus, WorkflowStatus], TransitionRule] = {
    (WorkflowStatus.RECEIVED, WorkflowStatus.VALIDATING): TransitionRule(
        ActorType.API, ("request_persisted",)
    ),
    (WorkflowStatus.VALIDATING, WorkflowStatus.PLANNING): TransitionRule(
        ActorType.WORKER, ("validation_passed",)
    ),
    (WorkflowStatus.VALIDATING, WorkflowStatus.REJECTED): TransitionRule(
        ActorType.WORKER, ("validation_failed",)
    ),
    (WorkflowStatus.PLANNING, WorkflowStatus.PLAN_REVIEW): TransitionRule(
        ActorType.WORKER, ("plan_schema_valid", "dag_valid", "budget_valid")
    ),
    (WorkflowStatus.PLAN_REVIEW, WorkflowStatus.AWAITING_APPROVAL): TransitionRule(
        ActorType.POLICY, ("approval_required",)
    ),
    (WorkflowStatus.PLAN_REVIEW, WorkflowStatus.AUTHORIZED): TransitionRule(
        ActorType.POLICY, ("policy_allowed",)
    ),
    (WorkflowStatus.AWAITING_APPROVAL, WorkflowStatus.AUTHORIZED): TransitionRule(
        ActorType.HUMAN, ("approval_valid", "plan_hash_matches", "policy_hash_matches")
    ),
    (WorkflowStatus.AUTHORIZED, WorkflowStatus.RUNNING): TransitionRule(
        ActorType.WORKER, ("lease_valid", "budget_available", "grant_valid")
    ),
    (WorkflowStatus.RUNNING, WorkflowStatus.PAUSED): TransitionRule(ActorType.SYSTEM),
    (WorkflowStatus.PAUSED, WorkflowStatus.RUNNING): TransitionRule(
        ActorType.HUMAN, ("resume_allowed",)
    ),
    (WorkflowStatus.RUNNING, WorkflowStatus.RECOVERING): TransitionRule(
        ActorType.RECOVERY, ("failure_retryable", "attempts_available")
    ),
    (WorkflowStatus.RECOVERING, WorkflowStatus.RUNNING): TransitionRule(
        ActorType.WORKER, ("retry_scheduled",)
    ),
    (WorkflowStatus.RUNNING, WorkflowStatus.RECONCILING): TransitionRule(
        ActorType.RECOVERY, ("outcome_unknown",)
    ),
    (WorkflowStatus.RECONCILING, WorkflowStatus.RUNNING): TransitionRule(
        ActorType.RECOVERY, ("outcome_resolved_continue",)
    ),
    (WorkflowStatus.RECONCILING, WorkflowStatus.CANCELLED): TransitionRule(
        ActorType.RECOVERY, ("cancel_effect_absent",)
    ),
    (WorkflowStatus.RECONCILING, WorkflowStatus.COMPENSATING): TransitionRule(
        ActorType.RECOVERY, ("effect_confirmed", "compensation_required")
    ),
    (WorkflowStatus.RECONCILING, WorkflowStatus.MANUAL_INTERVENTION): TransitionRule(
        ActorType.RECOVERY, ("outcome_unresolvable",)
    ),
    (WorkflowStatus.RUNNING, WorkflowStatus.COMPENSATING): TransitionRule(
        ActorType.RECOVERY, ("effect_confirmed", "terminal_failure")
    ),
    (WorkflowStatus.RUNNING, WorkflowStatus.QUALITY_REVIEW): TransitionRule(
        ActorType.WORKER, ("required_tasks_complete",)
    ),
    (WorkflowStatus.QUALITY_REVIEW, WorkflowStatus.REMEDIATING): TransitionRule(
        ActorType.GATE, ("remediation_available", "attempts_available")
    ),
    (WorkflowStatus.REMEDIATING, WorkflowStatus.RUNNING): TransitionRule(
        ActorType.WORKER, ("remediation_task_created",)
    ),
    (WorkflowStatus.QUALITY_REVIEW, WorkflowStatus.COMPLETED): TransitionRule(
        ActorType.GATE, ("all_blocking_gates_pass",)
    ),
    (WorkflowStatus.QUALITY_REVIEW, WorkflowStatus.FAILED): TransitionRule(
        ActorType.GATE, ("terminal_quality_failure",)
    ),
    (WorkflowStatus.COMPENSATING, WorkflowStatus.COMPENSATED): TransitionRule(
        ActorType.RECOVERY, ("all_compensations_pass",)
    ),
    (WorkflowStatus.COMPENSATING, WorkflowStatus.MANUAL_INTERVENTION): TransitionRule(
        ActorType.RECOVERY, ("compensation_failed",)
    ),
    (WorkflowStatus.CANCEL_REQUESTED, WorkflowStatus.CANCELLED): TransitionRule(
        ActorType.RECOVERY, ("no_running_task", "no_residual_effect",)
    ),
    (WorkflowStatus.CANCEL_REQUESTED, WorkflowStatus.CANCELLING): TransitionRule(
        ActorType.RECOVERY, ("running_task_present",)
    ),
    (WorkflowStatus.CANCELLING, WorkflowStatus.CANCELLED): TransitionRule(
        ActorType.RECOVERY, ("cooperative_stop", "no_residual_effect")
    ),
    (WorkflowStatus.CANCELLING, WorkflowStatus.RECONCILING): TransitionRule(
        ActorType.RECOVERY, ("outcome_unknown",)
    ),
    (WorkflowStatus.CANCELLING, WorkflowStatus.COMPENSATING): TransitionRule(
        ActorType.RECOVERY, ("effect_confirmed", "compensation_required")
    ),
}

CANCELLABLE = {
    status
    for status in WorkflowStatus
    if not status.terminal
    and status
    not in {
        WorkflowStatus.CANCEL_REQUESTED,
        WorkflowStatus.CANCELLING,
        WorkflowStatus.COMPENSATING,
        WorkflowStatus.RECONCILING,
    }
}


def validate_transition(
    current: WorkflowStatus,
    target: WorkflowStatus,
    actor: ActorType,
    context: TransitionContext,
) -> None:
    if target is WorkflowStatus.CANCEL_REQUESTED and current in CANCELLABLE:
        if actor not in {ActorType.API, ActorType.HUMAN, ActorType.SYSTEM}:
            raise IllegalTransition("Cancel request requires API, HUMAN or SYSTEM actor")
        context.require("cancel_request_persisted")
        return
    rule = RULES.get((current, target))
    if rule is None:
        raise IllegalTransition(f"Illegal transition: {current.value} -> {target.value}")
    if actor is not rule.actor:
        raise IllegalTransition(
            f"Wrong actor for {current.value}->{target.value}: {actor.value}, expected {rule.actor.value}"
        )
    context.require(*rule.required_flags)
