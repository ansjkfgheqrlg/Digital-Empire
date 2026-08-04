"""Agente operativo: brief editoriale e stesura dello script originale."""

from __future__ import annotations

import logging

from ..core.enums import AgentLevel
from ..core.models import ScriptAsset, VideoCandidate
from .base import BaseAgent

logger = logging.getLogger(__name__)


class ScriptAgent(BaseAgent):
    """Produce script **originali**.

    Il transcript del riferimento, quando presente, serve a capire tema, concetti e bisogni
    dell'audience. Non se ne riusano frasi, struttura o formulazioni: il campo
    ``derived_from_transcript`` resta ``False`` e il modello rifiuta qualunque tentativo di
    impostarlo a ``True``.
    """

    level = AgentLevel.OPERATIONAL

    def build_brief(self, candidate: VideoCandidate) -> str:
        """Brief editoriale ricavato dall'analisi del riferimento, non dal suo testo."""
        pezzi = [
            f"Tema di riferimento: {candidate.topic}.",
            f"Nicchia: {self.primary_niche}.",
            "Angolo editoriale proprio: affrontare il tema con struttura, esempi e "
            "argomentazioni originali.",
            "Uso del riferimento: analisi di tema e bisogni dell'audience. Nessun riuso di "
            "frasi, scaletta o formulazioni.",
        ]
        if candidate.transcript and candidate.transcript.available:
            pezzi.append(
                "Transcript disponibile: usato solo per individuare i concetti trattati e le "
                "domande implicite del pubblico."
            )
        else:
            nota = candidate.transcript.note if candidate.transcript else "non richiesto"
            pezzi.append(f"Transcript non disponibile ({nota}): brief costruito sul tema.")
        return " ".join(pezzi)

    def draft_script(
        self, *, workflow_id: str, candidate: VideoCandidate, title: str, body: str
    ) -> ScriptAsset:
        """Crea la bozza. Nasce con ``originality_checked=False``: il controllo viene dopo."""
        script = ScriptAsset(
            workflow_id=workflow_id,
            author=self.name,
            brief=self.build_brief(candidate),
            title=title,
            body=body,
            reference_candidate_id=candidate.id,
            derived_from_transcript=False,
        )
        logger.info(
            "[%s] bozza script %s (%s parole)", self.name, script.id, script.word_count
        )
        return script
