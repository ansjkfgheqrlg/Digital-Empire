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
    Ritorna True se il click e' riuscito."""
    for name in ("Retry", "Riprova"):
        try:
            btn = page.get_by_role("button", name=name, exact=True)
            if btn.count() > 0:
                _robust_click(btn.first, timeout=5000)
                return True
        except Exception:
            continue
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


def open_session(playwright: Playwright, headless: bool = True) -> ArenaSession:
    """Apre LM Arena su un PROFILO PERSISTENTE dedicato e seleziona la modalita' Direct.
    Fatto = pronta per send_text_prompt/send_image_prompt, nessun login richiesto.

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
            "LM Arena: sessione NON autenticata (bottone 'Log In' visibile) — "
            f"probabile invalidazione lato servizio di {config.LMARENA_SESSION_PATH}. "
            "Rifare il login: python -m engine.session_manager"
        )
    # Captcha gia' presente all'apertura: fallire SUBITO con la causa giusta, invece di
    # procedere e scoprirlo dopo minuti di attesa sul primo prompt (errore reale di CP5).
    if _captcha_present(page):
        _debug_log("captcha_detected", where="open_session")
        if not _wait_for_human_to_solve_captcha(page, "open_session"):
            raise CaptchaRequired(
                "LM Arena: sfida 'Security Verification' (captcha) presente all'apertura "
                f"della sessione e non risolta entro {CAPTCHA_WAIT_SECONDS}s. Risolvila a "
                "mano nella finestra aperta e rilancia. Non e' aggirabile da codice."
            )
    _select_direct_mode(page)
    _assert_direct_mode(page, "open_session")
    return ArenaSession(browser=browser, context=context, page=page)


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

    Prende l'ULTIMO elemento che soddisfa il criterio, non il primo — bug reale trovato in
    CP5 (2026-08-06, verificato dal vivo): con prompt di generazione piu' lunga/pesante
    (i capitoli veri, non gli echo brevi dei test precedenti), un retry-con-reload poteva
    innescarsi mentre la generazione era ancora davvero in corso lato server; al reload la
    UI mostrava temporaneamente solo i messaggi GIA' completati, e prendere il primo
    elemento fuori da bolla utente restituiva sempre la risposta del PRIMO turno della chat
    — sintomo osservato: 3 capitoli "diversi" richiesti, testo IDENTICO parola per parola
    per tutti e 3. La DOM cresce in ordine cronologico (verificato con diagnostica dal vivo:
    il conteggio elementi passa 1→2→3 dopo turni successivi), quindi l'ultimo elemento e'
    sempre il piu' recente — combinato con la verifica del conteggio in
    `_wait_for_completion_and_extract` (mai accettare una risposta se il conteggio dei
    messaggi non e' aumentato rispetto a prima dell'invio)."""
    return page.evaluate(
        """() => {
            const els = document.querySelectorAll('[class*="prose"]');
            let last = null;
            for (const el of els) {
                if (!el.closest('[class*="bg-surface-raised"]')) last = el;
            }
            return last ? last.innerText : null;
        }"""
    )


