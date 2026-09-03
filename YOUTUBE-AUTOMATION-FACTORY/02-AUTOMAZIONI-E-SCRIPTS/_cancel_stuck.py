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
    page.wait_for_timeout(3000)
    row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
    print("Riga trovata:", row.count() > 0)
    cancel_btn = row.locator("button:has-text('Cancel upload')").first
    if cancel_btn.count() > 0:
        cancel_btn.click(timeout=10000)
        page.wait_for_timeout(1500)
        # conferma eventuale dialog
        confirm = page.locator("button:has-text('Cancel'), button:has-text('Delete'), button:has-text('Yes')").first
        try:
            confirm.click(timeout=5000)
        except Exception:
            pass
        page.wait_for_timeout(3000)
        print("Upload bloccato cancellato.")
    else:
        print("Nessun bottone Cancel upload trovato (forse gia' finito o gia' cambiato stato).")
    page.screenshot(path="../memory/_after_cancel.png")
    ctx.close()
