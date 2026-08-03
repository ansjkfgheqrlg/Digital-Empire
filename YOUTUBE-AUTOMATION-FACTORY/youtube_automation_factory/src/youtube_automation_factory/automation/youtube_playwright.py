"""Client Playwright per YouTube.

## Confini deliberati

* **Nessun selettore hardcoded.** I selettori arrivano da configurazione
  (``YAF_YOUTUBE_SELECTORS``). Se mancano, il client solleva
  ``AutomationNotConfiguredError`` invece di tentare con valori inventati: un selettore
  sbagliato non fallisce, restituisce dati *falsi*, che e' molto peggio.
* **Solo pagine pubbliche.** Nessun login, nessun aggiramento di CAPTCHA, di controlli di
  accesso o di limitazioni della piattaforma.
* **Transcript.** Si tenta il recupero solo se e' configurato il percorso previsto. Se non e'
  disponibile, si salva ``None`` con una nota: non si inventa mai il contenuto.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Self

from ..core.exceptions import AutomationNotConfiguredError, BrowserAutomationError
from ..core.models import TranscriptAsset

logger = logging.getLogger(__name__)

#: Chiavi che devono essere presenti in ``YAF_YOUTUBE_SELECTORS`` per la ricerca video.
REQUIRED_SEARCH_SELECTORS: tuple[str, ...] = ("video_card", "title", "channel", "views")
#: Chiavi aggiuntive necessarie al recupero del transcript.
REQUIRED_TRANSCRIPT_SELECTORS: tuple[str, ...] = ("transcript_button", "transcript_segment")


@dataclass(frozen=True)
class YouTubeSearchResult:
    """Riga grezza estratta dalla pagina, prima della validazione di dominio."""

    title: str
    url: str
    channel: str
    views_text: str


class YouTubePlaywrightClient:
    """Client asincrono. Usare come context manager asincrono."""

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

    # -- configurazione -------------------------------------------------------------
    def missing_selectors(self, required: tuple[str, ...]) -> list[str]:
        return [k for k in required if not self.selectors.get(k)]

    def is_configured(self, required: tuple[str, ...] = REQUIRED_SEARCH_SELECTORS) -> bool:
        return bool(self.base_url) and not self.missing_selectors(required)

    def _require(self, required: tuple[str, ...]) -> None:
        mancanti = self.missing_selectors(required)
        if not self.base_url:
            mancanti.append("base_url")
        if mancanti:
            raise AutomationNotConfiguredError("youtube", mancanti)

    # -- ciclo di vita --------------------------------------------------------------
    async def __aenter__(self) -> Self:
        try:
            from playwright.async_api import async_playwright
        except ImportError as exc:  # pragma: no cover - dipende dall'ambiente
            raise BrowserAutomationError(
                "Playwright non installato. Installa l'extra 'browser': "
                "pip install -e '.[browser]' && playwright install chromium"
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

    # -- operazioni -----------------------------------------------------------------
    async def search_videos(self, query: str, *, limit: int = 10) -> list[YouTubeSearchResult]:
        """Cerca video sulle pagine pubbliche di YouTube.

        Solleva ``AutomationNotConfiguredError`` se i selettori non sono stati forniti.
        """
        self._require(REQUIRED_SEARCH_SELECTORS)
        if self._context is None:
            raise BrowserAutomationError("Client non avviato: usare 'async with'.")

        page = await self._context.new_page()
        try:
            await page.goto(f"{self.base_url}/results?search_query={query}")
            await page.wait_for_selector(self.selectors["video_card"])
            cards = await page.query_selector_all(self.selectors["video_card"])

            risultati: list[YouTubeSearchResult] = []
            for card in cards[:limit]:
                titolo_el = await card.query_selector(self.selectors["title"])
                canale_el = await card.query_selector(self.selectors["channel"])
                views_el = await card.query_selector(self.selectors["views"])
                if not (titolo_el and canale_el and views_el):
                    continue  # dato incompleto: si scarta, non si completa a mano
                risultati.append(
                    YouTubeSearchResult(
                        title=(await titolo_el.inner_text()).strip(),
                        url=(await titolo_el.get_attribute("href")) or "",
                        channel=(await canale_el.inner_text()).strip(),
                        views_text=(await views_el.inner_text()).strip(),
                    )
                )
            return risultati
        except AutomationNotConfiguredError:
            raise
        except Exception as exc:
            raise BrowserAutomationError(f"Ricerca su YouTube fallita: {exc}") from exc
        finally:
            await page.close()

    async def fetch_transcript(self, video_id: str, video_url: str) -> TranscriptAsset:
        """Tenta il recupero del transcript dal flusso pubblico previsto.

        Se non e' configurato o non e' disponibile, restituisce un ``TranscriptAsset`` con
        ``available=False`` e una nota esplicativa. Non inventa mai il contenuto.
        """
        if self.missing_selectors(REQUIRED_TRANSCRIPT_SELECTORS):
            return TranscriptAsset(
                video_id=video_id,
                available=False,
                note=(
                    "Recupero non configurato: mancano i selettori "
                    f"{', '.join(self.missing_selectors(REQUIRED_TRANSCRIPT_SELECTORS))}."
                ),
            )
        if self._context is None:
            raise BrowserAutomationError("Client non avviato: usare 'async with'.")

        page = await self._context.new_page()
        try:
            await page.goto(video_url)
            bottone = await page.query_selector(self.selectors["transcript_button"])
            if bottone is None:
                return TranscriptAsset(
                    video_id=video_id,
                    available=False,
                    note="Transcript non offerto dalla pagina per questo video.",
                )
            await bottone.click()
            await page.wait_for_selector(self.selectors["transcript_segment"])
            segmenti = await page.query_selector_all(self.selectors["transcript_segment"])
            testo = " ".join([(await s.inner_text()).strip() for s in segmenti]).strip()
            if not testo:
                return TranscriptAsset(
                    video_id=video_id,
                    available=False,
                    note="Pannello transcript aperto ma vuoto.",
                )
            return TranscriptAsset(
                video_id=video_id,
                text=testo,
                available=True,
                note="Transcript recuperato dal flusso pubblico della pagina.",
            )
        except Exception as exc:
            logger.warning("Transcript non recuperato per %s: %s", video_id, exc)
            return TranscriptAsset(
                video_id=video_id,
                available=False,
                note=f"Recupero fallito: {exc}",
            )
        finally:
            await page.close()
