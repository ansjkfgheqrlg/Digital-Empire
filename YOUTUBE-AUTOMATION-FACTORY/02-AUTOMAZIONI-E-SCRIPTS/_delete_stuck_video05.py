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
    page.goto("https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
    row.scroll_into_view_if_needed(timeout=10000)
    page.wait_for_timeout(500)
    row.hover(timeout=5000)
    page.wait_for_timeout(500)
    menu_btn = row.locator("#menu-button, ytcp-icon-button[aria-label='Options'], button[aria-label='Options']").first
    menu_btn.click(timeout=10000)
    page.wait_for_timeout(1000)
    page.screenshot(path="../memory/_delete_menu_open.png")
    delete_item = page.get_by_text("Delete forever", exact=False).first
    if delete_item.count() == 0:
        delete_item = page.get_by_text("Elimina", exact=False).first
    delete_item.click(timeout=8000)
    page.wait_for_timeout(1000)
    page.screenshot(path="../memory/_delete_confirm_dialog.png")
    confirm_btn = page.locator("button:has-text('Delete forever'), button:has-text('Elimina definitivamente')").first
    confirm_btn.click(timeout=8000)
    page.wait_for_timeout(3000)
    page.screenshot(path="../memory/_delete_done.png")
    print("Draft eliminato.")
    ctx.close()
