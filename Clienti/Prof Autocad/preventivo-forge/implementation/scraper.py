"""
scraper.py — S1 Acquisizione (Half A / Max).

Recupera l'HTML renderizzato di un annuncio mobile.de (Playwright) oppure da file
salvato (--manual), estrae i blob JSON-LD, le URL delle foto e i dati DOM grezzi,
scarica TUTTE le foto in runs/<id>/foto/ e scrive runs/<id>/raw.json.

NB: mobile.de ha anti-bot. Strategia: profilo persistente + UA realistico + gestione
consenso + retry. Se rilevato blocco -> errore con istruzioni per il fallback manuale.

raw.json NON è il contratto finale: lo normalizza parser.py (S2) in listing.json.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup  # type: ignore

from common import RunContext, load_config, save_json, _now_iso

BLOCK_MARKERS = (
    "Zugriff verweigert", "Access denied", "captcha", "Bitte bestätigen Sie",
    "unusual traffic", "Are you a human", "px-captcha",
)
CONSENT_SELECTORS = [
    "button[aria-label*='Akzeptieren']",
    "button:has-text('Akzeptieren')",
    "button:has-text('Alle akzeptieren')",
    "button:has-text('Accept')",
    "#gdpr-consent-accept-button",
    "[data-testid='gdpr-consent-accept']",
]


# --------------------------------------------------------------------------- #
# Public entrypoints
# --------------------------------------------------------------------------- #
def scrape(ctx: RunContext) -> dict[str, Any]:
    """Modalità live: Playwright -> HTML renderizzato -> raw.json (+ foto)."""
    cfg = load_config()
    html, final_url = _fetch_live(ctx, cfg)
    raw = _build_raw(ctx, html, base_url=final_url or ctx.source_url, method="playwright")
    return raw


def scrape_manual(ctx: RunContext, html_path: str, foto_dir: str | None = None) -> dict[str, Any]:
    """Fallback: HTML salvato (+ eventuale cartella foto già scaricate)."""
    html = Path(html_path).read_text(encoding="utf-8", errors="ignore")
    raw = _build_raw(ctx, html, base_url=ctx.source_url, method="manual",
                     local_foto_dir=foto_dir)
    return raw


# --------------------------------------------------------------------------- #
# Live fetch
# --------------------------------------------------------------------------- #
def _fetch_live(ctx: RunContext, cfg: dict[str, Any]) -> tuple[str, str | None]:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "Playwright non installato. `pip install playwright && playwright install chromium` "
            "oppure usa il fallback: run.py --manual <annuncio.html> <foto_dir>"
        ) from exc

    ctx.logger.info("Avvio browser (headless=%s)...", cfg["headless"])
    with sync_playwright() as pw:
        context = pw.chromium.launch_persistent_context(
            user_data_dir=cfg["browser_profile_dir"],
            headless=cfg["headless"],
            locale=cfg["locale"],
            user_agent=cfg["user_agent"] or None,
            viewport={"width": 1366, "height": 900},
        )
        page = context.new_page()
        page.set_default_timeout(cfg["nav_timeout_ms"])
        try:
            page.goto(ctx.source_url, wait_until="domcontentloaded")
            _accept_consent(page, ctx)
            # attende il caricamento dei dati dell'annuncio
            page.wait_for_timeout(2500)
            try:
                page.wait_for_load_state("networkidle", timeout=8000)
            except Exception:
                pass
            _scroll_to_load_gallery(page)
            html = page.content()
            final_url = page.url
        finally:
            context.close()

    if _looks_blocked(html):
        raise RuntimeError(
            "mobile.de sembra aver BLOCCATO la richiesta (anti-bot). "
            "Soluzioni: 1) imposta PLAYWRIGHT_HEADLESS=false e accetta consenso/captcha a mano "
            "(il profilo persistente resta valido per i run successivi); "
            "2) fallback manuale: salva la pagina come HTML e usa "
            "run.py --manual <annuncio.html> <foto_dir>."
        )
    return html, final_url


def _accept_consent(page, ctx: RunContext) -> None:
    for sel in CONSENT_SELECTORS:
        try:
            el = page.query_selector(sel)
            if el:
                el.click(timeout=3000)
                ctx.logger.info("Consenso GDPR accettato (%s).", sel)
                page.wait_for_timeout(1000)
                return
        except Exception:
            continue
    # consenso a volte in iframe
    for frame in page.frames:
        for sel in CONSENT_SELECTORS:
            try:
                el = frame.query_selector(sel)
                if el:
                    el.click(timeout=3000)
                    ctx.logger.info("Consenso GDPR accettato in iframe (%s).", sel)
                    page.wait_for_timeout(1000)
                    return
            except Exception:
                continue


def _scroll_to_load_gallery(page) -> None:
    """Scroll progressivo per innescare il lazy-load delle immagini."""
    try:
        for _ in range(6):
            page.mouse.wheel(0, 1600)
            page.wait_for_timeout(400)
    except Exception:
        pass


def _looks_blocked(html: str) -> bool:
    head = html[:6000]
    return any(m.lower() in head.lower() for m in BLOCK_MARKERS)


# --------------------------------------------------------------------------- #
# Extraction (condivisa live/manual)
# --------------------------------------------------------------------------- #
def _build_raw(ctx: RunContext, html: str, base_url: str, method: str,
               local_foto_dir: str | None = None) -> dict[str, Any]:
    soup = BeautifulSoup(html, "lxml")
    warnings: list[str] = []

    jsonld = _extract_jsonld(soup, warnings)
    image_urls = _extract_image_urls(soup, jsonld, base_url, warnings)
    dom = _extract_dom(soup, warnings)

    raw: dict[str, Any] = {
        "source_url": ctx.source_url,
        "scraped_at": _now_iso(),
        "scrape_method": method,
        "jsonld": jsonld,
        "dom": dom,
        "image_urls": image_urls,
        "images": [],
        "warnings": warnings,
    }

    # download / collegamento foto
    if local_foto_dir:
        raw["images"] = _link_local_images(local_foto_dir, ctx)
    else:
        raw["images"] = _download_images(image_urls, ctx, warnings)

    save_json(ctx.raw_path, raw)
    ctx.logger.info("raw.json salvato: %d JSON-LD, %d foto, %d warning.",
                    len(jsonld), len(raw["images"]), len(warnings))
    return raw


def _extract_jsonld(soup: BeautifulSoup, warnings: list[str]) -> list[dict]:
    out: list[dict] = []
    for tag in soup.find_all("script", attrs={"type": "application/ld+json"}):
        txt = tag.string or tag.get_text() or ""
        if not txt.strip():
            continue
        try:
            data = json.loads(txt)
        except json.JSONDecodeError:
            warnings.append("JSON-LD non parsabile saltato")
            continue
        if isinstance(data, list):
            out.extend(d for d in data if isinstance(d, dict))
        elif isinstance(data, dict):
            if "@graph" in data and isinstance(data["@graph"], list):
                out.extend(d for d in data["@graph"] if isinstance(d, dict))
            else:
                out.append(data)
    if not out:
        warnings.append("nessun blocco JSON-LD trovato (mobile.de potrebbe averlo cambiato)")
    return out


def _extract_image_urls(soup, jsonld: list[dict], base_url: str, warnings: list[str]) -> list[str]:
    urls: list[str] = []

    # 1) da JSON-LD (campo "image")
    for d in jsonld:
        img = d.get("image")
        if isinstance(img, str):
            urls.append(img)
        elif isinstance(img, list):
            urls.extend(u for u in img if isinstance(u, str))
        elif isinstance(img, dict) and isinstance(img.get("url"), str):
            urls.append(img["url"])

    # 2) fallback DOM: <img> e srcset nelle gallery (CDN mobile.de)
    if not urls:
        for img in soup.find_all("img"):
            for attr in ("src", "data-src"):
                u = img.get(attr)
                if u and ("classistatic" in u or "mobile.de" in u or u.startswith("//")):
                    urls.append(u)
            srcset = img.get("srcset")
            if srcset:
                # prende l'ultima (più grande) di ogni srcset
                cand = srcset.split(",")[-1].strip().split(" ")[0]
                if cand:
                    urls.append(cand)

    # normalizza + dedup mantenendo l'ordine
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u.startswith("//"):
            u = "https:" + u
        u = urljoin(base_url, u)
        # rimuove parametri di ridimensionamento comuni per ottenere la versione grande
        if u not in seen:
            seen.add(u)
            out.append(u)
    if not out:
        warnings.append("nessuna URL immagine estratta")
    return out


# Mappa label tedesche -> chiavi grezze (la normalizzazione finale è in parser.py)
GERMAN_LABELS = (
    "Erstzulassung", "Kilometerstand", "Leistung", "Kraftstoff", "Kraftstoffart",
    "Getriebe", "Fahrzeugtyp", "Kategorie", "Antriebsart", "Türen", "Sitzplätze",
    "Farbe", "Außenfarbe", "Herstellerfarbe", "Innenausstattung", "Polsterung",
    "Schadstoffklasse", "Emissionsklasse", "CO2-Emissionen", "Marke", "Modell",
    "Fahrzeug-Identifizierungsnummer", "Hubraum", "Anzahl der Vorbesitzer",
)


def _extract_dom(soup, warnings: list[str]) -> dict[str, Any]:
    dom: dict[str, Any] = {
        "title": None, "price_text": None, "attributes": {},
        "description": None, "equipment": [], "seller": {},
    }

    # titolo
    ogt = soup.find("meta", attrs={"property": "og:title"})
    if ogt and ogt.get("content"):
        dom["title"] = ogt["content"].strip()
    elif soup.find("h1"):
        dom["title"] = soup.find("h1").get_text(strip=True)

    # prezzo (testo): cerca pattern € nel documento, priorità a elementi con 'price'
    price_text = None
    for el in soup.find_all(attrs={"data-testid": re.compile("price", re.I)}):
        t = el.get_text(" ", strip=True)
        if "€" in t or re.search(r"\d", t):
            price_text = t
            break
    if not price_text:
        m = re.search(r"(?:€\s*[\d. ]{3,}|[\d. ]{3,}\s*€)", soup.get_text(" ", strip=True))
        if m:
            price_text = m.group(0)
    dom["price_text"] = price_text

    # scheda tecnica: scansione coppie label/valore (dt/dd o righe testo)
    attrs: dict[str, str] = {}
    for dt in soup.find_all("dt"):
        label = dt.get_text(" ", strip=True)
        dd = dt.find_next_sibling("dd")
        if dd and label:
            attrs[label] = dd.get_text(" ", strip=True)
    # fallback: cerca le label note nel testo e prendi il valore vicino
    if len(attrs) < 3:
        text_nodes = soup.find_all(string=re.compile("|".join(map(re.escape, GERMAN_LABELS))))
        for node in text_nodes:
            label = str(node).strip().rstrip(":")
            parent = node.parent
            val = None
            if parent:
                sib = parent.find_next_sibling()
                if sib:
                    val = sib.get_text(" ", strip=True)
            if label and val and label not in attrs:
                attrs[label] = val
    dom["attributes"] = attrs

    # descrizione: JSON-LD lo copre; qui fallback su meta description
    md = soup.find("meta", attrs={"name": "description"})
    if md and md.get("content"):
        dom["description"] = md["content"].strip()

    # equipaggiamento: liste sotto sezioni "Ausstattung"
    equipment: list[str] = []
    for ul in soup.find_all("ul"):
        items = [li.get_text(" ", strip=True) for li in ul.find_all("li")]
        items = [i for i in items if 2 < len(i) < 60]
        if 4 <= len(items) <= 80:
            equipment.extend(items)
    # dedup
    seen: set[str] = set()
    dom["equipment"] = [x for x in equipment if not (x in seen or seen.add(x))][:120]

    if not attrs:
        warnings.append("scheda tecnica (attributes) vuota: parser userà solo JSON-LD")
    return dom


# --------------------------------------------------------------------------- #
# Immagini
# --------------------------------------------------------------------------- #
def _download_images(urls: list[str], ctx: RunContext, warnings: list[str]) -> list[dict]:
    images: list[dict] = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": ctx.source_url,
    }
    for i, url in enumerate(urls):
        local_name = f"{i:02d}.jpg"
        dest = ctx.foto_dir / local_name
        for attempt in range(3):
            try:
                resp = requests.get(url, headers=headers, timeout=30)
                resp.raise_for_status()
                dest.write_bytes(resp.content)
                images.append({
                    "index": i,
                    "original_url": url,
                    "local_path": f"foto/{local_name}",
                    "is_cover": i == 0,
                })
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
    files = sorted([p for p in src.glob("*") if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")])
    for i, p in enumerate(files):
        dest = ctx.foto_dir / f"{i:02d}{p.suffix.lower()}"
        dest.write_bytes(p.read_bytes())
        images.append({
            "index": i,
            "original_url": p.as_uri(),
            "local_path": f"foto/{dest.name}",
            "is_cover": i == 0,
        })
    return images
