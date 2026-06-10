"""
WF-A — Ricerca Business Locali Senza Sito Web

Cerca business locali tramite Apify Google Maps Scraper, verifica la presenza
di un sito web e salva i candidati qualificati in CSV locale.

Uso:
    python implementation/search_no_website.py --citta "Milano" --categoria "ristorante"
    python implementation/search_no_website.py --citta "Roma" --categoria "idraulico" --max 100

Input:
    --citta: Città dove cercare (obbligatorio)
    --categoria: Tipo di attività (obbligatorio)
    --max: Numero massimo di risultati da Apify (default: 60)

Output:
    CSV in output/YYYY-MM-DD_lead_nosito_[citta]_[categoria].csv
    File di log in logs/
"""

import os
import sys
import csv
import time
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import requests

sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.utils.logger import get_logger, log_errore_fatale
from implementation.utils.website_checker import verifica_sito_attivo
from implementation.utils.contact_extractor import estrai_contatti_business
from implementation.utils.sheets_client import INTESTAZIONI_NO_SITO

load_dotenv()

# Costanti
APIFY_BASE_URL = "https://api.apify.com/v2"
TIMEOUT_POLL = 300          # secondi massimi di attesa per il run Apify
PAUSA_POLL = 5              # secondi tra un check di status e l'altro
SOGLIA_SCORE_MINIMO = 30

# Settori ad alta domanda (bonus score)
SETTORI_ALTA_DOMANDA = {
    "dentista", "avvocato", "commercialista", "ristorante", "palestra",
    "estetista", "idraulico", "elettricista", "dottore", "veterinario",
    "parrucchiere", "dentist", "lawyer", "accountant", "restaurant",
    "gym", "beauty_salon", "plumber", "electrician", "doctor"
}


# ---------------------------------------------------------------------------
# Client Apify
# ---------------------------------------------------------------------------

def avvia_run_apify(actor_id: str, input_data: dict, token: str) -> str:
    """
    Avvia un run Apify in modo asincrono.

    Args:
        actor_id: ID dell'actor Apify
        input_data: Input JSON per l'actor
        token: Apify API token

    Returns:
        run_id del run avviato

    Raises:
        Exception: se il run non parte
    """
    url = f"{APIFY_BASE_URL}/acts/{actor_id}/runs"
    risposta = requests.post(
        url,
        json=input_data,
        headers={"Authorization": f"Bearer {token}"},
        timeout=30
    )
    risposta.raise_for_status()
    run_id = risposta.json()["data"]["id"]
    return run_id


def attendi_run_apify(run_id: str, token: str, timeout: int = TIMEOUT_POLL) -> str:
    """
    Attende il completamento di un run Apify e restituisce il dataset ID.

    Args:
        run_id: ID del run da monitorare
        token: Apify API token
        timeout: Secondi massimi di attesa

    Returns:
        ID del dataset con i risultati

    Raises:
        Exception: se il run fallisce o va in timeout
    """
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
    """
    Scarica i risultati da un dataset Apify.

    Args:
        dataset_id: ID del dataset
        token: Apify API token

    Returns:
        Lista di item (dict)
    """
    url = f"{APIFY_BASE_URL}/datasets/{dataset_id}/items"
    risposta = requests.get(
        url,
        params={"format": "json", "clean": "true"},
        headers={"Authorization": f"Bearer {token}"},
        timeout=60
    )
    risposta.raise_for_status()
    return risposta.json()


def cerca_business_apify(citta: str, categoria: str, max_risultati: int, token: str, actor_id: str, logger) -> list:
    """
    Cerca business su Google Maps tramite Apify.

    Args:
        citta: Città target
        categoria: Categoria business
        max_risultati: Max risultati da ottenere
        token: Apify API token
        actor_id: ID actor Google Maps Apify

    Returns:
        Lista di business (dict)
    """
    query = f"{categoria} {citta}"

    input_actor = {
        "searchStringsArray": [query],
        "maxCrawledPlacesPerSearch": max_risultati,
        "language": "it",
        "country": "IT",
        "includeWebResults": False,
        "scrapeReviewsPersonalData": False,
        "maxReviews": 0,
    }

    logger.info(f"Apify Google Maps: avvio run per '{query}' (max {max_risultati})")

    # Retry x3 con backoff esponenziale
    for tentativo in range(3):
        try:
            run_id = avvia_run_apify(actor_id, input_actor, token)
            logger.info(f"Run avviato: {run_id}")

            dataset_id = attendi_run_apify(run_id, token)
            logger.info(f"Run completato. Dataset: {dataset_id}")

            risultati = scarica_dataset_apify(dataset_id, token)
            logger.info(f"Apify: {len(risultati)} business trovati")
            return risultati

        except Exception as e:
            attesa = 2 ** tentativo * 2
            logger.warning(f"Tentativo {tentativo + 1}/3 fallito: {e}. Attendo {attesa}s...")
            if tentativo < 2:
                time.sleep(attesa)
            else:
                raise


