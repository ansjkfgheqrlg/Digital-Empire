"""
Scraper — Sub-agent AI-Implementation
Trova business in settori ad alto potenziale AI tramite Apify Google Maps.
"""

import os
import time
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN")
ACTOR_GOOGLE_MAPS = "nwua9Gu5YrADL7ZDj"
APIFY_BASE = "https://api.apify.com/v2"

# Settori con alto bisogno AI — usati se non viene specificato un settore
SETTORI_AI_DEFAULT = [
    "dentista", "studio dentistico",
    "avvocato", "studio legale",
    "fisioterapista", "centro fisioterapia",
    "commercialista", "studio commercialista",
    "ristorante", "pizzeria",
    "hotel", "b&b", "affittacamere",
    "centro estetico", "salone parrucchiere",
    "agenzia immobiliare",
    "palestra", "centro sportivo",
    "studio medico", "clinica",
]


def trova_business_settore(citta: str, settore: str, max_risultati: int = 60) -> list[dict]:
    """Scraping Google Maps per un settore specifico."""
    print(f"[AI-IMPL] Scraping: {settore} a {citta}...")

    payload = {
        "searchStringsArray": [f"{settore} {citta}"],
        "maxCrawledPlacesPerSearch": max_risultati,
        "language": "it",
        "countryCode": "it",
    }

    run_id = _avvia_run(payload)
    stato = _attendi_completamento(run_id)
    if stato != "SUCCEEDED":
        print(f"[AI-IMPL] WARNING: run Apify stato {stato} per {settore}")
        return []

    dataset_id = _ottieni_dataset_id(run_id)
    items = _scarica_dataset(dataset_id)
    print(f"[AI-IMPL] Trovati {len(items)} risultati per: {settore}")
    return items


def trova_business_multi_settore(citta: str, settori: list[str] = None) -> list[dict]:
    """
    Trova business in più settori AI-ready.
    Se settori non specificati, usa la lista default.
    """
    settori_da_cercare = settori or SETTORI_AI_DEFAULT[:5]  # default: top 5
    tutti = []
    visti = set()  # evita duplicati per place_id

    for settore in settori_da_cercare:
        risultati = trova_business_settore(citta, settore, max_risultati=40)
        for item in risultati:
            pid = item.get("placeId") or item.get("id") or item.get("title")
            if pid and pid not in visti:
                item["settore_cercato"] = settore
                tutti.append(item)
                visti.add(pid)

    print(f"[AI-IMPL] Totale business unici trovati: {len(tutti)}")
    return tutti


def _avvia_run(payload: dict) -> str:
    resp = requests.post(
        f"{APIFY_BASE}/acts/{ACTOR_GOOGLE_MAPS}/runs",
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
