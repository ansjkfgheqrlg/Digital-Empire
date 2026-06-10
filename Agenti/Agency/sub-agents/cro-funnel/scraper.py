"""
Scraper — Sub-agent CRO-Funnel
Trova business con siti web che hanno ads attive ma funnel scarso.
Usa Apify Facebook Ads Library + Google Maps.
"""

import os
import time
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN")
ACTOR_FACEBOOK_ADS = "UeNJ51UGugQ9Cwgtd"
ACTOR_GOOGLE_MAPS = "nwua9Gu5YrADL7ZDj"
APIFY_BASE = "https://api.apify.com/v2"


def trova_siti_con_ads(citta: str, settore: str, max_risultati: int = 50) -> list[dict]:
    """
    Trova business locali che hanno ads Facebook attive.
    Questi investono in pubblicità ma potrebbero avere funnel scarso.
    """
    print(f"[CRO-FUNNEL] Ricerca business con ads: {settore} a {citta}...")

    payload = {
        "searchTerms": [f"{settore} {citta}"],
        "maxAds": max_risultati,
        "country": "IT",
    }

    run_id = _avvia_run(ACTOR_FACEBOOK_ADS, payload)
    stato = _attendi_completamento(run_id)
    if stato != "SUCCEEDED":
        raise RuntimeError(f"Run Apify fallita: {stato}")

    dataset_id = _ottieni_dataset_id(run_id)
    items = _scarica_dataset(dataset_id)

    # Tieni solo chi ha un sito web (hanno ads + sito = candidati CRO)
    con_sito = [i for i in items if i.get("website") or i.get("url")]
    print(f"[CRO-FUNNEL] Trovati {len(items)} business con ads -> {len(con_sito)} con sito web")
    return con_sito


def trova_siti_google_maps(citta: str, settore: str, max_risultati: int = 80) -> list[dict]:
    """
    Alternativa: usa Google Maps per trovare business con sito web nel settore.
    """
    print(f"[CRO-FUNNEL] Google Maps scraping: {settore} a {citta}...")

    payload = {
        "searchStringsArray": [f"{settore} {citta}"],
        "maxCrawledPlacesPerSearch": max_risultati,
        "language": "it",
        "countryCode": "it",
    }

    run_id = _avvia_run(ACTOR_GOOGLE_MAPS, payload)
    stato = _attendi_completamento(run_id)
    if stato != "SUCCEEDED":
        raise RuntimeError(f"Run Apify fallita: {stato}")

    dataset_id = _ottieni_dataset_id(run_id)
    items = _scarica_dataset(dataset_id)

    # Tieni solo chi ha sito web
    con_sito = [i for i in items if i.get("website")]
    print(f"[CRO-FUNNEL] {len(con_sito)}/{len(items)} hanno un sito web")
    return con_sito


def _avvia_run(actor_id: str, payload: dict) -> str:
    resp = requests.post(
        f"{APIFY_BASE}/acts/{actor_id}/runs",
        params={"token": APIFY_TOKEN},
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["data"]["id"]


def _attendi_completamento(run_id: str, timeout_sec: int = 300) -> str:
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
        print(f"[CRO-FUNNEL] Apify run in corso... ({stato})")
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
