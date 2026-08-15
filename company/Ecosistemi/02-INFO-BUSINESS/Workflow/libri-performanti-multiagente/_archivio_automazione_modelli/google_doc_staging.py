"""
Google Doc Staging (2026-08-15, PIANO-KDP libri via Arena v3) — Fase 3: un posto sicuro
dove il testo di ogni capitolo, appena estratto da LM Arena, non si perde mai — richiesta
esplicita di Gael ("in modo chirurgico perfetto, senza tralasciare neanche una parola").

RUOLO ESATTO, deciso esplicitamente (non da questo modulo): SOLO staging/sicurezza. Il
manoscritto vero e il PDF finale restano `engine/kdp_formatter.py` (gia' costruito, gia'
corretto per trim 6x9in e margini KDP) — questo modulo non genera mai un proprio PDF, e un
suo fallimento non deve MAI bloccare la scrittura dei capitoli, che scrivono comunque su
file (`BookProject`, gia' un canale affidabile). Per questo `append_chapter()` non solleva
mai un'eccezione verso il chiamante: ritorna un bool e logga.

Nessuna automazione Google Docs esisteva nel repo prima di questo file (verificato con
grep sull'intero monorepo). Costruita via Playwright, come richiesto esplicitamente — non
l'API REST di Google, che richiederebbe credenziali OAuth separate.

Profilo PERSISTENTE dedicato (`config.GOOGLE_DOCS_PROFILE_DIR`), non storage_state
effimero come Amazon: un editor stateful come Google Docs beneficia di un browser
"riconosciuto" almeno quanto Arena (stesso principio di `lmarena_client.LMARENA_PROFILE_DIR`).
Gira su un browser/context SEPARATO da quello di Arena — un hang di Google Docs non deve
poter bloccare la generazione dei capitoli.

Selettori Google Docs NON ancora verificati dal vivo (prima esecuzione mai fatta su questo
progetto) — segnalato esplicitamente, coerente con lo stile del resto del codice (mai
dichiarare verificato cio' che non lo e' stato): se al primo uso reale un selettore
risulta impreciso, va corretto guardando la pagina vera, non indovinato di nuovo qui.
"""
from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import Page, Playwright

from . import config

GOOGLE_DOCS_HOME_URL = "https://docs.google.com/document/u/0/"
GOOGLE_DOCS_CREATE_URL = "https://docs.google.com/document/create"


@dataclass
class GoogleDocSession:
    context: object
    page: Page
    doc_url: str


def _google_non_autenticato(page: Page) -> bool:
    """Vero se la pagina mostra un invito al login — stessa verifica esplicita gia' usata
    per Arena/Amazon (mai procedere alla cieca su una sessione forse rotta)."""
    for testo in ("Sign in", "Accedi"):
        try:
            if page.get_by_role("link", name=testo, exact=False).count() > 0:
                return True
        except Exception:
            continue
    return False


def ensure_google_session(playwright: Playwright, headless: bool = False) -> bool:
    """Garantisce un login Google nel profilo persistente dedicato a questo staging.

    Stesso principio del profilo persistente Arena: una volta loggato, il profilo resta
    autenticato fra i run — non serve rifare il login ogni volta. Ritorna True se gia'
    autenticato, False se e' appena stato fatto un login (mai un login automatico: Google
    blocca l'OAuth sotto automazione, stesso problema gia' documentato per Amazon/Arena in
    `session_manager.py` — qui pero' basta un profilo persistente gia' loggato una volta a
    mano, senza il giro del profilo Chrome "raw" perche' non serve un OAuth completo ogni
    volta, solo la PRIMA)."""
    profile_dir = config.GOOGLE_DOCS_PROFILE_DIR
    profile_dir.mkdir(parents=True, exist_ok=True)

    context = playwright.chromium.launch_persistent_context(
        user_data_dir=str(profile_dir), headless=headless,
        viewport={"width": 1280, "height": 900},
    )
    try:
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(GOOGLE_DOCS_HOME_URL, wait_until="domcontentloaded",
                  timeout=config.DEFAULT_TIMEOUT_MS)
        page.wait_for_timeout(2000)
        if not _google_non_autenticato(page):
            print(f"[google_doc_staging] profilo gia' autenticato: {profile_dir}")
            return True

        if headless:
            raise RuntimeError(
                "Google Docs: profilo non autenticato e headless=True — impossibile fare "
                "login manuale. Rilancia con headless=False."
            )
        print("\n[google_doc_staging] NESSUN login Google rilevato nel profilo dedicato.")
        input(">>> Fai login su Google nella finestra aperta, poi premi INVIO qui nel "
              "terminale...\n")
        page.wait_for_timeout(1500)
        if _google_non_autenticato(page):
            raise RuntimeError(
                "Google Docs: login non riuscito (ancora non autenticato dopo il tentativo)."
            )

        config.GOOGLE_SESSION_PATH.parent.mkdir(parents=True, exist_ok=True)
        context.storage_state(path=str(config.GOOGLE_SESSION_PATH))
        print(f"[google_doc_staging] login completato, sessione salvata in "
              f"{config.GOOGLE_SESSION_PATH}")
        return False
    finally:
        context.close()


