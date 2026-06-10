"""
Facebook Scraper Agent — Digital Empire Outreach
Cerca lead usando la Facebook Ad Library API ufficiale (GRATUITA).

Nessun Apify, nessun costo aggiuntivo.
Richiede: FB_ACCESS_TOKEN nel .env (vedi SETUP.md, 5 minuti di setup).

Logica:
1. Itera su combinazioni settore × città italiane
2. Per ogni combinazione chiama /ads_archive (API Meta gratuita)
3. Per ogni pagina trovata, recupera il sito web dal Graph API
4. Restituisce lista di business con nome + sito
"""

import time
import requests


SETTORI = [
    # Agenzie marketing / digital agency
    "agenzia marketing digitale",
    "digital agency",
    "agenzia social media marketing",
    "agenzia comunicazione",
    "agenzia web marketing",
    # Info-product / formatori / corsi online
    "formatore corsi online",
    "corso online business",
    "scuola di formazione online",
    "info product creator",
    # Business / life coach
    "business coach",
    "life coach",
    "mindset coach",
    "business mentor",
    # Social media manager
    "social media manager",
    "social media strategist",
    # Copywriter
    "copywriter freelance",
    "copywriter persuasivo",
    # Facebook / Meta / Google ads specialist
    "facebook ads specialist",
    "meta ads specialist",
    "google ads specialist",
    "advertising specialist",
    # Growth / funnel marketer
    "growth marketer",
    "funnel marketer",
    "performance marketer",
    # Consulenti marketing
    "consulente marketing digitale",
    "consulente marketing online",
    "marketing freelance",
    # E-commerce / Shopify / dropshipping
    "consulente ecommerce",
    "shopify expert",
    "ecommerce manager",
    "dropshipping store",
    "brand ecommerce",
]

CITTA = [
    "Milano", "Roma", "Napoli", "Torino", "Bologna",
    "Firenze", "Palermo", "Bari", "Venezia", "Catania",
    "Genova", "Verona", "Padova", "Brescia", "Bergamo",
    "Parma", "Modena", "Reggio Emilia", "Perugia", "Trieste",
    "Taranto", "Messina", "Prato", "Reggio Calabria", "Cagliari",
]


