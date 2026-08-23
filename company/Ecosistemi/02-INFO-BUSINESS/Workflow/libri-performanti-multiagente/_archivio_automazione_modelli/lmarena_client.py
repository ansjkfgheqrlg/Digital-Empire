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

import hashlib
import json
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from playwright.sync_api import Page, Playwright

from . import config

ARENA_LAUNCH_ARGS = ["--disable-blink-features=AutomationControlled"]

DEBUG_LOG_DIR = config.SESSIONS_DIR / "debug_logs"


class CaptchaRequired(RuntimeError):
    """LM Arena mostra una sfida "Security Verification" (reCAPTCHA "I'm not a robot").

    NON e' aggirabile da codice, e non va aggirata: e' un controllo di sicurezza pensato
    apposta per distinguere una persona da un programma — superarlo automaticamente
    significherebbe ingannarlo. L'unica gestione corretta e' fermarsi e chiedere a un umano
    di risolverlo nella finestra del browser (che per questo motivo gira in modalita'
    visibile, non headless).

    Esiste come eccezione DEDICATA (non un TimeoutError generico) perche' in CP5 il captcha
    e' stato ripetutamente scambiato per lentezza/blocco del servizio, facendo perdere ore
    di diagnosi su una causa sbagliata: un errore esplicito rende la causa ovvia al primo
    colpo. Per lo stesso motivo NON viene ritentata automaticamente dal loop di retry:
    ritentare senza intervento umano non puo' funzionare, allunga solo l'attesa."""


CAPTCHA_MARKERS = ["Security Verification", "I'm not a robot", "Non sono un robot"]

# Errore lato server di arena.ai: compare un banner rosso con un bottone "Retry" nella UI
# stessa. Segnalato da Gael con screenshot il 2026-08-07 ("non ti accorgi che da errori?"):
# il codice non lo rilevava e restava ad aspettare una generazione che non sarebbe mai
# arrivata, fino al timeout — causa di parte dei blocchi attribuiti erroneamente ad altro.
GENERATION_ERROR_MARKERS = [
    "Something went wrong while generating the response",
    "Something went wrong",
]

# Quante volte cliccare il "Retry" della UI prima di arrendersi su una singola richiesta.
MAX_UI_RETRY_CLICKS = 3

# Pausa minima fra due invii consecutivi nella stessa sessione (2026-08-07). Osservazione
# reale: il self-test CP4 (1 sola richiesta per tipo) non ha mai incontrato il captcha,
# mentre CP5 (outline + 3 capitoli in rapida successione) lo incontra quasi sempre — il
# fattore scatenante sembra il RITMO delle richieste, non il browser. Non e' un tentativo
# di aggirare la verifica: e' semplicemente non martellare un servizio esterno, che e' il
# comportamento corretto a prescindere (stessa lezione gia' annotata in CP-20260805-011:
# "spaziare i test, non lanciare raffiche").
MIN_SECONDS_BETWEEN_SENDS = 20
_last_send_at: float = 0.0


def _throttle_before_send() -> None:
    """Attende, se necessario, per rispettare `MIN_SECONDS_BETWEEN_SENDS`."""
    global _last_send_at
    if _last_send_at:
        elapsed = time.time() - _last_send_at
        if elapsed < MIN_SECONDS_BETWEEN_SENDS:
            pause = MIN_SECONDS_BETWEEN_SENDS - elapsed
            print(f"[lmarena] pausa {pause:.0f}s prima del prossimo invio "
                  f"(ritmo sostenibile, non raffiche)", flush=True)
            time.sleep(pause)
    _last_send_at = time.time()


def _generation_error_present(page: Page) -> bool:
    """True se la UI mostra il banner d'errore di generazione (con bottone Retry)."""
    for marker in GENERATION_ERROR_MARKERS:
        try:
            if page.get_by_text(marker, exact=False).count() > 0:
                return True
        except Exception:
            continue
    return False


