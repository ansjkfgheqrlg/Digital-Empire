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
import subprocess
import urllib.request
import urllib.error
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

# Chrome VERO come processo indipendente, non lanciato/posseduto da Playwright — richiesta
# esplicita di Max (2026-08-06): con Playwright che lancia E chiude Chrome, ogni crash o
# chiusura anticipata dello script si portava via anche la finestra (e la sessione di login
# appena fatta, mai salvata su disco per lo stesso motivo). Con un Chrome lanciato a parte e
# Playwright che si limita a COLLEGARSI (CDP), la finestra sopravvive allo script: si chiude
# solo se Max la chiude lui.
CHROME_EXE_CANDIDATI = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]
CDP_PORT = 9333

# --- motore di sessione CONDIVISO (TASK-ARENA-SESSION-W1) --------------------
# Il codice di sessione che stava qui (avvio Chrome reale via CDP, ricerca della
# scheda arena.ai, attesa del login, modali "Agree"/"Accept Cookies") e' stato
# promosso a `shared/arena_session.py` ed e' ora lo STESSO usato dal motore
# caroselli (`caroselli - agency/Core/browser_manager.py`), che quelle lezioni non
# le aveva: nessun controllo di login, modale Terms mai gestita, e un import
# obbligatorio di playwright_stealth che lo faceva morire prima di partire.
# Qui non cambia niente di comportamento: le funzioni sotto restano, ma delegano.
_REPO = os.path.abspath(os.path.join(FACTORY_DIR, ".."))
if _REPO not in sys.path:
    sys.path.insert(0, _REPO)
from shared.arena_session import ArenaSession  # noqa: E402

#: Sessione condivisa viva, creata da main(). Le funzioni sotto la usano se c'e'.
SESSIONE: "ArenaSession | None" = None


def _pagina_arena(context, timeout_s: float = 15):
    """Trova la scheda arena.ai fra quelle gia' aperte, invece di assumere che sia
    `context.pages[0]`. Chrome apre spesso PIU' schede al lancio (una vuota + quella passata
    da riga di comando): prendere sempre la prima significava a volte guardare la scheda
    sbagliata e poi rilanciare un goto() su una navigazione gia' in corso altrove — causa
    reale dei timeout ripetuti trovati fra il 2026-08-06 e il 2026-08-09, non un problema di
    login o di anti-bot. **Verificato con esecuzione reale**: con questo fix, login riuscito
    e prima copertina reale generata e scaricata (video CxdlEsEnZ9g, @Legamidiamore)."""
    scadenza = time.time() + timeout_s
    while time.time() < scadenza:
        for pg in context.pages:
            if "arena.ai" in pg.url:
                return pg
        time.sleep(0.5)
    # Nessuna scheda arena.ai trovata entro il timeout: se ne apre una esplicitamente.
    pg = context.new_page()
    pg.goto("https://arena.ai", wait_until="domcontentloaded", timeout=30000)
    return pg


def _sessione() -> ArenaSession:
    """La sessione condivisa, creandola se serve (stesso profilo di sempre)."""
    global SESSIONE
    if SESSIONE is None:
        SESSIONE = ArenaSession(profilo_dir=PROFILE_DIR, modo="cdp",
                                cdp_port=CDP_PORT, log=print)
    return SESSIONE


def _cdp_attivo() -> bool:
    """Delega al motore condiviso (era una copia identica di quella logica)."""
    return _sessione()._cdp_attivo()


def _avvia_chrome_reale():
    """Chrome VERO come processo indipendente: ora vive in shared/arena_session.py.

    Il motivo resta quello di Max (2026-08-06): con Playwright che lancia E chiude
    Chrome, ogni crash dello script si portava via la finestra e la sessione di
    login appena fatta. Con CDP la finestra sopravvive allo script.
    """
    try:
        _sessione()._avvia_chrome_reale()
    except RuntimeError as e:
        raise SystemExit("[!] %s" % e)


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


