"""Agente operativo di ricerca."""

from __future__ import annotations

import logging

from ..core.enums import AgentLevel
from ..core.models import TranscriptAsset, VideoCandidate
from .base import BaseAgent

logger = logging.getLogger(__name__)


class ResearchAgent(BaseAgent):
    """Cerca candidati nella nicchia primaria e ne raccoglie i dati disponibili.

    Non approva nulla e non cambia la nicchia: produce materiale per il livello superiore.
    """

    level = AgentLevel.OPERATIONAL

    def build_candidate(
        self,
        *,
        title: str,
        url: str,
        channel: str,
        topic: str,
        views: int,
        transcript: TranscriptAsset | None = None,
        notes: list[str] | None = None,
    ) -> VideoCandidate:
        """Costruisce un candidato **sempre** nella nicchia primaria.

        La nicchia non e' un parametro: un agente operativo non puo' sceglierla.
        """
        candidate = VideoCandidate(
            title=title,
            url=url,
            channel=channel,
            topic=topic,
            views=views,
            niche=self.primary_niche,
            transcript=transcript,
            notes=list(notes or []),
        )
        logger.info("[%s] candidato raccolto: %s (%s viste)", self.name, title, views)
        return candidate

    @staticmethod
    def transcript_unavailable(video_id: str, note: str) -> TranscriptAsset:
        """Registra l'assenza del transcript senza inventarne il contenuto."""
        return TranscriptAsset(video_id=video_id, available=False, note=note)
