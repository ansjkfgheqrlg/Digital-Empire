"""
Analisi della qualità di un sito web e calcolo del Funnel Score.

Input: URL del sito web da analizzare
Output: dizionario con score (0-100), breakdown penalità, dati tecnici
"""

import re
import time
import requests
from bs4 import BeautifulSoup
from typing import Optional
import logging

logger = logging.getLogger(__name__)

TIMEOUT_HTTP = 10  # secondi
USER_AGENT = "Mozilla/5.0 (compatible; OutreachAgent/1.0)"


def verifica_sito_attivo(url: str) -> dict:
    """
    Verifica se un sito web è attivo e raggiungibile.

    Args:
        url: URL del sito da verificare (con o senza https://)

    Returns:
        dict con chiavi: attivo (bool), status_code (int), errore (str|None)
    """
    if not url.startswith("http"):
        url = f"https://{url}"

    risultato = {"attivo": False, "status_code": None, "url_finale": url, "errore": None}

    try:
        risposta = requests.get(
            url,
            timeout=TIMEOUT_HTTP,
            headers={"User-Agent": USER_AGENT},
            allow_redirects=True
        )
        risultato["status_code"] = risposta.status_code
        risultato["url_finale"] = risposta.url
        risultato["attivo"] = risposta.status_code < 400

        # Sito "vuoto" (parking page o costruzione)
        if risposta.status_code == 200:
            contenuto = risposta.text
            if len(contenuto.strip()) < 500:
                risultato["attivo"] = False
                risultato["errore"] = "Pagina quasi vuota (possibile domain parking)"
            elif any(x in contenuto.lower() for x in ["coming soon", "under construction", "in costruzione", "sito in allestimento"]):
                risultato["attivo"] = False
                risultato["errore"] = "Sito in costruzione"

    except requests.exceptions.Timeout:
        risultato["errore"] = "Timeout"
    except requests.exceptions.ConnectionError:
        risultato["errore"] = "Connessione rifiutata"
    except requests.exceptions.RequestException as e:
        risultato["errore"] = str(e)

    return risultato


def analizza_html_funnel(url: str) -> dict:
    """
    Analizza la struttura HTML di una landing page per valutare la qualità del funnel.

    Args:
        url: URL della landing page da analizzare

    Returns:
        dict con penalità rilevate e punteggi parziali
    """
    penalita = {}
    dati = {
        "ha_h1": False,
        "ha_form": False,
        "ha_cta": False,
        "ha_testimonianze": False,
        "ha_telefono": False,
        "ha_garanzia": False,
        "ha_pixel_fb": False,
        "ha_analytics": False,
        "testo_h1": ""
    }

    try:
        risposta = requests.get(
            url,
            timeout=TIMEOUT_HTTP,
            headers={"User-Agent": USER_AGENT},
            allow_redirects=True
        )
        if risposta.status_code >= 400:
            return {"penalita": {}, "dati": dati, "errore": f"HTTP {risposta.status_code}"}

        soup = BeautifulSoup(risposta.text, "html.parser")
        html_lower = risposta.text.lower()

        # H1 presente e non generico
        h1_tags = soup.find_all("h1")
        if h1_tags:
            h1_testo = h1_tags[0].get_text(strip=True)
            dati["testo_h1"] = h1_testo
            if len(h1_testo) > 10:
                dati["ha_h1"] = True

        if not dati["ha_h1"]:
            penalita["no_headline"] = -15

        # Form di contatto o opt-in
        forms = soup.find_all("form")
        input_email = soup.find_all("input", {"type": "email"})
        if forms or input_email:
            dati["ha_form"] = True

        if not dati["ha_form"]:
            penalita["no_form_optin"] = -15

        # CTA (call to action)
        cta_keywords = ["contattaci", "prenota", "chiama", "scopri", "inizia", "iscriviti",
                        "richiedi", "scarica", "acquista", "prenota", "consulenza gratuita",
                        "clicca qui", "inizia ora", "chiamaci", "registrati"]
        buttons = soup.find_all(["button", "a"])
        testo_buttons = " ".join([b.get_text(strip=True).lower() for b in buttons])

        if any(kw in testo_buttons for kw in cta_keywords):
            dati["ha_cta"] = True

        if not dati["ha_cta"]:
            penalita["no_cta"] = -10

        # Testimonianze / social proof
        social_proof_keywords = ["recensione", "testimonianza", "clienti soddisfatti", "stella",
                                 "review", "rating", "★", "⭐", "5/5", "ottimo servizio"]
        if any(kw in html_lower for kw in social_proof_keywords):
            dati["ha_testimonianze"] = True

        if not dati["ha_testimonianze"]:
            penalita["no_social_proof"] = -10

        # Numero di telefono
        tel_pattern = r"(\+39|0039)?[\s\-\.]?0?[0-9]{2,4}[\s\-\.]?[0-9]{6,8}"
        if re.search(tel_pattern, risposta.text):
            dati["ha_telefono"] = True

        if not dati["ha_telefono"]:
            penalita["no_telefono"] = -5

        # Garanzia o policy
        garanzia_keywords = ["garanzia", "soddisfatti o rimborsati", "rimborso", "privacy policy",
                             "termini e condizioni", "cookie policy"]
        if any(kw in html_lower for kw in garanzia_keywords):
            dati["ha_garanzia"] = True

        if not dati["ha_garanzia"]:
            penalita["no_garanzia"] = -5

        # Pixel Facebook
        if "fbq(" in html_lower or "facebook.net/en_us/fbevents" in html_lower:
            dati["ha_pixel_fb"] = True

        if not dati["ha_pixel_fb"]:
            penalita["no_pixel_fb"] = -5

        # Google Analytics / GTM
        if "gtag(" in html_lower or "googletagmanager" in html_lower or "google-analytics" in html_lower:
            dati["ha_analytics"] = True

        if not dati["ha_analytics"]:
            penalita["no_analytics"] = -5

    except Exception as e:
        return {"penalita": {}, "dati": dati, "errore": str(e)}

    return {"penalita": penalita, "dati": dati, "errore": None}


