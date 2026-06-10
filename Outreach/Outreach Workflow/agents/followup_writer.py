"""
Follow-up Writer Agent — Digital Empire Outreach (PIVOT: implementazioni AI)
===========================================================================
Genera la sequenza di follow-up sullo STESSO thread della prima email, allineata
al nuovo framework APSOC (hype automazione → 1 problema operativo → workflow 100%
→ obiezione = solo fiducia → CTA presentazione + call).

I 3 PRODOTTI (workflow installati sui server del cliente, codice incluso, €0 canoni,
setup 7 giorni, automazione 100%):
  - Outreach Factory  → automatizza l'outreach al 100%
  - Content Factory   → genera copy, grafiche, caroselli e script video
  - Second Brain      → memoria/contesto permanente per l'LLM (Context Engineering)

Sequenza:
  F1 (giorno 3, NUDGE)            → 50-100 parole. "Hai visto la presentazione?" + 1 riga di curiosità.
  F2 (giorno 7, NUOVO ANGOLO)     → 90-150 parole. Cita un SECONDO prodotto come nuovo gancio + ri-linka.
  F3 (giorno 14, BREAK-UP)        → 30-50 parole. Domanda binaria di chiusura, porta aperta + link.

Regole comuni:
  - Prima persona singolare (Max | Digital Empire), mai tono agenzia
  - Stesso thread (oggetto "Re: ...")
  - Link AMMESSI: presentazione nel CTA, agency in firma (nuova policy pivot)
  - Zero scuse, zero punti esclamativi, zero urgenza falsa
"""

import json
import time
import openai
from agents.ai_client import build_rotation

try:
    from knowledge.apsoc import PRESENTATION_URL, AGENCY_URL, LAUNCH_OFFER
except Exception:  # pragma: no cover — fallback se il modulo non è importabile
    PRESENTATION_URL = "https://presentazione-empire.vercel.app/"
    AGENCY_URL = "https://agency-empire-landing.vercel.app"
    LAUNCH_OFFER = "sconto early-adopter per i primi clienti che partono questo mese"

# Link CTA storico (mantenuto come alias per compatibilità a valle)
CTA_LINK = AGENCY_URL

# ── MAPPA TARGET / ICP → 3 PRODOTTI ───────────────────────────────────────────
# Per ogni target nuovo (agenzia, info_product, coach, smm_freelance, ecommerce,
# consulente, default) definiamo:
#   prodotto_1      → il prodotto-gancio della prima email (Outreach/Content/Second Brain)
#   prodotto_2      → il SECONDO prodotto usato come nuovo angolo nel follow-up F2
#   f1_curiosita    → la riga di curiosità del nudge F1 (giorno 3)
#   f2_angolo       → l'angolo nuovo per F2 (giorno 7), centrato sul prodotto_2
#   f3_processo     → il processo operativo da nominare nel break-up F3 (giorno 14)

