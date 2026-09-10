#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
youtube_studio_reader.py — il lettore che chiude TRE buchi verificati sul codice della fabbrica:

  1. `03-AGENTI-E-RUOLI/operatori/channel-performance-analyst.md` dichiara che CTR, retention e
     ricavi "richiedono YouTube Studio, che e' privato" e scrive sempre `null` in
     memory/performance_logs.json, leggendo solo dati pubblici via scraping
     (youtube_hunter_playwright.py). Il canale pero' e' NOSTRO.
  2. `self_improve.py` e `meta_agent.py` (il motore che dovrebbe far migliorare la fabbrica)
     ragionano su dati ciechi: senza CTR/retention/ricavi reali non hanno materiale.
  3. `scripts/tesoreria.py` ha gia' "youtube" fra i MOTORI validi (riga ~57) e zero euro
     YouTube mai registrati: nessuno ha mai letto quanto guadagna il canale.

Il login Playwright persistente per entrare in Studio esiste gia' e funziona:
`youtube_uploader_playwright.py` lo usa a ogni upload. Qui si riusa lo STESSO profilo
(`chrome-profile-youtube/`), ma SOLO per leggere. Questo file non scrive mai nulla su
YouTube: nessun click su un controllo che cambia lo stato del canale o di un video.

QUESTO FILE NON TOCCA NESSUN FILE ESISTENTE. Non `youtube_uploader_playwright.py`, non
`channel-performance-analyst.md`, non `scripts/tesoreria.py`, non `self_improve.py`.
L'aggancio a quei file e' una decisione del gate che arriva dopo (stessa logica di
youtube_analytics_client.py, riga 15-18: "NON E' ANCORA AGGANCIATO"). Questo script prepara
pero' un blocco "entrate_pronte_per_tesoreria" gia' nella forma esatta che
`scripts/tesoreria.py entrata --importo ... --da ... --per youtube --stato ...` si aspetta,
cosi' l'aggancio quando arriva non richiede traduzioni.

