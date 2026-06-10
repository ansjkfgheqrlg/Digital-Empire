"""
Estrazione di contatti (email, telefono) da pagine web.

Input: URL sito web, nome business
Output: dict con email e telefono trovati

Non usa API esterne (no Hunter.io): estrae i contatti direttamente
dal sito web del business, cercando su più pagine interne (home,
pagina contatti, chi siamo).
"""

import re
import time
import requests
from bs4 import BeautifulSoup
from typing import Optional
from urllib.parse import urljoin, urlparse
import logging

logger = logging.getLogger(__name__)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)
TIMEOUT_HTTP = 10

# Pattern regex
PATTERN_EMAIL = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PATTERN_TEL_IT = r"(\+39|0039)?[\s\-\.]?0?[0-9]{2,4}[\s\-\.]?[0-9]{3,4}[\s\-\.]?[0-9]{3,4}"

# Prefissi email da escludere (generiche/non utili)
PREFISSI_DA_ESCLUDERE = [
    "noreply", "no-reply", "donotreply", "privacy", "legal",
    "abuse", "spam", "postmaster", "webmaster", "mailer",
    "support@sentry", "example@", "test@", "admin@",
    "unsubscribe", "bounce",
]

# Testi link che portano alla pagina contatti
LINK_CONTATTI_KEYWORDS = [
    "contatti", "contact", "contattaci", "contact us", "dove siamo",
    "chi siamo", "about", "chi-siamo", "contatto", "raggiungici",
]


def _e_email_di_sistema(email: str) -> bool:
    """Restituisce True se l'email è di sistema e non utile per l'outreach."""
    email_lower = email.lower()
    return any(p in email_lower for p in PREFISSI_DA_ESCLUDERE)


def _pulisci_numero(numero_raw) -> Optional[str]:
    """Normalizza e valida un numero di telefono."""
    if isinstance(numero_raw, tuple):
        numero_raw = "".join(numero_raw)
    numero_pulito = re.sub(r"[\s\-\.]", "", str(numero_raw))
    if len(numero_pulito) >= 8:
        return numero_pulito
    return None


def _scarica_pagina(url: str) -> Optional[str]:
    """Scarica il contenuto HTML di una pagina. Restituisce None in caso di errore."""
    try:
        risposta = requests.get(
            url,
            timeout=TIMEOUT_HTTP,
            headers={"User-Agent": USER_AGENT},
            allow_redirects=True
        )
        if risposta.status_code >= 400:
            return None
        return risposta.text
    except Exception as e:
        logger.debug(f"Errore scaricamento {url}: {e}")
        return None


def _trova_pagine_contatti(url_base: str, html_home: str) -> list:
    """
    Trova gli URL interni della pagina contatti / chi siamo.

    Args:
        url_base: URL della home page
        html_home: HTML della home page già scaricata

    Returns:
        Lista di URL da visitare (max 3)
    """
    url_da_visitare = []
    dominio_base = urlparse(url_base).netloc

    try:
        soup = BeautifulSoup(html_home, "html.parser")
        for link in soup.find_all("a", href=True):
            testo = link.get_text(strip=True).lower()
            href = link["href"]

            if any(k in testo or k in href.lower() for k in LINK_CONTATTI_KEYWORDS):
                url_assoluta = urljoin(url_base, href)
                # Rimani sullo stesso dominio
                if urlparse(url_assoluta).netloc == dominio_base:
                    if url_assoluta not in url_da_visitare and url_assoluta != url_base:
                        url_da_visitare.append(url_assoluta)
                        if len(url_da_visitare) >= 3:
                            break
    except Exception as e:
        logger.debug(f"Errore ricerca pagine contatti: {e}")

    return url_da_visitare


def estrai_email_da_html(url: str) -> list:
    """
    Estrae indirizzi email da una pagina web.

    Cerca anche nei tag <a href="mailto:"> che sono la fonte più affidabile.

    Args:
        url: URL da analizzare

    Returns:
        Lista di email trovate (filtrate e deduplicate, max 5)
    """
    email_trovate = []
    html = _scarica_pagina(url)
    if not html:
        return email_trovate

    # Priorità: mailto: links
    try:
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if href.startswith("mailto:"):
                email = href.replace("mailto:", "").split("?")[0].strip()
                if email and not _e_email_di_sistema(email) and email not in email_trovate:
                    email_trovate.append(email)
    except Exception:
        pass

    # Fallback: regex su tutto il testo HTML
    if not email_trovate:
        email_raw = re.findall(PATTERN_EMAIL, html)
        for email in email_raw:
            if not _e_email_di_sistema(email) and email not in email_trovate:
                email_trovate.append(email)

    return email_trovate[:5]


