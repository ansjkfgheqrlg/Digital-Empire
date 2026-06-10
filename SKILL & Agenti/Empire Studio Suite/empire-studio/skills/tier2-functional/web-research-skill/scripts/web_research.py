#!/usr/bin/env python3
"""
web-research-skill / web_research.py  (REALE, no API)

Apre URL con Playwright (render JS), estrae il testo principale e cattura uno
screenshot della pagina (per la visione di Claude). Degrada con grazia: se
Playwright non e' installato, usa urllib per scaricare l'HTML grezzo e segnala
che gli screenshot non sono disponibili.

Uso:
  python web_research.py --crawl <url> --run <run-id> [--max-pages 1]
  python web_research.py --query "<q>" --run <run-id>   (registra la query da approfondire)
Output: runs/<run-id>/web/  (pagine + screenshot) + sources.json
"""
import argparse
import json
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RUNS = ROOT / "runs"


def have_playwright():
    try:
        import playwright  # noqa
        return True
    except ImportError:
        return False


def fetch_urllib(url):
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 EmpireStudio"})
    with urllib.request.urlopen(req, timeout=30) as r:
        html = r.read().decode("utf-8", errors="replace")
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:20000], None


def fetch_playwright(url, shot_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page()
        pg.goto(url, timeout=45000, wait_until="domcontentloaded")
        pg.wait_for_timeout(2000)
        text = pg.evaluate("() => document.body ? document.body.innerText : ''")
        try:
            pg.screenshot(path=str(shot_path), full_page=False)
        except Exception:
            shot_path = None
        b.close()
    return (text or "")[:20000], (str(shot_path) if shot_path else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--crawl", help="URL da aprire")
    ap.add_argument("--query", help="query da registrare per approfondimento")
    ap.add_argument("--run", required=True)
    ap.add_argument("--max-pages", type=int, default=1)
    args = ap.parse_args()
    run_dir = RUNS / args.run
    web_dir = run_dir / "web"
    web_dir.mkdir(parents=True, exist_ok=True)

    sources = {"run": args.run, "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
               "playwright": have_playwright(), "pages": []}

    if args.query:
        sources["query"] = args.query
        (run_dir / "sources.json").write_text(json.dumps(sources, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[web_research] query registrata: '{args.query}'. "
              f"web-researcher (Claude) la usera' per trovare e passare URL a --crawl.")
        return

    if not args.crawl:
        print("ERRORE: specifica --crawl <url> o --query <q>.")
        raise SystemExit(2)

    shot = web_dir / "screenshot-001.png"
    if have_playwright():
        text, shot_file = fetch_playwright(args.crawl, shot)
        mode = "playwright"
    else:
        text, shot_file = fetch_urllib(args.crawl)
        mode = "urllib (no screenshot - installa playwright per la visione)"
    (web_dir / "page-001.txt").write_text(text, encoding="utf-8")
    sources["pages"].append({"url": args.crawl, "text_file": "web/page-001.txt",
                             "screenshot": shot_file, "mode": mode,
                             "trace": f"{args.crawl} + {Path(shot_file).name if shot_file else 'no-screenshot'}"})
    (run_dir / "sources.json").write_text(json.dumps(sources, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[web_research] {args.crawl} -> {len(text)} char ({mode})")
    if shot_file:
        print(f"[web_research] screenshot: {shot_file} (Claude puo' guardarlo)")


if __name__ == "__main__":
    main()