def _click_retry_button(page: Page) -> bool:
    """Clicca il bottone "Retry" del banner d'errore — e' la UI stessa a offrirlo per
    questo scopo, quindi usarlo e' l'uso previsto, non un aggiramento di nulla.

    Piu' strategie di selezione (2026-08-07): la prima versione usava solo
    `get_by_role("button", name="Retry", exact=True)` e falliva silenziosamente — il log
    lo ha mostrato (`generation_error_fatal` con `retries_used: 0`, cioe' errore rilevato
    ma click mai riuscito). Il bottone ha un'icona accanto al testo, quindi il nome
    accessibile puo' non essere esattamente "Retry". Si prova per ruolo (non esatto), poi
    per testo, poi per CSS.

    Ritorna True se il click e' riuscito."""
    for name in ("Retry", "Riprova"):
        # 1) per ruolo, match non esatto (tollera icona/spazi nel nome accessibile)
        try:
            btn = page.get_by_role("button", name=name, exact=False)
            if btn.count() > 0:
                _robust_click(btn.first, timeout=5000)
                return True
        except Exception:
            pass
        # 2) per testo visibile
        try:
            btn = page.get_by_text(name, exact=False)
            for i in range(btn.count()):
                el = btn.nth(i)
                if el.is_visible():
                    _robust_click(el, timeout=5000)
                    return True
        except Exception:
            pass
        # 3) selettore CSS diretto su un button che contiene quel testo
        try:
            btn = page.locator(f"button:has-text('{name}')")
            if btn.count() > 0:
                _robust_click(btn.first, timeout=5000)
                return True
        except Exception:
            pass
    return False

# Quanto attendere che un umano risolva il captcha prima di arrendersi (0 = non attendere).
CAPTCHA_WAIT_SECONDS = 300


def _captcha_present(page: Page) -> bool:
    """True se la sfida captcha e' visibile ORA. Cerca per testo (marcatori verificati dal
    vivo con screenshot reale il 2026-08-07, sia in inglese sia in italiano — la UI segue
    la lingua del browser)."""
    for marker in CAPTCHA_MARKERS:
        try:
            if page.get_by_text(marker, exact=False).count() > 0:
                return True
        except Exception:
            continue
    return False


def _wait_for_human_to_solve_captcha(page: Page, where: str) -> bool:
    """Mette in PAUSA e aspetta che una persona risolva il captcha nella finestra aperta,
    invece di far morire l'intero run (2026-08-07).

    Perche' cosi': il captcha e' progettato apposta perche' lo risolva un umano — non lo
    aggiro e non ci provo. Ma far fallire tutto il run costringeva a rilanciare da zero
    ogni volta (rigenerando outline e capitoli gia' fatti). Aspettando, l'intervento umano
    serve UNA volta e il lavoro gia' fatto non si perde.

    Ritorna True se il captcha e' stato risolto entro il tempo, False altrimenti."""
    if CAPTCHA_WAIT_SECONDS <= 0:
        return False
    print("\n" + "=" * 70, flush=True)
    print(">>> CAPTCHA da risolvere nella finestra del browser aperta.", flush=True)
    print(f">>> Clicca 'Non sono un robot', poi il lavoro riprende da solo.", flush=True)
    print(f">>> (attendo fino a {CAPTCHA_WAIT_SECONDS // 60} minuti, controllo ogni 3s)", flush=True)
    print("=" * 70 + "\n", flush=True)
    _debug_log("captcha_waiting_for_human", where=where, max_wait=CAPTCHA_WAIT_SECONDS)

    try:
        page.bring_to_front()
    except Exception:
        pass

    waited = 0
    while waited < CAPTCHA_WAIT_SECONDS:
        time.sleep(3)
        waited += 3
        if not _captcha_present(page):
            print(f">>> Captcha risolto dopo {waited}s — riprendo.\n", flush=True)
            _debug_log("captcha_solved_by_human", where=where, waited=waited)
            time.sleep(2)  # margine perche' la UI torni operativa dopo la sparizione
            return True
    _debug_log("captcha_wait_timeout", where=where, waited=waited)
    return False


def _debug_log(event: str, **fields) -> None:
    """Log di debug per ogni scambio prompt/risposta reale con LM Arena — un file .jsonl
    per giorno, mai silenzioso. Nato dal bug reale di CP5 (2026-08-06, capitoli duplicati
    passati inosservati perche' nessun log registrava prompt/risposta effettivi): senza
    questo, diagnosticare un problema richiede rilanciare tutto da capo con script ad-hoc.
    Con questo, il log stesso mostra cosa e' successo davvero, riga per riga, in ordine."""
    DEBUG_LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = DEBUG_LOG_DIR / f"lmarena_{datetime.now().strftime('%Y%m%d')}.jsonl"
    entry = {"ts": datetime.now().isoformat(), "event": event, **fields}
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _text_fingerprint(text: str | None) -> dict:
    if text is None:
        return {"len": 0, "hash": None, "preview": None}
    return {
        "len": len(text),
        "hash": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16],
        "preview": text[:120],
    }


@dataclass
class ArenaSession:
    browser: object
    context: object
    page: Page

    def close(self) -> None:
        # Con launch_persistent_context il browser e' di proprieta' del context: chiuderlo
        # a parte solleva errori. Si chiude il context e basta (best-effort sul browser,
        # che con un persistent context risulta gia' chiuso).
        self.context.close()
        try:
            if self.browser is not None and self.browser.is_connected():
                self.browser.close()
        except Exception:
            pass


