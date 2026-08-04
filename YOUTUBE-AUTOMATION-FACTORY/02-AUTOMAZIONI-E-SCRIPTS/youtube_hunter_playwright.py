#!/usr/bin/env python3
"""
Reparto RICERCA — agente `video-hunter-playwright`.

Entra DAVVERO su YouTube con Playwright (profilo Chrome dedicato, non quello personale: la
cronologia di chi guarda inquina i suggerimenti) e raccoglie i video reali del canale target
con views ed eta'. Scrive la stessa cache gia' usata dall'orchestratore
(`memory/channel_videos/<canale>.json`), quindi F1/F2 la leggono senza modifiche.

Perche' Playwright e non solo la lettura di ytInitialData: la pagina carica i video a scroll,
e con il browser vero si arriva a tutto il catalogo invece che ai primi 30. Il fetch statico
resta come fallback in apex7_orchestrator._fetch_channel_videos_live().

Uso:
    python youtube_hunter_playwright.py                    # @dosementale, max 60 video
    python youtube_hunter_playwright.py --handle @altro --max-video 100
    python youtube_hunter_playwright.py --visibile   # finestra vera, per diagnosticare
"""
import os
import re
import sys
import json
import time
import argparse
from datetime import datetime

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-youtube")
CACHE_DIR = os.path.join(FACTORY_DIR, "memory", "channel_videos")


def _cache_path(handle: str) -> str:
    return os.path.join(CACHE_DIR, re.sub(r"[^a-zA-Z0-9_-]", "_", handle.lstrip("@")) + ".json")


# I parser sono ANCORATI all'intera riga (^...$), non cercano un pattern dentro un testo
# qualsiasi. Motivo reale (bug trovato il 2026-08-03): il titolo "Hai 70-80 anni? SMETTI di
# camminare..." conteneva "80 anni" e veniva letto come eta' del video -> 80 anni fa -> 700.800
# ore, facendo crollare quel video da 38.6 a 0.2 views/ora. Un titolo non e' mai un metadato.
_RE_VIEWS = re.compile(
    r"^([\d.,]+)\s*(k|m|mln|mila)?\s*(?:di\s+)?(?:visualizzazioni|views?)$", re.IGNORECASE)
_RE_ETA = re.compile(r"^(\d+)\s+([a-zà-ù]+)\s+(?:fa|ago)$", re.IGNORECASE)


def _parse_views(text: str):
    """'2.2K views' -> 2200.0 · '1,4 Mln di visualizzazioni' -> 1400000.0.
    None se la riga non e' ESATTAMENTE un conteggio di visualizzazioni."""
    if not text:
        return None
    m = _RE_VIEWS.match(text.strip().replace("\xa0", " "))
    if not m:
        return None
    numero = m.group(1)
    # "1.234" e "1,234" sono separatori di migliaia; "2.2K"/"1,4 Mln" hanno il decimale.
    suffisso = (m.group(2) or "").strip().lower()
    if suffisso:
        numero = numero.replace(",", ".")
        try:
            valore = float(numero)
        except ValueError:
            return None
        moltiplicatori = {"k": 1_000, "mila": 1_000, "m": 1_000_000, "mln": 1_000_000}
        return valore * moltiplicatori.get(suffisso, 1)
    try:
        return float(re.sub(r"[.,]", "", numero))
    except ValueError:
        return None


_UNITA_ORE = {
    "hour": 1, "ora": 1, "ore": 1,
    "day": 24, "giorno": 24, "giorni": 24,
    "week": 168, "settimana": 168, "settimane": 168,
    "month": 730, "mese": 730, "mesi": 730,
    "year": 8760, "anno": 8760, "anni": 8760,
}


def _parse_eta_ore(text: str):
    """'3 weeks ago' / '12 giorni fa' -> ore. None se la riga non e' ESATTAMENTE una data
    relativa (deve finire con 'fa' o 'ago': vedi il commento sopra sul bug dei titoli)."""
    if not text:
        return None
    m = _RE_ETA.match(text.strip())
    if not m:
        return None
    n, unita = int(m.group(1)), m.group(2).lower()
    for chiave, ore in _UNITA_ORE.items():
        if unita.startswith(chiave[:4]):
            return float(n * ore)
    return None


# Estrazione volutamente INDIPENDENTE dai nomi di id/classe di YouTube: si prende il videoId dal
# primo link /watch e tutto il resto dall'innerText della card. Verificato il 2026-08-03: gli id
# storici (`a#video-title-link`, `#metadata-line span`, `.inline-metadata-item`) non esistono piu'
# e restituivano 0 video pur essendoci 36 card caricate. L'innerText invece da' righe pulite:
# ["9:51", "<titolo>", "2,4K visualizzazioni", "•", "12 giorni fa"].
_JS_ESTRAZIONE = """
    (maxVideo) => {
      const out = [];
      const visti = new Set();
      const nodi = document.querySelectorAll('ytd-rich-item-renderer, ytd-grid-video-renderer');
      for (const n of nodi) {
        const link = n.querySelector('a[href*="/watch"]');
        if (!link) continue;
        const m = (link.getAttribute('href') || '').match(/[?&]v=([\\w-]+)/);
        if (!m) continue;
        const videoId = m[1];
        if (visti.has(videoId)) continue;
        visti.add(videoId);
        const righe = (n.innerText || '').split('\\n').map(r => r.trim()).filter(Boolean);
        out.push({videoId, righe});
        if (out.length >= maxVideo) break;
      }
      return out;
    }
"""

