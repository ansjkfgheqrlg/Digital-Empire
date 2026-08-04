"""Agenti della fabbrica, organizzati per livello gerarchico.

* **Operativi** — eseguono: ricerca, stesura bozze, analisi preliminari.
* **Revisori** — filtrano: completezza dei dati e pertinenza di nicchia.
* **Senior** — decidono: riferimenti, script, proposte di nicchia.
* **Regolatori** — bloccano: trasversali, con potere di veto e nessun potere di approvazione.
"""

from .base import BaseAgent
from .competitor_analysis_agent import CompetitorAnalysisAgent
from .copywriting_agent import CopywritingAgent, DigitalEmpireCopyReviewer
from .niche_channel_scout_agent import NicheChannelScoutAgent
from .production_agent import ProductionAgent
from .profitable_niche_agent import ProfitableNicheAgent
from .regulatory_agent import RegulatoryAgent
from .research_agent import ResearchAgent
from .review_agent import ReviewAgent
from .script_agent import ScriptAgent
from .senior_decision_agent import SeniorDecisionAgent, SeniorEvaluation
from .thumbnail_agent import ThumbnailAgent

__all__ = [
    "BaseAgent",
    "CompetitorAnalysisAgent",
    "CopywritingAgent",
    "DigitalEmpireCopyReviewer",
    "NicheChannelScoutAgent",
    "ProductionAgent",
    "ProfitableNicheAgent",
    "RegulatoryAgent",
    "ResearchAgent",
    "ReviewAgent",
    "ScriptAgent",
    "SeniorDecisionAgent",
    "SeniorEvaluation",
    "ThumbnailAgent",
]