def _seed_profile_from_saved_session(context) -> None:
    """Inietta UNA VOLTA i cookie della sessione salvata (CP1) nel profilo persistente
    appena creato, cosi' non serve rifare il login a mano. Da li' in poi il profilo
    mantiene tutto da solo e questa funzione non viene piu' chiamata."""
    import json
    data = json.loads(config.LMARENA_SESSION_PATH.read_text(encoding="utf-8"))
    cookies = data.get("cookies", [])
    if cookies:
        context.add_cookies(cookies)
    print(f"[lmarena] profilo persistente inizializzato con {len(cookies)} cookie "
          f"dalla sessione salvata (login non richiesto)")


def open_session(playwright: Playwright, headless: bool = True, *,
                  profilo_reale: bool = False, browser_reale: str = "brave") -> ArenaSession:
    """Apre LM Arena su un PROFILO PERSISTENTE dedicato e seleziona la modalita' Direct.
    Fatto = pronta per send_text_prompt/send_image_prompt, nessun login richiesto.

    `profilo_reale=True` usa invece il profilo browser REALE della persona (Brave Profile 9
    di default) — la configurazione che la Fase 0 valida. Default `False`: il comportamento
    di tutti i chiamanti esistenti (copertine, orchestrator) resta identico finche' la
    Fase 0 non dice che il profilo reale e' meglio. Con `profilo_reale=True` il browser
    NON deve essere aperto altrove: il lock Chromium e' condiviso su tutta la cartella
    `User Data` (il lancio si ferma con un messaggio chiaro se lo e').

    PROFILO PERSISTENTE, non contesto effimero (2026-08-07 — causa reale del captcha,
    trovata dopo che Gael ha fatto notare che "in molti altri workflow questo problema del
    captcha non c'era"): il workflow gia' in produzione sullo STESSO sito
    (YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/arena_thumbnail.py, profilo
    `chrome-profile-arena`) gira headless senza mai incontrare la sfida "Security
    Verification". La differenza non era headless si'/no: era che quel workflow usa
    `launch_persistent_context` su un profilo che PERSISTE fra i run, mentre qui si creava
    un contesto nuovo ad ogni avvio (`browser.new_context(storage_state=...)`) — arena.ai
    vedeva ogni volta un browser mai visto prima, senza storia, e chiedeva la verifica.
    Con un profilo persistente il sito riconosce lo stesso browser che torna: nessuna
    sfida da innescare, quindi nessuna da aggirare (che non si farebbe comunque).

    Il profilo e' VUOTO e dedicato, creato da Playwright — NON la copia da 381MB del
    profilo Brave reale, che causava timeout al lancio (CP4 2026-08-06) e che resta
    archiviata ma non piu' usata. Al primo avvio i cookie della sessione salvata in CP1
    vengono iniettati una volta sola, cosi' il login manuale non va rifatto."""
    if profilo_reale:
        # Profilo REALE della persona (quello che usa ogni giorno), non quello dedicato e
        # vuoto. Aggiunto il 2026-08-15 perche' la Fase 0 (`lmarena_captcha_probe`) misura
        # proprio questa configurazione: senza questo ramo, un esito positivo del probe non
        # sarebbe utilizzabile in produzione e la validazione non servirebbe a niente.
        # NB: qui NON si semina la sessione salvata e NON si crea niente — il profilo e'
        # gia' autenticato per conto suo, e non va mai alterato.
        from .lmarena_captcha_probe import _launch_real_profile

        context, page = _launch_real_profile(playwright, browser_reale)
        prepare_authenticated_direct_page(page, "open_session(profilo_reale)")
        return ArenaSession(browser=context.browser, context=context, page=page)

    profile_dir = config.LMARENA_PROFILE_DIR
    first_run = not profile_dir.exists()
    if first_run and not config.LMARENA_SESSION_PATH.exists():
        raise FileNotFoundError(
            f"Profilo LM Arena assente e nessuna sessione salvata in "
            f"{config.LMARENA_SESSION_PATH}. Esegui prima: python -m engine.session_manager"
        )
    profile_dir.mkdir(parents=True, exist_ok=True)

    context = playwright.chromium.launch_persistent_context(
        user_data_dir=str(profile_dir),
        headless=headless,
        viewport={"width": 1440, "height": 900},
        args=ARENA_LAUNCH_ARGS,
    )
    browser = context.browser
    if first_run and config.LMARENA_SESSION_PATH.exists():
        _seed_profile_from_saved_session(context)
    page = context.pages[0] if context.pages else context.new_page()
    prepare_authenticated_direct_page(page, "open_session")
    return ArenaSession(browser=browser, context=context, page=page)


