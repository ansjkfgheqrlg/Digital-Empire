"""
Outscraper Scraper Agent — Digital Empire Outreach
Usa Outscraper (outscraper.com) per trovare business italiani con email.

Vantaggi vs Google Places / Facebook:
- Restituisce EMAIL direttamente (no email extraction da sito)
- Zero approval process — API key istantanea
- ~$1 per 300 lead (pay per result)
- Python SDK ufficiale: pip install outscraper

Setup (3 min): outscraper.com → Sign up → API Key → metti in .env
"""

import time
from outscraper import ApiClient

from agents.scraper import SETTORI, CITTA


class OutscraperScraper:
    """
    Cerca lead italiani via Outscraper Google Maps API.

    Interfaccia identica a FacebookScraperAgent / GooglePlacesScraper:
    Input:  target (int), paese (str, ignorato — cerca su Google Maps IT)
    Output: list[dict] {page_id, page_name, website, settore, citta, email}

    Bonus: restituisce email direttamente, bypassando EmailExtractorAgent.
    """

    DELAY_TRA_QUERY = 1.0   # secondi — Outscraper gestisce il rate limit internamente
    BATCH_SIZE      = 20    # risultati per query (default Outscraper)

    def __init__(self, api_key: str):
        self.client   = ApiClient(api_key=api_key)
        self.api_key  = api_key

    def _cerca(self, query: str, limite: int = 20) -> list:
        """Chiama Outscraper Google Maps Search — restituisce business con email."""
        try:
            results = self.client.google_maps_search(
                query,
                limit=limite,
                language="it",
                region="IT",
            )
            # Outscraper restituisce lista di liste (una per query)
            if results and isinstance(results[0], list):
                return results[0]
            return results or []

        except Exception as e:
            err = str(e).lower()
            if "quota" in err or "limit" in err or "429" in err:
                print("[SCRAPER] Rate limit Outscraper — attendo 10s...")
                time.sleep(10)
                return self._cerca(query, limite)
            if "unauthorized" in err or "api key" in err or "401" in err:
                print("\n[SCRAPER] API KEY OUTSCRAPER NON VALIDA!")
                print("[SCRAPER] Verifica OUTSCRAPER_API_KEY nel .env")
                print("[SCRAPER] Generala su: outscraper.com → Dashboard → API Key\n")
                raise RuntimeError("OUTSCRAPER_API_KEY_NON_VALIDA")
            print(f"[SCRAPER] Errore Outscraper: {e}")
            return []

    def run(self, target: int = 1000, paese: str = "IT") -> list:
        """
        Raccoglie business italiani da Google Maps via Outscraper.

        Returns:
            list[dict]: {page_id, page_name, website, settore, citta}
            Con extra field 'email' già estratta (bypassa EmailExtractorAgent).
        """
        risultati  = []
        place_visti = set()

        print(f"\n[SCRAPER] Avvio Outscraper — target: {target} business")

        for settore in SETTORI:
            if len(risultati) >= target:
                break

            for citta in CITTA:
                if len(risultati) >= target:
                    break

                query = f"{settore} {citta} Italia"
                print(f"[SCRAPER] Ricerca: '{settore} {citta}' ({len(risultati)}/{target})")

                places = self._cerca(query)
                nuovi_da_query = 0

                for place in places:
                    place_id = place.get("place_id") or place.get("cid") or place.get("name", "")
                    if not place_id or place_id in place_visti:
                        continue
                    place_visti.add(place_id)

                    sito  = place.get("site") or place.get("website") or ""
                    email = place.get("email") or place.get("emails") or ""

                    # Outscraper a volte mette le email in lista
                    if isinstance(email, list):
                        email = email[0] if email else ""

                    # Senza almeno sito o email non è utile
                    if not sito and not email:
                        continue
                    if sito and not sito.startswith("http"):
                        sito = f"https://{sito}"

                    risultati.append({
                        "page_id":   str(place_id),
                        "page_name": place.get("name", ""),
                        "website":   sito,
                        "settore":   settore,
                        "citta":     citta,
                        # Bonus field — usato dall'extractor se presente
                        "email_diretta": email,
                    })
                    nuovi_da_query += 1

                print(f"[SCRAPER]  → {nuovi_da_query} nuovi business. Totale: {len(risultati)}")
                time.sleep(self.DELAY_TRA_QUERY)

        print(f"\n[SCRAPER] Completato: {len(risultati)} business trovati")
        return risultati