def estrai_telefono_da_html(url: str) -> Optional[str]:
    """
    Estrae il primo numero di telefono trovato in una pagina web.

    Cerca prioritariamente nei tag <a href="tel:...">.

    Args:
        url: URL da analizzare

    Returns:
        Numero di telefono come stringa, o None
    """
    html = _scarica_pagina(url)
    if not html:
        return None

    try:
        soup = BeautifulSoup(html, "html.parser")

        # Priorità: link tel:
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if href.startswith("tel:"):
                numero = href.replace("tel:", "").strip()
                if numero:
                    return numero

        # Fallback: regex sul testo
        numeri = re.findall(PATTERN_TEL_IT, html)
        if numeri:
            return _pulisci_numero(numeri[0])

    except Exception as e:
        logger.debug(f"Errore estrazione telefono da {url}: {e}")

    return None


def estrai_contatti_business(
    nome_business: str,
    url_sito: Optional[str] = None,
    url_pagina_fb: Optional[str] = None,
) -> dict:
    """
    Funzione principale: estrae tutti i contatti disponibili per un business.

    Strategia (in ordine di priorità):
    1. Home page del sito: cerca mailto: e tel:
    2. Pagine interne (contatti, chi siamo): stessa ricerca
    3. Pagina Facebook: fallback se sito non disponibile

    Args:
        nome_business: Nome del business (usato per log)
        url_sito: URL sito web (opzionale)
        url_pagina_fb: URL pagina Facebook (opzionale)

    Returns:
        dict con chiavi: email (str|None), telefono (str|None),
                         fonte_email (str), fonte_telefono (str)
    """
    risultato = {
        "email": None,
        "telefono": None,
        "fonte_email": "non trovata",
        "fonte_telefono": "non trovata",
    }

    if not url_sito and not url_pagina_fb:
        return risultato

    # --- 1. Analisi home page ---
    if url_sito:
        html_home = _scarica_pagina(url_sito)

        if html_home:
            # Email da home
            email_list = estrai_email_da_html(url_sito)
            if email_list:
                risultato["email"] = email_list[0]
                risultato["fonte_email"] = "sito_home"

            # Telefono da home
            telefono = estrai_telefono_da_html(url_sito)
            if telefono:
                risultato["telefono"] = telefono
                risultato["fonte_telefono"] = "sito_home"

            # --- 2. Pagine interne (se mancano ancora contatti) ---
            if not risultato["email"] or not risultato["telefono"]:
                pagine_contatti = _trova_pagine_contatti(url_sito, html_home)

                for url_interna in pagine_contatti:
                    time.sleep(0.5)  # Pausa cortesia

                    if not risultato["email"]:
                        email_list = estrai_email_da_html(url_interna)
                        if email_list:
                            risultato["email"] = email_list[0]
                            risultato["fonte_email"] = "sito_pagina_contatti"

                    if not risultato["telefono"]:
                        telefono = estrai_telefono_da_html(url_interna)
                        if telefono:
                            risultato["telefono"] = telefono
                            risultato["fonte_telefono"] = "sito_pagina_contatti"

                    if risultato["email"] and risultato["telefono"]:
                        break  # Trovato tutto, stop

    # --- 3. Pagina Facebook (fallback) ---
    if url_pagina_fb and (not risultato["email"] or not risultato["telefono"]):
        logger.debug(f"Cerca contatti su pagina FB: {url_pagina_fb}")
        try:
            if not risultato["email"]:
                email_list = estrai_email_da_html(url_pagina_fb)
                if email_list:
                    risultato["email"] = email_list[0]
                    risultato["fonte_email"] = "pagina_facebook"

            if not risultato["telefono"]:
                telefono = estrai_telefono_da_html(url_pagina_fb)
                if telefono:
                    risultato["telefono"] = telefono
                    risultato["fonte_telefono"] = "pagina_facebook"
        except Exception as e:
            logger.debug(f"Errore accesso pagina FB: {e}")

    logger.info(
        f"{nome_business} — email: {risultato['email'] or 'N/A'} "
        f"({risultato['fonte_email']}), "
        f"tel: {risultato['telefono'] or 'N/A'} ({risultato['fonte_telefono']})"
    )

    return risultato
