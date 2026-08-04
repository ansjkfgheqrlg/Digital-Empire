"""Livello senior: l'unico che approva riferimenti, script e nuove nicchie."""

from __future__ import annotations

import logging
from dataclasses import dataclass

from ..core.approvals import record_approval
from ..core.enums import AgentLevel, ApprovalDecision
from ..core.models import Approval, NicheProposal, ScriptAsset, VideoCandidate, WorkflowRun
from ..core.validators import validate_candidate_data, validate_niche, validate_script
from .base import BaseAgent

logger = logging.getLogger(__name__)

#: Soglia minima di visualizzazioni perche' un riferimento sia considerato significativo.
MIN_VIEWS_FOR_REFERENCE = 1_000


@dataclass(frozen=True)
class SeniorEvaluation:
    """Valutazione motivata, con i criteri esaminati uno per uno."""

    approved: bool
    reason: str
    criteria: dict[str, bool]
    production_priority: int


class SeniorDecisionAgent(BaseAgent):
    """Decide su candidati, script e proposte di nicchia."""

    level = AgentLevel.SENIOR

    # -- candidati ------------------------------------------------------------------
    def evaluate_candidate(self, candidate: VideoCandidate) -> SeniorEvaluation:
        """Valuta visualizzazioni, argomento, pertinenza di nicchia e utilita' editoriale."""
        criteri = {
            "dati_minimi": not validate_candidate_data(candidate),
            "nicchia_pertinente": not validate_niche(candidate, self.primary_niche),
            "visualizzazioni_significative": candidate.views >= MIN_VIEWS_FOR_REFERENCE,
            "argomento_dichiarato": bool(candidate.topic.strip()),
        }
        approvato = all(criteri.values())
        falliti = [k for k, ok in criteri.items() if not ok]
        if approvato:
            motivo = (
                "Criteri superati: " + ", ".join(criteri) + ". Ammesso come riferimento "
                "analitico, non come modello da replicare."
            )
        else:
            motivo = "Criteri non superati: " + ", ".join(falliti) + "."
        priorita = 1 if candidate.views >= 100_000 else 2 if candidate.views >= 10_000 else 3
        return SeniorEvaluation(approvato, motivo, criteri, priorita)

    def approve_reference(self, run: WorkflowRun, candidate: VideoCandidate) -> Approval:
        """Registra la decisione sul candidato. Riservata al livello senior."""
        self.authorize("approve_reference")
        valutazione = self.evaluate_candidate(candidate)
        decisione = (
            ApprovalDecision.APPROVED if valutazione.approved else ApprovalDecision.REJECTED
        )
        return record_approval(
            run,
            subject_id=candidate.id,
            decision=decisione,
            approver=self.name,
            approver_level=self.level,
            reason=valutazione.reason,
            action="approve_reference",
        )

    # -- script ---------------------------------------------------------------------
    def approve_script(self, run: WorkflowRun, script: ScriptAsset) -> Approval:
        """Approva lo script solo se ha superato i controlli e non e' derivato."""
        self.authorize("approve_script")
        problemi = validate_script(script)
        if script.derived_from_transcript:
            problemi.append("Script derivato dal transcript del riferimento.")
        approvato = not problemi
        decisione = ApprovalDecision.APPROVED if approvato else ApprovalDecision.REJECTED
        motivo = "Script originale e completo." if approvato else "; ".join(problemi)
        return record_approval(
            run,
            subject_id=script.id,
            decision=decisione,
            approver=self.name,
            approver_level=self.level,
            reason=motivo,
            action="approve_script",
        )

    # -- nicchie --------------------------------------------------------------------
    def decide_niche_proposal(
        self, proposal: NicheProposal, *, approve: bool, reason: str
    ) -> NicheProposal:
        """Decide su una proposta di nicchia.

        Anche un'approvazione **non** cambia la nicchia primaria del sistema: abilita solo la
        valutazione della proposta per workflow futuri, con una modifica esplicita della
        configurazione fatta da un operatore umano.
        """
        self.authorize("decide_niche_proposal")
        proposal.senior_decision = (
            ApprovalDecision.APPROVED if approve else ApprovalDecision.REJECTED
        )
        logger.info(
            "[%s] proposta di nicchia '%s': %s — %s",
            self.name,
            proposal.name,
            proposal.senior_decision,
            reason,
        )
        return proposal
