"""
Copy Knowledge Agent — Team 2 (Copy Knowledge)
Prepara il briefing pack per il writer — 100% deterministico, zero AI, zero sleep.
Il Writer fa già la chiamata AI che conta: non serve duplicarla qui.
"""

from knowledge.apsoc import (
    APSOC_FULL_FRAMEWORK, TEMPLATE_A, TEMPLATE_B, TEMPLATE_C,
    CPB_FRAMEWORK, DR_PRINCIPLES, PROHIBITED_PHRASES, APPROVED_OPENERS,
)
from knowledge.brand_voice import (
    ANDREI_PASCU_BENCHMARK, QUALITY_CHECKLIST,
    SECTOR_TONE_CALIBRATION, BRAND_VOICE_GUIDELINES,
)
from knowledge.copy_training import (
    TEMPLATE_A_APPROVED_EXAMPLES, TEMPLATE_B_APPROVED_EXAMPLES,
    TEMPLATE_C_APPROVED_EXAMPLES, ANTI_EXAMPLES,
    SECTOR_MICRO_RULES, SUBJECT_LINE_FORMULAS, SECTOR_STATISTICS,
)

_TEMPLATE_MAP = {
    "A": (TEMPLATE_A_APPROVED_EXAMPLES, "template_a"),
    "B": (TEMPLATE_B_APPROVED_EXAMPLES, "template_b"),
    "C": (TEMPLATE_C_APPROVED_EXAMPLES, "template_c"),
}

# Mappa parole-chiave dei nuovi settori → chiavi CANONICHE del pivot
# (usate da SECTOR_MICRO_RULES in knowledge.copy_training).
# Chiavi canoniche: agenzia, info_product, coach, smm_freelance, ecommerce, consulente, default
_SETTORE_KEY_MAP = {
    # Agenzie marketing / digital agency
    "agenzia":      "agenzia",
    "agency":       "agenzia",
    # Coach / mentor
    "coach":        "coach",
    "mentor":       "coach",
    "mindset":      "coach",
    # Marketing freelance: SMM / copywriter / ads / growth / funnel
    "social media": "smm_freelance",
    "smm":          "smm_freelance",
    "copywriter":   "smm_freelance",
    "copy":         "smm_freelance",
    "ads":          "smm_freelance",
    "advertising":  "smm_freelance",
    "growth":       "smm_freelance",
    "funnel":       "smm_freelance",
    "performance market": "smm_freelance",
    # Info-product / formatori / corsi
    "corso":        "info_product",
    "formator":     "info_product",
    "formazione":   "info_product",
    "info":         "info_product",
    "creator":      "info_product",
    # E-commerce
    "ecommerce":    "ecommerce",
    "e-commerce":   "ecommerce",
    "shopify":      "ecommerce",
    "dropshipping": "ecommerce",
    "store":        "ecommerce",
    "brand":        "ecommerce",
    # Consulenti
    "consulente":   "consulente",
}


def _get_template_structure(template: str) -> str:
    return {"A": TEMPLATE_A, "B": TEMPLATE_B, "C": TEMPLATE_C}.get(template, TEMPLATE_A)


def _get_relevant_examples(template: str, settore: str) -> list:
    examples_list, _ = _TEMPLATE_MAP.get(template, (TEMPLATE_A_APPROVED_EXAMPLES, "template_a"))
    rilevanti = [ex for ex in examples_list if ex.get("settore", "") == settore]
    return (rilevanti if rilevanti else examples_list)[:2]


def _get_sector_rules(settore: str) -> list:
    sl = settore.lower()
    for kw, key in _SETTORE_KEY_MAP.items():
        if kw in sl:
            return SECTOR_MICRO_RULES.get(key, SECTOR_MICRO_RULES["default"])
    return SECTOR_MICRO_RULES["default"]


def _get_sector_tone(settore: str) -> dict:
    sl = settore.lower()
    for key in SECTOR_TONE_CALIBRATION:
        if key in sl or sl in key:
            return SECTOR_TONE_CALIBRATION[key]
    return SECTOR_TONE_CALIBRATION["default"]


def _genera_apertura_deterministica(lead: dict) -> dict:
    """Apertura su hype/operatività senza AI — keyed sul prodotto (template A/B/C)."""
    template = lead.get("template", "A")
    obs      = lead.get("key_observation", "")

    if template == "B":
        # Content Factory
        oggetto    = "I contenuti di una settimana in un pomeriggio"
        prima_riga = (
            "Io ho costruito un motore AI che genera il copy e mi costruisce caroselli, "
            "grafiche e script video in automatico — i contenuti social si producono quasi da soli."
        )
    elif template == "C":
        # Second Brain
        oggetto    = "L'AI che ricorda tutto del tuo business"
        prima_riga = (
            "Io ho dato all'AI una memoria permanente: un Second Brain a grafo che conosce "
            "clienti, processi e brand voice e non riparte più da zero a ogni chat."
        )
    else:
        # Outreach Factory (A, default)
        oggetto    = "300 email/giorno in automatico, codice tuo"
        prima_riga = (
            "Io ho costruito un sistema che fa l'outreach al posto mio: ogni mattina scova i lead, "
            "scrive 300 email personalizzate e parte da solo via Gmail e social."
        )

    # Se il qualifier ha lasciato un'osservazione concreta, usala come prima riga di aggancio.
    if obs:
        prima_riga = obs

    return {"oggetto": oggetto, "prima_riga": prima_riga}


class CopyKnowledgeAgent:
    """
    Team 2 — Copy Knowledge: prepara il briefing pack per il writer.
    100% deterministico — nessuna chiamata AI, nessun sleep.
    Velocità: ~0.001s per lead.
    """

    def __init__(self, openrouter_api_key: str = ""):
        pass  # nessuna connessione necessaria

    def _prepara_pack(self, lead: dict) -> dict:
        template = lead.get("template", "A")
        settore  = lead.get("settore_calibrato", lead.get("settore", ""))

        esempi_approvati = _get_relevant_examples(template, settore)
        regole_settore   = _get_sector_rules(settore)
        tono_settore     = _get_sector_tone(settore)
        anti_esempio     = ANTI_EXAMPLES[0] if ANTI_EXAMPLES else {}

        stats = []
        if "mobile" in settore.lower() or template == "B":
            stats.append(SECTOR_STATISTICS["mobile_search"])
        if template == "B":
            stats.append(SECTOR_STATISTICS["page_speed"])
        elif template == "C":
            stats.append(SECTOR_STATISTICS["first_response"])
        else:
            stats.append(SECTOR_STATISTICS["phone_vs_online"])
        if not stats:
            stats = [SECTOR_STATISTICS["mobile_search"]]

        apertura = _genera_apertura_deterministica(lead)

        pack = {
            "esempi_approvati":   esempi_approvati,
            "anti_esempio":       anti_esempio,
            "regole_settore":     regole_settore[:5],
            "statistiche":        stats[:2],
            "tono_settore":       tono_settore,
            "template_structure": _get_template_structure(template),
            "checklist_qualita":  QUALITY_CHECKLIST,
            "apertura_suggerita": apertura,
        }
        return {**lead, "copy_briefing_pack": pack}

    def run(self, leads: list) -> list:
        print(f"\n[COPY-KNOWLEDGE] Preparo briefing pack per {len(leads)} lead...")
        risultati = [self._prepara_pack(lead) for lead in leads]
        print(f"[COPY-KNOWLEDGE] Pack preparati: {len(risultati)} (istantaneo, no AI)")
        return risultati
