"""
Contact Finder — Sub-agent No-Website
Cerca email e telefono per i lead trovati.
"""

import re
import requests
from bs4 import BeautifulSoup


HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AgencyBot/1.0)"}
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")


def estrai_contatti(business: dict) -> dict:
    """
    Cerca email e telefono per un business.
    Fonti: Google Maps data → scraping pagina contatti del sito (se esiste parzialmente).
    Per no-website, usiamo principalmente i dati Apify.
    """
    email = business.get("email") or None
    telefono = (
        business.get("phone")
        or business.get("phoneUnformatted")
        or None
    )

    # Se Apify ha già i dati, usali direttamente
    if email and telefono:
        business["email_trovata"] = email
        business["telefono_trovato"] = telefono
        business["fonte_contatto"] = "apify"
        return business

    # Tenta scraping social/web links presenti nel profilo Google Maps
    social_links = business.get("socialMediaLinks") or []
    for link in social_links:
        if not email:
            email = _cerca_email_in_pagina(link)

    business["email_trovata"] = email
    business["telefono_trovato"] = telefono
    business["fonte_contatto"] = "apify+scraping" if email else "apify"
    return business


def _cerca_email_in_pagina(url: str) -> str | None:
    """Scarica una pagina e cerca email nel testo."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=8)
        testo = BeautifulSoup(resp.text, "html.parser").get_text()
        match = EMAIL_REGEX.search(testo)
        return match.group(0) if match else None
    except Exception:
        return None


def estrai_contatti_batch(lista_business: list[dict]) -> list[dict]:
    """Estrae contatti per tutti i business della lista."""
    risultati = []
    for b in lista_business:
        b = estrai_contatti(b)
        risultati.append(b)
    # Filtra: tieni SOLO chi ha email valida
    con_email = [b for b in risultati if b.get("email_trovata")]
    print(f"[NO-WEBSITE] Lead con email: {len(con_email)}/{len(risultati)}")
    return con_email
