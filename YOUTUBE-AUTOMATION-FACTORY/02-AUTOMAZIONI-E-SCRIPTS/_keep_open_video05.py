import sys, time
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

    deadline = time.time() + 20 * 60  # max 20 minuti di attesa
    last_pct = None
    while time.time() < deadline:
        page.reload(wait_until="domcontentloaded")
        page.wait_for_timeout(3000)
        row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
        status_text = row.locator("ytcp-video-thumbnail-with-info, .thumbnail-container, .upload-progress").first
        try:
            txt = row.inner_text(timeout=5000)
        except Exception:
            txt = "?"
        print(f"[stato] {txt.splitlines()[0] if txt else txt} | contiene 'Public/Private/Draft/Pending': ", 
              "Public" in txt, "Private" in txt, "Pending" in txt, "Uploading" in txt)
        if "Uploading" not in txt and "Pending" not in txt:
            print("FINITO — non e' piu' in upload/pending.")
            page.screenshot(path="../memory/_keepopen_final.png")
            break
        time.sleep(30)
    ctx.close()
