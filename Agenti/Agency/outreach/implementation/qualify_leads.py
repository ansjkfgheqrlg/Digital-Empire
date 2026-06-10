"""
WF-C — Qualifica e Scoring Lead

Legge i lead con stato "nuovo" dai fogli Google Sheets, li arricchisce
con dati aggiuntivi (email via Hunter.io), ricalcola lo score finale
e li classifica in fasce A/B/C.

Uso:
    python implementation/qualify_leads.py
    python implementation/qualify_leads.py --source no_sito
    python implementation/qualify_leads.py --source funnel_scarso --tutti

Input:
    --source: Quale tab processare (no_sito | funnel_scarso | tutti) (default: tutti)
    --tutti: Processa anche lead già qualificati (ri-qualifica)

Output:
    Colonne aggiornate in Google Sheets: SCORE_PRIORITÀ, FASCIA, PRONTO_OUTREACH
"""

import sys
import argparse
import time
from pathlib import Path
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.utils.logger import get_logger
from implementation.utils.contact_extractor import estrai_contatti_business
from implementation.utils.sheets_client import crea_client_da_env, INTESTAZIONI_NO_SITO, INTESTAZIONI_FUNNEL_SCARSO

load_dotenv()

# Settori ad alta domanda
SETTORI_ALTA_DOMANDA = {
    "dentista", "avvocato", "commercialista", "ristorante", "palestra",
    "estetista", "idraulico", "elettricista", "medico", "veterinario",
    "parrucchiere", "dentist", "lawyer", "accountant", "restaurant",
    "gym", "beauty_salon", "plumber", "electrician", "doctor"
}


def qualifica_lead_no_sito(riga: dict, ha_email_trovata: bool) -> dict:
    """
    Calcola score e fascia per un lead "senza sito".

    Args:
        riga: Dati del lead dal foglio
        ha_email_trovata: Se l'arricchimento ha trovato una nuova email

    Returns:
        Dict con aggiornamenti: score, fascia, pronto, motivo_esclusione
    """
    score = int(riga.get("SCORE_PRIORITÀ", 0) or 0)

    # Bonus arricchimento
    if ha_email_trovata:
        score += 15

    categoria = (riga.get("CATEGORIA", "") or "").lower()
    if any(s in categoria for s in SETTORI_ALTA_DOMANDA):
        score += 10

    score = min(100, score)

    fascia = "A" if score >= 70 else "B" if score >= 40 else "C"
    ha_contatto = bool(riga.get("EMAIL") or riga.get("TELEFONO"))
    pronto = "Sì" if fascia in ("A", "B") and ha_contatto else "No"
    motivo = ""
    if not ha_contatto:
        motivo = "nessun contatto trovato"
    elif fascia == "C":
        motivo = "score troppo basso"

    return {
        "SCORE_PRIORITÀ": str(score),
        "FASCIA": fascia,
        "PRONTO_OUTREACH": pronto,
        "MOTIVO_ESCLUSIONE": motivo
    }


def qualifica_lead_funnel_scarso(riga: dict, ha_email_trovata: bool) -> dict:
    """
    Calcola score e fascia per un lead "funnel scarso".

    Args:
        riga: Dati del lead dal foglio
        ha_email_trovata: Se l'arricchimento ha trovato una nuova email

    Returns:
        Dict con aggiornamenti
    """
    try:
        score_funnel = int(riga.get("SCORE_FUNNEL", 50) or 50)
    except (ValueError, TypeError):
        score_funnel = 50

    # Score priorità = inverso del funnel score + bonus
    score = 100 - score_funnel

    n_ads = int(riga.get("N_ADS_ATTIVI", 0) or 0)
    if n_ads >= 3:
        score += 15

    if ha_email_trovata or riga.get("EMAIL"):
        score += 15

    if riga.get("TELEFONO"):
        score += 10

    settore = (riga.get("SETTORE", "") or "").lower()
    if any(s in settore for s in SETTORI_ALTA_DOMANDA):
        score += 10

    # Normalizza su 100
    score = min(100, max(0, score))

    fascia = "A" if score >= 70 else "B" if score >= 40 else "C"
    ha_contatto = bool(riga.get("EMAIL") or riga.get("TELEFONO"))
    pronto = "Sì" if fascia in ("A", "B") and ha_contatto else "No"
    motivo = ""
    if not ha_contatto:
        motivo = "nessun contatto trovato"
    elif fascia == "C":
        motivo = "score priorità basso"

    return {
        "SCORE_PRIORITÀ": str(score),
        "FASCIA": fascia,
        "PRONTO_OUTREACH": pronto,
        "MOTIVO_ESCLUSIONE": motivo
    }


