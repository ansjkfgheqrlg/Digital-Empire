# -*- coding: utf-8 -*-
"""
Owner: NERI · Controllore: Emperator Agent · Origine: TASK-PREVENTA-CANALI-W1
Governo: MANDATO Art.8 + ADR-008

Estrae un'email pubblica da un sito web di concessionario, per abilitare il canale
Gmail accanto a WhatsApp (scraper.py cattura gia' `sito_web` ma non `email`).

Nessun login, nessuna sessione da mantenere: solo HTTP + regex/parsing HTML, quindi
niente della fragilita' che ha un motore Playwright (rate limit, captcha, selettori
che cambiano). Se il sito non risponde o non ha email pubblica, ritorna None
onestamente — non e' un errore, e' un dato mancante.
"""
from __future__ import annotations

import re
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

TIMEOUT = 8
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# Pagine tipiche dove i concessionari mettono l'email quando non e' in home.
PATH_CANDIDATI = ["", "contatti", "contatti.html", "contact", "chi-siamo", "azienda"]

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

# Domini di terze parti che finiscono nell'HTML per motivi tecnici, mai l'email vera
# dell'attivita' — scartati per non sporcare i lead con indirizzi inutilizzabili.
DOMINI_SCARTO = (
    "sentry.io", "wixpress.com", "example.com", "godaddy.com", "schema.org",
    "w3.org", "gstatic.com", "google.com", "googleapis.com", "cloudflare.com",
    "wordpress.org", "wp.com",
)
ESTENSIONI_SCARTO = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")


def _pulisci_candidati(testo: str) -> list[str]:
    trovate = EMAIL_RE.findall(testo)
    pulite = []
    for e in trovate:
        e = e.strip().strip(".,;:")
        dominio = e.split("@")[-1].lower()
        if any(d in dominio for d in DOMINI_SCARTO):
            continue
        if any(e.lower().endswith(ext) for ext in ESTENSIONI_SCARTO):
            continue
        pulite.append(e)
    return pulite


def _fetch(url: str) -> Optional[str]:
    try:
        r = requests.get(url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT})
        if r.status_code >= 400:
            return None
        return r.text
    except requests.RequestException:
        return None


def estrai_email_da_sito(sito_web: str) -> Optional[str]:
    """Prova la homepage e un pugno di pagine contatti tipiche. Ritorna la prima
    email pubblica valida trovata, o None se il sito non risponde o non ne ha."""
    if not sito_web or not sito_web.strip():
        return None

    url = sito_web.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"

    visitati = set()
    for path in PATH_CANDIDATI:
        target = urljoin(base + "/", path)
        if target in visitati:
            continue
        visitati.add(target)

        html = _fetch(target)
        if not html:
            continue

        # 1. mailto: espliciti (segnale piu' affidabile, l'autore del sito l'ha messo apposta)
        soup = BeautifulSoup(html, "lxml")
        for a in soup.select('a[href^="mailto:"]'):
            candidato = a["href"].replace("mailto:", "").split("?")[0].strip()
            pulite = _pulisci_candidati(candidato)
            if pulite:
                return pulite[0]

        # 2. regex sul testo pagina (fallback: email scritta come testo semplice)
        pulite = _pulisci_candidati(html)
        if pulite:
            return pulite[0]

    return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python email_extractor.py <url-sito>")
        sys.exit(1)
    risultato = estrai_email_da_sito(sys.argv[1])
    print(risultato or "(nessuna email trovata)")
