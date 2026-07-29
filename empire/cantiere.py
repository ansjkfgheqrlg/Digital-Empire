"""
EMPIRE — cantiere: `python -m empire cantiere`.

Owner: Claude · Origine: FORGE (presa di costruzione empire-wide, CP-20260729-002)

## Cosa fa (e come si distingue da `controllo`)

`empire controllo` risponde a "questo workflow e' pronto a SPEDIRE adesso?" (porta d'uscita:
sessione loggata, incasso, ecc.). `empire cantiere` risponde all'altra meta': "questo modello
operativo e' pronto a essere COSTRUITO/finito, e qual e' il prossimo passo?".

E' la presa del cervello (WORKFLOW-ESTATE) sui modelli operativi. Non li osserva soltanto: legge
il loro avanzamento reale (taskboard condiviso + STATO-RIPRESA) e dice, per ognuno, il prossimo
passo di costruzione, chi lo possiede, se e' bloccato, e se il codice che dice di avere esiste
davvero sul disco (check reale, non una promessa).

## Da dove legge (nessun dato inventato)

  - REGISTRO   WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/MODELLI-OPERATIVI.json  (quali modelli governa)
  - AVANZAMENTO EmpireDesk/state/taskboard.json                          (task fatti / da fare)
  - RIPRESA    <path>/STATO-RIPRESA.md per-modello, se dichiarato        (prossimo passo scritto)

Ogni modello dichiara `task_prefissi`: i suoi task nel taskboard sono quelli il cui id inizia con
uno di quei prefissi. Cosi' il progresso e' misurato sui fatti (stato == "fatto"), non stimato.

## Onesta'

Se l'entrypoint dichiarato nel registro non esiste sul disco, il comando lo segnala ASSENTE invece
di far finta. Se un modello e' bloccato da un atto di Max (soldi, login, 'via'), lo dice a chiare
lettere: il cervello puo' guidare la costruzione, non puo' firmare al posto di Max.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .paths import repo_root, safe_stdout

__all__ = ["stato_cantiere", "register"]

_RESET = "=" * 74
_REGISTRO = "WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/MODELLI-OPERATIVI.json"
_TASKBOARD = "EmpireDesk/state/taskboard.json"
_DASHBOARD = "WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/CANTIERE.md"


def _carica_registro() -> list[dict]:
    p = repo_root() / _REGISTRO
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("modelli", [])
    except (json.JSONDecodeError, OSError):
        return []


def _carica_task() -> list[dict]:
    p = repo_root() / _TASKBOARD
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("tasks", [])
    except (json.JSONDecodeError, OSError):
        return []


def _task_del_modello(m: dict, tutti: list[dict]) -> list[dict]:
    pref = tuple(m.get("task_prefissi", []))
    if not pref:
        return []
    return [t for t in tutti if str(t.get("id", "")).startswith(pref)]


def _esiste(rel: str | None) -> bool:
    if not rel:
        return False
    return (repo_root() / rel).exists()


def stato_cantiere() -> list[dict]:
    """Un dict per modello operativo governato: progresso reale + prossimo passo + check."""
    registro = _carica_registro()
    tutti = _carica_task()
    out: list[dict] = []
    for m in registro:
        task = _task_del_modello(m, tutti)
        fatti = [t for t in task if t.get("stato") == "fatto"]
        da_fare = [t for t in task if t.get("stato") != "fatto"]
        prossimo_task = da_fare[0] if da_fare else None
        out.append({
            "id": m.get("id", "?"),
            "nome": m.get("nome", m.get("id", "?")),
            "ruolo": m.get("ruolo", ""),
            "owner": m.get("owner", "?"),
            "path_ok": _esiste(m.get("path")),
            "entrypoint": m.get("entrypoint"),
            "entrypoint_ok": _esiste(m.get("entrypoint")),
            "stato_ripresa": m.get("stato_ripresa"),
            "stato_ripresa_ok": _esiste(m.get("stato_ripresa")),
            "n_task": len(task),
            "n_fatti": len(fatti),
            "prossimo_task": (
                {"id": prossimo_task.get("id"), "titolo": prossimo_task.get("titolo"),
                 "owner": prossimo_task.get("owner")}
                if prossimo_task else None
            ),
            "prossimo_passo": m.get("prossimo_passo", ""),
            "blocco": m.get("blocco"),
        })
    return out


def _riga_progresso(c: dict) -> str:
    if c["n_task"] == 0:
        return "task nel board: nessuno con questi prefissi"
    return f"task board: {c['n_fatti']}/{c['n_task']} fatti"


def _scrivi_dashboard(cantiere: list[dict]) -> Path:
    oggi = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    righe = [
        "# CANTIERE — presa di costruzione del Workflow Estate sui modelli operativi",
        "",
        f"> Generato da `empire cantiere` il {oggi}. Non modificare a mano: si rigenera.",
        "",
        "Il cervello (WORKFLOW-ESTATE) governa questi modelli operativi. Per ognuno: dove sta il",
        "prossimo passo di costruzione, chi lo possiede, se e' bloccato, se il codice esiste davvero.",
        "",
    ]
    for c in cantiere:
        righe.append(f"## {c['nome']}  (`{c['id']}`)")
        righe.append("")
        righe.append(f"- **Ruolo:** {c['ruolo']}")
        righe.append(f"- **Owner:** {c['owner']}")
        righe.append(f"- **Avanzamento:** {_riga_progresso(c)}")
        ep = c["entrypoint"] or "(non dichiarato)"
        righe.append(f"- **Entrypoint:** `{ep}` — {'presente' if c['entrypoint_ok'] else 'ASSENTE'}")
        if c["prossimo_task"]:
            pt = c["prossimo_task"]
            righe.append(f"- **Prossimo task board:** {pt['id']} — {pt['titolo']} (owner {pt['owner']})")
        righe.append(f"- **Prossimo passo:** {c['prossimo_passo']}")
        if c["blocco"]:
            righe.append(f"- **BLOCCO:** {c['blocco']}")
        righe.append("")
    p = repo_root() / _DASHBOARD
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(righe), encoding="utf-8")
    return p


def _cmd_cantiere(a) -> int:
    safe_stdout()
    cantiere = stato_cantiere()
    print(_RESET)
    print("  DIGITAL EMPIRE — CANTIERE — presa di costruzione sui modelli operativi")
    print(_RESET)
    if not cantiere:
        print("  Nessun modello nel registro. Atteso: " + _REGISTRO)
        print(_RESET)
        return 1
    for c in cantiere:
        stato_path = "ok" if c["path_ok"] else "PATH ASSENTE"
        print(f"  [{c['id']:>10}] {c['nome']}  ({stato_path})")
        print(f"             ruolo:  {c['ruolo']}")
        print(f"             {_riga_progresso(c)}   owner: {c['owner']}")
        ep_stato = "presente" if c["entrypoint_ok"] else "ASSENTE"
        print(f"             entrypoint: {c['entrypoint']}  [{ep_stato}]")
        if c["prossimo_task"]:
            pt = c["prossimo_task"]
            print(f"             prossimo task: {pt['id']} — {pt['titolo']}")
        print(f"             PROSSIMO PASSO: {c['prossimo_passo']}")
        if c["blocco"]:
            print(f"             BLOCCO: {c['blocco']}")
        print()
    dash = _scrivi_dashboard(cantiere)
    liberi = [c for c in cantiere if not c["blocco"]]
    print(_RESET)
    print(f"  {len(cantiere)} modelli governati.  {len(liberi)} senza blocco (costruibili adesso).")
    try:
        print(f"  dashboard visibile: {dash.relative_to(repo_root()).as_posix()}")
    except ValueError:
        print(f"  dashboard visibile: {dash}")
    print(_RESET)
    return 0


def register(sub) -> None:
    """Registrato via plugin loop (empire.flow.cli). `empire/cli.py` resta congelato."""
    p = sub.add_parser(
        "cantiere",
        help="presa di costruzione: prossimo passo per ogni modello operativo governato dall'Estate",
    )
    p.set_defaults(fn=_cmd_cantiere)
