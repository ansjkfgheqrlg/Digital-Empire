"""
Site Analyzer — Sub-agent CRO-Funnel
Analizza un sito web e calcola uno score CRO/funnel.
"""

import re
import requests
import time
from bs4 import BeautifulSoup


HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AgencyBot/1.0)"}


def analizza_sito(url: str) -> dict:
    """
    Analizza il sito e ritorna un dizionario con:
    - score_funnel (0-100, più basso = peggio = lead migliore per noi)
    - problemi: lista di problemi trovati
    - opportunita: lista di opportunità
    """
    if not url.startswith("http"):
        url = "https://" + url

    risultato = {
        "url": url,
        "score_funnel": 100,
        "problemi": [],
        "opportunita": [],
        "tempo_caricamento": None,
        "ha_cta": False,
        "ha_form_contatto": False,
        "ha_social_proof": False,
        "ha_chat": False,
        "mobile_friendly": None,
    }

    try:
        inizio = time.time()
        resp = requests.get(url, headers=HEADERS, timeout=10)
        risultato["tempo_caricamento"] = round(time.time() - inizio, 2)
        soup = BeautifulSoup(resp.text, "html.parser")
        testo = soup.get_text(separator=" ").lower()
        html = resp.text.lower()
    except Exception as e:
        risultato["problemi"].append(f"Sito non raggiungibile: {e}")
        risultato["score_funnel"] = 0
        return risultato

    # Penalità e analisi
    penalita = 0

    # 1. Velocità di caricamento
    if risultato["tempo_caricamento"] > 4:
        penalita += 20
        risultato["problemi"].append(f"Caricamento lento: {risultato['tempo_caricamento']}s (ideale <2s)")
        risultato["opportunita"].append("Ottimizzazione velocità pagina (CDN, caching, compressione immagini)")
    elif risultato["tempo_caricamento"] > 2:
        penalita += 10
        risultato["problemi"].append(f"Caricamento medio: {risultato['tempo_caricamento']}s")

    # 2. CTA above the fold
    cta_keywords = ["contattaci", "richiedi", "prenota", "chiama", "scopri", "inizia", "acquista", "compra", "iscriviti"]
    ha_cta = any(kw in testo[:2000] for kw in cta_keywords)
    risultato["ha_cta"] = ha_cta
    if not ha_cta:
        penalita += 20
        risultato["problemi"].append("Nessuna CTA chiara above the fold")
        risultato["opportunita"].append("Aggiungere CTA principale visibile subito")

    # 3. Form di contatto
    ha_form = bool(soup.find("form")) or "contattaci" in testo or "contact" in html
    risultato["ha_form_contatto"] = ha_form
    if not ha_form:
        penalita += 15
        risultato["problemi"].append("Nessun form di contatto trovato")
        risultato["opportunita"].append("Aggiungere form di contatto o pagina dedicata")

    # 4. Social proof (recensioni, testimonianze)
    social_proof_kw = ["recensioni", "testimonianze", "clienti soddisfatti", "casi studio", "stelle", "⭐", "★"]
    ha_social_proof = any(kw in testo for kw in social_proof_kw)
    risultato["ha_social_proof"] = ha_social_proof
    if not ha_social_proof:
        penalita += 15
        risultato["problemi"].append("Nessuna prova sociale (testimonianze, recensioni)")
        risultato["opportunita"].append("Aggiungere sezione testimonianze/recensioni Google")

    # 5. Live chat o chatbot
    chat_kw = ["livechat", "tawk.to", "intercom", "zendesk", "crisp", "tidio", "hubspot"]
    ha_chat = any(kw in html for kw in chat_kw)
    risultato["ha_chat"] = ha_chat
    if not ha_chat:
        penalita += 10
        risultato["problemi"].append("Nessuna live chat o chatbot")
        risultato["opportunita"].append("Aggiungere chatbot per catturare lead 24/7")

    # 6. Pixel tracking
    ha_pixel = "fbq(" in html or "gtag(" in html or "google-analytics" in html
    if not ha_pixel:
        penalita += 10
        risultato["problemi"].append("Nessun pixel di tracking (Facebook/Google Analytics)")
        risultato["opportunita"].append("Installare pixel Facebook e Google Analytics 4")

    # 7. HTTPS
    if not url.startswith("https"):
        penalita += 10
        risultato["problemi"].append("Sito non HTTPS — penalità SEO e fiducia")

    risultato["score_funnel"] = max(0, 100 - penalita)
    return risultato


def filtra_lead_cro(lista_business: list[dict], soglia_score: int = 60) -> list[dict]:
    """
    Analizza tutti i siti e tieni solo quelli con score_funnel <= soglia.
    Score basso = funnel scarso = opportunità per noi.
    """
    leads_qualificati = []
    print(f"[CRO-FUNNEL] Analisi siti in corso ({len(lista_business)} business)...")

    for b in lista_business:
        url = b.get("website") or b.get("url") or ""
        if not url:
            continue
        analisi = analizza_sito(url)
        b.update(analisi)
        if analisi["score_funnel"] <= soglia_score:
            leads_qualificati.append(b)
            print(f"  [LEAD] {b.get('title', url)} — score funnel: {analisi['score_funnel']}")

    print(f"[CRO-FUNNEL] Lead qualificati (score <={soglia_score}): {len(leads_qualificati)}/{len(lista_business)}")
    return leads_qualificati
