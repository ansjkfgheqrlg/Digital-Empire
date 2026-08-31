import os
import sys
import time

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-legamidiamore")

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR,
        headless=False,
        args=["--disable-blink-features=AutomationControlled"],
        viewport={"width": 1440, "height": 900},
        user_agent=USER_AGENT,
    )
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()
    pg.goto("https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload",
            wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_timeout(3000)

    row = pg.locator(
        "ytcp-video-row:has-text('5 Segnali che una Donna Vuole Farsi Notare da Te')"
    ).first
    row.wait_for(timeout=20000)
    print("Riga trovata:", row.inner_text()[:80].replace("\n", " | "))

    edit_btn = row.get_by_role("button", name="Edit draft")
    if edit_btn.count() == 0:
        print("[AVVISO] Nessun bottone Edit draft su questa riga (potrebbe essere gia' pubblicato o non ancora pronto).")
        ctx.close()
        raise SystemExit(1)

    edit_btn.click()
    pg.wait_for_timeout(3000)

    for attempt in range(6):
        private_visible = pg.locator(
            "tp-yt-paper-radio-button[name='PRIVATE'], "
            "tp-yt-paper-radio-button:has-text('Private')"
        ).first
        if private_visible.is_visible():
            print("Tab Visibility raggiunto.")
            break
        next_btn = pg.locator("button:has-text('Next'), button:has-text('Avanti')").first
        if next_btn.is_visible() and next_btn.is_enabled():
            print(f"Clic su Next (tentativo {attempt+1})...")
            next_btn.click()
            pg.wait_for_timeout(2500)
        else:
            print("Next non disponibile, attendo processing...")
            pg.wait_for_timeout(4000)

    private_radio = pg.locator(
        "tp-yt-paper-radio-button[name='PRIVATE'], "
        "tp-yt-paper-radio-button:has-text('Private'), "
        "tp-yt-paper-radio-button:has-text('Privato')"
    ).first
    if private_radio.is_visible():
        private_radio.click()
        pg.wait_for_timeout(1500)
        print("Privato selezionato.")
    else:
        print("[AVVISO] Radio Private non trovato.")

    save_btn = pg.locator(
        "button:has-text('Save'), button:has-text('Salva'), "
        "button:has-text('Publish'), button:has-text('Pubblica'), button:has-text('Done')"
    ).first
    if save_btn.is_visible():
        save_btn.click()
        pg.wait_for_timeout(4000)
        print("Salvato.")
    else:
        print("[AVVISO] Bottone Save/Done non trovato.")

    pg.screenshot(path=os.path.join(FACTORY_DIR, "memory", "_c_v3_upload_final.png"))
    print(f"URL finale: {pg.url}")
    ctx.close()
    print("FATTO.")
