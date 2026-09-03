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
    page.goto("https://studio.youtube.com/channel/UC/videos/upload", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(3000)
    page.goto("https://studio.youtube.com", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    page.locator("#menu-item-1").first.click(timeout=10000)
    page.wait_for_timeout(4000)
    page.screenshot(path="../memory/_content_check.png", full_page=False)
    print(page.url)
    ctx.close()