def prepare_authenticated_direct_page(page: Page, where: str) -> None:
    """Naviga su LM Arena, chiude i dialoghi noti, verifica login+captcha, seleziona Direct.

    Estratta da `open_session()` (2026-08-15, PIANO-KDP libri via Arena v3) perche' la
    Fase 0 di validazione captcha deve fare esattamente questi controlli su un CONTEXT
    diverso (profilo Brave/Chrome reale, non il profilo Playwright dedicato) — duplicare
    la logica di login/captcha in due file e' il modo sicuro per farla divergere in
    silenzio. `open_session()` non cambia comportamento: questa funzione e' lo stesso
    codice, solo richiamabile da un punto solo. `where` identifica il chiamante nei log di
    debug e nei messaggi d'errore (prima era sempre "open_session", ora e' parametrico)."""
    # domcontentloaded, non networkidle: arena.ai tiene connessioni persistenti aperte
    # (chat live) che a volte impediscono a networkidle di scattare mai (timeout reale
    # riscontrato in CP4, 2026-08-05) — stesso pattern gia' usato in amazon_research.py.
    page.goto(config.LMARENA_BASE_URL, wait_until="domcontentloaded", timeout=config.DEFAULT_TIMEOUT_MS)
    time.sleep(2.5)
    try:
        page.get_by_text("Accept Cookies", exact=True).click(timeout=3000)
    except Exception:
        pass
    # Modale "Terms of Use & Privacy Policy" (mai visto prima di questa sessione, appare
    # con un overlay scuro che intercetta i click su tutto quello che sta sotto — bug
    # reale trovato via screenshot dal vivo dopo hang inspiegabili: senza dismissarlo,
    # _robust_click cade sul fallback per coordinate e clicca sull'overlay/il bottone
    # "Agree" stesso invece del vero bottone di invio, spiegando parte degli hang
    # intermittenti di questa sessione).
    try:
        page.get_by_role("button", name="Agree", exact=True).click(timeout=3000)
    except Exception:
        pass
    # Verifica esplicita di login — MAI procedere alla cieca su una sessione rotta.
    # Bug reale trovato con screenshot dal vivo: lo stesso identico storage_state, nella
    # stessa sessione di debug, e' risultato a volte autenticato e a volte no (bottone
    # "Log In" visibile in sidebar) — coerente con un'invalidazione della sessione lato
    # servizio sotto uso automatizzato intenso, non un bug di codice. Fallire subito con
    # un errore chiaro invece di procedere a inviare prompt su una chat mai raggiungibile
    # (causa root di alcuni degli hang "silenziosi" osservati oggi).
    if page.get_by_text("Log In", exact=True).count() > 0:
        raise RuntimeError(
            f"LM Arena ({where}): sessione NON autenticata (bottone 'Log In' visibile) — "
            "probabile invalidazione lato servizio o profilo non loggato su Arena. "
            "Verifica il login nel browser."
        )
    # Captcha gia' presente all'apertura: fallire SUBITO con la causa giusta, invece di
    # procedere e scoprirlo dopo minuti di attesa sul primo prompt (errore reale di CP5).
    if _captcha_present(page):
        _debug_log("captcha_detected", where=where)
        if not _wait_for_human_to_solve_captcha(page, where):
            raise CaptchaRequired(
                f"LM Arena ({where}): sfida 'Security Verification' (captcha) presente "
                f"all'apertura della sessione e non risolta entro {CAPTCHA_WAIT_SECONDS}s. "
                "Risolvila a mano nella finestra aperta e rilancia. Non e' aggirabile da codice."
            )
    _select_direct_mode(page)
    _assert_direct_mode(page, where)


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


def _assert_direct_mode(page: Page, where: str) -> None:
    """Verifica che la modalita' sia davvero Direct, non Battle Mode (segnalato da Gael il
    2026-08-07: le immagini venivano generate in Battle Mode). `_select_direct_mode` fa un
    tentativo ma non verificava mai l'esito — se il click falliva silenziosamente si
    generava con 2 modelli anonimi invece del modello scelto, rendendo l'output non
    verificabile ne' ripetibile. Qui si controlla e, se serve, si riprova una volta."""
    if page.locator("button:has-text('Battle Mode')").count() == 0:
        return  # gia' in Direct
    _debug_log("battle_mode_detected", where=where)
    _select_direct_mode(page)
    time.sleep(0.5)
    if page.locator("button:has-text('Battle Mode')").count() > 0:
        raise RuntimeError(
            f"LM Arena: impossibile passare a modalita' Direct ({where}) — la UI resta in "
            f"Battle Mode (2 modelli anonimi). Output non verificabile/ripetibile, mai "
            f"accettato: serve controllare la UI a mano."
        )