# ---------------------------------------------------------------------------
# Scoring e utilità
# ---------------------------------------------------------------------------

def calcola_score_no_sito(business: dict, ha_email: bool, sito_rotto: bool) -> int:
    """
    Calcola lo score di priorità per un lead senza sito (0-100).

    Args:
        business: Dati del business da Apify
        ha_email: True se l'email è stata trovata
        sito_rotto: True se aveva un sito ma non funzionante

    Returns:
        Score intero 0-100
    """
    score = 0

    rating = business.get("rating") or business.get("reviewsRating") or 0
    n_recensioni = business.get("reviewsCount") or business.get("user_ratings_total") or 0

    try:
        rating = float(rating)
    except (ValueError, TypeError):
        rating = 0

    try:
        n_recensioni = int(n_recensioni)
    except (ValueError, TypeError):
        n_recensioni = 0

    if rating >= 4.0:
        score += 20
    elif rating >= 3.5:
        score += 10

    if n_recensioni >= 50:
        score += 20
    elif n_recensioni >= 20:
        score += 10

    # Telefono presente nei dati Apify
    telefono = business.get("phone") or business.get("phoneUnformatted") or ""
    if telefono:
        score += 20

    if ha_email:
        score += 20

    # Settore ad alta domanda
    categoria_lower = str(business.get("categoryName") or business.get("type") or "").lower()
    if any(s in categoria_lower for s in SETTORI_ALTA_DOMANDA):
        score += 10

    # Sito completamente assente (vs rotto)
    if not sito_rotto:
        score += 10

    return min(score, 100)


def genera_id_lead(citta: str) -> str:
    """Genera ID univoco per il lead."""
    iniziali = "".join([p[:2].upper() for p in citta.split()[:2]])
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"NS-{iniziali}-{timestamp}"


