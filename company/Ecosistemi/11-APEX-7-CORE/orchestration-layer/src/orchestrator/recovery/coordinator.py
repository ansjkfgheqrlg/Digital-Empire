from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from orchestrator.domain import ActorType, Workflow, WorkflowStatus
from orchestrator.domain.transitions import TransitionContext
from orchestrator.governance.grants import CapabilityGrantService

from .catalog import CompensationCatalog, ReconciliationStatus


class RecoveryOutcome(StrEnum):
    RETRYABLE = "RETRYABLE"
    COMPENSATED = "COMPENSATED"
    MANUAL_INTERVENTION = "MANUAL_INTERVENTION"
    CANCELLED = "CANCELLED"


@dataclass(frozen=True)
class RecoveryRecord:
    outcome: RecoveryOutcome
    evidence: dict[str, Any]


class RecoveryCoordinator:
    def __init__(self, catalog: CompensationCatalog, grants: CapabilityGrantService):
        self.catalog = catalog
        self.grants = grants

    async def request_cancel(
        self,
        workflow: Workflow,
        *,
        running_task_id: str | None,
        residual_effect: bool,
    ) -> RecoveryRecord:
        self._transition(
            workflow,
            WorkflowStatus.CANCEL_REQUESTED,
            ActorType.SYSTEM,
            "cancel_request_persisted",
        )
        if running_task_id:
            await self.grants.revoke_task(workflow.tenant_id, running_task_id)
            self._transition(
                workflow,
                WorkflowStatus.CANCELLING,
                ActorType.RECOVERY,
                "running_task_present",
            )
            return RecoveryRecord(
                RecoveryOutcome.RETRYABLE,
                {"state": "CANCELLING", "grants_revoked_for": running_task_id},
            )
        if residual_effect:
            raise ValueError("Residual effect requires reconciliation before cancellation")
        self._transition(
            workflow,
            WorkflowStatus.CANCELLED,
            ActorType.RECOVERY,
            "no_running_task",
            "no_residual_effect",
        )
        return RecoveryRecord(RecoveryOutcome.CANCELLED, {"state": "CANCELLED"})

    async def reconcile_and_recover(
        self,
        workflow: Workflow,
        operation_id: str,
        context: dict[str, Any],
        *,
        from_cancellation: bool = False,
    ) -> RecoveryRecord:
        operation = self.catalog.require(operation_id)
        if workflow.status is WorkflowStatus.RUNNING:
            self._transition(
                workflow,
                WorkflowStatus.RECONCILING,
                ActorType.RECOVERY,
                "outcome_unknown",
            )
        elif workflow.status is WorkflowStatus.CANCELLING:
            self._transition(
                workflow,
                WorkflowStatus.RECONCILING,
                ActorType.RECOVERY,
                "outcome_unknown",
            )
        elif workflow.status is not WorkflowStatus.RECONCILING:
            raise ValueError(f"Cannot reconcile from {workflow.status.value}")

        reconciliation = await operation.reconcile(context)
        if reconciliation.status is ReconciliationStatus.ABSENT:
            if from_cancellation:
                self._transition(
                    workflow,
                    WorkflowStatus.CANCELLED,
                    ActorType.RECOVERY,
                    "cancel_effect_absent",
                )
                return RecoveryRecord(
                    RecoveryOutcome.CANCELLED,
                    reconciliation.evidence,
                )
            self._transition(
                workflow,
                WorkflowStatus.RUNNING,
                ActorType.RECOVERY,
                "outcome_resolved_continue",
            )
            return RecoveryRecord(RecoveryOutcome.RETRYABLE, reconciliation.evidence)
        if reconciliation.status is ReconciliationStatus.UNKNOWN:
            self._transition(
                workflow,
                WorkflowStatus.MANUAL_INTERVENTION,
                ActorType.RECOVERY,
                "outcome_unresolvable",
            )
            return RecoveryRecord(RecoveryOutcome.MANUAL_INTERVENTION, reconciliation.evidence)

        self._transition(
            workflow,
            WorkflowStatus.COMPENSATING,
            ActorType.RECOVERY,
            "effect_confirmed",
            "compensation_required",
        )
        compensation = await operation.compensate(context)
        if compensation.success:
            self._transition(
                workflow,
                WorkflowStatus.COMPENSATED,
                ActorType.RECOVERY,
                "all_compensations_pass",
            )
            return RecoveryRecord(RecoveryOutcome.COMPENSATED, compensation.evidence)
        self._transition(
            workflow,
            WorkflowStatus.MANUAL_INTERVENTION,
            ActorType.RECOVERY,
            "compensation_failed",
        )
        return RecoveryRecord(
            RecoveryOutcome.MANUAL_INTERVENTION,
            {**compensation.evidence, "error": compensation.error},
        )

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
