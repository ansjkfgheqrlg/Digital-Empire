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
        print(f"=== {vid} ===")
        try:
            page.goto(f"https://studio.youtube.com/video/{vid}/monetization/ads", wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(3000)
            current = page.locator("#select, ytcp-dropdown-trigger").first
            txt_now = page.locator("text=On").count()
            if page.locator("text=Off").first.count() > 0 and page.locator("tp-yt-paper-radio-button").count() == 0:
                # ancora collassato su Off (non gia' On)
                page.locator("text=Off").first.click(timeout=8000)
                page.wait_for_timeout(800)
                page.locator("tp-yt-paper-radio-button").filter(has_text="On").first.click(timeout=8000)
                page.wait_for_timeout(800)
                page.locator("button:has-text('Next')").first.click(timeout=8000)
                page.wait_for_timeout(1500)
                # Questionario "Tell us what's in your video"
                none_cb = page.get_by_text("None of the above", exact=False)
                if none_cb.count() == 0:
                    # apri una categoria per far comparire il checkbox riassuntivo
                    page.locator("text=Inappropriate language").first.click(timeout=8000)
                    page.wait_for_timeout(1000)
                    none_cb = page.get_by_text("None of the above", exact=False)
                none_cb.first.scroll_into_view_if_needed()
                none_cb.first.click(timeout=8000)
                page.wait_for_timeout(1000)
                page.locator("button:has-text('Submit')").first.click(timeout=8000)
                page.wait_for_timeout(2000)
            else:
                print(f"[{vid}] gia' su On (o stato inatteso), salto la parte On/questionario.")

            save_btn = page.locator("button:has-text('Save')").first
            if save_btn.count() > 0 and save_btn.is_enabled():
                save_btn.click(timeout=8000)
                page.wait_for_timeout(2500)
                print(f"[{vid}] SALVATO.")
            else:
                print(f"[{vid}] Save non abilitato/non trovato — verifica manuale.")
        except Exception as e:
            print(f"[{vid}] ERRORE: {e}")
        page.screenshot(path=f"../memory/_ads_final_{vid}.png")

    ctx.close()
