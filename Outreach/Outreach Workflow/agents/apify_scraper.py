"""
Apify Scraper Agent — Digital Empire Outreach
Usa Apify Google Maps Scraper per trovare business italiani.

Vantaggi:
- Free tier $5/mese (sufficiente per ~500 lead/giorno)
- Zero billing setup richiesto
- Restituisce email e website direttamente
- Actor maturo e manutenuto dalla community Apify

Setup (2 min): apify.com → Sign up → Settings → API Token → metti in .env
"""

import time
from apify_client import ApifyClient

from agents.scraper import SETTORI, CITTA


class ApifyScraper:
    """
    Cerca lead italiani via Apify Google Maps Scraper.

    Interfaccia identica agli altri scraper:
    Input:  target (int), paese (str)
    Output: list[dict] {page_id, page_name, website, settore, citta, email_diretta?}
    """

    ACTOR_ID        = "compass/crawler-google-places"
    MAX_PER_QUERY   = 20
    DELAY_TRA_QUERY = 1.0

    def __init__(self, api_token: str):
        self.client = ApifyClient(api_token)

    def _cerca(self, query: str) -> list:
        """Avvia actor Apify e restituisce i risultati quando completo."""
        try:
            run = self.client.actor(self.ACTOR_ID).call(
                run_input={
                    "searchStringsArray":         [query],
                    "language":                   "it",
                    "countryCode":                "it",
                    "maxCrawledPlacesPerSearch":  self.MAX_PER_QUERY,
                    "scrapeReviews":              False,
                    "includeHistogram":           False,
                    "includeOpeningHours":        False,
                    "includePeopleAlsoSearch":    False,
                    "maxImages":                  0,
                    "skipClosedPlaces":           False,
                },
            )
            dataset_id = run.get("defaultDatasetId") if run else None
            if not dataset_id:
                return []
            return list(self.client.dataset(dataset_id).iterate_items())

        except Exception as e:
            err = str(e).lower()
            if "unauthorized" in err or "token" in err or "401" in err:
                print("\n[SCRAPER] API TOKEN APIFY NON VALIDO!")
                print("[SCRAPER] Verifica APIFY_API_TOKEN nel .env")
                print("[SCRAPER] Generalo su: apify.com → Settings → API Token\n")
                raise RuntimeError("APIFY_API_TOKEN_NON_VALIDO")
            if "monthly" in err or "hard limit" in err or "usage" in err:
                print("\n[SCRAPER] LIMITE MENSILE APIFY RAGGIUNTO — reset al 1° del mese.")
                print("[SCRAPER] Usa Google Places o Outscraper come alternativa.\n")
                raise RuntimeError("APIFY_MONTHLY_LIMIT")
            if "quota" in err or "429" in err:
                print("[SCRAPER] Rate limit Apify temporaneo — attendo 15s...")
                time.sleep(15)
                return self._cerca(query)
            print(f"[SCRAPER] Errore Apify: {e}")
            return []

    def run(self, target: int = 1000, paese: str = "IT") -> list:
        """
        Raccoglie business italiani da Google Maps via Apify.

        Returns:
            list[dict]: {page_id, page_name, website, settore, citta}
            Con extra field 'email_diretta' se disponibile nel listing.
        """
        risultati   = []
        place_visti = set()

        print(f"\n[SCRAPER] Avvio Apify Google Maps — target: {target} business")

        for settore in SETTORI:
            if len(risultati) >= target:
                break

            for citta in CITTA:
                if len(risultati) >= target:
                    break

                query = f"{settore} {citta} Italia"
                print(f"[SCRAPER] Ricerca: '{settore} {citta}' ({len(risultati)}/{target})")

                items = self._cerca(query)
                nuovi_da_query = 0

                for item in items:
                    place_id = item.get("placeId") or item.get("id") or item.get("title", "")
                    if not place_id or place_id in place_visti:
                        continue
                    place_visti.add(place_id)

                    sito  = item.get("website") or item.get("url") or ""
                    email = item.get("email") or ""

                    # Alcune versioni dell'actor restituiscono lista di email
                    if isinstance(email, list):
                        email = email[0] if email else ""

                    if not sito and not email:
                        continue
                    if sito and not sito.startswith("http"):
                        sito = f"https://{sito}"

                    entry = {
                        "page_id":   str(place_id),
                        "page_name": item.get("title", ""),
                        "website":   sito,
                        "settore":   settore,
                        "citta":     citta,
                    }
                    if email:
                        entry["email_diretta"] = email

                    risultati.append(entry)
                    nuovi_da_query += 1

                print(f"[SCRAPER]  → {nuovi_da_query} nuovi business. Totale: {len(risultati)}")
                time.sleep(self.DELAY_TRA_QUERY)

        print(f"\n[SCRAPER] Completato: {len(risultati)} business trovati")
        return risultati
