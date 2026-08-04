"""
common.py — Infrastruttura condivisa di AnnuncioForge (regia, Half A / Max).

Fornisce: caricamento config da .env, creazione cartella di run, logging,
stato (state.json), trace (trace.jsonl), helper JSON e validazione schema.

Nessuna dipendenza esterna obbligatoria oltre `jsonschema` (validazione) e,
opzionale, `python-dotenv` (se assente, legge comunque le variabili d'ambiente).
"""
from __future__ import annotations

import json
import logging
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Radice del progetto = cartella che contiene questo file salendo di 1 (implementation/ -> progetto)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = PROJECT_ROOT / "schema"
RUNS_DIR = PROJECT_ROOT / "runs"
LOGS_DIR = PROJECT_ROOT / "logs"


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
def load_config() -> dict[str, Any]:
    """Carica configurazione da .env (se presente) con default sensati."""
    env_path = PROJECT_ROOT / ".env"
    try:
        from dotenv import load_dotenv  # type: ignore

        if env_path.exists():
            load_dotenv(env_path)
    except ImportError:
        # python-dotenv non installato: si usano comunque le env var di sistema.
        pass

    def _get(key: str, default: str) -> str:
        val = os.environ.get(key)
        return val if val not in (None, "") else default

    return {
        "browser_profile_dir": _get("BROWSER_PROFILE_DIR", str(PROJECT_ROOT / "browser-profile")),
        "headless": _get("PLAYWRIGHT_HEADLESS", "true").strip().lower() in ("1", "true", "yes"),
        "nav_timeout_ms": int(_get("NAV_TIMEOUT_MS", "45000")),
        "user_agent": _get("USER_AGENT", "").strip(),
        "locale": _get("LOCALE", "de-DE"),
        "price_surcharge_pct": float(_get("PRICE_SURCHARGE_PCT", "3")),
        "price_fixed_1": float(_get("PRICE_FIXED_1", "1500")),
        "price_fixed_2": float(_get("PRICE_FIXED_2", "1500")),
    }


# --------------------------------------------------------------------------- #
# Run context
# --------------------------------------------------------------------------- #
def slugify(text: str, maxlen: int = 60) -> str:
    text = (text or "").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:maxlen] or "annuncio"


def source_id_from_url(url: str) -> str:
    """Estrae l'ID numerico dell'annuncio mobile.de dalla URL, se presente."""
    m = re.search(r"/(\d{6,})(?:[/?.]|$)", url or "")
    if m:
        return m.group(1)
    m = re.search(r"(\d{6,})", url or "")
    return m.group(1) if m else "noid"


class RunContext:
    """Cartella e stato di un singolo run della pipeline."""

    def __init__(self, source_url: str, run_id: str | None = None):
        self.source_url = source_url
        sid = source_id_from_url(source_url)
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.run_id = run_id or f"AF-{ts}-{sid}"
        self.dir = RUNS_DIR / self.run_id
        self.foto_dir = self.dir / "foto"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.foto_dir.mkdir(parents=True, exist_ok=True)
        LOGS_DIR.mkdir(parents=True, exist_ok=True)

        self.raw_path = self.dir / "raw.json"
        self.listing_path = self.dir / "listing.json"
        self.listing_it_path = self.dir / "listing_it.json"
        self.state_path = self.dir / "state.json"
        self.trace_path = self.dir / "trace.jsonl"

        self.logger = _make_logger(self.run_id)
        self.state: dict[str, Any] = {
            "run_id": self.run_id,
            "source_url": source_url,
            "created_at": _now_iso(),
            "steps": {},  # step -> {status, at, note}
        }
        self._save_state()
        self.trace("run_created", {"source_url": source_url})

    # -- stato ---------------------------------------------------------------
    def set_step(self, step: str, status: str, note: str = "") -> None:
        self.state["steps"][step] = {"status": status, "at": _now_iso(), "note": note}
        self._save_state()
        self.trace("step", {"step": step, "status": status, "note": note})
        level = logging.ERROR if status in ("failed", "blocked") else logging.INFO
        self.logger.log(level, "STEP %s -> %s %s", step, status, f"({note})" if note else "")

    def _save_state(self) -> None:
        save_json(self.state_path, self.state)

    # -- trace ---------------------------------------------------------------
    def trace(self, event: str, data: dict[str, Any] | None = None) -> None:
        rec = {"ts": _now_iso(), "event": event, **(data or {})}
        with self.trace_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _make_logger(run_id: str) -> logging.Logger:
    logger = logging.getLogger(f"annuncioforge.{run_id}")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(LOGS_DIR / f"{run_id}.log", encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger


# --------------------------------------------------------------------------- #
# JSON helpers + schema
# --------------------------------------------------------------------------- #
def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def save_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_against_schema(obj: Any, schema_name: str) -> list[str]:
    """Valida `obj` contro schema/<schema_name>. Ritorna lista errori (vuota = ok)."""
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return ["jsonschema non installato: validazione saltata (pip install jsonschema)"]
    schema = load_json(SCHEMA_DIR / schema_name)
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(obj), key=lambda e: list(e.path))
    return [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}" for e in errors]
