import time
from playwright.sync_api import sync_playwright

p = sync_playwright().start()
ctx = p.chromium.launch_persistent_context(
    user_data_dir="../chrome-profile-legamidiamore",
    headless=False,
    args=["--disable-blink-features=AutomationControlled"],
    viewport={"width": 1440, "height": 900},
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
)
pg = ctx.pages[0] if ctx.pages else ctx.new_page()
pg.goto("https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload",
        wait_until="domcontentloaded", timeout=60000)
pg.wait_for_timeout(3000)
try:
    row = pg.locator("ytcp-video-row:has-text('5 Segnali del Corpo che Rendono')").first
    row.wait_for(timeout=20000)
    row.get_by_role("button", name="Edit draft").click()
    pg.wait_for_timeout(3000)
except Exception as e:
    print(f"[avviso] {e}")

print("Finestra Chrome aperta e lasciata aperta per Max.")
while True:
    time.sleep(30)
