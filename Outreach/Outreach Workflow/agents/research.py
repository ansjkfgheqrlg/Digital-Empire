"""
Research Agent — Team DEEP-INTEL (Sub-Agent A)
Visita il sito del lead e estrae intelligence strutturata senza AI.
Pure requests + BeautifulSoup — veloce, zero costo API.

Output: website_intelligence con:
  - meta (title, description)
  - headings (H1, H2)
  - CTA presenti
  - social proof signals
  - contatti visibili
  - CRO signals (form, booking, mobile, velocità)
"""

import re
import time
import requests
from bs4 import BeautifulSoup


_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
_TIMEOUT = 8

_CTA_KEYWORDS = {
    "contattaci", "prenota", "prenota ora", "prenota subito", "richiedi", "richiedi preventivo",
    "scopri", "inizia", "prova", "iscriviti", "registrati", "acquista", "compra", "clicca",
    "scarica", "ottieni", "consulenza", "chiama", "invia", "mandaci", "get started",
    "free", "gratis", "gratuito", "senza impegno", "prova gratis",
}

_SOCIAL_PROOF_KEYWORDS = [
    "recensioni", "testimonianze", "clienti soddisfatti", "cosa dicono", "dicono di noi",
    "risultati", "casi di successo", "lavori realizzati", "portfolio", "le nostre recensioni",
    "certificazioni", "premi", "riconoscimenti", "anni di esperienza", "anni di attività",
    "clienti serviti", "oltre", "più di", "partner",
]

_BOOKING_KEYWORDS = [
    "prenota online", "prenotazione online", "book online", "prenota il tuo",
    "calendly", "cal.com", "doodle", "mindbody", "treatwell", "doctolib",
    "prenota una sessione", "scegli la data",
]


