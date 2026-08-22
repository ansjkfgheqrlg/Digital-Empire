#!/usr/bin/env python3
"""Apre Chrome vero sul profilo persistente Fliki e lo lascia aperto a tempo indeterminato
(nessun context.close()): il processo Python resta vivo apposta finche' non viene interrotto,
perche' chiudere il processo chiude anche il browser (Playwright lega il ciclo di vita del
browser al processo che l'ha lanciato — scoperta reale gia' fatta con Chrome/YouTube in
questa stessa sessione)."""
import os
import sys
import time

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-fliki")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR, headless=False,
        viewport={"width": 1440, "height": 900},
        args=["--disable-blink-features=AutomationControlled"],
        user_agent=USER_AGENT,
    )
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://app.fliki.ai/welcome", wait_until="domcontentloaded", timeout=60000)
    print("[+] Finestra aperta su app.fliki.ai — resta aperta, NON la chiudo da solo.")
    print("[+] Fai login/naviga tu liberamente. Il processo resta vivo per tenerla aperta.")
    while True:
        time.sleep(30)
