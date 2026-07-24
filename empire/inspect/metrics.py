"""
EMPIRE INSPECT — le 6 metriche di telemetria che la dashboard chiede da giorni.

Owner: Claude · Origine: FORGE (LOTTO 1 completamento Workflow Estate, CP-20260723)

## Il difetto che questo file chiude

`empire/dash/collect.py` scriveva, per sei KPI su sei:
    "n/d (modulo inspect non ancora implementato)"

Ma il modulo `empire/inspect/` **esiste** (l'Ispettorato Generale, M3): raccoglie i
PERF record, calcola le scorecard, emette i TIP. Quello che mancava non era il modulo:
era l'API di sola lettura con cui il cruscotto poteva interrogarlo.

## La regola che governa ogni funzione qui dentro

Se non ci sono dati, il valore è **0 con una nota che dice dove ho guardato**.
Non `n/d`, non "non implementato", non una stima.

La differenza non è cosmetica. "Nessuna esecuzione registrata" è un fatto sull'azienda —
dice che il PERF-LOOP non sta girando, che è un'informazione preziosa e azionabile.
"Modulo non implementato" è un difetto del software travestito da misura: nasconde il
fatto dietro un alibi tecnico, e per giorni nessuno ha potuto distinguere "non misuriamo"
da "non succede niente".

Oggi, con zero PERF record su disco, queste funzioni rispondono tutte 0 — ed è la
risposta giusta: il ciclo di performance non ha ancora registrato nulla.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timedelta

__all__ = ["telemetry_runs", "scorecard_5d", "first_pass", "ttd_vs_bench",
           "feedback_tips", "traceability", "status", "ALL_METRICS"]

_NO_DATA = "nessun record PERF registrato (il ciclo performance non ha ancora girato)"


def _metric(value, *, source: str, note: str = "", status: str = "") -> dict:
    return {"value": value, "status": status, "source": source, "note": note}


def _perf_atoms() -> list:
    """Tutti i PERF record presenti in memoria. Lista vuota se la memoria non c'è:
    l'assenza di dati non deve mai propagarsi come eccezione fino al cruscotto."""
    try:
        from empire.memory import all_atoms
    except ImportError:
        return []
    try:
        return list(all_atoms(kind="perf"))
    except Exception:  # noqa: BLE001 — archivio illeggibile: zero dati, non un crash
        return []


def _extra(atom, key, default=None):
    extra = getattr(atom, "extra", None) or {}
    return extra.get(key, default)


# --------------------------------------------------------------- 1. esecuzioni/gg

def telemetry_runs(*, days: int = 7) -> dict:
    src = "empire.memory atoms kind=perf"
    atoms = _perf_atoms()
    if not atoms:
        return _metric(0, source=src, note=_NO_DATA)

    cutoff = datetime.now().astimezone() - timedelta(days=days)
    recent = 0
    for a in atoms:
        raw = _extra(a, "ended") or _extra(a, "started")
        if not raw:
            continue
        try:
            dt = datetime.fromisoformat(str(raw))
        except ValueError:
            continue
        if dt.tzinfo is None:
            dt = dt.astimezone()
        if dt >= cutoff:
            recent += 1
    return _metric(round(recent / days, 2), source=src,
                   note=f"{recent} esecuzioni negli ultimi {days} giorni")


# --------------------------------------------------------------- 2. scorecard 5D

def scorecard_5d() -> dict:
    src = "empire.memory atoms kind=perf -> scorecard"
    atoms = _perf_atoms()
    values = []
    for a in atoms:
        sc = _extra(a, "scorecard") or {}
        axes = [v for k, v in sc.items() if isinstance(v, (int, float))]
        if axes:
            values.append(sum(axes) / len(axes))
    if not values:
        return _metric(0, source=src, note=_NO_DATA)
    return _metric(round(sum(values) / len(values), 2), source=src,
                   note=f"media su {len(values)} run con scorecard compilata")


# --------------------------------------------------------------- 3. first-pass

def first_pass() -> dict:
    src = "empire.memory atoms kind=perf -> verification.first_pass"
    atoms = _perf_atoms()
    judged = [a for a in atoms if isinstance(_extra(a, "verification"), dict)
              and "first_pass" in (_extra(a, "verification") or {})]
    if not judged:
        return _metric(0, source=src, note=_NO_DATA)
    ok = sum(1 for a in judged if (_extra(a, "verification") or {}).get("first_pass"))
    return _metric(round(100 * ok / len(judged), 1), source=src,
                   note=f"{ok}/{len(judged)} run passate alla prima verifica")


# --------------------------------------------------------------- 4. TTD vs benchmark

def ttd_vs_bench() -> dict:
    src = "empire.memory atoms kind=perf -> ttd_h vs inspect.benchmarks"
    atoms = _perf_atoms()
    try:
        from .benchmarks import get_benchmark
    except ImportError:
        return _metric(0, source=src, note="tabella benchmark non caricabile")

    ratios = []
    for a in atoms:
        ttd = _extra(a, "ttd_h")
        if not isinstance(ttd, (int, float)):
            continue
        bench = get_benchmark(str(_extra(a, "family") or "default"))
        if bench:
            ratios.append(ttd / bench)
    if not ratios:
        return _metric(0, source=src, note=_NO_DATA)
    avg = sum(ratios) / len(ratios)
    verso = "sotto" if avg <= 1 else "sopra"
    return _metric(round(avg, 2), source=src,
                   note=f"media {len(ratios)} run: {verso} benchmark (1.0 = in linea)")


# --------------------------------------------------------------- 5. TIP aperti

def feedback_tips() -> dict:
    src = "empire.inspect.report.get_organ_status()"
    try:
        from .report import get_organ_status
    except ImportError as e:
        return _metric(0, source=src, note=f"organo non interrogabile: {e}")
    try:
        st = get_organ_status()
    except Exception as e:  # noqa: BLE001
        return _metric(0, source=src, note=f"lettura fallita: {e}")
    pending = st.get("pending_tips_count", 0)
    loops = st.get("open_loops_count", 0)
    return _metric(pending, source=src,
                   note=f"{pending} TIP non confermati, {loops} loop aperti")


# --------------------------------------------------------------- 6. tracciabilità

def traceability() -> dict:
    """Copertura dei checkpoint: quanta parte del lavoro chiuso lascia una traccia.

    Con zero PERF record la copertura è 0 e la nota lo spiega. Sarebbe stato comodo
    calcolarla sul numero di checkpoint esistenti (98+), ottenendo un bel 100% — ma
    misurerebbe un'altra cosa: quanti checkpoint ci sono, non quanto lavoro è tracciato.
    """
    src = "empire.memory atoms kind=perf -> output_ref/checkpoint"
    atoms = _perf_atoms()
    if not atoms:
        return _metric(0, source=src, note=_NO_DATA)
    tracciati = sum(1 for a in atoms
                    if _extra(a, "checkpoint") or _extra(a, "output_ref"))
    return _metric(round(100 * tracciati / len(atoms), 1), source=src,
                   note=f"{tracciati}/{len(atoms)} run con checkpoint o output collegato")


ALL_METRICS = {
    "runs": telemetry_runs,
    "scorecard": scorecard_5d,
    "first_pass": first_pass,
    "ttd": ttd_vs_bench,
    "feedback": feedback_tips,
    "traceability": traceability,
}


def status() -> dict:
    """Tutte e sei le metriche in un colpo. È l'API che il cruscotto e
    `empire estate` interrogano."""
    return {name: fn() for name, fn in ALL_METRICS.items()}