class ResearchAgent:
    """
    Sub-Agent A del Team DEEP-INTEL.
    Scrapa il sito del lead ed estrae intelligence CRO rule-based.
    Non richiede AI — opera su HTML grezzo.
    """

    def __init__(self, timeout: int = _TIMEOUT):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(_HEADERS)

    # ──────────────────────────────────────────────────────────────────────
    # Fetch + parse
    # ──────────────────────────────────────────────────────────────────────

    def _fetch(self, url: str) -> tuple:
        """Returns (BeautifulSoup, load_time_seconds) or (None, 0) on failure."""
        try:
            t0 = time.time()
            resp = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            load_time = round(time.time() - t0, 2)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                return soup, load_time
        except Exception:
            pass
        return None, 0

    @staticmethod
    def _normalize(url: str) -> str:
        if not url:
            return ""
        url = url.strip().lower()
        # Scarta placeholder non-URL
        if url in ("nessuno", "none", "n/a", "na", "-", "no"):
            return ""
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        # Scarta domini fasulli (nessun punto nel hostname)
        from urllib.parse import urlparse
        host = urlparse(url).netloc or urlparse(url).path
        if "." not in host:
            return ""
        return url.rstrip("/")

    # ──────────────────────────────────────────────────────────────────────
    # Extractors (rule-based)
    # ──────────────────────────────────────────────────────────────────────

    @staticmethod
    def _extract_meta(soup: BeautifulSoup) -> dict:
        title = soup.find("title")
        desc = (
            soup.find("meta", attrs={"name": "description"})
            or soup.find("meta", property="og:description")
        )
        return {
            "title": title.get_text(strip=True) if title else "",
            "description": desc.get("content", "").strip()[:200] if desc else "",
        }

    @staticmethod
    def _extract_headings(soup: BeautifulSoup) -> dict:
        return {
            "h1": [h.get_text(strip=True) for h in soup.find_all("h1")][:3],
            "h2": [h.get_text(strip=True) for h in soup.find_all("h2")][:5],
        }

    @staticmethod
    def _extract_ctas(soup: BeautifulSoup) -> list:
        found = []
        for tag in soup.find_all(["a", "button"]):
            txt = tag.get_text(strip=True).lower()
            if len(txt) < 60 and any(kw in txt for kw in _CTA_KEYWORDS):
                found.append(tag.get_text(strip=True))
        return list(dict.fromkeys(found))[:8]  # dedup, max 8

    @staticmethod
    def _social_proof(soup: BeautifulSoup) -> dict:
        text = soup.get_text(" ", strip=True).lower()
        found = [kw for kw in _SOCIAL_PROOF_KEYWORDS if kw in text]
        has_stars = bool(soup.find_all(class_=re.compile(r"star|rating|review", re.I)))
        # Check for Google/TripAdvisor review widgets
        has_widget = bool(soup.find_all("iframe", src=re.compile(r"google|trustpilot|tripadvisor", re.I)))
        score = min(len(found) * 2 + (3 if has_stars else 0) + (2 if has_widget else 0), 10)
        return {
            "keywords": found[:5],
            "has_star_ratings": has_stars,
            "score": score,
        }

    @staticmethod
    def _contact_info(soup: BeautifulSoup) -> dict:
        text = soup.get_text(" ")
        phone = re.search(
            r"(\+39\s?)?0?\d{2,4}[\s\-\.]?\d{6,8}|\d{3}[\s\-]?\d{3}[\s\-]?\d{4}",
            text
        )
        email_match = re.search(
            r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b", text
        )
        return {
            "phone": phone.group(0).strip() if phone else None,
            "email_on_page": bool(email_match),
            "whatsapp": "whatsapp" in text.lower(),
        }

    @staticmethod
    def _has_form(soup: BeautifulSoup) -> bool:
        for form in soup.find_all("form"):
            if len(form.find_all(["input", "textarea"])) >= 2:
                return True
        return False

    @staticmethod
    def _has_mobile(soup: BeautifulSoup) -> bool:
        return bool(soup.find("meta", attrs={"name": "viewport"}))

    @staticmethod
    def _has_booking(soup: BeautifulSoup) -> bool:
        text = soup.get_text(" ", strip=True).lower()
        return any(kw in text for kw in _BOOKING_KEYWORDS)

    # ──────────────────────────────────────────────────────────────────────
    # Public interface
    # ──────────────────────────────────────────────────────────────────────

    def analyze(self, lead: dict) -> dict:
        """
        Fetch + analyze lead website.
        Returns lead enriched with 'website_intelligence' key.
        """
        url = self._normalize(lead.get("website", ""))
        nome = lead.get("page_name", "?")

        if not url:
            return {**lead, "website_intelligence": {"available": False, "reason": "no_website"}}

        soup, load_time = self._fetch(url)
        if soup is None:
            print(f"[RESEARCH] {nome}: sito non raggiungibile ({url})")
            return {**lead, "website_intelligence": {"available": False, "reason": "fetch_failed", "url": url}}

        meta      = self._extract_meta(soup)
        headings  = self._extract_headings(soup)
        ctas      = self._extract_ctas(soup)
        sp        = self._social_proof(soup)
        contact   = self._contact_info(soup)
        has_form  = self._has_form(soup)
        has_mob   = self._has_mobile(soup)
        has_book  = self._has_booking(soup)

        # Rule-based CRO flags
        cro_flags = {
            "no_cta":              len(ctas) == 0,
            "weak_social_proof":   sp["score"] < 4,
            "no_contact_form":     not has_form,
            "no_phone":            not contact["phone"],
            "no_mobile_viewport":  not has_mob,
            "slow_load":           load_time > 3.5,
            "missing_meta_desc":   len(meta["description"]) < 50,
            "no_booking_system":   not has_book,
            "no_h1":               len(headings["h1"]) == 0,
        }
        issues = [k for k, v in cro_flags.items() if v]

        intel = {
            "available": True,
            "url": url,
            "load_time_s": load_time,
            "meta": meta,
            "headings": headings,
            "ctas": ctas,
            "social_proof": sp,
            "contact": contact,
            "has_form": has_form,
            "has_mobile": has_mob,
            "has_booking": has_book,
            "cro_flags": cro_flags,
            "issues": issues,
            "issues_count": len(issues),
        }

        print(f"[RESEARCH] {nome}: {len(issues)} problemi CRO, load={load_time}s")
        return {**lead, "website_intelligence": intel}

    def run(self, leads: list) -> list:
        print(f"\n[RESEARCH] Analisi siti per {len(leads)} lead...")
        results = []
        for lead in leads:
            results.append(self.analyze(lead))
            time.sleep(0.4)
        n_ok = sum(1 for r in results if r.get("website_intelligence", {}).get("available"))
        print(f"[RESEARCH] Completato: {n_ok}/{len(leads)} siti analizzati con successo")
        return results
