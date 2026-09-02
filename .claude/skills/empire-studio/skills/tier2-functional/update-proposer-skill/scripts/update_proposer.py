#!/usr/bin/env python3
"""
update-proposer-skill / update_proposer.py  (REALE)

Confronta gli atomi di una run con i workflow esistenti (workflow-state +
cartelle note dell'utente) e produce uno scheletro di update-proposals.md:
elenca i possibili match (atomo -> workflow) che l'agente update-proposer
(Claude) poi raffina con proposte concrete e trace.

Non modifica nulla: produce solo proposte.

Uso:
  python update_proposer.py --run <run-id> [--mode normal|cross]
Output: runs/<run-id>/update-proposals.md
"""
import argparse
import json
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RUNS = ROOT / "runs"
MEM = ROOT / "memory"


def load_atoms(run_dir):
    p = run_dir / "atoms.json"
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else data.get("atoms", [])
    except Exception:
        return []


def known_workflows():
    """Indizi di workflow esistenti: voci in workflow-state + nomi noti."""
    flows = set()
    ws = MEM / "workflow-state"
    if ws.exists():
        for f in ws.glob("*.md"):
            flows.add(f.stem)
    # workflow tipici di Digital Empire (estendibile)
    flows.update(["skill-creator", "content-forge", "master-build-architecture",
                  "outreach", "instagram-automation", "empire-studio"])
    return sorted(flows)


def keywords(text):
    return set(re.findall(r"[a-zA-Z]{4,}", (text or "").lower()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--mode", default="normal", choices=["normal", "cross"])
    args = ap.parse_args()
    run_dir = RUNS / args.run
    atoms = load_atoms(run_dir)
    flows = known_workflows()

    lines = [
        f"# Update Proposals - run {args.run}  (modalita': {args.mode})",
        f"_{datetime.datetime.now():%Y-%m-%d %H:%M}_",
        "",
        "Scheletro generato dallo script: candidati match atomo->workflow. "
        "L'agente update-proposer (Claude) li trasforma in proposte concrete con "
        "razionale e trace, **senza modificare nulla** (sola proposta).",
        "",
        f"Workflow noti considerati: {', '.join(flows)}",
        "",
        "## Candidati",
    ]
    n = 0
    for a in atoms:
        atom_txt = a.get("atom") or a.get("text") or str(a)
        kw = keywords(atom_txt)
        matches = [w for w in flows if keywords(w) & kw]
        if matches:
            n += 1
            lines.append(f"\n### Atomo: {atom_txt[:120]}")
            lines.append(f"- Possibili workflow impattati: {', '.join(matches)}")
            lines.append(f"- Trace fonte: {a.get('trace', '(n/d)')}")
            lines.append("- [PROPOSTA: l'agente specifica cosa cambiare, dove e perche']")
    if n == 0:
        lines.append("\n_Nessun match automatico evidente. L'agente valuta comunque "
                     "manualmente la rilevanza._")
    lines += ["", f"**Totale candidati: {n}** · Atomi analizzati: {len(atoms)}",
              "", "Regola: solo PROPOSTE. Nessun workflow esistente viene modificato."]

    out = run_dir / "update-proposals.md"
    run_dir.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[update_proposer] {n} candidati su {len(atoms)} atomi -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
