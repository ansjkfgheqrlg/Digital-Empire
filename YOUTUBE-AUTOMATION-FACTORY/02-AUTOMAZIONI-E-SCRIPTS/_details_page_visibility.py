import sys
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
    page.wait_for_timeout(5000)
    row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
    row.scroll_into_view_if_needed()
    row.hover()
    page.wait_for_timeout(800)
    pencil = row.locator("ytcp-icon-button#edit-button, ytcp-button#edit-button, [aria-label='Edit'], [aria-label='Details']").first
    if pencil.count() == 0:
        pencil = row.locator("ytcp-icon-button").first
    pencil.click(timeout=10000)
    page.wait_for_timeout(4000)
    print("URL dopo click pencil:", page.url)

    private_radio = page.locator("tp-yt-paper-radio-button[name='PRIVATE']")
    for i in range(10):
        if private_radio.count() > 0 and private_radio.first.is_visible():
            print(f"Trovato al giro {i}")
            break
        page.mouse.wheel(0, 900)
        page.wait_for_timeout(1200)
    page.screenshot(path="../memory/_scrolled_bottom.png", full_page=False)
    print("radio count finale:", private_radio.count())
    if private_radio.count() > 0:
        try:
            private_radio.first.scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            private_radio.first.click(timeout=8000)
            page.wait_for_timeout(1000)
            print("Cliccato PRIVATE.")
            page.locator("button:has-text('Save'), button:has-text('Salva'), button:has-text('Publish'), button:has-text('Pubblica')").first.click(timeout=10000)
            page.wait_for_timeout(3000)
            print("Salvato.")
        except Exception as e:
            print("errore click/save:", e)
    page.screenshot(path="../memory/_scrolled_bottom_final.png")
    ctx.close()