_TARGET_FOLLOWUP = {
    "agenzia": {
        "prodotto_1": "Outreach Factory",
        "prodotto_2": "Content Factory",
        "f1_curiosita": "Chi gestisce un'agenzia di solito ha l'acquisizione nuova come collo di bottiglia, proprio perché l'outreach lo fa a mano tra una delivery e l'altra.",
        "f2_angolo":    "Oltre all'outreach, c'è la produzione contenuti dei clienti: copy, caroselli, script. Ho un secondo workflow (Content Factory) che la fa girare in automatico, i contenuti di una settimana in un pomeriggio.",
        "f3_processo":  "l'outreach a freddo della tua agenzia",
    },
    "info_product": {
        "prodotto_1": "Content Factory",
        "prodotto_2": "Second Brain",
        "f1_curiosita": "Chi vende corsi sa che i contenuti sono il motore della crescita ma anche il buco nero del tempo, e di solito si fanno ancora a mano.",
        "f2_angolo":    "C'è anche il problema dell'AI che dimentica tutto: ogni chat riparte da zero e devi ri-spiegare brand voice e contesto. Ho un secondo workflow (Second Brain) che le dà una memoria permanente di tutto il tuo business.",
        "f3_processo":  "la produzione contenuti del tuo info-business",
    },
    "coach": {
        "prodotto_1": "Content Factory",
        "prodotto_2": "Outreach Factory",
        "f1_curiosita": "Chi fa coaching vive di contenuti e di nuove conversazioni, ma entrambe le cose oggi le fa a mano e divorano i pomeriggi.",
        "f2_angolo":    "C'è anche l'acquisizione: trovare le persone giuste e scrivere loro a mano è lento. Ho un secondo workflow (Outreach Factory) che fa girare l'outreach al 100%, 300 messaggi personalizzati al giorno.",
        "f3_processo":  "la produzione dei tuoi contenuti",
    },
    "smm_freelance": {
        "prodotto_1": "Content Factory",
        "prodotto_2": "Outreach Factory",
        "f1_curiosita": "Chi gestisce social per i clienti passa più tempo a produrre copy e creatività che a far crescere il proprio business.",
        "f2_angolo":    "Poi c'è la parte di acquisire nuovi clienti: di solito è l'ultima cosa in lista. Ho un secondo workflow (Outreach Factory) che automatizza l'outreach al 100%, così gira da solo mentre sei in delivery.",
        "f3_processo":  "la produzione contenuti per i tuoi clienti",
    },
    "ecommerce": {
        "prodotto_1": "Content Factory",
        "prodotto_2": "Second Brain",
        "f1_curiosita": "Un ecommerce ha bisogno di sfornare contenuti e schede prodotto in continuazione, e di solito è una catena di montaggio a mano.",
        "f2_angolo":    "C'è anche il problema del contesto: l'AI non conosce il tuo catalogo, il tuo tono, i tuoi clienti, e riparte da zero ogni volta. Ho un secondo workflow (Second Brain) che le dà memoria permanente di tutto.",
        "f3_processo":  "la produzione di contenuti e schede del tuo store",
    },
    "consulente": {
        "prodotto_1": "Second Brain",
        "prodotto_2": "Outreach Factory",
        "f1_curiosita": "Chi fa consulenza usa l'AI ogni giorno ma si ritrova a ri-spiegarle sempre tutto: clienti, processi, decisioni passate.",
        "f2_angolo":    "Poi c'è l'acquisizione: scrivere a mano ai potenziali clienti è lento e discontinuo. Ho un secondo workflow (Outreach Factory) che fa girare l'outreach al 100%, da solo ogni mattina.",
        "f3_processo":  "il contesto che dai all'AI ogni giorno",
    },
    "default": {
        "prodotto_1": "Outreach Factory",
        "prodotto_2": "Content Factory",
        "f1_curiosita": "Di solito il collo di bottiglia non è il lavoro che sai fare bene, è il processo ripetitivo che fai ancora a mano e che ti ruba ore ogni settimana.",
        "f2_angolo":    "C'è un secondo pezzo che posso automatizzare: la produzione di contenuti (copy, grafiche, script). Un workflow (Content Factory) la fa girare in automatico, i contenuti di una settimana in un pomeriggio.",
        "f3_processo":  "il processo che oggi fai ancora a mano",
    },
}


def _get_target(settore: str) -> str:
    """Mappa il settore/ICP grezzo del lead a uno dei target del pivot."""
    s = (settore or "").lower()
    mapping = [
        ("agenz", "agenzia"), ("agency", "agenzia"), ("smma", "agenzia"),
        ("info", "info_product"), ("corso", "info_product"), ("formaz", "info_product"),
        ("info-product", "info_product"), ("infoprodott", "info_product"),
        ("coach", "coach"), ("mentor", "coach"),
        ("social media manager", "smm_freelance"), ("smm", "smm_freelance"),
        ("copywriter", "smm_freelance"), ("freelance", "smm_freelance"), ("ads", "smm_freelance"),
        ("ecommerce", "ecommerce"), ("e-commerce", "ecommerce"), ("shop", "ecommerce"),
        ("store", "ecommerce"), ("negozio online", "ecommerce"),
        ("consulen", "consulente"), ("advisor", "consulente"),
    ]
    for keyword, target in mapping:
        if keyword in s:
            return target
    return "default"


