#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pubblica_video.py — il secondo tempo della pubblicazione (A6, colma il buco dietro ADR-016).

`youtube_uploader_playwright.py` carica ogni video su YouTube SEMPRE in Privato — e' giusto,
e' policy voluta: approva Max prima che qualcosa esca. Ma dopo quell'approvazione non esisteva
NIENTE: nessuno script portava un video da Privato a Pubblico. apex7_orchestrator.py lo dice
testualmente (riga ~1546): "SEMPRE privata (visibilita' PRIVATE hardcoded in
youtube_uploader_playwright.py, non parametro)". Questo file e' il pezzo mancante.

QUESTO FILE NON TOCCA youtube_uploader_playwright.py. Quello resta l'unico modo per caricare,
resta sempre Privato, resta collaudato cosi' com'e'. pubblica_video.py agisce SOLO su un video
gia' presente su YouTube (in Privato), dato il suo id, e lo porta a Pubblico o lo programma.

Selettori riusati (non reinventati) da esperimenti gia' fatti dal vivo su questa UI:
  - `tp-yt-paper-radio-button[name='PRIVATE']` — verificato dal vivo in
    youtube_uploader_playwright.py e in _confirm_private.py / _details_page_visibility.py.
    Il nome 'PUBLIC' qui sotto segue la STESSA convenzione di enum (stesso attributo `name`
    sullo stesso componente Polymer), ma non e' mai stato cliccato dal vivo in questo
    repository: la prima esecuzione reale (anche in --prova, che arriva fino alla schermata
    e legge lo stato senza cliccare) e' la vera verifica.
  - Il click sul testo dello stato corrente ("Private"/"Pending"/...) per aprire il popup di
    visibilita' — pattern verificato in _confirm_private.py (click su "Pending").
  - Pulsanti "Done"/"Save" per confermare — stesso pattern usato in
    youtube_uploader_playwright.py e in _details_page_visibility.py.
  - Dump del DOM su fallimento — stessa tecnica di _dump_step_monetization() in
    youtube_uploader_playwright.py: un tentativo a vuoto su un'azione irreversibile non deve
    finire in un semplice "non ha funzionato", deve portarsi a casa il DOM vero.

TRE REGOLE NON NEGOZIABILI (di sicurezza, non di stile):

1. Nessuna pubblicazione senza un ordine esplicito. Questo script non pubblica mai "tutto
   quello che trova": vuole --video-id, uno alla volta, passato a mano. Niente liste, niente
   cartelle, niente "tutti i video privati". Un errore qui non e' un bug: e' un video che esce
   nel mondo quando non doveva.
2. --prova (dry-run) e' il comportamento di default. Senza --conferma esplicito, lo script
   arriva fino alla schermata Visibilita', LEGGE lo stato attuale, dice cosa farebbe — e non
   clicca niente. Pubblicare e' irreversibile: un video pubblico anche per un minuto puo'
   essere visto, indicizzato, scaricato.
3. Ogni esecuzione scrive nel log (memory/pubblicazioni.log), in append: data, id, modalita',
   stato prima, stato dopo. Anche le prove. Un'azione irreversibile senza traccia e' la
   combinazione peggiore possibile.

Uso:
    python pubblica_video.py --video-id RUg6TgSd79s --pubblica
        (PROVA: arriva alla schermata Visibilita', legge lo stato, non clicca — e' il default)

    python pubblica_video.py --video-id RUg6TgSd79s --pubblica --conferma
        (REALE: rende il video pubblico adesso. IRREVERSIBILE.)

    python pubblica_video.py --video-id RUg6TgSd79s --programma "2026-09-20 09:00" --conferma
        (REALE: programma la pubblicazione futura. Selettori data/ora NON verificati dal vivo
        in questo repository — vedi avviso a runtime e sezione finale del report di consegna.)

Console Windows cp1252: NIENTE EMOJI nell'output, o crasha.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DEFAULT_PROFILE = os.path.join(FACTORY_DIR, "chrome-profile-youtube")
DEFAULT_LOG = os.path.join(FACTORY_DIR, "memory", "pubblicazioni.log")

# Stesso User-Agent di youtube_uploader_playwright.py: senza, Studio mostra un interstiziale
# "browser non supportato" al posto della dashboard reale (bug gia' documentato e risolto li').
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

# Id YouTube: 11 caratteri e' lo standard, ma accettiamo un range un po' piu' largo per non
# rompersi su varianti future — l'importante e' che non sia vuoto e non contenga spazi/slash.
ID_VIDEO_RE = re.compile(r"^[\w-]{6,32}$")

