"""Client Playwright: senza selettori configurati devono dichiararlo, non tentare.

Nessun test qui avvia un browser: si verifica solo il comportamento di configurazione.
"""

from __future__ import annotations

import pytest

from youtube_automation_factory.automation.arena_playwright import ArenaPlaywrightClient
from youtube_automation_factory.automation.youtube_playwright import (
    REQUIRED_SEARCH_SELECTORS,
    REQUIRED_TRANSCRIPT_SELECTORS,
    YouTubePlaywrightClient,
)
from youtube_automation_factory.core.exceptions import AutomationNotConfiguredError


def test_youtube_non_configurato_di_default() -> None:
    client = YouTubePlaywrightClient(base_url="https://www.youtube.com", selectors={})
    assert not client.is_configured()
    assert set(client.missing_selectors(REQUIRED_SEARCH_SELECTORS)) == set(
        REQUIRED_SEARCH_SELECTORS
    )


def test_youtube_search_senza_selettori_solleva() -> None:
    import asyncio

    client = YouTubePlaywrightClient(base_url="https://www.youtube.com", selectors={})
    with pytest.raises(AutomationNotConfiguredError) as exc:
        asyncio.run(client.search_videos("query"))
    assert "youtube" in str(exc.value)
    assert "video_card" in str(exc.value)


def test_youtube_transcript_senza_selettori_non_inventa_contenuto() -> None:
    import asyncio

    client = YouTubePlaywrightClient(base_url="https://www.youtube.com", selectors={})
    asset = asyncio.run(client.fetch_transcript("v1", "https://example.invalid/watch?v=v1"))
    assert asset.available is False
    assert asset.text is None
    assert "non configurato" in asset.note
    for chiave in REQUIRED_TRANSCRIPT_SELECTORS:
        assert chiave in asset.note


def test_arena_non_configurata_di_default() -> None:
    client = ArenaPlaywrightClient(base_url="", selectors={})
    assert not client.is_configured()
    assert "base_url" in client.missing_config()


def test_arena_generate_senza_configurazione_solleva() -> None:
    import asyncio

    client = ArenaPlaywrightClient(base_url="", selectors={})
    with pytest.raises(AutomationNotConfiguredError):
        asyncio.run(client.generate_thumbnail("brief"))


def test_thumbnail_agent_non_finge_la_generazione(niche: str, run, script) -> None:
    import asyncio

    from youtube_automation_factory.agents import ThumbnailAgent

    agente = ThumbnailAgent("thumb-1", niche)
    thumbnail = agente.draft_thumbnail(workflow_id=run.id, script=script)
    client = ArenaPlaywrightClient(base_url="", selectors={})
    risultato, nota = asyncio.run(agente.try_generate(thumbnail, client))
    assert risultato.generated is False
    assert risultato.image_path is None
    assert "non configurata" in nota
    assert risultato.brief, "il brief resta valido anche senza generazione"


def test_settings_ignora_selettori_non_json(monkeypatch) -> None:
    from config.settings import Settings

    monkeypatch.setenv("YAF_YOUTUBE_SELECTORS", "non-json")
    s = Settings()
    assert s.youtube_selectors == {}
    assert not s.youtube_is_configured()


def test_settings_legge_selettori_json(monkeypatch) -> None:
    from config.settings import Settings

    monkeypatch.setenv(
        "YAF_YOUTUBE_SELECTORS",
        '{"video_card": "a", "title": "b", "channel": "c", "views": "d"}',
    )
    s = Settings()
    assert s.youtube_is_configured()


def test_flik_non_reale_di_default() -> None:
    from config.settings import Settings

    assert Settings().flik_is_real() is False
