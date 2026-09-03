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
    page.goto("https://studio.youtube.com", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    page.get_by_text("Settings", exact=True).first.click(timeout=10000)
    page.wait_for_timeout(2000)
    page.get_by_text("Upload defaults", exact=True).first.click(timeout=8000)
    page.wait_for_timeout(2000)
    page.screenshot(path="../memory/_upload_defaults_general.png")
    # Cerca eventuale sotto-tab Monetization dentro upload defaults
    monet_tab = page.get_by_text("Monetization", exact=True)
    print("Monetization tab count:", monet_tab.count())
    if monet_tab.count() > 0:
        monet_tab.first.click(timeout=8000)
        page.wait_for_timeout(1500)
        page.screenshot(path="../memory/_upload_defaults_monetization.png")
    ctx.close()
