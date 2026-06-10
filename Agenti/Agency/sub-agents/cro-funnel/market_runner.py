"""
Market Runner — Sub-agent CRO-Funnel
Esegue le skill market su un URL e raccoglie tutti i risultati in un unico report.
"""

import os
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SKILL_PROMPTS = {
    "audit": """Sei un esperto di marketing digitale. Esegui un MARKETING AUDIT completo di questo sito web.
URL: {url}
Business: {nome}

Analizza e fornisci in formato markdown strutturato:
1. **Panoramica generale** — Posizionamento, messaggi chiave, proposta di valore
2. **Problemi critici** (max 5) — Cosa sta perdendo soldi/clienti adesso
3. **Analisi UX** — Navigazione, chiarezza, percorso utente
4. **Presenza online** — SEO base, social, Google Business
5. **Score complessivo** — /100 con motivazione

Sii specifico, usa dati concreti dove possibile.""",

    "landing": """Sei un esperto CRO (Conversion Rate Optimization). Analizza questa landing page.
URL: {url}
Business: {nome}

Fornisci in markdown:
1. **Headline e sub-headline** — Sono chiari? Comunicano il beneficio principale?
2. **CTA (Call to Action)** — Presenza, posizionamento, testo, colore
3. **Above the fold** — Cosa vede l'utente senza scrollare?
4. **Social proof** — Testimonianze, numeri, loghi clienti
5. **Frizioni** — Cosa ostacola la conversione?
6. **Quick wins** — 3 modifiche immediate per aumentare conversioni""",

    "funnel": """Sei un esperto di funnel di vendita. Analizza il funnel di questo business.
URL: {url}
Business: {nome}

Analizza:
1. **Tipo di funnel attuale** — Come acquisisce clienti oggi?
2. **Punti di ingresso** — Traffico organico, ads, referral
3. **Lead magnet** — Esiste? È efficace?
4. **Email marketing** — Sequenze, automazioni
5. **Upsell/cross-sell** — Opportunità mancate
6. **Score funnel** — /100 con lista problemi prioritizzati""",

    "seo": """Sei un esperto SEO. Esegui un audit SEO on-page di questo sito.
URL: {url}
Business: {nome}

Analizza:
1. **Title tag e meta description** — Ottimizzati per le keyword target?
2. **Struttura H1-H6** — Gerarchia corretta?
3. **Keyword locali** — Sta targettando la zona geografica?
4. **Velocità e Core Web Vitals** — Stima basata su best practice
5. **Azioni prioritarie** — Top 5 fix SEO immediati""",
}


def esegui_market_audit(url: str, nome: str) -> dict:
    """
    Esegue tutti gli audit market sull'URL e ritorna i risultati.
    """
    risultati = {}
    print(f"[CRO-FUNNEL] Market audit per: {nome} ({url})")

    for skill, prompt_template in SKILL_PROMPTS.items():
        print(f"  >> Running market-{skill}...")
        try:
            prompt = prompt_template.format(url=url, nome=nome)
            risposta = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}],
            )
            risultati[skill] = risposta.content[0].text
        except Exception as e:
            risultati[skill] = f"ERRORE: {e}"

    return risultati


def compila_report_markdown(business: dict, audit_results: dict) -> str:
    """Compila tutti gli audit in un unico documento Markdown."""
    nome = business.get("title", "Business")
    url = business.get("url") or business.get("website", "")
    score_funnel = business.get("score_funnel", "N/D")
    problemi = business.get("problemi", [])

    md = f"""# Report Marketing Digitale — {nome}

**Sito:** {url}
**Data:** {__import__('datetime').datetime.now().strftime('%d/%m/%Y')}
**Score Funnel:** {score_funnel}/100

---

## Problemi tecnici rilevati automaticamente
{chr(10).join(f'- {p}' for p in problemi) if problemi else '- Nessun problema tecnico grave'}

---

## Marketing Audit Completo
{audit_results.get('audit', '')}

---

## Analisi Landing Page & CRO
{audit_results.get('landing', '')}

---

## Analisi Funnel di Vendita
{audit_results.get('funnel', '')}

---

## Audit SEO
{audit_results.get('seo', '')}

---

*Report generato da Digital Empire Agency*
"""
    return md
