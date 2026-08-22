#!/usr/bin/env python3
"""Script diagnostico temporaneo: apre la dashboard Fliki gia' loggata e fa uno screenshot
reale dopo che la SPA ha finito di renderizzare (non subito, come successo in fliki_login.py).
Serve solo per la scoperta live dei selettori reali — da cancellare a scoperta completata."""
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
    time.sleep(6)
    print(f"[+] URL dopo attesa: {page.url}")
    page.screenshot(path=os.path.join(FACTORY_DIR, "memory", "fliki_discovery_1_welcome.png"))
    print("[+] Screenshot 1 salvato (welcome/dashboard)")

    # Prova a raggiungere la home/dashboard principale (non /welcome, che potrebbe essere
    # un onboarding one-shot).
    page.goto("https://app.fliki.ai/app/home", wait_until="domcontentloaded", timeout=60000)
    time.sleep(6)
    print(f"[+] URL dopo attesa (home): {page.url}")
    page.screenshot(path=os.path.join(FACTORY_DIR, "memory", "fliki_discovery_2_home.png"))
    print("[+] Screenshot 2 salvato (home)")

    context.close()