def processa_tab(sheets, tab_nome: str, tipo: str, hunter_key: str, solo_nuovi: bool, logger) -> dict:
    """
    Processa un tab del foglio: arricchisce e qualifica ogni lead.

    Args:
        sheets: SheetsClient
        tab_nome: Nome del tab
        tipo: "no_sito" o "funnel_scarso"
        hunter_key: Hunter.io API key
        solo_nuovi: Se True, processa solo stato="nuovo"
        logger: Logger attivo

    Returns:
        Dict con statistiche: n_processati, n_aggiornati, fascia_A, fascia_B, fascia_C
    """
    intestazioni = INTESTAZIONI_NO_SITO if tipo == "no_sito" else INTESTAZIONI_FUNNEL_SCARSO

    righe = sheets.leggi_tab(tab_nome)
    if not righe:
        logger.info(f"Tab {tab_nome}: nessun lead trovato")
        return {"n_processati": 0, "n_aggiornati": 0, "fascia_A": 0, "fascia_B": 0, "fascia_C": 0}

    # Filtra solo quelli da qualificare
    if solo_nuovi:
        righe_da_qualificare = [
            (i + 1, r) for i, r in enumerate(righe)
            if r.get("STATO_OUTREACH") == "nuovo" and not r.get("FASCIA")
        ]
    else:
        righe_da_qualificare = [(i + 1, r) for i, r in enumerate(righe)]

    logger.info(f"Tab {tab_nome}: {len(righe_da_qualificare)} lead da qualificare")

    stats = {"n_processati": 0, "n_aggiornati": 0, "fascia_A": 0, "fascia_B": 0, "fascia_C": 0}

    for num_riga, riga in righe_da_qualificare:
        nome = riga.get("NOME_BUSINESS") or riga.get("NOME_PAGINA") or "?"
        id_lead = riga.get("ID_LEAD", "")

        # Arricchimento email via scraping diretto del sito
        ha_email_trovata = False
        if not riga.get("EMAIL"):
            url_sito = riga.get("URL_LANDING") or riga.get("SITO_WEB") or ""
            if url_sito:
                contatti = estrai_contatti_business(nome_business=nome, url_sito=url_sito)
                email_trovata = contatti.get("email")
                if email_trovata:
                    riga["EMAIL"] = email_trovata
                    ha_email_trovata = True
                    logger.info(f"Email trovata (scraping): {nome} → {email_trovata}")
                    if sheets:
                        sheets.aggiorna_cella(tab_nome, num_riga, "EMAIL", email_trovata, intestazioni)
                    time.sleep(1)  # Rate limit Hunter

        # Calcola qualifica
        if tipo == "no_sito":
            aggiornamenti = qualifica_lead_no_sito(riga, ha_email_trovata)
        else:
            aggiornamenti = qualifica_lead_funnel_scarso(riga, ha_email_trovata)

        fascia = aggiornamenti["FASCIA"]
        stats[f"fascia_{fascia}"] += 1

        # Aggiorna colonne nel foglio
        for colonna, valore in aggiornamenti.items():
            sheets.aggiorna_cella(tab_nome, num_riga, colonna, valore, intestazioni)

        logger.info(f"[{id_lead}] {nome} → fascia {fascia}, score {aggiornamenti['SCORE_PRIORITÀ']}, pronto: {aggiornamenti['PRONTO_OUTREACH']}")

        stats["n_processati"] += 1
        stats["n_aggiornati"] += 1
        time.sleep(0.3)  # Evita rate limit Sheets

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Qualifica e scoring dei lead nei fogli Google Sheets"
    )
    parser.add_argument(
        "--source",
        choices=["no_sito", "funnel_scarso", "tutti"],
        default="tutti",
        help="Quale tab processare (default: tutti)"
    )
    parser.add_argument(
        "--tutti",
        action="store_true",
        help="Processa anche lead già qualificati (ri-qualifica)"
    )
    args = parser.parse_args()

    logger = get_logger("WF-C", "qualifica")
    logger.info(f"START — Qualifica lead (source={args.source}, solo_nuovi={not args.tutti})")

    hunter_key = os.getenv("HUNTER_API_KEY", "")

    sheets = crea_client_da_env()
    if not sheets:
        logger.error("ERRORE: Google Sheets non configurato. Impossibile qualificare i lead.")
        sys.exit(1)

    solo_nuovi = not args.tutti
    stats_totali = {"n_processati": 0, "n_aggiornati": 0, "fascia_A": 0, "fascia_B": 0, "fascia_C": 0}

    # Processa tab in base al source
    tab_da_processare = []
    if args.source in ("no_sito", "tutti"):
        tab_da_processare.append(("Lead_NoSito", "no_sito"))
    if args.source in ("funnel_scarso", "tutti"):
        tab_da_processare.append(("Lead_FunnelScarso", "funnel_scarso"))

    for tab_nome, tipo in tab_da_processare:
        try:
            stats = processa_tab(sheets, tab_nome, tipo, hunter_key, solo_nuovi, logger)
            for k in stats_totali:
                stats_totali[k] += stats[k]
        except Exception as e:
            logger.error(f"Errore processing tab {tab_nome}: {e}")

    logger.info(
        f"END — Processati: {stats_totali['n_processati']} | "
        f"Fascia A: {stats_totali['fascia_A']} | "
        f"Fascia B: {stats_totali['fascia_B']} | "
        f"Fascia C: {stats_totali['fascia_C']}"
    )
    logger.info(
        f"Pronti per outreach: {stats_totali['fascia_A'] + stats_totali['fascia_B']} "
        f"(fascia A+B)"
    )


if __name__ == "__main__":
    main()