# Mappa testo-stato mostrato da Studio -> parola italiana usata nel log e in video_prodotti.json
# (stessa convenzione gia' in uso: vedi memory/video_prodotti.json, campo "visibilita").
STATI_VISIBILITA = (
    ("Private", "privato"), ("Privato", "privato"),
    ("Public", "pubblico"), ("Pubblico", "pubblico"),
    ("Unlisted", "non in elenco"), ("Non in elenco", "non in elenco"),
    ("Scheduled", "programmato"), ("Programmato", "programmato"),
    ("Pending", "in elaborazione"), ("In attesa", "in elaborazione"),
)


class ErroreValidazione(Exception):
    """Sollevato quando gli argomenti passati non sono sufficienti/coerenti per procedere.
    Ferma tutto PRIMA di aprire un browser — non e' un errore di rete, e' un rifiuto a monte."""


# ---------------------------------------------------------------------------------------
# Validazione — funzioni pure, nessuna dipendenza da Playwright o dalla rete.
# ---------------------------------------------------------------------------------------

def valida_video_id(video_id):
    """Regola 1: nessuna pubblicazione senza un id esplicito e valido, uno alla volta."""
    if video_id is None or not str(video_id).strip():
        raise ErroreValidazione(
            "Nessun --video-id valido passato: serve l'id esatto del video, uno alla volta. "
            "Ferma tutto: non si indovina e non si pubblica 'tutto quello che si trova'."
        )
    video_id = str(video_id).strip()
    if not ID_VIDEO_RE.match(video_id):
        raise ErroreValidazione(
            "--video-id %r non sembra un id YouTube valido (atteso: solo lettere/cifre/'-'/'_', "
            "6-32 caratteri, senza spazi ne' URL). Passa l'id nudo, non il link intero." % video_id
        )
    return video_id


def valida_quando(quando_str):
    """Parsa la data/ora di programmazione, se richiesta. Formato 'YYYY-MM-DD HH:MM'."""
    if not quando_str:
        return None
    testo = quando_str.strip()
    try:
        dt = datetime.strptime(testo, "%Y-%m-%d %H:%M")
    except ValueError as e:
        raise ErroreValidazione(
            "--programma %r non e' nel formato 'YYYY-MM-DD HH:MM' (es. '2026-09-20 09:00'): %s"
            % (quando_str, e)
        )
    if dt <= datetime.now():
        raise ErroreValidazione(
            "--programma %r e' nel passato (o adesso): una programmazione deve stare nel "
            "futuro, altrimenti e' una pubblicazione immediata mascherata — usa --pubblica."
            % quando_str
        )
    return dt


def valida_argomenti(args):
    """Trasforma gli argomenti grezzi in un piano d'azione validato. Solleva ErroreValidazione
    su qualunque incoerenza, PRIMA che un browser venga anche solo aperto."""
    video_id = valida_video_id(args.video_id)
    quando = valida_quando(args.programma) if getattr(args, "programma", None) else None

    if getattr(args, "prova", False) and getattr(args, "conferma", False):
        raise ErroreValidazione(
            "--prova e --conferma sono in contraddizione: --prova dichiara esplicitamente "
            "che non si vuole cliccare, --conferma chiede di farlo davvero. Scegline uno."
        )

    # Regola 2: SENZA --conferma esplicito, si resta sempre in prova. --prova da solo non fa
    # nulla di diverso dal default: esiste solo per rendere l'intenzione esplicita nei comandi
    # e nei log dei run (utile quando questo script viene invocato da un altro script).
    esegue_davvero = bool(getattr(args, "conferma", False)) and not getattr(args, "prova", False)

    modalita = "programma" if quando is not None else "pubblica"

    return {
        "video_id": video_id,
        "modalita": modalita,
        "quando": quando,
        "esegue_davvero": esegue_davvero,
    }


# ---------------------------------------------------------------------------------------
# Log — Regola 3: ogni azione (anche di prova) lascia traccia.
# ---------------------------------------------------------------------------------------