def calcola_funnel_score(url: str) -> dict:
    """
    Calcola il Funnel Score completo per una landing page (solo analisi HTML).

    Score iniziale: 100. Vengono sottratte penalità per ogni problema trovato.
    Score <= 60 indica un funnel migliorabile (lead qualificato).

    Args:
        url: URL della landing page

    Returns:
        dict con: score_finale (int), breakdown_penalita (dict), dati_analisi (dict)
    """
    score = 100
    tutte_penalita = {}

    # Analisi HTML
    analisi_html = analizza_html_funnel(url)
    if analisi_html.get("errore"):
        logger.warning(f"Errore analisi HTML per {url}: {analisi_html['errore']}")
        if "HTTP" in str(analisi_html.get("errore", "")):
            return {
                "score_finale": 0,
                "breakdown_penalita": {"pagina_irraggiungibile": -100},
                "dati_analisi": {},
                "errore": analisi_html["errore"]
            }
    else:
        tutte_penalita.update(analisi_html["penalita"])

    # Calcola score finale
    for penalita_valore in tutte_penalita.values():
        score += penalita_valore  # I valori sono negativi

    score = max(0, min(100, score))  # Clamp tra 0 e 100

    # Descrizione testuale dei problemi principali
    descrizione_problemi = []
    mappa_descrizioni = {
        "no_headline": "manca headline chiaro",
        "no_form_optin": "nessun form di contatto",
        "no_cta": "nessuna call-to-action",
        "no_social_proof": "nessuna testimonianza",
        "no_telefono": "nessun telefono visibile",
        "no_garanzia": "nessuna garanzia/policy",
        "no_pixel_fb": "nessun Pixel Facebook",
        "no_analytics": "nessun Analytics",
        "pagespeed_pessimo": "sito molto lento",
        "pagespeed_basso": "sito lento",
        "caricamento_lento": "caricamento > 5 secondi",
        "pagina_irraggiungibile": "pagina non raggiungibile"
    }

    for chiave, _ in tutte_penalita.items():
        if chiave in mappa_descrizioni:
            descrizione_problemi.append(mappa_descrizioni[chiave])

    return {
        "score_finale": score,
        "breakdown_penalita": tutte_penalita,
        "problemi_descrizione": ", ".join(descrizione_problemi[:3]),  # Max 3 per l'email
        "dati_analisi": analisi_html.get("dati", {}),
        "errore": None
    }
