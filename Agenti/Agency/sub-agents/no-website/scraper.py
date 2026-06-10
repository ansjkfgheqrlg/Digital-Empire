"""
Scraper — Sub-agent No-Website
Usa Apify Google Maps per trovare business senza sito web.
"""

import os
import time
import requests
from typing import Optional


APIFY_TOKEN = os.getenv("APIFY_TOKEN")
ACTOR_GOOGLE_MAPS = "nwua9Gu5YrADL7ZDj"
APIFY_BASE = "https://api.apify.com/v2"


def avvia_scraping_google_maps(citta: str, settore: str, max_risultati: int = 100) -> list[dict]:
    """
    Avvia Apify Google Maps e ritorna la lista di business.
    Filtra subito quelli che NON hanno sito web.
    """
    print(f"[NO-WEBSITE] Scraping Google Maps: {settore} a {citta}...")

    payload = {
        "searchStringsArray": [f"{settore} {citta}"],
        "maxCrawledPlacesPerSearch": max_risultati,
        "language": "it",
        "countryCode": "it",
    }

    # Avvia run Apify
    resp = requests.post(
        f"{APIFY_BASE}/acts/{ACTOR_GOOGLE_MAPS}/runs",
        params={"token": APIFY_TOKEN},
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    run_id = resp.json()["data"]["id"]
    print(f"[NO-WEBSITE] Run Apify avviata: {run_id}")

    # Poll fino a completamento
    stato = _attendi_completamento(run_id)
    if stato != "SUCCEEDED":
        raise RuntimeError(f"Run Apify fallita con stato: {stato}")

    # Scarica dataset
    dataset_id = _ottieni_dataset_id(run_id)
    items = _scarica_dataset(dataset_id)

    # Filtra: tieni solo quelli senza website
    no_website = [i for i in items if not i.get("website")]
    print(f"[NO-WEBSITE] Trovati {len(items)} business -> {len(no_website)} senza sito web")
    return no_website


def _attendi_completamento(run_id: str, timeout_sec: int = 300) -> str:
    """Poll run Apify ogni 10 secondi fino a completamento o timeout."""
    inizio = time.time()
    while time.time() - inizio < timeout_sec:
        resp = requests.get(
            f"{APIFY_BASE}/actor-runs/{run_id}",
            params={"token": APIFY_TOKEN},
            timeout=15,
        )
        stato = resp.json()["data"]["status"]
        if stato in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            return stato
        print(f"[NO-WEBSITE] Apify run in corso... ({stato})")
        time.sleep(10)
    return "TIMED-OUT"


def _ottieni_dataset_id(run_id: str) -> str:
    resp = requests.get(
        f"{APIFY_BASE}/actor-runs/{run_id}",
        params={"token": APIFY_TOKEN},
        timeout=15,
    )
    return resp.json()["data"]["defaultDatasetId"]


def _scarica_dataset(dataset_id: str) -> list[dict]:
    resp = requests.get(
        f"{APIFY_BASE}/datasets/{dataset_id}/items",
        params={"token": APIFY_TOKEN, "format": "json"},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()
