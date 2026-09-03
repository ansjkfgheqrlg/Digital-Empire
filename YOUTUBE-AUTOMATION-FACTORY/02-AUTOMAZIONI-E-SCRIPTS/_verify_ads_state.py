import sys
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
VIDEO_IDS = ["6hrhlS9jC4g", "JOUWaLkyoN8", "-U7ZzQG1Gn8", "1td8wfINGP8"]

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
    page.on("dialog", lambda d: d.accept())
    for vid in VIDEO_IDS:
        try:
            page.goto(f"https://studio.youtube.com/video/{vid}/monetization/ads", wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(2500)
            state = page.locator("#select, ytcp-dropdown-trigger").first.inner_text(timeout=5000)
            print(f"[{vid}] stato attuale: {state.strip()}")
        except Exception as e:
            print(f"[{vid}] ERRORE lettura stato: {e}")
    ctx.close()
