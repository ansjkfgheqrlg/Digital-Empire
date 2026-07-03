"""
scraper.py — S1 Acquisizione (Half A / Max).

Recupera l'annuncio mobile.de e TUTTE le foto, scrive runs/<id>/raw.json + runs/<id>/foto/.

mobile.de è protetto da Akamai Bot Manager (challenge comportamentale) che blocca il chromium
di Playwright anche in headful. Soluzione che passa in AUTOMATICO: si lancia **Google Chrome reale**
(non pilotato da Playwright) con la porta DevTools, e ci si collega via CDP (`connect_over_cdp`) per
leggere la pagina già renderizzata. Fingerprint = browser vero → Akamai passa (IP residenziale).

I dati veri NON sono in JSON-LD (mobile.de espone solo Organization/Breadcrumb): stanno in
`window.__INITIAL_STATE__ → search.vip.ads.<id>.data.ad`. Il parser (S2) li normalizza.

Modi:
  - live (default): Chrome reale + CDP.
  - manual: HTML salvato (+ cartella foto) → stesse funzioni di estrazione.
"""
from __future__ import annotations

import json
import os
import re
import socket
import subprocess
import time
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup  # type: ignore

from common import RunContext, load_config, save_json, _now_iso

BLOCK_MARKERS = (
    "zugriff verweigert", "access denied", "captcha", "unusual traffic",
    "are you a human", "px-captcha",
)
CHALLENGE_MARKERS = ("sec-if-cpt", "sec-cpt", "behavioral-content")
CONSENT_SELECTORS = [
    "button[aria-label*='Akzeptieren']",
    "button:has-text('Akzeptieren')",
    "button:has-text('Alle akzeptieren')",
    "button:has-text('Accept all')",
    "button[title*='Akzeptieren']",
    "[data-testid='gdpr-consent-accept']",
]


# --------------------------------------------------------------------------- #
# Public entrypoints
# --------------------------------------------------------------------------- #
def scrape(ctx: RunContext) -> dict[str, Any]:
    """Live: Chrome reale + CDP -> HTML renderizzato -> raw.json (+ foto)."""
    cfg = load_config()
    html, final_url = _fetch_live_cdp(ctx, cfg)
    return _build_raw(ctx, html, base_url=final_url or ctx.source_url, method="chrome-cdp")


def scrape_manual(ctx: RunContext, html_path: str, foto_dir: str | None = None) -> dict[str, Any]:
    """Fallback: HTML salvato (+ eventuale cartella foto già scaricate)."""
    html = Path(html_path).read_text(encoding="utf-8", errors="ignore")
    return _build_raw(ctx, html, base_url=ctx.source_url, method="manual", local_foto_dir=foto_dir)


