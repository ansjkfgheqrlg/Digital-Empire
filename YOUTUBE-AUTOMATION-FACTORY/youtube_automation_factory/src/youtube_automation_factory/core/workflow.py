"""Macchina a stati e orchestratore del workflow.

Le transizioni ammesse sono dichiarate in ``ALLOWED_TRANSITIONS``: qualunque salto fuori dalla
mappa solleva ``InvalidTransitionError`` **e** lascia un evento nel registro, cosi' un
tentativo illecito resta tracciato anche quando viene respinto.
"""

from __future__ import annotations

import logging

from .approvals import assert_senior_approval
from .enums import AgentLevel, WorkflowState
from .exceptions import (
    InvalidTransitionError,
    NicheLockError,
    RegulatoryBlockError,
)
from .models import WorkflowEvent, WorkflowRun
from .validators import validate_ready_for_completion

logger = logging.getLogger(__name__)

#: Grafo delle transizioni ammesse. Ogni stato elenca i successori legittimi.
ALLOWED_TRANSITIONS: dict[WorkflowState, frozenset[WorkflowState]] = {
    WorkflowState.DISCOVERED: frozenset({WorkflowState.UNDER_REVIEW, WorkflowState.BLOCKED}),
    WorkflowState.UNDER_REVIEW: frozenset(
        {
            WorkflowState.NEEDS_MORE_DATA,
            WorkflowState.REJECTED,
            WorkflowState.APPROVED_AS_REFERENCE,
            WorkflowState.BLOCKED,
        }
    ),
    WorkflowState.NEEDS_MORE_DATA: frozenset(
        {WorkflowState.UNDER_REVIEW, WorkflowState.REJECTED, WorkflowState.BLOCKED}
    ),
    WorkflowState.APPROVED_AS_REFERENCE: frozenset(
        {WorkflowState.SCRIPT_DRAFT, WorkflowState.BLOCKED}
    ),
    WorkflowState.SCRIPT_DRAFT: frozenset(
        {WorkflowState.SCRIPT_PENDING_APPROVAL, WorkflowState.BLOCKED}
    ),
    WorkflowState.SCRIPT_PENDING_APPROVAL: frozenset(
        {WorkflowState.SCRIPT_APPROVED, WorkflowState.SCRIPT_DRAFT, WorkflowState.BLOCKED}
    ),
    WorkflowState.SCRIPT_APPROVED: frozenset(
        {WorkflowState.PRODUCTION_PENDING, WorkflowState.BLOCKED}
    ),
    WorkflowState.PRODUCTION_PENDING: frozenset(
        {WorkflowState.IN_PRODUCTION, WorkflowState.BLOCKED}
    ),
    WorkflowState.IN_PRODUCTION: frozenset(
        {WorkflowState.VIDEO_READY_FOR_QA, WorkflowState.BLOCKED}
    ),
    WorkflowState.VIDEO_READY_FOR_QA: frozenset(
        {WorkflowState.COPY_DRAFT, WorkflowState.BLOCKED}
    ),
    WorkflowState.COPY_DRAFT: frozenset(
        {WorkflowState.COPY_PENDING_DIGITAL_EMPIRE_REVIEW, WorkflowState.BLOCKED}
    ),
    WorkflowState.COPY_PENDING_DIGITAL_EMPIRE_REVIEW: frozenset(
        {WorkflowState.COPY_APPROVED, WorkflowState.COPY_DRAFT, WorkflowState.BLOCKED}
    ),
    WorkflowState.COPY_APPROVED: frozenset(
        {WorkflowState.THUMBNAIL_DRAFT, WorkflowState.BLOCKED}
    ),
    WorkflowState.THUMBNAIL_DRAFT: frozenset(
        {WorkflowState.THUMBNAIL_PENDING_REVIEW, WorkflowState.BLOCKED}
    ),
    WorkflowState.THUMBNAIL_PENDING_REVIEW: frozenset(
        {
            WorkflowState.THUMBNAIL_APPROVED,
            WorkflowState.THUMBNAIL_DRAFT,
            WorkflowState.BLOCKED,
        }
    ),
    WorkflowState.THUMBNAIL_APPROVED: frozenset(
        {WorkflowState.QUALITY_CONTROL, WorkflowState.BLOCKED}
    ),
    WorkflowState.QUALITY_CONTROL: frozenset(
        {WorkflowState.COMPLETED, WorkflowState.BLOCKED}
    ),
    # Da BLOCKED si torna indietro solo dove un regolatore ha sbloccato esplicitamente.
    WorkflowState.BLOCKED: frozenset(
        {
            WorkflowState.UNDER_REVIEW,
            WorkflowState.SCRIPT_DRAFT,
            WorkflowState.COPY_DRAFT,
            WorkflowState.THUMBNAIL_DRAFT,
            WorkflowState.QUALITY_CONTROL,
            WorkflowState.REJECTED,
        }
    ),
    WorkflowState.COMPLETED: frozenset(),
    WorkflowState.REJECTED: frozenset(),
}