def scrivi_log(video_id, stato_prima, stato_dopo, modalita, dettaglio="", log_path=DEFAULT_LOG):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    riga = "%s | id=%s | modalita=%s | prima=%s | dopo=%s | %s\n" % (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        video_id, modalita, stato_prima, stato_dopo, dettaglio.replace("\n", " "),
    )
    # newline="\n" esplicito: stessa regola gia' in uso in scripts/ultimo_metro.py per non
    # rompere le fusioni con CRLF su Windows dentro file che due sessioni possono toccare.
    with open(log_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(riga)
    return riga


# ---------------------------------------------------------------------------------------
# Interazione con la pagina Studio — riceve un oggetto `page` (reale o un doppio nei test),
# mai importa Playwright a livello di modulo: cosi' i test non hanno bisogno che sia installato.
# ---------------------------------------------------------------------------------------

def leggi_stato_visibilita(page):
    """Legge lo stato attuale mostrato da Studio SENZA cliccare niente."""
    for etichetta, stato in STATI_VISIBILITA:
        try:
            if page.get_by_text(etichetta, exact=True).count() > 0:
                return stato
        except Exception:
            continue
    return "sconosciuto"


def _apri_popup_visibilita(page):
    """Clicca sul testo dello stato corrente per aprire il popup di visibilita' — stesso
    pattern verificato dal vivo in _confirm_private.py (li' il testo era 'Pending')."""
    for etichetta, _stato in STATI_VISIBILITA:
        try:
            loc = page.get_by_text(etichetta, exact=True).first
            if loc.count() > 0 and loc.is_visible():
                loc.click(timeout=6000)
                return True
        except Exception:
            continue
    # Ripiego: pattern esplorato in _visibility_dropdown.py sulla cella "Visibility" della lista.
    try:
        loc = page.locator("[class*='visibility'], ytcp-video-visibility-select").first
        if loc.count() > 0:
            loc.click(timeout=6000)
            return True
    except Exception:
        pass
    return False


def _imposta_radio(page, nome_enum):
    """Clicca `tp-yt-paper-radio-button[name='<nome_enum>']`. PRIVATE e' verificato dal vivo
    altrove nel reparto; PUBLIC segue la stessa convenzione di enum ma qui e' inedito."""
    radio = page.locator("tp-yt-paper-radio-button[name='%s']" % nome_enum)
    if radio.count() == 0:
        return False
    if not radio.first.is_visible():
        return False
    radio.first.click(timeout=8000)
    return True


def _clicca_bottone(page, etichette):
    """Prova una lista di etichette (testo esatto, poi bottone con quel testo) finche' una
    non risponde. Stesso doppio tentativo di youtube_uploader_playwright.py (Done/Save)."""
    for etichetta in etichette:
        try:
            loc = page.get_by_text(etichetta, exact=True).first
            if loc.count() > 0 and loc.is_visible():
                loc.click(timeout=6000)
                return etichetta
        except Exception:
            pass
        try:
            loc = page.locator("button:has-text('%s')" % etichetta).first
            if loc.count() > 0 and loc.is_visible():
                loc.click(timeout=8000)
                return etichetta
        except Exception:
            continue
    return None


def _dump_dom_diagnostico(page, motivo="generico"):
    """Stessa filosofia di _dump_step_monetization() in youtube_uploader_playwright.py: un
    tentativo a vuoto su un'azione irreversibile deve portarsi a casa il DOM vero, non solo
    un messaggio d'errore — altrimenti ogni fix richiede un altro giro dal vivo per vederlo."""
    memory_dir = os.path.join(FACTORY_DIR, "memory")
    try:
        os.makedirs(memory_dir, exist_ok=True)
        out = os.path.join(memory_dir, "pubblica_video_dom_%s.html" % motivo)
        with open(out, "w", encoding="utf-8") as f:
            f.write(page.content())
        print("[DIAGNOSTICA] DOM salvato (%s): %s" % (motivo, out))
    except Exception as e:
        print("[DIAGNOSTICA] Impossibile salvare il DOM: %s" % e)


def _imposta_programmato(page, quando_dt):
    """Attiva 'Schedule' e riempie data/ora. NON VERIFICATO DAL VIVO in questo repository —
    nessuno dei file _*.py tocca mai la programmazione, solo Privato/Pubblico. Best-effort con
    dump del DOM se fallisce: onesto invece di far finta che abbia funzionato."""
    if _clicca_bottone(page, ("Schedule", "Programma")) is None:
        _dump_dom_diagnostico(page, "schedule-toggle-non-trovato")
        return False
    page.wait_for_timeout(1000)

    data_ok = False
    ora_ok = False
    try:
        campo_data = page.locator("input[aria-label*='ate'], ytcp-date-picker input").first
        if campo_data.count() > 0:
            campo_data.click(timeout=4000)
            campo_data.fill(quando_dt.strftime("%b %d, %Y"))
            data_ok = True
    except Exception:
        pass
    try:
        campo_ora = page.locator("input[aria-label*='ime'], ytcp-dropdown-trigger input").first
        if campo_ora.count() > 0:
            campo_ora.click(timeout=4000)
            campo_ora.fill(quando_dt.strftime("%I:%M %p"))
            ora_ok = True
    except Exception:
        pass

    if not (data_ok and ora_ok):
        _dump_dom_diagnostico(page, "schedule-campi-data-ora-non-trovati")
        return False
    return True


def esegui_pubblicazione(piano, page, log_path=DEFAULT_LOG):
    """Cuore testabile dello script: riceve un piano gia' validato e un oggetto `page`
    (Playwright reale o un doppio nei test) e decide se cliccare o no. Non importa mai
    Playwright direttamente: chi lo chiama decide da dove viene `page`."""
    video_id = piano["video_id"]
    modalita = piano["modalita"]

    page.goto("https://studio.youtube.com/video/%s/edit" % video_id,
              wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(4000)
    stato_prima = leggi_stato_visibilita(page)

    intenzione = ("PUBBLICO adesso" if modalita == "pubblica"
                  else "programmato per %s" % piano["quando"].strftime("%Y-%m-%d %H:%M"))

    if not piano["esegue_davvero"]:
        # Regola 2: si arriva fino a qui (schermata letta), MAI oltre. Nessun clic.
        dettaglio = ("PROVA (dry-run): nessun clic eseguito. Stato attuale letto: %s. "
                     "Azione che verrebbe eseguita con --conferma: %s." % (stato_prima, intenzione))
        print("[PROVA] %s" % dettaglio)
        scrivi_log(video_id, stato_prima, stato_prima, "prova", dettaglio, log_path)
        return {"eseguito": False, "stato_prima": stato_prima, "stato_dopo": stato_prima,
                "prova": True}

    # Da qui in poi: esecuzione REALE, irreversibile.
    if not _apri_popup_visibilita(page):
        dettaglio = "Popup Visibilita' non trovato/apribile: nessun clic eseguito, va fatta a mano."
        print("[ERRORE] %s" % dettaglio)
        _dump_dom_diagnostico(page, "popup-non-apribile")
        scrivi_log(video_id, stato_prima, stato_prima, modalita, dettaglio, log_path)
        return {"eseguito": False, "errore": dettaglio,
                "stato_prima": stato_prima, "stato_dopo": stato_prima}
    page.wait_for_timeout(800)

    if modalita == "pubblica":
        impostato = _imposta_radio(page, "PUBLIC")
        motivo_fallimento = "radio PUBLIC non trovata/cliccabile"
    else:
        impostato = _imposta_programmato(page, piano["quando"])
        motivo_fallimento = "campi di programmazione non completati"

    if not impostato:
        dettaglio = "%s: nessun salvataggio eseguito, stato invariato, va fatta a mano." % motivo_fallimento
        print("[ERRORE] %s" % dettaglio)
        _dump_dom_diagnostico(page, "impostazione-fallita-%s" % modalita)
        scrivi_log(video_id, stato_prima, stato_prima, modalita, dettaglio, log_path)
        return {"eseguito": False, "errore": dettaglio,
                "stato_prima": stato_prima, "stato_dopo": stato_prima}

    page.wait_for_timeout(500)
    salvato_con = _clicca_bottone(page, ("Done", "Fine"))
    page.wait_for_timeout(800)
    salvato_con2 = _clicca_bottone(page, ("Save", "Salva", "Publish", "Pubblica"))
    page.wait_for_timeout(1500)

    if not (salvato_con or salvato_con2):
        dettaglio = ("Impostato %s ma nessun bottone Done/Save trovato: il popup potrebbe "
                     "essere rimasto aperto, verificare a mano." % intenzione)
        print("[AVVISO] %s" % dettaglio)
        _dump_dom_diagnostico(page, "salvataggio-non-confermato-%s" % modalita)
        scrivi_log(video_id, stato_prima, "INCERTO", modalita, dettaglio, log_path)
        return {"eseguito": False, "errore": dettaglio,
                "stato_prima": stato_prima, "stato_dopo": "incerto"}

    stato_dopo = leggi_stato_visibilita(page)
    dettaglio = "Azione eseguita: %s." % intenzione
    print("[OK] %s (stato prima: %s, stato dopo: %s)" % (dettaglio, stato_prima, stato_dopo))
    scrivi_log(video_id, stato_prima, stato_dopo, modalita, dettaglio, log_path)
    return {"eseguito": True, "stato_prima": stato_prima, "stato_dopo": stato_dopo}


# ---------------------------------------------------------------------------------------
# Driver reale — l'unico punto dove Playwright viene importato ed eseguito davvero.
# ---------------------------------------------------------------------------------------

def avvia_playwright_e_pubblica(piano, profile_dir, log_path=DEFAULT_LOG):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[ERRORE] Libreria 'playwright' non installata. "
              "Installa con: pip install playwright && playwright install")
        return {"eseguito": False, "errore": "playwright_non_installato"}

    if not profile_dir or not os.path.isdir(profile_dir):
        print("[ERRORE] Profilo Chrome '%s' non trovato. Serve lo stesso profilo persistente "
              "gia' autenticato usato da youtube_uploader_playwright.py." % profile_dir)
        return {"eseguito": False, "errore": "profilo_non_trovato"}

    with sync_playwright() as p:
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            channel="chrome",
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
            viewport={"width": 1440, "height": 900},
            user_agent=USER_AGENT,
        )
        page = browser_context.new_page()
        try:
            risultato = esegui_pubblicazione(piano, page, log_path)
        except Exception as ex:
            print("[ERRORE] Interazione con il browser fallita: %s" % ex)
            try:
                _dump_dom_diagnostico(page, "errore-non-gestito")
            except Exception:
                pass
            scrivi_log(piano["video_id"], "sconosciuto", "ERRORE", piano["modalita"], str(ex), log_path)
            risultato = {"eseguito": False, "errore": str(ex)}
        finally:
            browser_context.close()
        return risultato