def _wrap_prompt_with_markers(prompt: str, req_id: str) -> str:
    """Avvolge il prompt con l'istruzione di delimitare la risposta con marcatori univoci.

    I marcatori sono DESCRITTI a parole, mai scritti per esteso (bug reale trovato subito
    al primo run del nuovo metodo, 2026-08-07): la pagina mostra anche l'eco del prompt
    inviato, quindi se il prompt contenesse i marcatori letterali la ricerca li troverebbe
    li' dentro ed estrarrebbe un pezzo dell'istruzione invece della risposta (osservato:
    "' and end it with the exact line '"). Descrivendoli, il testo esatto compare SOLO
    nella risposta del modello, che li compone."""
    return (
        f"{prompt}\n\n"
        f"IMPORTANT OUTPUT RULE: your reply must begin with three '#' characters "
        f"immediately followed by {req_id}, then a newline. Your reply must end with a "
        f"newline followed by {req_id} immediately followed by three '#' characters. "
        f"Put your entire answer between those two delimiter lines."
    )


def _markers_for(req_id: str) -> tuple[str, str]:
    return f"###{req_id}", f"{req_id}###"


def start_new_chat(page: Page) -> None:
    """Apre una chat NUOVA prima di inviare il prompt.

    Perche' (2026-08-07, osservazione dai run reali): il captcha non compare mai sul primo
    messaggio di una chat, ma quasi sempre su quelli successivi nella stessa conversazione
    — coerente col fatto che il workflow gia' in produzione (`arena_thumbnail.py`, una
    richiesta per run) non lo incontra mai. Qui non serve la memoria della conversazione:
    ogni prompt di capitolo contiene GIA' trama completa e riassunto dei capitoli
    precedenti (vedi `book_writer._chapter_prompt`), quindi una chat nuova per richiesta
    non perde nessun contesto. Non aggira nessuna verifica: evita di innescarla."""
    for name in ("New Chat", "Nuova chat"):
        try:
            btn = page.get_by_role("button", name=name, exact=False)
            if btn.count() == 0:
                btn = page.get_by_text(name, exact=False)
            for i in range(btn.count()):
                el = btn.nth(i)
                if el.is_visible():
                    _robust_click(el, timeout=5000)
                    time.sleep(2)
                    _debug_log("new_chat_started", via=name)
                    return
        except Exception:
            continue
    # Fallback: navigazione diretta alla pagina di chat nuova
    try:
        page.goto(config.LMARENA_BASE_URL, wait_until="domcontentloaded",
                  timeout=config.DEFAULT_TIMEOUT_MS)
        time.sleep(2)
        _select_direct_mode(page)
        _debug_log("new_chat_started", via="goto")
    except Exception as exc:
        _debug_log("new_chat_failed", error=str(exc))


def _dismiss_blocking_overlay(page: Page) -> None:
    """Chiude un eventuale dialog/overlay che intercetta i click (bug reale 2026-08-07:
    `<div data-state="open" ... bg-black/80> intercepts pointer events` impediva di
    cliccare la casella di testo). Prova i bottoni di conferma noti, poi Escape."""
    try:
        overlay = page.locator("div[data-state='open'][aria-hidden='true']")
        if overlay.count() == 0:
            return
    except Exception:
        return
    for name in ("Continue", "Agree", "Accept", "OK", "Got it", "Continua", "Accetta"):
        try:
            btn = page.get_by_role("button", name=name, exact=False)
            if btn.count() > 0 and btn.first.is_visible():
                _robust_click(btn.first, timeout=3000)
                time.sleep(0.8)
                _debug_log("overlay_dismissed", via=name)
                return
        except Exception:
            continue
    try:
        page.keyboard.press("Escape")
        time.sleep(0.5)
        _debug_log("overlay_dismissed", via="Escape")
    except Exception:
        pass


