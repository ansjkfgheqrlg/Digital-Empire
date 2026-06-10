#!/usr/bin/env python3
"""
Empire Studio - save_to_memory_empire.py  (REALE)

Deposita il contenuto INTEGRALE di una run nella skill Memory Empire
(~/.claude/skills/memory-empire/knowledge/), realizzando il "doppio salvataggio"
richiesto: il contenuto va sia nella wiki (wiki_writer.py) sia in Memory Empire.

Mai riassunti: copia il materiale per intero (analisi/visione + atomi + fonte).

Uso: python scripts/save_to_memory_empire.py --run <run-id> [--type video]
"""
import argparse
import json
import re
import shutil
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
ME = Path.home() / ".claude" / "skills" / "memory-empire"
KNOW = ME / "knowledge"


def slug(t):
    t = re.sub(r'[<>:"/\\|?*+()\[\]]', "", (t or "").lower())
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return (t[:48].rstrip("-")) or "contenuto"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--type", default="contenuto")
    args = ap.parse_args()
    run_dir = RUNS / args.run
    if not run_dir.exists():
        print(f"ERRORE: run inesistente: {run_dir}")
        raise SystemExit(2)
    if not ME.exists():
        print(f"ERRORE: Memory Empire non trovata in {ME}")
        raise SystemExit(2)

    ingest = {}
    ip = run_dir / "ingest.json"
    if ip.exists():
        try:
            ingest = json.loads(ip.read_text(encoding="utf-8"))
        except Exception:
            ingest = {}
    title = ingest.get("title") or ingest.get("source_url") or args.run
    src = ingest.get("url") or ingest.get("source_url") or "(n/d)"
    dest = KNOW / slug(title)
    dest.mkdir(parents=True, exist_ok=True)

    # contenuto integrale: preferisci l'analisi (video/deep/web), mai riassunto
    integ = None
    for cand in ["video-analysis.md", "deep-analysis.md", "repo-analysis.md",
                 "web-content.md", "transcript.clean.md"]:
        if (run_dir / cand).exists():
            integ = run_dir / cand
            break
    if integ:
        shutil.copy2(integ, dest / "contenuto-integrale.md")
    if (run_dir / "atoms.json").exists():
        shutil.copy2(run_dir / "atoms.json", dest / "atoms.json")
    (dest / "fonte.txt").write_text(f"{src}\nrun: {args.run}\ntype: {args.type}\n", encoding="utf-8")

    # aggiorna l'indice di Memory Empire
    idx = ME / "index.md"
    row = (f"| {datetime.date.today()} | {args.type} | {title[:50]} | "
           f"knowledge/{dest.name}/ | (vedi wiki) |")
    if idx.exists():
        txt = idx.read_text(encoding="utf-8")
        txt = txt.replace("| - | - | - | - | - |", "| - | - | - | - | - |\n" + row, 1) \
            if "| - | - | - | - | - |" in txt else (txt + "\n" + row + "\n")
        idx.write_text(txt, encoding="utf-8")

    print(f"[memory-empire] contenuto integrale -> {dest}")
    print(f"[memory-empire] index aggiornato. Doppio salvataggio (wiki + Memory Empire) completo.")


if __name__ == "__main__":
    main()
