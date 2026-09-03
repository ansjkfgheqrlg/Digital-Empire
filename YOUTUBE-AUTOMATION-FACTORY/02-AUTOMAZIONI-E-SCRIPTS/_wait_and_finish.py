import sys, time
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
URL = "https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir="../chrome-profile-youtube",
        channel="chrome",
        headless=False,
        args=["--disable-blink-features=AutomationControlled"],
        viewport={"width": 1440, "height": 900},
        user_agent=USER_AGENT,
    )
    page = ctx.new_page()
    deadline = time.time() + 15*60
    found = False
    while time.time() < deadline:
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(4000)
        row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
        txt = row.inner_text(timeout=5000)
        first_line = txt.splitlines()[0] if txt else "?"
        has_edit_draft = row.locator("button:has-text('Edit draft')").count() > 0
        print(f"[poll] '{first_line}' | Edit draft disponibile: {has_edit_draft} | testo: {txt[:120].replace(chr(10),' | ')}")
        if has_edit_draft:
            found = True
            break
        time.sleep(20)

    if found:
        row.locator("button:has-text('Edit draft')").first.click(timeout=15000)
        page.wait_for_timeout(4000)
        private_radio = page.locator("tp-yt-paper-radio-button[name='PRIVATE']")
        for step in range(8):
            if private_radio.count() > 0 and private_radio.first.is_visible():
                print(f"Radio PRIVATE visibile dopo {step} tentativi.")
                break
            try:
                page.locator("button:has-text('Next'), button:has-text('Avanti')").first.click(timeout=8000)
                page.wait_for_timeout(2000)
            except Exception as e:
                print("Next fallito:", e)
                break
        if private_radio.count() > 0 and private_radio.first.is_visible():
            private_radio.first.click(timeout=8000)
            page.wait_for_timeout(1000)
            page.locator("button:has-text('Save'), button:has-text('Salva'), button:has-text('Publish'), button:has-text('Pubblica')").first.click(timeout=10000)
            page.wait_for_timeout(4000)
            print("SALVATO COME PRIVATE.")
        else:
            print("[ERRORE] radio non trovato neanche stavolta.")
    else:
        print("[TIMEOUT] Edit draft mai apparso in 15 minuti.")

    page.screenshot(path="../memory/_wait_and_finish_final.png")
    print("URL finale:", page.url)
    ctx.close()
