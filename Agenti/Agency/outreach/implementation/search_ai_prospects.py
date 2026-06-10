"""
WF-F — Ricerca Prospect per Implementazione AI

Trova aziende strutturate (10+ dipendenti) con processi manuali e ripetitivi
che possono essere automatizzati con agenti AI custom. Le fonti principali sono:
1. Ricerca Google per aziende nel settore target
2. Job board (Indeed, InfoJobs) per offerte che segnalano processi manuali
3. Analisi del sito aziendale per segnali di automazione potenziale

Uso:
    python implementation/search_ai_prospects.py --settore "logistica" --citta "Milano"
    python implementation/search_ai_prospects.py --settore "studi legali" --citta "Roma" --max 40
    python implementation/search_ai_prospects.py --settore "agenzie immobiliari" --citta "Torino" --min-dipendenti 20

Input:
    --settore: Settore target (obbligatorio)
    --citta: Città target (obbligatorio)
    --max: Numero massimo di aziende da analizzare (default: 40)
    --min-dipendenti: Dimensione minima stimata (default: 10)

Output:
    Nuove righe nel tab "Lead_AIProspect" del Google Sheets configurato
"""

import os
import re
import sys
import csv
import time
import random
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.utils.logger import get_logger, log_errore_fatale
from implementation.utils.contact_extractor import estrai_email_da_html, estrai_telefono_da_html
from implementation.utils.sheets_client import crea_client_da_env, INTESTAZIONI_AI_PROSPECT

load_dotenv()

# Costanti
SOGLIA_SCORE_MINIMO = 25          # Score minimo per inserire il lead
PAUSA_TRA_SITI = 2.5              # secondi (rispetta rate limit)
TIMEOUT_HTTP = 15                  # timeout richieste HTTP

# Header browser realistico per evitare blocchi
HEADERS_BROWSER = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Ruoli che segnalano processi manuali
RUOLI_MANUALI = [
    "back office", "data entry", "segreteria", "segretaria", "segretario",
    "addetto inserimento dati", "amministrativo", "impiegato amministrativo",
    "customer service", "supporto clienti", "assistente", "coordinatore operativo",
    "preventivista", "operatore", "receptionist", "addetto alle pratiche",
    "responsabile amministrativo", "contabile", "addetto contabilità",
    "logistica", "addetto magazzino", "spedizioni",
]

# Settori ad alta priorità AI
SETTORI_ALTA_PRIORITA = [
    "logistica", "trasporti", "studi legali", "avvocati", "commercialisti",
    "agenzie immobiliari", "immobiliare", "e-commerce", "ecommerce",
    "cliniche", "medici", "dentisti", "agenzie marketing", "manifattura",
    "assicurazioni", "finanza", "consulenza", "revisione contabile",
]


# ---------------------------------------------------------------------------
# Ricerca Google
# ---------------------------------------------------------------------------

def cerca_aziende_google(settore: str, citta: str, max_risultati: int, logger) -> list:
    """
    Cerca aziende nel settore target usando Google.

    Restituisce una lista di dict con: nome, url, snippet.
    Usa più query per massimizzare la copertura.
    """
    query_list = [
        f'"{settore}" "{citta}" srl contatti',
        f'"{settore}" "{citta}" azienda chi siamo',
        f'studio {settore} {citta} contatti',
        f'{settore} {citta} "la nostra azienda" OR "il nostro team"',
    ]

    url_trovati = {}  # url -> dict base

    for query in query_list:
        if len(url_trovati) >= max_risultati:
            break
        try:
            risultati = _ricerca_google(query, logger)
            for r in risultati:
                url = r.get("url", "")
                if url and url not in url_trovati:
                    url_trovati[url] = r
        except Exception as e:
            logger.warning(f"Errore ricerca Google query '{query}': {e}")
        time.sleep(PAUSA_TRA_SITI)

    return list(url_trovati.values())[:max_risultati]


