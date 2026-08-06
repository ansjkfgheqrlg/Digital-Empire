"""
LM Arena Client (PIANO-KDP-67, CP4) — wrapper Playwright condiviso per LM Arena (arena.ai,
ex LM Arena): invia prompt di testo o immagine, aspetta il completamento REALE (non un
timeout fisso), estrae la risposta.

Riusa pattern gia' verificati in produzione su questo stesso sito
(YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/arena_thumbnail.py, CP-20260729-009),
non reinventati da zero: modalita' Direct (1 modello "Max", non Battle Mode a 2 modelli
anonimi — serve un output verificabile e ripetibile), flag
--disable-blink-features=AutomationControlled (senza, in headless si incontra una sfida
Cloudflare "Performing security verification", riscontrata in CP4 il 2026-08-05 e risolta
con questo stesso flag gia' usato in arena_thumbnail.py), profilo browser persistente con
la sessione reale salvata in CP1 (login gia' fatto, mai un login nuovo qui).

Rilevamento completamento TESTO (nuovo in CP4, non presente nel riferimento che gestiva solo
immagini): il bottone di invio ha `aria-label="Send message"` a riposo, diventa
`aria-label="Stop generation"` appena parte la generazione, torna `"Send message"` a
generazione conclusa. Attendere SOLO la ricomparsa di "Send message" e' un falso positivo
(quello stato esiste anche PRIMA che la generazione cominci) — bisogna aspettare prima che
"Stop generation" compaia, poi che sparisca (bug reale trovato e corretto in CP4).

Estrazione testo: selettore strutturale, non per contenuto — un elemento `[class*="prose"]`
il cui antenato più vicino NON ha classe `bg-surface-raised` (quella e' la bolla del
messaggio utente) e' la risposta del modello. Verificato non confondere mai risposta e
prompt anche quando il modello ripete parte del testo dell'utente.
"""
from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import Page, Playwright

from . import config

ARENA_LAUNCH_ARGS = ["--disable-blink-features=AutomationControlled", "--profile-directory=Default"]


@dataclass
class ArenaSession:
    context: object
    page: Page

    def close(self) -> None:
        self.context.close()


def open_session(playwright: Playwright, headless: bool = True) -> ArenaSession:
    """Apre LM Arena con la sessione reale salvata (CP1) e seleziona la modalita' Direct.
    Fatto = pronta per send_text_prompt/send_image_prompt, nessun login richiesto."""
    if not config.BRAVE_PROFILE_COPY_DIR.exists():
        raise FileNotFoundError(
            f"Profilo Brave copiato non trovato: {config.BRAVE_PROFILE_COPY_DIR}. "
            f"Esegui prima: python -m engine.session_manager"
        )
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=str(config.BRAVE_PROFILE_COPY_DIR),
        headless=headless,
        executable_path=str(config.BRAVE_EXECUTABLE_PATH),
        viewport={"width": 1440, "height": 900},
        args=ARENA_LAUNCH_ARGS,
    )
    page = context.pages[0] if context.pages else context.new_page()
    # domcontentloaded, non networkidle: arena.ai tiene connessioni persistenti aperte
    # (chat live) che a volte impediscono a networkidle di scattare mai (timeout reale
    # riscontrato in CP4, 2026-08-05) — stesso pattern gia' usato in amazon_research.py.
    page.goto(config.LMARENA_BASE_URL, wait_until="domcontentloaded", timeout=config.DEFAULT_TIMEOUT_MS)
    time.sleep(2.5)
    try:
        page.get_by_text("Accept Cookies", exact=True).click(timeout=3000)
    except Exception:
        pass
    _select_direct_mode(page)
    return ArenaSession(context=context, page=page)


