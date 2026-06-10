"""
Generatore messaggi LinkedIn — Digital Empire
Pipeline multi-agente: Strategist → Writer → Humanizer

PIVOT: vendiamo IMPLEMENTAZIONI AI — non più landing page / CRO.
3 PRODOTTI (workflow installati sui server del cliente, codice incluso,
€0 canoni, setup 7 giorni, automazione 100%):
  1. Outreach Factory — outreach automatizzato al 100% (300+ email/giorno + social, gira ogni mattina)
  2. Content Factory  — l'AI genera copy CRO + grafiche/caroselli social + script video
  3. Second Brain     — knowledge base a grafo che dà memoria/contesto permanente all'LLM

Leva = "ti stravolgo l'operatività", NON "le tue conversioni".
Un workflow risolve UN problema al 1000% → unica obiezione = fiducia → "te lo mostro in demo live".

Framework messaggio (DM): A=hype automazione → P=problema operativo (1 solo) →
S=workflow che automazza al 100% (codice tuo, €0) → O=obiezione solo-fiducia →
C=CTA: guarda la presentazione (link) + prenota call, con sconto lancio.

NUOVA POLICY: LINK AMMESSI nel primo messaggio (presentazione + firma agency).
AI: Groq (llama-3.3-70b) → OpenRouter fallback
"""
import os
import json
import random

# ── COSTANTI / LINK ──────────────────────────────────────────────────────────
PRESENTATION_URL = "https://presentazione-empire.vercel.app/"
AGENCY_URL       = "https://agency-empire-landing.vercel.app"
LAUNCH_OFFER     = "sconto early-adopter per i primi clienti che partono questo mese"

# ── ENV ──────────────────────────────────────────────────────────────────────
_ENV = os.path.join(os.path.dirname(__file__), '..', 'Outreach Workflow', '.env')
if os.path.exists(_ENV):
    with open(_ENV) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith('#') and '=' in _line:
                _k, _v = _line.split('=', 1)
                os.environ.setdefault(_k.strip(), _v.strip())

try:
    from openai import OpenAI as _OAI
    _groq_key = os.getenv("GROQ_API_KEY", "")
    _or_key   = os.getenv("OPENROUTER_API_KEY", "")
    _CLIENTS: list[tuple] = []
    if _groq_key:
        _g = _OAI(base_url="https://api.groq.com/openai/v1", api_key=_groq_key)
        _CLIENTS += [(_g, "llama-3.3-70b-versatile"), (_g, "llama-3.1-8b-instant")]
    if _or_key:
        _o = _OAI(base_url="https://openrouter.ai/api/v1", api_key=_or_key)
        _CLIENTS += [(_o, "meta-llama/llama-3.3-70b-instruct:free")]
    _AI_OK = bool(_CLIENTS)
except Exception:
    _CLIENTS = []
    _AI_OK = False


def _ai(prompt: str, max_tokens: int = 250) -> str | None:
    for client, model in _CLIENTS:
        try:
            r = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.7,
            )
            return r.choices[0].message.content.strip()
        except Exception:
            continue
    return None


# ── PRODOTTI (nome leggibile per il gancio) ──────────────────────────────────
PRODUCTS = {
    "outreach":     "Outreach Factory",
    "content":      "Content Factory",
    "second_brain": "Second Brain",
}


# ── NICCHIE — target IMPLEMENTAZIONI AI ──────────────────────────────────────
# Ogni nicchia mappa a un PRODOTTO-gancio e ha:
#   prodotto    → "outreach" / "content" / "second_brain"
#   problema    → UN solo problema operativo (mai conversioni)
#   danno       → costo operativo quantificato (ore/settimana, lead persi, ecc.)
#   soluzione   → il workflow che automazza al 100% (codice tuo, €0 canoni, setup 7gg)
#   obiezione   → unica obiezione = fiducia → "te lo mostro in demo live"
#   cta         → guarda la presentazione + prenota call (con accenno sconto)
#   barnum      → opener universale-specifico sul DOLORE OPERATIVO
#   rainbow     → opener dualità (sei bravo a X, ma Y ti divora il tempo)
#   niche_term  → termine tecnico anti-AI-slop
#   free_value  → demo/analisi gratis del workflow
#   proof_hint  → risultato credibile sull'AUTOMAZIONE (tempo/volume, non conversioni)

