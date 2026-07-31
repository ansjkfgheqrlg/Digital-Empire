#!/usr/bin/env python3
"""Elenca i preset di sottotitoli REALI di Fliki con i loro ID.

Gli ID non sono esposti da nessuna API ne' presenti nell'HTML statico: si ottengono solo
cliccando il bottone "Copy subtitle preset ID" su fliki.ai/info/subtitle e leggendo la
clipboard. Questo script lo fa per ogni preset della pagina e stampa nome -> id.

Serve perche' il preset usato finora (`builtin-legacy-bold` + highlightSubtitles) rende i
sottotitoli UNA PAROLA ALLA VOLTA, piccoli e centrati: non leggibili per il pubblico anziano
del canale (difetto reale trovato il 2026-07-31 sul video v8).
"""
import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-fliki")
OUT_PATH = os.path.join(FACTORY_DIR, "memory", "fliki_subtitle_presets.json")


def main():
    os.makedirs(PROFILE_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    trovati = []

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            headless=False,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        context.grant_permissions(["clipboard-read", "clipboard-write"],
                                  origin="https://fliki.ai")
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://fliki.ai/info/subtitle", wait_until="networkidle", timeout=60000)
        time.sleep(2)

        bottoni = page.get_by_role("button", name="Copy subtitle preset ID")
        n = bottoni.count()
        print(f"[+] Preset trovati sulla pagina: {n}")
        for i in range(n):
            b = bottoni.nth(i)
            try:
                b.scroll_into_view_if_needed(timeout=5000)
                b.click(timeout=5000)
                time.sleep(0.4)
                preset_id = page.evaluate("navigator.clipboard.readText()")
            except Exception as e:
                print(f"[!] Preset {i}: click/clipboard fallito: {e}")
                continue
            # Il nome del preset e' il testo del contenitore attorno al bottone.
            try:
                nome = b.locator("xpath=ancestor::*[self::div or self::li][1]").inner_text(timeout=3000)
                nome = " / ".join(x.strip() for x in nome.splitlines() if x.strip())[:120]
            except Exception:
                nome = "(nome non leggibile)"
            print(f"    [{i}] {preset_id}  <-  {nome}")
            trovati.append({"indice": i, "preset_id": preset_id, "descrizione": nome})

        page.screenshot(path=os.path.join(FACTORY_DIR, "memory", "fliki_subtitle_page.png"),
                        full_page=True)
        context.close()

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(trovati, f, ensure_ascii=False, indent=2)
    print(f"[+] Salvati {len(trovati)} preset in {OUT_PATH}")


if __name__ == "__main__":
    main()
