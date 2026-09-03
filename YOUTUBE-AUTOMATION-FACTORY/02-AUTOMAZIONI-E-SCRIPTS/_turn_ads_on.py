import sys
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

VIDEO_IDS = {
    "JOUWaLkyoN8": "5 Segnali del Corpo che Rendono un UOMO Irresistibile",
}

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
    for vid, title in VIDEO_IDS.items():
        page.goto(f"https://studio.youtube.com/video/{vid}/monetization/ads", wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)
        dropdown = page.locator("ytcp-dropdown-trigger, #select, tp-yt-paper-menu-button").first
        print(f"[{vid}] {title} - apro dropdown Off...")
        page.get_by_text("Off", exact=True).first.click(timeout=8000)
        page.wait_for_timeout(1500)
        page.screenshot(path=f"../memory/_ads_dropdown_{vid}.png")
    ctx.close()
