"""Ricerca di altri canali dentro la nicchia primaria."""

from __future__ import annotations

import logging

from ..core.enums import AgentLevel
from ..core.models import ChannelDiscovery
from .base import BaseAgent

logger = logging.getLogger(__name__)


class NicheChannelScoutAgent(BaseAgent):
    """Amplia il bacino di analisi restando **dentro** la nicchia primaria.

    Dipendere da un solo canale e' fragile: se smette di pubblicare, l'analisi si ferma.
    Questo agente aggiunge fonti, non cambia la nicchia — la assegna sempre a partire dalla
    configurazione, non da un parametro.
    """

    level = AgentLevel.OPERATIONAL

    def register_channel(self, *, name: str, url: str, rationale: str) -> ChannelDiscovery:
        """Registra un canale come coerente con la nicchia primaria."""
        discovery = ChannelDiscovery(
            name=name,
            url=url,
            niche=self.primary_niche,
            rationale=rationale,
        )
        logger.info("[%s] canale registrato: %s", self.name, name)
        return discovery

    def register_many(self, entries: list[dict[str, str]]) -> list[ChannelDiscovery]:
        """Registra piu' canali. Le voci incomplete vengono scartate, non completate a mano."""
        risultati: list[ChannelDiscovery] = []
        for voce in entries:
            if not all(voce.get(k) for k in ("name", "url", "rationale")):
                logger.warning("[%s] voce incompleta scartata: %s", self.name, voce)
                continue
            risultati.append(
                self.register_channel(
                    name=voce["name"], url=voce["url"], rationale=voce["rationale"]
                )
            )
        return risultati
