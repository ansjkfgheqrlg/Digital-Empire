#!/usr/bin/env python3
"""
Automazione Playwright reale di arena.ai (ex LM Arena) per generare la copertina
del video corrente. Stesso pattern di youtube_uploader_playwright.py: profilo Chrome
persistente, login umano una tantum (Google o email), poi riuso automatico della sessione.

Modalita' "Direct" (1 modello, non Battle Mode a 2 modelli), modello "Max" (default
di Direct al momento della scrittura di questo script).
"""
import os
import time
import json
from playwright.sync_api import sync_playwright

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-arena")
OUT_DIR = os.path.join(FACTORY_DIR, "05-TEMPLATES-E-KIT")
STATUS_FILE = os.path.join(FACTORY_DIR, "memory", "arena_thumbnail_status.json")

os.makedirs(PROFILE_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)


def write_status(status: str, **extra):
    data = {"status": status, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"), **extra}
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[STATUS] {status} {extra}")


def build_prompt() -> str:
    brief_path = os.path.join(OUT_DIR, "brief-miniatura.json")
    with open(brief_path, "r", encoding="utf-8") as f:
        brief = json.load(f)
    return (
        f"YouTube thumbnail for a tutorial titled \"{brief['title']}\". "
        f"{brief['image_prompt']}. Bold high-contrast text overlay reading exactly: "
        f"\"{brief['text_overlay']}\". Visual concept: {brief['concept']}. "
        "Dark minimal terminal/console aesthetic with warm orange accent (#fb4604), "
        "tech coding tutorial vibe, clickable, high CTR, 16:9 aspect ratio."
    )


def click_first_visible(locator, timeout=5000):
    n = locator.count()
    for i in range(n):
        el = locator.nth(i)
        if el.is_visible():
            el.click(timeout=timeout)
            return True
    return False


def select_direct_mode(page):
    """Passa da Battle Mode (default) a Direct — 1 solo modello, non 2 in parallelo.
    Il modello resta quello di default di Direct (oggi 'Max')."""
    opened = click_first_visible(page.locator("button:has-text('Battle Mode')"))
    if not opened:
        write_status("avviso", messaggio="Bottone modalita' non trovato, provo a proseguire comunque")
        return
    time.sleep(0.5)
    page.get_by_role("option", name="Direct", exact=False).click(timeout=5000)
    time.sleep(0.5)


def enter_image_mode_and_send(page, prompt):
    try:
        page.locator("form button[aria-label='Image']").click(timeout=8000)
    except Exception:
        pass
    time.sleep(0.5)
    textbox = page.locator("textarea, [contenteditable='true']").first
    textbox.click()
    textbox.fill(prompt)
    time.sleep(0.3)
    page.locator("form button[aria-label='Send message']").click()


def main():
    prompt = build_prompt()
    write_status("avviato", prompt=prompt[:200])

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            headless=False,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://arena.ai", wait_until="networkidle", timeout=30000)
        time.sleep(1.5)

        try:
            page.get_by_text("Accept Cookies", exact=True).click(timeout=4000)
        except Exception:
            pass

        select_direct_mode(page)
        enter_image_mode_and_send(page, prompt)
        time.sleep(2)

        # Terms of Use al primo utilizzo
        try:
            agree = page.get_by_role("button", name="Agree")
            agree.wait_for(state="visible", timeout=4000)
            agree.click()
            time.sleep(1)
        except Exception:
            pass

        # Login richiesto? Attesa nativa di Playwright (wait_for state=hidden).
        google_btn = page.get_by_role("button", name="Continue with Google")
        if google_btn.is_visible():
            write_status("attesa_login", messaggio="Login manuale richiesto nella finestra Chrome aperta — attendo fino a 15 minuti")
            try:
                google_btn.wait_for(state="hidden", timeout=900000)
            except Exception:
                write_status("timeout_login")
                context.close()
                return
            write_status("login_completato")
            page.goto("https://arena.ai", wait_until="networkidle", timeout=30000)
            time.sleep(1.5)
            select_direct_mode(page)
            enter_image_mode_and_send(page, prompt)

        write_status("generazione_in_corso")
        # Direct = 1 solo modello: un solo placeholder "Generating image..." da attendere.
        waited = 0
        max_wait = 180
        pending = 1
        while waited < max_wait:
            pending = page.get_by_text("Generating image...").count()
            if pending == 0:
                break
            time.sleep(3)
            waited += 3
        write_status("attesa_generazione_terminata", secondi_attesi=waited, pending_residui=pending)
        time.sleep(3)  # margine per il rendering completo dopo la sparizione del placeholder

        saved = []
        imgs = page.locator("img")
        n = imgs.count()
        debug_sizes = []
        for i in range(n):
            img = imgs.nth(i)
            box = img.bounding_box()
            debug_sizes.append({"i": i, "src": (img.get_attribute("src") or "")[:60], "box": box})
        write_status("debug_immagini_trovate", n_totale=n, dettagli=debug_sizes)

        for i in range(n):
            img = imgs.nth(i)
            src = img.get_attribute("src") or ""
            box = img.bounding_box()
            if not box or box["width"] < 150 or box["height"] < 100:
                continue  # scarta icone/avatar piccoli
            out_path = os.path.join(OUT_DIR, f"copertina-arena-candidata-{len(saved)+1}.png")
            try:
                if src.startswith("http"):
                    resp = page.request.get(src)
                    with open(out_path, "wb") as f:
                        f.write(resp.body())
                else:
                    img.screenshot(path=out_path)
                saved.append(out_path)
            except Exception as e:
                print(f"[!] Impossibile salvare immagine {i}: {e}")

        page.screenshot(path=os.path.join(OUT_DIR, "arena_debug_final.png"), full_page=True)
        write_status("completato", immagini_salvate=saved)
        context.close()


if __name__ == "__main__":
    main()