NICCHIE = {
    # ── AGENZIE → Outreach Factory ───────────────────────────────────────────
    "agenzia": {
        "prodotto":   "outreach",
        "problema":   "l'acquisizione clienti della tua agenzia dipende ancora da prospecting manuale: qualcuno che ogni giorno cerca, scrive e segue lead a mano",
        "danno":      "sono 15-20 ore a settimana di una persona bruciate in copia-incolla — tempo che non scala e che paghi a stipendio invece di reinvestirlo sui clienti",
        "soluzione":  "Outreach Factory: un workflow installato sui tuoi server che ogni mattina parte da solo, manda 300+ email al giorno via Gmail + tocca i social, scrive personalizzato. Codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "l'unica vera domanda è la fiducia — quindi non te lo racconto, te lo mostro in demo live mentre gira sui dati veri",
        "cta":        "Ti va se ti mando la presentazione e fissiamo una call? C'è uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Quasi ogni agenzia che conosco ha lo stesso collo di bottiglia: l'acquisizione clienti dipende da qualcuno che ogni giorno scrive ai lead a mano, e quel qualcuno non scala.",
        "rainbow":    "Sei bravissimo a portare risultati ai clienti, ma il tempo che divori per trovarne di nuovi è esattamente quello che ti tiene incollato all'operatività.",
        "niche_term": "outbound manuale che non scala",
        "free_value": "ti mostro in demo live l'Outreach Factory mentre gira: vedi le email partire in automatico sui tuoi criteri di lead",
        "proof_hint": "ho automazzato l'outreach di un'agenzia al 100% — da 20 contatti al giorno fatti a mano a 300+ email/giorno che partono da sole ogni mattina",
    },

    # ── INFO-PRODUCT / FORMATORI → Content Factory ───────────────────────────
    "info_product": {
        "prodotto":   "content",
        "problema":   "la macchina dei contenuti per vendere i tuoi corsi è tutta sulle tue spalle: copy, caroselli, script video — ogni post è ore di lavoro tuo o di un editor",
        "danno":      "sono 10-15 ore a settimana che potresti spendere a creare prodotto o vendere, e quando ti fermi tu si ferma tutto il canale",
        "soluzione":  "Content Factory: un workflow che genera il copy CRO, costruisce grafiche e caroselli social e scrive gli script video in automatico. Installato da te, codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "l'unica obiezione sensata è la fiducia — per questo te lo mostro in demo live, generando contenuti veri sul tuo brand davanti a te",
        "cta":        "Ti mando la presentazione e ci sentiamo in call? Ho uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Chi vende corsi online ha quasi sempre lo stesso muro: la qualità del prodotto c'è, ma la macchina dei contenuti che lo vende è tutta appesa al tempo di una persona sola.",
        "rainbow":    "Hai un'audience che ti segue, ma ogni carosello e ogni script video è tempo tuo — e il giorno che ti fermi, si ferma tutta la distribuzione.",
        "niche_term": "produzione contenuti collo di bottiglia umano",
        "free_value": "in demo live ti faccio vedere la Content Factory che sforna copy, carosello e script video sul tuo argomento, in diretta",
        "proof_hint": "ho dato a un creator un workflow che produce copy + caroselli + script video in automatico — da 2 contenuti a settimana fatti a mano a una pipeline che gira da sola",
    },

    # ── COACH / BUSINESS MENTOR → Outreach Factory ───────────────────────────
    "coach": {
        "prodotto":   "outreach",
        "problema":   "il flusso di call qualificate dipende da quanto outreach riesci a fare tu di persona — DM, messaggi, follow-up tutti manuali tra una sessione e l'altra",
        "danno":      "ogni ora che passi a scrivere ai potenziali clienti è un'ora che non vendi e non eroghi: il tuo calendario di call dipende dalla tua resistenza, non da un sistema",
        "soluzione":  "Outreach Factory: un workflow sui tuoi server che ogni mattina manda 300+ messaggi personalizzati via email e social e gestisce i follow-up da solo. Codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "qui l'unica cosa che conta è la fiducia, quindi non te lo spiego: te lo mostro in demo live mentre invia sui contatti veri",
        "cta":        "Ti va se ti giro la presentazione e fissiamo una call? C'è uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Quasi ogni coach che fa numeri seri ha lo stesso tetto: il flusso di call qualificate dipende da quanto outreach riesci a fare di persona, e le giornate hanno un limite.",
        "rainbow":    "Sei fortissimo in sessione, ma riempire il calendario di call dipende ancora dalle tue dita sulla tastiera — non da un sistema che lavora mentre dormi.",
        "niche_term": "pipeline di call appesa all'outreach manuale",
        "free_value": "ti mostro in demo live l'Outreach Factory che invia DM ed email personalizzati e gestisce i follow-up al posto tuo",
        "proof_hint": "ho automazzato l'acquisizione di un coach al 100%: i messaggi e i follow-up partono da soli ogni mattina, lui apre solo le call già fissate",
    },

    # ── SOCIAL MEDIA MANAGER FREELANCE → Outreach Factory ────────────────────
    "smm_freelance": {
        "prodotto":   "outreach",
        "problema":   "trovare nuovi clienti per te stesso è l'attività che salti sempre: gestisci i social degli altri tutto il giorno e il tuo prospecting resta manuale e a singhiozzo",
        "danno":      "ogni mese perdi clienti potenziali non perché manchi il valore, ma perché l'outbound lo fai solo quando hai un buco — e i buchi sono rari",
        "soluzione":  "Outreach Factory: un workflow installato da te che ogni mattina manda 300+ messaggi personalizzati via email e social e segue i lead da solo. Codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "l'unica obiezione vera è fidarsi — per questo te lo mostro in demo live mentre gira, non a parole",
        "cta":        "Ti mando la presentazione e ci sentiamo in call? Ho uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Il paradosso di ogni social media manager freelance: passi la giornata a far crescere gli account degli altri e il tuo prospecting personale è l'unica cosa che resta sempre indietro.",
        "rainbow":    "Sai esattamente come riempire il feed di un cliente, ma riempire la tua pipeline di lead è l'attività che salti sempre perché è manuale e ti ruba ore.",
        "niche_term": "self-prospecting a singhiozzo",
        "free_value": "in demo live ti faccio vedere l'Outreach Factory che fa il prospecting al posto tuo, mentre tu lavori sui clienti",
        "proof_hint": "ho dato a un freelance un workflow che gli porta lead in automatico ogni giorno — il prospecting non dipende più dai suoi buchi di agenda",
    },

    # ── COPYWRITER FREELANCE → Outreach / Content ────────────────────────────
    "copywriter": {
        "prodotto":   "outreach",
        "problema":   "scrivi copy che vende per i clienti, ma il copy che dovrebbe vendere TE — i messaggi di outreach — lo mandi a mano, uno alla volta, quando capita",
        "danno":      "ogni settimana sono ore di prospecting manuale che non scrivi al posto del lavoro pagato, e il flusso di nuovi clienti resta legato al tuo tempo libero",
        "soluzione":  "Outreach Factory: un workflow che prende il tuo copy e lo manda a 300+ prospect al giorno via email e social, personalizzato, con i follow-up automatici. Codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "l'unico dubbio legittimo è la fiducia, quindi te lo mostro in demo live mentre invia il tuo copy sui lead veri",
        "cta":        "Ti giro la presentazione e fissiamo una call? C'è uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Quasi ogni copywriter freelance vive lo stesso paradosso: sai scrivere parole che fanno comprare gli altri, ma il messaggio che dovrebbe vendere te lo mandi a mano, uno alla volta.",
        "rainbow":    "Il tuo copy converte per i clienti, ma il tuo outreach personale è fermo all'invio manuale — il tuo miglior asset non lavora per te su scala.",
        "niche_term": "copy di acquisizione inviato a mano",
        "free_value": "ti mostro in demo live l'Outreach Factory che spara il tuo copy a centinaia di prospect al giorno con follow-up automatici",
        "proof_hint": "ho messo il copy di un copywriter dentro un workflow che lo invia a 300+ lead/giorno in automatico — il suo asset ora lavora su scala, non a mano",
    },

    # ── ADS SPECIALIST → Outreach Factory ────────────────────────────────────
    "ads_specialist": {
        "prodotto":   "outreach",
        "problema":   "porti risultati pubblicitari ai clienti, ma trovarne di nuovi dipende da referral e prospecting manuale fatto tra un'ottimizzazione e l'altra",
        "danno":      "il tuo flusso di nuovi clienti è instabile: dipende dal passaparola e dalle ore residue, non da un sistema di acquisizione che gira ogni giorno",
        "soluzione":  "Outreach Factory: un workflow sui tuoi server che ogni mattina manda 300+ messaggi mirati via email e social agli account che vuoi tu, con follow-up automatici. Codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "qui conta solo la fiducia — quindi te lo mostro in demo live mentre invia, non te lo descrivo",
        "cta":        "Ti mando la presentazione e ci sentiamo in call? Ho uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Quasi ogni ads specialist ha lo stesso punto cieco: sa far girare il budget degli altri alla perfezione, ma la propria acquisizione clienti è ferma a referral e prospecting manuale.",
        "rainbow":    "Ottimizzi campagne da migliaia di euro per i clienti, ma il tuo canale di acquisizione personale è ancora fatto di messaggi scritti a mano quando hai tempo.",
        "niche_term": "acquisizione clienti dipendente da referral",
        "free_value": "in demo live ti faccio vedere l'Outreach Factory che ti riempie la pipeline in automatico, senza dipendere dal passaparola",
        "proof_hint": "ho dato a uno specialista ads un workflow che gli porta nuovi lead ogni mattina in automatico — basta dipendere solo dai referral",
    },

    # ── ECOMMERCE → Content Factory ──────────────────────────────────────────
    "ecommerce": {
        "prodotto":   "content",
        "problema":   "il tuo brand divora contenuti — copy prodotto, caroselli, creatività, script video — e ogni asset è ore di lavoro tuo o di un team che paghi",
        "danno":      "sono decine di ore al mese in produzione manuale: quando rallenti tu, rallenta il calendario social e si ferma la macchina che alimenta le campagne",
        "soluzione":  "Content Factory: un workflow che genera copy CRO, costruisce grafiche e caroselli social e scrive script video in automatico per il tuo catalogo. Installato da te, codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "l'unica obiezione sensata è la fiducia, quindi te lo mostro in demo live generando contenuti veri sui tuoi prodotti",
        "cta":        "Ti va se ti mando la presentazione e fissiamo una call? C'è uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Ogni brand ecommerce serio sbatte sullo stesso muro: per alimentare social e campagne servono contenuti continui, e produrli a mano è un costo che cresce con te invece di scendere.",
        "rainbow":    "Hai i prodotti e il traffico, ma ogni carosello e ogni script video è tempo o budget di team — la produzione contenuti scala con la fatica, non con un sistema.",
        "niche_term": "produzione creatività manuale che scala coi costi",
        "free_value": "in demo live ti mostro la Content Factory che genera copy, caroselli e script video sui tuoi prodotti, in diretta",
        "proof_hint": "ho dato a un brand ecommerce un workflow che sforna copy + caroselli + script video in automatico — la produzione non dipende più dalle ore del team",
    },

    # ── CONSULENTE → Outreach Factory ────────────────────────────────────────
    "consulente": {
        "prodotto":   "outreach",
        "problema":   "la tua pipeline di nuovi incarichi dipende da networking e prospecting fatti a mano nei ritagli di tempo tra un progetto cliente e l'altro",
        "danno":      "ogni mese che sei sotto consegna l'acquisizione si ferma: il flusso di lead segue gli alti e bassi dei tuoi progetti, mai un sistema costante",
        "soluzione":  "Outreach Factory: un workflow sui tuoi server che ogni mattina manda 300+ messaggi personalizzati via email e social e segue i lead da solo. Codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "qui l'unica variabile vera è la fiducia — per questo te lo mostro in demo live mentre gira, non a parole",
        "cta":        "Ti giro la presentazione e ci sentiamo in call? Ho uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Quasi ogni consulente ha lo stesso ciclo: quando lavori non fai acquisizione, quando finisci il progetto riparti da zero a cercare clienti — un'altalena che non si stabilizza mai.",
        "rainbow":    "Chiudi benissimo quando sei davanti al cliente, ma riempire la pipeline dipende ancora dal prospecting manuale che fai solo quando hai tempo.",
        "niche_term": "pipeline ad altalena legata ai progetti",
        "free_value": "ti mostro in demo live l'Outreach Factory che tiene piena la pipeline in automatico, anche quando sei sotto consegna",
        "proof_hint": "ho automazzato l'acquisizione di un consulente al 100%: i lead arrivano ogni mattina anche mentre è in delivery, senza altalene",
    },

    # ── DEFAULT → Outreach Factory ───────────────────────────────────────────
    "default": {
        "prodotto":   "outreach",
        "problema":   "la tua acquisizione clienti dipende ancora da qualcuno che ogni giorno cerca e scrive ai lead a mano",
        "danno":      "sono ore di lavoro manuale a settimana che non scalano: il flusso di nuovi clienti è legato al tempo di una persona, non a un sistema che gira da solo",
        "soluzione":  "Outreach Factory: un workflow installato sui tuoi server che ogni mattina parte da solo, manda 300+ messaggi personalizzati via email e social con follow-up automatici. Codice tuo, €0 canoni, setup in 7 giorni, automazione al 100%",
        "obiezione":  "l'unica obiezione sensata qui è la fiducia, quindi te lo mostro in demo live mentre gira sui dati veri",
        "cta":        "Ti va se ti mando la presentazione e fissiamo una call? C'è uno sconto early-adopter per chi parte questo mese",
        "barnum":     "Quasi tutti quelli che lavorano bene nel loro campo hanno lo stesso collo di bottiglia: l'acquisizione clienti dipende da qualcuno che la fa a mano, e quel qualcuno non scala.",
        "rainbow":    "Sei bravo in quello che fai, ma il tempo che divori per trovare nuovi clienti è esattamente quello che ti tiene incollato all'operatività.",
        "niche_term": "acquisizione clienti manuale che non scala",
        "free_value": "ti mostro in demo live l'Outreach Factory che fa il prospecting al posto tuo, mentre tu lavori sul resto",
        "proof_hint": "ho automazzato l'outreach di chi lavora online al 100% — da decine di contatti al giorno fatti a mano a 300+ messaggi/giorno che partono da soli",
    },
}


