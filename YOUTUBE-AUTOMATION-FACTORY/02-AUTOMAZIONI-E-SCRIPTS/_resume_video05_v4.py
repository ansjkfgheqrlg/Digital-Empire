import sys, time
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
VIDEO_PATH = r"C:\Users\Utente\Desktop\qui tutto\Digital Empire\YOUTUBE-AUTOMATION-FACTORY\VIDEO-PRONTI\video-05\video.mp4"

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

    # Il bottone "Resume upload" vive SOLO nella riga della lista Content, non nella
    # pagina /edit (v3 lo ha cercato li' e non l'ha trovato, restando fermo 30 min senza
    # far nulla). Si parte quindi dalla lista, come nel primo tentativo riuscito.
    page.goto("https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
    row.scroll_into_view_if_needed(timeout=10000)
    row.hover(timeout=5000)
    page.wait_for_timeout(500)
    page.screenshot(path="../memory/_v4_list_before.png")

    resume_btn = row.get_by_text("Resume upload", exact=False).first
    resume_btn.click(timeout=10000)
    page.wait_for_timeout(1500)
    file_input = page.locator("input[type='file']")
    file_input.set_input_files(VIDEO_PATH, timeout=15000)
    page.wait_for_timeout(3000)
    page.screenshot(path="../memory/_v4_after_resume.png")
    print("Resume upload avviato (v4). Da qui in poi NESSUN reload/goto finche' non finisce.")

    # Attesa passiva pura: nessuna navigazione, nessun reload. Solo lettura del DOM
    # gia' presente in pagina, che Studio aggiorna da solo via JS interno.
    deadline = time.time() + 30 * 60
    poll = 0
    while time.time() < deadline:
        page.wait_for_timeout(15000)
        poll += 1
        try:
            body_txt = page.inner_text("body", timeout=8000)
        except Exception as e:
            print(f"[poll {poll}] pagina non leggibile ora (non navigo via comunque): {e}")
            continue
        pct_line = ""
        for line in body_txt.splitlines():
            low = line.lower()
            if "uploaded" in low and "%" in line:
                pct_line = line.strip()
        pending = "Pending" in body_txt
        print(f"[poll {poll}] pending={pending} {pct_line}")
        if pct_line == "" and not pending:
            print("UPLOAD COMPLETATO (nessun widget di progresso, non piu' Pending).")
            page.screenshot(path="../memory/_v4_final_ok.png")
            break
    else:
        print("[AVVISO] Tetto 30 minuti raggiunto.")
        page.screenshot(path="../memory/_v4_timeout.png")

    ctx.close()