def send_text_prompt(page: Page, prompt: str, timeout_s: int = 600) -> str:
    """Invia un prompt di testo, aspetta il completamento REALE, estrae e torna la risposta
    reale. Solleva TimeoutError/RuntimeError espliciti se qualcosa non torna, mai un testo
    finto.

    Rilevamento completamento: placeholder 'Generating...' che sparisce (stesso pattern gia'
    verificato per le immagini, non un timeout fisso). Il bottone 'Stop generation' NON e'
    affidabile da solo — bug reale trovato in CP4: per risposte brevi/quasi istantanee il
    bottone non transita mai visibilmente per lo stato 'Stop generation' (la generazione
    finisce troppo in fretta), mentre il placeholder 'Generating...' compare comunque anche
    per risposte di una sola frase (verificato con screenshot reale).

    Stabilita' testo post-placeholder (bug reale trovato dopo il fix della sessione
    leggera 2026-08-06): il placeholder 'Generating...' puo' sparire un istante PRIMA che
    l'ultimo chunk di testo sia effettivamente renderizzato nel DOM — estrarre subito dopo
    da' un testo troncato a meta' frase (osservato: risposta finita su "...becomes" senza
    punto). Fix: dopo la sparizione del placeholder, si rilegge il testo finche' non resta
    IDENTICO fra due letture consecutive (testo ancora cambiante = ancora in rendering).

    Retry via reload (bug reale trovato in CP5, intermittente — a volte al primo
    messaggio, a volte al secondo, nessun pattern fisso): il placeholder 'Generating...'
    a volte non sparisce mai lato client pur essendo la risposta gia' pronta lato server
    — coerente con una connessione live (WebSocket) persa silenziosamente durante una
    sessione headless lunga, mai un vero hang del modello (l'account funziona
    normalmente in un browser umano normale, confermato da Gael). Fix: se il timeout
    scatta, si ricarica la pagina (forza una riconnessione pulita, la chat e' salvata
    lato server quindi non si perde nulla) e si ricontrolla — MAI si rimanda il prompt,
    solo si rilegge lo stato vero. Fino a config.MAX_RETRIES tentativi totali.

    Verifica anti-risposta-vecchia (CP5, 2026-08-06): si conta quanti messaggi di risposta
    esistono PRIMA di inviare il prompt (`baseline_count`) — dopo, si accetta solo un
    conteggio maggiore, mai una risposta "gia' li'" da un turno precedente (vedi bug
    descritto in `_extract_latest_response_text`).

    Ogni tentativo e' loggato in `sessions/debug_logs/lmarena_<data>.jsonl` (prompt/risposta
    con hash e lunghezza, mai il testo intero per non gonfiare il log) — nato dal bug
    duplicati di CP5, per non dover piu' ricostruire cosa e' successo rilanciando tutto.

    Verifica anti-risposta-invariata (CP5, 2026-08-07, secondo bug reale trovato dopo il
    fix precedente): il conteggio messaggi da solo non basta — osservato un caso in cui il
    conteggio NON e' nemmeno servito da segnale (l'estrazione ha restituito il testo
    dell'OUTLINE, generata da una chiamata precedente, come "risposta" del primo capitolo).
    Fix aggiuntivo: si cattura il testo dell'ultima risposta ESISTENTE prima dell'invio
    (`prior_text`) e si rifiuta esplicitamente un risultato identico ad esso — indipendente
    dal conteggio, cattura anche i casi in cui quest'ultimo da solo non basta.

    Timeout di default alzato a 600s (CP5, 2026-08-07): verificato con diagnostica dal vivo
    che generazioni strutturate/lunghe (outline, capitoli) possono restare genuinamente in
    corso oltre i 300s precedenti, senza alcun blocco reale — semplicemente piu' lente di
    una risposta breve. I retry dopo reload restano a 45s (invariato): quel timeout ha uno
    scopo diverso, rilevare in fretta una risposta gia' pronta ma non riflessa lato client,
    non aspettare una generazione lenta da zero."""
    baseline_count = _count_assistant_messages(page)
    prior_text = _extract_latest_response_text(page) if baseline_count > 0 else None
    _debug_log("send_start", prompt_len=len(prompt), prompt_preview=prompt[:120],
               baseline_count=baseline_count, url=page.url)

    def _fill_and_send() -> None:
        tb = page.locator("textarea, [contenteditable='true']").first
        tb.click()
        tb.fill(prompt)
        time.sleep(0.3)
        _robust_click(page.locator("form button[aria-label='Send message']"))
        time.sleep(0.8)  # margine perche' il placeholder 'Generating...' compaia nel DOM
                          # prima del primo controllo — senza, un check troppo rapido puo'
                          # vederlo ancora assente e uscire credendo che sia gia' finita

    _fill_and_send()
    fresh_send = True  # True quando il prompt e' appena stato (ri)mandato: serve il
                       # timeout pieno, non quello breve dei retry-da-reload
    # Contatore condiviso dei click su "Retry" della UI (lista di 1 elemento perche' va
    # mutato da dentro `_wait_for_completion_and_extract`, che riceve il riferimento).
    retries_used = [0]

    last_error: Exception | None = None
    for attempt in range(1, config.MAX_RETRIES + 1):
        # Timeout pieno solo quando si attende una generazione appena avviata (la
        # generazione puo' essere genuinamente lunga). I retry dopo un reload servono a
        # rilevare una risposta GIA' pronta lato server ma non riflessa lato client (vedi
        # docstring) — se il reload non la rivela in una manciata di secondi, aspettare di
        # nuovo per intero non aiuta: meglio ricaricare ancora che stare fermi.
        attempt_timeout = timeout_s if fresh_send else min(timeout_s, 45)
        fresh_send = False
        try:
            text = _wait_for_completion_and_extract(page, attempt_timeout, baseline_count,
                                                     prior_text, retries_used)
            _debug_log("send_ok", attempt=attempt, **_text_fingerprint(text))
            return text
        except CaptchaRequired as exc:
            # Il captcha NON si aggira: si mette in pausa e si aspetta che lo risolva una
            # persona nella finestra aperta. Se risolto, si RIMANDA il prompt (quello di
            # prima non e' mai partito davvero, era bloccato dal captcha) e si continua —
            # cosi' l'intervento umano serve una volta sola, senza perdere il lavoro gia'
            # fatto nelle fasi precedenti del run.
            _debug_log("captcha_detected", attempt=attempt, error=str(exc))
            if not _wait_for_human_to_solve_captcha(page, "send_text_prompt"):
                raise CaptchaRequired(
                    "LM Arena: captcha non risolto entro "
                    f"{CAPTCHA_WAIT_SECONDS}s — run interrotto. Risolvilo nella finestra "
                    "aperta e rilancia. Non e' aggirabile da codice e non va aggirata."
                ) from exc
            baseline_count = _count_assistant_messages(page)
            prior_text = _extract_latest_response_text(page) if baseline_count > 0 else None
            _fill_and_send()
            fresh_send = True
            continue
        except (TimeoutError, RuntimeError) as exc:
            last_error = exc
            _debug_log("send_attempt_failed", attempt=attempt, error=str(exc))
            if attempt < config.MAX_RETRIES:
                # Reload SOLO se l'URL e' gia' quello di una chat specifica (bug reale
                # trovato: se si ricarica mentre l'URL e' ancora quello base, si perde
                # la chat intera invece di recuperare la risposta gia' pronta — la
                # pagina torna a una chat nuova vuota). Sulla base URL ci si limita ad
                # aspettare ancora, senza navigare via da nulla.
                if page.url.rstrip("/") != config.LMARENA_BASE_URL.rstrip("/"):
                    page.reload(wait_until="domcontentloaded", timeout=config.DEFAULT_TIMEOUT_MS)
                    time.sleep(2)
                    _debug_log("reload_retry", attempt=attempt)
    _debug_log("send_failed_all_attempts", error=str(last_error))
    raise last_error