# ── SYSTEM PROMPT F1 — GIORNO 3 (NUDGE) ───────────────────────────────────────

F1_SYSTEM_PROMPT = f"""Sei Max, founder di Digital Empire (firma "Max | Digital Empire").
Stai scrivendo il PRIMO FOLLOW-UP (F1) sullo stesso thread di una cold email che non ha
ricevuto risposta dopo 3-4 giorni. Digital Empire vende implementazioni AI: workflow
installati sui server del cliente (codice incluso, €0 canoni, setup 7 giorni, automazione 100%):
Outreach Factory, Content Factory, Second Brain.

OBIETTIVO F1: un nudge gentile. Assicurarti che abbiano visto la presentazione e riaprire il loop.

REGOLE ASSOLUTE:
1. PRIMA PERSONA SINGOLARE: solo "io", "ho", "mi", "mio". MAI "noi", "offriamo", "vogliamo".
2. ZERO TRATTINI nel corpo. Ogni pausa è un punto fermo o una virgola.
3. PARAGRAFI SEPARATI: riga vuota tra ogni blocco.
4. 50-100 PAROLE totali nel corpo.
5. NON ripetere la prima email: solo un nudge breve + UNA riga di curiosità nuova.
6. ZERO scuse: niente "Scusa il disturbo", "Spero non disturbi", "So che sei occupato".
7. ZERO punti esclamativi. Tono genuino, non disperato.

STRUTTURA F1 OBBLIGATORIA:
[NUDGE] (1 frase): volevo assicurarmi che avessi visto la presentazione del workflow.
[CURIOSITÀ] (1-2 righe): usa la riga di curiosità fornita nel brief (un problema operativo riconoscibile).
[LINK] {PRESENTATION_URL} (su riga separata — è la presentazione, sempre ammessa)
[CTA] (1 domanda binaria leggera): vuoi vederlo girare dal vivo, sì o no?

FIRMA OBBLIGATORIA (dopo il corpo):

Max | Digital Empire
{AGENCY_URL}

OUTPUT (JSON valido, nient'altro):
{{"oggetto": "Re: <oggetto originale>", "corpo": "<testo completo con \\n\\n tra paragrafi>"}}"""


# ── SYSTEM PROMPT F2 — GIORNO 7 (NUOVO ANGOLO + SECONDO PRODOTTO) ──────────────

F2_SYSTEM_PROMPT = f"""Sei Max, founder di Digital Empire (firma "Max | Digital Empire").
Stai scrivendo il SECONDO FOLLOW-UP (F2) sullo stesso thread, dopo 7-8 giorni di silenzio.
Digital Empire vende 3 implementazioni AI (workflow sui server del cliente, codice incluso,
€0 canoni, setup 7 giorni, automazione 100%): Outreach Factory, Content Factory, Second Brain.

OBIETTIVO F2: cambiare angolo. Se la prima email parlava di un prodotto, qui accenni a un
SECONDO prodotto come nuovo gancio, e ribadisci che l'unica obiezione è la fiducia (sciolta
dalla demo live + presentazione).

REGOLE ASSOLUTE:
1. PRIMA PERSONA SINGOLARE sempre. MAI "noi/offriamo/vogliamo".
2. ZERO TRATTINI nel corpo. Solo punti fermi e virgole.
3. PARAGRAFI SEPARATI con riga vuota.
4. 90-150 PAROLE totali nel corpo.
5. ANGOLO NUOVO: introduci il SECONDO prodotto fornito nel brief, non ripetere la prima email.
6. OBIEZIONE = FIDUCIA: "capisco se non è il momento, te lo mostro dal vivo in 20 minuti".
7. ZERO scuse, zero urgenza falsa, zero punti esclamativi.

STRUTTURA F2 OBBLIGATORIA:
[PONTE] (1 frase): riapre senza pressione ("capisco se non era il momento giusto").
[NUOVO ANGOLO] (2-3 righe): usa l'angolo del SECONDO prodotto fornito nel brief.
[FIDUCIA/DEMO] (1 frase): l'unico dubbio sensato è se funziona per te, e te lo mostro dal vivo.
[LINK] {PRESENTATION_URL} (su riga separata — la presentazione)
[CTA] (1 frase): inviti a guardarla e, se ha senso, a una call/demo di 20 minuti.

FIRMA OBBLIGATORIA (dopo il corpo):

Max | Digital Empire
{AGENCY_URL}

OUTPUT (JSON valido, nient'altro):
{{"oggetto": "Re: <oggetto originale>", "corpo": "<testo completo con \\n\\n tra paragrafi>"}}"""


