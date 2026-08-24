import os
import sys
import time

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-legamidiamore")
THUMB_PATH = os.path.join(FACTORY_DIR, "VIDEO-PRONTI", "video-02", "Max_a_No,_questo_soggetto_.png")

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR,
        headless=False,
        args=["--disable-blink-features=AutomationControlled", "--remote-debugging-port=9334"],
        viewport={"width": 1440, "height": 900},
        user_agent=USER_AGENT,
    )
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()
    pg.goto("https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload",
            wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_timeout(3000)

    print("Cerco riga video-02 (5 Segnali del Corpo)...")
    row = pg.locator("ytcp-video-row:has-text('5 Segnali del Corpo che Rendono')").first
    row.wait_for(timeout=20000)

    print("Attendo che l'upload/processing finisca (max 6 minuti)...")
    edit_btn = row.get_by_role("button", name="Edit draft")
    deadline = time.time() + 360
    while time.time() < deadline:
        if edit_btn.is_visible():
            uploading_text = row.locator("text=Uploading").count()
            if uploading_text == 0:
                break
        pg.wait_for_timeout(5000)
    print("Procedo (upload risulta completato o timeout raggiunto).")

    edit_btn.click()
    pg.wait_for_timeout(3000)
    pg.screenshot(path=os.path.join(FACTORY_DIR, "memory", "_v2_fix_modal_reopened.png"))

    print("Cerco selettore miniatura personalizzata...")
    try:
        pg.get_by_text("Upload thumbnail", exact=False).first.wait_for(timeout=15000)
    except Exception as e:
        print(f"[AVVISO] 'Upload thumbnail' non visibile ancora: {e}")

    thumb_input = pg.locator("input[type='file']").last
    thumb_input.set_input_files(THUMB_PATH)
    pg.wait_for_timeout(4000)
    pg.screenshot(path=os.path.join(FACTORY_DIR, "memory", "_v2_fix_after_thumb.png"))
    print(f"Miniatura impostata: {THUMB_PATH}")

    for step in range(3):
        print(f"Clic su Next (Passo {step+1}/3)...")
        pg.locator("button:has-text('Next'), button:has-text('Avanti')").first.click()
        pg.wait_for_timeout(2000)

    print("Verifico/imposto visibilita' Privato...")
    private_radio = pg.locator(
        "tp-yt-paper-radio-button[name='PRIVATE'], "
        "tp-yt-paper-radio-button:has-text('Private'), "
        "tp-yt-paper-radio-button:has-text('Privato')"
    ).first
    private_radio.click()
    pg.wait_for_timeout(1000)
    pg.screenshot(path=os.path.join(FACTORY_DIR, "memory", "_v2_fix_visibility.png"))

    print("Clic su Save/Salva...")
    pg.locator(
        "button:has-text('Save'), button:has-text('Salva'), "
        "button:has-text('Publish'), button:has-text('Pubblica'), button:has-text('Done')"
    ).first.click()
    pg.wait_for_timeout(4000)
    pg.screenshot(path=os.path.join(FACTORY_DIR, "memory", "_v2_fix_final.png"))
    print(f"URL finale: {pg.url}")

    ctx.close()
    print("FATTO.")
