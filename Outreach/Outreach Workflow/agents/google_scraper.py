"""
Google Places Scraper Agent — Digital Empire Outreach
Alternativa a FacebookScraperAgent, zero approval process.

Costo: ~$0 con il credito gratuito $200/mese di Google Cloud.
Setup (2 min): console.cloud.google.com → Enable Places API → Create API Key
"""

import time
import requests

from agents.scraper import SETTORI, CITTA


class GooglePlacesScraper:
    """
    Cerca lead usando Google Places Text Search + Place Details API.

    Interfaccia identica a FacebookScraperAgent:
    Input:  target (int), paese (str, ignorato — Google usa language=it)
    Output: list[dict] {page_id, page_name, website, settore, citta}
    """

    BASE_URL = "https://maps.googleapis.com/maps/api/place"
    DELAY_TRA_QUERY    = 0.5   # secondi tra Text Search calls
    DELAY_TRA_DETTAGLI = 0.3   # secondi tra Place Details calls

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def _cerca_places(self, query: str) -> list:
        """Chiama Places Text Search — restituisce fino a 20 places."""
        try:
            resp = self.session.get(
                f"{self.BASE_URL}/textsearch/json",
                params={
                    "query": query,
                    "key":   self.api_key,
                    "language": "it",
                    "type": "establishment",
                },
                timeout=15,
            )
            resp.raise_for_status()
            data   = resp.json()
            status = data.get("status", "")

            if status == "OK":
                return data.get("results", [])
            if status == "ZERO_RESULTS":
                return []
            if status == "OVER_QUERY_LIMIT":
                print("[SCRAPER] Rate limit Google Places — attendo 5s e riprovo...")
                time.sleep(5)
                return self._cerca_places(query)
            if status == "REQUEST_DENIED":
                msg = data.get("error_message", "chiave non valida o Places API non abilitata")
                print(f"\n[SCRAPER] API KEY GOOGLE RIFIUTATA: {msg}")
                print("[SCRAPER] Verifica GOOGLE_PLACES_API_KEY nel .env")
                print("[SCRAPER] e che 'Places API' sia abilitata su console.cloud.google.com\n")
                raise RuntimeError("API_KEY_GOOGLE_NON_VALIDA")

            print(f"[SCRAPER] Google Places status inatteso: {status}")
            return []

        except RuntimeError:
            raise
        except requests.exceptions.HTTPError as e:
            print(f"[SCRAPER] HTTP error Text Search: {e}")
            return []
        except Exception as e:
            print(f"[SCRAPER] Errore Text Search: {e}")
            return []

    def _sito_da_place(self, place_id: str) -> str:
        """Chiama Place Details per ottenere il website di un business."""
        try:
            resp = self.session.get(
                f"{self.BASE_URL}/details/json",
                params={
                    "place_id": place_id,
                    "fields":   "website",
                    "key":      self.api_key,
                },
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json().get("result", {}).get("website", "")
        except Exception:
            return ""

    def run(self, target: int = 1000, paese: str = "IT") -> list:
        """
        Raccoglie business italiani da Google Places fino al target.

        Returns:
            list[dict]: {page_id, page_name, website, settore, citta}
        """
        risultati   = []
        place_visti = set()

        print(f"\n[SCRAPER] Avvio Google Places — target: {target} business con sito web")

        for settore in SETTORI:
            if len(risultati) >= target:
                break

            for citta in CITTA:
                if len(risultati) >= target:
                    break

                query = f"{settore} {citta}"
                print(f"[SCRAPER] Ricerca: '{query}' ({len(risultati)}/{target})")

                places = self._cerca_places(query)
                nuovi_da_query = 0

                for place in places:
                    place_id = place.get("place_id")
                    if not place_id or place_id in place_visti:
                        continue
                    place_visti.add(place_id)

                    # Text Search non restituisce website — serve Place Details
                    time.sleep(self.DELAY_TRA_DETTAGLI)
                    sito = self._sito_da_place(place_id)

                    if not sito or not sito.startswith("http"):
                        continue  # Senza sito non troviamo l'email

                    risultati.append({
                        "page_id":   place_id,
                        "page_name": place.get("name", ""),
                        "website":   sito,
                        "settore":   settore,
                        "citta":     citta,
                    })
                    nuovi_da_query += 1

                print(f"[SCRAPER]  → {nuovi_da_query} nuovi business. Totale: {len(risultati)}")
                time.sleep(self.DELAY_TRA_QUERY)

        print(f"\n[SCRAPER] Completato: {len(risultati)} business con sito web trovati")
        return risultati
