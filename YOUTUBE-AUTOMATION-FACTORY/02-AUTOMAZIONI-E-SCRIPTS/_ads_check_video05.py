import sys
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
VIDEO_ID = "6hrhlS9jC4g"

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
    page.goto(f"https://studio.youtube.com/video/{VIDEO_ID}/monetization/ads",
               wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(3500)
    page.screenshot(path="../memory/_v05_ads_check.png")
    body = page.inner_text("body")
    print("URL finale:", page.url)
    print("contiene 'Off':", "Off" in body)
    print("contiene 'On':", "On" in body)
    ctx.close()
