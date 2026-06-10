"""
WF-B — Ricerca Business che Fanno Ads con Funnel Scarsi

Cerca business che pubblicano ads su Facebook/Instagram tramite Apify
Facebook Ad Library Scraper, analizza la qualità delle loro landing page
e salva i candidati con funnel debole in CSV locale.

Uso:
    python implementation/search_ads_leads.py --settore "dentista" --citta "Milano"
    python implementation/search_ads_leads.py --settore "palestra" --citta "Roma" --max 80

Input:
    --settore: Settore/tipo di attività (obbligatorio)
    --citta: Città target per filtraggio (obbligatorio)
    --paese: Codice paese ISO (default: IT)
    --max: Numero massimo di ads da analizzare (default: 50)

Output:
    CSV in output/YYYY-MM-DD_lead_adsscarsi_[settore]_[citta].csv
    File di log in logs/
"""

import os
import sys
import csv
import time
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from dotenv import load_dotenv
import requests

sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.utils.logger import get_logger, log_errore_fatale
from implementation.utils.website_checker import calcola_funnel_score
from implementation.utils.contact_extractor import estrai_contatti_business
from implementation.utils.sheets_client import INTESTAZIONI_FUNNEL_SCARSO

load_dotenv()

# Costanti
APIFY_BASE_URL = "https://api.apify.com/v2"
TIMEOUT_POLL = 300          # secondi massimi di attesa run Apify
PAUSA_POLL = 5              # secondi tra check status
PAUSA_TRA_SITI = 3.0        # secondi tra analisi landing page
SOGLIA_FUNNEL_SCARSO = 60   # Score <= questa soglia = lead


# ---------------------------------------------------------------------------
# Client Apify (condiviso con WF-A, replicato per indipendenza dei moduli)
# ---------------------------------------------------------------------------

def avvia_run_apify(actor_id: str, input_data: dict, token: str) -> str:
    """Avvia un run Apify e restituisce il run_id."""
    url = f"{APIFY_BASE_URL}/acts/{actor_id}/runs"
    risposta = requests.post(
        url,
        json=input_data,
        headers={"Authorization": f"Bearer {token}"},
        timeout=30
    )
    risposta.raise_for_status()
    return risposta.json()["data"]["id"]


def attendi_run_apify(run_id: str, token: str, timeout: int = TIMEOUT_POLL) -> str:
    """Attende il completamento del run e restituisce il dataset_id."""
    url = f"{APIFY_BASE_URL}/actor-runs/{run_id}"
    headers = {"Authorization": f"Bearer {token}"}
    atteso = 0

    while atteso < timeout:
        risposta = requests.get(url, headers=headers, timeout=15)
        risposta.raise_for_status()
        dati = risposta.json()["data"]
        status = dati["status"]

        if status == "SUCCEEDED":
            return dati["defaultDatasetId"]
        elif status in ("FAILED", "ABORTED", "TIMED-OUT"):
            raise Exception(f"Run Apify terminato con status: {status}")

        time.sleep(PAUSA_POLL)
        atteso += PAUSA_POLL

    raise Exception(f"Run Apify in timeout dopo {timeout}s")


def scarica_dataset_apify(dataset_id: str, token: str) -> list:
    """Scarica i risultati da un dataset Apify."""
    url = f"{APIFY_BASE_URL}/datasets/{dataset_id}/items"
    risposta = requests.get(
        url,
        params={"format": "json", "clean": "true"},
        headers={"Authorization": f"Bearer {token}"},
        timeout=60
    )
    risposta.raise_for_status()
    return risposta.json()


# ---------------------------------------------------------------------------
# Ricerca ads su Facebook Ad Library via Apify
# ---------------------------------------------------------------------------

