import sys, time
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
URL = "https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"
VIDEO_PATH = "../VIDEO-PRONTI/video-05/video.mp4"

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
    page.goto(URL, wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(4000)
    row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
    with page.expect_file_chooser(timeout=15000) as fc_info:
        row.locator("button:has-text('Resume upload')").first.click(timeout=10000)
    file_chooser = fc_info.value
    file_chooser.set_files(VIDEO_PATH)
    print("File riselezionato, upload ripreso.")
    page.wait_for_timeout(5000)
    page.screenshot(path="../memory/_resume_interrupted_start.png")

    deadline = time.time() + 20 * 60
    while time.time() < deadline:
        page.reload(wait_until="domcontentloaded")
        page.wait_for_timeout(4000)
        row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
        txt = row.inner_text(timeout=5000)
        first = txt.splitlines()[0] if txt else "?"
        print(f"[poll] interrupted={'interrupted' in txt.lower()} pending={'Pending' in txt} private={'Private' in txt} public={'Public' in txt}")
        if "interrupted" in txt.lower():
            print("[ERRORE] Interrotto di nuovo.")
            break
        if "Pending" not in txt and "interrupted" not in txt.lower():
            print("STATO FINALE RAGGIUNTO.")
            break
        time.sleep(25)
    page.screenshot(path="../memory/_resume_interrupted_final.png")
    ctx.close()
