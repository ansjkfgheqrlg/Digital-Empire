#!/usr/bin/env python3
"""
yt-ingest-skill / ingest.py  (wrapper REALE del motore scripts/yt_ingest.py)

Aggiunge default sensati e validazione minima, poi delega al motore condiviso
(scripts/yt_ingest.py) che usa yt-dlp. Tenere il motore condiviso evita la
duplicazione; questo wrapper e' il punto d'ingresso della skill.

Uso:
  python ingest.py <url> [--focus design] [--run myrun] [--max 15]
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENGINE = ROOT / "scripts" / "yt_ingest.py"


def main():
    ap = argparse.ArgumentParser(description="yt-ingest-skill (wrapper)")
    ap.add_argument("url", help="URL video o canale YouTube/TikTok")
    ap.add_argument("--focus", default="")
    ap.add_argument("--run", default="")
    ap.add_argument("--max", type=int, default=15)
    args = ap.parse_args()

    if not args.url.startswith(("http://", "https://")):
        print("ERRORE: fornisci un URL http(s) valido.")
        sys.exit(2)
    if not ENGINE.exists():
        print(f"ERRORE: motore mancante: {ENGINE}")
        sys.exit(1)

    cmd = [sys.executable, str(ENGINE), "--input", args.url, "--max", str(args.max)]
    if args.focus:
        cmd += ["--focus", args.focus]
    if args.run:
        cmd += ["--run", args.run]
    print(f"[yt-ingest-skill] delego al motore: {' '.join(cmd[2:])}")
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
