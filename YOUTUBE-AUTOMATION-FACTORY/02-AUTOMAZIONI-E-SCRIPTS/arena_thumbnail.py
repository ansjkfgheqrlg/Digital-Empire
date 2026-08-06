#!/usr/bin/env python3
"""
Automazione Playwright reale di arena.ai (ex LM Arena) per generare la copertina
del video corrente. Stesso pattern di youtube_uploader_playwright.py: profilo Chrome
persistente, login umano una tantum (Google o email), poi riuso automatico della sessione.

Modalita' "Direct" (1 modello, non Battle Mode a 2 modelli), modello "Max" (default
di Direct al momento della scrittura di questo script).
"""
import os
import sys
import time
import json
import argparse
from playwright.sync_api import sync_playwright

# Forza stdout/stderr in utf-8 su Windows, line_buffering=True obbligatorio: senza, quando
# l'output e' rediretto su file (non un terminale) resta invisibile per decine di minuti
# (bug reale trovato il 2026-07-30 su fliki_client.py, stesso rischio qui). reconfigure()
# (non un nuovo io.TextIOWrapper!): se in futuro questo script viene importato da un altro che
# fa lo stesso wrapping, un secondo TextIOWrapper chiuderebbe il buffer del primo al garbage
# collection ("I/O operation on closed file", bug reale trovato il 2026-07-30). reconfigure()
# modifica lo stream esistente, idempotente e sicuro anche chiamato piu' volte.
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PROFILE_DIR = os.path.join(FACTORY_DIR, "chrome-profile-arena")
OUT_DIR = os.path.join(FACTORY_DIR, "05-TEMPLATES-E-KIT")
STATUS_FILE = os.path.join(FACTORY_DIR, "memory", "arena_thumbnail_status.json")

#: Impostato da main(). Headless per default: una finestra che si apre da sola
#: interrompe il lavoro di chi sta usando il computer.
HEADLESS = True

os.makedirs(PROFILE_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)


