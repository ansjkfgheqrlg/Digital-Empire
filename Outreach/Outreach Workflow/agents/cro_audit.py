"""
Operations Audit Agent — Team DEEP-INTEL (Sub-Agent B)
Analizza website_intelligence con AI per estrarre OSSERVAZIONI OPERATIVE reali
sul business del lead e capire quale delle 3 implementazioni AI è il gancio giusto.

NON è un audit CRO della landing page: legge il sito per capire COME LAVORA il
business (outreach manuale? produzione contenuti intensa? team/processi complessi?)
e suggerisce il prodotto-gancio tra Outreach Factory, Content Factory, Second Brain.

Dipendenza: deve girare DOPO ResearchAgent (usa website_intelligence).
Modello: rotazione Groq → OpenRouter (stesso pattern del resto del sistema).

Compatibilità: la classe resta CROAuditAgent e l'output resta sotto la chiave
"cro_audit" con gli stessi campi (problema_1..3{titolo,evidenza,impatto},
cro_score, apertura_suggerita), perché lead_analyzer e insight li consumano.
Cambia solo la SEMANTICA del contenuto: "problema" = osservazione/leva operativa.
"""

import json
import time
import openai
from agents.ai_client import build_rotation, call_ai


_SYSTEM_PROMPT = """Sei il Solutions Engineer di Digital Empire, specializzato nel leggere un business dal suo sito e capire quale automazione AI gli farebbe risparmiare più ore.

Digital Empire NON vende landing page né conversioni. Vende 3 IMPLEMENTAZIONI AI (workflow chiavi in mano):
  1. OUTREACH FACTORY — automatizza al 100% l'acquisizione clienti (scraping lead, scrittura e invio messaggi, follow-up). Per chi fa outreach/lead-gen a mano, vende servizi/consulenze, è un'agenzia, cerca clienti attivamente.
  2. CONTENT FACTORY — genera contenuti social/blog con l'AI in volume e in modo coerente. Per chi pubblica molto, ha blog/social attivi, vende corsi/info-prodotti, gestisce un ecommerce con tante creatività.
  3. SECOND BRAIN — memoria/contesto permanente per l'LLM: l'AI conosce il business, i processi, i clienti. Per chi ha un team, processi documentati, usa già molta AI, ha una struttura complessa.

La leva NON è "convertire di più", è OPERATIVITÀ: fargli fare in automatico ciò che oggi fa a mano.

Il tuo compito: dai dati estratti dal sito, estrai 2-3 OSSERVAZIONI OPERATIVE REALI su come lavora questo business e suggerisci quale dei 3 prodotti è il gancio giusto.

COSA CERCARE NEI DATI (segnali operativi, NON difetti di conversione):
- CTA/servizi tipo "richiedi preventivo", "consulenza", "contattaci" → vendono servizi a mano → segnale OUTREACH FACTORY
- Blog, sezione articoli, molti contenuti, "scopri il corso", shop con tanti prodotti → producono contenuti a mano → segnale CONTENT FACTORY
- "il nostro team", più sedi, processi/metodologia descritti, molte pagine → struttura complessa → segnale SECOND BRAIN
- Settore agenzia / freelance marketing (SMM, copy, ads) → quasi sempre OUTREACH FACTORY o CONTENT FACTORY

REGOLE FONDAMENTALI:
- Usa SOLO i dati REALI forniti — mai inventare osservazioni non supportate dai dati
- Sii SPECIFICO: "Vendono consulenze ma raccolgono contatti solo con un form manuale" non "potrebbero automatizzare"
- Ogni osservazione è una LEVA OPERATIVA: cosa fanno a mano oggi che l'AI può fare al posto loro
- Tono: collega esperto che ha capito come lavorano, non venditore di conversioni
- NON parlare mai di tasso di conversione, bottoni, urgenza, scarsità: parla di ORE risparmiate e operatività automatizzata

OUTPUT OBBLIGATORIO — JSON valido, nient'altro:
{
  "problema_1": {
    "titolo": "<la leva operativa principale, max 8 parole — es: 'Acquisizione clienti tutta manuale'>",
    "evidenza": "<dato reale estratto dal sito, max 20 parole>",
    "impatto": "<ore/settimana sprecate o opportunità non sfruttate, max 15 parole>"
  },
  "problema_2": {
    "titolo": "<idem>",
    "evidenza": "<idem>",
    "impatto": "<idem>"
  },
  "problema_3": {
    "titolo": "<idem>",
    "evidenza": "<idem>",
    "impatto": "<idem>"
  },
  "cro_score": <intero 0-10 — quanto è FORTE il gancio operativo: 0=nessun segnale di lavoro manuale automatizzabile, 10=business pieno di processi manuali che le 3 Factory eliminerebbero>,
  "prodotto_gancio": "<uno tra 'Outreach Factory', 'Content Factory', 'Second Brain' — il più adatto a questo business>",
  "apertura_suggerita": "<1-2 frasi per aprire l'email — parti dall'osservazione operativa concreta e dal tempo che stanno perdendo, NON da 'Ciao'>"
}"""


