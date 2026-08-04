"""Configurazione applicativa.

I valori arrivano da variabili d'ambiente (prefisso ``YAF_``) o da un file ``.env`` locale,
mai da costanti scritte nel codice. Nessun segreto e' versionato: ``.env`` e' in ``.gitignore``
e ``.env.example`` contiene solo il template.
"""

from __future__ import annotations

import json
import logging
from functools import lru_cache
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

#: Nicchia operativa primaria. E' protetta: nessun agente operativo, revisore o di produzione
#: puo' modificarla a runtime. Solo il livello senior puo' *proporre* un cambio per workflow
#: futuri (vedi ``ProfitableNicheAgent`` e ``docs/niche_research.md``).
PRIMARY_NICHE = "Dose Mentale"


class Settings(BaseSettings):
    """Impostazioni caricate dall'ambiente."""

    model_config = SettingsConfigDict(
        env_prefix="YAF_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    primary_niche: str = PRIMARY_NICHE
    reports_dir: Path = Path("reports")

    browser_headless: bool = True
    browser_timeout_ms: int = Field(default=30_000, ge=1_000, le=300_000)
    browser_profile_dir: str = ""

    youtube_base_url: str = "https://www.youtube.com"
    youtube_selectors: dict[str, str] = Field(default_factory=dict)

    arena_base_url: str = ""
    arena_selectors: dict[str, str] = Field(default_factory=dict)

    flik_adapter: str = "mock"

    @field_validator("youtube_selectors", "arena_selectors", mode="before")
    @classmethod
    def _parse_selectors(cls, value: object) -> object:
        """Accetta un JSON dall'ambiente; una stringa vuota significa "non configurato".

        I selettori non hanno default: inventarli produrrebbe dati falsi al primo cambio di
        layout della piattaforma. Se mancano, i client Playwright lo dichiarano apertamente
        invece di tentare comunque.
        """
        if value in (None, ""):
            return {}
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError:
                logger.warning("Selettori ignorati: il valore non e' JSON valido.")
                return {}
            return parsed if isinstance(parsed, dict) else {}
        return value

    @property
    def reports_path(self) -> Path:
        """Percorso assoluto della cartella report, creata se assente."""
        path = self.reports_dir
        if not path.is_absolute():
            path = PROJECT_ROOT / path
        path.mkdir(parents=True, exist_ok=True)
        return path

    def youtube_is_configured(self) -> bool:
        return bool(self.youtube_base_url and self.youtube_selectors)

    def arena_is_configured(self) -> bool:
        return bool(self.arena_base_url and self.arena_selectors)

    def flik_is_real(self) -> bool:
        """``True`` solo se e' stato configurato un adapter diverso dal mock locale."""
        return self.flik_adapter.strip().lower() not in ("", "mock")


@lru_cache
def get_settings() -> Settings:
    """Istanza condivisa (cache) delle impostazioni."""
    return Settings()
