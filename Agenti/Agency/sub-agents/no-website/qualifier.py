"""
Qualifier — Sub-agent No-Website
Calcola score 0-100 per ogni lead e assegna fascia A/B/C.
"""


def calcola_score(business: dict) -> int:
    """
    Score basato su:
    - Rating Google (0-30 punti)
    - Numero recensioni (0-30 punti)
    - Ha email (0-25 punti)
    - Ha telefono (0-15 punti)
    """
    score = 0

    # Rating: più alto = più credibile il business
    rating = business.get("totalScore") or business.get("rating") or 0
    if rating >= 4.5:
        score += 30
    elif rating >= 4.0:
        score += 22
    elif rating >= 3.5:
        score += 14
    elif rating > 0:
        score += 5

    # Recensioni: più ne ha, più è attivo
    recensioni = business.get("reviewsCount") or 0
    if recensioni >= 100:
        score += 30
    elif recensioni >= 50:
        score += 22
    elif recensioni >= 20:
        score += 15
    elif recensioni >= 5:
        score += 8

    # Email presente
    if business.get("email_trovata"):
        score += 25

    # Telefono presente
    telefono = business.get("phone") or business.get("phoneUnformatted")
    if telefono:
        score += 15

    return min(score, 100)


def assegna_fascia(score: int) -> str:
    if score >= 70:
        return "A"
    elif score >= 40:
        return "B"
    else:
        return "C"


def qualifica_leads(lista_business: list[dict]) -> list[dict]:
    """Aggiunge score e fascia a ogni business. Ritorna lista ordinata per score."""
    qualificati = []
    for b in lista_business:
        score = calcola_score(b)
        fascia = assegna_fascia(score)
        b["score"] = score
        b["fascia"] = fascia
        qualificati.append(b)

    # Ordina per score decrescente
    qualificati.sort(key=lambda x: x["score"], reverse=True)
    print(f"[NO-WEBSITE] Lead qualificati: {len(qualificati)} (A={sum(1 for l in qualificati if l['fascia']=='A')}, B={sum(1 for l in qualificati if l['fascia']=='B')}, C={sum(1 for l in qualificati if l['fascia']=='C')})")
    return qualificati
