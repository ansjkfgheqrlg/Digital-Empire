#!/usr/bin/env python3
"""
Memory Empire - enrich_skill.py  (REALE - modifica ALTRE skill in sicurezza)

Aggiunge nuova conoscenza (principi/regole/esempi da un contenuto ingerito) a un
file di un'ALTRA skill/workflow. E' la capacita' potente di Memory Empire, resa
SICURA:
  1. BACKUP del file target prima di toccarlo (in memory/enrichments/backups/).
  2. APPEND di una sezione MARCATA (mai overwrite, mai delete).
  3. LOG della modifica (cosa/dove/quando/fonte) in memory/enrichments/ → reversibile.

Uso:
  python scripts/enrich_skill.py --target <file.md> --content <atomi.md|testo> --source "<fonte>" [--section "Titolo"] [--dry-run]
  (rollback: usa audit_log.py --rollback <id>)
"""
import argparse
import datetime
import shutil
import sys
from pathlib import Path

try:  # output utf-8 sicuro anche su console Windows (cp1252)
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ME = Path(__file__).resolve().parent.parent
ENR = ME / "memory" / "enrichments"
BAK = ENR / "backups"
MARK = "<!-- memory-empire-enrichment -->"


def ts():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True, help="file .md della skill da arricchire")
    ap.add_argument("--content", required=True, help="file .md con la conoscenza, o testo diretto")
    ap.add_argument("--source", default="(n/d)", help="fonte (video/url/file)")
    ap.add_argument("--section", default="Conoscenza aggiunta")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    target = Path(args.target)
    if not target.exists() or target.suffix.lower() != ".md":
        print(f"ERRORE: target non valido (serve un file .md esistente): {target}")
        raise SystemExit(2)

    # contenuto: file o testo diretto
    cpath = Path(args.content)
    content = cpath.read_text(encoding="utf-8", errors="replace") if cpath.exists() else args.content

    block = (f"\n\n{MARK}\n## ➕ {args.section} — aggiunto da Memory Empire ({ts()})\n"
             f"_Fonte: {args.source}_\n\n{content.strip()}\n{MARK}\n")

    if args.dry_run:
        print(f"[dry-run] BACKUP di {target} -> {BAK}")
        print(f"[dry-run] APPEND ({len(block)} char) in coda a {target}")
        print(f"[dry-run] LOG in {ENR}")
        print("--- anteprima blocco ---")
        print(block[:400] + ("..." if len(block) > 400 else ""))
        return

    # 1. backup
    BAK.mkdir(parents=True, exist_ok=True)
    bak_name = f"{ts()}-{target.name}.bak"
    shutil.copy2(target, BAK / bak_name)

    # 2. append (mai overwrite)
    with target.open("a", encoding="utf-8") as f:
        f.write(block)

    # 3. log (reversibile)
    ENR.mkdir(parents=True, exist_ok=True)
    log_id = ts()
    (ENR / f"ENR-{log_id}.md").write_text(
        f"# Arricchimento {log_id}\n\n"
        f"- **Target:** {target}\n- **Backup:** memory/enrichments/backups/{bak_name}\n"
        f"- **Fonte:** {args.source}\n- **Sezione:** {args.section}\n"
        f"- **Char aggiunti:** {len(block)}\n- **Rollback:** `python scripts/audit_log.py --rollback {log_id}`\n",
        encoding="utf-8")

    print(f"[enrich] OK: aggiunta sezione a {target.name}")
    print(f"[enrich] backup: {bak_name} · log: ENR-{log_id}")
    print(f"[enrich] reversibile: python scripts/audit_log.py --rollback {log_id}")


if __name__ == "__main__":
    main()