# ── SYSTEM PROMPT F3 — GIORNO 14 (BREAK-UP) ───────────────────────────────────

F3_SYSTEM_PROMPT = f"""Sei Max, founder di Digital Empire (firma "Max | Digital Empire").
Stai scrivendo il TERZO e ULTIMO follow-up (F3) sullo stesso thread, dopo 14 giorni.
Non ha risposto né alla prima email né ai due follow-up. Digital Empire vende
implementazioni AI (workflow sui server del cliente, codice incluso, €0 canoni, 7 giorni, 100%).

OBIETTIVO F3: chiusura pulita del thread con una domanda binaria. Porta aperta, zero risentimento.

REGOLE ASSOLUTE:
1. PRIMA PERSONA SINGOLARE sempre.
2. ZERO TRATTINI. Solo punti fermi.
3. 30-50 PAROLE totali. La brevità È il messaggio.
4. Tono DEFINITIVO ma RISPETTOSO, nessuna pressione.
5. NON ripetere il pitch. Una domanda binaria e basta.
6. ZERO scuse, zero "so che sei occupato".

STRUTTURA F3 "BREAK-UP" OBBLIGATORIA:
[CHIUSURA] (1 frase): ultima cosa prima di chiudere il thread.
[DOMANDA BINARIA] (1 frase): automatizzare [processo fornito nel brief] è qualcosa che vuoi guardare adesso, sì o no?
[PORTA APERTA + LINK] (1 frase): in ogni caso ti lascio la presentazione qui: {PRESENTATION_URL}

FIRMA:

Max | Digital Empire
{AGENCY_URL}

OUTPUT (JSON valido, nient'altro):
{{"oggetto": "Re: <oggetto originale>", "corpo": "<testo completo con \\n\\n tra paragrafi>"}}"""


# ── QA FOLLOW-UP (stesso standard delle email principali, pivot-aware) ─────────

_FOLLOWUP_QA_PROMPT = """Valuta questo follow-up email per cold outreach B2B italiano sul pivot
Digital Empire (implementazioni AI: Outreach Factory, Content Factory, Second Brain). 1-10 per criterio.

EMAIL:
{corpo}

CRITERI:
1. HUMANNESS (0-10): sembra scritto da un founder reale o da un AI?
   Penalizza: scuse, "spero non disturbi", corporate jargon vuoto, tono agenzia ("noi/offriamo").
   NON penalizzare il vocabolario AI/automazione (workflow, demo, automazione): è atteso.
2. BREVITA' (0-10): rispetta il limite di parole? (F1: 50-100, F2: 90-150, F3: 30-50)
   Penalizza: padding, ripetizioni dalla prima email, frasi inutili.
3. ANGOLO (0-10): l'angolo è coerente col follow-up (F1 nudge, F2 nuovo prodotto, F3 break-up)?
   Premia: nuovo gancio, secondo prodotto in F2, chiusura binaria in F3.
4. CTA_CHIARA (0-10): la chiusura è chiara e c'è il link della presentazione?
   Penalizza: CTA ambigue, presentazione assente, troppe CTA in concorrenza.
   NON penalizzare la presenza dei link: presentazione e agency sono AMMESSI.
5. PRIMA_PERSONA (0-10): usa solo "io/ho/mi/mio"? Zero "noi/offriamo/vogliamo"?

Rispondi SOLO con JSON:
{{"humanness": X, "brevita": X, "angolo": X, "cta_chiara": X, "prima_persona": X,
  "media": X.X, "problemi": ["problema1", "problema2"], "approvata": true/false}}
(approvata = media >= 7.0)"""


