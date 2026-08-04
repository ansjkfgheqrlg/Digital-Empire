"""Team copy: produce copy originale e lo manda in revisione a Digital Empire."""

from __future__ import annotations

import logging

from ..core.enums import AgentLevel, CopyReviewStatus
from ..core.models import CopyAsset
from .base import BaseAgent

logger = logging.getLogger(__name__)


class CopywritingAgent(BaseAgent):
    """Scrive il copy.

    Puo' ricevere insight dalla formazione Second Brain o dall'analisi di copy performanti
    della nicchia: quelle fonti sono **studio di pattern comunicativi** (struttura di una
    headline, tipo di promessa, registro), non testo da riusare. Gli insight vengono
    registrati in ``pattern_insights`` per rendere tracciabile cosa ha influenzato il lavoro.
    """

    level = AgentLevel.OPERATIONAL

    def draft_copy(
        self,
        *,
        workflow_id: str,
        headline: str,
        body: str,
        brief: str,
        pattern_insights: list[str] | None = None,
    ) -> CopyAsset:
        """Crea la bozza di copy, non ancora sottoposta a revisione esterna."""
        copy = CopyAsset(
            workflow_id=workflow_id,
            author=self.name,
            brief=brief,
            headline=headline,
            body=body,
            pattern_insights=list(pattern_insights or []),
            digital_empire_status=CopyReviewStatus.NOT_SUBMITTED,
        )
        logger.info("[%s] bozza copy %s", self.name, copy.id)
        return copy

    def submit_to_digital_empire(self, copy: CopyAsset) -> CopyAsset:
        """Invia il copy alla revisione esterna, rendendo lo stato tracciabile."""
        copy.digital_empire_status = CopyReviewStatus.PENDING
        logger.info("[%s] copy %s inviato al settore copy di Digital Empire", self.name, copy.id)
        return copy


class DigitalEmpireCopyReviewer:
    """Revisore esterno: il settore copy di Digital Empire.

    Non e' un agente della fabbrica e non appartiene alla sua gerarchia: rappresenta un
    passaggio di approvazione **esterno**, che la fabbrica puo' solo attendere. Per questo la
    sua decisione e' registrata sull'asset e non fra le ``Approval`` interne.
    """

    def __init__(self, reviewer_name: str = "settore-copy-digital-empire") -> None:
        self.reviewer_name = reviewer_name

    def review(self, copy: CopyAsset, *, approve: bool, reason: str) -> CopyAsset:
        """Registra l'esito della revisione esterna."""
        if copy.digital_empire_status is CopyReviewStatus.NOT_SUBMITTED:
            raise ValueError(
                "Il copy non e' stato inviato in revisione: chiamare prima "
                "submit_to_digital_empire()."
            )
        copy.digital_empire_status = (
            CopyReviewStatus.APPROVED if approve else CopyReviewStatus.REJECTED
        )
        copy.digital_empire_reviewer = self.reviewer_name
        copy.digital_empire_reason = reason
        logger.info(
            "[%s] copy %s: %s — %s",
            self.reviewer_name,
            copy.id,
            copy.digital_empire_status,
            reason,
        )
        return copy