------------------------------------------------------------------------------------------
SELETTORI RIUSATI (verificati dal vivo altrove in questo repository — fonte citata):
------------------------------------------------------------------------------------------
  - USER_AGENT esplicito: senza, Studio mostra un interstiziale "browser non supportato" al
    posto della dashboard reale. Verificato dal vivo in youtube_uploader_playwright.py
    (righe 276-281) e in pubblica_video.py (righe 77-80).
  - `channel="chrome"` (Chrome vero, non il Chromium bundled) + profilo persistente +
    `--disable-blink-features=AutomationControlled`: stessa configurazione di
    youtube_uploader_playwright.py (righe 283-298) e pubblica_video.py
    (avvia_playwright_e_pubblica, righe 395-403). Motivo: fingerprint riconosciuto da Google,
    verificato dal vivo il 2026-09-03.
  - Verifica di login fallito ("login" in page.url o input[type='email'] visibile):
    youtube_uploader_playwright.py, riga 306.
  - Ricavare il channel id risalendo l'URL dopo "/channel/" e navigare a un path sotto quel
    id: stessa tecnica di `_id_dalla_lista_contenuti()` in youtube_uploader_playwright.py
    (righe 172-222), verificata dal vivo il 2026-09-04.
  - Il TESTO REALE della schermata "Channel analytics" (Overview) e' stato catturato dal vivo
    il 2026-09-03 e salvato in `memory/_report_analytics_overview.txt` (esiste gia' nel
    repository, non toccato da questo file). Contiene, verbatim: le tab "Overview / Content /
    Audience / Revenue / Trends", le etichette "Views", "Watch time (hours)", "Subscribers",
    "Estimated revenue" con relativo valore "€31.72", il selettore di periodo
    "Aug 6 – Sep 2, 2026" / "Last 28 days", la tabella "Your top content in this period" con
    colonne Content / Average view duration / Views (dove la durata media porta con se' fra
    parentesi la percentuale media vista, es. "9:22 (37.1%)"), e il riquadro "Latest content"
    con "Views", "Thumbnail click-through rate" (es. "6.7%") e "Average view duration"
    (es. "6:33"). Le funzioni di estrazione qui sotto che leggono queste etichette sono
    costruite SU QUEL TESTO REALE, non indovinate — ma NON e' garantito che l'URL con cui ci
    si arriva dal vivo sia identico (Studio puo' avere versioni diverse per account diversi).
  - Il TESTO REALE della schermata "Video details" (tab Details di un video) e' catturato in
    `memory/_report_video_body_text.txt` (2026-09-03): conferma che la barra dei tab di un
    video include "Details | Analytics | Editor | Comments | Languages | Earn | Claims |
    Clips and Shorts | Settings" — cioe' che un tab "Analytics" per-video esiste davvero.
  - `/video/<id>/monetization` come URL raggiungibile per un video: verificato dal vivo in
    `_earn_tab2.py` (esperimento usa-e-getta gia' nel repository).
  - `/channel/<cid>/monetization/onbehalf/uploaddefaults` come URL raggiungibile per le
    impostazioni di monetizzazione: verificato dal vivo in `_check_monetization_settings.py`.

------------------------------------------------------------------------------------------
SELETTORI/URL DEDOTTI — IPOTESI, mai visti dal vivo in questo repository, da calibrare:
------------------------------------------------------------------------------------------
  - Il path esatto `/video/<id>/analytics/tab-overview/period-default` e
    `/channel/<cid>/analytics/tab-overview/period-default`: dedotti dalla convenzione nota
    di Studio (tab-<nome>/period-<intervallo>) usata altrove su YouTube, MAI catturati dal
    vivo in questo repo. Se il redirect non produce la pagina attesa, si ripiega sul path
    semplice `/analytics` (senza suffisso), che e' quello effettivamente raggiunto quando si
    clicca "Analytics" nel menu laterale.
  - L'etichetta esatta del CTR sulla scheda Analytics DI UN SINGOLO VIDEO (non quella del
    riquadro "Latest content" del canale, quella e' verificata): si prova prima
    "Impressions click-through rate" (nome ufficiale della metrica lato Google), poi
    "Thumbnail click-through rate" (l'unica vista dal vivo, ma su un altro widget), poi "CTR".
  - Le etichette per periodi diversi da "Last 28 days" (es. "Last 90 days", "Lifetime"): solo
    "Last 28 days" e' stato visto dal vivo nella cattura reale. Le altre sono i nomi standard
    noti dei preset di Studio, non verificati in QUESTO account.
  - La retention curve (grafico) e il punto preciso ai 30 secondi: il grafico e' un SVG, non
    testo — un dump DOM/testo puro difficilmente contiene un valore numerico leggibile per un
    punto preciso della curva. Questo file prova comunque una ricerca testuale di riepilogo
    ("Average percentage viewed"), MAI vista dal vivo su questa schermata in questo repo; se
    non la trova (probabile), scrive `null` con il motivo — e indica che l'alternativa GIA'
    pronta e verificata e' `youtube_analytics_client.py` (YouTube Analytics API via OAuth,
    legge `audienceWatchRatio` in modo esatto, non uno scraping di un grafico).

------------------------------------------------------------------------------------------
ONESTA' — `null` e' la risposta giusta quando manca il dato
------------------------------------------------------------------------------------------
Ogni campo che non si riesce a leggere diventa `{"valore": null, "motivo": "..."}`. Non si
stima mai un numero plausibile: un numero inventato in Analytics avvelena ogni decisione
presa dopo (stessa regola gia' scritta in channel-performance-analyst.md riga 36-39).

Uso da riga di comando:
  python youtube_studio_reader.py --video-id JOUWaLkyoN8 --video-id 6hrhlS9jC4g
  python youtube_studio_reader.py --solo-canale
  python youtube_studio_reader.py --video-id JOUWaLkyoN8 --periodo "Last 90 days"

Console Windows cp1252: NIENTE EMOJI nell'output, o crasha (stessa regola di pubblica_video.py).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
        sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DEFAULT_PROFILE = os.path.join(FACTORY_DIR, "chrome-profile-youtube")
DEFAULT_OUTPUT_DIR = os.path.join(FACTORY_DIR, "memory", "studio_reports")
DEFAULT_DIAGNOSTICA_DIR = os.path.join(FACTORY_DIR, "memory")

# Stesso User-Agent di youtube_uploader_playwright.py e pubblica_video.py — vedi commento
# in cima al file, sezione "SELETTORI RIUSATI".
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

# Stessa regola di pubblica_video.py::ID_VIDEO_RE (riga 84): 11 caratteri e' lo standard, un
# range piu' largo per non rompersi su varianti future.
ID_VIDEO_RE = re.compile(r"^[\w-]{6,32}$")

# Unico periodo preset VERIFICATO dal vivo nella cattura reale (memory/_report_analytics_
# overview.txt, riga 32). Gli altri sono i nomi standard noti dei preset di Studio: IPOTESI.
ETICHETTE_PERIODO_NOTE = (
    "Last 7 days", "Last 28 days", "Last 90 days", "Last 365 days",
    "Lifetime", "This year", "Last calendar year",
)


class ErroreValidazione(Exception):
    """Argomenti insufficienti/incoerenti: si ferma PRIMA di aprire un browser."""


# ============================================================================================
# PARSING NUMERI — funzioni pure, nessuna dipendenza da Playwright o dalla rete.
# Costruite sulle forme viste DAL VIVO nella cattura reale (memory/_report_analytics_
# overview.txt): "13,2K" (virgola decimale + suffisso K), "2.344" (punto delle migliaia),
# "€31.72" (valuta, punto decimale — coerenza mista del widget, e' un fatto reale della
# pagina, non un errore di questo file), "37.1%" / "4,5%" (percentuale, decimale libero),
# "1,2 mila" (virgola decimale + suffisso parola intera), "6:33" (durata mm:ss).
# ============================================================================================

_MOLTIPLICATORI = (
    (re.compile(r"(mila|k)\s*$", re.IGNORECASE), 1_000.0),
    (re.compile(r"(mln|milioni|mio)\s*$", re.IGNORECASE), 1_000_000.0),
    (re.compile(r"(mld|miliardi)\s*$", re.IGNORECASE), 1_000_000_000.0),
)


def _pulisci_spazi(testo):
    return testo.replace(" ", " ").strip()


def parse_numero(testo):
    """Converte una stringa numerica (italiana o mista, con o senza suffisso/valuta/%) in
    float. Ritorna None se non c'e' nessuna cifra utilizzabile — MAI un numero indovinato.

    Casi coperti (verificati contro il testo reale catturato in Studio, vedi commento sopra):
      "13,2K"    -> 13200.0   (virgola = decimale, K = mille)
      "1,2 mila" -> 1200.0    (virgola = decimale, "mila" = mille)
      "2.344"    -> 2344.0    (punto seguito da esattamente 3 cifre = separatore migliaia)
      "31.72"    -> 31.72     (punto seguito da 1-2 cifre = decimale)
      "€31.72"   -> 31.72     (simbolo valuta ignorato)
      "37.1%"    -> 37.1      (percentuale, simbolo ignorato)
      "4,5%"     -> 4.5
      "-6,3K"    -> -6300.0   (segno preservato)
    """
    if testo is None:
        return None
    t = _pulisci_spazi(str(testo))
    if not t:
        return None
    t = t.replace("€", "").replace("$", "").replace("%", "").strip()
    if not t:
        return None

    moltiplicatore = 1.0
    for regex, fattore in _MOLTIPLICATORI:
        m = regex.search(t)
        if m:
            moltiplicatore = fattore
            t = t[:m.start()].strip()
            break

    m = re.search(r"[+-]?[\d.,\s ]+", t)
    if not m:
        return None
    numero = m.group(0).replace(" ", "").replace(" ", "")
    if not numero or not re.search(r"\d", numero):
        return None

    segno = -1.0 if numero.startswith("-") else 1.0
    numero = numero.lstrip("+-")

    if "," in numero and "." in numero:
        # entrambi presenti: l'ultimo che compare e' il decimale, l'altro sono le migliaia.
        if numero.rfind(",") > numero.rfind("."):
            numero = numero.replace(".", "").replace(",", ".")
        else:
            numero = numero.replace(",", "")
    elif "," in numero:
        # una sola virgola: convenzione italiana, e' sempre decimale.
        numero = numero.replace(",", ".")
    elif "." in numero:
        parti = numero.split(".")
        if len(parti) >= 2 and len(parti[-1]) == 3:
            # punto come separatore delle migliaia ("2.344" -> 2344): esattamente 3 cifre
            # dopo l'ultimo punto e' l'unico segnale disponibile per distinguerlo da un
            # decimale ("31.72" ne ha 2). Euristica verificata sui due casi reali catturati.
            numero = "".join(parti)
        # altrimenti resta decimale ("31.72" -> 31.72, "9.5" -> 9.5)

    try:
        valore = float(numero)
    except ValueError:
        return None
    return segno * moltiplicatore * valore


def parse_percentuale(testo):
    """Come parse_numero, ma richiede che il simbolo '%' sia presente — altrimenti chi chiama
    stava leggendo la cosa sbagliata, meglio None che un numero silenziosamente non-percento."""
    if testo is None or "%" not in str(testo):
        return None
    return parse_numero(testo)


def parse_durata_hhmmss(testo):
    """'6:33' -> 393 (secondi). '1:02:03' -> 3723. None se il formato non torna."""
    if testo is None:
        return None
    t = _pulisci_spazi(str(testo))
    m = re.fullmatch(r"(\d+):(\d{2})(?::(\d{2}))?", t)
    if not m:
        return None
    if m.group(3) is not None:
        ore, minuti, secondi = int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        ore, minuti, secondi = 0, int(m.group(1)), int(m.group(2))
    return ore * 3600 + minuti * 60 + secondi


def _rileva_valuta(testo):
    if testo is None:
        return None
    t = str(testo)
    if "€" in t:
        return "EUR"
    if "$" in t:
        return "USD"
    if "£" in t:
        return "GBP"
    return None


def campo(valore, motivo_se_mancante=None, grezzo=None):
    """Involucro uniforme per ogni dato letto: {"valore": ..., "motivo": ..., "grezzo": ...}.
    Se valore e' None, motivo NON puo' essere vuoto — un null senza spiegazione e' inutile
    quanto un numero inventato."""
    if valore is None:
        return {"valore": None,
                "motivo": motivo_se_mancante or "dato non trovato nella pagina",
                "grezzo": grezzo}
    return {"valore": valore, "motivo": None, "grezzo": grezzo}


# ============================================================================================
# ESTRAZIONE DA TESTO — funzioni pure che operano su una stringa (il testo della pagina),
# mai su un oggetto Playwright. Cosi' sono testabili senza rete e senza browser.
# ============================================================================================

def valida_video_id(video_id):
    if video_id is None or not str(video_id).strip():
        raise ErroreValidazione("Nessun --video-id valido: serve l'id esatto del video.")
    video_id = str(video_id).strip()
    if not ID_VIDEO_RE.match(video_id):
        raise ErroreValidazione(
            "--video-id %r non sembra un id YouTube valido (atteso solo lettere/cifre/'-'/'_', "
            "6-32 caratteri, senza spazi ne' URL)." % video_id
        )
    return video_id


def _righe(testo):
    return [r.strip() for r in (testo or "").splitlines()]


def _estrai_dopo_etichetta(testo, etichetta, salta_righe_vuote_max=3):
    """Cerca `etichetta` come riga ESATTA e ritorna la prima riga non vuota successiva.
    Pattern verificato sul dump reale memory/_report_analytics_overview.txt: Studio (Polymer)
    rende ogni "blocco" visivo come righe separate nel testo estratto via inner_text, ed
    etichetta e valore stanno su righe consecutive (es. "Estimated revenue" poi "€31.72")."""
    righe = _righe(testo)
    for i, r in enumerate(righe):
        if r == etichetta:
            for j in range(i + 1, min(i + 1 + salta_righe_vuote_max, len(righe))):
                if righe[j]:
                    return righe[j]
    return None


def _blocco_tra(testo, marcatore_inizio, marcatore_fine=None, da_indice=0):
    i = testo.find(marcatore_inizio, da_indice)
    if i < 0:
        return None
    j = testo.find(marcatore_fine, i) if marcatore_fine else -1
    return testo[i: j if j > 0 else None]


def rileva_periodo_effettivo(testo):
    """Legge davvero quale periodo e' selezionato invece di assumere che il click richiesto
    abbia funzionato — stessa filosofia di leggi_stato_visibilita() in pubblica_video.py
    (riga 192-200): si legge lo stato vero dalla pagina, non si dichiara quello desiderato."""
    for etichetta in ETICHETTE_PERIODO_NOTE:
        if etichetta in (testo or ""):
            return etichetta
    return None


def estrai_tiles_overview_canale(testo):
    """Legge il blocco dei riquadri di riepilogo della schermata 'Channel analytics' ->
    Overview: Views, Watch time (hours), Subscribers, Estimated revenue.

    Etichette e struttura VERIFICATE sul dump reale (memory/_report_analytics_overview.txt,
    righe 36-53). Attenzione alla trappola: la parola "Views" compare TRE volte prima del
    valore (intestazione del grafico + nome del riquadro), quindi qui si cerca il pattern
    "Views\\nViews\\n<valore>" invece del generico "prima riga dopo l'etichetta" (che
    prenderebbe la seconda "Views" invece del numero)."""
    blocco = _blocco_tra(testo, "Estimated revenue")
    # Il blocco delle tile parte prima di "Estimated revenue": recupera un contesto piu' ampio
    # includendo cio' che precede, fino a "Your top content" come limite superiore assente qui
    # (usiamo l'intero testo per la ricerca di Views/Watch time, che possono precedere).
    testo_ricerca = testo or ""

    m_views = re.search(r"Views\s*\n\s*Views\s*\n\s*([^\n]+)", testo_ricerca)
    views_raw = m_views.group(1).strip() if m_views else None

    watch_time_raw = _estrai_dopo_etichetta(testo_ricerca, "Watch time (hours)")
    subscribers_raw = _estrai_dopo_etichetta(testo_ricerca, "Subscribers")
    revenue_raw = _estrai_dopo_etichetta(testo_ricerca, "Estimated revenue")
    periodo = rileva_periodo_effettivo(testo_ricerca)

    return {
        "periodo_effettivo": periodo,
        "views": campo(parse_numero(views_raw), None if views_raw else
                       "etichetta 'Views' (tile riepilogo) non trovata nella pagina", views_raw),
        "watch_time_ore": campo(parse_numero(watch_time_raw), None if watch_time_raw else
                                 "etichetta 'Watch time (hours)' non trovata", watch_time_raw),
        "iscritti_variazione": campo(parse_numero(subscribers_raw), None if subscribers_raw else
                                      "etichetta 'Subscribers' (tile riepilogo) non trovata",
                                      subscribers_raw),
        "entrate_stimate": campo(parse_numero(revenue_raw), None if revenue_raw else
                                  "etichetta 'Estimated revenue' non trovata — probabile "
                                  "canale non monetizzato o schermata diversa da quella attesa",
                                  revenue_raw),
        "entrate_valuta": _rileva_valuta(revenue_raw) or "EUR",
    }


def estrai_top_content_canale(testo):
    """Estrae la tabella 'Your top content in this period' della Overview del canale.

    Pattern VERIFICATO dal vivo in memory/_report_analytics_overview.txt (righe 67-133,
    catturato 2026-09-03): ogni riga della tabella e', in sequenza — rank / titolo / data di
    pubblicazione / [eventuale riga extra "Recent upload"] / durata "mm:ss" / percentuale fra
    parentesi "(NN.N%)" (retention media di quel video) / views. Questa e' l'UNICA fonte
    testuale verificata che dia CTR-adiacenti/retention-adiacenti per piu' video insieme senza
    aprire la scheda Analytics di ciascuno."""
    blocco = _blocco_tra(testo, "Your top content in this period", "See more")
    if blocco is None:
        return []

    righe = [r for r in _righe(blocco) if r]
    # salta l'intestazione: "Your top content in this period", "Content", "Average view
    # duration", "Views" — ci si ferma dopo l'ultima etichetta nota "Views".
    i = 0
    while i < len(righe) and righe[i] != "Views":
        i += 1
    i += 1  # salta la riga "Views" di intestazione

    risultati = []
    while i < len(righe):
        if not re.fullmatch(r"\d+", righe[i]):
            break  # non e' un rank: la tabella e' finita (es. e' iniziata un'altra sezione)
        rank = int(righe[i]); i += 1
        if i >= len(righe):
            break
        titolo = righe[i]; i += 1
        if i >= len(righe):
            break
        data_pubblicazione = righe[i]; i += 1
        if i < len(righe) and righe[i] == "Recent upload":
            i += 1  # marcatore extra, visto dal vivo su upload recenti — non e' un dato
        if i >= len(righe):
            break
        durata_raw = righe[i]; i += 1
        if i >= len(righe):
            break
        m_percento = re.fullmatch(r"\(([\d.,]+)%\)", righe[i])
        if not m_percento:
            break  # la forma attesa non torna: meglio fermarsi che disallineare le righe dopo
        retention_raw = m_percento.group(1); i += 1
        if i >= len(righe):
            break
        views_raw = righe[i]; i += 1

        risultati.append({
            "rank": rank,
            "titolo": titolo,
            "data_pubblicazione": data_pubblicazione,
            "durata_video_secondi": campo(parse_durata_hhmmss(durata_raw), grezzo=durata_raw),
            "retention_media_percento": campo(parse_numero(retention_raw), grezzo=retention_raw + "%"),
            "views": campo(parse_numero(views_raw), grezzo=views_raw),
        })
    return risultati


def estrai_ultimo_video_realtime(testo):
    """Legge il riquadro 'Latest content' della Overview (l'unico punto, verificato dal vivo,
    dove CTR miniatura E durata media vista compaiono insieme per un video, testualmente).
    Vale SOLO per l'ultimo video pubblicato — non e' generalizzabile a un video a scelta.
    Pattern verificato in memory/_report_analytics_overview.txt, righe 152-161."""
    blocco = _blocco_tra(testo, "Latest content", "See video analytics")
    if blocco is None:
        return {
            "titolo": None,
            "views": campo(None, "sezione 'Latest content' non trovata nella pagina"),
            "ctr_miniatura_percento": campo(None, "sezione 'Latest content' non trovata"),
            "durata_media_visualizzazione_secondi": campo(None, "sezione 'Latest content' non trovata"),
        }
    righe = [r for r in _righe(blocco) if r]
    titolo = righe[1] if len(righe) > 1 else None  # righe[0] == "Latest content"

    views_raw = _estrai_dopo_etichetta(blocco, "Views")
    ctr_raw = _estrai_dopo_etichetta(blocco, "Thumbnail click-through rate")
    durata_raw = _estrai_dopo_etichetta(blocco, "Average view duration")

    return {
        "titolo": titolo,
        "views": campo(parse_numero(views_raw), None if views_raw else
                        "etichetta 'Views' non trovata dentro 'Latest content'", views_raw),
        "ctr_miniatura_percento": campo(parse_percentuale(ctr_raw), None if ctr_raw else
                                         "etichetta 'Thumbnail click-through rate' non trovata",
                                         ctr_raw),
        "durata_media_visualizzazione_secondi": campo(
            parse_durata_hhmmss(durata_raw), None if durata_raw else
            "etichetta 'Average view duration' non trovata dentro 'Latest content'", durata_raw),
    }


def estrai_metriche_video_singolo(testo, video_id):
    """Legge la scheda Analytics di UN video specifico (CTR, retention media, punto ai 30s,
    views, durata media). A differenza di estrai_top_content_canale() e
    estrai_ultimo_video_realtime(), qui le etichette NON sono verificate dal vivo su questa
    schermata precisa in questo repository — vedi sezione "IPOTESI" in cima al file.
    Tenta piu' varianti di etichetta per ogni campo, in ordine di plausibilita'."""
    def prova_etichette(etichette):
        for et in etichette:
            v = _estrai_dopo_etichetta(testo, et)
            if v:
                return v, et
        return None, None

    ctr_raw, ctr_etichetta = prova_etichette(
        ("Impressions click-through rate", "Thumbnail click-through rate", "Click-through rate", "CTR"))
    views_raw, _ = prova_etichette(("Views",))
    durata_raw, _ = prova_etichette(("Average view duration",))
    retention_raw, retention_etichetta = prova_etichette(
        ("Average percentage viewed", "Average view percentage"))

    motivo_ctr = (None if ctr_raw else
                  "nessuna delle etichette CTR ipotizzate ('Impressions/Thumbnail "
                  "click-through rate', 'CTR') e' stata trovata nel testo della pagina — "
                  "etichetta reale da calibrare dal vivo su questa schermata")
    motivo_retention = (
        "il grafico di retention e' un SVG, non testo: nessuna etichetta testuale col valore "
        "trovata nel DOM. Alternativa GIA' pronta e verificata: youtube_analytics_client.py "
        "(YouTube Analytics API via OAuth) legge audienceWatchRatio in modo esatto — usa "
        "quello per un numero affidabile invece di questo scraping." if not retention_raw else None)

    return {
        "video_id": video_id,
        "ctr_miniatura_percento": campo(parse_percentuale(ctr_raw), motivo_ctr, ctr_raw),
        "ctr_etichetta_trovata": ctr_etichetta,
        "views": campo(parse_numero(views_raw), None if views_raw else
                        "etichetta 'Views' non trovata sulla scheda Analytics del video",
                        views_raw),
        "durata_media_visualizzazione_secondi": campo(
            parse_durata_hhmmss(durata_raw), None if durata_raw else
            "etichetta 'Average view duration' non trovata sulla scheda Analytics del video",
            durata_raw),
        "retention_media_percento": campo(parse_numero(retention_raw), motivo_retention, retention_raw),
        "retention_30s_percento": campo(
            None,
            "punto preciso della curva ai 30 secondi non estraibile da un dump testuale del "
            "grafico SVG. Usa youtube_analytics_client.py::costruisci_curva_retention() "
            "(A4-RC-15, gia' pronto) che legge audienceWatchRatio per elapsedVideoTimeRatio "
            "dalla YouTube Analytics API e isola il punto piu' vicino a 30s con precisione."
        ),
    }


def costruisci_entrata_tesoreria(entrate_stimate_campo, valuta, periodo_effettivo, canale_nome=None):
    """Prepara UNA entrata nella forma esatta che scripts/tesoreria.py accetta con
    `entrata --importo ... --da ... --per youtube --stato ... --nota ...` (vedi
    scripts/tesoreria.py, funzione registra_entrata(), righe 127-146, e MOTORI/STATI righe
    57-63). Questo script NON chiama mai tesoreria.py e non scrive mai nei suoi file: prepara
    solo il dizionario pronto, cosi' l'aggancio quando arriva non richiede traduzioni.
    Ritorna None se non c'e' un valore reale da proporre — niente entrate finte in tesoreria."""
    valore = entrate_stimate_campo.get("valore") if entrate_stimate_campo else None
    if valore is None:
        return None
    return {
        "importo": round(float(valore), 2),
        "valuta": valuta or "EUR",
        "da": "YouTube Studio" + (" - %s" % canale_nome if canale_nome else ""),
        "per": "youtube",
        "stato": "previsto",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "nota": (
            "Entrate stimate lette da YouTube Studio (periodo: %s) via "
            "youtube_studio_reader.py il %s. Stato 'previsto' perche' e' una stima di Google "
            "(\"Your final amount may change\"), non un incasso confermato: verificare a mano "
            "prima di registrare davvero con 'python scripts/tesoreria.py entrata ...'. "
            "Questo file non scrive mai in tesoreria da solo."
            % (periodo_effettivo or "sconosciuto", datetime.now().strftime("%Y-%m-%d %H:%M"))
        ),
    }


# ============================================================================================
# INTERAZIONE CON LA PAGINA — riceve un oggetto `page` (Playwright reale o un doppio nei
# test), mai importa Playwright a livello di modulo: i test non hanno bisogno che sia
# installato (stessa scelta architetturale di pubblica_video.py, righe 187-190).
# ============================================================================================

def _testo_pagina(page):
    try:
        return page.inner_text("body")
    except Exception:
        try:
            return page.content()
        except Exception:
            return ""


def verifica_login(page):
    """Stessa verifica di youtube_uploader_playwright.py, riga 306."""
    try:
        if "login" in page.url:
            return False
        return not page.locator("input[type='email']").is_visible()
    except Exception:
        return True  # nessun modo di verificare: si prosegue e si lascia fallire piu' avanti


def ricava_channel_id(page):
    """Stessa tecnica di _id_dalla_lista_contenuti() in youtube_uploader_playwright.py
    (righe 172-222): Studio, una volta autenticato, reindirizza sempre a /channel/<CID>/..."""
    try:
        url = page.url
        if "/channel/" not in url:
            page.goto("https://studio.youtube.com", wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(3000)
            url = page.url
        if "/channel/" not in url:
            return None
        return url.split("/channel/")[1].split("/")[0]
    except Exception:
        return None


def _naviga_con_ipotesi(page, url_ipotesi, url_ripiego, attesa_ms=4000):
    """Prova l'URL ipotizzato (tab-overview/period-default); se dopo la navigazione l'URL
    effettivo non contiene '/analytics', ripiega sul path semplice — quello raggiunto
    davvero cliccando 'Analytics' nel menu, meno preciso ma sempre presente."""
    page.goto(url_ipotesi, wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(attesa_ms)
    if "/analytics" not in page.url:
        page.goto(url_ripiego, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(attesa_ms)
    return page.url


def leggi_overview_canale(page, channel_id):
    url_ipotesi = "https://studio.youtube.com/channel/%s/analytics/tab-overview/period-default" % channel_id
    url_ripiego = "https://studio.youtube.com/channel/%s/analytics" % channel_id
    _naviga_con_ipotesi(page, url_ipotesi, url_ripiego)
    testo = _testo_pagina(page)
    dati = estrai_tiles_overview_canale(testo)
    dati["top_content"] = estrai_top_content_canale(testo)
    dati["ultimo_video_realtime"] = estrai_ultimo_video_realtime(testo)
    dati["url_letto"] = page.url
    return dati


def leggi_metriche_video(page, video_id):
    video_id = valida_video_id(video_id)
    url_ipotesi = "https://studio.youtube.com/video/%s/analytics/tab-overview/period-default" % video_id
    url_ripiego = "https://studio.youtube.com/video/%s/analytics" % video_id
    _naviga_con_ipotesi(page, url_ipotesi, url_ripiego)
    testo = _testo_pagina(page)
    dati = estrai_metriche_video_singolo(testo, video_id)
    dati["url_letto"] = page.url
    return dati


def _dump_dom_diagnostico(page, motivo="generico", cartella=DEFAULT_DIAGNOSTICA_DIR):
    """Stessa filosofia di _dump_step_monetization() in youtube_uploader_playwright.py e di
    _dump_dom_diagnostico() in pubblica_video.py: un tentativo a vuoto non deve finire in un
    semplice messaggio d'errore, deve portarsi a casa il DOM vero."""
    try:
        os.makedirs(cartella, exist_ok=True)
        out = os.path.join(cartella, "youtube_studio_reader_dom_%s.html" % motivo)
        with open(out, "w", encoding="utf-8") as f:
            f.write(page.content())
        print("[DIAGNOSTICA] DOM salvato (%s): %s" % (motivo, out))
    except Exception as e:
        print("[DIAGNOSTICA] Impossibile salvare il DOM: %s" % e)


def leggi_tutto(page, video_ids=None, canale_nome=None):
    """Cuore testabile dello script: riceve un `page' (reale o doppio) e un elenco opzionale
    di video_id, e ritorna il report completo. Non importa mai Playwright direttamente."""
    generato_il = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    loggato = verifica_login(page)
    if not loggato:
        return {
            "generato_il": generato_il,
            "errore": "Il profilo Chrome non risulta loggato su Google/YouTube Studio. "
                      "Effettua il login manualmente nel profilo persistente prima di rilanciare.",
            "canale": None,
            "video": [],
            "entrate_pronte_per_tesoreria": [],
        }

    channel_id = ricava_channel_id(page)
    report = {"generato_il": generato_il, "channel_id": channel_id}

    if channel_id is None:
        report["canale"] = None
        report["canale_errore"] = "Channel id non risolto dall'URL: Studio non ha reindirizzato a /channel/<id>/."
    else:
        try:
            report["canale"] = leggi_overview_canale(page, channel_id)
        except Exception as e:
            _dump_dom_diagnostico(page, "overview-canale-fallita")
            report["canale"] = None
            report["canale_errore"] = "Lettura Overview canale fallita: %s" % e

    video_out = []
    for vid in (video_ids or []):
        try:
            video_out.append(leggi_metriche_video(page, vid))
        except ErroreValidazione as e:
            video_out.append({"video_id": vid, "errore": str(e)})
        except Exception as e:
            _dump_dom_diagnostico(page, "video-%s-fallito" % vid)
            video_out.append({"video_id": vid, "errore": "Lettura fallita: %s" % e})
    report["video"] = video_out

    entrata = None
    if report.get("canale"):
        entrata = costruisci_entrata_tesoreria(
            report["canale"].get("entrate_stimate", {}),
            report["canale"].get("entrate_valuta"),
            report["canale"].get("periodo_effettivo"),
            canale_nome,
        )
    report["entrate_pronte_per_tesoreria"] = [entrata] if entrata else []
    if not entrata:
        report["entrate_pronte_per_tesoreria_motivo"] = (
            "Nessuna entrata proposta: 'Estimated revenue' non e' stato letto (canale non "
            "monetizzato, dato non disponibile, o schermata diversa da quella attesa). "
            "Vedi report['canale']['entrate_stimate']['motivo']." if report.get("canale") else
            "Nessuna entrata proposta: lettura del canale fallita, vedi report['canale_errore']."
        )
    return report


# ============================================================================================
# SALVATAGGIO SU DISCO — nome file con data e ora: i rapporti vecchi non si sovrascrivono
# mai, il confronto fra due date e' meta' del valore di questo script.
# ============================================================================================

def salva_report(dati, output_dir=DEFAULT_OUTPUT_DIR, adesso=None):
    adesso = adesso or datetime.now()
    os.makedirs(output_dir, exist_ok=True)
    nome = "youtube_studio_report_%s.json" % adesso.strftime("%Y%m%d-%H%M%S")
    percorso = os.path.join(output_dir, nome)
    with open(percorso, "w", encoding="utf-8", newline="\n") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)
    return percorso


# ============================================================================================
# DRIVER REALE — l'unico punto dove Playwright viene importato ed eseguito davvero.
# ============================================================================================

def avvia_playwright_e_leggi(video_ids, profile_dir=DEFAULT_PROFILE, canale_nome=None):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[ERRORE] Libreria 'playwright' non installata. "
              "Installa con: pip install playwright && playwright install")
        return {"errore": "playwright_non_installato"}

    if not profile_dir or not os.path.isdir(profile_dir):
        print("[ERRORE] Profilo Chrome '%s' non trovato. Serve lo stesso profilo persistente "
              "gia' autenticato usato da youtube_uploader_playwright.py." % profile_dir)
        return {"errore": "profilo_non_trovato"}

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
            print("Navigazione su YouTube Studio...")
            page.goto("https://studio.youtube.com", wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(5000)
            risultato = leggi_tutto(page, video_ids, canale_nome)
        except Exception as ex:
            print("[ERRORE] Interazione con il browser fallita: %s" % ex)
            try:
                _dump_dom_diagnostico(page, "errore-non-gestito")
            except Exception:
                pass
            risultato = {"errore": str(ex), "generato_il": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        finally:
            browser_context.close()
        return risultato


# ============================================================================================
# CLI
# ============================================================================================

def main():
    ap = argparse.ArgumentParser(
        description="Legge YouTube Studio (analytics per-video ed entrate canale) col profilo "
                     "Chrome persistente gia' autenticato. Non scrive MAI nulla su YouTube.")
    ap.add_argument("--video-id", action="append", default=[],
                     help="Id video da leggere (ripetibile: --video-id X --video-id Y).")
    ap.add_argument("--solo-canale", action="store_true",
                     help="Legge solo l'overview e le entrate del canale, nessun video.")
    ap.add_argument("--canale-nome", default=None,
                     help="Nome del canale, solo per etichettare l'entrata pronta per tesoreria.")
    ap.add_argument("--profile", default=DEFAULT_PROFILE,
                     help="Cartella del profilo Chrome persistente gia' loggato su Studio.")
    ap.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR,
                     help="Cartella dove salvare il report JSON (nome con data/ora, mai sovrascritto).")
    args = ap.parse_args()

    video_ids = [] if args.solo_canale else args.video_id
    for vid in video_ids:
        try:
            valida_video_id(vid)
        except ErroreValidazione as e:
            print("[ERRORE] %s" % e)
            return 1

    print("=" * 78)
    print("YOUTUBE STUDIO READER -- lettura, mai scrittura")
    print("Video da leggere : %s" % (", ".join(video_ids) if video_ids else "nessuno (solo canale)"))
    print("Profilo          : %s" % args.profile)
    print("=" * 78)

    risultato = avvia_playwright_e_leggi(video_ids, args.profile, args.canale_nome)
    percorso = salva_report(risultato, args.output_dir)
    print("[OK] Report salvato: %s" % percorso)

    if risultato.get("errore"):
        print("[FALLITO] %s" % risultato["errore"])
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