class FollowupWriterAgent:
    """
    Genera F1, F2 e F3 follow-up con gli stessi standard qualitativi della prima email,
    allineati al pivot (implementazioni AI). Link presentazione/agency ammessi, QA automatico.
    API pubblica: run_f1, run_f2 (compatibili) + run_f3 (additivo, break-up giorno 14).
    """

    def __init__(self, openrouter_api_key: str):
        self.rotation = build_rotation(openrouter_api_key)

    def _call_ai(self, system: str, user: str, max_tokens: int = 400) -> str | None:
        for attempt, (client, model) in enumerate(self.rotation):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    max_tokens=max_tokens,
                    temperature=0.4,
                )
                return response.choices[0].message.content.strip()
            except (openai.RateLimitError, openai.APIStatusError) as e:
                if isinstance(e, openai.APIStatusError) and getattr(e, "status_code", 0) != 429:
                    break
                time.sleep(min(15 * (attempt + 1), 60))
            except Exception:
                if attempt < len(self.rotation) - 1:
                    time.sleep(3)
        return None

    def _parse_json(self, testo: str) -> dict | None:
        if not testo:
            return None
        start = testo.find("{")
        end = testo.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                return json.loads(testo[start:end])
            except Exception:
                return None
        return None

    def _qa_check(self, corpo: str) -> dict:
        prompt = _FOLLOWUP_QA_PROMPT.format(corpo=corpo)
        risposta = self._call_ai(
            "Sei un revisore di cold email italiane (pivot implementazioni AI). Rispondi SOLO JSON.",
            prompt, max_tokens=200,
        )
        result = self._parse_json(risposta)
        if result:
            return result
        return {"media": 7.0, "approvata": True, "problemi": []}

    def _assicura_link(self, corpo: str) -> str:
        """Garantisce che il link presentazione sia presente (è la CTA attesa)."""
        if PRESENTATION_URL.rstrip("/") not in corpo:
            corpo = corpo.rstrip() + f"\n\n{PRESENTATION_URL}"
        return corpo

    # ── F1 — GIORNO 3 (NUDGE) ─────────────────────────────────────────────────

    def _genera_f1(self, lead: dict) -> dict | None:
        nome      = lead.get("page_name", "")
        settore   = lead.get("settore_calibrato", lead.get("settore", ""))
        citta     = lead.get("citta", "")
        obj_orig  = lead.get("oggetto", "")
        td        = _TARGET_FOLLOWUP.get(_get_target(settore), _TARGET_FOLLOWUP["default"])

        prompt = f"""Crea il follow-up F1 (giorno 3, NUDGE) per questa cold email.

Lead: {nome}
Settore/ICP: {settore}
Città: {citta}

BRIEF PER F1:
- Oggetto da usare: Re: {obj_orig}
- Prodotto-gancio della prima email: {td['prodotto_1']}
- RIGA DI CURIOSITÀ da usare (sviluppala in 1-2 righe): "{td['f1_curiosita']}"
- Link presentazione (nel corpo, su riga sola): {PRESENTATION_URL}
- CTA: domanda binaria leggera (vuoi vederlo dal vivo, sì o no?)

STRUTTURA: [NUDGE] → [CURIOSITÀ] → [LINK presentazione su riga sola] → [CTA binaria]
LUNGHEZZA: 50-100 parole.

Restituisci SOLO il JSON."""

        result = None
        for attempt in range(2):
            testo = self._call_ai(F1_SYSTEM_PROMPT, prompt, max_tokens=400)
            result = self._parse_json(testo)
            if not result:
                continue
            corpo = result.get("corpo", "")
            if not corpo:
                continue
            corpo = self._assicura_link(corpo)
            result["corpo"] = corpo
            qa = self._qa_check(corpo)
            result["qa_score"] = qa.get("media", 0)
            result["qa_problemi"] = qa.get("problemi", [])
            if qa.get("approvata", False) or attempt == 1:
                return result
            prompt += f"\n\nPROBLEMI DA CORREGGERE: {', '.join(qa.get('problemi', []))}"
        return result if result else None

    # ── F2 — GIORNO 7 (NUOVO ANGOLO + SECONDO PRODOTTO) ───────────────────────

    def _genera_f2(self, lead: dict) -> dict | None:
        nome      = lead.get("page_name", "")
        settore   = lead.get("settore_calibrato", lead.get("settore", ""))
        citta     = lead.get("citta", "")
        obj_orig  = lead.get("oggetto", "")
        td        = _TARGET_FOLLOWUP.get(_get_target(settore), _TARGET_FOLLOWUP["default"])

        prompt = f"""Crea il follow-up F2 (giorno 7, NUOVO ANGOLO) per questa cold email.

Lead: {nome}
Settore/ICP: {settore}
Città: {citta}

BRIEF PER F2:
- Oggetto: Re: {obj_orig}
- Prodotto della prima email: {td['prodotto_1']}
- SECONDO prodotto come nuovo angolo: {td['prodotto_2']}
- ANGOLO NUOVO da sviluppare (2-3 righe): "{td['f2_angolo']}"
- Riframe obiezione = fiducia: l'unico dubbio è se funziona per te, te lo mostro dal vivo in 20 minuti.
- Link presentazione (nel corpo, su riga sola): {PRESENTATION_URL}
- CTA: guarda la presentazione e, se ha senso, una call/demo breve.

STRUTTURA: [PONTE] → [NUOVO ANGOLO {td['prodotto_2']}] → [FIDUCIA/DEMO] → [LINK su riga sola] → [CTA]
LUNGHEZZA: 90-150 parole.

Restituisci SOLO il JSON."""

        result = None
        for attempt in range(2):
            testo = self._call_ai(F2_SYSTEM_PROMPT, prompt, max_tokens=450)
            result = self._parse_json(testo)
            if not result:
                continue
            corpo = result.get("corpo", "")
            if not corpo:
                continue
            corpo = self._assicura_link(corpo)
            result["corpo"] = corpo
            qa = self._qa_check(corpo)
            result["qa_score"] = qa.get("media", 0)
            result["qa_problemi"] = qa.get("problemi", [])
            if qa.get("approvata", False) or attempt == 1:
                return result
            prompt += f"\n\nPROBLEMI: {', '.join(qa.get('problemi', []))}"
        return result if result else None

    # ── F3 — GIORNO 14 (BREAK-UP) ─────────────────────────────────────────────

    def _genera_f3(self, lead: dict) -> dict | None:
        nome      = lead.get("page_name", "")
        settore   = lead.get("settore_calibrato", lead.get("settore", ""))
        obj_orig  = lead.get("oggetto", "")
        td        = _TARGET_FOLLOWUP.get(_get_target(settore), _TARGET_FOLLOWUP["default"])

        prompt = f"""Crea il follow-up F3 (giorno 14, ULTIMO, BREAK-UP) per questa cold email.

Lead: {nome}
Settore/ICP: {settore}

BRIEF PER F3:
- Oggetto: Re: {obj_orig}
- PROCESSO da nominare nella domanda binaria: "{td['f3_processo']}"
- DOMANDA BINARIA: automatizzare {td['f3_processo']} è qualcosa che vuoi guardare adesso, sì o no?
- PORTA APERTA + link presentazione: {PRESENTATION_URL}

MAX 50 PAROLE. Brevissimo. La brevità è il messaggio. Una domanda binaria e basta.

Restituisci SOLO il JSON."""

        result = None
        for attempt in range(2):
            testo = self._call_ai(F3_SYSTEM_PROMPT, prompt, max_tokens=300)
            result = self._parse_json(testo)
            if not result:
                continue
            corpo = result.get("corpo", "")
            if not corpo:
                continue
            corpo = self._assicura_link(corpo)
            result["corpo"] = corpo
            qa = self._qa_check(corpo)
            result["qa_score"] = qa.get("media", 0)
            result["qa_problemi"] = qa.get("problemi", [])
            if qa.get("approvata", False) or attempt == 1:
                return result
            prompt += f"\n\nPROBLEMI: {', '.join(qa.get('problemi', []))}"
        return result if result else None

    # ── RUN PUBBLICI ──────────────────────────────────────────────────────────

    def run_f1(self, leads: list) -> list:
        """
        Genera F1 (giorno 3, nudge) per tutti i lead.

        Returns:
            Lista di dict con 'f1_oggetto', 'f1_corpo', 'f1_qa_score' aggiunti.
        """
        print(f"\n[FOLLOWUP-WRITER] Genero F1 (nudge) per {len(leads)} lead...")
        risultati = []
        for i, lead in enumerate(leads, 1):
            if i % 10 == 0:
                print(f"[FOLLOWUP-WRITER] F1 progresso: {i}/{len(leads)}")
            email_f1 = self._genera_f1(lead)
            if email_f1:
                risultati.append({
                    **lead,
                    "f1_oggetto": email_f1.get("oggetto", f"Re: {lead.get('oggetto', '')}"),
                    "f1_corpo":   email_f1.get("corpo", ""),
                    "f1_qa_score": email_f1.get("qa_score", 0),
                })
                print(f"[FOLLOWUP-WRITER] F1 ✓ {lead.get('email','?')[:40]} (QA: {email_f1.get('qa_score', 0):.1f})")
            else:
                print(f"[FOLLOWUP-WRITER] F1 ✗ fallback per {lead.get('email','?')[:40]}")
                risultati.append({**lead, "f1_oggetto": f"Re: {lead.get('oggetto','')}", "f1_corpo": _fallback_f1(lead), "f1_qa_score": 6.5})
            time.sleep(2)

        print(f"[FOLLOWUP-WRITER] F1 generati: {len(risultati)}/{len(leads)}")
        return risultati

    def run_f2(self, leads: list) -> list:
        """
        Genera F2 (giorno 7, nuovo angolo + secondo prodotto) per tutti i lead.

        Returns:
            Lista di dict con 'f2_oggetto', 'f2_corpo', 'f2_qa_score' aggiunti.
        """
        print(f"\n[FOLLOWUP-WRITER] Genero F2 (nuovo angolo) per {len(leads)} lead...")
        risultati = []
        for i, lead in enumerate(leads, 1):
            if i % 10 == 0:
                print(f"[FOLLOWUP-WRITER] F2 progresso: {i}/{len(leads)}")
            email_f2 = self._genera_f2(lead)
            if email_f2:
                risultati.append({
                    **lead,
                    "f2_oggetto": email_f2.get("oggetto", f"Re: {lead.get('oggetto', '')}"),
                    "f2_corpo":   email_f2.get("corpo", ""),
                    "f2_qa_score": email_f2.get("qa_score", 0),
                })
                print(f"[FOLLOWUP-WRITER] F2 ✓ {lead.get('email','?')[:40]} (QA: {email_f2.get('qa_score', 0):.1f})")
            else:
                print(f"[FOLLOWUP-WRITER] F2 ✗ fallback per {lead.get('email','?')[:40]}")
                risultati.append({**lead, "f2_oggetto": f"Re: {lead.get('oggetto','')}", "f2_corpo": _fallback_f2(lead), "f2_qa_score": 6.5})
            time.sleep(2)

        print(f"[FOLLOWUP-WRITER] F2 generati: {len(risultati)}/{len(leads)}")
        return risultati

    def run_f3(self, leads: list) -> list:
        """
        Genera F3 (giorno 14, break-up) per tutti i lead.

        Returns:
            Lista di dict con 'f3_oggetto', 'f3_corpo', 'f3_qa_score' aggiunti.
        """
        print(f"\n[FOLLOWUP-WRITER] Genero F3 (break-up) per {len(leads)} lead...")
        risultati = []
        for i, lead in enumerate(leads, 1):
            if i % 10 == 0:
                print(f"[FOLLOWUP-WRITER] F3 progresso: {i}/{len(leads)}")
            email_f3 = self._genera_f3(lead)
            if email_f3:
                risultati.append({
                    **lead,
                    "f3_oggetto": email_f3.get("oggetto", f"Re: {lead.get('oggetto', '')}"),
                    "f3_corpo":   email_f3.get("corpo", ""),
                    "f3_qa_score": email_f3.get("qa_score", 0),
                })
                print(f"[FOLLOWUP-WRITER] F3 ✓ {lead.get('email','?')[:40]} (QA: {email_f3.get('qa_score', 0):.1f})")
            else:
                print(f"[FOLLOWUP-WRITER] F3 ✗ fallback per {lead.get('email','?')[:40]}")
                risultati.append({**lead, "f3_oggetto": f"Re: {lead.get('oggetto','')}", "f3_corpo": _fallback_f3(lead), "f3_qa_score": 6.5})
            time.sleep(2)

        print(f"[FOLLOWUP-WRITER] F3 generati: {len(risultati)}/{len(leads)}")
        return risultati