_DURATA = re.compile(r"^\d{1,2}(:\d{2}){1,2}$")


def estrai_video(page, max_video: int) -> list[dict]:
    """Legge i video dalla pagina /videos gestendo sia lo schema legacy
    (`ytd-grid-video-renderer`) sia quello nuovo (`ytd-rich-item-renderer`)."""
    grezzi = page.evaluate(_JS_ESTRAZIONE, max_video)
    video, scartati = [], 0
    for g in grezzi:
        righe = g["righe"]
        views = next((v for r in righe if (v := _parse_views(r)) is not None), None)
        eta = next((e for r in righe if (e := _parse_eta_ore(r)) is not None), None)
        # Il titolo e' strutturalmente la riga SUBITO DOPO la durata ("9:51"). In mancanza della
        # durata (layout diverso), si prende la riga piu' lunga fra quelle non-metadato: un
        # titolo e' sempre piu' lungo di "2,4K visualizzazioni" o "12 giorni fa".
        titolo = None
        for i, riga in enumerate(righe):
            if _DURATA.match(riga) and i + 1 < len(righe):
                titolo = righe[i + 1]
                break
        if titolo is None:
            candidati = [r for r in righe
                         if not _DURATA.match(r) and r not in ("•", "-")
                         and _parse_views(r) is None and _parse_eta_ore(r) is None]
            titolo = max(candidati, key=len) if candidati else None
        if views is None or eta is None or not titolo:
            scartati += 1
            continue
        video.append({
            "videoId": g["videoId"],
            "title": titolo,
            "url": f"https://www.youtube.com/watch?v={g['videoId']}",
            "views": views,
            "age_hours": eta,
        })
    if scartati:
        print(f"[i] {scartati} elementi scartati (views o data non riconoscibili: non si inventano).")
    return video


def raccogli(handle: str, max_video: int, *, headless: bool = True) -> list[dict]:
    os.makedirs(PROFILE_DIR, exist_ok=True)
    os.makedirs(CACHE_DIR, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            headless=headless,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()
        url = f"https://www.youtube.com/{handle}/videos"
        print(f"[+] Apro {url}")
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        time.sleep(2)

        # Banner cookie (compare solo la prima volta su un profilo nuovo).
        for etichetta in ("Accetta tutto", "Accept all", "Rifiuta tutto", "Reject all"):
            try:
                page.get_by_role("button", name=etichetta).click(timeout=3000)
                print(f"[i] Banner cookie: '{etichetta}'")
                time.sleep(1.5)
                break
            except Exception:
                continue

        try:
            page.wait_for_selector("ytd-rich-item-renderer, ytd-grid-video-renderer", timeout=20000)
        except Exception:
            print("[!] Nessun video trovato nella pagina: layout cambiato o canale inesistente.")
            context.close()
            return []

        # Scroll fino a esaurimento: senza, si fermerebbe ai primi ~12 video caricati.
        precedente, fermi = 0, 0
        while fermi < 3:
            n = page.evaluate(
                "document.querySelectorAll('ytd-rich-item-renderer, ytd-grid-video-renderer').length")
            if n >= max_video:
                break
            if n == precedente:
                fermi += 1
            else:
                fermi = 0
                print(f"    ...{n} video caricati")
            precedente = n
            page.keyboard.press("End")
            time.sleep(1.5)

        video = estrai_video(page, max_video)
        context.close()
    return video


def main():
    ap = argparse.ArgumentParser(description="Raccoglie i video reali di un canale YouTube via Playwright.")
    ap.add_argument("--handle", default="@dosementale")
    ap.add_argument("--max-video", type=int, default=60)
    # Headless per DEFAULT (richiesta di Gael, 2026-08-04): una finestra del browser che si
    # apre da sola ruba il focus a chi sta lavorando. Il banner dei cookie viene gestito dal
    # codice, quindi non serve una finestra vera nemmeno al primo giro.
    ap.add_argument("--visibile", action="store_true",
                    help="Apre una finestra vera. Serve solo per capire perche' un fetch fallisce.")
    args = ap.parse_args()

    video = raccogli(args.handle, args.max_video, headless=not args.visibile)
    if not video:
        raise SystemExit("[!] Nessun video reale raccolto. Nessuna cache scritta: meglio niente "
                         "che dati inventati.")

    video.sort(key=lambda v: -(v["views"] / max(v["age_hours"], 1.0)))
    percorso = _cache_path(args.handle)
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump({"handle": args.handle, "fetched_at": datetime.now().isoformat(),
                   "fonte": "playwright", "videos": video}, f, ensure_ascii=False, indent=2)

    print(f"\n[+] {len(video)} video reali raccolti da {args.handle} → {percorso}")
    print("\n  Top 5 per velocity (views/ora):")
    for v in video[:5]:
        vph = v["views"] / max(v["age_hours"], 1.0)
        print(f"    {vph:7.1f} vph · {v['views']:>10,.0f} viste · {v['title'][:60]}")


if __name__ == "__main__":
    main()
