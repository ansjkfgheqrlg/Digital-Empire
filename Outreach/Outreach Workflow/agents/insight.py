"""
Insight Agent — Team SYNTHESIS
Il "cervello" che trasforma dati grezzi in munizioni per il Writer.

Riceve:
  - website_intelligence (da ResearchAgent)
  - cro_audit (da CROAuditAgent)
  - competitor_intel (da CompetitorAgent)

Produce:
  - insight_brief: 3 problemi specifici + apertura email suggerita

Questo è il passaggio che trasforma una cold email generica
in una che inizia: "Ho guardato il tuo sito — ho trovato X, Y, Z."
"""

import json
import time

from agents.ai_client import build_rotation, call_ai


_SYSTEM_PROMPT = """Sei l'Insight Director di Digital Empire.

Il tuo compito: sintetizzare tutta l'intelligence raccolta su un lead in 3 problemi
SPECIFICI, CONCRETI, VERIFICABILI — che il Writer userà per scrivere l'email.

PRINCIPIO FONDAMENTALE:
"Ho guardato il tuo sito — ho trovato questo, questo e questo."
Ogni problema deve essere VERIFICABILE dalla lettura del sito, non ipotetico.

COME COSTRUIRE L'APERTURA EMAIL:
Non scrivere "Ciao" o introduzioni su di te.
Inizia con un'osservazione concreta e verificata.

ESEMPIO BUONO:
  "Ho aperto il sito di [nome] stamattina — non c'è un solo bottone per prenotare.
   Ho cercato il form di contatto: c'è solo un numero di telefono nel footer."

ESEMPIO SBAGLIATO (troppo generico):
  "Ho analizzato la tua presenza online e ho notato alcune aree di miglioramento."

FORMATO TONO:
- Seconda persona singolare: "il tuo sito", "hai", "stai"
- Osservativo, non accusatorio: "ho notato" non "stai sbagliando"
- Specifico con dati reali: "3.8 secondi di caricamento" non "il sito è lento"

OUTPUT OBBLIGATORIO — JSON valido:
{
  "problema_principale": {
    "testo": "<osservazione specifica + evidenza in 1-2 frasi, max 35 parole>",
    "dato_reale": "<numero/fatto verificato — es: '0 CTA trovate', 'load 4.2s', 'no form'>",
    "impatto_stimato": "<perdita concreta mensile, max 15 parole>"
  },
  "problema_2": {
    "testo": "<idem>",
    "dato_reale": "<idem>",
    "impatto_stimato": "<idem>"
  },
  "problema_3": {
    "testo": "<idem>",
    "dato_reale": "<idem>",
    "impatto_stimato": "<idem>"
  },
  "apertura_email": "<2-3 frasi per aprire l'email — inizia dall'osservazione concreta, scrivi come se avessi davvero aperto il loro sito, max 50 parole>",
  "insight_score": <1-10 — quanto è potente questo brief? 8+ = problemi evidenti e specifici>
}"""