def get_nicchia(title: str) -> str:
    tl = title.lower()

    # Agenzie marketing / digital agency
    if any(w in tl for w in ["agenzia", "agency", "digital agency", "advertising agency",
                               "comunicazione", "web agency"]):
        return "agenzia"

    # Coach / business mentor
    if any(w in tl for w in ["coach", "coaching", "mentor", "mentoring",
                               "business coach", "business mentor"]):
        return "coach"

    # Social media manager freelance
    if any(w in tl for w in ["social media manager", "smm", "social media strategist",
                               "social media specialist", "community manager"]):
        return "smm_freelance"

    # Copywriter freelance
    if any(w in tl for w in ["copywriter", "copywriting", "copy a risposta diretta",
                               "direct response"]):
        return "copywriter"

    # Ads specialist (facebook / meta / google)
    if any(w in tl for w in ["facebook ads", "meta ads", "google ads", "ads specialist",
                               "ads manager", "ppc", "performance marketer", "media buyer"]):
        return "ads_specialist"

    # Info-product / formatori / creator corsi
    if any(w in tl for w in ["corso", "corsi", "formatore", "formazione", "infoprodotto",
                               "info product", "info-product", "ebook", "membership",
                               "lancio corso", "insegno", "creator", "academy", "edutainer"]):
        return "info_product"

    # E-commerce / shopify / dropshipping
    if any(w in tl for w in ["ecommerce", "e-commerce", "shopify", "dropshipping",
                               "amazon fba", "store owner", "brand owner", "dtc"]):
        return "ecommerce"

    # Consulente / freelance generico marketing-business
    if any(w in tl for w in ["consulente", "consulenza", "consultant", "freelance",
                               "growth", "funnel"]):
        return "consulente"

    return "default"


