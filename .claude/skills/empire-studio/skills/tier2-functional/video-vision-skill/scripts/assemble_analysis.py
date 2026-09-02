#!/usr/bin/env python3
"""
video-vision-skill / assemble_analysis.py  (REALE)

Costruisce lo SCHELETRO di runs/<run>/video-analysis.md a partire da:
  - runs/<run>/frames/manifest.json  (frame -> timestamp -> capitolo)
  - runs/<run>/<id>.<lang>.vtt        (transcript, se presente)

Lo scheletro contiene una voce per OGNI frame con timestamp e capitolo, e un
segnaposto esplicito "[VISIONE: l'agente video-watcher (Claude) descrive qui
frame-NNN.png leggendolo]". La parte di VISIONE NON viene inventata dallo script:
viene riempita da Claude che guarda il PNG. Lo script fa solo lavoro
deterministico (struttura + transcript + trace), cosi' la visione resta reale.

Uso:
  python scripts/assemble_analysis.py --run <run-id>
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # .../empire-studio
RUNS = ROOT / "runs"


def load_transcript(run_dir: Path):
    vtts = list(run_dir.glob("*.vtt"))
    if not vtts:
        return ""
    raw = vtts[0].read_text(encoding="utf-8", errors="replace").splitlines()
    out, seen = [], set()
    for line in raw:
        if re.match(r"^(WEBVTT|Kind|Language|NOTE)", line) or "-->" in line or not line.strip():
            continue
        clean = re.sub(r"<[^>]*>", "", line).strip()
        if clean and clean not in seen:
            seen.add(clean)
            out.append(clean)
    return " ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()

    run_dir = RUNS / args.run
    man_path = run_dir / "frames" / "manifest.json"
    if not man_path.exists():
        print(f"ERRORE: manca {man_path}. Esegui prima frame_extractor.py.")
        sys.exit(1)
    man = json.loads(man_path.read_text(encoding="utf-8"))
    ingest = {}
    ip = run_dir / "ingest.json"
    if ip.exists():
        ingest = json.loads(ip.read_text(encoding="utf-8"))

    vid = ingest.get("id", man.get("url", "video"))
    title = ingest.get("title", "(senza titolo)")
    transcript = load_transcript(run_dir)

    lines = [
        f"# Video Analysis - {title} ({vid})",
        "",
        f"- **Source:** {man.get('url')}",
        f"- **Durata:** {man.get('duration_sec')}s · **Frame:** {len(man.get('frames', []))}",
        "- **Visione eseguita da:** Claude (legge i PNG) - lo script crea solo lo scheletro",
        "",
        "## Transcript (reale)",
        transcript or "_(nessun transcript disponibile)_",
        "",
        "## Visual Timeline (da riempire guardando i frame)",
        "",
    ]
    for fr in man.get("frames", []):
        name = Path(fr["file"]).name
        ch = f" [{fr['chapter']}]" if fr.get("chapter") else ""
        lines.append(f"- **{fr['timestamp_hms']} ({name}){ch}** - "
                     f"[VISIONE: descrivi qui cosa mostra {name} - UI, gesti, testo, "
                     f"risultati a schermo]")
        lines.append(f"  - **Trace (P12):** {fr['trace']}")
    lines += [
        "",
        "## Key Visual Passages (cio' che si vede ma il testo non dice)",
        "[da compilare dopo la visione]",
        "",
        "## Knowledge Atoms (con trace)",
        "[da compilare: ogni atomo con trace <id>#<ts> + frame-NNN.png; inferenze con +]",
        "",
    ]
    out = run_dir / "video-analysis.SKELETON.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[video-vision] scheletro -> {out.relative_to(ROOT)}")
    print(f"[video-vision] {len(man.get('frames', []))} frame da guardare. "
          f"Ora l'agente video-watcher legge i PNG e riempie le voci [VISIONE].")


if __name__ == "__main__":
    main()
