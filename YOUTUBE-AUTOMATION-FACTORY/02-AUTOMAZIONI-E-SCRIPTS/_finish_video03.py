import os
import sys
import re
import time

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-legamidiamore")
THUMB_PATH = os.path.join(FACTORY_DIR, "VIDEO-PRONTI", "video-03",
                           "1787700960160-01a03b47-68dd-76a0-b80c-9526a1a6ccf5.png")

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

    row = pg.locator("ytcp-video-row:has-text('Notare da Te')").first
    row.wait_for(timeout=20000)
    row.get_by_role("button", name="Edit draft").click()
    pg.wait_for_timeout(3000)

    thumb_ok = False
    try:
        thumb_input = pg.locator("input[type='file']").nth(1)
        thumb_input.wait_for(state="attached", timeout=10000)
        thumb_input.set_input_files(THUMB_PATH)
        pg.wait_for_timeout(3000)
        thumb_ok = True
        print("Miniatura caricata.")
    except Exception as e:
        print(f"[AVVISO] Miniatura non caricata: {e}")

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
            print(f"Next (tentativo {attempt+1})...")
            next_btn.click()
            pg.wait_for_timeout(3000)
        else:
            print("Next non abilitato, attendo processing...")
            pg.wait_for_timeout(6000)

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

    try:
        pg.wait_for_url(re.compile(r"/video/[\w-]+/"), timeout=10000)
    except Exception:
        pass
    match = re.search(r"/video/([\w-]+)/", pg.url)
    video_id = match.group(1) if match else None
    print(f"video_id: {video_id}, thumb_ok: {thumb_ok}")
    print(f"URL finale: {pg.url}")

    pg.screenshot(path=os.path.join(FACTORY_DIR, "memory", "_c_v3_finish_final.png"))
    ctx.close()
    print("FATTO.")