# ── AGENTE 1: STRATEGIST ─────────────────────────────────────────────────────

def run_strategist(lead: dict, nd: dict) -> dict:
    nome   = lead.get("name", "").split()[0] or "professionista"
    titolo = lead.get("title", "")
    citta  = lead.get("location", "")

    opener_type = random.choice(["barnum", "rainbow"])
    opener = nd.get(opener_type, nd.get("barnum", ""))
    prodotto = PRODUCTS.get(nd.get("prodotto", "outreach"), "Outreach Factory")

    prompt = f"""Sei uno strategist di cold outreach LinkedIn per Digital Empire.
Vendiamo IMPLEMENTAZIONI AI: workflow installati sui server del cliente, codice incluso,
€0 canoni, setup 7 giorni, automazione 100%. La leva è "ti stravolgo l'operatività",
MAI "le tue conversioni".

Prodotto-gancio per questo lead: {prodotto}

Lead: {nome}, {titolo}, {citta}

Framework messaggio (A-P-S-O-C):
A = HYPE automazione (opener Barnum/Rainbow sul dolore operativo)
P = PROBLEMA operativo (UNO solo)
S = SOLUZIONE: il workflow {prodotto} che automazza al 100% (codice tuo, €0 canoni)
O = OBIEZIONE: l'unica è la fiducia → "te lo mostro in demo live"
C = CTA: guarda la presentazione + prenota call (con sconto lancio)

Dati nicchia:
- Opener {opener_type}: {opener}
- Termine tecnico: {nd.get('niche_term', '')}
- Proof hint (automazione): {nd.get('proof_hint', '')}
- Free value (demo): {nd.get('free_value', '')}

Genera brief JSON con:
- "apertura": prima riga DM (usa opener o variazione sul dolore OPERATIVO, max 15 parole)
- "hook_problema": 1 frase col termine tecnico di nicchia + danno operativo
- "tono": 3 parole per questa nicchia
- "opener_type": "{opener_type}"

Solo JSON puro, nessun markdown."""

    resp = _ai(prompt, max_tokens=200)
    if resp:
        try:
            cleaned = resp.strip().lstrip("```json").lstrip("```").rstrip("```").strip()
            return json.loads(cleaned)
        except Exception:
            pass
    return {
        "apertura": opener[:90] if opener else f"Una cosa sul tuo {titolo.split()[0].lower() if titolo else 'lavoro'}",
        "hook_problema": nd["danno"],
        "tono": "diretto concreto operativo",
        "opener_type": opener_type,
    }


