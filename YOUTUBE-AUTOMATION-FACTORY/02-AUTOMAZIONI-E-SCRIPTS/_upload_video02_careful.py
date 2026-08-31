import os
import sys
import re
import json
import time

from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-legamidiamore")
VIDEO_DIR = os.path.join(FACTORY_DIR, "VIDEO-PRONTI", "video-02")
VIDEO_PATH = os.path.join(VIDEO_DIR, "video.mp4")
THUMB_PATH = os.path.join(VIDEO_DIR, "Max_a_No,_questo_soggetto_.png")

with open(os.path.join(VIDEO_DIR, "metadata.json"), "r", encoding="utf-8") as f:
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

    print("Create > Upload videos...")
    pg.get_by_role("button", name="Create", exact=False).first.click()
    pg.wait_for_timeout(1000)
    pg.locator(
        "tp-yt-paper-item:has-text('Upload videos'), tp-yt-paper-item:has-text('Carica video')"
    ).first.click()
    pg.wait_for_timeout(2000)

    print("Carico il video...")
    file_input = pg.locator("input[type='file']")
    file_input.set_input_files(VIDEO_PATH)
    pg.wait_for_timeout(6000)

    print("Attendo che l'overlay/backdrop iniziale sparisca...")
    for _ in range(20):
        backdrop = pg.locator("tp-yt-iron-overlay-backdrop.opened")
        if backdrop.count() == 0:
            print("Nessun backdrop aperto, procedo.")
            break
        pg.wait_for_timeout(2000)
    else:
        print("[AVVISO] Backdrop ancora presente dopo attesa, provo comunque.")

    print("Titolo...")
    title_box = pg.locator(
        "#textbox[aria-label*='Add a title'], #textbox[aria-label*='Aggiungi un titolo']"
    ).first
    title_box.click()
    title_box.press("Control+A")
    title_box.type(metadata["title"])
    pg.wait_for_timeout(1000)

    print("Descrizione...")
    desc_box = pg.locator(
        "#textbox[aria-label*='Tell viewers'], #textbox[aria-label*='Descrivi il video']"
    ).first
    desc_box.click()
    desc_box.press("Control+A")
    desc_box.type(metadata["description"])
    pg.wait_for_timeout(1000)

    print("Attendo che l'upload video raggiunga il 100% PRIMA di continuare (fino a 6 minuti)...")
    deadline = time.time() + 360
    last_pct_text = ""
    while time.time() < deadline:
        uploading_els = pg.locator("text=/Uploading \\d+%/")
        if uploading_els.count() == 0:
            print("Nessun testo 'Uploading X%' visibile: upload video completato o non piu' mostrato.")
            break
        txt = uploading_els.first.inner_text()
        if txt != last_pct_text:
            print(f"Stato upload: {txt}")
            last_pct_text = txt
        pg.wait_for_timeout(5000)
    else:
        print("[AVVISO] Timeout raggiunto attendendo fine upload, procedo comunque.")

    print("Provo miniatura (retry paziente)...")
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
            print(f"[tentativo {attempt+1}] miniatura non pronta: {e}")
            pg.wait_for_timeout(8000)

    if not thumb_ok:
        print("[AVVISO] Miniatura non caricata durante il wizard — la aggiungero' dopo dal draft.")

    print("Imposto non per bambini...")
    pg.locator("tp-yt-paper-radio-button[name='VIDEO_MADE_FOR_KIDS_NOT_MFK']").click()
    pg.wait_for_timeout(1000)

    for step in range(3):
        print(f"Next {step+1}/3...")
        next_btn = pg.locator("button:has-text('Next'), button:has-text('Avanti')").first
        for _ in range(20):
            if next_btn.is_enabled():
                break
            pg.wait_for_timeout(3000)
        next_btn.click()
        pg.wait_for_timeout(2500)

    print("Privato...")
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
    print(f"video_id: {video_id}, thumb_ok: {thumb_ok}")
    print(f"URL finale: {pg.url}")

    pg.screenshot(path=os.path.join(FACTORY_DIR, "memory", "_c_v2_careful_final.png"))
    ctx.close()
    print("FATTO.")
