# -*- coding: utf-8 -*-
"""scrape_batch.py — cattura testo + risorse + vimeo-id di tutte le lezioni di outHeadline."""
import json
import os
import re
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.join(
    os.path.expanduser("~"), "AppData", "Local", "Temp", "claude",
    "c--Users-Utente-Desktop-qui-tutto-Digital-Empire",
    "089c840c-dbd9-4a6c-be69-756af5ceb502", "scratchpad", "andrei-copy-auth",
    "andrei_copy_state.json",
)

BASE = "https://www.andrei-copy.com/outheadlinedash-1"

LESSONS = [
    (1, "Sezione A - Intro", "Lezione 1 - Benvenuto", "lezione-1-benvenuto-s7dya", "3:29"),
    (2, "Sezione A - Intro", "Lezione 2 - Com'è strutturato il corso", "lezione-3-com-strutturato-il-corso-c78hs", "1:36"),
    (3, "Sezione B - Copywriting", "Lezione 3 - Cos'è il copywriting", "lezione-4-cos-il-copywriting-ny6am", "7:09"),
    (4, "Sezione B - Copywriting", "Lezione 4 - Perché il copy è importante", "lezione-5-perch-il-copy-importante-a6gw8", "6:08"),
    (5, "Sezione B - Copywriting", "Lezione 5 - Perché le persone comprano", "lezione-6-perch-le-persone-comprano-59k9m", "4:15"),
    (6, "Sezione B - Copywriting", "Lezione 6 - I tipi principali di copy [con esempi]", "lezione-7-i-tipi-principali-di-copy-con-esempi-kccsp", "4:05"),
    (7, "Sezione B - Copywriting", "Lezione 7 - Elementi chiave del copywriting persuasivo", "lezione-7-elementi-chiave-di-copywriting-persuasivo-lsw9w", "7:01"),
    (8, "Sezione B - Copywriting", "Lezione 8 - Fasi di composizione del copy", "eyyhzdskbsacwrebyzs97hm6rzc9kb-3e5jk", "2:41"),
    (9, "Sezione B - Copywriting", "Lezione 9 - Anatomia del copy", "lezione-9-anatomia-del-copy-48e29", "4:07"),
    (10, "Sezione 1 - Headline basics", "Lezione 10 - Cos'è una headline", "lezione-10-cos-una-headline-5s728", "6:53"),
    (11, "Sezione 1 - Headline basics", "Lezione 11 - L'importanza dell'attenzione", "lezione-11-limportanza-dellattenzione-84tfj", "8:40"),
    (12, "Sezione 1 - Headline basics", "Lezione 12 - APSOC framework", "lezione-12-apsoc-framework-k8hnb", "5:53"),
    (13, "Sezione 2 - Come scrivere le headline", "Lezione 13 - Le basi del headline writing", "lezione-13-le-basi-del-headline-writing-na5l9", "9:25"),
    (14, "Sezione 2 - Come scrivere le headline", "Lezione 14 - Strategie per ottenere attenzione", "lezione-14-strategie-per-ottenere-attenzione-8dx8d", "9:33"),
    (15, "Sezione 2 - Come scrivere le headline", "Lezione 15 - Metodo iterazione", "lezione-15-metodo-iterazione-bt6fw", "9:01"),
    (16, "Sezione 2 - Come scrivere le headline", "Lezione 16 - Problema VS pain point nelle headline", "lezione-16-problema-vs-pain-point-nelle-headline-6pejp", "4:36"),
    (17, "Sezione 2 - Come scrivere le headline", "Lezione 17 - Direct Response VS Storytelling nelle headline", "lezione-17-direct-response-vs-storytelling-nelle-headline-znrrr", "3:37"),
    (18, "Sezione 2 - Come scrivere le headline", "Lezione 18 - Headline urgenti", "lezione-18-headline-urgenti-6srps", "6:00"),
    (19, "Sezione 2 - Come scrivere le headline", "Lezione 19 - Livello di consapevolezza nelle headline", "lezione-19-headline-e-livello-di-consapevolezza-bcg35", "10:33"),
    (20, "Sezione 2 - Come scrivere le headline", "Lezione 20 - Attenzione logica o emotiva nella headline", "lezione-20-headline-logica-emotiva-77e3s", "6:22"),
    (21, "Sezione 2 - Come scrivere le headline", "Lezione 21 - USP nelle headline", "lezione-21-usp-in-headline-fhxz8", "1:46"),
    (22, "Sezione 2 - Come scrivere le headline", "Lezione 22 - Enfasi tipografica nelle headline", "lezione-22-enfasi-tipografica-nelle-headline-4xwtd", "4:49"),
    (23, "Sezione 2 - Come scrivere le headline", "Lezione 23 - Obiezioni nelle headline", "lezione-24-obiezioni-nelle-headline-5gsl5", "5:43"),
    (24, "Sezione 3 - La scienza dietro gli headline", "Lezione 24 - Dati scientifici sugli headline (pt. 1)", "lezione-24-dati-scientifici-sugli-headline-pt-1-gbtxj", "6:10"),
    (25, "Sezione 3 - La scienza dietro gli headline", "Lezione 25 - Dati scientifici sugli headline (pt. 2)", "lezione-25-dati-scientifici-sugli-headline-pt-2-l84wr", "8:00"),
    (26, "Sezione 3 - La scienza dietro gli headline", "Lezione 26 - Dati scientifici sugli headline (pt. 3)", "lezione-26-dati-scientifici-sugli-headline-pt-3-rkfe9", "9:24"),
    (27, "Sezione 3 - La scienza dietro gli headline", "Lezione 27 - Dati scientifici sugli headline (pt. 4)", "lezione-27-dati-scientifici-sugli-headline-pt-4-r76mx", "6:40"),
    (28, "Sezione 4 - Andrei scrive headlines", "Lezione 28 - Andrei scrive headline", "lezione-28-andrei-scrive-headline-f8ed2", "19:53"),
    (29, "Sezione 5 - Headline checklist", "Lezione 29 - Headline checklist (versione base)", "lezione-29-headline-checklist-versione-base-wlyst", "4:00"),
    (30, "Sezione 5 - Headline checklist", "Lezione 30 - Headline checklist (versione avanzata)", "lezione-30-headline-checklist-versione-avanzata-x3zwh", "6:33"),
]


def main():
    if not os.path.isfile(STATE_PATH):
        print(f"[ERRORE] sessione non trovata in {STATE_PATH}", file=sys.stderr)
        return 1

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, storage_state=STATE_PATH)
        pg = ctx.new_page()

        for n, sezione, titolo, slug, durata in LESSONS:
            out_dir = os.path.join(HERE, "lessons", f"lezione-{n:02d}")
            os.makedirs(out_dir, exist_ok=True)
            raw_path = os.path.join(out_dir, "_page_raw.txt")
            if os.path.isfile(raw_path):
                print(f"[SALTO] lezione {n:02d}: gia' catturata")
                continue

            url = f"{BASE}/{slug}"
            print(f"[{n:02d}/30] {url}")
            try:
                pg.goto(url, wait_until="networkidle", timeout=45000)
            except Exception:
                try:
                    pg.goto(url, wait_until="domcontentloaded", timeout=45000)
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
                "url": url, "slug": slug, "durata_dichiarata": durata,
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
