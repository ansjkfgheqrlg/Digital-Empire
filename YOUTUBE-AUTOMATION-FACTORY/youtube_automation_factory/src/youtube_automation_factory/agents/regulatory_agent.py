"""Agente regolatorio: opera trasversalmente e puo' bloccare il workflow.

Non produce contenuti e non li approva: verifica e, se serve, ferma. La separazione e'
applicata da ``core.approvals.require_level``, che nega a un regolatore le azioni ``approve_*``.
"""

from __future__ import annotations

import logging

from ..core.enums import AgentLevel, WorkflowState
from ..core.models import WorkflowRun
from ..core.validators import (
    validate_copy,
    validate_ready_for_completion,
    validate_script,
    validate_thumbnail,
)
from ..core.workflow import ALLOWED_TRANSITIONS, YouTubeFactoryWorkflow
from ..services.originality_service import OriginalityService
from .base import BaseAgent

logger = logging.getLogger(__name__)


class RegulatoryAgent(BaseAgent):
    """Quality control e applicazione delle regole."""

    level = AgentLevel.REGULATORY

    def __init__(
        self,
        name: str,
        primary_niche: str,
        originality_service: OriginalityService | None = None,
    ) -> None:
        super().__init__(name, primary_niche)
        self.originality = originality_service or OriginalityService()

    # -- controlli ------------------------------------------------------------------
    def audit(self, run: WorkflowRun) -> list[str]:
        """Elenca tutte le non conformita' presenti. Lista vuota = conforme."""
        motivi: list[str] = []

        if run.candidate is not None:
            if run.candidate.niche.strip().casefold() != self.primary_niche.strip().casefold():
                motivi.append(
                    f"Candidato fuori nicchia: '{run.candidate.niche}' invece di "
                    f"'{self.primary_niche}'."
                )
            if not run.candidate.reference_only:
                motivi.append("Il candidato non e' marcato come riferimento analitico.")

        if run.script is not None:
            motivi.extend(validate_script(run.script))
        if run.copy is not None:
            motivi.extend(validate_copy(run.copy))
        if run.thumbnail is not None:
            motivi.extend(validate_thumbnail(run.thumbnail))

        return motivi

    def verify_transition(self, run: WorkflowRun, target: WorkflowState) -> bool:
        """Verifica che una transizione sia ammessa dal grafo, senza applicarla."""
        return target in ALLOWED_TRANSITIONS.get(run.state, frozenset())

    def check_originality_of_all(self, run: WorkflowRun) -> list[str]:
        """Ricontrolla gli asset creativi presenti e riporta quelli non conformi."""
        problemi: list[str] = []
        for asset in (run.script, run.copy, run.thumbnail):
            if asset is None:
                continue
            result = self.originality.check(asset)
            if not result.passed:
                problemi.extend(result.reasons)
        return problemi

    # -- azioni ---------------------------------------------------------------------
    def block_if_needed(
        self, workflow: YouTubeFactoryWorkflow, *, extra_reasons: list[str] | None = None
    ) -> list[str]:
        """Blocca il workflow se ci sono non conformita'. Restituisce le motivazioni."""
        self.authorize("block_workflow")
        motivi = self.audit(workflow.run) + list(extra_reasons or [])
        if motivi:
            workflow.block(actor=self.name, reasons=motivi)
        return motivi

    def clear_block(self, workflow: YouTubeFactoryWorkflow, target: WorkflowState) -> None:
        """Sblocca il workflow riportandolo a uno stato di lavorazione."""
        self.authorize("clear_regulatory_block")
        residui = self.audit(workflow.run)
        if residui:
            raise ValueError(
                "Impossibile sbloccare: restano non conformita' — " + "; ".join(residui)
            )
        workflow.run.blocked_reasons = []
        workflow.transition(
            target,
            actor=self.name,
            actor_level=self.level,
            reason="Cause di blocco rimosse.",
        )

    def final_quality_control(self, workflow: YouTubeFactoryWorkflow) -> list[str]:
        """Controllo finale prima della chiusura: video, sottotitoli, copy e copertina."""
        self.authorize("block_workflow")
        motivi = self.audit(workflow.run) + validate_ready_for_completion(workflow.run)
        # Deduplica mantenendo l'ordine, per non ripetere lo stesso motivo due volte.
        visti: set[str] = set()
        unici = [m for m in motivi if not (m in visti or visti.add(m))]
        if unici:
            workflow.block(actor=self.name, reasons=unici)
        return unici
