"""
Google Maps Browser Scraper — Digital Empire Outreach
Usa Playwright con sessione browser persistente (come se fossi tu).

VANTAGGI rispetto alle API:
- Zero costi API
- Zero blocchi (Google non vede bot, vede un utente Chrome)
- Nessun limite mensile
- Estrae email, sito, telefono direttamente dalla scheda Maps

PRIMO AVVIO (una volta sola):
    python -m playwright install chromium
    python agents/maps_browser_scraper.py --login
    # Si apre Chrome → fai login con il tuo account Google → chiudi
    # La sessione viene salvata in maps_session/

UTILIZZO NORMALE (dopo il login):
    # Viene chiamato automaticamente dall'orchestratore
    # Oppure manuale: python agents/maps_browser_scraper.py --query "fisioterapista Milano" --n 20
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

SCRAPE_CHECKPOINT = Path(__file__).parent.parent / "scrape_checkpoint.json"

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Aggiunge la cartella padre al path — funziona sia con `python agents/...` che come modulo
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.scraper import SETTORI, CITTA
from utils.printer import scraping_header, scraping_query, scraping_risultato, scraping_done

SESSION_DIR = Path(__file__).parent.parent / "maps_session"
MAPS_URL    = "https://www.google.com/maps"


def _setup_playwright():
    """Import playwright lazy — non crasha se non installato."""
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        raise RuntimeError(
            "Playwright non installato. Esegui:\n"
            "  pip install playwright\n"
            "  python -m playwright install chromium"
        )


class MapsBrowserScraper:
    """
    Naviga Google Maps come un utente reale usando sessione browser salvata.

    Interfaccia identica agli altri scraper:
    Input:  target (int), paese (str)
    Output: list[dict] {page_id, page_name, website, settore, citta, email_diretta?}
    """

    SCROLL_PAUSE   = 2.0   # secondi tra scroll nella lista risultati
    DETAIL_PAUSE   = 2.0   # secondi prima di estrarre la scheda dettaglio
    QUERY_PAUSE    = 12.0  # secondi tra query diverse (basso = Google blocca)

    def __init__(self):
        self.sync_playwright = _setup_playwright()

    # ─── Login (solo prima volta) ─────────────────────────────────────────────

    def login_interattivo(self):
        """
        Apre Chrome in modalità visibile per il login manuale.
        Salva la sessione in maps_session/ — non serve più dopo.
        """
        SESSION_DIR.mkdir(exist_ok=True)
        sync_playwright = self.sync_playwright

        print("\n[MAPS] Apertura Chrome per login Google...")
        print("[MAPS] Accedi con il tuo account → poi chiudi il browser")
        print("[MAPS] La sessione verrà salvata automaticamente.\n")

        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=str(SESSION_DIR),
                headless=False,
                args=["--disable-blink-features=AutomationControlled"],
                locale="it-IT",
            )
            page = browser.new_page()
            page.goto("https://accounts.google.com")
            print("[MAPS] Browser aperto. Fai login e poi chiudi la finestra.")
            # Aspetta che l'utente chiuda il browser
            try:
                browser.wait_for_event("close", timeout=300_000)
            except Exception:
                pass
            browser.close()

        print("[MAPS] Sessione salvata in maps_session/")
        print("[MAPS] Ora puoi usare il scraper normalmente.\n")

    # ─── Estrazione dati da scheda Maps ──────────────────────────────────────

    def _estrai_email(self, testo: str) -> str:
        """Cerca email nel testo della pagina con regex."""
        pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
        trovate = re.findall(pattern, testo)
        # Filtra email di sistema Google
        trovate = [e for e in trovate if "google" not in e.lower()
                   and "gstatic" not in e.lower() and "schema" not in e.lower()]
        return trovate[0] if trovate else ""

    def _estrai_sito(self, page) -> str:
        """Estrae il sito web dalla scheda dettaglio Maps."""
        try:
            # Link "Sito web" nella scheda
            sito_link = page.locator('a[data-item-id="authority"]').first
            if sito_link.count() > 0:
                href = sito_link.get_attribute("href", timeout=3000)
                if href and href.startswith("http"):
                    # Google Maps usa redirect, estrai URL reale
                    if "google.com/url" in href:
                        match = re.search(r"url=([^&]+)", href)
                        if match:
                            from urllib.parse import unquote
                            return unquote(match.group(1))
                    return href
        except Exception:
            pass

        # Fallback: cerca link nel testo aria
        try:
            links = page.locator('a[href^="http"]:not([href*="google"])').all()
            for link in links[:5]:
                href = link.get_attribute("href", timeout=1000)
                if href and "google" not in href.lower() and "maps" not in href.lower():
                    return href
        except Exception:
            pass
        return ""

    def _estrai_scheda(self, page, nome: str) -> dict:
        """Estrae nome, sito, email, telefono dalla scheda aperta."""
        time.sleep(self.DETAIL_PAUSE)
        testo = page.inner_text("body")

        sito  = self._estrai_sito(page)
        email = self._estrai_email(testo)

        # Telefono
        tel = ""
        try:
            tel_el = page.locator('[data-item-id^="phone"]').first
            if tel_el.count() > 0:
                tel = tel_el.inner_text(timeout=2000).strip()
        except Exception:
            pass

        return {
            "page_id":   f"maps_{nome[:40].replace(' ', '_')}_{int(time.time())}",
            "page_name": nome,
            "website":   sito,
            "email_diretta": email,
            "telefono":  tel,
        }

    # ─── Ricerca e scroll lista Maps ─────────────────────────────────────────

    def _accetta_cookie(self, page) -> None:
        """Accetta il banner cookie/consenso Google se presente."""
        try:
            # Banner consenso EU
            for selector in [
                'button:has-text("Accetta tutto")',
                'button:has-text("Accept all")',
                'button:has-text("Acconsento")',
                'form[action*="consent"] button',
            ]:
                btn = page.locator(selector).first
                if btn.count() > 0:
                    btn.click(timeout=3000)
                    time.sleep(1.0)
                    return
        except Exception:
            pass

    def _cerca_query(self, page, query: str, max_risultati: int = 20) -> list:
        """
        Cerca una query su Google Maps e torna la lista di schede trovate.
        Scrolla fino a max_risultati o fino a quando la lista è esaurita.
        """
        print(f"[MAPS] Cerco: '{query}'")
        try:
            # Naviga direttamente all'URL di ricerca (evita il problema del search box)
            query_url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
            page.goto(query_url, timeout=30_000)
            page.wait_for_load_state("domcontentloaded", timeout=20_000)
            time.sleep(2.5)

            # Accetta cookie/consenso se presenti
            self._accetta_cookie(page)

            # Aspetta lista risultati (div[role="feed"] o lista Places)
            lista_selector = 'div[role="feed"]'
            try:
                page.wait_for_selector(lista_selector, timeout=12_000)
            except Exception:
                # Fallback: a volte Maps mostra direttamente una scheda singola
                print(f"[MAPS]  → nessun feed risultati per '{query}'")
                return []

            risultati = []
            place_visti = set()
            scroll_tentativi = 0
            max_scroll = max_risultati // 5 + 8

            while len(risultati) < max_risultati and scroll_tentativi < max_scroll:
                # Raccogli card visibili nella lista sinistra
                cards = page.locator('a[href*="/maps/place/"]').all()
                nuove_cards = [c for c in cards]

                for card in nuove_cards:
                    try:
                        nome = card.get_attribute("aria-label", timeout=1000) or ""
                        if not nome:
                            nome = card.inner_text(timeout=1000).split("\n")[0].strip()

                        if not nome or nome in place_visti:
                            continue
                        place_visti.add(nome)

                        # Clicca sulla card per aprire la scheda dettaglio
                        card.click(timeout=5000)
                        time.sleep(self.DETAIL_PAUSE)

                        dati = self._estrai_scheda(page, nome)
                        risultati.append(dati)
                        print(f"[MAPS]   ✓ {nome} | sito: {dati.get('website','—')[:50]}")

                        if len(risultati) >= max_risultati:
                            break

                        # Torna alla lista (Back o click sul pannello lista)
                        try:
                            page.go_back(timeout=8_000)
                        except Exception:
                            page.goto(
                                f"https://www.google.com/maps/search/{query.replace(' ', '+')}",
                                timeout=15_000
                            )
                        time.sleep(1.5)

                    except Exception:
                        continue

                # Scrolla in fondo alla lista per caricare altri risultati
                try:
                    feed = page.locator(lista_selector)
                    feed.evaluate("el => el.scrollTop = el.scrollHeight")
                    time.sleep(self.SCROLL_PAUSE)
                    scroll_tentativi += 1
                except Exception:
                    break

            print(f"[MAPS]  → {len(risultati)} schede estratte")
            return risultati

        except Exception as e:
            print(f"[MAPS] Errore query '{query}': {e}")
            return []

    # ─── Run principale ───────────────────────────────────────────────────────

    def run(self, target: int = 200, paese: str = "IT") -> list:
        """
        Raccoglie business italiani da Google Maps via browser sessione.

        Returns:
            list[dict]: {page_id, page_name, website, settore, citta, email_diretta?}
        """
        if not SESSION_DIR.exists():
            raise RuntimeError(
                "Sessione Maps non trovata. Esegui prima:\n"
                "  python agents/maps_browser_scraper.py --login"
            )

        sync_playwright = self.sync_playwright
        risultati  = []
        nomi_visti = set()

        # Carica checkpoint esistente: non sovrascrivere mai una sessione più ricca
        if SCRAPE_CHECKPOINT.exists():
            try:
                _old = json.loads(SCRAPE_CHECKPOINT.read_text(encoding="utf-8"))
                if isinstance(_old, list) and len(_old) > 0:
                    risultati  = _old
                    nomi_visti = {r["page_name"] for r in _old}
                    print(f"[MAPS] Checkpoint caricato: {len(risultati)} business già trovati — continuo da qui")
            except Exception:
                pass

        scraping_header(len(SETTORI), len(CITTA))

        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=str(SESSION_DIR),
                headless=False,         # False = Google non detecta il bot
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--disable-dev-shm-usage",
                    "--no-sandbox",
                    "--window-size=1280,900",
                ],
                locale="it-IT",
            )
            page = browser.new_page()

            # Anti-detection: rimuovi la firma Playwright
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            """)

            for settore in SETTORI:
                if len(risultati) >= target:
                    break

                for citta in CITTA:
                    if len(risultati) >= target:
                        break

                    rimasti = target - len(risultati)
                    per_query = min(rimasti, 20)

                    scraping_query(settore, citta, len(risultati), target)
                    query    = f"{settore} {citta}"
                    estratti = self._cerca_query(page, query, max_risultati=per_query)
                    nuovi    = 0

                    for item in estratti:
                        nome = item["page_name"]
                        if nome in nomi_visti:
                            continue
                        nomi_visti.add(nome)

                        entry = {
                            "page_id":   item["page_id"],
                            "page_name": nome,
                            "website":   item.get("website", ""),
                            "settore":   settore,
                            "citta":     citta,
                        }
                        email = item.get("email_diretta", "")
                        if email:
                            entry["email_diretta"] = email

                        risultati.append(entry)
                        nuovi += 1

                    scraping_risultato(nuovi, settore, citta)

                    # Checkpoint ogni 25 lead — non si perdono più se crasha
                    if len(risultati) % 25 == 0 and risultati:
                        with open(SCRAPE_CHECKPOINT, "w", encoding="utf-8") as _f:
                            json.dump(risultati, _f, ensure_ascii=False)

                    time.sleep(self.QUERY_PAUSE)

            browser.close()

        con_email = sum(1 for r in risultati if r.get("email_diretta"))
        scraping_done(len(risultati), con_email, len(risultati))
        return risultati


