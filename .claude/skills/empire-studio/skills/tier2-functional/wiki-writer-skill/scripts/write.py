#!/usr/bin/env python3
"""
wiki-writer-skill / write.py  (wrapper REALE del motore scripts/wiki_writer.py)

Punto d'ingresso della skill: sceglie la sottocartella wiki in base al tipo di
contenuto e delega al motore condiviso (scrittura nella wiki di Digital Empire
+ aggiornamento log.md).

Uso:
  python write.py --note runs/<run>/wiki-notes/ --kind sources --topic <t> --source <url>
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENGINE = ROOT / "scripts" / "wiki_writer.py"

KIND_TO_SUBDIR = {
    "external": "sources", "video": "sources", "web": "sources",
    "concept": "concepts", "tool": "tools", "synthesis": "synthesis",
    "sources": "sources",
}


def main():
    ap = argparse.ArgumentParser(description="wiki-writer-skill (wrapper)")
    ap.add_argument("--note", required=True, help="file .md o cartella di note forgiate")
    ap.add_argument("--kind", default="external", help="external|web|concept|tool|synthesis")
    ap.add_argument("--topic", default="empire-ingest")
    ap.add_argument("--source", default="")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not ENGINE.exists():
        print(f"ERRORE: motore mancante: {ENGINE}")
        sys.exit(1)

    subdir = KIND_TO_SUBDIR.get(args.kind, "sources")
    cmd = [sys.executable, str(ENGINE), "--note", args.note, "--subdir", subdir,
           "--topic", args.topic, "--source", args.source]
    if args.dry_run:
        cmd.append("--dry-run")
    print(f"[wiki-writer-skill] kind={args.kind} -> wiki/{subdir}")
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
