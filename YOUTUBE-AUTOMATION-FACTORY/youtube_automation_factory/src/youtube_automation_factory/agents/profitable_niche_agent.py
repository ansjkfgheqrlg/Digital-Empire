"""Proposte di nicchie potenzialmente profittevoli.

Questo agente **non** cambia mai ``PRIMARY_NICHE``. Produce proposte che restano tali finche'
il livello senior non le valuta e finche' un operatore umano non modifica esplicitamente la
configurazione. Il vincolo e' applicato in tre punti: qui, nel modello ``NicheProposal``
(``requires_senior_decision`` non puo' essere ``False``) e in ``core.approvals``.
"""

from __future__ import annotations

import logging

from ..core.enums import AgentLevel
from ..core.models import NicheProposal
from .base import BaseAgent

logger = logging.getLogger(__name__)


class ProfitableNicheAgent(BaseAgent):
    """Registra proposte di nuove nicchie, senza alcun potere di attivarle."""

    level = AgentLevel.OPERATIONAL

    def propose(
        self, *, name: str, rationale: str, evidence: list[str] | None = None
    ) -> NicheProposal:
        """Crea una proposta.

        La nicchia primaria configurata resta invariata: questo metodo non la legge per
        modificarla e non espone alcun modo per farlo.
        """
        proposal = NicheProposal(
            name=name,
            rationale=rationale,
            evidence=list(evidence or []),
            requires_senior_decision=True,
        )
        logger.info(
            "[%s] proposta registrata: '%s' (nicchia primaria invariata: '%s')",
            self.name,
            name,
            self.primary_niche,
        )
        return proposal
