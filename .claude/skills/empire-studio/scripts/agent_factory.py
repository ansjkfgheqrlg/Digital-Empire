#!/usr/bin/env python3
"""
Empire Studio - agent_factory.py

Genera i 7 file canonici di un agente a partire da una specifica RICCA e
specifica (un dict Python per agente, in scripts/_specs/<dept>.py).

NON e' un generatore di stub: rifiuta specifiche povere. Ogni agente deve avere
ruolo, responsabilita', tool, >=5 failure modes, >=4 evals, protocollo memory.
La sostanza la scrive l'umano nelle spec; la factory garantisce struttura
coerente + soglia anti-stub (allineata a validator.py).

Uso:
  python scripts/agent_factory.py --spec youtube_department
  python scripts/agent_factory.py --spec all          # tutti i moduli in _specs/
  python scripts/agent_factory.py --spec web_department --dry-run
"""
import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = Path(__file__).resolve().parent / "_specs"

REQUIRED = ["name", "department", "role", "responsibilities",
            "failure_modes", "evals", "memory", "trace"]
# tool di default per gli agenti di puro ragionamento (non tutti avvolgono uno script)
DEFAULT_TOOLS = [
    {"name": "ragionamento dell'agente", "desc": "analisi/decisione svolta da Claude nel ruolo, "
     "leggendo i file della run e applicando le regole del reparto"},
    {"name": "memory_manager.py", "desc": "registrazione checkpoint/stato dopo l'azione",
     "cmd": "python scripts/memory_manager.py --checkpoint \"<azione> completata\" --phase <n>"},
]
MIN_RESP = 3
MIN_FM = 5
MIN_EVALS = 4


def _bullets(items):
    return "\n".join(f"- {x}" for x in items)


def render_spec(a):
    name = a["name"]
    lead = a.get("lead", "department-lead")
    skills = a.get("skills", [])
    inputs = a.get("inputs", "handoff dal lead/conductor")
    outputs = a.get("outputs", "artefatti nella run + handoff")
    parts = [
        f"# {name} (L{a.get('level',3)} - {a['department']})",
        "",
        f"**Ruolo:** {a['role']}",
        f"**Reparto:** {a['department']} · **Livello:** L{a.get('level',3)} · **Lead:** {lead}",
        f"**Skill usate:** {', '.join(skills) if skills else '(usa i tool del reparto)'}",
        "",
        "**Responsabilita':**",
        _bullets(a["responsibilities"]),
        "",
        f"**Input (handoff in):** {inputs}",
        f"**Output (handoff out):** {outputs}",
        f"**Quando si attiva:** {a.get('when', 'su handoff dal lead del reparto')}",
        "",
        f"**Trace (P12):** {a['trace']}",
    ]
    return "\n".join(parts) + "\n"


def render_system_prompt(a):
    rules = a.get("rules", [
        "NO-FINTO: niente dati inventati; le inferenze si marcano +.",
        "Memory-first: aggiorna memory dopo ogni azione (P10).",
        "Tracciabilita' (P12): ogni atomo ancorato alla fonte.",
        "CLI-only, no API, no paid.",
    ])
    parts = [
        f"# {a['name']} - System Prompt",
        "",
        f"Tu sei **{a['name']}** di Empire Studio, nel reparto {a['department']}.",
        "",
        "## Identita' e missione",
        a.get("mission", a["role"]),
        "",
        "## Regole non negoziabili",
        _bullets(rules),
        "",
        "## Cosa fai",
        _bullets(a["responsibilities"]),
        "",
        "## Cosa NON fai",
        _bullets(a.get("not_do", [
            "Non parli direttamente con l'utente (riporti al lead).",
            "Non esci dal tuo perimetro di reparto.",
            "Non dichiari 'fatto' senza che il validator/verifica lo confermi.",
        ])),
        "",
        "## Tono",
        a.get("tone", "Preciso, concreto, asciutto. Professionale come un reparto vero."),
    ]
    return "\n".join(parts) + "\n"


def render_tools(a):
    lines = [f"# {a['name']} - Tools", "",
             "Strumenti CLI/script che questo agente usa. Solo CLI, no API, no paid "
             "(la visione, dove serve, la fornisce Claude leggendo i frame).",
             "", "## Strumenti che usa"]
    for i, t in enumerate(a.get("tools") or DEFAULT_TOOLS, 1):
        lines.append(f"{i}. **{t['name']}** - {t['desc']}")
        if t.get("cmd"):
            lines.append("   ```")
            lines.append(f"   {t['cmd']}")
            lines.append("   ```")
    lines += [
        "",
        "## Schema handoff (I/O)",
        "Lo scambio con gli altri agenti del reparto avviene via file nella run e via "
        "handoff strutturato:",
        "```json",
        a.get("io_schema", '{ "in": {"run_id": "...", "from": "<lead>"},\n  "out": {"artifacts": ["..."], "summary_for_lead": "...", "trace": "..."} }'),
        "```",
        "",
        "## Memory hook (P10)",
        "Dopo l'azione principale registra un checkpoint e lo stato pertinente:",
        "```",
        a.get("memory_hook",
              "python scripts/memory_manager.py --checkpoint \"<azione> completata\" --phase <n> --trace \"<run/fonte>\""),
        "```",
        "Vedi `memory.md` per il protocollo completo di questo agente.",
    ]
    return "\n".join(lines) + "\n"


