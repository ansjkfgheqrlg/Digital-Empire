"""
Competitor Agent — Team DEEP-INTEL (Sub-Agent C)
Trova 2-3 competitor del lead nella stessa nicchia/città usando il nostro DB leads.

Strategia: il nostro DB SQLite contiene già centinaia di business scrapati — SONO i competitor.
Questo agente li recupera, li confronta con il lead target e produce intelligence competitiva.

Gira in PARALLELO a ResearchAgent (non ha dipendenze da altri sub-agent).
Modello: rotazione Groq → OpenRouter per la synthesis AI.
"""

import json
import sqlite3
import time
from pathlib import Path

from agents.ai_client import build_rotation, call_ai


_SYSTEM_PROMPT = """Sei un analista di mercato specializzato in business italiani locali.

Il tuo compito: dati un lead target e i suoi competitor nella stessa città/nicchia,
sintetizza intelligence competitiva utile per personalizzare la nostra proposta.

FOCUS: Digital Empire vende landing page CRO. L'obiettivo è mostrare al lead
che i competitor stanno già acquisendo clienti online che lui sta perdendo.

REGOLE:
- Sii specifico con dati reali dei competitor trovati
- Identifica cosa stanno facendo meglio (o peggio) del lead target
- Trasforma ogni osservazione in opportunità per il lead
- Scrivi come un analista di mercato, non come un venditore

OUTPUT OBBLIGATORIO — JSON valido:
{
  "competitor_1": {
    "nome": "<nome business>",
    "vantaggio": "<cosa fanno meglio del lead, max 15 parole>",
    "debolezza": "<dove anche loro mancano, max 15 parole>"
  },
  "competitor_2": {
    "nome": "<nome business>",
    "vantaggio": "<idem>",
    "debolezza": "<idem>"
  },
  "insight_mercato": "<1-2 frasi: cosa sta succedendo nel mercato locale che il lead non vede, max 30 parole>",
  "opportunita_lead": "<1 frase: cosa può fare il lead per battere i competitor, max 20 parole>"
}"""


class CompetitorAgent:
    """
    Sub-Agent C del Team DEEP-INTEL.
    Recupera competitor dal DB SQLite ed analizza il posizionamento competitivo.
    """

    def __init__(self, openrouter_api_key: str, db_path: str = None):
        self.rotation = build_rotation(openrouter_api_key)
        self.db_path  = db_path  # Path to output/leads.db

    # ──────────────────────────────────────────────────────────────────────
    # DB lookup
    # ──────────────────────────────────────────────────────────────────────

    def _find_in_db(self, lead: dict) -> list:
        """Query SQLite per trovare competitor nella stessa nicchia/città."""
        if not self.db_path or not Path(self.db_path).exists():
            return []

        settore = lead.get("settore_calibrato", lead.get("settore", ""))
        citta   = lead.get("citta", "")
        email   = lead.get("email", "")

        # Keyword più corta del settore (es: "business coach" → "coach")
        kw = settore.split()[-1] if settore else ""
        if not kw or len(kw) < 4:
            kw = settore[:8] if settore else ""

        try:
            with sqlite3.connect(self.db_path) as conn:
                rows = conn.execute("""
                    SELECT page_name, settore, citta, website, score, settore_calibrato
                    FROM leads_contattati
                    WHERE email != ?
                      AND (
                        settore LIKE ? OR settore_calibrato LIKE ?
                        OR settore LIKE ? OR settore_calibrato LIKE ?
                      )
                      AND citta LIKE ?
                    LIMIT 5
                """, (
                    email,
                    f"%{kw}%", f"%{kw}%",
                    f"%{settore[:12]}%", f"%{settore[:12]}%",
                    f"%{citta}%" if citta else "%",
                )).fetchall()
            return [
                {
                    "page_name": r[0],
                    "settore":   r[5] or r[1],
                    "citta":     r[2],
                    "website":   r[3],
                    "score":     r[4],
                }
                for r in rows if r[0]  # skip empty names
            ]
        except Exception as e:
            print(f"[COMPETITOR] DB query error: {e}")
            return []

    # ──────────────────────────────────────────────────────────────────────
    # AI synthesis
    # ──────────────────────────────────────────────────────────────────────

    def _synthesize(self, lead: dict, competitors: list) -> dict:
        nome    = lead.get("page_name", "?")
        settore = lead.get("settore_calibrato", lead.get("settore", ""))
        citta   = lead.get("citta", "")

        comp_text = "\n".join([
            f"  - {c['page_name']} | Sito: {'Sì' if c.get('website') else 'No'} | Score qualità: {c.get('score', '?')}/100"
            for c in competitors[:3]
        ])

        prompt = f"""Competitor analysis per:
TARGET: {nome} ({settore}, {citta})

COMPETITOR TROVATI NEL MERCATO LOCALE:
{comp_text}

Sintetizza l'intelligence competitiva. Restituisci SOLO il JSON."""

        messages = [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ]

        testo = call_ai(self.rotation, messages, max_tokens=300, temperature=0.3, label="COMPETITOR")
        if testo:
            try:
                start = testo.find("{")
                end   = testo.rfind("}") + 1
                if start >= 0 and end > start:
                    return json.loads(testo[start:end])
            except json.JSONDecodeError:
                pass

        # Fallback deterministico
        c1 = competitors[0] if competitors else {"page_name": "competitor locale"}
        c2 = competitors[1] if len(competitors) > 1 else {"page_name": "secondo competitor"}
        return {
            "competitor_1": {
                "nome": c1["page_name"],
                "vantaggio": "presenza online con sito web",
                "debolezza": "landing page non ottimizzata per conversione",
            },
            "competitor_2": {
                "nome": c2["page_name"],
                "vantaggio": "già trovabile su Google Maps",
                "debolezza": "nessun sistema di prenotazione online",
            },
            "insight_mercato": (
                f"Il mercato {settore} a {citta} ha già {len(competitors)} competitor attivi online "
                f"che acquisiscono clienti digitalmente."
            ),
            "opportunita_lead": (
                "Ottimizzare la conversione ora significa battere chi è già online ma non converte."
            ),
        }

    # ──────────────────────────────────────────────────────────────────────
    # Public interface
    # ──────────────────────────────────────────────────────────────────────

    def analyze(self, lead: dict) -> dict:
        nome = lead.get("page_name", "?")
        competitors = self._find_in_db(lead)

        if not competitors:
            settore = lead.get("settore_calibrato", lead.get("settore", ""))
            citta   = lead.get("citta", "")
            print(f"[COMPETITOR] {nome}: nessun competitor nel DB per {settore}/{citta}")
            return {
                **lead,
                "competitor_intel": {
                    "available": False,
                    "insight_mercato": (
                        f"Il mercato locale {settore} sta migrando verso l'acquisizione online."
                    ),
                    "opportunita_lead": "Chi ottimizza la conversione prima domina il segmento locale.",
                }
            }

        intel = self._synthesize(lead, competitors)
        print(f"[COMPETITOR] {nome}: {len(competitors)} competitor analizzati")
        return {**lead, "competitor_intel": {"available": True, "n_competitor": len(competitors), **intel}}

    def run(self, leads: list) -> list:
        print(f"\n[COMPETITOR] Ricerca competitor per {len(leads)} lead...")
        results = [self.analyze(lead) for lead in leads]
        n_ok = sum(1 for r in results if r.get("competitor_intel", {}).get("available"))
        print(f"[COMPETITOR] Completato: {n_ok}/{len(leads)} con intelligence competitiva")
        return results
