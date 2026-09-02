#!/usr/bin/env python3
"""
cli-doc-skill / make_report.py  (REALE - stile cli-printing-press)

Assembla runs/<run-id>/REPORT.md leggibile per l'utente: cosa e' stato ingerito,
dove e' finito (frame, analisi, note wiki), con le trace principali.

Uso: python make_report.py --run <run-id>
"""
import argparse
import json
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RUNS = ROOT / "runs"


def read_json(p):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    run_dir = RUNS / args.run
    if not run_dir.exists():
        print(f"ERRORE: run inesistente: {run_dir}")
        raise SystemExit(2)

    ingest = read_json(run_dir / "ingest.json")
    fman = read_json(run_dir / "frames" / "manifest.json")
    has_analysis = (run_dir / "video-analysis.md").exists()
    wiki_notes = list((run_dir / "wiki-notes").glob("*.md")) if (run_dir / "wiki-notes").exists() else []
    has_updates = (run_dir / "update-proposals.md").exists()

    L = [
        f"# Empire Studio - Report run `{args.run}`",
        f"_{datetime.datetime.now():%Y-%m-%d %H:%M}_",
        "",
        "## Sorgente",
        f"- Titolo: {ingest.get('title', '(n/d)')}",
        f"- URL/percorso: {ingest.get('url', ingest.get('source_url', '(n/d)'))}",
        f"- Tipo: {ingest.get('kind', '(n/d)')} · Durata: {ingest.get('duration_sec', '(n/d)')}s",
        "",
        "## Cosa e' stato fatto",
        f"- Ingest: {'OK' if ingest else 'no'}",
        f"- Frame estratti (ffmpeg): {len(fman.get('frames', []))}",
        f"- Visione (Claude) -> video-analysis.md: {'OK' if has_analysis else 'no'}",
        f"- Note forgiate per la wiki: {len(wiki_notes)}",
        f"- Update proposals: {'OK' if has_updates else 'no'}",
        "",
        "## Trace principali (fonte -> frame -> nota)",
    ]
    for fr in fman.get("frames", [])[:8]:
        L.append(f"- {fr.get('timestamp_hms')} -> {fr.get('file')}  ({fr.get('trace', '')})")
    if wiki_notes:
        L += ["", "## Note wiki prodotte"]
        for w in wiki_notes:
            L.append(f"- {w.name}")
    L += ["", "## Note",
          "Report generato da cli-doc-skill (stile cli-printing-press). "
          "Tutti gli artefatti sono in `runs/" + args.run + "/`.", ""]

    out = run_dir / "REPORT.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"[make_report] -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