def render_playbook(a):
    steps = a.get("steps", a["responsibilities"])
    lines = [f"# {a['name']} - Playbook", "", "## Flusso operativo"]
    for i, s in enumerate(steps, 1):
        lines.append(f"{i}. {s}")
    lines += ["", "## Esempi"]
    examples = a.get("examples", [
        f"Happy: input valido -> {a['name']} produce l'output atteso con trace.",
        "Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.",
        "Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.",
    ])
    for ex in examples:
        lines.append(f"- {ex}")
    lines += ["", "## Handoff in uscita",
              a.get("handoff_out", "Al reparto successivo (o al verification/forge) con summary + trace.")]
    return "\n".join(lines) + "\n"


def render_evals(a):
    lines = [f"# {a['name']} - Evals (casi discriminanti)", ""]
    for i, e in enumerate(a["evals"], 1):
        lines.append(f"## EV-{i:02d} - {e['name']}")
        lines.append(f"- **Input:** {e['input']}")
        lines.append(f"- **Atteso:** {e['expected']}")
        lines.append(f"- **Voto:** {e.get('grade', 'PASS se il criterio sopra e soddisfatto')}")
        lines.append("")
    return "\n".join(lines) + "\n"


def render_failure_modes(a):
    lines = [
        f"# {a['name']} - Failure Modes (P09)", "",
        "| Failure | Sintomo | Prevenzione | Detection | Recovery |",
        "|---|---|---|---|---|",
    ]
    for fm in a["failure_modes"]:
        lines.append(f"| {fm['failure']} | {fm['symptom']} | {fm['prevention']} | {fm['detection']} | {fm['recovery']} |")
    lines += ["", "I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o "
              "`memory/errors/`; il silent-observer li usa per il miglioramento."]
    return "\n".join(lines) + "\n"


def render_memory(a):
    m = a["memory"]
    lines = [
        f"# {a['name']} - Memory (P10)", "",
        "L'agente aggiorna l'ecosistema di memoria dopo OGNI azione significativa.",
        "",
        "## Cosa registra e dove",
    ]
    if isinstance(m, dict):
        for cat, what in m.items():
            lines.append(f"- **{cat}/**: {what}")
    else:
        lines.append(_bullets(m if isinstance(m, list) else [str(m)]))
    lines += [
        "",
        "## Quando aggiorna",
        a.get("memory_when",
              "Prima di iniziare legge lo stato rilevante della run (per non rifare lavoro "
              "gia' fatto); dopo ogni azione significativa crea un checkpoint; a fine "
              "handoff aggiorna agent-state con le metriche della propria esecuzione."),
        "",
        "## Two-layer (P10)",
        "Short-term: lo stato operativo della run corrente vive nei file di "
        "`runs/<run-id>/` (artefatti, manifest). Long-term: i checkpoint, le decisioni e "
        "gli stati persistenti vivono in `memory/` e sono indicizzati in `MEMORY-INDEX.md`, "
        "riutilizzabili in run future (es. stesso canale/argomento).",
        "",
        "## Comando tipico",
        "```",
        "python scripts/memory_manager.py --checkpoint \"<azione> completata\" --phase <n> --trace \"<run/fonte>\"",
        "```",
        "",
        f"## Trace (P12)\n{a['trace']}",
    ]
    return "\n".join(lines) + "\n"


RENDERERS = {
    "{name}.md": render_spec,
    "system-prompt.md": render_system_prompt,
    "tools.md": render_tools,
    "playbook.md": render_playbook,
    "evals.md": render_evals,
    "failure-modes.md": render_failure_modes,
    "memory.md": render_memory,
}


def validate_spec(a):
    errs = []
    for r in REQUIRED:
        if not a.get(r):
            errs.append(f"manca campo '{r}'")
    if len(a.get("responsibilities", [])) < MIN_RESP:
        errs.append(f"responsibilities < {MIN_RESP}")
    if len(a.get("failure_modes", [])) < MIN_FM:
        errs.append(f"failure_modes < {MIN_FM}")
    if len(a.get("evals", [])) < MIN_EVALS:
        errs.append(f"evals < {MIN_EVALS}")
    return errs


def build_agent(a, dry=False):
    errs = validate_spec(a)
    if errs:
        print(f"  SPEC POVERA [{a.get('name','?')}]: {errs}")
        return False
    dest = ROOT / "agents" / a["department"] / a["name"]
    for fname_tpl, renderer in RENDERERS.items():
        fname = fname_tpl.format(name=a["name"])
        content = renderer(a)
        if dry:
            print(f"  [dry] {dest.relative_to(ROOT)}/{fname} ({len(content)} char)")
            continue
        dest.mkdir(parents=True, exist_ok=True)
        (dest / fname).write_text(content, encoding="utf-8")
    if not dry:
        print(f"  OK  {a['department']}/{a['name']} (7 file)")
    return True


def load_module(spec_name):
    path = SPECS_DIR / f"{spec_name}.py"
    if not path.exists():
        print(f"ERRORE: spec non trovata: {path}")
        sys.exit(1)
    spec = importlib.util.spec_from_file_location(spec_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "AGENTS", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True, help="nome modulo in _specs/ o 'all'")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    modules = []
    if args.spec == "all":
        modules = [p.stem for p in SPECS_DIR.glob("*.py") if not p.stem.startswith("_")]
    else:
        modules = [args.spec]

    total, ok = 0, 0
    for m in modules:
        agents = load_module(m)
        print(f"== {m}: {len(agents)} agenti ==")
        for a in agents:
            total += 1
            if build_agent(a, args.dry_run):
                ok += 1
    print(f"\nFactory: {ok}/{total} agenti generati.")
    if ok < total:
        sys.exit(1)


if __name__ == "__main__":
    main()
