"""
EMPIRE — configurazione e segreti.

Owner: Max · Controllore: Claude · Origine: FORGE (seed CP-20260722-003)
Governo: MANDATO Art.7 (supply-chain/segreti) + ADR-008

FILE CONGELATO — fondazione condivisa. Modifiche con nota di coordinamento.

Regola assoluta: un segreto non viene MAI stampato, loggato o scritto su file.
Neanche parzialmente, neanche in debug.
"""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any
import yaml

from .paths import config_data, repo_root

__all__ = ["MissingSecret", "get_secret", "has_secret", "env_keys", "setting", "Settings", "get_settings"]

class MissingSecret(RuntimeError):
    """Segreto richiesto e non presente in .env né in ambiente."""

@lru_cache(maxsize=1)
def _dotenv() -> dict[str, str]:
    """Parser minimale di .env alla radice. Nessuna dipendenza esterna."""
    out: dict[str, str] = {}
    p = repo_root() / ".env"
    if not p.exists():
        return out
    with open(p, encoding="utf-8", errors="replace") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            val = val.strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            out[key.strip()] = val
    return out

def has_secret(name: str) -> bool:
    return bool(os.environ.get(name) or _dotenv().get(name))

def get_secret(name: str, *, required: bool = True) -> str | None:
    """Segreto da ambiente, poi da .env. Errore azionabile se manca."""
    val = os.environ.get(name) or _dotenv().get(name)
    if val:
        return val
    if not required:
        return None
    raise MissingSecret(
        f"Manca il segreto {name!r}.\n"
        f"  aggiungilo a: {repo_root() / '.env'}  (riga: {name}=...)\n"
        "  oppure impostalo come variabile d'ambiente.\n"
        "  Il file .env non va mai committato."
    )

def env_keys() -> list[str]:
    """Solo i NOMI delle chiavi presenti. Mai i valori."""
    return sorted(set(_dotenv()) | {k for k in os.environ if k.startswith("EMPIRE_")})

def setting(section: str, key: str, default=None):
    """Valore da empire.toml."""
    return config_data().get(section, {}).get(key, default)

def data_dir(*parts: str) -> Path:
    """Cartella dati locale (cache, indici, stato). Non versionata."""
    d = repo_root() / "empire" / ".data"
    d = d.joinpath(*parts) if parts else d
    d.mkdir(parents=True, exist_ok=True)
    return d

@dataclass(frozen=True, slots=True)
class Settings:
    """Configurazione immutabile dell'OS."""
    # API
    anthropic_api_key: str | None = field(default_factory=lambda: os.getenv("ANTHROPIC_API_KEY"))
    default_model: str = "claude-3-5-sonnet-20241022"
    
    # Paths
    project_root: Path = field(default_factory=lambda: Path.cwd())
    agents_dir: Path = field(default_factory=lambda: Path.cwd() / "agents")
    workspace_dir: Path = field(default_factory=lambda: Path.cwd() / "workspace_scripts")
    data_dir: Path = field(default_factory=lambda: Path.cwd() / "data")
    db_path: Path = field(default_factory=lambda: Path.cwd() / "data" / "empire.db")
    
    # Memory
    max_history: int = 10
    max_tool_iterations: int = 5
    enable_persistence: bool = True
    
    # Security
    sandbox_enabled: bool = True
    allowed_script_extensions: tuple[str, ...] = (".py", ".sh")
    max_tool_output_chars: int = 8000
    shell_timeout: int = 15
    
    # Runtime
    log_level: str = "INFO"
    api_host: str = "127.0.0.1"
    api_port: int = 8000

    def ensure_dirs(self) -> None:
        self.agents_dir.mkdir(parents=True, exist_ok=True)
        self.workspace_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

def load_yaml_config(path: Path | str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {}
    try:
        data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}

_settings_cache: Settings | None = None

def get_settings(force_reload: bool = False) -> Settings:
    global _settings_cache
    if _settings_cache and not force_reload:
        return _settings_cache
    
    yaml_cfg = load_yaml_config(Path.cwd() / "empire.yaml")
    
    settings = Settings(
        default_model=yaml_cfg.get("default_model", "claude-3-5-sonnet-20241022"),
        max_history=int(yaml_cfg.get("max_history", 10)),
        max_tool_iterations=int(yaml_cfg.get("max_tool_iterations", 5)),
        log_level=yaml_cfg.get("log_level", "INFO"),
    )
    settings.ensure_dirs()
    _settings_cache = settings
    return settings
