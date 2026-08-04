"""Team copertine: brief originale e, quando configurata, generazione via Arena."""

from __future__ import annotations

import logging

from ..automation.arena_playwright import ArenaPlaywrightClient
from ..core.enums import AgentLevel
from ..core.exceptions import AutomationNotConfiguredError, BrowserAutomationError
from ..core.models import CopyAsset, ScriptAsset, ThumbnailAsset
from .base import BaseAgent

logger = logging.getLogger(__name__)


class ThumbnailAgent(BaseAgent):
    """Crea il brief della copertina e ne coordina l'eventuale generazione.

    Se l'automazione browser non e' configurata o fallisce, il brief resta valido e la
    copertina **non** viene dichiarata generata: il workflow prosegue in uno stato coerente
    invece di fingere un risultato che non esiste.
    """

    level = AgentLevel.OPERATIONAL

    def draft_thumbnail(
        self,
        *,
        workflow_id: str,
        script: ScriptAsset,
        copy: CopyAsset | None = None,
        concept: str | None = None,
    ) -> ThumbnailAsset:
        """Costruisce il brief a partire da script e copy, per garantirne la coerenza."""
        concetto = concept or f"Rappresentazione visiva originale del tema: {script.title}."
        parti = [
            f"Titolo del video: {script.title}.",
            f"Concept: {concetto}",
            "Vincolo: composizione originale. Non replicare layout, elementi distintivi o "
            "creativita' di terzi.",
        ]
        if copy is not None:
            parti.append(f"Coerenza con la headline del copy: {copy.headline}")
        thumbnail = ThumbnailAsset(
            workflow_id=workflow_id,
            author=self.name,
            brief=" ".join(parti),
            concept=concetto,
            generated=False,
            replicates_competitor_layout=False,
        )
        logger.info("[%s] brief copertina %s", self.name, thumbnail.id)
        return thumbnail

    async def try_generate(
        self, thumbnail: ThumbnailAsset, client: ArenaPlaywrightClient
    ) -> tuple[ThumbnailAsset, str]:
        """Tenta la generazione. Restituisce l'asset e una nota sull'esito.

        Non solleva se l'automazione non e' configurata: quello e' uno scenario previsto.
        """
        if not client.is_configured():
            nota = (
                "Automazione Arena non configurata (mancano: "
                f"{', '.join(client.missing_config())}). Brief prodotto, copertina non generata."
            )
            logger.info("[%s] %s", self.name, nota)
            return thumbnail, nota

        try:
            async with client:
                result = await client.generate_thumbnail(thumbnail.brief)
        except (AutomationNotConfiguredError, BrowserAutomationError) as exc:
            nota = f"Generazione non riuscita: {exc}. Brief mantenuto, copertina non generata."
            logger.warning("[%s] %s", self.name, nota)
            return thumbnail, nota

        if not result.generated or not result.image_url:
            return thumbnail, f"Nessuna immagine prodotta: {result.note}"

        thumbnail.generated = True
        thumbnail.generation_backend = "arena-playwright"
        thumbnail.image_path = result.image_url
        return thumbnail, result.note
