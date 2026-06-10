"""
Email Composer — Sub-agent CRO-Funnel
Genera bozza email personalizzata con riferimento al PDF allegato.
"""

import os
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def genera_email_con_pdf(business: dict, pdf_path: str) -> str:
    """
    Genera email fredda personalizzata che menziona il PDF allegato.
    """
    nome = business.get("title", "")
    url = business.get("url") or business.get("website", "")
    score_funnel = business.get("score_funnel", "N/D")
    problemi = business.get("problemi", [])
    n_problemi = len(problemi)
    primo_problema = problemi[0] if problemi else "problemi di conversione"

    prompt = f"""Sei un consulente di marketing digitale che scrive email fredde professionali in italiano.

Business: {nome}
Sito web: {url}
Score funnel: {score_funnel}/100
Numero di problemi trovati: {n_problemi}
Problema principale: {primo_problema}

Hai preparato un report PDF gratuito con l'analisi del loro sito.

Scrivi un'email fredda (max 150 parole) con:
- Oggetto che incuriosisce e menziona il sito specifico
- Apertura che mostra che HAI ANALIZZATO il loro sito (non generica)
- Menziona che hai trovato {n_problemi} problemi specifici
- Cita il problema principale: {primo_problema}
- Dì che hai allegato un PDF gratuito con l'analisi completa
- CTA chiara: call di 20 minuti per discutere le soluzioni
- Tono professionale e diretto, non commerciale

Formato:
OGGETTO: [oggetto]

[corpo email]"""

    risposta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}],
    )
    return risposta.content[0].text


def componi_bozze_batch(leads_con_pdf: list[dict]) -> list[dict]:
    """Genera bozze email per tutti i lead con PDF."""
    print(f"[CRO-FUNNEL] Generazione email per {len(leads_con_pdf)} lead...")
    for lead in leads_con_pdf:
        try:
            lead["bozza_email"] = genera_email_con_pdf(lead, lead.get("pdf_path", ""))
        except Exception as e:
            lead["bozza_email"] = f"ERRORE: {e}"
    return leads_con_pdf
