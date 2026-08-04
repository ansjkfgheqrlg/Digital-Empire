"""Agente revisore: completezza dei dati e pertinenza di nicchia."""

from __future__ import annotations

import logging

from ..core.enums import AgentLevel, ReviewOutcome
from ..core.models import ReviewRequest, VideoCandidate
from ..core.validators import validate_candidate_data, validate_niche
from .base import BaseAgent

logger = logging.getLogger(__name__)


class ReviewAgent(BaseAgent):
    """Filtra i candidati prima che arrivino al livello senior."""

    level = AgentLevel.REVIEWER

    def review(self, candidate: VideoCandidate) -> ReviewRequest:
        """Approva, respinge o chiede integrazioni. Non decide la produzione."""
        self.authorize("review_candidate")

        fuori_nicchia = validate_niche(candidate, self.primary_niche)
        if fuori_nicchia:
            return ReviewRequest(
                subject_id=candidate.id,
                reviewer=self.name,
                outcome=ReviewOutcome.REJECTED,
                reason=" ".join(fuori_nicchia),
            )

        dati_mancanti = validate_candidate_data(candidate)
        if dati_mancanti:
            _, mancanti = candidate.has_minimum_data()
            return ReviewRequest(
                subject_id=candidate.id,
                reviewer=self.name,
                outcome=ReviewOutcome.NEEDS_MORE_DATA,
                reason=" ".join(dati_mancanti),
                missing_fields=mancanti,
            )

        return ReviewRequest(
            subject_id=candidate.id,
            reviewer=self.name,
            outcome=ReviewOutcome.APPROVED,
            reason=(
                f"Dati completi e nicchia coerente con '{self.primary_niche}'. "
                f"Pronto per la valutazione senior."
            ),
        )