# ── AGENTE 2: WRITER ──────────────────────────────────────────────────────────

def run_writer(lead: dict, brief: dict, nd: dict, tipo: str = "primo") -> str:
    nome   = lead.get("name", "").split()[0] or "ciao"
    titolo = lead.get("title", "")
    citta  = lead.get("location", "")
    loc    = f" a {citta}" if citta else ""

    opener_type = brief.get("opener_type", random.choice(["barnum", "rainbow"]))
    opener      = nd.get(opener_type, nd.get("barnum", ""))
    prodotto    = PRODUCTS.get(nd.get("prodotto", "outreach"), "Outreach Factory")

    if tipo == "primo":
        if not _AI_OK:
            return _fallback(nome, titolo, loc, nd, "primo")

        prompt = f"""Scrivi un messaggio LinkedIn di PRIMO CONTATTO per {nome} ({titolo}{loc}).

Vendiamo {prodotto}: un'IMPLEMENTAZIONE AI = workflow installato sui server del cliente,
codice incluso, €0 canoni, setup 7 giorni, automazione 100%.
LEVA: "ti stravolgo l'operatività", MAI "le tue conversioni" (offende chi fa marketing).

STRUTTURA OBBLIGATORIA — framework A-P-S-O-C, MAX 90 parole totali:

1. OPENER hype/Barnum/Rainbow (1 frase) — sul DOLORE OPERATIVO:
   Usa o migliora: "{brief.get('apertura', opener)}"
   → sembra scritto per lui ma vale per il 99% della nicchia.

2. PROBLEMA operativo + termine tecnico (1 frase, UN solo problema):
   Termine: "{nd.get('niche_term', '')}"
   Danno: "{nd['danno']}"

3. IDENTITÀ + PROVA + SOLUZIONE (1-2 frasi):
   "Sono Max — {nd.get('proof_hint', '')}"
   Presenta {prodotto}: workflow installato da te, codice tuo, €0 canoni, setup 7 giorni, automazione 100%.

4. OBIEZIONE solo-fiducia (mezza frase):
   "{nd.get('obiezione', 'te lo mostro in demo live')}"

5. PRESENTAZIONE + CTA (1-2 frasi):
   Inserisci ESATTAMENTE: "ho preparato una presentazione: {PRESENTATION_URL}"
   Poi la CTA call: "{nd['cta']}"

CHIUSURA OBBLIGATORIA (su righe separate, dopo il corpo):
{AGENCY_URL}
Max

REGOLE ASSOLUTE:
- MAX 90 parole nel corpo (esclusa firma)
- NON iniziare con "Ciao {nome}" — inizia con l'opener
- DEVE contenere il link {PRESENTATION_URL} introdotto come "ho preparato una presentazione"
- DEVE finire con {AGENCY_URL} e poi "Max" come firma
- DEVE nominare il prodotto "{prodotto}"
- ZERO punti esclamativi
- ZERO promesse sulle conversioni/CRO — parla SOLO di automazione e operatività
- ZERO frasi AI generiche: niente "Spero che...", "Volevo contattarla per...", "In qualità di..."
- Italiano diretto, come se lo conosci già di vista

Solo il messaggio, nient'altro."""

    elif tipo == "followup1":
        if not _AI_OK:
            return _fallback(nome, titolo, loc, nd, "followup1")

        prompt = f"""Follow-up LinkedIn per {nome} ({titolo}). Non ha risposto al primo DM (3-4 giorni fa).
Stiamo vendendo {prodotto} (implementazione AI, automazione 100%, codice del cliente, €0 canoni).

REGOLA CHIAVE: il denaro è nel secondo messaggio. Tasso risposta cumulativo F1 ~40%.

STRUTTURA (nudge breve):
- NON ripetere tutto il pitch
- Aggiungi 1 angolo nuovo sull'automazione: usa "{nd.get('niche_term', nd['problema'][:60])}"
- Ricorda che la demo live di {prodotto} è ancora disponibile
- Termina con domanda binaria sì/no

MAX 40 parole. Tono genuino, diretto, non insistente.
ZERO link. ZERO "Spero non disturbi". ZERO scuse. ZERO accenni a conversioni/CRO.
Solo il messaggio."""

    else:  # followup2
        agency_url       = os.getenv("AGENCY_URL_OVERRIDE") or AGENCY_URL
        presentation_url = os.getenv("PRESENTATION_URL_OVERRIDE") or PRESENTATION_URL
        if not _AI_OK:
            return _fallback(nome, titolo, loc, nd, "followup2")

        prompt = f"""TERZO e ULTIMO follow-up LinkedIn per {nome} ({titolo}).
Ha ricevuto 2 messaggi precedenti senza rispondere.
Prodotto: {prodotto} (implementazione AI, automazione 100%, codice del cliente, €0 canoni).

STRUTTURA "break-up message":
1. Framing definitivo: "Ultimo messaggio, poi sparisco"
2. 1 risultato concreto sull'automazione: "{nd.get('proof_hint', nd['danno'])}"
3. Lascia la presentazione: "se vuoi capire {prodotto} in 2 minuti: {presentation_url}"
4. Firma con l'agency su riga separata: {agency_url} e poi "Max"
5. Chiusura rispettosa: "Sì o no — rispetto entrambe"

MAX 60 parole nel corpo. ZERO pressione. ZERO "so che sei occupato". ZERO accenni a conversioni/CRO.
Tono professionale, finale, senza risentimento.
Solo il messaggio."""

    resp = _ai(prompt, max_tokens=260)
    return resp if resp else _fallback(nome, titolo, loc, nd, tipo)