# ─── CLI per setup e test ──────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Maps Browser Scraper")
    parser.add_argument("--login", action="store_true",
                        help="Apri Chrome per login manuale (solo prima volta)")
    parser.add_argument("--query", type=str, default="",
                        help="Query di test, es: 'fisioterapista Milano'")
    parser.add_argument("--n", type=int, default=10,
                        help="Numero massimo di risultati (default: 10)")
    args = parser.parse_args()

    scraper = MapsBrowserScraper()

    if args.login:
        scraper.login_interattivo()

    elif args.query:
        from playwright.sync_api import sync_playwright as sp
        print(f"\nTest query: '{args.query}' — max {args.n} risultati\n")
        with sp() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=str(SESSION_DIR),
                headless=False,   # visibile durante il test — puoi vedere cosa fa
                args=["--disable-blink-features=AutomationControlled"],
                locale="it-IT",
            )
            page = browser.new_page()
            page.add_init_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
            )
            risultati = scraper._cerca_query(page, args.query, max_risultati=args.n)
            browser.close()

        print("\nRisultati:")
        for r in risultati:
            print(f"  {r['page_name']} | sito: {r.get('website','—')} | email: {r.get('email_diretta','—')}")

    else:
        print("Usa --login per il primo setup, o --query 'testo' per testare.")
        print("Esempio: python agents/maps_browser_scraper.py --login")