def _wait_for_completion_and_extract(page: Page, timeout_s: int, baseline_count: int,
                                      prior_text: str | None,
                                      retries_used: list[int] | None = None) -> str:
    if retries_used is None:
        retries_used = [0]
    waited, max_wait = 0, timeout_s
    while waited < max_wait:
        # Captcha: controllato PRIMA di tutto il resto e ad ogni giro. Se compare, la
        # generazione non partira' mai — continuare ad aspettare significa solo bruciare
        # l'intero timeout su una causa gia' nota (errore reale ripetuto in CP5).
        if _captcha_present(page):
            raise CaptchaRequired(
                "LM Arena: sfida 'Security Verification' (captcha) attiva — la generazione "
                "e' bloccata finche' non viene risolta a mano."
            )
        # Errore lato server con bottone "Retry" nella UI: senza questo controllo si
        # aspettava una generazione che non sarebbe mai arrivata, fino al timeout
        # (segnalato da Gael con screenshot, 2026-08-07). Si usa il Retry della UI stessa,
        # fino a un numero limitato di volte, poi si fallisce onestamente.
        if _generation_error_present(page):
            if retries_used[0] < MAX_UI_RETRY_CLICKS and _click_retry_button(page):
                retries_used[0] += 1
                _debug_log("generation_error_retry", attempt=retries_used[0], waited=waited)
                print(f"[lmarena] errore di generazione lato sito — clicco 'Retry' "
                      f"({retries_used[0]}/{MAX_UI_RETRY_CLICKS})", flush=True)
                time.sleep(3)
                waited += 3
                continue
            _debug_log("generation_error_fatal", retries_used=retries_used[0])
            raise RuntimeError(
                "LM Arena: errore di generazione lato sito ('Something went wrong') "
                f"non risolto dopo {retries_used[0]} click su Retry — mai mascherato "
                "da timeout generico."
            )
        pending = page.get_by_text("Generating", exact=False).count()
        # baseline_count: mai considerare "fatto" finche' non e' comparso un messaggio IN
        # PIU' rispetto a prima dell'invio — senza questo controllo, un reload che rivela
        # solo l'ultimo messaggio GIA' completato (il turno precedente, non quello nuovo)
        # verrebbe scambiato per "generazione finita" (bug reale corretto in CP5).
        if pending == 0 and _count_assistant_messages(page) > baseline_count:
            break
        time.sleep(1)
        waited += 1
    else:
        raise TimeoutError(f"LM Arena: generazione testo non completata dopo {max_wait}s")
    time.sleep(1)  # margine per il rendering finale dopo la sparizione del placeholder

    text = _extract_latest_response_text(page)
    stable_checks, max_stable_checks, total_checks, max_total_checks = 0, 2, 0, 30
    while stable_checks < max_stable_checks and total_checks < max_total_checks:
        time.sleep(1)
        total_checks += 1
        recheck = _extract_latest_response_text(page)
        if recheck == text and recheck is not None:
            stable_checks += 1
        else:
            text = recheck
            stable_checks = 0
    if text is None:
        raise RuntimeError("LM Arena: nessuna risposta testuale trovata dopo la generazione")
    if _count_assistant_messages(page) <= baseline_count:
        raise RuntimeError(
            "LM Arena: nessun messaggio nuovo rilevato dopo la generazione (probabile "
            "estrazione di una risposta di un turno precedente) — mai accettata"
        )
    if prior_text is not None and text == prior_text:
        raise RuntimeError(
            "LM Arena: la risposta estratta e' IDENTICA all'ultima risposta gia' presente "
            "prima dell'invio (probabile estrazione di una risposta vecchia/di un turno "
            "precedente, bug reale trovato in CP5 2026-08-07) — mai accettata"
        )
    return text


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