def open_or_create_doc(playwright: Playwright, titolo_libro: str,
                        doc_url_esistente: str | None = None) -> GoogleDocSession:
    """Apre un Google Doc esistente (resume, `doc_url_esistente` salvato in `progetto.json`
    da un run precedente) o ne crea uno nuovo intitolato al libro. Solleva un'eccezione se
    il setup fallisce — a differenza di `append_chapter`, questo gira UNA volta sola
    all'inizio: il chiamante (Fase 3 orchestrata da `workflow.py`) decide se trattare un
    fallimento qui come "salta lo staging per questo libro" senza abortire la scrittura,
    non questo modulo."""
    profile_dir = config.GOOGLE_DOCS_PROFILE_DIR
    profile_dir.mkdir(parents=True, exist_ok=True)
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=str(profile_dir), headless=False,
        viewport={"width": 1280, "height": 900},
    )
    try:
        context.grant_permissions(["clipboard-read", "clipboard-write"],
                                  origin="https://docs.google.com")
    except Exception as exc:
        print(f"[google_doc_staging] impossibile concedere i permessi clipboard "
              f"(non bloccante, si tenta comunque): {exc}")

    page = context.pages[0] if context.pages else context.new_page()

    if doc_url_esistente:
        page.goto(doc_url_esistente, wait_until="domcontentloaded",
                  timeout=config.DEFAULT_TIMEOUT_MS)
        page.wait_for_timeout(2000)
        return GoogleDocSession(context=context, page=page, doc_url=doc_url_esistente)

    page.goto(GOOGLE_DOCS_CREATE_URL, wait_until="domcontentloaded",
              timeout=config.DEFAULT_TIMEOUT_MS)
    page.wait_for_timeout(2500)
    if _google_non_autenticato(page):
        context.close()
        raise RuntimeError(
            "Google Docs: profilo non autenticato. Esegui prima "
            "google_doc_staging.ensure_google_session()."
        )

    try:
        titolo_box = page.locator("input.docs-title-input").first
        titolo_box.click(timeout=5000)
        titolo_box.fill(f"{titolo_libro} — bozza")
        page.keyboard.press("Enter")
    except Exception as exc:
        print(f"[google_doc_staging] impossibile rinominare il documento "
              f"(non bloccante, resta 'Documento senza titolo'): {exc}")

    doc_url = page.url
    return GoogleDocSession(context=context, page=page, doc_url=doc_url)


def append_chapter(session: GoogleDocSession, numero: int, titolo_capitolo: str,
                   corpo: str) -> bool:
    """Appende un capitolo in coda al documento, via clipboard (incolla, non digita
    carattere per carattere — piu' veloce e affidabile su migliaia di parole).

    MAI solleva eccezioni verso il chiamante (decisione esplicita di Gael, Fase 3): un
    fallimento qui non deve mai bloccare la scrittura, che ha gia' un canale affidabile
    (il file su disco in `BookProject`). Ritorna True/False e logga soltanto."""
    try:
        page = session.page
        testo_capitolo = f"Chapter {numero}: {titolo_capitolo}\n\n{corpo}\n\n"
        page.evaluate("(t) => navigator.clipboard.writeText(t)", testo_capitolo)
        page.click("body", timeout=5000)
        page.keyboard.press("Control+End")
        page.keyboard.press("Enter")
        page.keyboard.press("Control+V")
        page.wait_for_timeout(800)
        return True
    except Exception as exc:
        print(f"[google_doc_staging] append_chapter fallito per il capitolo {numero} "
              f"(non bloccante, il capitolo e' comunque salvo su disco): {exc}")
        return False


def close(session: GoogleDocSession) -> None:
    try:
        session.context.close()
    except Exception:
        pass