class FacebookScraperAgent:
    """
    Agente di ricerca lead dalla Facebook Ad Library API.

    Pattern Anthropic: Worker agent specializzato con tool use simulato.
    Input:  target (int) — quanti business raccogliere
    Output: lista di dict {page_id, page_name, website, settore, citta}

    API Meta ufficiale — gratuita, nessun costo.
    Rate limit: 200 chiamate/ora (sufficiente per 500+ lead).
    """

    BASE_URL = "https://graph.facebook.com/v21.0"
    DELAY_TRA_QUERY = 1.5       # secondi tra query di ricerca
    DELAY_TRA_PAGINE = 0.4      # secondi tra richieste info-pagina

    def __init__(self, access_token: str):
        self.token = access_token
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    # ────────────────────────────────────────────────────────────────────────
    # Strumenti interni (tools)
    # ────────────────────────────────────────────────────────────────────────

    def _cerca_ads(self, query: str, paese: str = "IT", limite: int = 50) -> list:
        """Chiama /ads_archive — restituisce lista di ads attivi."""
        try:
            resp = self.session.get(
                f"{self.BASE_URL}/ads_archive",
                params={
                    "access_token": self.token,
                    "search_terms": query,
                    "ad_reached_countries": f'["{paese}"]',
                    "ad_active_status": "ACTIVE",
                    "fields": (
                        "id,page_id,page_name,"
                        "ad_creative_link_captions,"
                        "ad_creative_bodies"
                    ),
                    "limit": limite,
                },
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json().get("data", [])

        except requests.exceptions.HTTPError as e:
            codice_http = e.response.status_code if e.response is not None else 0
            # Leggi il codice FB dall'errore nel body (non dallo status HTTP)
            codice_fb = 0
            if e.response is not None:
                try:
                    codice_fb = e.response.json().get("error", {}).get("code", 0)
                except Exception:
                    pass
            if codice_fb == 190 or (codice_http == 400 and codice_fb == 190):
                print("\n[SCRAPER] TOKEN FACEBOOK SCADUTO!")
                print("[SCRAPER] Rinnova il token in 2 minuti:")
                print("[SCRAPER]  1. Vai su: developers.facebook.com/tools/explorer")
                print("[SCRAPER]  2. Genera un nuovo token con permesso 'ads_read'")
                print("[SCRAPER]  3. Copialo nel file .env alla riga FB_ACCESS_TOKEN=\n")
                raise RuntimeError("TOKEN_SCADUTO")
            elif codice_fb == 10:
                print("\n[SCRAPER] PERMESSO MANCANTE — ads_read non abilitato su questo token.")
                print("[SCRAPER] Soluzione (5 minuti):")
                print("[SCRAPER]  1. Vai su facebook.com/ads/library → accetta i Termini di Servizio")
                print("[SCRAPER]  2. Vai su developers.facebook.com/tools/explorer")
                print("[SCRAPER]  3. In 'Permissions' seleziona 'ads_read'")
                print("[SCRAPER]  4. Clicca 'Generate Access Token' e copia il nuovo token nel .env\n")
                raise RuntimeError("PERMESSO_MANCANTE")
            elif codice_http == 403:
                print("[SCRAPER] ERRORE: Permessi insufficienti — il token deve avere 'ads_read'.")
            elif codice_http == 429:
                print("[SCRAPER] Rate limit raggiunto — attendo 60s...")
                time.sleep(60)
            else:
                print(f"[SCRAPER] Errore HTTP {codice_http} (FB code: {codice_fb}): {e}")
            return []
        except Exception as e:
            print(f"[SCRAPER] Errore connessione: {e}")
            return []

    def _sito_da_pagina(self, page_id: str) -> str:
        """Recupera il sito web ufficiale di una pagina Facebook."""
        try:
            resp = self.session.get(
                f"{self.BASE_URL}/{page_id}",
                params={
                    "access_token": self.token,
                    "fields": "website,name",
                },
                timeout=15,
            )
            resp.raise_for_status()
            return resp.json().get("website", "")
        except Exception:
            return ""

    def _sito_da_caption(self, ad: dict) -> str:
        """
        Estrae URL dall'ad creative caption come fallback.
        Le captions spesso hanno il display URL (es. 'miobusiness.it').
        """
        captions = ad.get("ad_creative_link_captions", [])
        for caption in captions:
            caption = caption.strip()
            if not caption or "." not in caption:
                continue
            # Escludi social media
            escludi = ("facebook.com", "instagram.com", "fb.com", "wa.me")
            if any(e in caption.lower() for e in escludi):
                continue
            # Aggiungi schema se mancante
            if not caption.startswith("http"):
                caption = f"https://{caption}"
            return caption
        return ""

    # ────────────────────────────────────────────────────────────────────────
    # Interfaccia pubblica dell'agente
    # ────────────────────────────────────────────────────────────────────────

    def run(self, target: int = 1000, paese: str = "IT") -> list:
        """
        Raccoglie business da Facebook Ads fino al target.

        Returns:
            Lista di dict: {page_id, page_name, website, settore, citta}
        """
        risultati = []
        page_ids_visti = set()

        print(f"\n[SCRAPER] Avvio — target: {target} business unici con sito web")

        for settore in SETTORI:
            if len(risultati) >= target:
                break

            for citta in CITTA:
                if len(risultati) >= target:
                    break

                query = f"{settore} {citta}"
                print(f"[SCRAPER] Ricerca: '{query}' ({len(risultati)}/{target})")

                ads = self._cerca_ads(query, paese)
                nuovi_da_query = 0

                for ad in ads:
                    page_id = ad.get("page_id")
                    if not page_id or page_id in page_ids_visti:
                        continue

                    page_ids_visti.add(page_id)

                    # Prova prima dal Graph API (più affidabile)
                    time.sleep(self.DELAY_TRA_PAGINE)
                    sito = self._sito_da_pagina(page_id)

                    # Fallback: estrai dall'ad creative
                    if not sito or not sito.startswith("http"):
                        sito = self._sito_da_caption(ad)

                    if not sito or not sito.startswith("http"):
                        continue  # Senza sito non possiamo trovare l'email

                    risultati.append({
                        "page_id": page_id,
                        "page_name": ad.get("page_name", ""),
                        "website": sito,
                        "settore": settore,
                        "citta": citta,
                    })
                    nuovi_da_query += 1

                print(f"[SCRAPER]  → {nuovi_da_query} nuovi business. Totale: {len(risultati)}")
                time.sleep(self.DELAY_TRA_QUERY)

        print(f"\n[SCRAPER] Completato: {len(risultati)} business con sito web trovati")
        return risultati