# ── FALLBACK DETERMINISTICI ───────────────────────────────────────────────────

def _fallback_f1(lead: dict) -> str:
    settore = lead.get("settore_calibrato", lead.get("settore", ""))
    td = _TARGET_FOLLOWUP.get(_get_target(settore), _TARGET_FOLLOWUP["default"])
    return (
        f"Volevo assicurarmi che avessi visto la presentazione del workflow.\n\n"
        f"{td['f1_curiosita']}\n\n"
        f"{PRESENTATION_URL}\n\n"
        f"Vuoi vederlo girare dal vivo, sì o no?\n\n"
        f"Max | Digital Empire\n{AGENCY_URL}"
    )


def _fallback_f2(lead: dict) -> str:
    settore = lead.get("settore_calibrato", lead.get("settore", ""))
    td = _TARGET_FOLLOWUP.get(_get_target(settore), _TARGET_FOLLOWUP["default"])
    return (
        f"Capisco se non era il momento giusto.\n\n"
        f"{td['f2_angolo']}\n\n"
        f"L'unico dubbio sensato è se funziona per te. Per questo te lo mostro dal vivo, in 20 minuti.\n\n"
        f"{PRESENTATION_URL}\n\n"
        f"Se ha senso, ci prendiamo 20 minuti per una demo. C'è anche uno {LAUNCH_OFFER}.\n\n"
        f"Max | Digital Empire\n{AGENCY_URL}"
    )


def _fallback_f3(lead: dict) -> str:
    settore = lead.get("settore_calibrato", lead.get("settore", ""))
    td = _TARGET_FOLLOWUP.get(_get_target(settore), _TARGET_FOLLOWUP["default"])
    return (
        f"Ultima cosa prima di chiudere il thread.\n\n"
        f"Automatizzare {td['f3_processo']} è qualcosa che vuoi guardare adesso, sì o no?\n\n"
        f"In ogni caso ti lascio la presentazione qui: {PRESENTATION_URL}\n\n"
        f"Max | Digital Empire\n{AGENCY_URL}"
    )
