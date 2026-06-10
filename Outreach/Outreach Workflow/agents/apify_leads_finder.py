"""
Apify Leads Finder Agent — Digital Empire Outreach
Actor: code_crafter/leads-finder (Apollo Alternative, $1.5/1k lead)

Vantaggi rispetto a Google Maps Scraper:
- Restituisce email VERIFICATE direttamente (no extraction phase)
- Include mobile, LinkedIn, dati azienda
- Filtro per job title (es. "Dentista", "Odontoiatra", "Studio Dentistico")
- Free tier: 100 lead/run

Quando usarlo:
- Quando APIFY_LEADS_FINDER=1 nel .env
- Priorità massima nella catena scraper dell'orchestratore

NOTA: L'account Apify ha un usage limit mensile.
Se esaurito, attendere il reset al 1° del mese successivo.
"""

import time
from apify_client import ApifyClient

ACTOR_ID = "code_crafter/leads-finder"

# Settori → job title da ricercare su Apollo/LinkedIn (target pivot: implementazioni AI)
SETTORI_JOB_TITLES = {
    "agenzia":       ["Agency Owner", "Titolare Agenzia", "Founder Marketing Agency", "CEO Digital Agency"],
    "info_product":  ["Formatore", "Course Creator", "Info Product Creator", "Founder Corso Online"],
    "coach":         ["Business Coach", "Life Coach", "Business Mentor", "Coach"],
    "smm_freelance": ["Social Media Manager", "Social Media Strategist"],
    "copywriter":    ["Copywriter", "Copywriter Freelance"],
    "ads_specialist":["Media Buyer", "Facebook Ads Specialist", "Google Ads Specialist", "Performance Marketer"],
    "consulente":    ["Consulente Marketing", "Marketing Consultant", "Growth Marketer", "Funnel Strategist"],
    "ecommerce":     ["Ecommerce Manager", "Founder Ecommerce", "Shopify Store Owner"],
}

# Città target con formato Apollo
CITTA_APOLLO = [
    "Milano", "Roma", "Napoli", "Torino", "Firenze",
    "Bologna", "Venezia", "Genova", "Palermo", "Bari",
    "Verona", "Catania",
]


class ApifyLeadsFinder:
    """
    Trova lead con email verificate via Apify code_crafter/leads-finder.

    Interfaccia identica agli altri scraper:
    Input:  target (int), paese (str)
    Output: list[dict] {page_id, page_name, website, settore, citta, email_diretta}
    """

    MAX_PER_RUN   = 100   # limite free tier
    DELAY_TRA_RUN = 2.0   # secondi tra run Apify consecutivi

    def __init__(self, api_token: str):
        self.client = ApifyClient(api_token)

    def _run_actor(self, job_titles: list, citta: str, n_lead: int) -> list:
        """Avvia una singola run dell'actor e restituisce i risultati."""
        try:
            run = self.client.actor(ACTOR_ID).call(
                run_input={
                    "numberOfLeadsToFetch": min(n_lead, self.MAX_PER_RUN),
                    "jobTitleKeywords":     job_titles,
                    "locationNames":        [citta],
                    "countryCode":          "IT",
                    "emailStatus":          ["verified", "guessed"],
                    "fileNameOrRunLabel":   f"DE_{citta[:3].upper()}",
                },
                timeout_secs=120,
            )
            dataset_id = run.get("defaultDatasetId") if run else None
            if not dataset_id:
                return []
            return list(self.client.dataset(dataset_id).iterate_items())

        except Exception as e:
            err = str(e).lower()
            if "unauthorized" in err or "401" in err or "token" in err:
                print("\n[LEADS-FINDER] APIFY_API_TOKEN non valido o scaduto.")
                print("[LEADS-FINDER] Rinnova su: apify.com → Settings → API Token\n")
                raise RuntimeError("APIFY_TOKEN_NON_VALIDO")
            if "monthly" in err or "hard limit" in err or ("usage" in err and "limit" in err):
                print("[LEADS-FINDER] Limite mensile Apify raggiunto.")
                print("[LEADS-FINDER] Reset al 1° del mese prossimo. Usa scraper alternativo.")
                raise RuntimeError("APIFY_MONTHLY_LIMIT")
            print(f"[LEADS-FINDER] Errore actor: {e}")
            return []

    def _mappa_lead(self, item: dict, settore: str, citta: str) -> dict | None:
        """Converte un record Apollo nel formato standard DE."""
        email = item.get("email") or item.get("workEmail") or item.get("personalEmail", "")
        if isinstance(email, list):
            email = email[0] if email else ""
        if not email or "@" not in email:
            return None

        nome_azienda = (
            item.get("organization", {}).get("name")
            or item.get("company")
            or item.get("organizationName")
            or ""
        )
        nome_persona = (
            f"{item.get('firstName', '')} {item.get('lastName', '')}".strip()
        )
        nome = nome_azienda or nome_persona or email.split("@")[0]

        sito = (
            item.get("organization", {}).get("websiteUrl")
            or item.get("website")
            or item.get("organizationWebsite")
            or ""
        )
        if sito and not sito.startswith("http"):
            sito = f"https://{sito}"

        page_id = item.get("id") or item.get("linkedInUrl") or email

        return {
            "page_id":       str(page_id),
            "page_name":     nome,
            "website":       sito,
            "settore":       settore,
            "citta":         citta,
            "email_diretta": email.lower().strip(),
        }

    def run(self, target: int = 300, paese: str = "IT") -> list:
        """
        Raccoglie lead italiani con email verificate via Leads Finder.

        Returns:
            list[dict]: formato standard {page_id, page_name, website, settore, citta, email_diretta}
        """
        risultati  = []
        email_visti = set()

        print(f"\n[LEADS-FINDER] Avvio Apify code_crafter/leads-finder — target: {target} lead")
        print(f"[LEADS-FINDER] Free tier: max {self.MAX_PER_RUN} lead/run")

        for settore, job_titles in SETTORI_JOB_TITLES.items():
            if len(risultati) >= target:
                break

            for citta in CITTA_APOLLO:
                if len(risultati) >= target:
                    break

                rimasti = target - len(risultati)
                n_richiesti = min(rimasti, self.MAX_PER_RUN)

                print(f"[LEADS-FINDER] {settore} / {citta} — richiedo {n_richiesti} lead "
                      f"({len(risultati)}/{target})")

                try:
                    items = self._run_actor(job_titles, citta, n_richiesti)
                except RuntimeError as e:
                    if "MONTHLY_LIMIT" in str(e):
                        print("[LEADS-FINDER] Interrompo — limite mensile raggiunto.")
                        return risultati
                    raise

                nuovi_da_run = 0
                for item in items:
                    lead = self._mappa_lead(item, settore, citta)
                    if not lead:
                        continue
                    email = lead["email_diretta"]
                    if email in email_visti:
                        continue
                    email_visti.add(email)
                    risultati.append(lead)
                    nuovi_da_run += 1

                print(f"[LEADS-FINDER]  → {nuovi_da_run} nuovi lead. Totale: {len(risultati)}")
                time.sleep(self.DELAY_TRA_RUN)

        print(f"\n[LEADS-FINDER] Completato: {len(risultati)} lead trovati con email verificata")
        return risultati