# ---------------------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Il secondo tempo della pubblicazione: porta un video gia' caricato in "
                     "Privato a Pubblico, o lo programma. --prova (dry-run) e' il default.")
    ap.add_argument("--video-id", required=True,
                     help="Id YouTube del video (uno solo, passato a mano — mai un elenco).")
    gruppo = ap.add_mutually_exclusive_group(required=True)
    gruppo.add_argument("--pubblica", action="store_true",
                         help="Intenzione: rendi PUBBLICO il video adesso.")
    gruppo.add_argument("--programma", metavar="'YYYY-MM-DD HH:MM'",
                         help="Intenzione: programma la pubblicazione a questa data/ora futura.")
    ap.add_argument("--conferma", action="store_true",
                     help="Esegue davvero il clic (IRREVERSIBILE). Senza questo flag lo script "
                          "e' SEMPRE in modalita' prova, qualunque altra opzione sia passata.")
    ap.add_argument("--prova", action="store_true",
                     help="Rende esplicita la modalita' di prova (e' comunque il default se "
                          "--conferma non e' passato: qui solo per chiarezza nei comandi/log).")
    ap.add_argument("--profile", default=DEFAULT_PROFILE,
                     help="Cartella del profilo Chrome persistente gia' loggato su Studio.")
    ap.add_argument("--log", default=DEFAULT_LOG,
                     help="Percorso del file di log in append (data, id, stato prima/dopo).")
    args = ap.parse_args()

    try:
        piano = valida_argomenti(args)
    except ErroreValidazione as e:
        print("[ERRORE] %s" % e)
        return 1

    modalita_desc = ("PROVA (dry-run, nessun clic)" if not piano["esegue_davvero"]
                      else "REALE (clic effettivo, IRREVERSIBILE)")
    intenzione_desc = ("rendi pubblico adesso" if piano["modalita"] == "pubblica"
                        else "programma per %s" % piano["quando"].strftime("%Y-%m-%d %H:%M"))

    print("=" * 74)
    print("PUBBLICA VIDEO -- il secondo tempo della pubblicazione")
    print("Video ID   : %s" % piano["video_id"])
    print("Intenzione : %s" % intenzione_desc)
    print("Modalita'  : %s" % modalita_desc)
    print("Log        : %s" % args.log)
    print("=" * 74)

    risultato = avvia_playwright_e_pubblica(piano, args.profile, args.log)

    if not risultato.get("eseguito") and risultato.get("errore"):
        print("[FALLITO] %s" % risultato["errore"])
        return 1

    print("[FINE] stato prima: %s -> stato dopo: %s"
          % (risultato.get("stato_prima"), risultato.get("stato_dopo")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