def _extract_between_markers(page: Page, req_id: str) -> str | None:
    """Estrae la risposta cercando i marcatori univoci nel testo dell'INTERA pagina.

    APPROCCIO RISCRITTO IL 2026-08-07 (su richiesta esplicita di Gael: "è da 2 giorni che
    continui a dire di aver trovato il bug vero, cambia completamente approccio"). Il
    metodo precedente indovinava quale nodo della DOM fosse la risposta (`[class*="prose"]`
    fuori da una bolla utente, primo o ultimo elemento) e ha prodotto una catena di bug
    diversi: risposta del turno precedente, risposta identica all'outline, ordine DOM
    invertito, testo troncato. Ognuno "risolto" da un'ipotesi nuova sulla struttura della
    pagina, che il ciclo dopo si rivelava sbagliata.

    Qui non si indovina piu' niente. Ogni richiesta porta un ID univoco che il modello
    deve ripetere in apertura e chiusura; si legge `document.body.innerText` (stesso
    approccio di `read_arena_chat.py`, in produzione) e si prende cio' che sta fra i due
    marcatori. Proprieta' garantite senza assunzioni sulla UI:
    - impossibile restituire la risposta di un altro turno (l'ID e' unico per richiesta);
    - la presenza del marcatore di CHIUSURA prova che la risposta e' COMPLETA, non
      troncata a meta' (bug che prima serviva un controllo separato per rilevare);
    - indipendente da classi CSS, ordine dei nodi, bolle utente/assistente.

    Ritorna None se la risposta non e' ancora completa (marcatori assenti) — il chiamante
    interpreta questo come "continua ad aspettare"."""
    body = page.evaluate("() => document.body.innerText") or ""
    open_marker, close_marker = _markers_for(req_id)
    start = body.find(open_marker)
    if start == -1:
        return None
    end = body.find(close_marker, start + len(open_marker))
    if end == -1:
        return None
    return body[start + len(open_marker):end].strip()


def _count_assistant_messages(page: Page) -> int:
    """Conta i messaggi di risposta del modello presenti ORA (elementi `[class*="prose"]`
    fuori da una bolla utente). Usato per verificare che l'estrazione prenda davvero la
    risposta NUOVA e non una vecchia (vedi bug in `_extract_latest_response_text`)."""
    return page.evaluate(
        """() => {
            const els = document.querySelectorAll('[class*="prose"]');
            let n = 0;
            for (const el of els) {
                if (!el.closest('[class*="bg-surface-raised"]')) n++;
            }
            return n;
        }"""
    )


def _extract_latest_response_text(page: Page) -> str | None:
    """Elemento `[class*="prose"]` FUORI da una bolla utente (`bg-surface-raised`) — la
    risposta del modello, mai il prompt, verificato per struttura non per contenuto.

    Prende il PRIMO elemento che soddisfa il criterio: nella DOM di questa chat i messaggi
    sono in ordine INVERTITO (il piu' recente per primo). Verificato dal vivo il 2026-08-07
    con un dump completo degli elementi: idx=0 era il prompt appena inviato, idx=4 il primo
    messaggio della conversazione.

    Storia di questo selettore, per non ripetere l'errore: era `first`, poi cambiato in
    `last` il 2026-08-06 credendo che la DOM crescesse in ordine cronologico — quel cambio
    ha INTRODOTTO un bug peggiore (si estraeva sempre il messaggio piu' VECCHIO, cioe'
    l'outline al posto di ogni capitolo), trovato subito dopo grazie al log di debug e alla
    guardia `prior_text`. Tornato a `first`, che e' corretto per questa UI. Le guardie
    (`baseline_count`, `prior_text`, anti-duplicato in book_writer) restano: sono loro ad
    aver reso visibile l'errore invece di lasciar passare capitoli sbagliati."""
    return page.evaluate(
        """() => {
            const els = document.querySelectorAll('[class*="prose"]');
            for (const el of els) {
                if (!el.closest('[class*="bg-surface-raised"]')) return el.innerText;
            }
            return null;
        }"""
    )


