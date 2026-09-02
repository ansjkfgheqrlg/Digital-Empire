#!/usr/bin/env python3
"""
Empire Studio - skill_factory.py

Genera i SKILL.md delle skill (tier0/tier1/tier2) da specifiche compatte in
scripts/_specs/skills_*.py. NON crea gli script .py: quelli sono codice reale
scritto a mano e gia' presenti nelle cartelle scripts/ delle skill (il validator
verifica che le tier2-functional abbiano uno script reale che compila).

Uso:
  python scripts/skill_factory.py --spec skills_tier2
  python scripts/skill_factory.py --spec all
"""
import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS_DIR = Path(__file__).resolve().parent / "_specs"


def render_skill(s):
    name = s["name"]
    tier = s["tier"]
    L = [
        "---",
        f"name: {name}",
        f"tier: {tier}",
        f"description: \"{s['description']}\"",
    ]
    if s.get("uses_scripts"):
        L.append("uses_scripts:")
        for sc in s["uses_scripts"]:
            L.append(f"  - {sc}")
    if s.get("controls"):
        L.append("controls:")
        for c in s["controls"]:
            L.append(f"  - {c}")
    L.append("---")
    L += [
        "",
        f"# {name} ({tier})",
        "",
        f"> {s.get('tagline', s['description'][:120])}",
        "",
        "## Cosa fa",
    ]
    for r in s["does"]:
        L.append(f"- {r}")
    L += ["", "## Come si usa"]
    L.append("```")
    for u in s.get("usage", ["(invocata dagli agenti del reparto)"]):
        L.append(u)
    L.append("```")
    L += ["", "## Invarianti"]
    for inv in s.get("invariants", [
        "CLI-only, no API, no paid.", "Tracciabilita' P12 sugli output.",
        "Memory-first: aggiorna memory dopo l'azione."]):
        L.append(f"- {inv}")
    if s.get("agents"):
        L += ["", "## Agenti che la impugnano"]
        for ag in s["agents"]:
            L.append(f"- `{ag}`")
    if s.get("script_note"):
        L += ["", "## Script", s["script_note"]]
    L += ["", "## Trace", s.get("trace", "Parte dell'ecosistema Empire Studio.")]
    return "\n".join(L) + "\n"


def build_skill(s, dry=False):
    tier = s["tier"]
    dest = ROOT / "skills" / tier / s["name"]
    content = render_skill(s)
    if dry:
        print(f"  [dry] {dest.relative_to(ROOT)}/SKILL.md ({len(content)} char)")
        return
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "SKILL.md").write_text(content, encoding="utf-8")
    print(f"  OK  {tier}/{s['name']}/SKILL.md")


def load_module(spec_name):
    path = SPECS_DIR / f"{spec_name}.py"
    if not path.exists():
        print(f"ERRORE: spec non trovata: {path}")
        sys.exit(1)
    spec = importlib.util.spec_from_file_location(spec_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "SKILLS", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    modules = ([p.stem for p in SPECS_DIR.glob("skills_*.py")]
               if args.spec == "all" else [args.spec])
    for m in modules:
        skills = load_module(m)
        print(f"== {m}: {len(skills)} skill ==")
        for s in skills:
            build_skill(s, args.dry_run)


if __name__ == "__main__":
    main()
