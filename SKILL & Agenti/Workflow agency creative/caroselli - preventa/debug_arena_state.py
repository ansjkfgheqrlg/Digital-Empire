"""
Diagnostica una tantum (non fa parte del flusso): 1 solo prompt, screenshot reali
a ogni step, per vedere DAVVERO cosa succede su Arena dopo l'invio del prompt.
Motivo: 2 run complete (9 tentativi totali) hanno prodotto 0 immagini senza
nessun errore nel log - serve vedere lo schermo, non indovinare dal testo.
"""
import os
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.join(os.path.dirname(PROJECT_DIR), "caroselli - agency")
sys.path.insert(0, AGENCY_DIR)

from ArenaAI.arena_generator import wait_for_login, setup_arena_chat, solve_arena_captcha, dismiss_blocking_dialogs  # noqa: E402
from Core.browser_manager import BrowserManager  # noqa: E402

DEBUG_DIR = os.path.join(PROJECT_DIR, "debug_screens")
os.makedirs(DEBUG_DIR, exist_ok=True)

manager = BrowserManager('ArenaAI-Debug', headless=False)
try:
    context = manager.get_context()
    page = manager.new_page(context)

    page.goto("https://arena.ai/", timeout=60000)
    time.sleep(5)
    page.screenshot(path=os.path.join(DEBUG_DIR, "01_home.png"))

    if not wait_for_login(page):
        print("[DEBUG] Login non completato.")
        sys.exit(1)
    page.screenshot(path=os.path.join(DEBUG_DIR, "02_after_login.png"))

    setup_arena_chat(page)
    page.screenshot(path=os.path.join(DEBUG_DIR, "03_after_setup.png"))

    prompt = "Genera la slide 1. Testo: 'test diagnostico'. Regole: grafica perfetta, gradiente #062155/#edeebe, font elegante, NO testo eccessivo."
    textarea = page.locator("textarea").first
    solve_arena_captcha(page)
    textarea.click(force=True)
    textarea.fill("")
    textarea.type(prompt, delay=30)
    time.sleep(2)
    page.screenshot(path=os.path.join(DEBUG_DIR, "04_before_submit.png"))

    submit_selector = "button[type='submit'], button:has(svg path[d*='M6 12L3.269 3.126'])"
    submit_btn = page.locator(submit_selector).last
    print(f"[DEBUG] submit_btn count visibili: {page.locator(submit_selector).count()}")
    submit_btn.click(force=True)
    time.sleep(2)
    if dismiss_blocking_dialogs(page, timeout_ms=2000):
        print("[DEBUG] Gate Terms of Use dismesso — reinvio il prompt.")
        textarea.click(force=True)
        time.sleep(1)
        submit_btn.click(force=True)
    print("[DEBUG] Prompt inviato, aspetto 15s...")
    time.sleep(15)
    page.screenshot(path=os.path.join(DEBUG_DIR, "05_after_submit_15s.png"))

    print("[DEBUG] Aspetto altri 30s (45s totali)...")
    time.sleep(30)
    page.screenshot(path=os.path.join(DEBUG_DIR, "06_after_submit_45s.png"))

    imgs = page.locator("img, canvas").all()
    print(f"[DEBUG] Elementi img/canvas trovati: {len(imgs)}")
    for i, el in enumerate(imgs):
        try:
            box = el.bounding_box()
            src = el.get_attribute("src") or "(no src / canvas)"
            print(f"  [{i}] box={box} src={src[:80]}")
        except Exception as e:
            print(f"  [{i}] errore lettura: {e}")

    body_text = page.locator("body").inner_text()[:1500]
    print("[DEBUG] --- testo pagina (primi 1500 char) ---")
    print(body_text)

finally:
    manager.close()
    print("[DEBUG] Fatto. Screenshot in:", DEBUG_DIR)
