# -*- coding: utf-8 -*-
"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE
Governo: MANDATO Art.8 + ADR-008

Website quality checker and priority assignment module.
"""
from __future__ import annotations

import logging
import time
import requests
from typing import Dict

log = logging.getLogger("preventa-pw.checker")

HEADERS_WEBSITE = {"User-Agent": "Mozilla/5.0 PreventaBot/1.0"}

def check_website_quality(url: str) -> Dict:
    if not url:
        return {"ha_sito": False, "ha_pixel": False, "ha_gtm": False, "vecchio": True, "note": "Nessun sito", "https": False}
    res = {"ha_sito": True, "ha_pixel": False, "ha_gtm": False, "ha_ads": False, "vecchio": False, "https": url.startswith("https://"), "note": ""}
    try:
        t0 = time.time()
        r = requests.get(url, headers=HEADERS_WEBSITE, timeout=10, allow_redirects=True)
        html = r.text.lower()
        if time.time() - t0 > 4:
            res["note"] += "Sito lento. "
        if "fbevents.js" in html or "fbq(" in html or "connect.facebook.net" in html:
            res["ha_pixel"] = True
        if "googletagmanager.com" in html or "gtag(" in html or "google-analytics.com" in html:
            res["ha_gtm"] = True
        if "doubleclick.net" in html or "adsbygoogle" in html:
            res["ha_ads"] = True

        vecchio_score = 0
        if not res["https"]: vecchio_score += 2
        if "copyright 201" in html or "© 201" in html: vecchio_score += 1
        if "joomla" in html or "frontpage" in html: vecchio_score += 1
        if len(html) < 8000: vecchio_score += 1
        if "under construction" in html or "sito in manutenzione" in html or "costruzione" in html: vecchio_score += 2
        if vecchio_score >= 2:
            res["vecchio"] = True
            res["note"] += f"Sito scarso/vecchio score {vecchio_score}. "
        if not res["ha_pixel"] and not res["ha_gtm"]:
            res["note"] += "Nessun pixel/tracking (probabile no campagne). "
    except Exception as e:
        res["note"] += f"Err check sito {e}. "
        res["vecchio"] = True
    return res

def calcola_priorita(row: Dict, site_check: Dict) -> tuple[str, str]:
    ha_sito = row.get("ha_sito", False)
    num = int(row.get("numero_recensioni") or 0)
    media = float(row.get("media_recensioni") or 0)

    if not ha_sito:
        return ("ALTA", "Senza sito web - priorità massima. Pitch modernizzazione.")
    if site_check.get("vecchio"):
        return ("ALTA", f"Sito vecchio/scarso. {site_check.get('note','')}")
    if num < 10:
        return ("ALTA", f"Poche recensioni ({num}) - attività poco digitalizzata.")
    if not site_check.get("ha_pixel") and not site_check.get("ha_gtm"):
        return ("MEDIA", "Sito ok ma no pixel/GTM -> probabile no ads attive.")
    if num < 25 or media < 4.0:
        return ("MEDIA", f"Base debole: {num} rec, media {media}.")
    return ("BASSA", "Strutturato: sito moderno + recensioni alte + tracking.")

import concurrent.futures

def qualify_leads_parallel(leads: list[dict], max_workers: int = 10) -> list[dict]:
    """Qualifica in parallelo una lista di lead usando un pool di thread."""
    def check_and_qualify(row: dict) -> dict:
        sito = row.get("sito_web", "")
        site_check = check_website_quality(sito)
        row["ha_sito"] = bool(sito) and site_check.get("ha_sito", True)
        row["ha_ads_attive"] = bool(site_check.get("ha_pixel") or site_check.get("ha_gtm") or site_check.get("ha_ads"))
        prio, note = calcola_priorita(row, site_check)
        row["priorita_lead"] = prio
        row["note_qualifica"] = note
        return row

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(check_and_qualify, leads))
    return results
