"""
Qualifier Agent — Team 1 (Intelligence)
Modello: NVIDIA Nemotron via OpenRouter (gratuito)

Riceve un lead grezzo con email e restituisce:
- score 0-100 (qualità del lead)
- template A / B / C da usare
- pain_point principale identificato
- key_observation per il writer
"""

import json
import time
import openai
from openai import OpenAI
from agents.ai_client import build_rotation


QUALIFIER_SYSTEM_PROMPT = """Sei un lead qualification specialist per Digital Empire.
Digital Empire vende 3 IMPLEMENTAZIONI AI = workflow installati sui server del cliente,
codice sorgente incluso, €0 canoni mensili, setup in 7 giorni, automazione 100%:
1. OUTREACH FACTORY — automatizza l'outreach al 100% (300+ email personalizzate/giorno via Gmail + social)
2. CONTENT FACTORY — l'AI genera copy + costruisce grafiche/caroselli social e script video in automatico
3. SECOND BRAIN — knowledge base a grafo che dà memoria/contesto permanente all'LLM (Context Engineering)

La leva è OPERATIVA ("ti stravolgo l'operatività"), MAI le conversioni (offende chi fa marketing).

TARGET IDEALE (alto score) — chi "compra automazione":
- Agenzie di marketing / digital agency che gestiscono campagne per clienti
- Info-business: chi vende corsi online, ebook, programmi, membership (info product)
- Coach e mentor (business/life coach) con percorsi ad alto ticket
- Marketing freelance: social media manager, copywriter, facebook/google ads specialist, growth/funnel marketer
- Consulenti marketing
- Brand e-commerce / Shopify / dropshipping

SEGNALI CHE PREMIANO LO SCORE (compra automazione):
- Vende servizi, prodotti o corsi online
- Fa outreach o produce contenuti A MANO (lavoro ripetitivo che non scala)
- Ha un team (org strutturata)
- Gira advertising attivo (Facebook/Meta/Google Ads)
- È in fase di scaling / crescita

NON TARGET (score basso, scartare):
- Professionisti locali puri (dentisti, avvocati, ristoranti, artigiani, salute, immobiliare)
- Pubblica amministrazione, grande distribuzione, multinazionali
- Chi non vende nulla online

Il tuo compito: analizzare un lead e restituire una valutazione strutturata.

CRITERI DI SCORING (0-100):
- 80-100 (Hot): agenzia/info-business/marketing pro che fa outreach o contenuti a mano, ha team o gira ads, in scaling
- 60-79 (Warm): rientra nel target ideale, segnali di vendita online presenti
- 40-59 (Tiepido): target plausibile ma segnali deboli
- 0-39 (Cold): professionista locale puro, PA, nessuna vendita online — scartare

LOGICA TEMPLATE = scegli il PRODOTTO-GANCIO giusto:
- Template A (OUTREACH FACTORY): agenzie, coach, consulenti, marketing freelance (SMM/copy/ads) — chi vive di acquisizione clienti
- Template B (CONTENT FACTORY): info-product, creator, ecommerce, chi pubblica molti contenuti
- Template C (SECOND BRAIN): org strutturate, con team, uso intenso di AI

REGOLE SCORING:
- +20 punti se: agenzia, info-business/coach, marketing freelance, ecommerce (target ideale)
- +15 punti se: fa outreach o produce contenuti a mano (lavoro manuale che non scala)
- +15 punti se: fa advertising attivo (Facebook/Google Ads)
- +10 punti se: ha un team / è in scaling
- -30 punti se: professionista locale puro (dentista, avvocato, ristorante, artigiano, salute, immobiliare)
- -30 punti se: pubblica amministrazione, grande distribuzione, nessuna vendita online

CHIAVI SETTORE CANONICHE (usa quando possibile una di queste in "settore_calibrato"):
"agenzia", "info_product", "coach", "smm_freelance", "ecommerce", "consulente", "default"
(copywriter / ads specialist / social media manager → "smm_freelance"; formatore/corso → "info_product")

COERENZA prodotto_guida ↔ template:
- template A → prodotto_guida "outreach"
- template B → prodotto_guida "content"
- template C → prodotto_guida "second_brain"

OUTPUT OBBLIGATORIO (JSON valido, nient'altro):
{
  "score": <numero 0-100>,
  "template": "<A|B|C>",
  "prodotto_guida": "<outreach|content|second_brain>",
  "pain_point": "<problema operativo principale in max 15 parole>",
  "key_observation": "<osservazione specifica e concreta sul loro business, max 20 parole>",
  "settore_calibrato": "<una chiave canonica: agenzia|info_product|coach|smm_freelance|ecommerce|consulente|default>"
}"""


