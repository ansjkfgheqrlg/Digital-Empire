"""Client Playwright per Arena (generazione copertine).

Stessi confini del client YouTube: URL e selettori arrivano dalla configurazione, non ci sono
valori predefiniti, e senza configurazione il client lo dichiara invece di tentare.

Il workflow e' costruito perche' l'assenza di questa automazione **non** sia bloccante: il
brief della copertina viene comunque prodotto e la copertina resta marcata come non generata.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Self

from ..core.exceptions import AutomationNotConfiguredError, BrowserAutomationError

logger = logging.getLogger(__name__)

#: Chiavi richieste in ``YAF_ARENA_SELECTORS``.
REQUIRED_SELECTORS: tuple[str, ...] = ("prompt_input", "submit_button", "result_image")


@dataclass(frozen=True)
class ThumbnailGenerationResult:
    """Esito di un tentativo di generazione."""

    generated: bool
    image_url: str | None
    note: str


class ArenaPlaywrightClient:
    """Client asincrono per la generazione assistita di copertine."""

    def __init__(
        self,
        *,
        base_url: str,
        selectors: dict[str, str],
        headless: bool = True,
        timeout_ms: int = 30_000,
        profile_dir: str = "",
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.selectors = dict(selectors)
        self.headless = headless
        self.timeout_ms = timeout_ms
        self.profile_dir = profile_dir
        self._playwright: Any | None = None
        self._context: Any | None = None

    def missing_config(self) -> list[str]:
        mancanti = [k for k in REQUIRED_SELECTORS if not self.selectors.get(k)]
        if not self.base_url:
            mancanti.append("base_url")
        return mancanti

    def is_configured(self) -> bool:
        return not self.missing_config()

    async def __aenter__(self) -> Self:
        try:
            from playwright.async_api import async_playwright
        except ImportError as exc:  # pragma: no cover - dipende dall'ambiente
            raise BrowserAutomationError(
                "Playwright non installato. Installa l'extra 'browser'."
            ) from exc
        try:
            self._playwright = await async_playwright().start()
            if self.profile_dir:
                self._context = await self._playwright.chromium.launch_persistent_context(
                    user_data_dir=self.profile_dir, headless=self.headless
                )
            else:
                browser = await self._playwright.chromium.launch(headless=self.headless)
                self._context = await browser.new_context()
            self._context.set_default_timeout(self.timeout_ms)
        except Exception as exc:  # pragma: no cover - dipende dall'ambiente
            await self.aclose()
            raise BrowserAutomationError(f"Avvio del browser fallito: {exc}") from exc
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        if self._context is not None:
            await self._context.close()
            self._context = None
        if self._playwright is not None:
            await self._playwright.stop()
            self._playwright = None

    async def generate_thumbnail(self, prompt: str) -> ThumbnailGenerationResult:
        """Invia il brief e attende l'immagine risultante.

        Solleva ``AutomationNotConfiguredError`` se manca la configurazione: chi chiama deve
        gestirla mantenendo la copertina come "non generata".
        """
        mancanti = self.missing_config()
        if mancanti:
            raise AutomationNotConfiguredError("arena", mancanti)
        if self._context is None:
            raise BrowserAutomationError("Client non avviato: usare 'async with'.")

        page = await self._context.new_page()
        try:
            await page.goto(self.base_url)
            await page.fill(self.selectors["prompt_input"], prompt)
            await page.click(self.selectors["submit_button"])
            await page.wait_for_selector(self.selectors["result_image"])
            elemento = await page.query_selector(self.selectors["result_image"])
            src = await elemento.get_attribute("src") if elemento else None
            if not src:
                return ThumbnailGenerationResult(
                    generated=False,
                    image_url=None,
                    note="Nessuna immagine trovata al termine della generazione.",
                )
            return ThumbnailGenerationResult(
                generated=True, image_url=src, note="Immagine generata dal brief."
            )
        except AutomationNotConfiguredError:
            raise
        except Exception as exc:
            raise BrowserAutomationError(f"Generazione copertina fallita: {exc}") from exc
        finally:
            await page.close()