def _ricerca_google(query: str, logger) -> list:
    """
    Esegue una singola ricerca Google e restituisce URL + snippet.
    Usa l'HTML pubblico di Google (nessuna API key richiesta).
    """
    url = "https://www.google.com/search"
    params = {"q": query, "num": 10, "hl": "it", "gl": "it"}

    try:
        risposta = requests.get(
            url, params=params, headers=HEADERS_BROWSER,
            timeout=TIMEOUT_HTTP
        )
        if risposta.status_code != 200:
            return []

        soup = BeautifulSoup(risposta.text, "lxml")
        risultati = []

        for div in soup.select("div.g"):
            link_tag = div.select_one("a[href]")
            snippet_tag = div.select_one("div.VwiC3b, span.st")

            if not link_tag:
                continue

            href = link_tag.get("href", "")
            if not href.startswith("http"):
                continue

            dominio = urlparse(href).netloc
            # Salta motori di ricerca, social, aggregatori
            da_saltare = ["google.", "facebook.", "instagram.", "linkedin.",
                          "paginegialle", "tuttocittà", "yelp.", "tripadvisor.",
                          "wikipedia.", "youtube.", "twitter.", "tiktok."]
            if any(s in dominio for s in da_saltare):
                continue

            snippet = snippet_tag.get_text(strip=True) if snippet_tag else ""
            risultati.append({
                "url": href,
                "dominio": dominio,
                "snippet": snippet,
                "nome_azienda": "",  # verrà estratto dal sito
            })

        return risultati

    except Exception as e:
        logger.debug(f"Errore _ricerca_google: {e}")
        return []


# ---------------------------------------------------------------------------
# Ricerca offerte di lavoro (Indeed)
# ---------------------------------------------------------------------------

def cerca_offerte_lavoro(settore: str, citta: str, logger) -> dict:
    """
    Cerca offerte di lavoro su Indeed per ruoli manuali nel settore target.

    Restituisce un dict: {nome_azienda_lower: [descrizione_offerta, ...]}
    """
    offerte_per_azienda = {}

    # Costruisce query con ruoli manuali più rilevanti
    ruoli_query = " OR ".join(f'"{r}"' for r in RUOLI_MANUALI[:6])
    query = f'({ruoli_query}) {settore} {citta}'

    url = "https://it.indeed.com/jobs"
    params = {"q": query, "l": citta, "lang": "it"}

    try:
        risposta = requests.get(
            url, params=params, headers=HEADERS_BROWSER,
            timeout=TIMEOUT_HTTP
        )
        if risposta.status_code != 200:
            logger.debug(f"Indeed: status {risposta.status_code}")
            return {}

        soup = BeautifulSoup(risposta.text, "lxml")

        for card in soup.select("div.job_seen_beacon, div.tapItem"):
            titolo_tag = card.select_one("h2.jobTitle, span[title]")
            azienda_tag = card.select_one("span.companyName, [data-testid='company-name']")

            titolo = titolo_tag.get_text(strip=True) if titolo_tag else ""
            azienda = azienda_tag.get_text(strip=True) if azienda_tag else ""

            if not azienda or not titolo:
                continue

            # Verifica che il titolo contenga effettivamente un ruolo manuale
            titolo_lower = titolo.lower()
            if not any(r in titolo_lower for r in RUOLI_MANUALI):
                continue

            chiave = azienda.lower().strip()
            if chiave not in offerte_per_azienda:
                offerte_per_azienda[chiave] = []
            offerte_per_azienda[chiave].append(titolo)

    except Exception as e:
        logger.warning(f"Errore ricerca Indeed: {e}")

    return offerte_per_azienda


# ---------------------------------------------------------------------------
# Analisi sito aziendale
# ---------------------------------------------------------------------------

