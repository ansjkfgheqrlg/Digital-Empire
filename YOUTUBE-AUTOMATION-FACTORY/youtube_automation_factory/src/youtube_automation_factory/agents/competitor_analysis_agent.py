"""Analisi competitor e performance di canale."""

from __future__ import annotations

import logging
import statistics

from ..core.enums import AgentLevel
from ..core.models import CompetitorReport
from .base import BaseAgent

logger = logging.getLogger(__name__)


class CompetitorAnalysisAgent(BaseAgent):
    """Produce osservazioni strutturate su competitor e canale.

    Le osservazioni spiegano **perche'** qualcosa funziona in termini di formato, tema e
    struttura. Non producono in nessun caso indicazioni per replicare contenuti altrui.
    """

    level = AgentLevel.OPERATIONAL

    def analyse(
        self,
        *,
        channels: list[str],
        channel_metrics: dict[str, float] | None = None,
        video_views: dict[str, int] | None = None,
        unavailable_metrics: list[str] | None = None,
    ) -> CompetitorReport:
        """Costruisce il report.

        ``unavailable_metrics`` elenca i dati che non sono ottenibili (per esempio CTR e
        retention, che richiedono le analytics del proprietario del canale). Vengono
        dichiarati come mancanti: non si stimano.
        """
        osservazioni: list[str] = []
        views = video_views or {}

        if views:
            valori = list(views.values())
            mediana = statistics.median(valori)
            osservazioni.append(
                f"Mediana delle visualizzazioni sul campione: {mediana:.0f} "
                f"({len(valori)} video)."
            )
            sopra = [t for t, v in views.items() if v > mediana]
            if sopra:
                osservazioni.append(
                    "Video sopra la mediana: " + ", ".join(sorted(sopra)[:5]) + "."
                )
            osservazioni.append(
                "La mediana e' preferita alla media: un singolo contenuto virale "
                "sposterebbe la media e farebbe sembrare regolare un canale che non lo e'."
            )
        else:
            osservazioni.append("Nessun dato di visualizzazioni fornito: analisi limitata.")

        if channel_metrics:
            osservazioni.append(
                "Metriche di canale ricevute: " + ", ".join(sorted(channel_metrics)) + "."
            )

        osservazioni.append(
            "Uso ammesso: capire quali formati e temi rispondono a un bisogno reale "
            "dell'audience. Non sono indicazioni per replicare contenuti di terzi."
        )

        report = CompetitorReport(
            niche=self.primary_niche,
            channels_analysed=list(channels),
            observations=osservazioni,
            channel_metrics=dict(channel_metrics or {}),
            data_gaps=list(
                unavailable_metrics
                or ["CTR e retention: richiedono le analytics del proprietario del canale."]
            ),
        )
        logger.info("[%s] analisi su %s canali", self.name, len(channels))
        return report
