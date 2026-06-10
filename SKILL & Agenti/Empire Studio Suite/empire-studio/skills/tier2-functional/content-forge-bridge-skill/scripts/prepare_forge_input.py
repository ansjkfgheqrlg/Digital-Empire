#!/usr/bin/env python3
"""
content-forge-bridge-skill / prepare_forge_input.py  (REALE)

Assembla runs/<run-id>/forge-input/ con tutto il materiale che content-forge
deve forgiare in note wiki: video-analysis.md, transcript pulito, atoms.json,
e un INDEX che elenca le fonti con trace. Poi l'agente content-forge-invoker
invoca /forge runs/<run-id>/forge-input/ --target=wiki.

Uso: python prepare_forge_input.py --run <run-id>
"""
import argparse
import json
import shutil
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RUNS = ROOT / "runs"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    run_dir = RUNS / args.run
    if not run_dir.exists():
        print(f"ERRORE: run inesistente: {run_dir}")
        raise SystemExit(2)

    fi = run_dir / "forge-input"
    fi.mkdir(parents=True, exist_ok=True)

    copied = []
    for fname in ["video-analysis.md", "transcript.clean.md", "atoms.json",
                  "kg.json", "deep-analysis.md", "repo-analysis.md", "web-content.md"]:
        src = run_dir / fname
        if src.exists():
            shutil.copy2(src, fi / fname)
            copied.append(fname)

    # INDEX delle fonti per il forge
    ingest = {}
    ip = run_dir / "ingest.json"
    if ip.exists():
        try:
            ingest = json.loads(ip.read_text(encoding="utf-8"))
        except Exception:
            ingest = {}
    idx = [
        f"# Forge Input - run {args.run}",
        f"_{datetime.datetime.now():%Y-%m-%d %H:%M}_",
        "",
        f"- Sorgente: {ingest.get('title', ingest.get('source_url', '(n/d)'))}",
        f"- URL: {ingest.get('url', '(n/d)')}",
        "",
        "## File da forgiare (--target=wiki)",
    ]
    for c in copied:
        idx.append(f"- {c}")
    idx += ["", "Comando suggerito per l'agente content-forge-invoker:",
            "```", f"/forge runs/{args.run}/forge-input/ --target=wiki --name {args.run}", "```",
            "", "Regola: ogni nota forgiata deve conservare la trace (video-id#ts + frame / URL / file:riga)."]
    (fi / "INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    print(f"[prepare_forge_input] {len(copied)} file in forge-input/: {copied}")
    if not copied:
        print("[prepare_forge_input] ATTENZIONE: nessun materiale trovato (manca l'analisi?).")
    print(f"FORGE_INPUT={fi}")


if __name__ == "__main__":
    main()