def analizza_sito_azienda(url: str, logger) -> dict:
    """
    Analizza il sito di un'azienda per rilevare segnali di automazione potenziale.

    Restituisce un dict con:
        - nome_azienda: str
        - score_ai: int (0-100+)
        - segnali: list[str]
        - telefono: str
        - email: str
        - tool_usati: list[str]
        - n_dipendenti_stimato: str
        - processo_target: str
    """
    risultato = {
        "nome_azienda": "",
        "score_ai": 0,
        "segnali": [],
        "telefono": None,
        "email": None,
        "tool_usati": [],
        "n_dipendenti_stimato": "sconosciuto",
        "processo_target": "",
        "raggiungibile": True,
    }

    try:
        risposta = requests.get(
            url, headers=HEADERS_BROWSER,
            timeout=TIMEOUT_HTTP, allow_redirects=True
        )
        if risposta.status_code >= 400:
            risultato["raggiungibile"] = False
            return risultato

        html = risposta.text
        soup = BeautifulSoup(html, "lxml")

        testo_pagina = soup.get_text(separator=" ", strip=True).lower()

        # Estrai nome azienda
        tag_title = soup.find("title")
        if tag_title:
            risultato["nome_azienda"] = tag_title.get_text(strip=True).split("|")[0].split("-")[0].strip()

        # Estrai contatti
        risultato["email"] = estrai_email_da_html(url)
        risultato["telefono"] = estrai_telefono_da_html(url)

        # --- Calcolo score AI potenziale ---
        score = 0
        segnali = []

        # Segnale 1: Pagina lavora-con-noi con ruoli manuali
        link_lavora = soup.find_all("a", string=re.compile(
            r"lavora con noi|careers|posizioni aperte|offerte lavoro|join us",
            re.IGNORECASE
        ))
        if link_lavora:
            score += 15
            segnali.append("Pagina 'Lavora con noi' presente")
            # Prova a seguire il link per cercare ruoli manuali
            try:
                href_lavora = link_lavora[0].get("href", "")
                if href_lavora:
                    url_lavora = urljoin(url, href_lavora)
                    r2 = requests.get(url_lavora, headers=HEADERS_BROWSER, timeout=10)
                    testo_lavora = r2.text.lower() if r2.status_code == 200 else ""
                    if any(r in testo_lavora for r in RUOLI_MANUALI):
                        score += 20
                        segnali.append("Ruoli manuali trovati nella pagina lavora-con-noi")
            except Exception:
                pass

        # Segnale 2: Nessun chatbot o widget di supporto
        script_chatbot = ["intercom", "zendesk", "tidio", "tawk", "crisp",
                          "hubspot", "drift", "freshchat", "livechat"]
        html_lower = html.lower()
        ha_chatbot = any(c in html_lower for c in script_chatbot)
        if not ha_chatbot:
            score += 10
            segnali.append("Nessun chatbot rilevato (customer service manuale)")

        # Segnale 3: Form di contatto generico (no booking online)
        form_booking = ["calendly", "simplybook", "doctolib", "booksy",
                        "mindbody", "prenotazione online", "prenota online"]
        ha_booking = any(b in html_lower for b in form_booking)
        if not ha_booking:
            forms = soup.find_all("form")
            if forms:
                score += 15
                segnali.append("Form contatto generico (nessun booking automatizzato)")

        # Segnale 4: Nessun portale clienti o area riservata
        area_riservata = ["area clienti", "portale clienti", "accedi", "login",
                          "my account", "area riservata"]
        if not any(a in html_lower for a in area_riservata):
            score += 10
            segnali.append("Nessun portale clienti self-service")

        # Segnale 5: Prezzi su richiesta (preventivazione manuale)
        preventivo_keywords = ["preventivo", "richiedi preventivo", "contattaci per un preventivo",
                               "su richiesta", "richiedi informazioni", "mandaci una email"]
        if any(k in html_lower for k in preventivo_keywords):
            score += 10
            segnali.append("Preventivi su richiesta (processo manuale)")

        # Segnale 6: Più email diverse (routing comunicazioni manuale)
        email_trovate = re.findall(
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html
        )
        email_uniche = {e.lower() for e in email_trovate if not _email_di_sistema(e)}
        if len(email_uniche) >= 3:
            score += 10
            segnali.append(f"Più email dipartimentali ({len(email_uniche)} trovate)")

        # Segnale 7: Menzione staff o team operativo
        team_keywords = ["il nostro team", "i nostri operatori", "il nostro staff",
                         "il team dedicato", "our team", "personale specializzato"]
        if any(k in html_lower for k in team_keywords):
            score += 10
            segnali.append("Menzione team/staff dedicato")

        # Segnale negativo: già usa automazione avanzata
        automazione_esistente = ["intelligenza artificiale", "ai integrata", "machine learning",
                                 "automazione avanzata", "powered by ai", "ai-powered"]
        if any(a in html_lower for a in automazione_esistente):
            score -= 25
            segnali.append("[NEGATIVO] Già usa soluzioni AI avanzate")

        # Segnale negativo: presenza di chatbot
        if ha_chatbot:
            score -= 20
            segnali.append("[NEGATIVO] Chatbot già attivo")

        # Segnale negativo: portale clienti
        if any(a in html_lower for a in area_riservata):
            score -= 15
            segnali.append("[NEGATIVO] Portale clienti già presente")

        # Stima dipendenti
        risultato["n_dipendenti_stimato"] = _stima_dipendenti(testo_pagina, len(email_uniche))

        # Tool usati
        risultato["tool_usati"] = _rileva_tool(html_lower)

        # Processo target principale
        risultato["processo_target"] = _identifica_processo_target(segnali, testo_pagina)

        risultato["score_ai"] = max(0, score)
        risultato["segnali"] = segnali

    except requests.exceptions.Timeout:
        logger.debug(f"Timeout analisi sito: {url}")
        risultato["raggiungibile"] = False
    except Exception as e:
        logger.debug(f"Errore analisi sito {url}: {e}")
        risultato["raggiungibile"] = False

    return risultato