# ── AGENTE 3: HUMANIZER ───────────────────────────────────────────────────────

def run_humanizer(msg: str, lead: dict) -> tuple[str, float, str]:
    if not _AI_OK:
        return msg, 8.0, ""

    prompt = f"""Valuta questo messaggio LinkedIn (1-10 per criterio). Vendiamo IMPLEMENTAZIONI AI
(workflow installati, automazione 100%), leva su OPERATIVITÀ non su conversioni.

MESSAGGIO:
{msg}

LEAD: {lead.get('title', '')} — {lead.get('location', '')}

CRITERI:
1. OPENER: inizia con hype/Barnum/Rainbow sul dolore operativo? Sembra personalizzato?
2. PROOF: c'è un risultato concreto credibile sull'automazione?
3. SOLUTION: il workflow (codice tuo, €0 canoni, 100% automatico) è chiaro?
4. CTA: c'è la presentazione (link) + invito alla call con sconto lancio?
5. HUMANNESS: sembra scritto da un umano? NON parla di conversioni/CRO?

Rispondi SOLO JSON:
{{"op": X, "pr": X, "so": X, "ct": X, "h": X, "media": X.X, "fix": "problema principale in 10 parole"}}"""

    resp = _ai(prompt, max_tokens=120)
    if resp:
        try:
            cleaned = resp.strip().lstrip("```json").lstrip("```").rstrip("```").strip()
            data = json.loads(cleaned)
            return msg, float(data.get("media", 7.5)), data.get("fix", "")
        except Exception:
            pass
    return msg, 7.5, ""


# ── PIPELINE PUBBLICA ──────────────────────────────────────────────────────────

def generate_message(lead: dict) -> dict:
    """Ritorna dict {corpo, link_msg}. Messaggio 1: corpo senza firma.
    Messaggio 2: firma completa + link (inviato subito dopo)."""
    nd    = NICCHIE[get_nicchia(lead.get("title", ""))]
    brief = run_strategist(lead, nd)
    msg   = run_writer(lead, brief, nd, "primo")
    _, score, fix = run_humanizer(msg, lead)

    if score < 7.0 and _AI_OK and fix:
        nome     = lead.get("name", "").split()[0]
        titolo   = lead.get("title", "")
        prodotto = PRODUCTS.get(nd.get("prodotto", "outreach"), "Outreach Factory")
        retry  = _ai(
            f"Rivedi questo DM LinkedIn (score {score:.1f}/10). Problema: {fix}\n\n"
            f"ORIGINALE:\n{msg}\n\n"
            f"Mantieni il framework A-P-S-O-C e il prodotto {prodotto}. Max 90 parole nel corpo. "
            f"DEVE contenere il link della presentazione {PRESENTATION_URL}. "
            f"Parla SOLO di automazione/operatività, MAI di conversioni. "
            f"Lead: {nome}, {titolo}. Solo il messaggio.",
            max_tokens=260
        )
        if retry:
            msg = retry

    # Rimuovi firma residua dal corpo (se c'è)
    corpo = msg.replace("\n\nMax", "").replace("\nMax", "").rstrip()
    link_msg = f"Maximilian - Agency | Digital Empire\nlink sito web: {AGENCY_URL}"
    return {"corpo": corpo, "link_msg": link_msg}


def generate_followup1(lead: dict) -> dict:
    """Ritorna dict {corpo, link_msg}."""
    nd = NICCHIE[get_nicchia(lead.get("title", ""))]
    msg = run_writer(lead, {}, nd, "followup1")
    corpo = msg.replace("\n\nMax", "").replace("\nMax", "").rstrip()
    link_msg = f"Maximilian - Agency | Digital Empire\nlink sito web: {AGENCY_URL}"
    return {"corpo": corpo, "link_msg": link_msg}


