import os
import sys
import json
import re
import time

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-legamidiamore")
VIDEO_DIR = os.path.join(FACTORY_DIR, "VIDEO-PRONTI", "video-03")
VIDEO_PATH = os.path.join(VIDEO_DIR, "video.mp4")
THUMB_PATH = os.path.join(VIDEO_DIR, "1787700960160-01a03b47-68dd-76a0-b80c-9526a1a6ccf5.png")
META_PATH = os.path.join(VIDEO_DIR, "metadata.json")

with open(META_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

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
    pg.goto("https://studio.youtube.com", wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_timeout(4000)

    print("Clic su Create...")
    pg.get_by_role("button", name="Create", exact=False).first.click()
    pg.wait_for_timeout(1000)
    pg.locator(
        "tp-yt-paper-item:has-text('Upload videos'), tp-yt-paper-item:has-text('Carica video')"
    ).first.click()
    pg.wait_for_timeout(2000)

    print("Carico il file video...")
    file_input = pg.locator("input[type='file']")
    file_input.set_input_files(VIDEO_PATH)
    pg.wait_for_timeout(6000)

    print("Compilo titolo...")
    title_box = pg.locator(
        "#textbox[aria-label*='Add a title'], #textbox[aria-label*='Aggiungi un titolo']"
    ).first
    title_box.click()
    title_box.press("Control+A")
    title_box.type(metadata["title"])
    pg.wait_for_timeout(1000)

    print("Compilo descrizione...")
    desc_box = pg.locator(
        "#textbox[aria-label*='Tell viewers'], #textbox[aria-label*='Descrivi il video']"
    ).first
    desc_box.click()
    desc_box.press("Control+A")
    desc_box.type(metadata["description"])
    pg.wait_for_timeout(1000)

    print("Provo a caricare la miniatura (con retry paziente)...")
    thumb_ok = False
    for attempt in range(5):
        try:
            thumb_input = pg.locator("input[type='file']").nth(1)
            thumb_input.wait_for(state="attached", timeout=15000)
            thumb_input.set_input_files(THUMB_PATH)
            pg.wait_for_timeout(3000)
            thumb_ok = True
            print(f"Miniatura caricata al tentativo {attempt+1}.")
            break
        except Exception as e:
            print(f"[tentativo {attempt+1}] miniatura non pronta ancora: {e}")
            pg.wait_for_timeout(8000)

    if not thumb_ok:
        print("[AVVISO] Miniatura non caricata dopo 5 tentativi — procedo comunque, la aggiungo dopo dal draft.")

    print("Imposto non per bambini...")
    pg.locator("tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_NOT_MFK']").click()
    pg.wait_for_timeout(1000)

    for step in range(3):
        print(f"Next {step+1}/3...")
        pg.locator("button:has-text('Next'), button:has-text('Avanti')").first.click()
        pg.wait_for_timeout(2000)

    print("Imposto Privato...")
    pg.locator(
        "tp-yt-paper-radio-button[name='PRIVATE'], "
        "tp-yt-paper-radio-button:has-text('Private'), "
        "tp-yt-paper-radio-button:has-text('Privato')"
    ).first.click()
    pg.wait_for_timeout(1000)

    print("Salvo...")
    pg.locator(
        "button:has-text('Save'), button:has-text('Salva'), "
        "button:has-text('Publish'), button:has-text('Pubblica'), button:has-text('Done')"
    ).first.click()
    pg.wait_for_timeout(5000)

    try:
        pg.wait_for_url(re.compile(r"/video/[\w-]+/"), timeout=15000)
    except Exception:
        pass
    match = re.search(r"/video/([\w-]+)/", pg.url)
    video_id = match.group(1) if match else None
    print(f"video_id: {video_id}")
    print(f"URL finale: {pg.url}")

    pg.screenshot(path=os.path.join(FACTORY_DIR, "memory", "_c_v3_full_final.png"))
    ctx.close()
    print("FATTO.")
