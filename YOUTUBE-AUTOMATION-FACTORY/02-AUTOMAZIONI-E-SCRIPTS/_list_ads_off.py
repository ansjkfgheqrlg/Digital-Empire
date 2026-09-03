import sys, re
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
URL = "https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"

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
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    # scroll per caricare piu' righe
    for _ in range(5):
        page.mouse.wheel(0, 1500)
        page.wait_for_timeout(800)
    rows = page.locator("ytcp-video-row")
    n = rows.count()
    print("righe totali visibili:", n)
    ads_off_titles = []
    for i in range(n):
        row = rows.nth(i)
        try:
            txt = row.inner_text(timeout=3000)
        except Exception:
            continue
        if "Ads off" in txt:
            first_line = txt.splitlines()[0]
            ads_off_titles.append(first_line)
            print(f"ADS OFF -> {first_line}")
    print("TOTALE ads off:", len(ads_off_titles))
    ctx.close()
