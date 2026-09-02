#!/usr/bin/env python3
"""
Empire Studio - catalog_status.py

Genera lo STATO REALE del roster leggendo il filesystem (non dichiarazioni).
Un agente conta come 'completo' solo se ha i 7 file canonici. Scrive
agents/STATUS.md con il quadro vero. Cosi' il catalogo non puo' mentire.

Uso: python scripts/catalog_status.py
"""
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANON = ["system-prompt.md", "tools.md", "playbook.md", "evals.md",
         "failure-modes.md", "memory.md"]


def agent_complete(d: Path):
    spec = d / f"{d.name}.md"
    return spec.exists() and all((d / f).exists() for f in CANON)


def main():
    agents_root = ROOT / "agents"
    skills_root = ROOT / "skills"
    lines = ["# Empire Studio - STATUS (auto-generato dal filesystem)", "",
             f"_Generato: {datetime.datetime.now():%Y-%m-%d %H:%M}_  ·  "
             "Fonte: scansione reale di agents/ e skills/ (non dichiarazioni).", ""]

    total, complete = 0, 0
    lines.append("## Agenti per reparto")
    for dept in sorted(p for p in agents_root.iterdir() if p.is_dir()):
        ags = sorted(p for p in dept.iterdir() if p.is_dir())
        if not ags:
            continue
        done = [a for a in ags if agent_complete(a)]
        total += len(ags); complete += len(done)
        lines.append(f"\n### {dept.name}  ({len(done)}/{len(ags)} completi)")
        for a in ags:
            mark = "OK" if agent_complete(a) else "  "
            nfiles = len(list(a.glob("*.md")))
            lines.append(f"- [{mark}] {a.name}  ({nfiles} file)")

    lines.append("")
    lines.append(f"**TOTALE AGENTI: {complete}/{total} completi (7 file)**")
    lines.append("")

    # Skill
    lines.append("## Skill per tier")
    sk_total, sk_done = 0, 0
    if skills_root.exists():
        for tier in sorted(p for p in skills_root.iterdir() if p.is_dir()):
            sks = sorted(p for p in tier.iterdir() if p.is_dir())
            if not sks:
                lines.append(f"\n### {tier.name}  (0)")
                continue
            lines.append(f"\n### {tier.name}  ({len(sks)})")
            for sk in sks:
                sk_total += 1
                has_md = (sk / "SKILL.md").exists()
                has_py = bool(list((sk / "scripts").glob("*.py")) if (sk / "scripts").exists() else []) or bool(list(sk.glob("*.py")))
                ok = has_md and (has_py or tier.name != "tier2-functional")
                if ok:
                    sk_done += 1
                lines.append(f"- [{'OK' if ok else '  '}] {sk.name}  (SKILL.md={'y' if has_md else 'n'}, script={'y' if has_py else 'n'})")
    lines.append("")
    lines.append(f"**TOTALE SKILL: {sk_done}/{sk_total} pronte**")
    lines.append("")

    # Script motore
    lines.append("## Script motore (scripts/)")
    for s in sorted((ROOT / "scripts").glob("*.py")):
        lines.append(f"- {s.name}")

    out = agents_root / "STATUS.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[catalog] {out.relative_to(ROOT)} aggiornato")
    print(f"[catalog] AGENTI {complete}/{total} completi · SKILL {sk_done}/{sk_total}")


if __name__ == "__main__":
    main()
