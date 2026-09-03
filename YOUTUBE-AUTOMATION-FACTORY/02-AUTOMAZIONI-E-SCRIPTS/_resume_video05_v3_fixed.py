import sys, time
from playwright.sync_api import sync_playwright

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
VIDEO_PATH = r"C:\Users\Utente\Desktop\qui tutto\Digital Empire\YOUTUBE-AUTOMATION-FACTORY\VIDEO-PRONTI\video-05\video.mp4"
VIDEO_ID = "6hrhlS9jC4g"

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

    # UNA sola navigazione, poi MAI PIU' reload/goto finche' l'upload non e' finito.
    # Bug reale trovato in questa stessa sessione (2026-09-03): un loop precedente
    # chiamava page.reload() ogni 15s "solo per controllare lo stato" e questo ha
    # abortito l'upload appena ripartito (era arrivato al 24%, azzerato di nuovo).
    # Lo stato dell'upload nella pagina Studio si aggiorna DA SOLO via JS/websocket
    # interno, senza bisogno di reload: basta leggere il DOM in place.
    page.goto(f"https://studio.youtube.com/video/{VIDEO_ID}/edit", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    page.screenshot(path="../memory/_v3_start_state.png")

    warning_icon = page.locator("[class*='error'], ytcp-thumbnail-error, .thumbnail-container ytcp-icon-button").first
    resume_visible = page.get_by_text("Resume upload", exact=False).count() > 0
    print(f"Resume upload visibile su questa pagina: {resume_visible}")

    if resume_visible:
        page.get_by_text("Resume upload", exact=False).first.click(timeout=10000)
        page.wait_for_timeout(1500)
        file_input = page.locator("input[type='file']")
        file_input.set_input_files(VIDEO_PATH, timeout=15000)
        page.wait_for_timeout(3000)
        page.screenshot(path="../memory/_v3_after_resume_click.png")
        print("Resume upload avviato con video.mp4.")
    else:
        print("Nessun bottone 'Resume upload' su questa pagina — controllo se sta gia' caricando.")

    # Attesa PASSIVA senza reload: legge solo il widget di progresso e lo stato Pending/Public.
    deadline = time.time() + 30 * 60
    poll = 0
    while time.time() < deadline:
        page.wait_for_timeout(15000)
        poll += 1
        try:
            body_txt = page.inner_text("body", timeout=8000)
        except Exception as e:
            print(f"[poll {poll}] errore lettura pagina (pagina viva, non navigo via): {e}")
            continue
        uploading_widget = "uploaded" in body_txt.lower() and "%" in body_txt
        interrupted = "interrupted" in body_txt.lower()
        pending = "Pending" in body_txt
        pct_line = ""
        for line in body_txt.splitlines():
            if "% uploaded" in line.lower() or "%uploaded" in line.lower():
                pct_line = line.strip()
        print(f"[poll {poll}] widget_upload={uploading_widget} interrotto={interrupted} pending={pending} {pct_line}")
        if interrupted:
            print("[ERRORE] Upload interrotto di nuovo senza che io abbia navigato via — problema di rete/sessione, non di reload.")
            page.screenshot(path="../memory/_v3_interrupted_again.png")
            break
        if not uploading_widget and not pending:
            print("UPLOAD COMPLETATO.")
            page.screenshot(path="../memory/_v3_final_ok.png")
            break
    else:
        print("[AVVISO] Tetto 30 minuti raggiunto ancora in attesa.")
        page.screenshot(path="../memory/_v3_timeout.png")

    ctx.close()