def generate_followup2(lead: dict, agency_url: str) -> dict:
    """Ritorna dict {corpo, link_msg}."""
    os.environ["AGENCY_URL_OVERRIDE"] = agency_url
    nd = NICCHIE[get_nicchia(lead.get("title", ""))]
    msg = run_writer(lead, {}, nd, "followup2")
    corpo = msg.replace("\n\nMax", "").replace("\nMax", "").rstrip()
    link_msg = f"Maximilian - Agency | Digital Empire\nlink sito web: {AGENCY_URL}"
    return {"corpo": corpo, "link_msg": link_msg}


# ── FALLBACK (AI non disponibile) ────────────────────────────────────────────

def _fallback(nome, titolo, loc, nd, tipo) -> str:
    opener_type = random.choice(["barnum", "rainbow"])
    opener      = nd.get(opener_type, nd.get("barnum", ""))
    prodotto    = PRODUCTS.get(nd.get("prodotto", "outreach"), "Outreach Factory")

    if tipo == "primo":
        _proof = nd.get("proof_hint", "")
        _sol   = nd.get("soluzione", "")
        _obj   = nd.get("obiezione", "te lo mostro in demo live")
        return (
            f"{opener}\n\n"
            f"{nd['danno'].capitalize()}.\n\n"
            f"Sono Max: {_proof}. La soluzione è {_sol}.\n\n"
            f"{_obj.capitalize()}.\n\n"
            f"Ho preparato una presentazione: {PRESENTATION_URL}\n"
            f"{nd['cta']}\n\n"
            f"{AGENCY_URL}\n"
            f"Max"
        )
    elif tipo == "followup1":
        return (
            f"Ti riscrivo, {nome}.\n\n"
            f"Una cosa sola sul {prodotto}: {nd.get('niche_term', nd['problema'][:70])}. "
            f"La demo live è ancora lì quando vuoi.\n\n"
            f"Sì o no — basta quello."
        )
    else:  # followup2
        url  = os.getenv("AGENCY_URL_OVERRIDE", AGENCY_URL)
        purl = os.getenv("PRESENTATION_URL_OVERRIDE", PRESENTATION_URL)
        return (
            f"Ultimo messaggio, {nome} — poi sparisco.\n\n"
            f"{nd.get('proof_hint', nd['danno'])}.\n\n"
            f"Se vuoi capire {prodotto} in 2 minuti: {purl}\n\n"
            f"{url}\n"
            f"Max\n\n"
            f"Sì o no — rispetto entrambe."
        )


# ── COMMENTO WARMING ─────────────────────────────────────────────────────────
# Insight di automazione AI / operatività. NON è un pitch. Max 25 parole.

_COMMENT_FALLBACKS = {
    "agenzia":        "Il vero collo di bottiglia di un'agenzia non è il delivery: è l'acquisizione clienti ancora appesa al prospecting manuale di una persona. Quello non scala.",
    "info_product":   "La qualità del corso non è mai il problema. È la macchina dei contenuti che lo vende, tutta appesa al tempo di una persona sola.",
    "coach":          "Il tetto di chi fa coaching non è la bravura in sessione: è che il flusso di call dipende da quanto outreach riesci a fare di persona.",
    "smm_freelance":  "Il paradosso del social media manager freelance: fa crescere gli account degli altri tutto il giorno e il proprio prospecting resta sempre l'ultima cosa.",
    "copywriter":     "Strano vedere copywriter che scrivono parole che fanno comprare gli altri, ma mandano il proprio messaggio di acquisizione a mano, uno alla volta.",
    "ads_specialist": "Tanti ads specialist ottimizzano budget enormi per i clienti, ma la propria acquisizione è ferma a referral e messaggi scritti quando avanza tempo.",
    "ecommerce":      "Nel commerce la produzione contenuti scala con la fatica, non con un sistema: ogni carosello e script video è tempo o budget di team che cresce coi ricavi.",
    "consulente":     "Il ciclo del consulente: quando lavora non fa acquisizione, quando finisce riparte da zero a cercare clienti. Un'altalena che raramente si stabilizza.",
    "default":        "La parte dell'operatività che quasi nessuno automatizza è proprio l'acquisizione: resta manuale, legata al tempo di una persona, e per questo non scala.",
}


def generate_comment(post_text: str, nicchia: str, author_name: str = "") -> str:
    """
    Genera un commento genuino e contestuale per warming su post LinkedIn.
    NON è un pitch — è un'osservazione da esperto su automazione/operatività.
    Max 25 parole. Non menziona Digital Empire o i prodotti.
    """
    if not _AI_OK:
        return _COMMENT_FALLBACKS.get(nicchia, _COMMENT_FALLBACKS["default"])

    nd = NICCHIE.get(nicchia, NICCHIE["default"])
    prompt = f"""Scrivi un commento LinkedIn per questo post.

AUTORE: {author_name or 'professionista'}
NICCHIA: {nicchia}
POST (estratto): {post_text[:220] if post_text else '[nessun testo]'}

OBIETTIVO: essere notato come esperto di AUTOMAZIONE e operatività — non fare pitch.
Angolo: "{nd.get('niche_term', nd['problema'][:60])}"

REGOLE:
- MAX 25 parole
- Osservazione precisa e contestuale al post, su automazione AI/operatività
- NON menzionare Digital Empire, Outreach/Content Factory, Second Brain o servizi
- NON parlare di conversioni, CRO o landing page
- NON fare complimenti vuoti ("Ottimo post!", "Grazie per la condivisione!")
- Aggiungi 1 dato o prospettiva che arricchisce la discussione
- Puoi chiudere con 1 domanda breve se viene naturale
- Italiano diretto, tono da professionista esperto

Solo il commento, nient'altro."""

    resp = _ai(prompt, max_tokens=80)
    if resp and len(resp.strip()) > 8:
        return resp.strip()
    return _COMMENT_FALLBACKS.get(nicchia, _COMMENT_FALLBACKS["default"])


