import sys, re
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

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
    page.goto("https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    print("Clic su Edit draft (prima riga, la nostra)...")
    page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").locator("button:has-text('Edit draft')").first.click(timeout=15000)
    page.wait_for_timeout(4000)

    # Cicla Next finche' non vede il radio group di visibilita' reale (non il testo dello stepper)
    private_radio = page.locator("tp-yt-paper-radio-button[name='PRIVATE']")
    for step in range(8):
        if private_radio.count() > 0 and private_radio.first.is_visible():
            print(f"Radio PRIVATE visibile dopo {step} tentativi.")
            break
        print(f"Non ancora visibile, clic Next (tentativo {step+1})...")
        try:
            page.locator("button:has-text('Next'), button:has-text('Avanti')").first.click(timeout=10000)
            page.wait_for_timeout(2000)
        except Exception as e:
            print(f"Next non cliccabile: {e}")
            break
    page.wait_for_timeout(1000)
    page.screenshot(path="../memory/_resume_visibility_check.png")

    if private_radio.count() > 0:
        private_radio.first.click(timeout=10000)
        page.wait_for_timeout(1000)
        print("PRIVATE selezionato.")
        page.locator("button:has-text('Save'), button:has-text('Salva'), button:has-text('Publish'), button:has-text('Pubblica')").first.click(timeout=10000)
        page.wait_for_timeout(5000)
        print("Salvato/Pubblicato come Private.")
    else:
        print("[ERRORE] radio PRIVATE non trovato dopo i tentativi.")

    page.screenshot(path="../memory/_resume_final.png")
    print("URL finale:", page.url)
    ctx.close()