def _email_di_sistema(email: str) -> bool:
    """Restituisce True se l'email è di sistema (es. noreply, privacy, ecc.)."""
    prefissi_sistema = [
        "noreply", "no-reply", "donotreply", "privacy", "legal",
        "abuse", "spam", "postmaster", "webmaster", "mailer",
        "support@sentry", "example@", "test@"
    ]
    email_l = email.lower()
    return any(p in email_l for p in prefissi_sistema)


def _stima_dipendenti(testo: str, n_email: int) -> str:
    """Stima la fascia di dipendenti basandosi su segnali testuali."""
    if any(k in testo for k in ["500 dipendenti", "1000 dipendenti", "gruppo internazionale"]):
        return "200+"
    if any(k in testo for k in ["100 dipendenti", "200 dipendenti", "50 sedi"]):
        return "50-200"
    if any(k in testo for k in ["20 dipendenti", "30 dipendenti", "un team di oltre"]):
        return "20-50"
    if n_email >= 4:
        return "20-50"
    if n_email >= 2:
        return "10-20"
    return "sconosciuto"


def _rileva_tool(html_lower: str) -> list:
    """Rileva tool/software menzionati nel codice del sito."""
    tool_map = {
        "salesforce": "Salesforce",
        "hubspot": "HubSpot",
        "google analytics": "Google Analytics",
        "google tag manager": "Google Tag Manager",
        "microsoft": "Microsoft 365",
        "dropbox": "Dropbox",
        "monday.com": "Monday.com",
        "asana": "Asana",
        "trello": "Trello",
        "mailchimp": "Mailchimp",
        "shopify": "Shopify",
        "woocommerce": "WooCommerce",
        "prestashop": "PrestaShop",
        "gestionale": "Gestionale (non specificato)",
        "erp": "ERP",
        "crm": "CRM",
    }
    trovati = []
    for chiave, nome in tool_map.items():
        if chiave in html_lower and nome not in trovati:
            trovati.append(nome)
    return trovati


