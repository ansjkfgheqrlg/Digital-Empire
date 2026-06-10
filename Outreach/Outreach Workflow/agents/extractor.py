"""
Email Extractor Agent — Digital Empire Outreach
Motore: Playwright (headless Chrome) + requests fallback.

Strategia di ricerca (in ordine):
1. requests rapido sulla homepage (per siti semplici, fast path)
2. Playwright → homepage renderizzata con JS
3. Playwright → segue link "contatti / contact / chi siamo" nella pagina
4. Playwright → prova URL diretti /contatti /contact /about /info
5. Playwright → cerca nel footer (dove le email si trovano quasi sempre)

Tasso di successo atteso: 65-80% (rispetto al 20-30% del vecchio requests puro).
"""

import re
import time
import socket
import json
import requests
from pathlib import Path
from typing import Optional

EXTRACTOR_CHECKPOINT = Path(__file__).parent.parent / "extractor_checkpoint.json"

socket.setdefaulttimeout(10)

EMAIL_REGEX = re.compile(
    r'\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,7}\b'
)

DOMINI_FINTI = {
    "example.com", "esempio.it", "sentry.io", "googleapis.com",
    "jquery.com", "cloudflare.com", "wixpress.com", "shopify.com",
    "wordpress.com", "squarespace.com", "webflow.io", "godaddy.com",
    "wix.com", "strikingly.com", "weebly.com", "jimdo.com",
    "siteground.com", "aruba.it", "register.it", "email.it",
    "schema.org", "w3.org", "json-ld.org", "mailchimp.com",
    "sendgrid.net", "constantcontact.com", "hubspot.com",
    "formspree.io", "typeform.com", "getresponse.com",
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9,en;q=0.5",
}

# Keyword nei link per trovare la pagina contatti
CONTACT_KEYWORDS = [
    "contatt", "contact", "chi-siam", "about", "chi_siam",
    "info", "scrivici", "reach", "get-in-touch", "trovaci",
    "dove-siam", "headquarters", "support", "help",
]

# Path da provare se non trova link nella pagina
CONTACT_PATHS = [
    "/contatti", "/contattaci", "/contact", "/contact-us",
    "/chi-siamo", "/about", "/about-us", "/info",
    "/informazioni", "/contatti.html", "/contact.html",
    "/contatti.php", "/contattaci.php", "/dove-siamo",
]


