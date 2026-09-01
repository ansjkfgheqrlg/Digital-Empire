#!/usr/bin/env python3
"""
Memory Empire - relevance_scan.py  (REALE)

Analizza a quali skill installate e' rilevante una nuova conoscenza (atomi),
per indirizzare l'arricchimento. Matching per parole chiave tra gli atomi e la
descrizione/nome di ogni skill. Sola lettura.

Uso:
  python scripts/relevance_scan.py --atoms <atoms.json> [--skills-dir ~/.claude/skills] [--top 8]
Output: stampa le skill candidate ordinate per rilevanza.
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def keywords(text, minlen=4):
    return set(w for w in re.findall(r"[a-zA-Zàèéìòù]{%d,}" % minlen, (text or "").lower()))


def load_atom_keywords(atoms_path):
    p = Path(atoms_path)
    if not p.exists():
        return set()
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return keywords(p.read_text(encoding="utf-8", errors="replace"))
    items = data if isinstance(data, list) else data.get("atoms", [])
    kw = set()
    for a in items:
        kw |= keywords(a.get("atom") or a.get("text") or str(a))
    return kw


def skill_keywords(skill_dir: Path):
    md = skill_dir / "SKILL.md"
    if not md.exists():
        return skill_keywords_name(skill_dir)
    txt = md.read_text(encoding="utf-8", errors="replace")[:4000]
    return keywords(skill_dir.name + " " + txt)


def skill_keywords_name(skill_dir: Path):
    return keywords(skill_dir.name)


# parole troppo comuni che non indicano rilevanza
STOP = keywords("skill use when user wants quando questo questa della delle content "
                "anche essere viene sempre ogni tutto come into this that with from")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--atoms", required=True)
    ap.add_argument("--skills-dir", default=str(Path.home() / ".claude" / "skills"))
    ap.add_argument("--top", type=int, default=8)
    args = ap.parse_args()

    atom_kw = load_atom_keywords(args.atoms) - STOP
    if not atom_kw:
        print("Nessuna parola chiave dagli atomi (atoms.json vuoto?).")
        return
    sdir = Path(args.skills_dir).expanduser()
    scored = []
    for d in sdir.iterdir():
        if not d.is_dir() or d.name == "memory-empire":
            continue
        skw = skill_keywords(d) - STOP
        overlap = atom_kw & skw
        if overlap:
            scored.append((len(overlap), d.name, sorted(overlap)[:8]))
    scored.sort(reverse=True)

    print(f"Atomi: {len(atom_kw)} parole chiave. Skill candidate all'arricchimento:")
    for score, name, words in scored[:args.top]:
        print(f"  [{score}] {name}  <- {', '.join(words)}")
    if not scored:
        print("  (nessuna skill chiaramente rilevante)")
    print("\nPassa i match sopra soglia allo skill-enricher (con backup+log).")


if __name__ == "__main__":
    main()