# --------------------------------------------------------------------------- #
# Live fetch — Chrome reale + CDP (bypassa Akamai in automatico)
# --------------------------------------------------------------------------- #
def _fetch_live_cdp(ctx: RunContext, cfg: dict[str, Any]) -> tuple[str, str | None]:
    """Scraping via cdp.py (Chrome reale + CDP, NO Playwright): robusto ai reload della
    challenge Akamai (Runtime.evaluate non va in crash mentre la pagina naviga)."""
    import shutil
    import tempfile
    import cdp

    chrome = cfg.get("chrome_path") or cdp.find_chrome()
    if not chrome:
        raise RuntimeError(
            "Google Chrome non trovato. Installa Chrome o imposta CHROME_PATH in .env, "
            "oppure usa run.py --manual <annuncio.html> <foto_dir>."
        )

    port = cdp.free_port()
    profile = tempfile.mkdtemp(prefix="pf-chrome-")   # profilo dedicato per-run (evita lock/reuse)
    ctx.logger.info("Avvio Chrome reale (CDP :%d, headless=%s) su %s", port, cfg["headless"], chrome)
    proc = cdp.launch(chrome, port, profile, headless=cfg["headless"], url=ctx.source_url)

    html, final_url = "", ctx.source_url
    try:
        cdp.wait_devtools(port, timeout=45)
        page = cdp.Page(port)
        try:
            deadline = time.time() + max(cfg["nav_timeout_ms"] / 1000.0, 45)
            while time.time() < deadline:
                try:
                    cur = page.html()          # Runtime.evaluate: non crasha durante i reload
                except Exception:
                    cur = ""                   # pagina in navigazione → riprova
                if cur:
                    html = cur
                    low = cur.lower()
                    ready = "window.__initial_state__" in low or "application/ld+json" in low
                    challenge = any(m in low for m in CHALLENGE_MARKERS)
                    if ready and not challenge and "zugriff verweigert" not in low:
                        break
                page.scroll()
                time.sleep(1.5)
            # scroll finale per il lazy-load della gallery, poi ultima lettura
            for _ in range(5):
                page.scroll(1600)
                time.sleep(0.4)
            try:
                cur = page.html()
                if cur:
                    html = cur
            except Exception:
                pass
        finally:
            page.close()
    finally:
        cdp.kill_tree(proc)
        try:
            shutil.rmtree(profile, ignore_errors=True)
        except Exception:
            pass

    low = html.lower()
    if not html or _looks_blocked(html) or any(m in low for m in CHALLENGE_MARKERS):
        raise RuntimeError(
            "mobile.de: challenge Akamai non superata automaticamente in questo run. "
            "Riprova (di solito passa con Google Chrome + IP residenziale), oppure usa il "
            "fallback: apri l'annuncio nel tuo browser, salva la pagina come HTML e lancia "
            "run.py --manual <annuncio.html> <foto_dir>."
        )
    return html, final_url


def _find_chrome() -> str | None:
    cands = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for c in cands:
        if c and os.path.exists(c):
            return c
    import shutil
    return shutil.which("chrome") or shutil.which("google-chrome") or shutil.which("chrome.exe")


def _free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def _wait_devtools(port: int, timeout: float = 45) -> None:
    """Attende che l'endpoint DevTools di Chrome risponda (conferma che è partito davvero)."""
    deadline = time.time() + timeout
    url = f"http://127.0.0.1:{port}/json/version"
    while time.time() < deadline:
        try:
            if requests.get(url, timeout=1).ok:
                return
        except Exception:
            pass
        time.sleep(0.5)
    raise RuntimeError(
        "DevTools non risponde: Chrome non è partito o il profilo è bloccato. "
        "Chiudi eventuali Chrome zombie, o usa run.py --manual."
    )


def _kill_tree(proc) -> None:
    """Termina Chrome e tutti i processi figli (Windows: taskkill /T)."""
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            proc.terminate()
        proc.wait(timeout=8)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


def _accept_consent(page, ctx: RunContext) -> None:
    targets = [page] + list(getattr(page, "frames", []))
    for fr in targets:
        for sel in CONSENT_SELECTORS:
            try:
                el = fr.query_selector(sel)
                if el:
                    el.click(timeout=2500)
                    ctx.logger.info("Consenso GDPR accettato (%s).", sel)
                    page.wait_for_timeout(1200)
                    return
            except Exception:
                continue


def _scroll_to_load_gallery(page) -> None:
    try:
        for _ in range(6):
            page.mouse.wheel(0, 1600)
            page.wait_for_timeout(400)
    except Exception:
        pass


def _looks_blocked(html: str) -> bool:
    head = html[:6000].lower()
    return any(m in head for m in BLOCK_MARKERS)