def salva_csv(riga: dict, citta: str, categoria: str) -> None:
    """Salva un lead su CSV locale."""
    Path("output").mkdir(exist_ok=True)
    nome_file = (
        f"output/{datetime.now().strftime('%Y-%m-%d')}"
        f"_lead_nosito_{citta}_{categoria}.csv"
    ).replace(" ", "_").lower()
    file_esiste = Path(nome_file).exists()
    with open(nome_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=INTESTAZIONI_NO_SITO)
        if not file_esiste:
            writer.writeheader()
        writer.writerow(riga)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cerca business locali senza sito web tramite Apify"
    )
    parser.add_argument("--citta", required=True, help="Città dove cercare (es. Milano)")
    parser.add_argument("--categoria", required=True, help="Categoria business (es. ristorante)")
    parser.add_argument("--max", type=int, default=60, help="Max risultati (default: 60)")
    args = parser.parse_args()

    suffix = f"{args.citta}_{args.categoria}".replace(" ", "_").lower()
    logger = get_logger("WF-A", suffix)
    logger.info(f"START — Ricerca: {args.categoria} in {args.citta}")

    # Leggi credenziali
    apify_token = os.getenv("APIFY_API_TOKEN")
    if not apify_token:
        log_errore_fatale("WF-A", "APIFY_API_TOKEN non configurato nel .env")
        logger.error("ERRORE FATALE: APIFY_API_TOKEN mancante")
        sys.exit(1)

    actor_id = os.getenv("APIFY_ACTOR_GOOGLE_MAPS", "nwua9Gu5YrADL7ZDj")

    # Carica place_id già presenti (deduplicazione da CSV precedenti)
    place_id_esistenti = _carica_place_id_da_csv(args.citta, args.categoria)
    logger.info(f"Place ID già in database: {len(place_id_esistenti)}")

    # Step 1: Cerca business su Google Maps via Apify
    try:
        business_list = cerca_business_apify(
            args.citta, args.categoria, args.max, apify_token, actor_id, logger
        )
    except Exception as e:
        log_errore_fatale("WF-A", str(e))
        logger.error(f"ERRORE FATALE Apify: {e}")
        sys.exit(1)

    # Step 2-4: Analisi, filtraggio e scoring
    nuovi_lead = []
    n_con_sito_ok = 0
    n_duplicati = 0

    for business in business_list:
        place_id = business.get("placeId") or business.get("place_id") or ""
        nome = business.get("title") or business.get("name") or "Sconosciuto"

        # Deduplicazione
        if place_id and place_id in place_id_esistenti:
            logger.debug(f"Duplicato: {nome}")
            n_duplicati += 1
            continue

        sito_url = business.get("website") or ""

        # Verifica sito
        sito_rotto = False
        if sito_url:
            check = verifica_sito_attivo(sito_url)
            if check["attivo"]:
                logger.debug(f"Sito OK: {nome} — SKIP")
                n_con_sito_ok += 1
                continue
            else:
                sito_rotto = True
                logger.debug(f"Sito rotto ({check['errore']}): {nome} → lead!")

        # Estrai contatti aggiuntivi dal sito (se rotto) o cerca via scraping
        contatti = estrai_contatti_business(
            nome_business=nome,
            url_sito=sito_url if sito_rotto else None,
        )

        telefono_finale = (
            business.get("phone") or business.get("phoneUnformatted") or
            contatti["telefono"] or ""
        )
        email_finale = contatti["email"] or ""

        # REGOLA CRITICA: senza email il lead non viene salvato
        if not email_finale:
            logger.debug(f"Email assente: {nome} — SKIP (nessun contatto email)")
            continue

        ha_email = True

        # Score
        score = calcola_score_no_sito(business, ha_email, sito_rotto)

        if score < SOGLIA_SCORE_MINIMO:
            logger.debug(f"Score basso ({score}): {nome} — SKIP")
            continue

        id_lead = genera_id_lead(args.citta)
        riga = {
            "ID_LEAD": id_lead,
            "DATA_TROVATO": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "NOME_BUSINESS": nome,
            "CATEGORIA": args.categoria,
            "INDIRIZZO": business.get("address") or business.get("formatted_address") or "",
            "CITTÀ": args.citta,
            "TELEFONO": telefono_finale,
            "EMAIL": email_finale,
            "RATING_GOOGLE": str(business.get("rating") or business.get("reviewsRating") or ""),
            "N_RECENSIONI": str(business.get("reviewsCount") or business.get("user_ratings_total") or ""),
            "PLACE_ID": place_id,
            "SCORE_PRIORITÀ": str(score),
            "FASCIA": "A" if score >= 70 else "B" if score >= 40 else "C",
            "PRONTO_OUTREACH": "Sì" if score >= 40 and (telefono_finale or email_finale) else "No",
            "STATO_OUTREACH": "nuovo",
            "BOZZA_GENERATA": "",
            "DATA_BOZZA": "",
            "DATA_ULTIMO_CONTATTO": "",
            "DATA_RISPOSTA": "",
            "DATA_FOLLOWUP_SCHEDULATO": "",
            "STORICO_STATI": "",
            "NOTE": f"Sito {'rotto' if sito_rotto else 'assente'}",
            "MOTIVO_ESCLUSIONE": "" if (telefono_finale or email_finale) else "nessun contatto trovato",
        }

        nuovi_lead.append(riga)
        if place_id:
            place_id_esistenti.add(place_id)
        logger.info(f"Lead: {nome} (score: {score}, fascia: {riga['FASCIA']})")

    # Step 5: Salva su CSV
    for riga in nuovi_lead:
        salva_csv(riga, args.citta, args.categoria)

    logger.info(
        f"END — Trovati: {len(business_list)} | "
        f"Con sito OK: {n_con_sito_ok} | "
        f"Duplicati: {n_duplicati} | "
        f"Nuovi lead salvati: {len(nuovi_lead)}"
    )


def _carica_place_id_da_csv(citta: str, categoria: str) -> set:
    """Carica i place_id già salvati nei CSV precedenti per deduplicazione."""
    place_ids = set()
    output_dir = Path("output")
    if not output_dir.exists():
        return place_ids

    pattern = f"*_lead_nosito_{citta}_{categoria}*".replace(" ", "_").lower()
    for csv_file in output_dir.glob(pattern):
        try:
            with open(csv_file, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    pid = row.get("PLACE_ID", "")
                    if pid:
                        place_ids.add(pid)
        except Exception:
            pass
    return place_ids


if __name__ == "__main__":
    main()