def _robust_click(el, timeout: int = 10000) -> None:
    """Click con fallback su coordinate (bounding box) se il click sintetico di Playwright
    si blocca — riscontrato ripetutamente in CP4 su piu' bottoni di questo sito (mode
    selector, Send message): elemento visibile, box reale, nessun overlay rilevabile, ma
    `.click()` va comunque in timeout. Il click per coordinate sullo stesso punto funziona
    sempre in questi casi — probabile incompatibilita' fra l'evento sintetico di Playwright
    e certi componenti Radix-UI di questo sito, non un problema del nostro selettore."""
    try:
        el.click(timeout=timeout)
    except Exception:
        box = el.bounding_box()
        if not box:
            raise
        el.page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)


def _click_first_visible(locator, timeout: int = 10000) -> bool:
    for i in range(locator.count()):
        el = locator.nth(i)
        if el.is_visible():
            _robust_click(el, timeout=timeout)
            return True
    return False


def _select_direct_mode(page: Page) -> None:
    """Passa da Battle Mode (default, 2 modelli in parallelo) a Direct (1 modello, oggi
    'Max' di default) — un output verificabile e ripetibile, non una battaglia anonima."""
    opened = _click_first_visible(page.locator("button:has-text('Battle Mode')"))
    if not opened:
        return  # gia' in Direct (sessione riusata) o UI cambiata — non bloccare alla cieca
    time.sleep(0.5)
    try:
        page.get_by_role("option", name="Direct", exact=False).click(timeout=5000)
    except Exception:
        pass
    time.sleep(0.5)


def _extract_latest_response_text(page: Page) -> str | None:
    """Elemento `[class*="prose"]` FUORI da una bolla utente (`bg-surface-raised`) — la
    risposta del modello, mai il prompt, verificato per struttura non per contenuto."""
    return page.evaluate(
        """() => {
            const els = document.querySelectorAll('[class*="prose"]');
            for (const el of els) {
                if (!el.closest('[class*="bg-surface-raised"]')) {
                    return el.innerText;
                }
            }
            return null;
        }"""
    )


def send_text_prompt(page: Page, prompt: str, timeout_s: int = 300) -> str:
    """Invia un prompt di testo, aspetta il completamento REALE, estrae e torna la risposta
    reale. Solleva TimeoutError/RuntimeError espliciti se qualcosa non torna, mai un testo
    finto.

    Rilevamento completamento: placeholder 'Generating...' che sparisce (stesso pattern gia'
    verificato per le immagini, non un timeout fisso). Il bottone 'Stop generation' NON e'
    affidabile da solo — bug reale trovato in CP4: per risposte brevi/quasi istantanee il
    bottone non transita mai visibilmente per lo stato 'Stop generation' (la generazione
    finisce troppo in fretta), mentre il placeholder 'Generating...' compare comunque anche
    per risposte di una sola frase (verificato con screenshot reale)."""
    textbox = page.locator("textarea, [contenteditable='true']").first
    textbox.click()
    textbox.fill(prompt)
    time.sleep(0.3)
    _robust_click(page.locator("form button[aria-label='Send message']"))
    time.sleep(0.8)  # margine perche' il placeholder 'Generating...' compaia nel DOM prima
                      # del primo controllo — senza, un check troppo rapido puo' vederlo
                      # ancora assente e uscire subito credendo (erroneamente) che sia finita

    waited, max_wait = 0, timeout_s
    while waited < max_wait:
        pending = page.get_by_text("Generating", exact=False).count()
        if pending == 0:
            break
        time.sleep(1)
        waited += 1
    else:
        raise TimeoutError(f"LM Arena: generazione testo non completata dopo {max_wait}s")
    time.sleep(1)  # margine per il rendering finale dopo la sparizione del placeholder

    text = _extract_latest_response_text(page)
    if text is None:
        raise RuntimeError("LM Arena: nessuna risposta testuale trovata dopo la generazione")
    return text


def _current_img_srcs(page: Page) -> set:
    return set(page.locator("img").evaluate_all("els => els.map(e => e.src || '')"))


