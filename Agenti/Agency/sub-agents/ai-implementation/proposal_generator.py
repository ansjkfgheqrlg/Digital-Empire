"""
Proposal Generator — Sub-agent AI-Implementation
Genera proposta AI personalizzata + bozza email per ogni lead.
"""

import os
import anthropic

MAX_PROPOSTE = 500
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def genera_proposta_ai(business: dict) -> str:
    """Genera email fredda con proposta AI altamente personalizzata."""
    nome = business.get("title", "")
    settore = business.get("categoryName") or business.get("settore_cercato", "la vostra attività")
    citta = business.get("city") or business.get("address", "")
    soluzione = business.get("ai_soluzione", "chatbot AI e automazione")
    segnali = business.get("ai_segnali", [])
    n_recensioni = business.get("reviewsCount") or ""
    rating = business.get("totalScore") or business.get("rating") or ""

    contesto_segnali = "\n".join(f"- {s}" for s in segnali[:4]) if segnali else "- Settore ad alto potenziale AI"

    prompt = f"""Sei un esperto di implementazioni AI per business locali. Scrivi un'email fredda professionale in italiano.

Business: {nome}
Settore: {settore}
Città: {citta}
Recensioni Google: {n_recensioni} (rating: {rating})
Soluzione AI identificata: {soluzione}
Segnali di bisogno AI rilevati:
{contesto_segnali}

Scrivi un'email fredda (max 160 parole) con:
- Oggetto specifico che menziona il business o settore
- Apertura che dimostra di aver analizzato il loro business (cita almeno un segnale specifico)
- Descrivi in 1-2 righe ESATTAMENTE quale soluzione AI proponi ({soluzione})
- Beneficio concreto e misurabile (es: "risponde ai clienti alle 2 di notte", "riduce il 70% delle telefonate ripetitive")
- Proposta di demo gratuita in 48 ore
- CTA: call di 15 minuti o demo pratica
- Tono: consulente esperto, non venditore

Formato:
OGGETTO: [oggetto]

[corpo email]"""

    risposta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=450,
        messages=[{"role": "user", "content": prompt}],
    )
    return risposta.content[0].text


def genera_proposte_batch(leads: list[dict]) -> list[dict]:
    """Genera proposte AI per tutti i lead. Max 20."""
    leads_da_processare = leads[:MAX_PROPOSTE]
    print(f"[AI-IMPL] Generazione proposte AI per {len(leads_da_processare)} lead...")

    for lead in leads_da_processare:
        try:
            lead["bozza_email"] = genera_proposta_ai(lead)
        except Exception as e:
            lead["bozza_email"] = f"ERRORE GENERAZIONE: {e}"

    return leads_da_processare
