#!/usr/bin/env python3
"""
Empire Studio - frame_extractor.py  (REALE - estrae FRAME VERI con ffmpeg)

Questo sostituisce il watcher FINTO del primo tentativo (che rifaceva lo stesso
screenshot e inventava le descrizioni). Qui:
  1. scarica il video a bassa risoluzione (yt-dlp, veloce/leggero, no audio);
  2. estrae frame REALI con ffmpeg ai timestamp dei capitoli (da ingest.json) o
     a intervalli regolari;
  3. salva frames/frame-NNN.png + frames/manifest.json (frame -> timestamp).

I PNG risultanti vengono poi LETTI DA CLAUDE (visione nativa) per descrivere i
"passaggi mostrati". Lo script NON descrive nulla: estrae solo frame veri.

Uso:
  python scripts/frame_extractor.py --run <run-id> [--max-frames 12] [--height 360]
  python scripts/frame_extractor.py --run <run-id> --input <url>   (se manca ingest.json)

Dipendenze: yt-dlp + ffmpeg/ffprobe.
"""
import argparse
import json
import subprocess
import sys
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"


def hms(seconds):
    seconds = int(seconds or 0)
    return str(datetime.timedelta(seconds=seconds))


def have(cmd):
    from shutil import which
    return which(cmd) is not None


def download_video(url, run_dir: Path, height=360):
    """Scarica il video a bassa risoluzione (solo video, niente audio)."""
    try:
        import yt_dlp
    except ImportError:
        print("ERRORE: yt-dlp non installato.")
        sys.exit(1)
    out = run_dir / "video.%(ext)s"
    opts = {
        "format": f"bv*[height<={height}]/b[height<={height}]/worst",
        "outtmpl": str(out),
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "ignoreerrors": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
    if not info:
        return None, None
    vids = list(run_dir.glob("video.*"))
    vids = [v for v in vids if v.suffix.lower() in (".mp4", ".webm", ".mkv", ".m4v")]
    return (vids[0] if vids else None), info


def ffprobe_duration(video: Path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(video)],
            capture_output=True, text=True, timeout=30)
        return float(out.stdout.strip())
    except Exception:
        return None


def plan_timestamps(duration, chapters, max_frames, interval=None):
    """Decide a quali secondi estrarre i frame.

    Se interval e' impostato, estrae 1 frame ogni <interval> secondi
    ignorando max_frames (modalita' densa per visione reale del video).
    """
    if interval and duration:
        # modalita' densa: 1 frame ogni N secondi
        stamps = []
        t = 0.0
        while t < duration - 0.5:
            stamps.append((round(t, 1), ""))
            t += interval
        return stamps  # nessun cap: tutti i frame

    stamps = []
    if chapters:
        for c in chapters:
            st = c.get("start")
            if st is not None:
                stamps.append((float(st), c.get("title") or ""))
        # se pochi capitoli, aggiungi punti intermedi
    if len(stamps) < max_frames and duration:
        # intervalli regolari (escludi 0 e fine esatta)
        n = max_frames - len(stamps)
        step = duration / (n + 1)
        for i in range(1, n + 1):
            stamps.append((round(step * i, 1), ""))
    if not stamps and duration:
        stamps = [(round(duration * p, 1), "") for p in (0.1, 0.3, 0.5, 0.7, 0.9)]
    # dedup + ordina + cap
    seen, uniq = set(), []
    for t, label in sorted(stamps, key=lambda x: x[0]):
        key = int(t)
        if key in seen:
            continue
        seen.add(key)
        uniq.append((t, label))
    return uniq[:max_frames]


def extract_frame(video: Path, t_sec, out_png: Path):
    """Estrae UN frame al secondo t con ffmpeg (seek veloce)."""
    cmd = ["ffmpeg", "-y", "-ss", str(t_sec), "-i", str(video),
           "-frames:v", "1", "-q:v", "2", str(out_png),
           "-loglevel", "error"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return out_png.exists() and out_png.stat().st_size > 0, r.stderr


def main():
    ap = argparse.ArgumentParser(description="Estrae frame veri con ffmpeg")
    ap.add_argument("--run", required=True, help="run-id sotto runs/")
    ap.add_argument("--input", default=None, help="URL (se manca ingest.json)")
    ap.add_argument("--max-frames", type=int, default=12)
    ap.add_argument("--height", type=int, default=360)
    ap.add_argument("--interval", type=float, default=None,
                    help="Estrai 1 frame ogni N secondi (modalita' densa). "
                         "Es: --interval 2 per ~1 frame/2s. Sovrascrive --max-frames.")
    args = ap.parse_args()

    if not have("ffmpeg") or not have("ffprobe"):
        print("ERRORE: ffmpeg/ffprobe non trovati nel PATH.")
        sys.exit(1)

    run_dir = RUNS / args.run
    run_dir.mkdir(parents=True, exist_ok=True)
    ingest_path = run_dir / "ingest.json"
    ingest = json.loads(ingest_path.read_text(encoding="utf-8")) if ingest_path.exists() else {}
    url = args.input or ingest.get("url")
    if not url:
        print("ERRORE: nessun URL (passa --input o assicurati che ingest.json esista).")
        sys.exit(1)

    # 1. download a bassa risoluzione
    video = next(iter(run_dir.glob("video.*")), None)
    if not video:
        print(f"[frame] scarico video a <= {args.height}p ...")
        video, info = download_video(url, run_dir, args.height)
        if not video:
            print("[frame] ERRORE: download fallito.")
            sys.exit(2)
    print(f"[frame] video: {video.name} ({video.stat().st_size//1024} KB)")

    # 2. durata + capitoli
    duration = ingest.get("duration_sec") or ffprobe_duration(video)
    chapters = ingest.get("chapters") or []
    stamps = plan_timestamps(duration, chapters, args.max_frames, interval=args.interval)
    mode = f"intervallo {args.interval}s (densa)" if args.interval else f"capitoli/max-frames={args.max_frames}"
    print(f"[frame] durata {hms(duration)} · modalita' {mode} · estraggo {len(stamps)} frame")

    # 3. estrazione
    frames_dir = run_dir / "frames"
    frames_dir.mkdir(exist_ok=True)
    manifest = {"run": args.run, "url": url, "duration_sec": duration,
                "video_file": video.name, "frames": []}
    ok = 0
    for i, (t, label) in enumerate(stamps, 1):
        # 4 cifre se >999 frame (modalita' densa)
        pad = 4 if len(stamps) > 999 else 3
        png = frames_dir / f"frame-{i:0{pad}d}.png"
        good, err = extract_frame(video, t, png)
        if good:
            ok += 1
            manifest["frames"].append({
                "file": f"frames/{png.name}", "index": i,
                "timestamp_sec": t, "timestamp_hms": hms(t),
                "chapter": label,
                "trace": f"{ingest.get('id', 'video')}#{hms(t)} + frames/{png.name}",
            })
            if i % 50 == 0 or i <= 5:  # log ogni 50 per modalita' densa
                print(f"  + {png.name} @ {hms(t)} {('['+label+']') if label else ''}")
        else:
            print(f"  ! frame {i} fallito @ {t}s: {err.strip()[:80]}")

    (frames_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[frame] OK: {ok}/{len(stamps)} frame -> {frames_dir.relative_to(ROOT)}")
    print(f"FRAMES_DIR={frames_dir}")
    if ok == 0:
        sys.exit(3)


if __name__ == "__main__":
    main()
