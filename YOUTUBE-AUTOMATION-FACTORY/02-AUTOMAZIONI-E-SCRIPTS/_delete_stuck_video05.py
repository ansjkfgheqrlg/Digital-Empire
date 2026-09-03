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
    page.goto("https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
    row.scroll_into_view_if_needed(timeout=10000)
    page.wait_for_timeout(500)
    row.hover(timeout=5000)
    page.wait_for_timeout(500)
    page.screenshot(path="../memory/_delete_row_hover.png")

    # Stato reale trovato dal vivo: "Upload interrupted" con bottoni nativi
    # "Resume upload" (click + riseleziona video.mp4 per riprendere da dove si e' fermato,
    # via protocollo resumable upload di YouTube) e "Delete video". Resume e' molto meglio
    # di cancellare e ricaricare da zero: non rifa' i minuti gia' trasferiti.
    resume_btn = row.get_by_text("Resume upload", exact=False).first
    resume_btn.click(timeout=10000)
    page.wait_for_timeout(2000)
    page.screenshot(path="../memory/_resume_native_after_click.png")

    file_input = page.locator("input[type='file']")
    file_input.set_input_files(VIDEO_PATH, timeout=15000)
    page.wait_for_timeout(3000)
    page.screenshot(path="../memory/_resume_native_file_selected.png")
    print("Resume upload avviato con video.mp4 riselezionato.")

    # REGOLA di Max (2026-09-03): l'upload va SEMPRE finito, mai chiuso il browser a meta'.
    # Restiamo sulla pagina finche' la riga non mostra piu' "Uploading"/"Pending"/"interrupted",
    # fino a un tetto di 30 minuti (file da 272MB, gia' bloccato una volta).
    deadline = time.time() + 30 * 60
    last_txt = ""
    while time.time() < deadline:
        page.wait_for_timeout(15000)
        try:
            page.reload(wait_until="domcontentloaded")
            page.wait_for_timeout(3000)
            row = page.locator("ytcp-video-row").filter(has_text="7 SEGNALI che una DONNA si sta inn").first
            txt = row.inner_text(timeout=8000)
        except Exception as e:
            print(f"[stato] errore lettura riga: {e}")
            continue
        first_line = txt.splitlines()[0] if txt else txt
        stuck = ("interrupted" in txt) or ("Uploading" in txt)
        pending = "Pending" in txt
        print(f"[stato] {first_line} | interrotto/uploading={stuck} pending={pending}")
        if not stuck and not pending:
            print("UPLOAD COMPLETATO — non e' piu' in caricamento/pending.")
            page.screenshot(path="../memory/_resume_native_final_ok.png")
            break
        last_txt = txt
    else:
        print(f"[AVVISO] Tetto di 30 minuti raggiunto. Ultimo stato: {last_txt.splitlines()[0] if last_txt else last_txt}")
        page.screenshot(path="../memory/_resume_native_timeout.png")

    ctx.close()