# Prompt di RIFINITURA (secondo giro) — dettato letteralmente da Max il 2026-08-10 dopo aver
# giudicato la prima copertina reale generata (video CxdlEsEnZ9g) non professionale. Max lo ha
# gia' incollato lui stesso a mano su LM Arena come test. Va applicato con un secondo giro
# "Modify this image" SULL'IMMAGINE GIA' GENERATA dal primo prompt (build_prompt), non al posto
# suo — non ancora agganciato automaticamente al flusso (richiesta esplicita: "guarda, non
# risolvilo" — solo salvare il prompt per ora, non lanciare altro).
#
# Requisiti tradotti dalla descrizione di Max, uno per uno:
# 1. L'evidenziatore nero dietro al testo va tolto: "orribile, non professionale, non si vede".
# 2. Testo MAI bianco: oro e rosso mescolati insieme nello stesso lettering.
# 3. Qualita' del testo ultra-alta, estremamente realistico e professionale — ma NON troppo
#    ornato/elegante: Max lo paragona esplicitamente a uno stile "medievale/storia di Roma" da
#    evitare, non da cercare.
# 4. Testo perfettamente leggibile sullo sfondo.
# 5. Soggetto (la persona) piu' nitido e piu' realistico/fotorealistico.
# 6. Soggetto con un contorno sottilissimo rosso+oro, leggermente luminoso — luminosita' MINIMA,
#    non un bagliore forte.
# 7. Il testo non deve MAI sovrapporsi al soggetto (nessuna scritta sopra la persona).
PROMPT_RIFINITURA = (
    "Refine this exact thumbnail image (do not redesign it from scratch, keep the same "
    "composition, subject pose and text content):\n\n"
    "1. Remove the solid dark/black highlight box behind the text completely — it looks "
    "unprofessional and hides the background.\n"
    "2. The text must NEVER be plain white. Recolor all text using a blended gold-and-red "
    "lettering (the two colors mixed together within the same letters), not two separate "
    "solid-color blocks.\n"
    "3. The text must look ultra high quality, extremely realistic and professional — but NOT "
    "overly ornate, decorative or medieval/Roman-looking. Clean, premium, modern — not "
    "old-fashioned engraved lettering.\n"
    "4. Text must stay perfectly readable against the background at every point.\n"
    "5. Make the subject (the person) sharper and more photorealistic.\n"
    "6. Add a very thin red-and-gold outline around the subject's silhouette, with only a "
    "minimal, subtle glow — the luminosity must be very low-key, not a strong bright glow.\n"
    "7. The text must never overlap or sit on top of the subject — keep all text fully "
    "outside the person's silhouette at all times."
)


