# -*- coding: utf-8 -*-
"""
esplora_member_area.py — usa la sessione salvata per mappare l'area membri: quali pagine
esistono dentro ogni prodotto (Armageddon Bundle, Claude Speedrun 2, Copywriting Mentorship),
e ne stampa gli URL reali.

Uso:
    python esplora_member_area.py
"""
import json
import os
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
AUTH = os.path.join(BASE, "auth")
STATE_PATH = os.path.join(AUTH, "andrei_copy_state.json")
DASHBOARD_URL = "https://www.andrei-copy.com/armageddon-dashboard"


def main():
    if not os.path.isfile(STATE_PATH):
        print("[ERRORE] manca auth/andrei_copy_state.json — esegui prima login_member_area.py",
              file=sys.stderr)
        return 1

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, storage_state=STATE_PATH)
        pg = ctx.new_page()
        pg.goto(DASHBOARD_URL, wait_until="networkidle", timeout=45000)
        pg.wait_for_timeout(2000)
        pg.screenshot(path=os.path.join(AUTH, "_dashboard_loggato.png"), full_page=True)

        html = pg.content()
        if "solo per i membri" in html and "Esci" not in html:
            print("[ATTENZIONE] sembra ancora bloccato dal paywall — screenshot salvato per controllo")

        # apri il pannello "Prodotti digitali" se non e' gia' aperto
        try:
            pg.get_by_text("Prodotti digitali", exact=False).first.click(timeout=3000)
            pg.wait_for_timeout(800)
        except Exception:
            pass

        # espandi ogni dropdown "Pagine"
        chevrons = pg.locator("text=Pagine")
        n = chevrons.count()
        print(f"[INFO] trovati {n} blocchi 'Pagine'")
        for i in range(n):
            try:
                chevrons.nth(i).click(timeout=2000)
                pg.wait_for_timeout(500)
            except Exception as e:
                print(f"  [salto {i}] {e}")

        pg.wait_for_timeout(800)
        pg.screenshot(path=os.path.join(AUTH, "_dashboard_espanso.png"), full_page=True)

        # raccogli tutti i link visibili nel pannello / pagina
        links = pg.eval_on_selector_all(
            "a[href]",
            "els => els.map(e => ({text: e.innerText.trim(), href: e.getAttribute('href')}))"
        )
        utili = [l for l in links if l["text"] and l["href"] and not l["href"].startswith("#")]
        with open(os.path.join(AUTH, "_link_area_membri.json"), "w", encoding="utf-8") as f:
            json.dump(utili, f, ensure_ascii=False, indent=1)

        print(f"[OK] {len(utili)} link salvati in auth/_link_area_membri.json")
        for l in utili:
            print(f"  {l['text']!r:50s} -> {l['href']}")

        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