# Chiavi settore canoniche (allineate a knowledge: copy_training / brand_voice)
_CHIAVI_SETTORE_CANONICHE = {
    "agenzia", "info_product", "coach", "smm_freelance",
    "ecommerce", "consulente", "default",
}

# Mappa template → prodotto_guida (coerenza garantita lato codice)
_TEMPLATE_PRODOTTO = {"A": "outreach", "B": "content", "C": "second_brain"}


class QualifierAgent:
    """
    Team 1 — Intelligence: qualifica i lead e seleziona il template.
    Usa NVIDIA Nemotron (gratuito via OpenRouter).
    """

    def __init__(self, openrouter_api_key: str):
        self.rotation = build_rotation(openrouter_api_key)

    def _qualifica(self, lead: dict) -> dict:
        """Qualifica un singolo lead. Ritorna il lead con score e template aggiunti."""
        nome = lead.get("page_name", "Business sconosciuto")
        settore = lead.get("settore", "settore non specificato")
        citta = lead.get("citta", "Italia")
        website = lead.get("website", "")
        email = lead.get("email", "")
        ha_ads = lead.get("ha_ads", True)  # trovato tramite FB Ads

        ha_sito = bool(website and website.strip() and website != "N/A")
        tipo_lead = "ha_ads_senza_sito" if ha_ads and not ha_sito else (
            "ha_ads_con_sito" if ha_ads and ha_sito else "senza_sito"
        )

        prompt = f"""Qualifica questo lead per Digital Empire (implementazioni AI / 3 workflow:
Outreach Factory, Content Factory, Second Brain):

Nome business: {nome}
Settore: {settore}
Città: {citta}
Ha sito web: {"Sì — " + website if ha_sito else "No"}
Ha email trovata: {"Sì — " + email if email else "No"}
Trovato tramite: {"Facebook Ads" if ha_ads else "Google Maps"}
Tipo identificato: {tipo_lead}

Scegli il prodotto-gancio (template) più adatto e dai uno score in base a quanto
"compra automazione". Restituisci SOLO il JSON di valutazione, senza testo aggiuntivo."""

        for attempt, (client, model) in enumerate(self.rotation):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": QUALIFIER_SYSTEM_PROMPT},
                        {"role": "user", "content": prompt},
                    ],
                    max_tokens=200,
                    temperature=0.2,
                )
                testo = response.choices[0].message.content.strip()
                start = testo.find("{")
                end = testo.rfind("}") + 1
                if start >= 0 and end > start:
                    risultato = json.loads(testo[start:end])
                    template = str(risultato.get("template", "A")).strip().upper()
                    if template not in ("A", "B", "C"):
                        template = "A"
                    # Coerenza prodotto_guida ↔ template (il template comanda)
                    prodotto = risultato.get("prodotto_guida", "")
                    if prodotto not in ("outreach", "content", "second_brain"):
                        prodotto = _TEMPLATE_PRODOTTO[template]
                    elif prodotto != _TEMPLATE_PRODOTTO[template]:
                        prodotto = _TEMPLATE_PRODOTTO[template]
                    # settore_calibrato: usa la chiave canonica quando possibile
                    settore_cal = str(risultato.get("settore_calibrato", settore)).strip()
                    if settore_cal.lower() in _CHIAVI_SETTORE_CANONICHE:
                        settore_cal = settore_cal.lower()
                    return {
                        **lead,
                        "score": risultato.get("score", 50),
                        "template": template,
                        "prodotto_guida": prodotto,
                        "pain_point": risultato.get("pain_point", ""),
                        "key_observation": risultato.get("key_observation", ""),
                        "settore_calibrato": settore_cal,
                    }
            except (openai.RateLimitError, openai.APIStatusError) as e:
                if isinstance(e, openai.APIStatusError) and getattr(e, "status_code", 0) != 429:
                    break
                wait = min(15 * (attempt + 1), 60)
                time.sleep(wait)
            except Exception as e:
                if attempt < len(self.rotation) - 1:
                    time.sleep(3)
                else:
                    print(f"[QUALIFIER] Fallback per '{nome}': {e}")

        # Fallback deterministico se tutti i tentativi falliscono
        settore_cal, template = self._fallback_settore_template(settore)
        prodotto = _TEMPLATE_PRODOTTO[template]
        pain_default = {
            "outreach": "fa l'outreach a mano, non scala e ruba ore ogni settimana",
            "content": "produce copy e contenuti a mano, divora pomeriggi ogni settimana",
            "second_brain": "l'AI riparte da zero ogni volta, contesto da ri-fornire di continuo",
        }[prodotto]
        return {
            **lead,
            "score": 55,
            "template": template,
            "prodotto_guida": prodotto,
            "pain_point": pain_default,
            "key_observation": f"Attività nel settore {settore}{' a ' + citta if citta else ''}",
            "settore_calibrato": settore_cal,
        }

    @staticmethod
    def _fallback_settore_template(settore: str) -> tuple:
        """Mappa deterministica settore grezzo → (chiave canonica, template A/B/C)."""
        sl = (settore or "").lower()
        # info_product / content → Template B
        if any(k in sl for k in ("corso", "formator", "formazione", "info product", "info-product", "creator")):
            return "info_product", "B"
        if any(k in sl for k in ("ecommerce", "e-commerce", "shopify", "dropshipping", "store", "brand ")):
            return "ecommerce", "B"
        # outreach-driven → Template A
        if any(k in sl for k in ("agenzia", "agency")):
            return "agenzia", "A"
        if any(k in sl for k in ("coach", "mentor", "mindset")):
            return "coach", "A"
        if any(k in sl for k in ("social media", "smm", "copywriter", "ads", "advertising",
                                  "growth", "funnel", "performance market")):
            return "smm_freelance", "A"
        if "consulente" in sl or "marketing freelance" in sl:
            return "consulente", "A"
        return "default", "A"

    def run(self, leads: list) -> list:
        """
        Qualifica tutti i lead e filtra quelli con score >= 40.

        Returns:
            Lista di lead qualificati, ordinati per score decrescente.
        """
        print(f"\n[QUALIFIER] Scoring {len(leads)} lead con NVIDIA Nemotron...")

        qualificati = []
        scartati = 0

        for i, lead in enumerate(leads, 1):
            nome = lead.get("page_name", "?")
            if i % 20 == 0:
                print(f"[QUALIFIER] Progresso: {i}/{len(leads)}")

            risultato = self._qualifica(lead)

            if risultato["score"] >= 40:
                qualificati.append(risultato)
            else:
                scartati += 1

            time.sleep(0.3)  # Rate limiting cortesia

        qualificati.sort(key=lambda x: x["score"], reverse=True)

        distribuzione = {
            "hot (80-100)": sum(1 for l in qualificati if l["score"] >= 80),
            "warm (60-79)": sum(1 for l in qualificati if 60 <= l["score"] < 80),
            "tiepido (40-59)": sum(1 for l in qualificati if 40 <= l["score"] < 60),
        }

        print(f"[QUALIFIER] Risultati: {len(qualificati)} qualificati, {scartati} scartati")
        print(f"[QUALIFIER] Distribuzione: Hot={distribuzione['hot (80-100)']}, "
              f"Warm={distribuzione['warm (60-79)']}, Tiepido={distribuzione['tiepido (40-59)']}")

        return qualificati
