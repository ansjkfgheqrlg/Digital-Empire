#!/usr/bin/env python3
"""
Empire Studio - yt_ingest.py  (REALE, non stub)

Ingestion CLI per YouTube/TikTok via yt-dlp (no API, no paid).
- Singolo video: estrae info.json + auto-subs (vtt) + thumbnail (no download video).
- Canale/playlist: elenca i video, fa SCREENING per --focus (match su titolo),
  scrive videos.json. (Niente download di massa.)

Output in runs/<run-id>/ :
  info.json, <id>.<lang>.vtt (se subs), thumbnail, ingest.json (manifest)

Uso:
  python scripts/yt_ingest.py --input "https://youtu.be/XXXX" --run myrun
  python scripts/yt_ingest.py --input "https://youtube.com/@tizio" --focus design --max 15

Dipendenze: yt-dlp (pip install --user yt-dlp).
"""
import argparse
import json
import sys
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"

try:
    import yt_dlp
except ImportError:
    print("ERRORE: yt-dlp non installato. -> python -m pip install --user yt-dlp")
    sys.exit(1)


def run_id(custom=None):
    if custom:
        return custom
    return "run-" + datetime.datetime.now().strftime("%Y%m%dT%H%M%S")


def is_channel(url: str) -> bool:
    u = url.lower()
    return any(k in u for k in ["/@", "/channel/", "/c/", "/playlist", "/user/"])


def ingest_single(url, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    opts = {
        "skip_download": True,
        "writeinfojson": True,
        "writeautomaticsub": True,
        "writesubtitles": True,
        "subtitleslangs": ["en", "it", "en-US"],
        "subtitlesformat": "vtt",
        "writethumbnail": True,
        "outtmpl": str(outdir / "%(id)s.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
    if not info:
        return None
    vid = info.get("id", "unknown")
    subs = [str(p.relative_to(ROOT)) for p in outdir.glob(f"{vid}*.vtt")]
    thumbs = [str(p.relative_to(ROOT)) for p in
              list(outdir.glob(f"{vid}*.jpg")) + list(outdir.glob(f"{vid}*.webp"))]
    chapters = info.get("chapters") or []
    manifest = {
        "kind": "single-video",
        "id": vid,
        "title": info.get("title"),
        "url": info.get("webpage_url", url),
        "duration_sec": info.get("duration"),
        "uploader": info.get("uploader"),
        "chapters": [{"start": c.get("start_time"), "title": c.get("title")} for c in chapters],
        "subs": subs,
        "thumbnails": thumbs,
        "ingested_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "trace": f"yt-dlp ingest of {info.get('webpage_url', url)}",
    }
    return manifest


def ingest_channel(url, outdir: Path, focus="", maxv=15):
    outdir.mkdir(parents=True, exist_ok=True)
    opts = {
        "skip_download": True,
        "extract_flat": "in_playlist",
        "playlistend": maxv * 4,  # prendi piu' candidati, poi filtra
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    entries = (info or {}).get("entries", []) or []
    focus_l = (focus or "").lower()
    picked = []
    for e in entries:
        if not e:
            continue
        title = (e.get("title") or "")
        match = (focus_l in title.lower()) if focus_l else True
        if match:
            picked.append({
                "id": e.get("id"),
                "title": title,
                "url": e.get("url") or f"https://youtu.be/{e.get('id')}",
                "duration_sec": e.get("duration"),
                "focus_match": bool(focus_l),
            })
        if len(picked) >= maxv:
            break
    manifest = {
        "kind": "channel",
        "source_url": url,
        "focus": focus,
        "total_candidates": len(entries),
        "selected": len(picked),
        "videos": picked,
        "ingested_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "trace": f"yt-dlp screening of {url} focus='{focus}'",
    }
    return manifest


def main():
    ap = argparse.ArgumentParser(description="Empire Studio YouTube/TikTok ingestion")
    ap.add_argument("--input", required=True, help="URL video o canale/playlist")
    ap.add_argument("--run", default=None, help="run-id (default auto)")
    ap.add_argument("--focus", default="", help="parola chiave per screening canali")
    ap.add_argument("--max", type=int, default=15, help="max video da selezionare (canali)")
    args = ap.parse_args()

    rid = run_id(args.run)
    outdir = RUNS / rid
    print(f"[yt_ingest] run={rid} input={args.input}")

    if is_channel(args.input):
        manifest = ingest_channel(args.input, outdir, args.focus, args.max)
    else:
        manifest = ingest_single(args.input, outdir)

    if not manifest:
        print("[yt_ingest] ERRORE: nessuna info estratta (video privato/rimosso/offline?)")
        sys.exit(2)

    (outdir / "ingest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[yt_ingest] OK -> {(outdir / 'ingest.json').relative_to(ROOT)}")
    if manifest["kind"] == "single-video":
        print(f"  title : {manifest['title']}")
        print(f"  dur   : {manifest['duration_sec']}s · chapters: {len(manifest['chapters'])} · subs: {len(manifest['subs'])}")
    else:
        print(f"  selezionati {manifest['selected']}/{manifest['total_candidates']} (focus='{args.focus}')")
    print(f"RUN_DIR={outdir}")


if __name__ == "__main__":
    main()
