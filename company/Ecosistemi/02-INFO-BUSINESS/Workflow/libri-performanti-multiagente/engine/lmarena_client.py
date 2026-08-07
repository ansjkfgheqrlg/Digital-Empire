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
        self.context.close()
        self.browser.close()


def open_session(playwright: Playwright, headless: bool = False) -> ArenaSession:
    """Apre LM Arena con la sessione reale salvata (CP1) e seleziona la modalita' Direct.
    Fatto = pronta per send_text_prompt/send_image_prompt, nessun login richiesto.

    DEFAULT headless=False (2026-08-07, bug reale trovato e verificato con screenshot):
    in modalita' nascosta (headless=True) LM Arena mostra una sfida "Security
    Verification" (reCAPTCHA "I'm not a robot") che blocca ogni generazione — verificato
    che NON compare affatto in una finestra normale (headless=False), a parita' di
    profilo/sessione/account, con Gael che ha confermato una generazione riuscita subito
    dopo l'apertura. Non e' un problema di rate-limit o di codice: e' un rilevamento
    specifico della modalita' headless lato servizio. Nessun tentativo di aggirare la
    verifica stessa — si evita semplicemente di innescarla, usando una finestra reale.

    CORRETTO 2026-08-06: prima lanciava l'intero profilo Brave reale copiato (381MB,
    con Safe Browsing/Crowd Deny/component-updater/estensioni) via
    `launch_persistent_context` — trovato essere la causa di lanci del browser che vanno
    in timeout (180s) dopo l'accumulo di ~20+ lanci automatizzati sulla stessa copia.
    Ora usa lo STESSO pattern gia' verificato affidabile per Amazon
    (`session_manager.load_context`): Chromium bundlato di Playwright, pulito ad ogni
    lancio, con solo cookie/localStorage iniettati da `lmarena_state.json` (esportato in
    CP1) — nessun profilo browser reale coinvolto, nessuno stato che si accumula."""
    if not config.LMARENA_SESSION_PATH.exists():
        raise FileNotFoundError(
            f"Sessione LM Arena non trovata: {config.LMARENA_SESSION_PATH}. "
            f"Esegui prima: python -m engine.session_manager"
        )
    browser = playwright.chromium.launch(headless=headless, args=ARENA_LAUNCH_ARGS)
    context = browser.new_context(
        storage_state=str(config.LMARENA_SESSION_PATH),
        viewport={"width": 1440, "height": 900},
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
            text = _wait_for_completion_and_extract(page, attempt_timeout, baseline_count, prior_text)
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
                                      prior_text: str | None) -> str:
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
        session = open_session(p, headless=False)
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
