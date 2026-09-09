# -*- coding: utf-8 -*-
"""Clicca sulla card outFunnel nella dashboard membri e stampa dove porta."""
import json
import os
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
AUTH = os.path.join(BASE, "auth")
STATE_PATH = os.path.join(AUTH, "andrei_copy_state.json")
DASHBOARD_URL = "https://www.andrei-copy.com/armageddon-dashboard"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, storage_state=STATE_PATH)
    pg = ctx.new_page()
    pg.goto(DASHBOARD_URL, wait_until="networkidle", timeout=45000)
    pg.wait_for_timeout(1500)

    # tutte le card con link, anche senza testo (immagini/loghi)
    cards = pg.eval_on_selector_all(
        "a[href]",
        "els => els.map(e => ({text: e.innerText.trim(), href: e.getAttribute('href'), "
        "cls: e.className, hasImg: !!e.querySelector('img,svg')}))"
    )
    with open(os.path.join(AUTH, "_tutti_i_link.json"), "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=1)
    print(f"[INFO] {len(cards)} link totali (con e senza testo) salvati in _tutti_i_link.json")

    try:
        card = pg.locator("text=outFunnel").first
        card.wait_for(state="visible", timeout=5000)
        # sali al piu' vicino <a> antenato, se c'e'
        href = card.evaluate("el => { const a = el.closest('a'); return a ? a.getAttribute('href') : null; }")
        print(f"[INFO] href card outFunnel: {href}")
        card.click(timeout=5000)
        pg.wait_for_timeout(2500)
        print(f"[INFO] URL dopo click: {pg.url}")
        pg.screenshot(path=os.path.join(AUTH, "_outfunnel_dopo_click.png"), full_page=True)
        with open(os.path.join(AUTH, "_outfunnel_dopo_click.html"), "w", encoding="utf-8") as f:
            f.write(pg.content())
    except Exception as e:
        print(f"[ERRORE] {e}", file=sys.stderr)
        pg.screenshot(path=os.path.join(AUTH, "_outfunnel_errore.png"), full_page=True)

    browser.close()
