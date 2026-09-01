"""Conferma il completamento ('Si') e scarica DAVVERO lo ZIP finale sul
disco locale - non ci si fida del solo testo della chat che dice 'pronto'.

Salva nell'Arsenale Caroselli (libreria dei caroselli finiti, un prodotto =
una cartella - richiesta esplicita di Max 2026-08-06), non dentro la cartella
del motore - qui vive solo il codice, non gli output."""
import os
import sys
import time
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKFLOW_DIR = os.path.dirname(PROJECT_DIR)  # "Workflow agency creative/"
AGENCY_DIR = os.path.join(WORKFLOW_DIR, "caroselli - agency")
sys.path.insert(0, AGENCY_DIR)

from ArenaAI.arena_generator import wait_for_login, dismiss_blocking_dialogs  # noqa: E402
from Core.browser_manager import BrowserManager  # noqa: E402

DEBUG_DIR = os.path.join(PROJECT_DIR, "debug_screens_factory")

# Nome cartella prodotto: passa un argomento (es. "python confirm_and_download.py Preventa
# nome-carosello") o usa il default Preventa/data-di-oggi.
PRODOTTO = sys.argv[1] if len(sys.argv) > 1 else "Preventa"
NOME_CAROSELLO = sys.argv[2] if len(sys.argv) > 2 else date.today().isoformat()
OUTPUT_DIR = os.path.join(WORKFLOW_DIR, "Arsenale Caroselli", PRODOTTO, NOME_CAROSELLO)
os.makedirs(OUTPUT_DIR, exist_ok=True)
print(f"[DOWNLOAD] Destinazione: {OUTPUT_DIR}")

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

    # Step 1: e' un "chip" inline dentro una frase ("ZIP 8 slide: [chip] -
    # 11MB..."), non un bottone isolato in una lista. get_by_text(exact=True)
    # prende l'elemento piu' piccolo con ESATTAMENTE questo testo, non
    # l'intero paragrafo che lo contiene (bug del tentativo precedente con
    # :has-text, che aggancia qualunque ancestor).
    ZIP_NAME = "Preventa_CAROSELLO_8SLIDE_ULTRA_GRAIN_4K.zip"
    zip_chip = page.get_by_text(ZIP_NAME, exact=True).last
    zip_chip.wait_for(state="visible", timeout=15000)
    zip_chip.click(force=True)
    time.sleep(2)
    page.screenshot(path=os.path.join(DEBUG_DIR, "13_preview_panel_v2.png"))
    print("[DOWNLOAD] Clic sul chip del filename fatto.")

    # Step 2: elenca TUTTI i controlli download visibili ora, prima di
    # sceglierne uno alla cieca - 2 tentativi precedenti hanno gia' mostrato
    # che esistono piu' bottoni "Download" (uno per il file, uno per l'intero
    # workspace) e serve scegliere quello giusto guardando cosa c'e' davvero.
    candidates = page.evaluate("""
        () => [...document.querySelectorAll('a, button, [role=button]')]
          .filter(el => {
            const r = el.getBoundingClientRect();
            return r.width>0 && r.height>0 && /download/i.test((el.getAttribute('aria-label')||'') + (el.textContent||''));
          })
          .map(el => {
            const r = el.getBoundingClientRect();
            return {tag: el.tagName, text: (el.textContent||'').trim().slice(0,40),
                    aria: el.getAttribute('aria-label'), x: Math.round(r.x), y: Math.round(r.y)};
          })
    """)
    print("[DOWNLOAD] Controlli download visibili ora:")
    for c in candidates:
        print(f"  {c}")

    # Preferisci quello con aria-label "Download file" (singolare, il file
    # specifico) - se non c'e', prendi l'ultimo trovato (di solito il piu'
    # vicino al pannello appena aperto, non nella sidebar/header globale).
    file_specific = [c for c in candidates if c["aria"] and "file" in c["aria"].lower()]
    target = file_specific[-1] if file_specific else (candidates[-1] if candidates else None)

    if not target:
        print("[DOWNLOAD] [X] Nessun controllo download trovato dopo il clic sul chip.")
        sys.exit(1)

    print(f"[DOWNLOAD] Uso: {target}")
    with page.expect_download(timeout=30000) as download_info:
        page.mouse.click(target["x"] + 5, target["y"] + 5)
    download = download_info.value
    dest = os.path.join(OUTPUT_DIR, download.suggested_filename or ZIP_NAME)
    download.save_as(dest)
    size = os.path.getsize(dest)
    print(f"[DOWNLOAD] Scaricato davvero: {dest} ({size} bytes)")

finally:
    manager.close()
    print("[DOWNLOAD] Fatto.")
