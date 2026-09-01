"""Solo osservazione: riapre la chat Content Factory e controlla lo stato
reale (quante slide su 8 sono state generate), senza scrivere/inviare nulla."""
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

    # Scorri fino in fondo alla cronologia prima di leggere - altrimenti si
    # rischia di leggere/screenshottare un punto vecchio della chat.
    chat_log = page.locator("[role='log']").first
    for _ in range(6):
        chat_log.hover()
        page.mouse.wheel(0, 2000)
        time.sleep(0.5)
    time.sleep(1)

    page.screenshot(path=os.path.join(DEBUG_DIR, "07_status_check.png"), full_page=False)

    body_text = page.locator("body").inner_text()
    slide_count = body_text.count("/8")
    ha_8_di_8 = "8/8" in body_text
    ha_zip = ("zip" in body_text.lower()) or ("download" in body_text.lower())
    ancora_in_corso = page.locator("button svg rect").count() > 0  # icona stop = quadrato

    print(f"[STATUS] Occorrenze 'N/8' nel testo pagina: {slide_count}")
    print(f"[STATUS] Trovato '8/8' (ultima slide): {ha_8_di_8}")
    print(f"[STATUS] Menzione zip/download: {ha_zip}")
    print(f"[STATUS] Generazione ancora in corso (icona stop visibile): {ancora_in_corso}")
    print("[STATUS] --- ultimi 2000 char ---")
    print(body_text[-2000:])

finally:
    manager.close()
    print("[STATUS] Fatto.")
