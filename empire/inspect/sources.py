"""
EMPIRE INSPECT — sources.py (connettori ai dati reali su disco).

Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008

## Perché questo file esiste

L'ARCHITETTURA-COMPLETAMENTO.md (§2.1) prevede esplicitamente un modulo `sources.py`
che documenti *da dove vengono i numeri*: le directory di sorgente che questo
pacchetto interroga. Il contratto è semplice:

    ogni funzione qui ritorna dati o una lista vuota — mai eccezioni che crashano il cruscotto.

Le sorgenti canoniche sono:
    - 02-AUTOMAZIONI-E-SCRIPTS/performances/   (PERF record scritti da WF-PERF-LOOP)
    - 02-AUTOMAZIONI-E-SCRIPTS/feedback/       (TIP e feedback aperti)
    - 02-AUTOMAZIONI-E-SCRIPTS/sessions/       (log di sessione)
    - 02-AUTOMAZIONI-E-SCRIPTS/checkpoints/    (checkpoint atomici)
    - 06-DASHBOARD-E-METRICHE/lead.csv         (lead commerciali)
    - empire/.data/flow/facts.json             (fatti correnti dei gate)

Queste path sono risolte tramite `empire.paths` e mai hardcoded: se il repo
viene spostato, le sorgenti si trovano lo stesso.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

__all__ = [
    "performances_dir",
    "feedback_dir",
    "sessions_dir",
    "checkpoints_dir",
    "lead_csv_path",
    "facts_json_path",
    "get_csv_rows",
    "count_files",
    "load_json_safe",
    "source_summary",
]


# ---------------------------------------------------------------------------
# Path resolver (lazy: importa empire.paths solo se disponibile)
# ---------------------------------------------------------------------------

def _root() -> Path:
    """Radice del monorepo. Usa empire.paths se disponibile, fallback sicuro."""
    try:
        from empire import paths  # noqa: PLC0415
        return paths.repo_root()
    except Exception:  # pragma: no cover
        # Fallback: empire/inspect/sources.py → inspect → empire → monorepo
        return Path(__file__).resolve().parents[2]


def _automazioni() -> Path:
    """Cartella 02-AUTOMAZIONI-E-SCRIPTS nel ramo WORKFLOW-ESTATE."""
    return _root() / "WORKFLOW-ESTATE" / "02-AUTOMAZIONI-E-SCRIPTS"


# ---------------------------------------------------------------------------
# Path pubbliche (leggibili dall'esterno senza chiamare il costruttore)
# ---------------------------------------------------------------------------

def performances_dir() -> Path:
    """Directory dei PERF record scritti da WF-PERF-LOOP."""
    return _automazioni() / "performances"


def feedback_dir() -> Path:
    """Directory dei TIP/feedback aperti."""
    return _automazioni() / "feedback"


def sessions_dir() -> Path:
    """Directory dei log di sessione."""
    return _automazioni() / "sessions"


def checkpoints_dir() -> Path:
    """Directory dei checkpoint atomici."""
    return _automazioni() / "checkpoints"


def lead_csv_path() -> Path:
    """Path del file lead.csv della dashboard commerciale."""
    return _root() / "WORKFLOW-ESTATE" / "06-DASHBOARD-E-METRICHE" / "lead.csv"


def facts_json_path() -> Path:
    """Path dei fatti correnti del motore gate."""
    return _root() / "empire" / ".data" / "flow" / "facts.json"


# ---------------------------------------------------------------------------
# Helper corazzati contro file mancanti
# ---------------------------------------------------------------------------

def get_csv_rows(path: Path, *, encoding: str = "utf-8") -> list[dict[str, str]]:
    """
    Legge un CSV e ritorna le righe come lista di dizionari.
    Se il file non esiste o è illeggibile ritorna [] senza eccezioni.

    Args:
        path: Path assoluto al file CSV.
        encoding: Encoding da usare (default utf-8).

    Returns:
        Lista di dict {colonna: valore}. Vuota se il file manca o è corrotto.
    """
    if not path.is_file():
        return []
    try:
        with open(path, encoding=encoding, newline="") as fh:
            return list(csv.DictReader(fh))
    except Exception:  # noqa: BLE001
        return []


def count_files(directory: Path, *, glob: str = "*") -> int:
    """
    Conta i file (non directory) in `directory` che corrispondono al pattern `glob`.
    Ritorna 0 se la directory non esiste — mai eccezioni.

    Args:
        directory: Path della directory da contare.
        glob: Pattern glob (default "*" = tutti i file).

    Returns:
        Numero intero di file trovati. 0 se directory mancante.
    """
    if not directory.is_dir():
        return 0
    try:
        return sum(1 for p in directory.glob(glob) if p.is_file())
    except Exception:  # noqa: BLE001
        return 0


def load_json_safe(path: Path) -> Any:
    """
    Legge e deserializza un file JSON. Ritorna None se il file manca o è
    invalido — mai eccezioni propagate al chiamante.

    Args:
        path: Path assoluto al file JSON.

    Returns:
        Oggetto Python deserializzato, oppure None.
    """
    if not path.is_file():
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:  # noqa: BLE001
        return None


# ---------------------------------------------------------------------------
# Riepilogo sorgenti (utile per debug e per la CLI)
# ---------------------------------------------------------------------------

def source_summary() -> dict[str, dict[str, Any]]:
    """
    Ritorna un dizionario con lo stato di tutte le sorgenti canoniche:
    se la directory/file esiste, quanti elementi contiene, path assoluta.

    Usato da `empire inspect sources` nella CLI e da `empire estate --verbose`.

    Returns:
        Dict {nome_sorgente: {path, exists, count_or_size}}
    """
    dirs = {
        "performances": performances_dir(),
        "feedback":     feedback_dir(),
        "sessions":     sessions_dir(),
        "checkpoints":  checkpoints_dir(),
    }
    files = {
        "lead_csv":   lead_csv_path(),
        "facts_json": facts_json_path(),
    }

    result: dict[str, dict[str, Any]] = {}

    for name, d in dirs.items():
        exists = d.is_dir()
        result[name] = {
            "path":   str(d),
            "exists": exists,
            "files":  count_files(d) if exists else 0,
        }

    for name, f in files.items():
        exists = f.is_file()
        result[name] = {
            "path":   str(f),
            "exists": exists,
            "size_bytes": f.stat().st_size if exists else 0,
        }

    return result
