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
    vis_dropdown = page.locator("text=Visibility").locator("xpath=following::*[contains(@class,'dropdown') or self::ytcp-select or self::tp-yt-paper-menu-button][1]").first
    # fallback semplice: cerca il testo Pending vicino a Visibility e cliccalo
    pending_ctrl = page.locator("ytcp-video-visibility-select, [aria-label*='Visibility'], #visibility").first
    print("pending_ctrl count:", pending_ctrl.count())
    try:
        pending_ctrl.click(timeout=8000)
    except Exception as e:
        print("primo selettore fallito:", e)
        page.get_by_text("Pending", exact=True).first.click(timeout=8000)
    page.wait_for_timeout(1500)
    page.screenshot(path="../memory/_vis_menu_open.png")
    ctx.close()
