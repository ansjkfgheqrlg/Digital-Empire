"""Base comune a tutti gli agenti.

Ogni agente dichiara il proprio ``level``. I metodi che compiono azioni riservate chiamano
``self.authorize(...)``, che delega a ``core.approvals.require_level``: la gerarchia e' quindi
applicata dal codice, non solo descritta nella documentazione.
"""

from __future__ import annotations

import logging

from ..core.approvals import require_level
from ..core.enums import AgentLevel
from ..core.exceptions import NicheLockError

logger = logging.getLogger(__name__)


class BaseAgent:
    """Antenato di tutti gli agenti."""

    #: Livello gerarchico. Le sottoclassi devono ridefinirlo.
    level: AgentLevel = AgentLevel.OPERATIONAL

    def __init__(self, name: str, primary_niche: str) -> None:
        self.name = name
        self.primary_niche = primary_niche

    def authorize(self, action: str) -> None:
        """Verifica che il livello dell'agente basti per ``action``."""
        require_level(self.name, self.level, action)

    def assert_primary_niche(self, niche: str) -> None:
        """Impedisce a chiunque non sia senior di lavorare fuori dalla nicchia primaria."""
        if niche.strip().casefold() != self.primary_niche.strip().casefold():
            raise NicheLockError(self.name, niche, self.primary_niche)

    def __repr__(self) -> str:  # pragma: no cover - diagnostica
        return f"{type(self).__name__}(name={self.name!r}, level={self.level})"