class EmailExtractorAgent:
    """
    Estrae email dai siti web con Playwright (JS rendering completo).

    Pattern: requests fast-path → Playwright homepage → Playwright contact page.
    Input:  lista di {page_name, website, ...}
    Output: stessa lista, solo i record con email trovata
    """

    TIMEOUT_REQUESTS = (5, 8)
    DELAY_TRA_SITI   = 0.8
    MAX_FOLLOW_LINKS = 3    # max link contatti da seguire per sito

    def __init__(self):
        self._req_session = requests.Session()
        self._req_session.headers.update(HEADERS)
        self._playwright = None
        self._browser    = None

    # ── Validazione email ────────────────────────────────────────────────────

    def _email_valida(self, email: str) -> bool:
        if not email or "@" not in email:
            return False
        email = email.strip(".,;:\"'<> ")
        dominio = email.split("@")[-1].lower()
        if any(finto in dominio for finto in DOMINI_FINTI):
            return False
        parti = dominio.split(".")
        if len(parti) < 2:
            return False
        if parti[-1] in ("png", "jpg", "gif", "css", "js", "svg", "ico", "woff"):
            return False
        return True

    def _prima_email_valida(self, testo: str) -> Optional[str]:
        """Estrae la prima email valida da un testo/HTML grezzo."""
        matches = EMAIL_REGEX.findall(testo)
        for m in matches:
            m = m.strip(".,;:\"'<> ").lower()
            if self._email_valida(m):
                return m
        return None

    # ── Fast path: requests semplice ────────────────────────────────────────

    def _requests_fast(self, url: str) -> Optional[str]:
        """Prova con requests (niente JS). Veloce ma fallisce su siti moderni."""
        try:
            resp = self._req_session.get(url, timeout=self.TIMEOUT_REQUESTS,
                                         allow_redirects=True)
            if resp.status_code == 200:
                # Cerca mailto: prima
                for m in re.findall(r'mailto:([^"\'>\s?]+)', resp.text):
                    m = m.split("?")[0].strip().lower()
                    if self._email_valida(m):
                        return m
                return self._prima_email_valida(resp.text)
        except Exception:
            pass
        return None

    # ── Playwright: browser headless ────────────────────────────────────────

    def _ensure_browser(self):
        """Avvia Playwright solo se necessario (lazy init)."""
        if self._browser is None:
            try:
                from playwright.sync_api import sync_playwright
                self._playwright = sync_playwright().start()
                self._browser = self._playwright.chromium.launch(
                    headless=True,
                    args=[
                        "--disable-blink-features=AutomationControlled",
                        "--disable-dev-shm-usage",
                        "--no-sandbox",
                    ],
                )
            except Exception as e:
                raise RuntimeError(f"Playwright non disponibile: {e}")

    def _pw_get_text(self, page, url: str, timeout: int = 12000) -> Optional[str]:
        """Naviga a URL con Playwright e restituisce il testo visibile + HTML."""
        try:
            page.goto(url, timeout=timeout, wait_until="domcontentloaded")
            page.wait_for_timeout(1200)  # lascia caricare lazy content
            return page.content()
        except Exception:
            return None

    def _pw_trova_link_contatti(self, page) -> list[str]:
        """Trova link alla pagina contatti nella pagina corrente."""
        try:
            links = page.locator("a[href]").all()
            trovati = []
            for link in links[:80]:
                try:
                    href = link.get_attribute("href", timeout=500) or ""
                    testo = (link.inner_text(timeout=500) or "").lower()
                    href_l = href.lower()
                    # Controlla keyword nell'href o nel testo del link
                    if any(kw in href_l or kw in testo for kw in CONTACT_KEYWORDS):
                        # Normalizza URL relativo → assoluto
                        if href.startswith("http"):
                            trovati.append(href)
                        elif href.startswith("/"):
                            base = page.url.split("/")
                            base_url = f"{base[0]}//{base[2]}"
                            trovati.append(base_url + href)
                except Exception:
                    continue
            # Deduplica mantenendo l'ordine
            seen = set()
            return [u for u in trovati if not (u in seen or seen.add(u))]
        except Exception:
            return []

    def _pw_estrai_da_pagina(self, page, url: str) -> Optional[str]:
        """Naviga a URL con Playwright ed estrae email dal contenuto renderizzato."""
        html = self._pw_get_text(page, url)
        if not html:
            return None

        # 1. Cerca mailto: link (più affidabili)
        for m in re.findall(r'mailto:([^"\'>\s?]+)', html):
            m = m.split("?")[0].strip().lower()
            if self._email_valida(m):
                return m

        # 2. Cerca email nel testo visibile (più pulito dell'HTML grezzo)
        try:
            testo_visibile = page.inner_text("body")
            email = self._prima_email_valida(testo_visibile)
            if email:
                return email
        except Exception:
            pass

        # 3. Cerca nell'HTML grezzo
        return self._prima_email_valida(html)

    def _pw_cerca_nel_footer(self, page) -> Optional[str]:
        """Cerca email specificamente nel footer della pagina."""
        selectors = ["footer", "[id*='footer']", "[class*='footer']",
                     "[id*='contact']", "[class*='contact']",
                     "[id*='bottom']", "[class*='bottom']"]
        for sel in selectors:
            try:
                el = page.locator(sel).first
                if el.count() > 0:
                    testo = el.inner_text(timeout=1000)
                    email = self._prima_email_valida(testo)
                    if email:
                        return email
            except Exception:
                continue
        return None

    # ── Logica principale per singolo sito ──────────────────────────────────

    def _ottieni_email_da_sito(self, url: str) -> Optional[str]:
        url_base = url.rstrip("/")

        # STEP 1: fast path con requests (non pesa su Playwright)
        email = self._requests_fast(url_base)
        if email:
            return email

        # STEP 2: Playwright
        try:
            self._ensure_browser()
        except RuntimeError:
            return None  # Playwright non installato → skip

        ctx  = self._browser.new_context(locale="it-IT")
        page = ctx.new_page()
        page.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
        )

        try:
            # 2a. Homepage renderizzata
            email = self._pw_estrai_da_pagina(page, url_base)
            if email:
                return email

            # 2b. Cerca email nel footer della homepage
            email = self._pw_cerca_nel_footer(page)
            if email:
                return email

            # 2c. Segue link contatti trovati nella homepage
            link_contatti = self._pw_trova_link_contatti(page)
            for link in link_contatti[:self.MAX_FOLLOW_LINKS]:
                if link == url_base or link == url_base + "/":
                    continue
                email = self._pw_estrai_da_pagina(page, link)
                if email:
                    return email
                email = self._pw_cerca_nel_footer(page)
                if email:
                    return email

            # 2d. Prova percorsi contatti standard se non trovati link
            if not link_contatti:
                for path in CONTACT_PATHS[:5]:
                    email = self._pw_estrai_da_pagina(page, url_base + path)
                    if email:
                        return email

        except Exception:
            pass
        finally:
            try:
                ctx.close()
            except Exception:
                pass

        return None

    # ── Cleanup ─────────────────────────────────────────────────────────────

    def _chiudi_browser(self):
        try:
            if self._browser:
                self._browser.close()
            if self._playwright:
                self._playwright.stop()
        except Exception:
            pass
        self._browser    = None
        self._playwright = None

    # ── Interfaccia pubblica ─────────────────────────────────────────────────

    def run(self, businesses: list) -> list:
        """
        Estrae email per ogni business. Restituisce solo i lead con email trovata.
        Salva checkpoint ogni 20 lead — riprende automaticamente se crashato.
        """
        # Carica checkpoint se esiste (resume da crash)
        leads_con_email = []
        processed_count = 0
        if EXTRACTOR_CHECKPOINT.exists():
            try:
                saved = json.loads(EXTRACTOR_CHECKPOINT.read_text(encoding="utf-8"))
                leads_con_email = saved.get("leads", [])
                processed_count = saved.get("processed", 0)
                if processed_count > 0:
                    print(f"\n[EXTRACTOR] Checkpoint trovato: {len(leads_con_email)} email già estratte, "
                          f"riprendo da business {processed_count + 1}...")
            except Exception:
                leads_con_email = []
                processed_count = 0

        businesses_da_fare = businesses[processed_count:]
        totale = len(businesses)

        print(f"\n[EXTRACTOR] Processo {len(businesses_da_fare)} siti (di {totale} totali)...")

        try:
            for i, biz in enumerate(businesses_da_fare, processed_count + 1):
                nome = biz.get("page_name", biz.get("website", "?"))
                sito = biz.get("website", "").strip()

                if not sito:
                    processed_count += 1
                    continue

                if not sito.startswith("http"):
                    sito = "https://" + sito

                print(f"[EXTRACTOR] {i}/{totale}: {nome[:45]}", end=" ", flush=True)

                email = self._ottieni_email_da_sito(sito)

                if email:
                    leads_con_email.append({**biz, "email": email})
                    print(f"-> {email}")
                else:
                    print("-> non trovata")

                processed_count += 1
                time.sleep(self.DELAY_TRA_SITI)

                # Salva checkpoint ogni 20 lead processati
                if processed_count % 20 == 0:
                    EXTRACTOR_CHECKPOINT.write_text(
                        json.dumps({"leads": leads_con_email, "processed": processed_count},
                                   ensure_ascii=False, indent=None),
                        encoding="utf-8"
                    )

        finally:
            self._chiudi_browser()

        # Completato — rimuovi checkpoint
        if EXTRACTOR_CHECKPOINT.exists():
            EXTRACTOR_CHECKPOINT.unlink()

        tasso = len(leads_con_email) / max(totale, 1) * 100
        print(f"\n[EXTRACTOR] Email trovate: {len(leads_con_email)}/{totale} ({tasso:.0f}%)")
        return leads_con_email
