"""
Strategist Agent — Team 3 (Strategy)
100% deterministico — zero AI, zero sleep.
Genera strategy brief settore-specifico con Barnum opener hardcoded.
Il Writer FA l'AI call che conta: qui prepariamo solo il contesto.
"""


# Barnum opener per settore — frasi universali-specifiche sul DOLORE OPERATIVO
# Chiavi allineate ai nuovi target/settori canonici del pivot AI.
_BARNUM_OPENERS = {
    "agenzia":       "Chi gestisce un'agenzia sa che il collo di bottiglia non è chiudere i clienti, è riempire la pipeline ogni giorno a mano.",
    "info_product":  "Chi vive di info-prodotti lo sa: i contenuti sono il motore delle vendite, ma sono anche il buco nero che ti divora ogni pomeriggio.",
    "coach":         "Chi fa coaching conosce il paradosso: quando sei dentro i percorsi dei clienti, l'acquisizione di nuovi si ferma del tutto.",
    "smm":           "Chi gestisce i social dei clienti tutto il giorno ha sempre lo stesso problema: il proprio outreach resta l'ultima cosa in lista.",
    "smm_freelance": "Chi gestisce i social dei clienti tutto il giorno ha sempre lo stesso problema: il proprio outreach resta l'ultima cosa in lista.",
    "copywriter":    "Chi scrive copy per i clienti tutto il giorno raramente trova il tempo di scrivere a sé stesso le email che porterebbero clienti nuovi.",
    "ads":           "Chi gestisce le ads dei clienti sa far girare il traffico, ma trovare i propri clienti nuovi resta un lavoro manuale che non scala.",
    "ecommerce":     "Chi gestisce un ecommerce sa che il ritmo dei contenuti — schede, creatività, social — non regge mai se li fai a mano.",
    "consulente":    "Chi fa consulenza lo sa: il tempo vale tanto, ma cercare e contattare nuovi prospect a mano è proprio l'attività non fatturabile che ne brucia di più.",
    "default":       "Chi manda avanti un business da solo o con un piccolo team ha sempre lo stesso problema: c'è un processo ripetitivo, fatto a mano, che ruba ore e non scala.",
}

_NICHE_TERMS = {
    "agenzia":       "ore/settimana di acquisizione a freddo gestita a mano",
    "info_product":  "ore/settimana di produzione contenuti manuale (copy + grafiche + script)",
    "coach":         "acquisizione che si ferma quando sei in delivery sui percorsi",
    "smm":           "outreach in entrata fatto a mano tra un cliente e l'altro",
    "smm_freelance": "outreach in entrata fatto a mano tra un cliente e l'altro",
    "copywriter":    "tempo non fatturabile speso a cercare e contattare clienti nuovi",
    "ads":           "prospecting manuale che non scala con il numero di clienti gestiti",
    "ecommerce":     "produzione contenuti (schede/ads creative/social) che non regge il ritmo a mano",
    "consulente":    "ore non fatturabili bruciate nel prospecting manuale",
    "default":       "processo operativo ripetitivo gestito ancora a mano",
}

# Keyed A/B/C = i 3 prodotti del pivot
_PROBLEMI = {
    "A": "L'outreach a freddo lo fai a mano: cercare lead e scrivere una per una divora 8-12 ore a settimana, e appena ti fermi si ferma tutto.",
    "B": "La produzione contenuti la fai a mano: copy, caroselli, grafiche e script ti portano via interi pomeriggi ogni settimana.",
    "C": "L'AI che usi ogni giorno dimentica tutto: ogni chat riparte da zero, devi ri-spiegare contesto e brand voice, e l'output resta generico.",
}

