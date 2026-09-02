#!/usr/bin/env python3
"""
frame-extractor-skill / extract.py  (wrapper REALE del motore scripts/frame_extractor.py)

Punto d'ingresso della skill: applica default (max-frames, height) adatti al tipo
di contenuto e delega al motore condiviso (ffmpeg). Per i video brevi (TikTok)
alza la densita' dei frame.

Uso:
  python extract.py --run <run-id> [--kind youtube|tiktok] [--max-frames N] [--height 360]
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENGINE = ROOT / "scripts" / "frame_extractor.py"


def main():
    ap = argparse.ArgumentParser(description="frame-extractor-skill (wrapper)")
    ap.add_argument("--run", required=True)
    ap.add_argument("--kind", default="youtube", choices=["youtube", "tiktok", "web"])
    ap.add_argument("--max-frames", type=int, default=0)
    ap.add_argument("--height", type=int, default=360)
    args = ap.parse_args()

    if not ENGINE.exists():
        print(f"ERRORE: motore mancante: {ENGINE}")
        sys.exit(1)

    # default per tipo: TikTok = frame piu' densi data la brevita'
    max_frames = args.max_frames or (10 if args.kind == "tiktok" else 12)
    cmd = [sys.executable, str(ENGINE), "--run", args.run,
           "--max-frames", str(max_frames), "--height", str(args.height)]
    print(f"[frame-extractor-skill] kind={args.kind} max_frames={max_frames} -> motore ffmpeg")
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