class CROAuditAgent:
    """
    Sub-Agent B del Team DEEP-INTEL.
    Riceve lead con website_intelligence e produce cro_audit con 3 problemi specifici.
    """

    def __init__(self, openrouter_api_key: str):
        self.rotation = build_rotation(openrouter_api_key)

    def _build_prompt(self, lead: dict, intel: dict) -> str:
        nome    = lead.get("page_name", "?")
        settore = lead.get("settore_calibrato", lead.get("settore", ""))
        citta   = lead.get("citta", "")

        meta     = intel.get("meta", {})
        headings = intel.get("headings", {})
        ctas     = intel.get("ctas", [])
        sp       = intel.get("social_proof", {})
        contact  = intel.get("contact", {})
        issues   = intel.get("issues", [])

        return f"""Analizza questo sito web e identifica i 3 problemi CRO più critici:

BUSINESS: {nome} | SETTORE: {settore} | CITTÀ: {citta}
URL: {intel.get("url", "N/A")} | LOAD TIME: {intel.get("load_time_s", "?")}s

TITOLO PAGINA: {meta.get("title") or "assente"}
META DESCRIPTION: {meta.get("description")[:100] if meta.get("description") else "assente"}

H1: {headings.get("h1") or ["assente"]}
H2 principali: {headings.get("h2", [])[:3]}

CTA trovate: {ctas if ctas else "NESSUNA — homepage senza bottoni call-to-action"}
Form contatto: {"Sì" if intel.get("has_form") else "NO"}
Prenotazione online: {"Sì" if intel.get("has_booking") else "NO"}
Telefono visibile: {contact.get("phone") or "NON TROVATO"}
Mobile-friendly: {"Sì" if intel.get("has_mobile") else "NO"}

Social proof score: {sp.get("score", 0)}/10
Segnali trovati: {sp.get("keywords", []) or "nessuno"}
Valutazioni a stelle: {"Sì" if sp.get("has_star_ratings") else "No"}

Problemi CRO rilevati automaticamente ({len(issues)}):
{chr(10).join(f"  - {p}" for p in issues) if issues else "  - Nessuno (sito relativamente ben strutturato)"}

Restituisci SOLO il JSON con i 3 problemi specifici per QUESTO sito."""

    def audit(self, lead: dict) -> dict:
        nome  = lead.get("page_name", "?")
        intel = lead.get("website_intelligence", {})

        if not intel.get("available"):
            return {**lead, "cro_audit": {"available": False, "reason": intel.get("reason", "no_site")}}

        prompt   = self._build_prompt(lead, intel)
        messages = [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ]

        testo = call_ai(self.rotation, messages, max_tokens=450, temperature=0.2, label="CRO_AUDIT")

        if testo:
            try:
                start = testo.find("{")
                end   = testo.rfind("}") + 1
                if start >= 0 and end > start:
                    result = json.loads(testo[start:end])
                    print(f"[CRO_AUDIT] {nome}: score={result.get('cro_score', '?')}/10")
                    return {**lead, "cro_audit": {"available": True, **result}}
            except json.JSONDecodeError:
                pass

        # Fallback deterministico — usa i dati rule-based
        issues = intel.get("issues", [])
        ctas   = intel.get("ctas", [])
        sp     = intel.get("social_proof", {})
        load   = intel.get("load_time_s", 0)
        settore = lead.get("settore_calibrato", lead.get("settore", ""))

        fallback_score = max(10 - len(issues) * 1.2, 1)
        print(f"[CRO_AUDIT] {nome}: fallback deterministico ({len(issues)} issues)")

        p1 = {
            "titolo": f"{'Nessuna CTA' if not ctas else 'CTA insufficienti'} sulla homepage",
            "evidenza": f"{len(ctas)} CTA trovate — {'zero bottoni visibili' if not ctas else 'non abbastanza chiari'}",
            "impatto": "20-35% visitatori escono senza compiere alcuna azione",
        }
        p2 = {
            "titolo": "Social proof assente o debole",
            "evidenza": f"Score: {sp.get('score', 0)}/10 — {sp.get('keywords', ['nessun segnale trovato'])[0] if sp.get('keywords') else 'nessuna recensione/testimonianza visibile'}",
            "impatto": "Bassa fiducia iniziale = minor conversione del 40%",
        }
        p3_titolo = f"Sito lento ({load}s)" if load > 3 else (issues[2].replace("_", " ") if len(issues) > 2 else "Ottimizzazione mobile assente")
        p3 = {
            "titolo": p3_titolo,
            "evidenza": f"Load time {load}s" if load > 3 else "Verifica necessaria",
            "impatto": "Ogni secondo in più = 7% abbandoni in più",
        }

        return {
            **lead,
            "cro_audit": {
                "available": True,
                "problema_1": p1,
                "problema_2": p2,
                "problema_3": p3,
                "cro_score": int(fallback_score),
                "apertura_suggerita": (
                    f"Ho analizzato il sito di {lead.get('page_name', 'questa attività')} come {settore} "
                    f"e ho trovato {len(issues)} aspetti che probabilmente stanno costando clienti ogni mese."
                ),
            }
        }

    def run(self, leads: list) -> list:
        print(f"\n[CRO_AUDIT] Audit CRO su {len(leads)} siti...")
        results = []
        for lead in leads:
            results.append(self.audit(lead))
            time.sleep(0.8)
        n_ok = sum(1 for r in results if r.get("cro_audit", {}).get("available"))
        print(f"[CRO_AUDIT] Completato: {n_ok}/{len(leads)} audit prodotti")
        return results