# ── NOTE CONNESSIONE (max 300 char) ─────────────────────────────────────────
# Barnum/Rainbow compresso: sembra personale, vale per il 99% della nicchia.
# Nessun pitch, NESSUN link (LinkedIn le tronca) — solo insight + porta aperta.

_CONNECTION_NOTE_TEMPLATES = {
    "agenzia": (
        "L'acquisizione clienti di quasi ogni agenzia dipende ancora dal prospecting manuale "
        "di una persona — e quello non scala. Ho un modo per automatizzarlo al 100%, "
        "ti va se ne parliamo?"
    ),
    "coach": (
        "Il flusso di call qualificate di un coach dipende da quanto outreach riesci a fare "
        "di persona, e le giornate hanno un limite. Sto aiutando alcuni a renderlo automatico — "
        "ti interessa scambiarci due idee?"
    ),
    "info_product": (
        "La qualità del corso non è mai il problema: è la macchina dei contenuti che lo vende, "
        "tutta appesa al tempo di una persona. Sto lavorando a come automatizzarla — "
        "ci colleghiamo?"
    ),
    "smm_freelance": (
        "Il paradosso del social media manager freelance: fai crescere gli account degli altri "
        "tutto il giorno e il tuo prospecting resta sempre l'ultima cosa. "
        "Ho un modo per automatizzarlo — ne parliamo?"
    ),
    "copywriter": (
        "Strano vedere copywriter che scrivono copy che fa comprare gli altri ma mandano il proprio "
        "messaggio di acquisizione a mano, uno alla volta. Sto aiutando alcuni a metterlo in automatico — "
        "ci colleghiamo?"
    ),
    "ads_specialist": (
        "Tanti ads specialist ottimizzano budget enormi per i clienti ma la propria acquisizione "
        "è ferma a referral e messaggi manuali. Ho un modo per renderla automatica — "
        "ti va di parlarne?"
    ),
    "ecommerce": (
        "Nel commerce la produzione contenuti scala con la fatica: ogni carosello e script video è "
        "tempo o budget di team. Sto lavorando a come automatizzarla — ci colleghiamo?"
    ),
    "consulente": (
        "Il ciclo del consulente: quando lavori non fai acquisizione, quando finisci riparti da zero. "
        "Sto aiutando alcuni a tenere la pipeline piena in automatico — ti va di scambiarci due idee?"
    ),
    "default": (
        "La parte dell'operatività che quasi nessuno automatizza è proprio l'acquisizione: "
        "resta manuale e legata al tempo di una persona. Ho un modo per renderla automatica — "
        "ci colleghiamo?"
    ),
}


def generate_connection_note(lead: dict) -> str:
    """
    Restituisce la nota per la connection request LinkedIn (max 300 char).
    Insight di nicchia su automazione/operatività + porta aperta. NESSUN link.
    """
    nicchia = get_nicchia(lead.get("title", ""))
    note = _CONNECTION_NOTE_TEMPLATES.get(nicchia, _CONNECTION_NOTE_TEMPLATES["default"])
    return note[:300]


# ── TEST ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Console Windows (cp1252) non gestisce €, —, ecc. — forziamo UTF-8 per il test.
    try:
        import sys
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    leads = [
        {"name": "Marco Bianchi",    "title": "Titolare agenzia marketing digitale", "location": "Milano"},
        {"name": "Laura Rossi",      "title": "Business coach e mentor",              "location": "Roma"},
        {"name": "Giulia Ferrara",   "title": "Social media manager freelance",       "location": "Torino"},
        {"name": "Davide Conti",     "title": "Formatore corsi online di trading",    "location": "Bologna"},
        {"name": "Sara De Luca",     "title": "Founder brand ecommerce skincare",     "location": "Napoli"},
        {"name": "Andrea Marchetti", "title": "Copywriter freelance a risposta diretta", "location": "Verona"},
        {"name": "Elena Greco",      "title": "Meta ads specialist e media buyer",    "location": "Firenze"},
    ]
    print(f"AI disponibile: {_AI_OK} ({'Groq/OpenRouter' if _AI_OK else 'fallback template'})\n")
    print("=" * 64)
    print("TEST PIVOT — Implementazioni AI (Outreach / Content / Second Brain)")
    print("=" * 64)
    for lead in leads:
        nicchia  = get_nicchia(lead["title"])
        prodotto = PRODUCTS.get(NICCHIE[nicchia]["prodotto"], "Outreach Factory")
        print(f"\n=== {lead['name']} - {lead['title']} ({nicchia} -> {prodotto}) ===")
        print("--- NOTA CONNESSIONE ---")
        print(generate_connection_note(lead))
        print("--- PRIMO MESSAGGIO ---")
        print(generate_message(lead))
        print("--- FOLLOW-UP 1 (giorno 3) ---")
        print(generate_followup1(lead))
        print("--- FOLLOW-UP 2 (giorno 7) ---")
        print(generate_followup2(lead, AGENCY_URL))
        print()
