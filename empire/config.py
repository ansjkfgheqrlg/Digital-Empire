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

from .paths import config_data, repo_root

__all__ = ["MissingSecret", "get_secret", "has_secret", "env_keys", "setting"]


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
    """Segreto da ambiente, poi da .env. Errore azionabile se manca.

    Il VALORE non compare mai nel messaggio di errore.
    """
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
