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
    for vid in VIDEO_IDS:
        print(f"--- {vid} ---")
        page.goto(f"https://studio.youtube.com/video/{vid}/monetization/ads", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)
        try:
            on_radio = page.locator("tp-yt-paper-radio-button").filter(has_text="On").first
            if on_radio.count() == 0:
                on_radio = page.get_by_text("On", exact=True).first
            on_radio.click(timeout=8000)
            page.wait_for_timeout(800)
            next_btn = page.locator("button:has-text('Next')").first
            if next_btn.count() > 0 and next_btn.is_visible():
                next_btn.click(timeout=5000)
                page.wait_for_timeout(1500)
            save_btn = page.locator("button:has-text('Save')").first
            save_btn.click(timeout=8000)
            page.wait_for_timeout(2500)
            print(f"[{vid}] Ads ON + salvato.")
        except Exception as e:
            print(f"[{vid}] ERRORE: {e}")
        page.screenshot(path=f"../memory/_ads_on2_{vid}.png")
    ctx.close()
