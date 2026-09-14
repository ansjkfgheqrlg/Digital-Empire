#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apri_studio_visibile.py — apre YouTube Studio in una finestra VISIBILE sul profilo Chrome con
cui la fabbrica carica (lo stesso di apex7_orchestrator CANALI["legamidiamore"]), e aspetta
che Max chiuda la finestra.

Serve per i gesti che solo Max puo' fare e che la macchina non deve nemmeno tentare:
  - il popup Google «Verify it's you» (14/9/2026: e' comparso SOPRA il wizard di caricamento di
    video-06 e ha bloccato l'upload al 10%: la macchina non ha, e non deve avere, cio' che
    Google chiede per confermare l'identita');
  - «Accept updated YouTube Partner Program terms» (banner rosso in cima a Studio);
  - completare o cancellare le BOZZE lasciate da un wizard interrotto (Content → filtro
    Bozze): oggi RUg6TgSd79s e, con ogni probabilita', una seconda bozza di video-06.

Non legge, non scrive, non clicca: apre e aspetta. Quando la finestra viene chiusa, esce.
Dopo, `python legamidiamore_session_check.py` dice se la sessione e' buona e
`python carica_pronti.py --prova` dice cosa e' ancora da caricare.

Uso:
    python apri_studio_visibile.py            # dashboard di Studio
    python apri_studio_visibile.py --bozze    # direttamente sull'elenco contenuti (per le bozze)
"""
import os
import sys

from playwright.sync_api import sync_playwright

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
try:
    from apex7_orchestrator import CANALI as _CANALI
    _PROFILO = _CANALI["legamidiamore"].get("chrome_profile_dir") or "chrome-profile-youtube"
except Exception:
    _PROFILO = "chrome-profile-youtube"
PROFILE_DIR = os.path.join(FACTORY_DIR, _PROFILO)

# Stesso User-Agent degli altri script della fabbrica: senza, Studio mostra "browser non
# supportato" (bug reale del 2026-08-05, vedi legamidiamore_session_check.py).
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/131.0.0.0 Safari/537.36")


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    url = ("https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"
           if "--bozze" in argv else "https://studio.youtube.com")
    if not os.path.isdir(PROFILE_DIR):
        print("[ERRORE] Profilo non trovato: %s" % PROFILE_DIR)
        return 1
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR, headless=False,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"], user_agent=USER_AGENT)
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        print("=" * 70)
        print("FINESTRA APERTA sul profilo: %s" % os.path.basename(PROFILE_DIR))
        print("Fai quello che serve (Verify it's you / termini YPP / bozze) e CHIUDI la finestra.")
        print("Qui non si clicca niente: aspetto solo che tu chiuda.")
        print("=" * 70)
        try:
            page.wait_for_event("close", timeout=0)
        except Exception:
            pass
        try:
            context.close()
        except Exception:
            pass
    print("Finestra chiusa. Ora: python legamidiamore_session_check.py  (poi carica_pronti.py --prova)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