def send_text_prompt(page: Page, prompt: str, timeout_s: int = 600,
                      force_new_chat: bool = True) -> str:
    """Invia un prompt, aspetta la risposta COMPLETA, la estrae e la ritorna.

    METODO RISCRITTO IL 2026-08-07 — vedi `_extract_between_markers` per il perche'
    (richiesta esplicita di Gael di cambiare approccio dopo una catena di bug diversi
    tutti dovuti a ipotesi sbagliate sulla struttura della pagina).

    Come funziona ora, senza indovinare nulla della UI:
    1. si genera un ID univoco e si chiede al modello di delimitare la risposta con esso;
    2. si invia (rispettando una pausa minima fra invii, per non martellare il servizio);
    3. si legge il testo dell'intera pagina finche' NON compaiono entrambi i marcatori —
       la presenza di quello di chiusura e' la prova che la risposta e' finita e completa,
       quindi non serve piu' indovinare "quando ha finito" dal placeholder 'Generating...';
    4. lungo l'attesa si gestiscono captcha (pausa per intervento umano) ed errore lato
       sito (click sul 'Retry' della UI).

    `force_new_chat` (2026-08-15, PIANO-KDP libri via Arena v3): di default apre una chat
    nuova a ogni invio (comportamento invariato dal 2026-08-07, vedi `start_new_chat`).
    Impostare `False` riusa la chat corrente — serve alla Fase 0 di validazione captcha per
    confrontare i due pattern, e alla scrittura del copy KDP che deve girare nella STESSA
    chat degli ultimi capitoli. Non e' provato quale pattern eviti meglio il captcha: e'
    proprio cio' che la Fase 0 misura, non un'assunzione.

    Solleva errori espliciti (TimeoutError/RuntimeError/CaptchaRequired) — mai un testo
    finto, mai una risposta di un altro turno."""
    import uuid

    req_id = f"REQ{uuid.uuid4().hex[:10].upper()}"
    wrapped = _wrap_prompt_with_markers(prompt, req_id)
    _debug_log("send_start", req_id=req_id, prompt_len=len(prompt),
               prompt_preview=prompt[:120], url=page.url, force_new_chat=force_new_chat)

    def _fill_and_send() -> None:
        _throttle_before_send()
        # Chat nuova per ogni richiesta (default): evita di innescare il captcha, che nei
        # run reali non compare mai sul primo messaggio di una chat (vedi `start_new_chat`).
        # Se force_new_chat=False si riusa la chat corrente (vedi docstring sopra).
        if force_new_chat:
            start_new_chat(page)
        _dismiss_blocking_overlay(page)
        tb = page.locator("textarea, [contenteditable='true']").first
        tb.click()
        tb.fill(wrapped)
        time.sleep(0.3)
        _robust_click(page.locator("form button[aria-label='Send message']"))
        time.sleep(1.0)

    _fill_and_send()

    ui_retries = 0
    resends = 0
    waited = 0
    while waited < timeout_s:
        # 1) risposta completa? (entrambi i marcatori presenti)
        text = _extract_between_markers(page, req_id)
        if text:
            _debug_log("send_ok", req_id=req_id, waited=waited, **_text_fingerprint(text))
            return text

        # 2) captcha: pausa, intervento umano, poi si rimanda il prompt
        if _captcha_present(page):
            _debug_log("captcha_detected", req_id=req_id, waited=waited)
            if not _wait_for_human_to_solve_captcha(page, "send_text_prompt"):
                raise CaptchaRequired(
                    f"LM Arena: captcha non risolto entro {CAPTCHA_WAIT_SECONDS}s. "
                    "Risolvilo nella finestra aperta e rilancia. Non e' aggirabile da "
                    "codice e non va aggirata."
                )
            if resends < config.MAX_RETRIES:
                resends += 1
                _fill_and_send()
                waited = 0
                continue
            raise RuntimeError("LM Arena: troppi captcha consecutivi, run interrotto")

        # 3) errore lato sito: si usa il bottone 'Retry' che la UI stessa offre
        if _generation_error_present(page):
            if ui_retries < MAX_UI_RETRY_CLICKS and _click_retry_button(page):
                ui_retries += 1
                _debug_log("generation_error_retry", req_id=req_id, attempt=ui_retries)
                print(f"[lmarena] errore lato sito — clicco 'Retry' "
                      f"({ui_retries}/{MAX_UI_RETRY_CLICKS})", flush=True)
                time.sleep(3)
                waited += 3
                continue
            if resends < config.MAX_RETRIES:
                resends += 1
                _debug_log("generation_error_resend", req_id=req_id, resend=resends)
                print(f"[lmarena] errore lato sito, 'Retry' non disponibile — rimando il "
                      f"prompt ({resends}/{config.MAX_RETRIES})", flush=True)
                _fill_and_send()
                waited = 0
                continue
            _debug_log("generation_error_fatal", req_id=req_id)
            raise RuntimeError(
                "LM Arena: errore di generazione lato sito ('Something went wrong') non "
                f"risolto dopo {ui_retries} Retry e {resends} reinvii."
            )

        time.sleep(3)
        waited += 3

    _debug_log("send_timeout", req_id=req_id, waited=waited)
    raise TimeoutError(
        f"LM Arena: risposta completa non ricevuta dopo {timeout_s}s "
        f"(marcatori {req_id} mai comparsi entrambi)"
    )



def _current_img_srcs(page: Page) -> set:
    return set(page.locator("img").evaluate_all("els => els.map(e => e.src || '')"))