def _identifica_processo_target(segnali: list, testo: str) -> str:
    """Identifica il processo principale più automatizzabile."""
    segnali_lower = " ".join(segnali).lower()

    if "ruoli manuali" in segnali_lower or "data entry" in testo:
        return "Inserimento dati e back office"
    if "customer service" in segnali_lower or "supporto clienti" in testo:
        return "Gestione comunicazioni e customer service"
    if "preventivi" in segnali_lower or "preventivo" in testo:
        return "Generazione e gestione preventivi"
    if "form contatto" in segnali_lower:
        return "Gestione appuntamenti e follow-up lead"
    if "email dipartimentali" in segnali_lower:
        return "Routing e gestione comunicazioni email"
    if "team/staff" in segnali_lower:
        return "Automazione processi operativi"
    return "Processi amministrativi e operativi"


# ---------------------------------------------------------------------------
# Qualifica finale e scoring
# ---------------------------------------------------------------------------

def calcola_score_priorita(
    score_ai: int,
    offerte_lavoro: list,
    ha_email: bool,
    ha_telefono: bool,
    ha_referente: bool,
    n_dipendenti: str,
    settore: str,
) -> int:
    """
    Calcola lo score di priorità outreach (0-100) per un AI prospect.

    Args:
        score_ai: Score potenziale AI (0-100+)
        offerte_lavoro: Lista di offerte di lavoro trovate
        ha_email: Se è stata trovata un'email di contatto
        ha_telefono: Se è stato trovato un telefono
        ha_referente: Se è stato trovato il nome del referente decisionale
        n_dipendenti: Fascia dipendenti (es. "20-50")
        settore: Settore dell'azienda

    Returns:
        Score finale normalizzato 0-100
    """
    score = 0

    # Score AI potenziale
    if score_ai >= 60:
        score += 30
    elif score_ai >= 40:
        score += 15

    # Offerte lavoro (segnale diretto di processo manuale)
    if offerte_lavoro:
        score += 20

    # Contattabilità — critica per il Servizio 2
    if ha_referente:
        score += 20
    if ha_email:
        score += 15
    if ha_telefono:
        score += 10

    # Dimensione aziendale (sweet spot: 20-50)
    if n_dipendenti == "20-50":
        score += 10
    elif n_dipendenti == "50-200":
        score += 5

    # Settore ad alta priorità
    settore_lower = settore.lower()
    if any(s in settore_lower for s in SETTORI_ALTA_PRIORITA):
        score += 10

    # Normalizza su 100
    return min(100, score)


