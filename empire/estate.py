"""
EMPIRE — verdetto unico sul Workflow Estate: `python -m empire estate`.

Owner: Claude · Origine: FORGE (LOTTO 6 completamento Workflow Estate, CP-20260723)
Piano: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/PIANO-COMPLETAMENTO-L3.md §2

## Perché un comando solo

Il piano di livello 2 aveva dieci "definizioni di finito", una per lavoro, ognuna con il suo
comando. Erano tutte corrette e nessuno le avrebbe mai rieseguite tutte insieme: una verifica
che richiede dieci comandi ricordati a memoria, in pratica, non viene fatta. Da lì nasce la
condizione che ha bloccato questa settimana — la dashboard mostrava Gate-FUNNEL verde mentre
il file conteneva ancora `YOUR_STRIPE`, e nessuno aveva un modo rapido di accorgersene.

Questo comando è quel modo rapido. Una riga per controllo, un exit code solo.

## Cosa conta come "finito"

Un gate ROSSO non è automaticamente un fallimento del piano: il piano prevede rossi e per
ognuno prescrive una contromossa (`on_red`). Un rosso la cui contromossa è stata eseguita e
registrata (`flow gate <id> --applied-on-red`) è **risolto**. Un rosso ignorato no.
Un gate in attesa (PENDING) vale rosso: "nessun gate quasi verde" (WF-MASTER §3).

Il verdetto non rende mai verde niente da solo: legge e riferisce.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from .paths import repo_root

__all__ = ["Check", "run_checks", "register"]

# Pagine che devono poter incassare: un placeholder qui significa un funnel morto.
_SALES_GLOBS = ("Crea siti/Siti CCM/*.html", "Crea siti/Preventa/*.html")
_PAYMENT_PLACEHOLDERS = ("YOUR_STRIPE", "YOUR_PAYPAL", "INSERISCI_LINK", "TODO_CHECKOUT")

# Artefatti promessi dal piano. La chiave e' la descrizione leggibile, il valore un glob.
_PROMISED = {
    "case study Novacar": "Clienti/Prof Autocad/preventa-launch-kit/07_CASE_STUDY_NOVACAR.*",
    "landing Preventa": "Crea siti/Preventa/index.html",
    "pacchetto video S5": "WORKFLOW-ESTATE/07-VIDEO-RUN/*/05-STATO.md",
    "checkout configurabile": "Crea siti/Siti CCM/checkout.config.json",
}


@dataclass(slots=True)
class Check:
    name: str
    ok: bool
    detail: str
    blocking: bool = True
    notes: list[str] = field(default_factory=list)


def _check_gates() -> list[Check]:
    try:
        from .flow import runner as _runner
    except ImportError as e:
        return [Check("gate", False, f"motore flow non caricabile: {e}")]

    out: list[Check] = []
    try:
        results = _runner.gates_table()
    except Exception as e:  # noqa: BLE001 — un file di config rotto non deve far esplodere il verdetto
        return [Check("gate", False, f"valutazione gate fallita: {e}")]

    for r in results:
        if r.status == "GREEN":
            out.append(Check(f"gate {r.id}", True, "verde"))
        elif r.status == "RED" and r.on_red_applied:
            out.append(Check(f"gate {r.id}", True,
                             f"rosso PREVISTO, contromossa applicata ({r.on_red})"))
        elif r.status == "RED":
            out.append(Check(f"gate {r.id}", False,
                             f"rosso, contromossa NON applicata: {r.on_red or 'nessuna prevista'}"))
        else:
            out.append(Check(f"gate {r.id}", False, "in attesa (vale rosso: nessun gate quasi verde)"))
        if r.evidence:
            out[-1].notes.append(r.evidence)
    return out


def _check_placeholders() -> Check:
    root = repo_root()
    hits: list[str] = []
    for pattern in _SALES_GLOBS:
        for p in root.glob(pattern):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for ph in _PAYMENT_PLACEHOLDERS:
                if ph in text:
                    hits.append(f"{p.relative_to(root)} -> {ph}")
    if hits:
        return Check("pagine di vendita senza placeholder", False,
                     f"{len(hits)} placeholder di pagamento residui", notes=hits[:10])
    return Check("pagine di vendita senza placeholder", True, "nessun placeholder di pagamento")


def _check_promised() -> list[Check]:
    root = repo_root()
    out = []
    for label, pattern in _PROMISED.items():
        found = sorted(root.glob(pattern))
        if found:
            out.append(Check(f"artefatto: {label}", True,
                             f"{len(found)} file ({found[0].relative_to(root)})"))
        else:
            out.append(Check(f"artefatto: {label}", False, f"non trovato ({pattern})"))
    return out


def _check_conform() -> Check:
    try:
        from . import conform as _conform
    except ImportError as e:
        return Check("conform WORKFLOW-ESTATE", False, f"modulo conform non caricabile: {e}")
    try:
        findings = _conform.run("WORKFLOW-ESTATE")
    except Exception as e:  # noqa: BLE001
        return Check("conform WORKFLOW-ESTATE", False, f"esecuzione fallita: {e}")
    blocks = [f for f in findings if getattr(f, "severity", "") == "block"]
    warns = [f for f in findings if getattr(f, "severity", "") == "warn"]
    ok = not blocks
    return Check("conform WORKFLOW-ESTATE", ok,
                 f"block: {len(blocks)}  warn: {len(warns)}",
                 notes=[str(f) for f in blocks[:5]])


def _check_inspect() -> Check:
    try:
        from . import inspect as _inspect
    except ImportError:
        return Check("telemetria misurata", False,
                     "modulo inspect assente: i KPI di telemetria restano non misurati")
    try:
        st = _inspect.status()
    except Exception as e:  # noqa: BLE001
        return Check("telemetria misurata", False, f"inspect.status() fallito: {e}")
    bad = []
    values = st.values() if isinstance(st, dict) else []
    for m in values:
        note = str(m.get("note", "")) if isinstance(m, dict) else ""
        if "non implementat" in note.lower():
            bad.append(note)
    if bad:
        return Check("telemetria misurata", False, "KPI ancora dichiarati non implementati", notes=bad[:5])
    return Check("telemetria misurata", True, f"{len(values)} metriche esposte")


def run_checks() -> list[Check]:
    checks: list[Check] = []
    checks.extend(_check_gates())
    checks.append(_check_placeholders())
    checks.extend(_check_promised())
    checks.append(_check_conform())
    checks.append(_check_inspect())
    return checks


def _cmd_estate(a) -> int:
    checks = run_checks()
    failed = [c for c in checks if c.blocking and not c.ok]

    if getattr(a, "json", False):
        print(json.dumps([{"name": c.name, "ok": c.ok, "detail": c.detail,
                           "notes": c.notes} for c in checks], indent=2, ensure_ascii=False))
        return 1 if failed else 0

    print("VERDETTO WORKFLOW ESTATE")
    print("=" * 72)
    for c in checks:
        print(f"{'OK  ' if c.ok else 'NO  '} {c.name:44} {c.detail}")
        if getattr(a, "verbose", False):
            for n in c.notes:
                print(f"       - {n}")
    print("=" * 72)
    if failed:
        print(f"NON FINITO: {len(failed)} controlli su {len(checks)} non passano.")
        print("Dettaglio con --verbose. Le voci che dipendono da Max sono in")
        print("WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/AZIONI-MAX.md")
        return 1
    print(f"FINITO: {len(checks)} controlli su {len(checks)} passano.")
    return 0


def register(sub) -> None:
    """Registrato dal loop di plugin tramite empire.flow.cli.

    `empire/cli.py` e' un file congelato (nessun lotto lo modifica, per non creare
    collisioni di merge tra sessioni parallele) e la sua tupla `_PLUGIN_MODULES` non
    contiene `empire.estate`. Il loop passa pero' i subparser di primo livello a ogni
    plugin, quindi un modulo gia' registrato puo' aggiungere questo comando senza che
    nessuno tocchi il file congelato.
    """
    p = sub.add_parser("estate", help="verdetto unico sul Workflow Estate (exit 0 = finito)")
    p.add_argument("--json", action="store_true")
    p.add_argument("--verbose", "-v", action="store_true", help="mostra le note di ogni controllo")
    p.set_defaults(fn=_cmd_estate)
