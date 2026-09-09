# -*- coding: utf-8 -*-
"""
scrape_batch.py — cattura in un solo passaggio testo + risorse + vimeo-id di TUTTE le lezioni
di outFunnel (Armageddon Bundle, andrei-copy.com). Usa la sessione salvata da
competitor/Andrei Pascu/site-study/scripts/login_member_area.py (mai credenziali su disco).

Uso:
    python scrape_batch.py
"""
import json
import os
import re
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

STATE_DIR = os.environ.get(
    "ANDREI_COPY_STATE_DIR",
    os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp", "claude",
                 "c--Users-Utente-Desktop-qui-tutto-Digital-Empire",
                 "089c840c-dbd9-4a6c-be69-756af5ceb502", "scratchpad", "andrei-copy-auth"),
)
STATE_PATH = os.path.join(STATE_DIR, "andrei_copy_state.json")

LESSONS = [
    (1, "Sezione 1 - Le basi", "Lezione 1 - Cos'è un funnel", "lezione-1-cos-un-funnel-4pxk3"),
    (2, "Sezione 1 - Le basi", "Lezione 2 - Livelli di consapevolezza", "lezione-2-livelli-di-consapevolezza-nxly7"),
    (3, "Sezione 1 - Le basi", "Lezione 3 - Obiettivi che un funnel può avere", "lezione-3-obiettivi-che-un-funnel-puo-avere-9zlsg"),
    (4, "Sezione 1 - Le basi", "Lezione 4 - Come creare un funnel", "lezione-4-come-creare-un-funnel-3erfw"),
    (5, "Sezione 1 - Le basi", "Lezione 5 - Funnel reali: la situazione interessante delle vere pubblicità", "lezione-5-funnel-reali-la-situazione-interessante-delle-vere-pubblicita-x8pza"),
    (6, "Sezione 1 - Le basi", "Lezione 6 - Tipi di funnel", "lezione-6-tipi-di-funnel-73ctz"),
    (7, "Sezione 1 - Le basi", "Lezione 7 - Pezzi del puzzle", "lezione-7-pezzi-del-puzzle-yrf2p"),
    (8, "Sezione 1 - Le basi", "Lezione 8 - Step di un funnel completo", "lezione-8-step-di-un-funnel-completo-jby8b"),
    (9, "Sezione 2 - Esempi strategici", "Lezione 9 - Opzioni per il lead magnet", "lezione-9-opzioni-per-il-lead-magnet-49ryz"),
    (10, "Sezione 2 - Esempi strategici", "Lezione 10 - Tipi di sequenze automatiche e come fare follow up", "lezione-10-tipi-di-sequenze-automatiche-e-come-fare-follow-up-kb6gj"),
    (11, "Sezione 2 - Esempi strategici", "Lezione 11 - Opzioni per upsell/xell base", "lezione-11-opzioni-per-upsellxell-base-kwx9z"),
    (12, "Sezione 3 - Strategie avanzate", "Lezione 12 - Considerazioni tra gli step del funnel", "lezione-12-considerazioni-tra-gli-step-del-funnel-fyh26"),
    (13, "Sezione 3 - Strategie avanzate", "Lezione 13 - Quello che non misuri, non cresce: funnel troubleshooting", "lezione-13-quello-che-non-misuri-non-cresce-funnel-troubleshooting-p4lg8"),
    (14, "Sezione 3 - Strategie avanzate", "Lezione 14 - KPIs", "lezione-14-kpis-3jzth"),
    (15, "Sezione 3 - Strategie avanzate", "Lezione 15 - Segmentazione Audience", "lezione-15-segmentazione-audience-9h4at"),
    (16, "Sezione 3 - Strategie avanzate", "Lezione 16 - Come i funnel si evolvono col tempo", "lezione-16-come-i-funnel-si-evolvono-col-tempo-dhxde"),
    (17, "Sezione 4 - Esempi di Funnel completi", "Lezione 17 - Funnel base: Lead Magnet Funnel", "lezione-17-funnel-base-lead-magnet-funnel-eypsa"),
    (18, "Sezione 4 - Esempi di Funnel completi", "Lezione 18 - Funnel base: Sales Page Funnel", "lezione-18-funnel-base-sales-page-funnel-srwss"),
    (19, "Sezione 4 - Esempi di Funnel completi", "Lezione 19 - High-price sales team Funnel", "lezione-19-highprice-sales-team-funnel-sb4tz"),
    (20, "Sezione 4 - Esempi di Funnel completi", "Lezione 20 - Full funnel example", "lezione-20-full-funnel-example-kz4t6"),
]

BASE = "https://www.andrei-copy.com/bjrkfv9"


def main():
    if not os.path.isfile(STATE_PATH):
        print(f"[ERRORE] sessione non trovata in {STATE_PATH} — esegui login_member_area.py",
              file=sys.stderr)
        return 1

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, storage_state=STATE_PATH)
        pg = ctx.new_page()

        for n, sezione, titolo, slug in LESSONS:
            out_dir = os.path.join(HERE, "lessons", f"lezione-{n:02d}")
            os.makedirs(out_dir, exist_ok=True)
            raw_path = os.path.join(out_dir, "_page_raw.txt")
            if os.path.isfile(raw_path):
                print(f"[SALTO] lezione {n:02d}: gia' catturata")
                continue

            url = f"{BASE}/{slug}"
            print(f"[{n:02d}/20] {url}")
            try:
                pg.goto(url, wait_until="networkidle", timeout=45000)
            except Exception as e:
                print(f"  [ERRORE goto] {e}")
                continue
            pg.wait_for_timeout(2000)

            testo = pg.evaluate("() => document.body.innerText")
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(testo)

            iframes = pg.eval_on_selector_all("iframe", "els => els.map(e => e.getAttribute('src'))")
            vimeo = next((u for u in iframes if u and "vimeo" in u), None)
            vimeo_id = None
            if vimeo:
                m = re.search(r"/video/(\d+)", vimeo)
                vimeo_id = m.group(1) if m else None

            links = pg.eval_on_selector_all(
                "a[href]",
                "els => els.map(e => ({text: e.innerText.trim(), href: e.getAttribute('href')}))"
            )
            risorse = [l for l in links if l["href"] and (
                "drive.google.com" in l["href"] or l["href"].endswith((".pdf", ".png", ".jpg", ".jpeg"))
                or ("artificiale" in l["href"]) or (l["href"].startswith("http") and "andrei-copy.com" not in l["href"]
                                                     and "instagram" not in l["href"] and "youtube.com" not in l["href"]
                                                     and "tiktok" not in l["href"] and "spotify" not in l["href"])
            )]

            meta = {
                "lesson_number": n, "section": sezione, "title": titolo,
                "url": url, "slug": slug,
                "vimeo_embed": vimeo, "vimeo_id": vimeo_id,
                "risorse_esterne": risorse,
            }
            with open(os.path.join(out_dir, "_scrape_meta.json"), "w", encoding="utf-8") as f:
                json.dump(meta, f, ensure_ascii=False, indent=1)

            print(f"  [OK] testo {len(testo)} char, vimeo {vimeo_id}, {len(risorse)} risorse esterne")

        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