# --------------------------------------------------------------------------- #
# Extraction (condivisa live/manual)
# --------------------------------------------------------------------------- #
def _build_raw(ctx: RunContext, html: str, base_url: str, method: str,
               local_foto_dir: str | None = None) -> dict[str, Any]:
    soup = BeautifulSoup(html, "lxml")
    warnings: list[str] = []

    ad = _extract_initial_state(html)          # dati veri mobile.de (primario)
    jsonld = _extract_jsonld(soup, warnings)   # fallback
    dom = _extract_dom(soup, warnings)         # fallback

    if ad and ad.get("galleryImages"):
        image_urls = _images_from_ad(ad)
    else:
        image_urls = _extract_image_urls(soup, jsonld, base_url, warnings)

    if not ad:
        warnings.append("window.__INITIAL_STATE__ non trovato: parser userà JSON-LD/DOM (dati ridotti)")

    raw: dict[str, Any] = {
        "source_url": ctx.source_url,
        "scraped_at": _now_iso(),
        "scrape_method": method,
        "initial_state_ad": ad,
        "jsonld": jsonld,
        "dom": dom,
        "image_urls": image_urls,
        "images": [],
        "warnings": warnings,
    }

    if local_foto_dir:
        raw["images"] = _link_local_images(local_foto_dir, ctx)
    else:
        raw["images"] = _download_images(image_urls, ctx, warnings)

    save_json(ctx.raw_path, raw)
    ctx.logger.info("raw.json: initial_state=%s, %d JSON-LD, %d foto, %d warning.",
                    "SI" if ad else "no", len(jsonld), len(raw["images"]), len(warnings))
    return raw


# --- window.__INITIAL_STATE__ (dati veri mobile.de) ------------------------- #
def _extract_initial_state(html: str) -> dict | None:
    i = html.find("window.__INITIAL_STATE__")
    if i < 0:
        return None
    eq = html.find("=", i)
    start = html.find("{", eq)
    if start < 0:
        return None
    depth = 0
    for j in range(start, len(html)):
        c = html[j]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                try:
                    data = json.loads(html[start:j + 1])
                except Exception:
                    return None
                return _find_ad(data)
    return None


def _find_ad(data: Any) -> dict | None:
    try:
        ads = data["search"]["vip"]["ads"]
        for _id, node in ads.items():
            ad = (node or {}).get("data", {}).get("ad")
            if isinstance(ad, dict) and ad.get("make"):
                return ad
    except Exception:
        pass

    def rec(o: Any) -> dict | None:
        if isinstance(o, dict):
            price = o.get("price")
            if o.get("make") and isinstance(price, dict) and "grossAmount" in price:
                return o
            for v in o.values():
                r = rec(v)
                if r:
                    return r
        elif isinstance(o, list):
            for v in o:
                r = rec(v)
                if r:
                    return r
        return None
    return rec(data)


def _images_from_ad(ad: dict) -> list[str]:
    out: list[str] = []
    for g in ad.get("galleryImages", []):
        src = g.get("src") or ""
        if not src and g.get("srcSet"):
            src = g["srcSet"].split(",")[-1].strip().split(" ")[0]
        if src:
            src = re.sub(r"rule=mo-\d+w?", "rule=mo-1600", src)
            if src not in out:
                out.append(src)
    return out


# --- fallback JSON-LD / DOM ------------------------------------------------- #
def _extract_jsonld(soup: BeautifulSoup, warnings: list[str]) -> list[dict]:
    out: list[dict] = []
    for tag in soup.find_all("script", attrs={"type": "application/ld+json"}):
        txt = tag.string or tag.get_text() or ""
        if not txt.strip():
            continue
        try:
            data = json.loads(txt)
        except json.JSONDecodeError:
            continue
        if isinstance(data, list):
            out.extend(d for d in data if isinstance(d, dict))
        elif isinstance(data, dict):
            if "@graph" in data and isinstance(data["@graph"], list):
                out.extend(d for d in data["@graph"] if isinstance(d, dict))
            else:
                out.append(data)
    return out