def cerca_ads_apify(
    settore: str,
    citta: str,
    paese: str,
    max_ads: int,
    token: str,
    actor_id: str,
    logger
) -> list:
    """
    Cerca annunci attivi su Facebook Ad Library tramite Apify.

    L'actor Apify riceve come startUrl la URL della Facebook Ad Library
    con i parametri di ricerca pre-impostati.

    Args:
        settore: Termine di ricerca (settore/categoria)
        citta: Città per filtraggio risultati
        paese: Codice paese ISO (es. "IT")
        max_ads: Max annunci da recuperare
        token: Apify API token
        actor_id: ID actor Facebook Ads Apify

    Returns:
        Lista di annunci (dicts)
    """
    # Costruisce la URL della Facebook Ad Library come start URL
    params_fb = urlencode({
        "active_status": "active",
        "ad_type": "all",
        "country": paese,
        "q": settore,
        "search_type": "keyword_unordered",
    })
    start_url = f"https://www.facebook.com/ads/library/?{params_fb}"

    input_actor = {
        "startUrls": [{"url": start_url}],
        "maxItems": max_ads,
        "searchTerms": [settore],
        "country": paese,
        "activeStatus": "ACTIVE",
    }

    logger.info(f"Apify Facebook Ads: avvio run per '{settore}' in {paese} (max {max_ads})")

    for tentativo in range(3):
        try:
            run_id = avvia_run_apify(actor_id, input_actor, token)
            logger.info(f"Run avviato: {run_id}")

            dataset_id = attendi_run_apify(run_id, token)
            logger.info(f"Run completato. Dataset: {dataset_id}")

            ads = scarica_dataset_apify(dataset_id, token)
            logger.info(f"Apify: {len(ads)} annunci trovati")
            return ads

        except Exception as e:
            attesa = 2 ** tentativo * 2
            logger.warning(f"Tentativo {tentativo + 1}/3 fallito: {e}. Attendo {attesa}s...")
            if tentativo < 2:
                time.sleep(attesa)
            else:
                raise


# ---------------------------------------------------------------------------
# Elaborazione ads
# ---------------------------------------------------------------------------

def filtra_per_citta(ads: list, citta: str) -> list:
    """
    Filtra gli annunci per città target cercando il nome nel testo dell'ad.

    Se il filtro è troppo restrittivo (< 10% dei risultati) restituisce tutto.
    """
    citta_lower = citta.lower()
    filtrati = [
        ad for ad in ads
        if citta_lower in str(ad.get("pageName", "")).lower()
        or citta_lower in str(ad.get("pageAbout", "")).lower()
        or citta_lower in str(ad.get("adBody", "")).lower()
        or citta_lower in str(ad.get("adTitle", "")).lower()
    ]

    if len(filtrati) < max(1, len(ads) * 0.1):
        return ads  # Filtro troppo restrittivo → usa tutto

    return filtrati


def raggruppa_per_pagina(ads: list) -> dict:
    """
    Raggruppa gli annunci per pagina Facebook (un business = una pagina).

    Returns:
        Dict {page_id: {"page_name": ..., "ads": [...], "url_landing": ...}}
    """
    pagine = {}

    for ad in ads:
        page_id = (
            ad.get("pageId") or ad.get("page_id") or
            ad.get("fundingEntityId") or str(ad.get("id", ""))
        )
        if not page_id:
            continue

        if page_id not in pagine:
            pagine[page_id] = {
                "page_id": page_id,
                "page_name": ad.get("pageName") or ad.get("page_name") or "",
                "ads": [],
                "url_landing": "",
                "url_pagina_fb": ad.get("pageUrl") or f"https://www.facebook.com/{page_id}",
            }

        pagine[page_id]["ads"].append(ad)

        # Prendi il primo URL di landing page disponibile
        if not pagine[page_id]["url_landing"]:
            url = (
                ad.get("adCreativeLinkUrl") or
                ad.get("linkUrl") or
                ad.get("adSnapshotUrl") or
                ""
            )
            if url and url.startswith("http") and "facebook.com" not in url:
                pagine[page_id]["url_landing"] = url

    return pagine