def genera_id_lead_ai(citta: str) -> str:
    """Genera ID univoco per lead AI prospect."""
    iniziali = "".join([p[:2].upper() for p in citta.split()[:2]])
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"AI-{iniziali}-{timestamp}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cerca prospect aziendali per implementazione AI"
    )
    parser.add_argument("--settore", required=True,
                        help="Settore target (es. logistica, studi legali)")
    parser.add_argument("--citta", required=True,
                        help="Città target (es. Milano, Roma)")
    parser.add_argument("--max", type=int, default=40,
                        help="Max aziende da analizzare (default: 40)")
    parser.add_argument("--min-dipendenti", type=int, default=10,
                        help="Dimensione minima stimata dipendenti (default: 10)")
    args = parser.parse_args()

    suffix = f"{args.settore}_{args.citta}".replace(" ", "_").lower()
    logger = get_logger("WF-F", suffix)
    logger.info(f"START — Ricerca AI prospect: {args.settore} in {args.citta}")

    hunter_key = os.getenv("HUNTER_API_KEY", "")

    # Connessione Google Sheets
    sheets = crea_client_da_env()
    tab_nome = "Lead_AIProspect"

    # Carica siti già presenti per deduplicazione
    siti_esistenti = set()
    if sheets:
        try:
            righe = sheets.leggi_tab(tab_nome)
            siti_esistenti = {r.get("SITO_WEB", "") for r in righe if r.get("SITO_WEB")}
            logger.info(f"Aziende già in database: {len(siti_esistenti)}")
        except Exception:
            logger.warning("Impossibile leggere tab Lead_AIProspect (potrebbe non esistere ancora)")

    # Step 1: Ricerca aziende su Google
    logger.info(f"Google search: ricerca aziende '{args.settore}' a {args.citta}")
    candidati = cerca_aziende_google(args.settore, args.citta, args.max, logger)
    logger.info(f"Trovati {len(candidati)} candidati da Google")

    # Step 2: Ricerca offerte di lavoro
    logger.info("Indeed: ricerca offerte di lavoro con ruoli manuali")
    offerte_per_azienda = cerca_offerte_lavoro(args.settore, args.citta, logger)
    logger.info(f"Offerte trovate per {len(offerte_per_azienda)} aziende uniche")

    # Step 3-6: Analisi siti e scoring
    nuovi_lead = []
    n_esclusi_score = 0
    n_duplicati = 0
    n_irraggiungibili = 0
    n_troppo_piccoli = 0

    for candidato in candidati:
        url_sito = candidato.get("url", "")

        if not url_sito:
            continue

        # Deduplicazione
        if url_sito in siti_esistenti:
            logger.debug(f"Duplicato: {url_sito}")
            n_duplicati += 1
            continue

        time.sleep(PAUSA_TRA_SITI + random.uniform(0, 1.5))

        # Analisi sito
        logger.info(f"Analisi: {url_sito}")
        analisi = analizza_sito_azienda(url_sito, logger)

        if not analisi["raggiungibile"]:
            logger.debug(f"Sito irraggiungibile: {url_sito}")
            n_irraggiungibili += 1
            continue

        # Verifica dimensione minima
        n_dip = analisi["n_dipendenti_stimato"]
        if n_dip == "sconosciuto":
            pass  # Procedi con l'incertezza
        elif n_dip == "10-20" and args.min_dipendenti > 10:
            logger.debug(f"Troppo piccola: {analisi['nome_azienda']} ({n_dip})")
            n_troppo_piccoli += 1
            continue

        # Cerca offerte lavoro per questa azienda
        nome_lower = analisi["nome_azienda"].lower()
        offerte_trovate = []
        for chiave_azienda, offerte in offerte_per_azienda.items():
            if chiave_azienda and (chiave_azienda in nome_lower or nome_lower in chiave_azienda):
                offerte_trovate.extend(offerte)

        # Aggiunge il contributo delle offerte allo score AI
        score_ai_finale = analisi["score_ai"]
        if offerte_trovate:
            score_ai_finale = min(100, score_ai_finale + 20)

        # Soglia minima score AI
        if score_ai_finale < SOGLIA_SCORE_MINIMO:
            logger.debug(
                f"Score AI troppo basso ({score_ai_finale}): {analisi['nome_azienda']} — SKIP"
            )
            n_esclusi_score += 1
            continue

        logger.info(
            f"Lead AI trovato (score {score_ai_finale}): {analisi['nome_azienda']} "
            f"→ {analisi['processo_target']}"
        )

        # Calcola score priorità outreach
        ha_email = bool(analisi["email"])
        ha_telefono = bool(analisi["telefono"])
        score_priorita = calcola_score_priorita(
            score_ai=score_ai_finale,
            offerte_lavoro=offerte_trovate,
            ha_email=ha_email,
            ha_telefono=ha_telefono,
            ha_referente=False,  # Ricerca referente non automatizzata (richiederebbe LinkedIn API)
            n_dipendenti=n_dip,
            settore=args.settore,
        )

        fascia = "A" if score_priorita >= 70 else "B" if score_priorita >= 40 else "C"

        # Un lead AI senza email è difficile da approcciare
        pronto = "Sì" if score_priorita >= 40 and ha_email else "No"
        motivo_esclusione = ""
        if not ha_email:
            motivo_esclusione = "nessuna email trovata — necessario trovare referente manualmente"
        elif score_priorita < 40:
            motivo_esclusione = "score priorità insufficiente"

        id_lead = genera_id_lead_ai(args.citta)

        riga = {
            "ID_LEAD": id_lead,
            "DATA_TROVATO": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "NOME_AZIENDA": analisi["nome_azienda"] or urlparse(url_sito).netloc,
            "SETTORE": args.settore,
            "CITTÀ": args.citta,
            "SITO_WEB": url_sito,
            "EMAIL": analisi["email"] or "",
            "TELEFONO": analisi["telefono"] or "",
            "REFERENTE": "",  # Da compilare manualmente o via LinkedIn
            "N_DIPENDENTI_STIMATO": n_dip,
            "SEGNALI_AUTOMAZIONE": "; ".join(
                s for s in analisi["segnali"] if not s.startswith("[NEGATIVO]")
            ),
            "OFFERTE_LAVORO_TROVATE": "; ".join(offerte_trovate),
            "TOOL_USATI": ", ".join(analisi["tool_usati"]),
            "SCORE_AI_POTENZIALE": str(score_ai_finale),
            "PROCESSO_TARGET": analisi["processo_target"],
            "SCORE_PRIORITÀ": str(score_priorita),
            "FASCIA": fascia,
            "PRONTO_OUTREACH": pronto,
            "STATO_OUTREACH": "nuovo",
            "BOZZA_GENERATA": "",
            "DATA_BOZZA": "",
            "DATA_ULTIMO_CONTATTO": "",
            "DATA_RISPOSTA": "",
            "DATA_FOLLOWUP_SCHEDULATO": "",
            "STORICO_STATI": "",
            "NOTE": f"Segnali: {'; '.join(analisi['segnali'][:3])}",
            "MOTIVO_ESCLUSIONE": motivo_esclusione,
        }

        nuovi_lead.append(riga)
        siti_esistenti.add(url_sito)

    # Step 7: Inserimento in Google Sheets
    n_inseriti = 0
    for riga in nuovi_lead:
        if sheets:
            if sheets.aggiungi_riga(tab_nome, riga, INTESTAZIONI_AI_PROSPECT):
                n_inseriti += 1
        else:
            _salva_csv_locale(riga, args.settore, args.citta)
            n_inseriti += 1
        logger.info(
            f"Lead {riga['ID_LEAD']} inserito: {riga['NOME_AZIENDA']} "
            f"— Score AI: {riga['SCORE_AI_POTENZIALE']} "
            f"— Processo: {riga['PROCESSO_TARGET']}"
        )

    logger.info(
        f"END — Candidati trovati: {len(candidati)} | "
        f"Irraggiungibili: {n_irraggiungibili} | "
        f"Troppo piccoli: {n_troppo_piccoli} | "
        f"Score insufficiente: {n_esclusi_score} | "
        f"Duplicati: {n_duplicati} | "
        f"Nuovi lead inseriti: {n_inseriti}"
    )


def _salva_csv_locale(riga: dict, settore: str, citta: str) -> None:
    """Fallback CSV locale se Google Sheets non è disponibile."""
    Path("output").mkdir(exist_ok=True)
    nome_file = (
        f"output/{datetime.now().strftime('%Y-%m-%d')}"
        f"_lead_ai_{settore}_{citta}.csv"
    ).replace(" ", "_").lower()
    file_esiste = Path(nome_file).exists()
    with open(nome_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=INTESTAZIONI_AI_PROSPECT)
        if not file_esiste:
            writer.writeheader()
        writer.writerow(riga)


if __name__ == "__main__":
    main()
