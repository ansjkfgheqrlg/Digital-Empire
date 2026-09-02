#!/usr/bin/env python3
"""
transcript-clean-skill / clean_transcript.py  (REALE)

Pulisce un transcript .vtt/.srt: rimuove header, timestamp, tag, righe duplicate
consecutive, e ricompone frasi leggibili conservando ancore temporali ogni N
secondi. Output: runs/<run-id>/transcript.clean.md

Uso: python clean_transcript.py --run <run-id>
"""
import argparse
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RUNS = ROOT / "runs"

TS = re.compile(r"(\d{2}):(\d{2}):(\d{2})[.,]\d{3}")


def parse_vtt(text):
    """Ritorna lista (start_seconds|None, testo)."""
    out = []
    cur_ts = None
    seen_last = None
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        if "-->" in s:
            m = TS.search(s)
            if m:
                h, mm, ss = map(int, m.groups())
                cur_ts = h * 3600 + mm * 60 + ss
            continue
        clean = re.sub(r"<[^>]*>", "", s).strip()
        if not clean or clean == seen_last:
            continue
        seen_last = clean
        out.append((cur_ts, clean))
    return out


def hms(sec):
    return str(datetime.timedelta(seconds=int(sec))) if sec is not None else "?"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    run_dir = RUNS / args.run
    vtts = list(run_dir.glob("*.vtt")) + list(run_dir.glob("*.srt"))
    if not vtts:
        print(f"[clean_transcript] nessun .vtt/.srt in {run_dir} (transcript assente -> sola visione)")
        out = run_dir / "transcript.clean.md"
        out.write_text("# Transcript\n\n_(nessun transcript disponibile: si procede con la sola visione)_\n",
                       encoding="utf-8")
        return
    segs = parse_vtt(vtts[0].read_text(encoding="utf-8", errors="replace"))
    # ricompone testo con ancora ogni ~30s
    lines = [f"# Transcript pulito - {args.run}", "", f"_Fonte: {vtts[0].name}_", ""]
    buff, last_anchor = [], None
    for ts, txt in segs:
        if last_anchor is None or (ts is not None and ts - (last_anchor or 0) >= 30):
            if buff:
                lines.append(" ".join(buff)); buff = []
            lines.append(f"\n**[{hms(ts)}]**")
            last_anchor = ts
        buff.append(txt)
    if buff:
        lines.append(" ".join(buff))
    out = run_dir / "transcript.clean.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[clean_transcript] {len(segs)} segmenti -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