def genera_id_lead_fb(citta: str) -> str:
    """Genera ID univoco per lead da Facebook."""
    iniziali = "".join([p[:2].upper() for p in citta.split()[:2]])
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"AF-{iniziali}-{timestamp}"


def salva_csv(riga: dict, settore: str, citta: str) -> None:
    """Salva un lead su CSV locale."""
    Path("output").mkdir(exist_ok=True)
    nome_file = (
        f"output/{datetime.now().strftime('%Y-%m-%d')}"
        f"_lead_adsscarsi_{settore}_{citta}.csv"
    ).replace(" ", "_").lower()
    file_esiste = Path(nome_file).exists()
    with open(nome_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=INTESTAZIONI_FUNNEL_SCARSO)
        if not file_esiste:
            writer.writeheader()
        writer.writerow(riga)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cerca business che fanno ads con funnel scarsi tramite Apify"
    )
    parser.add_argument("--settore", required=True, help="Settore target (es. dentista)")
    parser.add_argument("--citta", required=True, help="Città target per filtraggio")
    parser.add_argument("--paese", default="IT", help="Codice paese ISO (default: IT)")
    parser.add_argument("--max", type=int, default=50, help="Max ads da analizzare (default: 50)")
    args = parser.parse_args()

    suffix = f"{args.settore}_{args.citta}".replace(" ", "_").lower()
    logger = get_logger("WF-B", suffix)
    logger.info(f"START — Ricerca ads: {args.settore} in {args.paese}, filtro città: {args.citta}")

    # Credenziali
    apify_token = os.getenv("APIFY_API_TOKEN")
    if not apify_token:
        log_errore_fatale("WF-B", "APIFY_API_TOKEN non configurato nel .env")
        logger.error("ERRORE FATALE: APIFY_API_TOKEN mancante")
        sys.exit(1)

    actor_id = os.getenv("APIFY_ACTOR_FACEBOOK_ADS", "UeNJ51UGugQ9Cwgtd")

    # Carica page_id già presenti da CSV precedenti
    page_id_esistenti = _carica_page_id_da_csv(args.settore, args.citta)
    logger.info(f"Business già in database: {len(page_id_esistenti)}")

    # Step 1: Cerca ads via Apify
    try:
        ads = cerca_ads_apify(
            args.settore, args.citta, args.paese, args.max,
            apify_token, actor_id, logger
        )
    except Exception as e:
        log_errore_fatale("WF-B", str(e))
        logger.error(f"ERRORE FATALE Apify: {e}")
        sys.exit(1)

    # Filtra per città e raggruppa per pagina
    ads_filtrati = filtra_per_citta(ads, args.citta)
    logger.info(f"Ads dopo filtro città '{args.citta}': {len(ads_filtrati)}")

    pagine = raggruppa_per_pagina(ads_filtrati)
    logger.info(f"Business unici: {len(pagine)}")

    # Step 2-4: Analisi funnel e raccolta contatti
    nuovi_lead = []
    n_funnel_ok = 0
    n_duplicati = 0
    n_senza_landing = 0

    for page_id, info in pagine.items():
        nome_pagina = info["page_name"]
        url_landing = info["url_landing"]
        n_ads = len(info["ads"])

        # Deduplicazione
        if page_id in page_id_esistenti:
            logger.debug(f"Duplicato: {nome_pagina}")
            n_duplicati += 1
            continue

        # Skip se senza landing page
        if not url_landing:
            logger.debug(f"Nessuna landing page: {nome_pagina}")
            n_senza_landing += 1
            continue

        time.sleep(PAUSA_TRA_SITI)

        # Analisi funnel score (solo HTML, senza PageSpeed)
        logger.info(f"Analisi funnel: {nome_pagina} → {url_landing}")
        analisi = calcola_funnel_score(url_landing)
        score_funnel = analisi["score_finale"]

        if score_funnel > SOGLIA_FUNNEL_SCARSO:
            logger.debug(f"Funnel ok (score {score_funnel}): {nome_pagina} — SKIP")
            n_funnel_ok += 1
            continue

        logger.info(f"Funnel scarso (score {score_funnel}): {nome_pagina} → lead!")

        # Estrai contatti
        contatti = estrai_contatti_business(
            nome_business=nome_pagina,
            url_sito=url_landing,
            url_pagina_fb=info["url_pagina_fb"],
        )

        # REGOLA CRITICA: senza email il lead non viene salvato
        if not contatti["email"]:
            logger.debug(f"Email assente: {nome_pagina} — SKIP (nessun contatto email)")
            continue

        # Score priorità outreach
        score_priorita = 100 - score_funnel
        if n_ads >= 3:
            score_priorita += 15
        if contatti["email"]:
            score_priorita += 15
        if contatti["telefono"]:
            score_priorita += 10
        score_priorita = min(100, score_priorita)

        id_lead = genera_id_lead_fb(args.citta)
        problemi = analisi.get("problemi_descrizione", "")

        riga = {
            "ID_LEAD": id_lead,
            "DATA_TROVATO": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "NOME_PAGINA": nome_pagina,
            "SETTORE": args.settore,
            "CITTÀ": args.citta,
            "URL_PAGINA_FB": info["url_pagina_fb"],
            "URL_LANDING": url_landing,
            "TELEFONO": contatti["telefono"] or "",
            "EMAIL": contatti["email"] or "",
            "SCORE_FUNNEL": str(score_funnel),
            "DETTAGLIO_SCORE": problemi,
            "N_ADS_ATTIVI": str(n_ads),
            "SCORE_PRIORITÀ": str(score_priorita),
            "FASCIA": "A" if score_priorita >= 70 else "B" if score_priorita >= 40 else "C",
            "PRONTO_OUTREACH": "Sì" if score_priorita >= 40 and (contatti["email"] or contatti["telefono"]) else "No",
            "STATO_OUTREACH": "nuovo",
            "BOZZA_GENERATA": "",
            "DATA_BOZZA": "",
            "DATA_ULTIMO_CONTATTO": "",
            "DATA_RISPOSTA": "",
            "DATA_FOLLOWUP_SCHEDULATO": "",
            "STORICO_STATI": "",
            "NOTE": f"Problemi: {problemi}",
            "MOTIVO_ESCLUSIONE": "" if (contatti["email"] or contatti["telefono"]) else "nessun contatto trovato",
        }

        nuovi_lead.append(riga)
        page_id_esistenti.add(page_id)

    # Step 5: Salva su CSV
    for riga in nuovi_lead:
        salva_csv(riga, args.settore, args.citta)

    logger.info(
        f"END — Ads trovati: {len(ads)} | "
        f"Business unici: {len(pagine)} | "
        f"Funnel ok (esclusi): {n_funnel_ok} | "
        f"Senza landing: {n_senza_landing} | "
        f"Duplicati: {n_duplicati} | "
        f"Nuovi lead salvati: {len(nuovi_lead)}"
    )


def _carica_page_id_da_csv(settore: str, citta: str) -> set:
    """Carica i page_id già salvati nei CSV precedenti per deduplicazione."""
    page_ids = set()
    output_dir = Path("output")
    if not output_dir.exists():
        return page_ids

    pattern = f"*_lead_adsscarsi_{settore}_{citta}*".replace(" ", "_").lower()
    for csv_file in output_dir.glob(pattern):
        try:
            with open(csv_file, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    url_fb = row.get("URL_PAGINA_FB", "")
                    if url_fb:
                        pid = url_fb.split("/")[-1]
                        if pid:
                            page_ids.add(pid)
        except Exception:
            pass
    return page_ids


if __name__ == "__main__":
    main()