def write_status(status: str, **extra):
    data = {"status": status, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"), **extra}
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[STATUS] {status} {extra}")


def load_brief() -> dict:
    with open(os.path.join(OUT_DIR, "brief-miniatura.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def source_thumbnail_path(brief: dict) -> str | None:
    """Miniatura REALE del video @dosementale che stiamo adattando: e' la base da modificare,
    non un riferimento vago. Se manca, il prompt testuale la descrive comunque."""
    rel = brief.get("source_thumbnail")
    if not rel:
        return None
    path = os.path.join(OUT_DIR, rel)
    return path if os.path.exists(path) else None


def build_prompt(brief: dict, has_source_image: bool) -> str:
    lines = brief["text_overlay_lines"]
    highlight = brief.get("text_overlay_highlight_lines", [])
    text_block = " / ".join(lines)
    highlight_block = " and ".join(f'"{h}"' for h in highlight) if highlight else "none"
    base = (
        "Modify the attached YouTube thumbnail" if has_source_image
        else f"Recreate this YouTube thumbnail style: {brief['source_style']}"
    )
    # "pose" e' opzionale: se il brief e' scritto a mano puo' indicare la posa esatta del
    # soggetto. F5 non puo' inventarla, quindi genera solo il contesto del tema (`concept`) e
    # qui si chiede di adattare l'illustrazione al nuovo argomento.
    cambio_soggetto = (f"Change 1 — the pose of the subject: {brief['pose']}" if brief.get("pose")
                       else f"Change 1 — adapt the illustration to the new topic instead of the "
                            f"original one. New topic context: {brief['concept']}")
    return (
        f"{base}, keeping its exact visual language: white background, warm yellow radial "
        "light rays behind the subject, hand-drawn pencil-sketch illustration of a smiling "
        "elderly man, very heavy bold black uppercase Italian text on the left half, key lines "
        "highlighted with a solid green box and white text. 16:9.\n\n"
        f"{cambio_soggetto}\n"
        f"Change 2 — replace ALL text with exactly these lines, in this order: {text_block}\n"
        f"Lines that must sit inside the solid green highlight box: {highlight_block}\n\n"
        "Keep the text perfectly readable, no spelling mistakes, no extra words, no watermark. "
        f"Video title for context: \"{brief['title']}\"."
    )


def click_first_visible(locator, timeout=5000):
    n = locator.count()
    for i in range(n):
        el = locator.nth(i)
        if el.is_visible():
            el.click(timeout=timeout)
            return True
    return False


def select_direct_mode(page):
    """Passa da Battle Mode (default) a Direct — 1 solo modello, non 2 in parallelo.
    Il modello resta quello di default di Direct (oggi 'Max')."""
    opened = click_first_visible(page.locator("button:has-text('Battle Mode')"))
    if not opened:
        write_status("avviso", messaggio="Bottone modalita' non trovato, provo a proseguire comunque")
        return
    time.sleep(0.5)
    page.get_by_role("option", name="Direct", exact=False).click(timeout=5000)
    time.sleep(0.5)


def attach_source_image(page, image_path) -> bool:
    """Carica la miniatura reale di @dosementale nella chat, cosi' il modello la MODIFICA
    invece di disegnarne una da zero (richiesta esplicita di Gael, 2026-07-31)."""
    if not image_path:
        return False
    try:
        page.locator("input[type='file']").first.set_input_files(image_path, timeout=8000)
    except Exception as e:
        write_status("avviso", messaggio=f"Upload miniatura sorgente non riuscito: {e}")
        return False
    # L'anteprima dell'allegato deve comparire prima dell'invio, altrimenti il messaggio
    # parte senza immagine e il modello disegna da zero.
    try:
        page.locator("form img, form [aria-label*='attach' i]").first.wait_for(
            state="visible", timeout=20000)
    except Exception:
        write_status("avviso", messaggio="Anteprima allegato non confermata, invio comunque")
    return True


def enter_image_mode_and_send(page, brief, image_path=None) -> str:
    try:
        page.locator("form button[aria-label='Image']").click(timeout=8000)
    except Exception:
        pass
    time.sleep(0.5)
    # Il prompt si costruisce DOPO l'upload: se l'allegato non passa, il testo deve descrivere
    # lo stile della sorgente invece di dire "modifica l'immagine allegata" (che non c'e').
    attached = attach_source_image(page, image_path)
    prompt = build_prompt(brief, attached)
    textbox = page.locator("textarea, [contenteditable='true']").first
    textbox.click()
    textbox.fill(prompt)
    time.sleep(0.3)
    page.locator("form button[aria-label='Send message']").click()
    write_status("prompt_inviato", con_immagine_sorgente=attached, prompt=prompt[:300])
    return prompt


def current_img_srcs(page) -> set:
    return set(page.locator("img").evaluate_all("els => els.map(e => e.src || '')"))


def open_new_chat(page):
    """Chat rotta/bloccata: si chiude e se ne apre una nuova invece di insistere (regola di
    Gael, 2026-07-31). Il bottone 'New chat' se c'e', altrimenti ricaricando arena.ai."""
    try:
        page.get_by_role("button", name="New chat").click(timeout=5000)
        time.sleep(2)
    except Exception:
        page.goto("https://arena.ai", wait_until="networkidle", timeout=30000)
        time.sleep(2)
    select_direct_mode(page)


def harvest_images(page, ignore_srcs: set) -> list:
    """Salva solo le immagini COMPARSE dopo l'invio: cosi' la miniatura sorgente caricata da noi
    e gli avatar non finiscono per errore tra i candidati."""
    saved = []
    imgs = page.locator("img")
    debug = []
    for i in range(imgs.count()):
        img = imgs.nth(i)
        src = img.get_attribute("src") or ""
        box = img.bounding_box()
        debug.append({"i": i, "src": src[:60], "box": box, "nuova": src not in ignore_srcs})
        if src in ignore_srcs or not box or box["width"] < 150 or box["height"] < 100:
            continue
        out_path = os.path.join(OUT_DIR, f"copertina-arena-candidata-{len(saved)+1}.png")
        try:
            if src.startswith("http"):
                resp = page.request.get(src)
                with open(out_path, "wb") as f:
                    f.write(resp.body())
            else:
                img.screenshot(path=out_path)
            saved.append(out_path)
        except Exception as e:
            print(f"[!] Impossibile salvare immagine {i}: {e}")
    write_status("debug_immagini", dettagli=debug, salvate=len(saved))
    return saved


def run_attempt(page, brief, image_path, tentativo: int) -> list:
    write_status("tentativo_avviato", n=tentativo)
    enter_image_mode_and_send(page, brief, image_path)
    time.sleep(2)

    # Terms of Use al primo utilizzo
    try:
        agree = page.get_by_role("button", name="Agree")
        agree.wait_for(state="visible", timeout=4000)
        agree.click()
        time.sleep(1)
    except Exception:
        pass

    # Login richiesto? Attesa nativa di Playwright (wait_for state=hidden).
    google_btn = page.get_by_role("button", name="Continue with Google")
    if google_btn.is_visible():
        if HEADLESS:
            # Senza finestra visibile nessuno puo' fare il login: aspettare 15 minuti sarebbe
            # solo tempo perso. Si fallisce subito dicendo cosa fare.
            write_status(
                "login_richiesto_ma_headless",
                messaggio="La sessione Arena e' scaduta. Rilancia UNA VOLTA con --visibile, "
                          "fai il login a mano, poi i run successivi tornano headless da soli "
                          "(il profilo e' persistente).",
            )
            return []
        write_status("attesa_login", messaggio="Login manuale richiesto nella finestra Chrome aperta — attendo fino a 15 minuti")
        try:
            google_btn.wait_for(state="hidden", timeout=900000)
        except Exception:
            write_status("timeout_login")
            return []
        write_status("login_completato")
        page.goto("https://arena.ai", wait_until="networkidle", timeout=30000)
        time.sleep(1.5)
        select_direct_mode(page)
        enter_image_mode_and_send(page, brief, image_path)

    ignore_srcs = current_img_srcs(page)  # allegato + avatar, gia' presenti prima della risposta
    write_status("generazione_in_corso")
    # Direct = 1 solo modello: un solo placeholder "Generating image..." da attendere.
    waited, max_wait, pending = 0, 240, 1
    while waited < max_wait:
        pending = page.get_by_text("Generating image...").count()
        if pending == 0:
            break
        time.sleep(3)
        waited += 3
    write_status("attesa_generazione_terminata", secondi_attesi=waited, pending_residui=pending)
    time.sleep(3)  # margine per il rendering completo dopo la sparizione del placeholder
    return harvest_images(page, ignore_srcs)


def main():
    ap = argparse.ArgumentParser(description="Genera la copertina su Arena adattando quella reale del video sorgente.")
    # Headless per DEFAULT (richiesta di Gael, 2026-08-04): una finestra del browser che si apre
    # da sola ruba il focus e interrompe il lavoro. La sessione Google resta valida perche' il
    # profilo persistente e' lo stesso: headless non significa "senza login".
    ap.add_argument("--visibile", action="store_true",
                    help="Apre una finestra vera. Serve SOLO per il primo login manuale su Arena.")
    args = ap.parse_args()

    global HEADLESS
    HEADLESS = not args.visibile

    brief = load_brief()
    image_path = source_thumbnail_path(brief)
    write_status("avviato", miniatura_sorgente=image_path, titolo=brief["title"],
                 headless=not args.visibile)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            headless=not args.visibile,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://arena.ai", wait_until="networkidle", timeout=30000)
        time.sleep(1.5)

        try:
            page.get_by_text("Accept Cookies", exact=True).click(timeout=4000)
        except Exception:
            pass

        select_direct_mode(page)

        saved = []
        for tentativo in range(1, 4):
            try:
                saved = run_attempt(page, brief, image_path, tentativo)
            except Exception as e:
                write_status("tentativo_fallito", n=tentativo, errore=str(e)[:300])
                saved = []
            if saved:
                break
            if tentativo < 3:
                write_status("nuova_chat", motivo="nessuna immagine prodotta in questa chat")
                open_new_chat(page)

        page.screenshot(path=os.path.join(OUT_DIR, "arena_debug_final.png"), full_page=True)

        # regolatore-copertina: fino ad ora nessun controllo verificava che la copertina
        # generata fosse davvero riadattata e non solo un ricalco della sorgente — "originale"
        # era affidato solo al testo del prompt (build_prompt), mai misurato dopo il fatto.
        esito_copertina = None
        if saved:
            sys.path.insert(0, SCRIPT_DIR)
            import regolatori as _regolatori  # noqa: E402
            esito_copertina = _regolatori.verifica_copertina(image_path, saved[0])
            simbolo = "🟢" if esito_copertina["esito"] == "passa" else "🔴"
            print(f"[{simbolo} regolatore-copertina] {esito_copertina['esito']} — {esito_copertina['motivo']}")

        write_status("completato" if saved else "fallito", immagini_salvate=saved,
                     regolatore_copertina=esito_copertina)
        context.close()


if __name__ == "__main__":
    main()
