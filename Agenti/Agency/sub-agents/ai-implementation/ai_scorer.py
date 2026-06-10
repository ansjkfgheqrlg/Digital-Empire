"""
AI Scorer — Sub-agent AI-Implementation
Analizza i segnali di bisogno AI per ogni business e calcola uno score.
"""

import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AgencyBot/1.0)"}

# Parole nelle recensioni che indicano bisogno AI
SEGNALI_RECENSIONI_NEGATIVI = [
    "attesa", "aspettare", "lento", "non rispondono", "impossibile contattare",
    "non rispondono al telefono", "difficile prenotare", "mai risposto",
    "settimane", "troppo tempo", "occupato", "irraggiungibile",
]

# Settori con altissimo potenziale AI
SETTORI_ALTA_PRIORITA = {
    "dentista": "chatbot prenotazioni + FAQ dentali",
    "studio dentistico": "chatbot prenotazioni + FAQ dentali",
    "avvocato": "chatbot qualifica lead + FAQ legali",
    "studio legale": "chatbot qualifica lead + FAQ legali",
    "fisioterapista": "sistema prenotazioni AI + promemoria",
    "ristorante": "chatbot prenotazioni + menu digitale AI",
    "hotel": "chatbot check-in + raccomandazioni AI",
    "b&b": "chatbot prenotazioni + guest experience AI",
    "centro estetico": "prenotazioni AI + upsell automatico",
    "parrucchiere": "prenotazioni AI + promemoria appuntamenti",
    "agenzia immobiliare": "chatbot qualifica acquirenti AI",
    "palestra": "chatbot iscrizioni + piani allenamento AI",
    "commercialista": "chatbot FAQ fiscali + qualifica clienti",
    "studio medico": "prenotazioni AI + triage sintomi",
    "clinica": "prenotazioni AI + follow-up pazienti",
}


def calcola_ai_score(business: dict) -> dict:
    """
    Calcola score bisogno AI (0-100) e identifica la soluzione AI più adatta.
    Ritorna il business arricchito con score e proposta AI.
    """
    score = 0
    segnali_trovati = []
    soluzione_ai = "Automazione workflow e chatbot"

    settore = (
        business.get("categoryName", "")
        or business.get("settore_cercato", "")
    ).lower()

    # Settore ad alta priorità AI
    for kw, soluzione in SETTORI_ALTA_PRIORITA.items():
        if kw in settore:
            score += 25
            segnali_trovati.append(f"Settore ad alto potenziale AI: {kw}")
            soluzione_ai = soluzione
            break

    # Nessun sito web → potenziale doppio (no-website + AI)
    if not business.get("website"):
        score += 15
        segnali_trovati.append("Nessun sito web (doppia opportunità)")

    # Nessuna chat sul sito
    url = business.get("website") or ""
    if url:
        ha_chat = _controlla_chat_su_sito(url)
        if not ha_chat:
            score += 10
            segnali_trovati.append("Nessuna chat/chatbot sul sito")

    # Analisi recensioni
    recensioni = business.get("reviews") or []
    if isinstance(recensioni, list):
        testo_recensioni = " ".join(
            r.get("text", "") if isinstance(r, dict) else str(r)
            for r in recensioni[:20]
        ).lower()
        segnali_negativi = [s for s in SEGNALI_RECENSIONI_NEGATIVI if s in testo_recensioni]
        if segnali_negativi:
            score += min(len(segnali_negativi) * 5, 20)
            segnali_trovati.append(f"Recensioni citano: {', '.join(segnali_negativi[:3])}")

    # Numero recensioni alto → business attivo con volume
    n_recensioni = business.get("reviewsCount") or 0
    if n_recensioni >= 100:
        score += 15
        segnali_trovati.append(f"Business ad alto volume ({n_recensioni} recensioni)")
    elif n_recensioni >= 30:
        score += 8
        segnali_trovati.append(f"Business attivo ({n_recensioni} recensioni)")

    # Rating medio → non ottimale, potrebbe migliorare con AI
    rating = business.get("totalScore") or business.get("rating") or 0
    if 3.0 <= rating <= 4.0:
        score += 10
        segnali_trovati.append(f"Rating medio ({rating}) — margine di miglioramento")

    business["ai_score"] = min(score, 100)
    business["ai_segnali"] = segnali_trovati
    business["ai_soluzione"] = soluzione_ai
    return business


def _controlla_chat_su_sito(url: str) -> bool:
    """Verifica se il sito ha già una chat/chatbot."""
    if not url.startswith("http"):
        url = "https://" + url
    try:
        resp = requests.get(url, headers=HEADERS, timeout=8)
        html = resp.text.lower()
        chat_kw = ["livechat", "tawk.to", "intercom", "zendesk", "crisp",
                   "tidio", "hubspot", "drift", "chatbot", "whatsapp"]
        return any(kw in html for kw in chat_kw)
    except Exception:
        return False


def filtra_leads_ai(lista_business: list[dict], soglia: int = 40) -> list[dict]:
    """Calcola score AI per tutti i business e filtra quelli >= soglia."""
    qualificati = []
    print(f"[AI-IMPL] Scoring AI per {len(lista_business)} business...")

    for b in lista_business:
        b = calcola_ai_score(b)
        if b["ai_score"] >= soglia:
            qualificati.append(b)

    qualificati.sort(key=lambda x: x["ai_score"], reverse=True)
    print(f"[AI-IMPL] Lead qualificati per AI: {len(qualificati)}/{len(lista_business)}")
    return qualificati
