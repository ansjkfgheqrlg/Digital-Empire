"""Riprende una generazione ferma su 'The AI took too long to respond' -
manda 'continua' nel composer (stesso, individuato via DOM contentEditable=true)
e aspetta piu' a lungo prima di richiudere."""
import os
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.join(os.path.dirname(PROJECT_DIR), "caroselli - agency")
sys.path.insert(0, AGENCY_DIR)

from ArenaAI.arena_generator import wait_for_login, dismiss_blocking_dialogs  # noqa: E402
from Core.browser_manager import BrowserManager  # noqa: E402

DEBUG_DIR = os.path.join(PROJECT_DIR, "debug_screens_factory")

manager = BrowserManager('ArenaAI', headless=False)
try:
    context = manager.get_context()
    page = manager.new_page(context)

    page.goto("https://arena.ai/", timeout=60000)
    time.sleep(4)
    dismiss_blocking_dialogs(page)
    if not wait_for_login(page):
        sys.exit(1)

    page.locator("text=Search").first.click(force=True)
    time.sleep(2)
    page.locator("button:has-text('Archived')").first.click(force=True)
    time.sleep(2)
    page.locator("text=PROMPT INGEGNERIZZATI").first.click(force=True)
    time.sleep(4)
    dismiss_blocking_dialogs(page)

    els = page.evaluate("""
        () => [...document.querySelectorAll('[contenteditable]')]
          .filter(el => el.contentEditable === 'true')
          .map(el => { const r = el.getBoundingClientRect();
            return {x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height)}; })
    """)
    if not els:
        print("[RESUME] [X] Composer non trovato.")
        page.screenshot(path=os.path.join(DEBUG_DIR, "08_no_composer.png"))
        sys.exit(1)
    t = els[0]
    cx, cy = t["x"] + t["w"] // 2, t["y"] + t["h"] // 2
    print(f"[RESUME] Composer a ({cx},{cy}).")

    page.mouse.click(cx, cy)
    time.sleep(0.5)
    page.keyboard.insert_text("continua")
    time.sleep(0.5)
    page.keyboard.press("Enter")
    print("[RESUME] 'continua' inviato. Aspetto 120s...")
    time.sleep(120)

    page.screenshot(path=os.path.join(DEBUG_DIR, "09_after_resume.png"))
    body_text = page.locator("body").inner_text()
    print(f"[RESUME] Occorrenze 'N/8': {body_text.count('/8')}")
    print(f"[RESUME] Errore timeout ancora presente: {'took too long' in body_text}")
    print("[RESUME] --- ultimi 2000 char ---")
    print(body_text[-2000:])

finally:
    manager.close()
    print("[RESUME] Fatto.")
