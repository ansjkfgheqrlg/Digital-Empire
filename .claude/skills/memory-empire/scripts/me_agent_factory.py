#!/usr/bin/env python3
"""
Memory Empire - me_agent_factory.py

Genera gli agenti di Memory Empire (uno per file, organizzati per categoria:
operativi/analizzatori/studiosi/controllori). Ogni agente NON e' solo un ruolo:
ha Ruolo + Principi + Regole + Strumenti/Script + Esempi + Memoria, come richiesto.

Rifiuta spec povere (anti-stub). Uso:
  python scripts/me_agent_factory.py
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # memory-empire/
SPEC = Path(__file__).resolve().parent / "me_agents.py"
REQUIRED = ["name", "category", "role", "principles", "rules", "tools", "examples", "memory", "trace"]


def b(items):
    return "\n".join(f"- {x}" for x in items)


def render(a):
    L = [
        f"# {a['name']} (Memory Empire - {a['category']})",
        "",
        f"**Ruolo:** {a['role']}",
        f"**Categoria:** {a['category']}",
        "",
        "## Quando si attiva",
        a.get("when", "Quando Memory Empire e' attiva e l'intento ricade nel suo compito."),
        "",
        "## Principi",
        b(a["principles"]),
        "",
        "## Regole",
        b(a["rules"]),
        "",
        "## Strumenti / Script",
    ]
    for t in a["tools"]:
        L.append(f"- **{t['name']}** - {t['desc']}")
        if t.get("cmd"):
            L.append(f"  ```\n  {t['cmd']}\n  ```")
    L += ["", "## Esempi", b(a["examples"]),
          "", "## Memoria", a["memory"],
          "", "## Trace", a["trace"]]
    return "\n".join(L) + "\n"


def validate(a):
    errs = [r for r in REQUIRED if not a.get(r)]
    if len(a.get("principles", [])) < 2: errs.append("principi<2")
    if len(a.get("rules", [])) < 2: errs.append("regole<2")
    if len(a.get("examples", [])) < 2: errs.append("esempi<2")
    return errs


def main():
    spec = importlib.util.spec_from_file_location("me_agents", SPEC)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    agents = getattr(mod, "AGENTS", [])
    ok = 0
    for a in agents:
        e = validate(a)
        if e:
            print(f"  SPEC POVERA [{a.get('name','?')}]: {e}"); continue
        dest = ROOT / "agents" / a["category"]
        dest.mkdir(parents=True, exist_ok=True)
        (dest / f"{a['name']}.md").write_text(render(a), encoding="utf-8")
        ok += 1
        print(f"  OK  agents/{a['category']}/{a['name']}.md")
    print(f"\nMemory Empire factory: {ok}/{len(agents)} agenti.")
    if ok < len(agents):
        sys.exit(1)


if __name__ == "__main__":
    main()