def build_prompt(brief: dict, has_source_image: bool) -> str:
    lines = brief["text_overlay_lines"]
    highlight = brief.get("text_overlay_highlight_lines", [])
    text_block = " / ".join(lines)
    highlight_block = " and ".join(f'"{h}"' for h in highlight) if highlight else "none"

    if has_source_image:
        # Con l'immagine reale allegata, lo stile visivo lo detta l'immagine stessa — non una
        # descrizione testuale fissa. Fino al 2026-08-06 qui c'era una descrizione hardcoded
        # ("hand-drawn pencil-sketch illustration of a smiling elderly man..."): corretta per
        # Dose Mentale, sbagliata per qualunque altro canale (bug reale trovato producendo per
        # @Legamidiamore, il cui stile reale sono foto fotorealistiche, non disegni a matita).
        base = "Modify the attached YouTube thumbnail, keeping its exact visual style, layout, color palette and typography"
    else:
        # Senza immagine (download fallito): l'unica descrizione disponibile e' quella nel
        # brief stesso (source_style, gia' specifico per canale — vedi apex7_orchestrator.py
        # run_phase_5), non piu' una frase fissa su Dose Mentale.
        base = f"Recreate this YouTube thumbnail style: {brief['source_style']}"

    # "pose" e' opzionale: se il brief e' scritto a mano puo' indicare la posa esatta del
    # soggetto. F5 non puo' inventarla, quindi genera solo il contesto del tema (`concept`) e
    # qui si chiede di adattare l'illustrazione al nuovo argomento.
    cambio_soggetto = (f"Change 1 — the pose of the subject: {brief['pose']}" if brief.get("pose")
                       else f"Change 1 — adapt the subject/illustration to the new topic instead "
                            f"of the original one. New topic context: {brief['concept']}")
    return (
        f"{base}. 16:9.\n\n"
        f"{cambio_soggetto}\n"
        f"Change 2 — replace ALL text with exactly these lines, in this order: {text_block}\n"
        f"Lines that must sit inside a highlighted box: {highlight_block}\n\n"
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
        # domcontentloaded, non networkidle: arena.ai ha traffico di rete continuo che non si
        # ferma mai davvero — networkidle ha fatto scadere goto() stesso dopo 30s (bug reale
        # trovato il 2026-08-06, stesso identico problema gia' risolto la stessa mattina su
        # YouTube Studio in legamidiamore_session_check.py: crash non gestito qui, non un
        # errore di rete/API esterna).
        page.goto("https://arena.ai", wait_until="domcontentloaded", timeout=30000)
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

    # Terms of Use / cookie al primo utilizzo -> motore condiviso.
    # (Il motore caroselli questa modale non la gestiva affatto: e' una delle
    #  lezioni che la condivisione porta anche a lui.)
    sess = _sessione()
    sess.page = page
    sess.gestisci_modali()

    # Login richiesto? Ora la domanda si fa al motore condiviso, che risponde
    # anche 'captcha' — prima qui un captcha era indistinguibile da "loggato",
    # perche' si guardava solo il bottone Google.
    stato = sess.stato_login()
    if stato in ("login_richiesto", "captcha"):
        write_status("attesa_login", stato=stato,
                     messaggio="Login manuale richiesto nella finestra Chrome aperta - attendo fino a 15 minuti")
        if not sess.attendi_login(timeout_s=900):
            write_status("timeout_login")
            return []
        write_status("login_completato")
        # domcontentloaded, non networkidle: arena.ai ha traffico di rete continuo che non si
        # ferma mai davvero — networkidle ha fatto scadere goto() stesso dopo 30s (bug reale
        # trovato il 2026-08-06, stesso identico problema gia' risolto la stessa mattina su
        # YouTube Studio in legamidiamore_session_check.py: crash non gestito qui, non un
        # errore di rete/API esterna).
        page.goto("https://arena.ai", wait_until="domcontentloaded", timeout=30000)
        time.sleep(1.5)
        select_direct_mode(page)
        enter_image_mode_and_send(page, brief, image_path)

    ignore_srcs = current_img_srcs(page)  # allegato + avatar, gia' presenti prima della risposta
    write_status("generazione_in_corso")
    # Il placeholder "Generating image..." si e' rivelato INAFFIDABILE come segnale di fine
    # generazione: in piu' run reali fra il 2026-08-06 e il 2026-08-10 risultava scomparso
    # (0 secondi di attesa rilevati) prima che l'immagine finale fosse pronta, facendo
    # raccogliere solo anteprime 128x128 o niente. Fix: si interroga direttamente il DOM
    # aspettando che compaia una nuova immagine di dimensione REALE (>=300x150), fino a 90s,
    # invece di fidarsi di un testo che puo' sparire troppo presto.
    trovata = False
    scadenza = time.time() + 90
    while time.time() < scadenza:
        imgs = page.locator("img")
        for i in range(imgs.count()):
            img = imgs.nth(i)
            src = img.get_attribute("src") or ""
            if src in ignore_srcs:
                continue
            box = img.bounding_box()
            if box and box["width"] >= 300 and box["height"] >= 150:
                trovata = True
                break
        if trovata:
            break
        time.sleep(2)
    write_status("attesa_generazione_terminata", immagine_grande_trovata=trovata)
    time.sleep(2)  # margine breve per assestamento finale del rendering
    return harvest_images(page, ignore_srcs)


def main():
    ap = argparse.ArgumentParser(description="Genera la copertina su Arena adattando quella reale del video sorgente.")
    ap.add_argument("--visibile", action="store_true",
                    help="Ignorato (compatibilita'): Chrome e' sempre una finestra vera, "
                         "non piu' lanciata/posseduta da Playwright.")
    args = ap.parse_args()

    global HEADLESS
    HEADLESS = False

    brief = load_brief()
    image_path = source_thumbnail_path(brief)
    write_status("avviato", miniatura_sorgente=image_path, titolo=brief["title"])

    write_status("apertura_chrome_reale" if not _cdp_attivo() else "chrome_gia_aperto",
                 messaggio="Sessione Arena via motore condiviso shared/arena_session.py")

    # Tutto l'avvio (Chrome reale via CDP, attesa della porta di debug, ricerca
    # della scheda arena.ai, wait domcontentloaded, modali Agree/Accept Cookies)
    # e' ora una sola chiamata al motore condiviso: era il blocco duplicato che
    # nel motore caroselli non esisteva.
    sess = _sessione()
    try:
        page = sess.apri()
        try:
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
                    # Bug reale trovato il 2026-08-06: open_new_chat() non era protetta come
                    # run_attempt() sopra — un suo fallimento (es. goto in timeout) crashava
                    # l'intero script invece di passare semplicemente al tentativo successivo.
                    try:
                        open_new_chat(page)
                    except Exception as e:
                        write_status("nuova_chat_fallita", n=tentativo, errore=str(e)[:300])

            page.screenshot(path=os.path.join(OUT_DIR, "arena_debug_final.png"), full_page=True)

            # regolatore-copertina: fino ad ora nessun controllo verificava che la copertina
            # generata fosse davvero riadattata e non solo un ricalco della sorgente —
            # "originale" era affidato solo al testo del prompt (build_prompt), mai misurato
            # dopo il fatto.
            esito_copertina = None
            if saved:
                sys.path.insert(0, SCRIPT_DIR)
                import regolatori as _regolatori  # noqa: E402
                esito_copertina = _regolatori.verifica_copertina(image_path, saved[0])
                simbolo = "🟢" if esito_copertina["esito"] == "passa" else "🔴"
                print(f"[{simbolo} regolatore-copertina] {esito_copertina['esito']} — {esito_copertina['motivo']}")

            write_status("completato" if saved else "fallito", immagini_salvate=saved,
                         regolatore_copertina=esito_copertina)
        finally:
            pass
    finally:
        # `chiudi()` in modo CDP si limita a DISCONNETTERE Playwright: non chiude
        # il browser, perche' quella finestra e' di Max e non di questo script.
        # E' il comportamento che il passaggio a CDP del 2026-08-06 doveva
        # garantire — la finestra (e la sessione di login) sopravvive allo script.
        # Ora e' il motore condiviso a garantirlo, per tutti i consumatori.
        sess.chiudi()


if __name__ == "__main__":
    main()
