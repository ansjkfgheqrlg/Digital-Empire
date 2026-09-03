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
    page.goto("https://studio.youtube.com/video/6hrhlS9jC4g/edit", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    page.get_by_text("Pending", exact=True).first.click(timeout=8000)
    page.wait_for_timeout(1500)
    # Assicura Private selezionato esplicitamente
    private_radio = page.locator("tp-yt-paper-radio-button[name='PRIVATE']")
    if private_radio.count() > 0:
        private_radio.first.click(timeout=5000)
        page.wait_for_timeout(500)
    done_btn = page.locator("button:has-text('Done')").first
    done_btn.click(timeout=8000)
    page.wait_for_timeout(2000)
    print("Done cliccato.")
    save_btn = page.locator("button:has-text('Save')").first
    save_btn.click(timeout=8000)
    page.wait_for_timeout(4000)
    print("Save cliccato.")
    page.screenshot(path="../memory/_confirm_private_final.png")
    ctx.close()
