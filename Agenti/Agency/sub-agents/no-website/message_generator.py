"""
Message Generator — Sub-agent No-Website
Genera bozze email e SMS personalizzate con Claude API.
"""

import os
import anthropic

MAX_MESSAGGI = 500

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def genera_email(business: dict) -> str:
    """Genera email personalizzata per un business senza sito web."""
    nome = business.get("title", "")
    settore = business.get("categoryName", "la vostra attività")
    citta = business.get("city") or business.get("address", "")
    rating = business.get("totalScore") or business.get("rating") or ""
    recensioni = business.get("reviewsCount") or ""

    prompt = f"""Sei un consulente web che scrive email fredde professionali in italiano.

Business: {nome}
Settore: {settore}
Città: {citta}
Rating Google: {rating} ({recensioni} recensioni)
Problema: Non ha un sito web

Scrivi un'email fredda breve (max 120 parole) con:
- Oggetto accattivante
- Apertura personalizzata che mostra che conosci il loro business
- Un beneficio concreto (es. clienti da Google, visibilità locale)
- Call to action chiara (chiamata 10 minuti)
- Tono professionale ma diretto, non commerciale

Formato:
OGGETTO: [oggetto email]

[corpo email]"""

    risposta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}],
    )
    return risposta.content[0].text


def genera_sms(business: dict) -> str:
    """Genera SMS breve personalizzato (max 160 caratteri)."""
    nome = business.get("title", "")
    settore = business.get("categoryName", "la vostra attività")

    prompt = f"""Scrivi un SMS freddo in italiano per contattare {nome} ({settore}).
Non ha un sito web. Proponi una consulenza gratuita.
MAX 160 caratteri. Deve sembrare un messaggio personale, non spam.
Solo il testo del SMS, nient'altro."""

    risposta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}],
    )
    return risposta.content[0].text.strip()


def genera_messaggi_batch(leads: list[dict]) -> list[dict]:
    """Genera email (e SMS se c'è telefono) per tutti i lead. Max 20."""
    leads_da_processare = leads[:MAX_MESSAGGI]
    print(f"[NO-WEBSITE] Generazione messaggi per {len(leads_da_processare)} lead...")

    for lead in leads_da_processare:
        try:
            lead["bozza_email"] = genera_email(lead)
            if lead.get("telefono_trovato"):
                lead["bozza_sms"] = genera_sms(lead)
        except Exception as e:
            lead["bozza_email"] = f"ERRORE GENERAZIONE: {e}"

    return leads_da_processare