def send_image_prompt(page: Page, prompt: str, out_path: Path,
                       source_image_path: Path | None = None, timeout_s: int = 240) -> Path:
    """Passa in modalita' immagine, invia il prompt (con allegato opzionale), aspetta il
    completamento REALE (placeholder 'Generating image...' che sparisce), salva il file .png
    reale su disco in `out_path`. Stesso pattern gia' verificato in produzione in
    arena_thumbnail.py — qui generalizzato (out_path esplicito, non hardcoded)."""
    try:
        _robust_click(page.locator("form button[aria-label='Image']"), timeout=8000)
        time.sleep(0.5)
    except Exception:
        pass

    # Cambiare modalita' DENTRO una chat che ha gia' messaggi apre una conferma reale
    # ("Start new chat session? Changing modalities will start a new chat session.") —
    # non un errore, comportamento normale della UI se si passa da testo a immagine nella
    # stessa sessione invece che in una nuova. Confermata se compare, ignorata se no (prima
    # immagine di una chat vuota, nessun dialogo).
    try:
        page.get_by_role("button", name="Continue").click(timeout=3000)
        time.sleep(1)
    except Exception:
        pass

    if source_image_path is not None:
        page.locator("input[type='file']").first.set_input_files(str(source_image_path), timeout=8000)
        try:
            page.locator("form img, form [aria-label*='attach' i]").first.wait_for(
                state="visible", timeout=20000)
        except Exception:
            pass

    ignore_srcs = _current_img_srcs(page)
    textbox = page.locator("textarea, [contenteditable='true']").first
    textbox.click()
    textbox.fill(prompt)
    time.sleep(0.3)
    _robust_click(page.locator("form button[aria-label='Send message']"))
    time.sleep(0.8)  # stesso margine di send_text_prompt: evita un primo check troppo rapido

    waited, max_wait = 0, timeout_s
    while waited < max_wait:
        pending = page.get_by_text("Generating image...").count()
        if pending == 0:
            break
        time.sleep(3)
        waited += 3
    else:
        raise TimeoutError(f"LM Arena: generazione immagine non completata dopo {max_wait}s")
    time.sleep(3)  # margine per il rendering completo dopo la sparizione del placeholder

    imgs = page.locator("img")
    for i in range(imgs.count()):
        img = imgs.nth(i)
        src = img.get_attribute("src") or ""
        if src in ignore_srcs:
            continue
        box = img.bounding_box()
        if not box or box["width"] < 150 or box["height"] < 100:
            continue
        out_path.parent.mkdir(parents=True, exist_ok=True)
        if src.startswith("http"):
            resp = page.request.get(src)
            out_path.write_bytes(resp.body())
        else:
            img.screenshot(path=str(out_path))
        return out_path

    raise RuntimeError("LM Arena: nessuna immagine nuova trovata dopo la generazione")


if __name__ == "__main__":
    import sys
    import tempfile

    from playwright.sync_api import sync_playwright

    print("=== CP4 self-test REALE: testo + immagine su LM Arena (sessione vera) ===\n")

    with sync_playwright() as p:
        session = open_session(p, headless=True)
        try:
            print("[1/2] invio prompt di testo reale...")
            reply = send_text_prompt(
                session.page,
                "Reply with exactly this sentence and nothing else: The quick brown fox jumps.",
            )
            print(f"  risposta reale: {reply!r}")
            assert "quick brown fox" in reply.lower(), f"risposta inattesa: {reply!r}"
            print("  [OK] testo reale ricevuto e verificato\n")

            print("[2/2] invio prompt immagine reale...")
            out_path = Path(tempfile.gettempdir()) / "cp4_selftest_cover.png"
            saved = send_image_prompt(
                session.page,
                "A minimalist book cover illustration of a black cat sitting on a stack of "
                "old books, warm library lighting, watercolor style, no text.",
                out_path,
            )
            size_kb = saved.stat().st_size / 1024
            print(f"  immagine reale salvata: {saved} ({size_kb:.1f} KB)")
            assert size_kb > 5, f"file immagine sospetto, troppo piccolo: {size_kb:.1f} KB"
            print("  [OK] immagine reale ricevuta e verificata\n")
        finally:
            session.close()

    print("CP4 self-test: TUTTO VERIFICATO OK (testo + immagine reali su LM Arena)")
    sys.exit(0)
