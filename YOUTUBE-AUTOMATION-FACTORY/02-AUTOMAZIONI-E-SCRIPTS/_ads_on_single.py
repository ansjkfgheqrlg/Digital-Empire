import sys, time
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
VID = sys.argv[1]

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
    page.goto(f"https://studio.youtube.com/video/{VID}/monetization/ads", wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(3000)
    page.locator("text=Off").first.click(timeout=8000)
    page.wait_for_timeout(1000)
    page.locator("tp-yt-paper-radio-button").filter(has_text="On").first.click(timeout=8000)
    page.wait_for_timeout(1000)
    page.locator("button:has-text('Next')").first.click(timeout=8000)
    page.wait_for_timeout(2000)
    page.locator("text=Inappropriate language").first.click(timeout=8000)
    page.wait_for_timeout(1200)
    none_cb = page.get_by_text("None of the above", exact=False).first
    none_cb.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    none_cb.click(timeout=8000)
    page.wait_for_timeout(1200)
    page.screenshot(path=f"../memory/_single_{VID}_before_submit.png")
    submit_btn = page.locator("button:has-text('Submit')").first
    submit_btn.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    submit_btn.click(timeout=10000)
    page.wait_for_timeout(2500)
    page.screenshot(path=f"../memory/_single_{VID}_after_submit.png")
    save_btn = page.locator("button:has-text('Save')").first
    save_btn.click(timeout=10000)
    page.wait_for_timeout(3000)
    print(f"[{VID}] fatto.")
    page.screenshot(path=f"../memory/_single_{VID}_final.png")
    ctx.close()