def send_image_prompt(page: Page, prompt: str, out_path: Path,
                       source_image_path: Path | None = None, timeout_s: int = 480) -> Path:
    """Passa in modalita' immagine, invia il prompt (con allegato opzionale), aspetta il
    completamento REALE (placeholder 'Generating image...' che sparisce), salva il file .png
    reale su disco in `out_path`. Stesso pattern gia' verificato in produzione in
    arena_thumbnail.py — qui generalizzato (out_path esplicito, non hardcoded).

    Rilevamento captcha + log + timeout allungato (2026-08-07): stesse protezioni gia'
    costruite e verificate per il testo, applicate qui perche' il sintomo osservato sulle
    immagini (placeholder 'Generating image...' che non sparisce mai fino al timeout) e'
    IDENTICO a quello che sul testo si e' rivelato essere il captcha — ipotesi non ancora
    confermata dal vivo sulle immagini, ma le protezioni sono corrette a prescindere:
    se e' captcha lo dice subito, se non lo e' il log mostra cos'altro succede."""
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

    # Il passaggio in modalita' immagine puo' riportare la UI in Battle Mode (segnalato da
    # Gael il 2026-08-07 guardando la finestra reale: le copertine venivano generate in
    # Battle Mode invece che in Direct/Max). Riverificato e ricorretto qui, DOPO il cambio
    # modalita' — farlo solo in open_session non basta.
    _assert_direct_mode(page, "send_image_prompt")

    if source_image_path is not None:
        page.locator("input[type='file']").first.set_input_files(str(source_image_path), timeout=8000)
        try:
            page.locator("form img, form [aria-label*='attach' i]").first.wait_for(
                state="visible", timeout=20000)
        except Exception:
            pass

    ignore_srcs = _current_img_srcs(page)
    _debug_log("image_send_start", prompt_len=len(prompt), prompt_preview=prompt[:120],
               known_imgs=len(ignore_srcs), url=page.url)
    textbox = page.locator("textarea, [contenteditable='true']").first
    textbox.click()
    textbox.fill(prompt)
    time.sleep(0.3)
    _robust_click(page.locator("form button[aria-label='Send message']"))
    time.sleep(0.8)  # stesso margine di send_text_prompt: evita un primo check troppo rapido

    waited, max_wait = 0, timeout_s
    img_retries = 0
    while waited < max_wait:
        if _captcha_present(page):
            _debug_log("captcha_detected", where="send_image_prompt", waited=waited)
            if not _wait_for_human_to_solve_captcha(page, "send_image_prompt"):
                raise CaptchaRequired(
                    "LM Arena: captcha durante la generazione immagine, non risolto entro "
                    f"{CAPTCHA_WAIT_SECONDS}s. Risolvilo nella finestra aperta e rilancia. "
                    "Non e' aggirabile da codice e non va aggirata."
                )
            # Captcha risolto: la generazione era bloccata, va rimandata da capo.
            textbox = page.locator("textarea, [contenteditable='true']").first
            textbox.click()
            textbox.fill(prompt)
            time.sleep(0.3)
            _robust_click(page.locator("form button[aria-label='Send message']"))
            time.sleep(0.8)
            waited = 0
            continue
        # Stesso errore lato sito gestito per il testo (banner + bottone Retry della UI).
        if _generation_error_present(page):
            if img_retries < MAX_UI_RETRY_CLICKS and _click_retry_button(page):
                img_retries += 1
                _debug_log("image_generation_error_retry", attempt=img_retries, waited=waited)
                print(f"[lmarena] errore generazione immagine lato sito — clicco 'Retry' "
                      f"({img_retries}/{MAX_UI_RETRY_CLICKS})", flush=True)
                time.sleep(3)
                waited += 3
                continue
            _debug_log("image_generation_error_fatal", retries_used=img_retries)
            raise RuntimeError(
                "LM Arena: errore di generazione immagine lato sito ('Something went "
                f"wrong') non risolto dopo {img_retries} click su Retry."
            )
        pending = page.get_by_text("Generating image...").count()
        if pending == 0:
            break
        time.sleep(3)
        waited += 3
    else:
        _debug_log("image_timeout", waited=waited)
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
        _debug_log("image_ok", path=str(out_path), size_kb=round(out_path.stat().st_size / 1024, 1))
        return out_path

    _debug_log("image_not_found", total_imgs=imgs.count(), known_imgs=len(ignore_srcs))
    raise RuntimeError("LM Arena: nessuna immagine nuova trovata dopo la generazione")


if __name__ == "__main__":
    import sys
    import tempfile

    from playwright.sync_api import sync_playwright

    print("=== CP4 self-test REALE: testo + immagine su LM Arena (sessione vera) ===\n")

    with sync_playwright() as p:
        session = open_session(p)
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