_ANGOLI = {
    "A": "Outreach Factory: un workflow che fa scraping, qualifica, scrive 300 email personalizzate/giorno e invia da solo. Codice tuo, €0 canoni, 7 giorni, sui tuoi server.",
    "B": "Content Factory: una pipeline AI che genera copy ottimizzato e costruisce caroselli, grafiche e script video in automatico. Codice tuo, €0 canoni, 7 giorni, sui tuoi server.",
    "C": "Second Brain: una knowledge base a grafo (Context Engineering) che dà all'LLM memoria permanente di clienti, processi e brand voice. Codice tuo, €0 canoni, 7 giorni, sui tuoi server.",
}

_TONI = {
    "agenzia":       "Da founder a founder. Entusiasta sull'automazione, concreto sulle ore liberate. Vocabolario AI/workflow pieno, niente da spiegare.",
    "info_product":  "Da creator a creator. Focalizzato sull'output e sul tempo recuperato. Mai parlare di conversioni.",
    "coach":         "Peer-to-peer, da consulente a consulente. Quantifica le ore (8-12/settimana). Parla di pipeline che non si svuota, non di conversioni.",
    "smm":           "Peer-to-peer tecnico. Vocabolario AI/automazione senza spiegazioni — è un professionista del digitale.",
    "smm_freelance": "Peer-to-peer tecnico. Vocabolario AI/automazione senza spiegazioni — è un professionista del digitale.",
    "copywriter":    "Da pari nel mestiere della scrittura. Concreto sul tempo non fatturabile recuperato.",
    "ads":           "Tecnico e diretto. Riconosci che sa far girare il traffico; il gap è il prospecting manuale.",
    "ecommerce":     "Concreto e orientato a volume/output. Vocabolario operativo, scala senza assumere.",
    "consulente":    "Molto peer-to-peer, da consulente a consulente. Numeri concreti sulle ore fatturabili.",
    "default":       "Diretto, italiano, peer-to-peer. Entusiasta sull'automazione, prima persona singolare. Dati reali.",
}


def _get_barnum(settore: str) -> str:
    sl = settore.lower()
    for k, v in _BARNUM_OPENERS.items():
        if k in sl:
            return v
    return _BARNUM_OPENERS["default"]


def _get_niche_term(settore: str) -> str:
    sl = settore.lower()
    for k, v in _NICHE_TERMS.items():
        if k in sl:
            return v
    return _NICHE_TERMS["default"]


def _get_tono(settore: str) -> str:
    sl = settore.lower()
    for k, v in _TONI.items():
        if k in sl:
            return v
    return _TONI["default"]


class StrategistAgent:
    """
    Team 3 — Strategy: genera strategy brief per ogni lead.
    100% deterministico — zero AI, zero sleep.
    Velocità: ~0.001s per lead.
    """

    def __init__(self, openrouter_api_key: str = ""):
        pass  # nessuna connessione necessaria

    def _genera_brief(self, lead: dict) -> dict:
        nome    = lead.get("page_name", "Business")
        settore = lead.get("settore_calibrato", lead.get("settore", "attività"))
        citta   = lead.get("citta", "Italia")
        template = lead.get("template", "A")

        barnum  = _get_barnum(settore)
        niche   = _get_niche_term(settore)
        problema = _PROBLEMI.get(template, _PROBLEMI["A"])
        angolo   = _ANGOLI.get(template, _ANGOLI["A"])
        tono     = _get_tono(settore)
        loc      = f" a {citta}" if citta else ""

        brief = {
            "barnum_opener":           barnum,
            "niche_term":              niche,
            "hook_angle":              f"Apri con il Barnum opener, poi porta a {nome}{loc}.",
            "problema_da_amplificare": problema,
            "angolo_soluzione":        angolo,
            "nota_tono":               tono,
        }
        return {**lead, "strategy_brief": brief}

    def run(self, leads: list) -> list:
        print(f"\n[STRATEGIST] Genero strategy brief per {len(leads)} lead...")
        risultati = [self._genera_brief(lead) for lead in leads]
        print(f"[STRATEGIST] Brief generati: {len(risultati)} (istantaneo, no AI)")
        return risultati