class InsightAgent:
    """
    Team SYNTHESIS — sintetizza Research + CROAudit + Competitor in insight_brief.
    È l'agente che trasforma i dati in narrativa persuasiva per il Writer.
    """

    def __init__(self, openrouter_api_key: str):
        self.rotation = build_rotation(openrouter_api_key)

    def _build_context(self, lead: dict) -> str:
        """Costruisce il contesto completo per la sintesi AI."""
        nome    = lead.get("page_name", "?")
        settore = lead.get("settore_calibrato", lead.get("settore", ""))
        citta   = lead.get("citta", "")

        intel    = lead.get("website_intelligence", {})
        cro      = lead.get("cro_audit", {})
        comp     = lead.get("competitor_intel", {})

        lines = [f"LEAD: {nome} | Settore: {settore} | Città: {citta}\n"]

        # Website intelligence
        if intel.get("available"):
            meta     = intel.get("meta", {})
            headings = intel.get("headings", {})
            ctas     = intel.get("ctas", [])
            sp       = intel.get("social_proof", {})
            contact  = intel.get("contact", {})
            issues   = intel.get("issues", [])

            lines.append(f"DATI SITO ({intel.get('url', 'N/A')}):")
            lines.append(f"  Load time: {intel.get('load_time_s', '?')}s")
            lines.append(f"  Titolo: {meta.get('title') or 'assente'}")
            lines.append(f"  Meta desc: {('assente' if not meta.get('description') else meta['description'][:80])}")
            lines.append(f"  H1: {headings.get('h1') or ['ASSENTE']}")
            lines.append(f"  CTA trovate: {ctas if ctas else 'NESSUNA'}")
            lines.append(f"  Form contatto: {'Sì' if intel.get('has_form') else 'NO'}")
            lines.append(f"  Prenotazione online: {'Sì' if intel.get('has_booking') else 'NO'}")
            lines.append(f"  Telefono: {contact.get('phone') or 'non trovato'}")
            lines.append(f"  Mobile viewport: {'Sì' if intel.get('has_mobile') else 'NO'}")
            lines.append(f"  Social proof score: {sp.get('score', 0)}/10")
            lines.append(f"  Issues CRO ({len(issues)}): {issues}")
        else:
            lines.append(f"SITO: {intel.get('reason', 'non analizzabile')}")

        # CRO Audit
        if cro.get("available"):
            lines.append(f"\nAUDIT CRO (score: {cro.get('cro_score', '?')}/10):")
            for k in ["problema_1", "problema_2", "problema_3"]:
                p = cro.get(k, {})
                if p:
                    lines.append(f"  {k}: {p.get('titolo', '')} — {p.get('evidenza', '')}")
            if cro.get("apertura_suggerita"):
                lines.append(f"  Apertura suggerita dall'audit: {cro['apertura_suggerita']}")

        # Competitor
        if comp.get("available"):
            lines.append(f"\nINTELLIGENCE COMPETITIVA ({comp.get('n_competitor', '?')} competitor):")
            lines.append(f"  Insight mercato: {comp.get('insight_mercato', '')}")
            lines.append(f"  Opportunità: {comp.get('opportunita_lead', '')}")

        return "\n".join(lines)

    def synthesize(self, lead: dict) -> dict:
        nome  = lead.get("page_name", "?")
        intel = lead.get("website_intelligence", {})
        cro   = lead.get("cro_audit", {})

        # Se non abbiamo dati reali, skip (il Strategist userà il suo approccio standard)
        has_data = intel.get("available") or cro.get("available")
        if not has_data:
            return {**lead, "insight_brief": {"available": False, "reason": "no_website_data"}}

        context = self._build_context(lead)
        prompt  = f"{context}\n\nSintetizza i 3 problemi più impattanti per questo lead specifico. Restituisci SOLO il JSON."

        messages = [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ]

        testo = call_ai(self.rotation, messages, max_tokens=550, temperature=0.25, label="INSIGHT")

        if testo:
            try:
                start = testo.find("{")
                end   = testo.rfind("}") + 1
                if start >= 0 and end > start:
                    brief = json.loads(testo[start:end])
                    score = brief.get("insight_score", 5)
                    print(f"[INSIGHT] {nome}: insight_score={score}/10")
                    return {**lead, "insight_brief": {"available": True, **brief}}
            except json.JSONDecodeError:
                pass

        # Fallback: costruisce brief dai dati disponibili senza AI aggiuntiva
        return self._fallback_brief(lead)

    def _fallback_brief(self, lead: dict) -> dict:
        nome    = lead.get("page_name", "?")
        settore = lead.get("settore_calibrato", lead.get("settore", ""))
        citta   = lead.get("citta", "")
        intel   = lead.get("website_intelligence", {})
        cro     = lead.get("cro_audit", {})

        # Usa i dati CRO audit se disponibili
        if cro.get("available"):
            p1 = cro.get("problema_1", {})
            p2 = cro.get("problema_2", {})
            p3 = cro.get("problema_3", {})
            apertura = cro.get("apertura_suggerita", "")
        else:
            issues = intel.get("issues", []) if intel.get("available") else []
            ctas   = intel.get("ctas", []) if intel.get("available") else []
            load   = intel.get("load_time_s", 0) if intel.get("available") else 0

            p1 = {"testo": "CTA assenti o insufficienti", "dato_reale": f"{len(ctas)} CTA trovate", "impatto_stimato": "visitatori escono senza azioni"}
            p2 = {"testo": "Social proof debole", "dato_reale": f"Score {intel.get('social_proof', {}).get('score', 0)}/10", "impatto_stimato": "bassa fiducia iniziale"}
            p3 = {"testo": f"{'Sito lento' if load > 3 else 'Form contatto assente'}", "dato_reale": f"{load}s load" if load > 3 else "no form", "impatto_stimato": "clienti persi"}
            apertura = f"Ho aperto il sito di {nome} e ho trovato alcune cose che probabilmente stanno costando clienti ogni mese."

        print(f"[INSIGHT] {nome}: fallback brief (dati AI non disponibili)")
        return {
            **lead,
            "insight_brief": {
                "available": True,
                "problema_principale": p1,
                "problema_2": p2,
                "problema_3": p3,
                "apertura_email": apertura or f"Ho analizzato il sito di {nome} come {settore} a {citta}.",
                "insight_score": 5,
            }
        }

    def run(self, leads: list) -> list:
        print(f"\n[INSIGHT] Sintesi intelligence per {len(leads)} lead...")
        results = []
        for lead in leads:
            results.append(self.synthesize(lead))
            time.sleep(1.2)
        n_ok = sum(1 for r in results if r.get("insight_brief", {}).get("available"))
        print(f"[INSIGHT] Completato: {n_ok}/{len(leads)} brief con dati reali")
        return results