def _extract_image_urls(soup, jsonld: list[dict], base_url: str, warnings: list[str]) -> list[str]:
    urls: list[str] = []
    for d in jsonld:
        img = d.get("image")
        if isinstance(img, str):
            urls.append(img)
        elif isinstance(img, list):
            urls.extend(u for u in img if isinstance(u, str))
        elif isinstance(img, dict) and isinstance(img.get("url"), str):
            urls.append(img["url"])
    if not urls:
        for img in soup.find_all("img"):
            for attr in ("src", "data-src"):
                u = img.get(attr)
                if u and ("classistatic" in u or u.startswith("//")):
                    urls.append(u)
            srcset = img.get("srcset")
            if srcset:
                cand = srcset.split(",")[-1].strip().split(" ")[0]
                if cand:
                    urls.append(cand)
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u.startswith("//"):
            u = "https:" + u
        u = urljoin(base_url, u)
        if u not in seen:
            seen.add(u)
            out.append(u)
    if not out:
        warnings.append("nessuna URL immagine estratta")
    return out


GERMAN_LABELS = (
    "Erstzulassung", "Kilometerstand", "Leistung", "Kraftstoff", "Kraftstoffart",
    "Getriebe", "Fahrzeugtyp", "Kategorie", "Antriebsart", "Türen", "Sitzplätze",
    "Farbe", "Außenfarbe", "Herstellerfarbe", "Innenausstattung", "Schadstoffklasse",
    "Marke", "Modell", "Hubraum",
)


def _extract_dom(soup, warnings: list[str]) -> dict[str, Any]:
    dom: dict[str, Any] = {
        "title": None, "price_text": None, "attributes": {},
        "description": None, "equipment": [], "seller": {},
    }
    ogt = soup.find("meta", attrs={"property": "og:title"})
    if ogt and ogt.get("content"):
        dom["title"] = ogt["content"].strip()
    elif soup.find("h1"):
        dom["title"] = soup.find("h1").get_text(strip=True)

    price_text = None
    for el in soup.find_all(attrs={"data-testid": re.compile("price", re.I)}):
        t = el.get_text(" ", strip=True)
        if "€" in t or re.search(r"\d", t):
            price_text = t
            break
    dom["price_text"] = price_text

    attrs: dict[str, str] = {}
    for dt in soup.find_all("dt"):
        label = dt.get_text(" ", strip=True)
        dd = dt.find_next_sibling("dd")
        if dd and label:
            attrs[label] = dd.get_text(" ", strip=True)
    dom["attributes"] = attrs

    md = soup.find("meta", attrs={"name": "description"})
    if md and md.get("content"):
        dom["description"] = md["content"].strip()
    return dom


# --------------------------------------------------------------------------- #
# Immagini
# --------------------------------------------------------------------------- #
def _download_images(urls: list[str], ctx: RunContext, warnings: list[str]) -> list[dict]:
    images: list[dict] = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer": ctx.source_url,
    }
    for i, url in enumerate(urls):
        dest = ctx.foto_dir / f"{i:02d}.jpg"
        for attempt in range(3):
            try:
                resp = requests.get(url, headers=headers, timeout=30)
                resp.raise_for_status()
                dest.write_bytes(resp.content)
                images.append({"index": i, "original_url": url,
                               "local_path": f"foto/{dest.name}", "is_cover": i == 0})
                break
            except Exception as exc:  # noqa: BLE001
                if attempt == 2:
                    warnings.append(f"foto {i} non scaricata: {exc}")
                else:
                    time.sleep(1.2 * (attempt + 1))
    ctx.logger.info("Scaricate %d/%d foto.", len(images), len(urls))
    return images


def _link_local_images(foto_dir: str, ctx: RunContext) -> list[dict]:
    src = Path(foto_dir)
    images: list[dict] = []
    files = sorted(p for p in src.glob("*") if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"))
    for i, p in enumerate(files):
        dest = ctx.foto_dir / f"{i:02d}{p.suffix.lower()}"
        dest.write_bytes(p.read_bytes())
        images.append({"index": i, "original_url": p.as_uri(),
                       "local_path": f"foto/{dest.name}", "is_cover": i == 0})
    return images