class YouTubeFactoryWorkflow:
    """Orchestratore: unico punto in cui lo stato di un ``WorkflowRun`` cambia."""

    def __init__(self, run: WorkflowRun, primary_niche: str) -> None:
        self.run = run
        self.primary_niche = primary_niche

    # -- registro ------------------------------------------------------------------
    def log_event(
        self,
        *,
        actor: str,
        action: str,
        reason: str = "",
        actor_level: AgentLevel | None = None,
        from_state: WorkflowState | None = None,
        to_state: WorkflowState | None = None,
    ) -> WorkflowEvent:
        event = WorkflowEvent(
            workflow_id=self.run.id,
            actor=actor,
            actor_level=actor_level,
            action=action,
            reason=reason,
            from_state=from_state,
            to_state=to_state,
        )
        self.run.events.append(event)
        return event

    # -- transizioni ---------------------------------------------------------------
    def can_transition(self, target: WorkflowState) -> bool:
        return target in ALLOWED_TRANSITIONS.get(self.run.state, frozenset())

    def transition(
        self,
        target: WorkflowState,
        *,
        actor: str,
        actor_level: AgentLevel | None = None,
        reason: str = "",
    ) -> WorkflowState:
        """Applica una transizione, verificando grafo e precondizioni di dominio."""
        corrente = self.run.state
        if not self.can_transition(target):
            self.log_event(
                actor=actor,
                actor_level=actor_level,
                action="transition_rejected",
                reason=f"{corrente} → {target} non ammessa",
                from_state=corrente,
            )
            raise InvalidTransitionError(corrente, target, "transizione non nel grafo")

        self._check_preconditions(target)

        self.run.state = target
        self.log_event(
            actor=actor,
            actor_level=actor_level,
            action="transition",
            reason=reason,
            from_state=corrente,
            to_state=target,
        )
        logger.info("[%s] %s → %s (%s)", self.run.id, corrente, target, actor)
        return target

    def _check_preconditions(self, target: WorkflowState) -> None:
        """Vincoli di dominio che il solo grafo non puo' esprimere."""
        run = self.run

        if target is WorkflowState.APPROVED_AS_REFERENCE:
            if run.candidate is None:
                raise InvalidTransitionError(
                    run.state, target, "nessun candidato da approvare"
                )
            assert_senior_approval(run, run.candidate.id, "Candidato video")

        elif target is WorkflowState.SCRIPT_APPROVED:
            if run.script is None:
                raise InvalidTransitionError(run.state, target, "nessuno script presente")
            if not run.script.originality_checked:
                raise RegulatoryBlockError(
                    ["Lo script non ha superato il controllo di originalita'."]
                )
            assert_senior_approval(run, run.script.id, "Script")

        elif target is WorkflowState.PRODUCTION_PENDING:
            if run.script is None or not run.script.approved:
                raise InvalidTransitionError(
                    run.state, target, "la produzione richiede uno script approvato"
                )

        elif target is WorkflowState.COPY_APPROVED:
            if run.copy_asset is None:
                raise InvalidTransitionError(run.state, target, "nessun copy presente")
            from .enums import CopyReviewStatus  # import locale: evita cicli

            if run.copy_asset.digital_empire_status is not CopyReviewStatus.APPROVED:
                raise RegulatoryBlockError(
                    [
                        "Il copy non e' stato approvato dal settore copy di Digital Empire "
                        f"(stato: {run.copy_asset.digital_empire_status})."
                    ]
                )

        elif target is WorkflowState.THUMBNAIL_APPROVED:
            if run.thumbnail is None:
                raise InvalidTransitionError(run.state, target, "nessuna copertina presente")
            if not run.thumbnail.originality_checked:
                raise RegulatoryBlockError(
                    ["La copertina non ha superato il controllo di originalita'."]
                )
            if not run.thumbnail.brief.strip():
                raise RegulatoryBlockError(["La copertina non ha un brief associato."])

        elif target is WorkflowState.COMPLETED:
            motivi = validate_ready_for_completion(run)
            if motivi:
                raise RegulatoryBlockError(motivi)

    # -- nicchia -------------------------------------------------------------------
    def assert_niche_unchanged(self, agent: str, attempted_niche: str) -> None:
        """La nicchia primaria non si cambia durante un workflow."""
        if attempted_niche.strip().casefold() != self.primary_niche.strip().casefold():
            self.log_event(
                actor=agent,
                action="niche_change_blocked",
                reason=f"tentato passaggio a '{attempted_niche}'",
            )
            raise NicheLockError(agent, attempted_niche, self.primary_niche)

    # -- blocchi -------------------------------------------------------------------
    def block(self, *, actor: str, reasons: list[str]) -> None:
        """Porta il run in ``BLOCKED`` registrando le motivazioni."""
        corrente = self.run.state
        self.run.blocked_reasons = list(reasons)
        if corrente is not WorkflowState.BLOCKED:
            self.run.state = WorkflowState.BLOCKED
        self.log_event(
            actor=actor,
            actor_level=AgentLevel.REGULATORY,
            action="block",
            reason="; ".join(reasons),
            from_state=corrente,
            to_state=WorkflowState.BLOCKED,
        )
        logger.warning("[%s] BLOCCATO: %s", self.run.id, "; ".join(reasons))
