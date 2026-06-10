"""
Generatore messaggi Instagram — Digital Empire
Pipeline multi-agente: Strategist → Writer → Humanizer

PIVOT: vendiamo IMPLEMENTAZIONI AI (workflow installati sui server del cliente,
codice incluso, zero canoni, setup 7 giorni, automazione 100%).
3 prodotti = 3 soluzioni:
  - Outreach Factory  → automatizza l'outreach al 100% (300+ email/giorno + social)
  - Content Factory   → l'AI genera copy CRO + grafiche/caroselli + script video
  - Second Brain      → knowledge base a grafo, memoria/contesto permanente all'LLM

Framework DM (A-P-S-O-C):
  A = hype automazione (Barnum/Rainbow opener)
  P = problema operativo (UNO solo)
  S = workflow 100% (codice tuo, zero canoni)
  O = obiezione solo-fiducia ("te lo mostro live")
  C = CTA: guarda la presentazione (link) + scrivimi per una call, sconto lancio

Leva = "ti stravolgo l'operatività", NON "le tue conversioni".

Instagram: tono diretto, primo DM ≤ ~60 parole (il link conta poco).
NOVITÀ: i link sono AMMESSI nel primo DM (PRESENTATION_URL).

AI: Groq (llama-3.3-70b) → OpenRouter fallback
"""
import os
import json
import random

# ── ENV ──────────────────────────────────────────────────────────────────────
_ENV = os.path.join(os.path.dirname(__file__), '..', 'Outreach Workflow', '.env')
if os.path.exists(_ENV):
    with open(_ENV) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith('#') and '=' in _line:
                _k, _v = _line.split('=', 1)
                os.environ.setdefault(_k.strip(), _v.strip())

# ── COSTANTI / LINK ──────────────────────────────────────────────────────────
PRESENTATION_URL = "https://presentazione-empire.vercel.app/"
AGENCY_URL       = "https://agency-empire-landing.vercel.app"
LAUNCH_OFFER     = "sconto early-adopter per i primi clienti che partono questo mese"

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


def _ai(prompt: str, max_tokens: int = 200) -> str | None:
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


# ── NICCHIE — target IMPLEMENTAZIONI AI (Outreach / Content / Second Brain) ────
# Ogni nicchia mappa a UN prodotto e UN solo problema operativo.
NICCHIE = {
    "agenzia": {
        "prodotto":   "Outreach Factory",
        "problema":   "passi ore ogni giorno a cercare lead e scrivere a mano email e DM, e l'acquisizione resta il collo di bottiglia dell'agenzia",
        "danno":      "ogni ora persa a fare outreach manuale è un'ora che non vendi e non gestisci clienti, e la pipeline si svuota appena ti fermi",
        "soluzione":  "ti installo Outreach Factory sui tuoi server: scova i lead, scrive e invia 300+ email al giorno via Gmail più i social, in automatico al 100%, codice tuo e zero canoni",
        "barnum":     "Chi gestisce un'agenzia sa già che il vero collo di bottiglia non è chiudere i clienti, è riempire la pipeline ogni giorno senza passarci le ore.",
        "rainbow":    "Sei bravo a portare risultati ai clienti, ma l'acquisizione la fai ancora a mano e ti mangia il tempo che dovresti usare per crescere.",
        "niche_term": "outreach manuale come collo di bottiglia",
        "free_value": "ti mostro live il workflow che gira già e fa 300+ contatti al giorno",
        "proof_hint": "agenzia che ha automatizzato l'outreach al 100% e ha smesso di scrivere a mano",
        "cta":        "Ti mando la presentazione?",
    },
    "info_product": {
        "prodotto":   "Content Factory",
        "problema":   "produrre contenuti ogni giorno (copy, caroselli, script video) ti divora il tempo e quando ti fermi il funnel si spegne",
        "danno":      "ogni lancio o post saltato è traffico e vendite che non recuperi, e il content resta un lavoro infinito fatto a mano",
        "soluzione":  "ti installo Content Factory sui tuoi server: l'AI genera copy CRO, costruisce grafiche e caroselli e ti scrive gli script video in automatico, codice tuo e zero canoni",
        "barnum":     "Chi vive di info-product sa già che il prodotto non è il problema, è alimentare la macchina dei contenuti ogni singolo giorno senza fermarsi mai.",
        "rainbow":    "Hai un'offerta che funziona, ma sei tu il collo di bottiglia: senza i tuoi contenuti il funnel non gira.",
        "niche_term": "produzione contenuti manuale che non scala",
        "free_value": "ti mostro live l'AI che sforna copy, caroselli e script da sola",
        "proof_hint": "creator che ha automatizzato la produzione contenuti e pubblica ogni giorno senza scriverli a mano",
        "cta":        "Ti mando la presentazione?",
    },
    "coach": {
        "prodotto":   "Outreach Factory",
        "problema":   "dipendi dai tuoi follower e dal passaparola per riempire le call, e quando finiscono devi ricominciare a contattare a mano",
        "danno":      "ogni settimana senza nuove call qualificate è fatturato fermo, e l'acquisizione manuale ti ruba il tempo che vorresti dare ai clienti",
        "soluzione":  "ti installo Outreach Factory sui tuoi server: trova i lead giusti e li contatta da solo, 300+ email al giorno via Gmail più i social, in automatico al 100%, codice tuo e zero canoni",
        "barnum":     "Chi fa coaching ad alto ticket sa già che il problema non è chiudere, è avere un flusso costante di call qualificate senza passarci le giornate.",
        "rainbow":    "Chiudi bene chi ti conosce già, ma il flusso di nuovi prospect lo costruisci ancora a mano e si ferma quando ti fermi tu.",
        "niche_term": "acquisizione call qualificate fatta a mano",
        "free_value": "ti mostro live il workflow che riempie la pipeline al posto tuo",
        "proof_hint": "coach che ha automatizzato la prospezione e arrivano call qualificate senza scrivere un DM",
        "cta":        "Ti mando la presentazione?",
    },
    "smm_freelance": {
        "prodotto":   "Outreach Factory",
        "problema":   "trovi clienti col passaparola e qualche DM scritto a mano, e tra il lavoro per i clienti non ti resta tempo per acquisirne di nuovi",
        "danno":      "ogni mese senza nuovi clienti è reddito fermo, e l'outreach manuale è la prima cosa che salti quando sei sotto consegne",
        "soluzione":  "ti installo Outreach Factory sui tuoi server: cerca i lead e invia 300+ email al giorno via Gmail più i social in automatico al 100%, lavora mentre tu segui i clienti, codice tuo e zero canoni",
        "barnum":     "Chi fa il social media manager freelance sa già che il problema non è il lavoro, è trovare clienti nuovi senza rubare tempo a quelli che hai già.",
        "rainbow":    "Sei pieno di lavoro per i clienti, ma la tua acquisizione la fai a mano nei ritagli e si ferma appena hai una consegna.",
        "niche_term": "acquisizione clienti manuale tra le consegne",
        "free_value": "ti mostro live il workflow che fa 300+ contatti al giorno mentre lavori",
        "proof_hint": "freelance marketing che ha automatizzato l'outreach e riceve lead senza fermarsi sul lavoro clienti",
        "cta":        "Ti mando la presentazione?",
    },
    "copywriter": {
        "prodotto":   "Outreach Factory",
        "problema":   "il tuo tempo è prezioso ma lo spendi a cercare clienti e scrivere DM di acquisizione invece che progetti pagati",
        "danno":      "ogni ora di prospezione manuale è un'ora non fatturata, e quando sei pieno di lavoro l'acquisizione si ferma del tutto",
        "soluzione":  "ti installo Outreach Factory sui tuoi server: scova i lead e manda 300+ email al giorno via Gmail più i social in automatico al 100%, tu scrivi solo i progetti veri, codice tuo e zero canoni",
        "barnum":     "Chi vive di copywriting sa già che il problema non è scrivere, è non avere una pipeline costante senza dover fare il commerciale di se stesso.",
        "rainbow":    "Scrivi benissimo per i clienti, ma per trovarli fai ancora outreach a mano e ti porta via le ore migliori.",
        "niche_term": "prospezione manuale al posto del lavoro fatturato",
        "free_value": "ti mostro live il workflow che fa la prospezione al posto tuo",
        "proof_hint": "copywriter che ha automatizzato l'acquisizione e dedica le ore solo ai progetti pagati",
        "cta":        "Ti mando la presentazione?",
    },
    "ads_specialist": {
        "prodotto":   "Outreach Factory",
        "problema":   "porti risultati con le ads ma per trovare nuovi clienti dipendi da referral e DM scritti a mano, senza un sistema costante",
        "danno":      "ogni mese senza nuovi clienti è budget di crescita fermo, e l'acquisizione manuale è ingestibile mentre ottimizzi le campagne",
        "soluzione":  "ti installo Outreach Factory sui tuoi server: trova i lead e invia 300+ email al giorno via Gmail più i social in automatico al 100%, gira da solo mentre tu gestisci le campagne, codice tuo e zero canoni",
        "barnum":     "Chi fa ads sa già che sa portare clienti ai clienti, ma per se stesso l'acquisizione resta sempre l'ultima cosa fatta a mano.",
        "rainbow":    "Sei ossessionato dal ROAS dei clienti, ma il tuo di funnel di acquisizione non l'hai mai sistematizzato.",
        "niche_term": "acquisizione propria fatta a mano",
        "free_value": "ti mostro live il workflow che riempie la pipeline al posto tuo",
        "proof_hint": "ads specialist che ha automatizzato la propria acquisizione e non scrive più DM a mano",
        "cta":        "Ti mando la presentazione?",
    },
    "ecommerce": {
        "prodotto":   "Content Factory",
        "problema":   "i tuoi prodotti hanno bisogno di contenuti continui (creatività, caroselli, script) e produrli a mano frena ogni lancio e ogni campagna",
        "danno":      "ogni creatività in ritardo è una campagna che parte fiacca, e la produzione manuale tiene fermo lo scaling dell'advertising",
        "soluzione":  "ti installo Content Factory sui tuoi server: l'AI genera copy CRO, costruisce grafiche e caroselli e ti scrive gli script video in automatico per ogni prodotto, codice tuo e zero canoni",
        "barnum":     "Chi gestisce un e-commerce serio sa già che il limite non è il traffico, è non riuscire a sfornare creatività e contenuti abbastanza in fretta.",
        "rainbow":    "Hai i prodotti e il traffico, ma la produzione di contenuti e creatività è il collo di bottiglia che frena ogni lancio.",
        "niche_term": "produzione creatività manuale che frena lo scaling",
        "free_value": "ti mostro live l'AI che genera copy, caroselli e script per i tuoi prodotti",
        "proof_hint": "brand e-commerce che ha automatizzato copy e creatività e lancia campagne senza colli di bottiglia",
        "cta":        "Ti mando la presentazione?",
    },
    "consulente": {
        "prodotto":   "Outreach Factory",
        "problema":   "vendi consulenza ad alto valore ma l'acquisizione la fai a mano col passaparola, e senza un flusso costante la pipeline è imprevedibile",
        "danno":      "ogni mese senza nuovi contatti qualificati è fatturato instabile, e l'outreach manuale è la prima cosa che salti quando sei carico di lavoro",
        "soluzione":  "ti installo Outreach Factory sui tuoi server: trova i lead e contatta 300+ persone al giorno via Gmail più i social in automatico al 100%, codice tuo e zero canoni",
        "barnum":     "Chi vende consulenza sa già che il problema non è chiudere, è avere un flusso prevedibile di contatti qualificati senza dipendere dal passaparola.",
        "rainbow":    "Sei bravissimo quando sei davanti al cliente, ma il sistema per arrivarci non l'hai automatizzato e dipende ancora da te.",
        "niche_term": "pipeline imprevedibile da acquisizione manuale",
        "free_value": "ti mostro live il workflow che porta contatti qualificati al posto tuo",
        "proof_hint": "consulente che ha automatizzato l'outreach e ha una pipeline costante senza scrivere a mano",
        "cta":        "Ti mando la presentazione?",
    },
    "default": {
        "prodotto":   "Outreach Factory",
        "problema":   "spendi troppe ore a cercare clienti e scrivere a mano email e DM, e l'acquisizione resta il collo di bottiglia del business",
        "danno":      "ogni ora persa in outreach manuale è un'ora che non lavori e non vendi, e la pipeline si svuota appena ti fermi",
        "soluzione":  "ti installo Outreach Factory sui tuoi server: scova i lead, scrive e invia 300+ email al giorno via Gmail più i social in automatico al 100%, codice tuo e zero canoni",
        "barnum":     "Chi fa business online sa già che il vero collo di bottiglia è l'acquisizione fatta a mano, che ti mangia il tempo e si ferma quando ti fermi tu.",
        "rainbow":    "Sei bravo nel tuo lavoro, ma trovare clienti lo fai ancora a mano e ti porta via le ore che vorresti dedicare a crescere.",
        "niche_term": "acquisizione manuale come collo di bottiglia",
        "free_value": "ti mostro live il workflow che fa 300+ contatti al giorno da solo",
        "proof_hint": "imprenditore digitale che ha automatizzato l'outreach al 100% e ha smesso di scrivere a mano",
        "cta":        "Ti mando la presentazione?",
    },
}


def _estrai_nome(bio: str, username: str) -> str:
    """Estrae il primo nome dalla bio o dall'username."""
    if bio:
        # Cerca pattern "Nome Cognome | ..." o "Nome |" o prima parola maiuscola
        import re
        m = re.match(r'^([A-ZÀ-Ö][a-zà-ö]{2,})', bio.strip())
        if m:
            return m.group(1)
    # Prova dall'username: prende la prima parola alfanumerica
    if username:
        parts = username.replace("_", " ").replace(".", " ").split()
        if parts and len(parts[0]) > 2:
            return parts[0].capitalize()
    return ""


def get_nicchia(bio_or_title: str) -> str:
    tl = (bio_or_title or "").lower()

    # Agenzia → Outreach Factory
    if any(w in tl for w in ["agenzia", "agency", "web agency", "digital agency"]):
        return "agenzia"
    # Coach / mentor → Outreach Factory
    if any(w in tl for w in ["coach", "coaching", "mentor", "mentoring", "mindset coach",
                               "business coach", "life coach"]):
        return "coach"
    # Ads specialist / media buyer → Outreach Factory
    if any(w in tl for w in ["ads specialist", "facebook ads", "meta ads", "google ads",
                               "media buyer", "advertising", "ads manager", "performance marketing"]):
        return "ads_specialist"
    # Copywriter → Outreach Factory
    if any(w in tl for w in ["copywriter", "copywriting", "copy writer"]):
        return "copywriter"
    # SMM / freelance marketing → Outreach Factory
    #   (ruolo esplicito: ha priorità su "personal brand/creator" generici)
    if any(w in tl for w in ["social media manager", "smm", "social media",
                               "freelance marketing", "marketing freelance",
                               "growth", "freelance", "freelancer"]):
        return "smm_freelance"
    # Info product / formatori / creator → Content Factory
    if any(w in tl for w in ["corso", "corsi", "formatore", "formatrice", "formazione",
                               "infoprodotto", "info product", "ebook", "membership",
                               "lancio corso", "insegno", "academy", "accademia",
                               "masterclass", "creator", "content creator", "ugc",
                               "personal brand", "personal branding"]):
        return "info_product"
    # E-commerce → Content Factory
    if any(w in tl for w in ["ecommerce", "e-commerce", "shopify", "dropshipping",
                               "amazon fba", "negozio online", "brand", "store", "seller"]):
        return "ecommerce"
    # Consulente / servizi → Outreach Factory
    if any(w in tl for w in ["consulente", "consulenza", "consultant"]):
        return "consulente"
    # Marketing/digital generico → Outreach Factory (smm_freelance)
    if any(w in tl for w in ["marketing", "digital", "strategist", "funnel", "imprenditore",
                               "entrepreneur", "business"]):
        return "smm_freelance"

    return "default"


# ── AGENTE 1: STRATEGIST ─────────────────────────────────────────────────────

def run_strategist(lead: dict, nd: dict) -> dict:
    username = lead.get("username", "professionista")
    bio      = lead.get("bio", "")
    nicchia  = lead.get("nicchia", "default")

    opener_type = random.choice(["barnum", "rainbow"])
    opener = nd.get(opener_type, nd.get("barnum", ""))

    prompt = f"""Sei uno strategist di cold outreach Instagram per Digital Empire.
Vendiamo IMPLEMENTAZIONI AI: workflow installati sui server del cliente, codice incluso,
zero canoni, setup 7 giorni, automazione 100%. La leva è "ti stravolgo l'operativita'".

Lead Instagram: @{username}
Bio: {bio[:150]}
Nicchia: {nicchia}
Prodotto da proporre: {nd.get('prodotto', 'Outreach Factory')}

Framework A-P-S-O-C Instagram (corto e diretto):
1. A = HYPE AUTOMAZIONE — opener Barnum/Rainbow sul tema "automatizzare l'operativita'"
2. P = PROBLEMA OPERATIVO (uno solo)
3. S = SOLUZIONE workflow 100% (codice tuo, zero canoni)
4. C = CTA guarda la presentazione + scrivimi per una call

Opener disponibile ({opener_type}): "{opener}"
Problema operativo: "{nd.get('niche_term', '')}"

Genera brief JSON:
- "apertura": prima riga DM (usa opener, max 12 parole)
- "pain_data": 1 frase sul problema operativo (max 10 parole)
- "opener_type": "{opener_type}"

Solo JSON puro."""

    resp = _ai(prompt, max_tokens=150)
    if resp:
        try:
            cleaned = resp.strip().lstrip("```json").lstrip("```").rstrip("```").strip()
            return json.loads(cleaned)
        except Exception:
            pass
    return {
        "apertura": opener[:80] if opener else f"Domanda su {nicchia}",
        "pain_data": nd["danno"][:80],
        "opener_type": opener_type,
    }


# ── AGENTE 2: WRITER ──────────────────────────────────────────────────────────

def run_writer(lead: dict, brief: dict, nd: dict, tipo: str = "primo") -> str:
    username = lead.get("username", "")
    bio      = lead.get("bio", "")
    nicchia  = lead.get("nicchia", "default")
    prodotto = nd.get("prodotto", "Outreach Factory")

    opener_type = brief.get("opener_type", random.choice(["barnum", "rainbow"]))
    opener = nd.get(opener_type, nd.get("barnum", ""))

    nome = _estrai_nome(bio, username)
    saluto = f"Ciao {nome}" if nome else "Ciao"

    # La 'soluzione' nelle NICCHIE inizia con "ti installo {prodotto} sui tuoi server: <descr>".
    # Per lo step SOLUZIONE passo solo la <descr> dopo i due punti, così il modello non
    # ripete "ti installo {prodotto} sui tuoi server" due volte.
    _sol_full = nd.get("soluzione", "")
    sol_descr = _sol_full.split(":", 1)[1].strip() if ":" in _sol_full else _sol_full

    if tipo == "primo":
        if not _AI_OK:
            return _fallback(lead, nd, "primo")

        prompt = f"""Scrivi un PRIMO DM Instagram che dia VALORE reale: un messaggio umano
da founder a founder, MAI un elenco telegrafico di frammenti.
Vendiamo {prodotto}: un workflow AI installato sui server del cliente, codice incluso,
zero canoni, setup 7 giorni, automazione 100%. Leva: "ti stravolgo l'operativita'".

LEAD: @{username}
Bio: {bio[:160]}
Nome da usare nel saluto: {nome if nome else "(non disponibile, scrivi solo Ciao)"}
Nicchia: {nicchia}
Prodotto: {prodotto}

STRUTTURA OBBLIGATORIA — ogni punto e' una FRASE COMPLETA e scorrevole, mai un frammento:

1. SALUTO: scrivi esattamente "{saluto}"
2. AGGANCIO personalizzato (1 frase): mostra che hai capito cosa fa dalla bio e collegalo
   al dolore operativo. Ispirazione: {brief.get('apertura', opener)}
3. PROBLEMA OPERATIVO concreto (1 frase): {nd.get('niche_term', '')}.
   Quantifica le ore o il lavoro manuale perso, MAI parlare di conversioni o di clienti persi.
4. SOLUZIONE (1-2 frasi): nomina {prodotto} UNA sola volta e di' che e' un workflow che fa
   tutto al 100%, installato sui SUOI server, codice suo, zero canoni, pronto in 7 giorni.
   Cosa fa (NON ripetere "ti installo sui server", e' gia' detto sopra): {sol_descr[:110]}
5. FIDUCIA + PRESENTAZIONE (1 frase): l'unica vera domanda e' fidarsi, per questo glielo mostri.
   Te la mostro qui: {PRESENTATION_URL}
6. CTA breve a basso attrito (1 frase): {nd['cta']}

REGOLE — VIOLARNE UNA RENDE IL MESSAGGIO INUTILIZZABILE:
- DEVE iniziare esattamente con "{saluto}"
- MAI iniziare con virgolette o apostrofi
- ZERO trattini (-) e ZERO esclamativi (!) in tutto il messaggio
- ZERO lettere accentate: scrivi "operativita'", "gia'", "piu'", "perche'", "e'" con l'apostrofo
- INCLUDI il link {PRESENTATION_URL} (e' obbligatorio)
- INCLUDI il nome del prodotto "{prodotto}"
- NON scrivere nessuna firma: al "Max" e al link agency ci pensa il sistema dopo
- ZERO "Salve", "Gentile", "Spero stia bene", "ti contatto perche'", zero AI slop
- Scrivi in italiano, tono diretto e umano, da founder a founder
- TRA 55 E 85 PAROLE: abbastanza da dare valore e struttura, mai telegrafico

RISPOSTA: scrivi ESCLUSIVAMENTE il testo del messaggio DM, dal saluto alla CTA, SENZA firma.
ZERO spiegazioni, ZERO commenti, ZERO note, ZERO intestazioni. Se la risposta contiene
qualcosa che non e' il messaggio stesso, il sistema si rompe."""

    elif tipo == "followup1":
        if not _AI_OK:
            return _fallback(lead, nd, "followup1")

        prompt = f"""Follow-up Instagram per @{username} ({nicchia}). Non ha risposto al primo DM (2-3 giorni fa).
Vendiamo {prodotto}: workflow AI installato sui suoi server, codice incluso, zero canoni, automazione 100%.

STRUTTURA ESATTA (MAX 35 parole):
1. Saluto breve: "{saluto}"
2. 1 frase nuova di valore sul vantaggio operativo (usa: {nd.get('niche_term', nd['problema'][:60])})
3. Ricorda che la presentazione e' qui: {PRESENTATION_URL}
4. CTA binaria si/no

REGOLE:
- DEVE iniziare con "{saluto}"
- MAI "Spero non disturbi", "Scusa il disturbo", "Volevo solo"
- ZERO trattini (-), ZERO esclamativi (!), ZERO virgolette iniziali
- INCLUDI il link {PRESENTATION_URL}
- Firma "Max"
- MAX 35 parole totali

RISPOSTA: SOLO il messaggio, nessun altro testo."""

    else:  # followup2
        if not _AI_OK:
            return _fallback(lead, nd, "followup2")

        prompt = f"""TERZO e ULTIMO DM Instagram per @{username} ({nicchia}).
Ha ricevuto 2 messaggi senza risposta — messaggio di break-up.
Vendiamo {prodotto}: workflow AI installato sui suoi server, codice incluso, zero canoni, automazione 100%.

STRUTTURA ESATTA (MAX 45 parole):
1. "{saluto}"
2. "Ultimo messaggio da parte mia."
3. 1 risultato concreto (usa: {nd.get('proof_hint', nd['danno'])})
4. Presentazione: {PRESENTATION_URL}
5. Ricorda lo {LAUNCH_OFFER[:55]}
6. "Si o no, rispetto entrambe."
7. Firma "Max"

REGOLE:
- DEVE iniziare con "{saluto}"
- ZERO trattini (-), ZERO esclamativi (!), ZERO virgolette iniziali
- INCLUDI il link {PRESENTATION_URL}
- Tono diretto, senza pressione
- MAX 45 parole totali

RISPOSTA: SOLO il messaggio, nessun altro testo."""

    resp = _ai(prompt, max_tokens=200)
    return resp if resp else _fallback(lead, nd, tipo)


# ── AGENTE 3: HUMANIZER ───────────────────────────────────────────────────────

def run_humanizer(msg: str, lead: dict) -> tuple[str, float, str]:
    if not _AI_OK:
        return msg, 8.0, ""

    # Controlli immediati senza AI
    # NB: PRESENTATION_URL è ora ATTESO nel primo DM — NON va penalizzato.
    errori = []
    prima_char = msg.strip()[0] if msg.strip() else ""
    if prima_char in ('"', "'", "“", "‘"):
        errori.append("inizia con virgolette")

    # Trattini: ignora quelli interni all'URL della presentazione.
    msg_senza_url = msg.replace(PRESENTATION_URL, "").replace(AGENCY_URL, "")
    if " - " in msg_senza_url or msg_senza_url.lstrip().startswith("- "):
        errori.append("contiene trattini")

    if "!" in msg:
        errori.append("contiene esclamativi")
    if not msg.strip().lower().startswith("ciao"):
        errori.append("non inizia con Ciao")
    if PRESENTATION_URL not in msg:
        errori.append("manca il link presentazione")

    if errori:
        return msg, 4.0, " | ".join(errori)

    prompt = f"""Valuta questo DM Instagram (1-10 per criterio). Vendiamo un'IMPLEMENTAZIONE AI
(workflow installato sui server del cliente, codice incluso, zero canoni, automazione 100%).

MESSAGGIO:
{msg}

LEAD: {lead.get('nicchia', '')} @{lead.get('username', '')}

CRITERI:
1. SALUTO: inizia con "Ciao [nome]"?
2. HYPE/PROBLEMA: opener sull'automazione + un solo problema operativo chiaro?
3. SOLUZIONE: nomina il prodotto e dice che e' un workflow 100% (codice tuo, zero canoni)?
4. PRESENTAZIONE+CTA: include il link presentazione e una CTA binaria a basso attrito?
5. HUMANNESS: sembra scritto da un umano, zero AI slop?

PENALITA' AUTOMATICHE (se presenti, media scende a 3):
- Inizia con virgolette -> -5
- Contiene trattini (-) fuori dal link -> -3
- Contiene esclamativi (!) -> -2
- Manca il link presentazione -> -4

NB: la presenza del link presentazione e' ATTESA e POSITIVA, non penalizzarla.

Rispondi SOLO JSON:
{{"op": X, "prob": X, "sol": X, "cta": X, "h": X, "media": X.X, "fix": "problema in 8 parole"}}"""

    resp = _ai(prompt, max_tokens=100)
    if resp:
        try:
            cleaned = resp.strip().lstrip("```json").lstrip("```").rstrip("```").strip()
            data = json.loads(cleaned)
            return msg, float(data.get("media", 7.5)), data.get("fix", "")
        except Exception:
            pass
    return msg, 7.5, ""


# ── PIPELINE PUBBLICA ──────────────────────────────────────────────────────────

def _pulisci(msg: str) -> str:
    """
    Rimuove meta-commentary AI, virgolette, testo dopo firma.
    Garantisce che il risultato inizi con "Ciao" o sia fallback.
    NON rimuove mai il link presentazione (PRESENTATION_URL).
    """
    import re
    msg = msg.strip()

    # 1. Strip virgolette esterne (smart + normali)
    OPEN_Q  = ('"', '“', '‘', "'")
    CLOSE_Q = ('"', '”', '’', "'")
    if msg and msg[0] in OPEN_Q:
        msg = msg[1:].strip()
    if msg and msg[-1] in CLOSE_Q:
        msg = msg[:-1].strip()

    # 2. Rimuovi meta-commentary iniziale
    #    Es. "Ecco un'opzione:\n\n\"Ciao...\"\n\nQuesta versione..."
    first_line_l = msg.split('\n')[0].lower()
    META = ['ecco', 'qui di seguito', 'di seguito', 'possibile revisione',
            'opzione di revisione', 'revisione del messaggio', 'proposta',
            'questa versione', 'questa revisione']
    if any(w in first_line_l for w in META):
        # Cerca "Ciao" nel testo e prendi da lì
        lower = msg.lower()
        ciao_pos = lower.find('ciao')
        if ciao_pos > 0:
            msg = msg[ciao_pos:].strip()
        else:
            # Prendi testo tra prime virgolette doppie (il messaggio vero)
            m = re.search(r'["“]([^"”]{20,})["”]', msg, re.DOTALL)
            if m:
                msg = m.group(1).strip()

    # 3. Se inizia ancora con meta-commentary senza virgolette, estrai da Ciao
    lower = msg.lower()
    if not lower.startswith('ciao'):
        ciao_pos = lower.find('\nciao')
        if ciao_pos >= 0:
            msg = msg[ciao_pos:].strip()

    # 4. Taglia tutto ciò che viene dopo la firma "Max".
    #    Cerca "Max" SOLO dopo la posizione del link presentazione, così non
    #    tronchiamo mai prima del link (il link è atteso e deve restare).
    url_pos = msg.find(PRESENTATION_URL)
    search_from = (url_pos + len(PRESENTATION_URL)) if url_pos >= 0 else 0
    max_match = re.search(r'\bMax\b', msg[search_from:], re.IGNORECASE)
    if max_match:
        abs_end = search_from + max_match.end()
        after = msg[abs_end:].strip()
        # Se c'è testo dopo Max che NON è vuoto/punteggiatura finale
        if after and not re.match(r'^[.,!?\s]*$', after):
            msg = msg[:abs_end].strip()

    # 5. Strip virgolette finali rimaste
    if msg and msg[-1] in CLOSE_Q:
        msg = msg[:-1].strip()

    # 6. Normalizza trattini SENZA toccare il link presentazione.
    #    Proteggi l'URL con un placeholder, normalizza, poi ripristina.
    _PH = "\x00URL\x00"
    msg = msg.replace(PRESENTATION_URL, _PH)
    msg = re.sub(r' - ', ', ', msg)
    msg = re.sub(r'(?m)^- ', '', msg)
    msg = msg.replace(_PH, PRESENTATION_URL)

    return msg.strip()


# Mappa accenti → forma ASCII con apostrofo: evita il mojibake ("gia'" non "gi�")
# quando run_today digita il DM carattere per carattere su Instagram.
_ACCENTI = {
    "à": "a'", "è": "e'", "é": "e'", "ì": "i'", "í": "i'",
    "ò": "o'", "ó": "o'", "ù": "u'", "ú": "u'",
    "À": "A'", "È": "E'", "É": "E'", "Ì": "I'", "Ò": "O'", "Ù": "U'",
}


def _no_accenti(testo: str) -> str:
    """Converte le lettere accentate in forma apostrofata e rimuove i caratteri
    di rimpiazzo (corruzione UTF-8). Instagram via Playwright sbaglia gli accenti."""
    for a, b in _ACCENTI.items():
        testo = testo.replace(a, b)
    return testo.replace("�", "")


def _enforce_corpo(msg: str) -> str:
    """Pulisce il corpo del DM: rimuove accenti rotti, strutture di firma residue.
    Ritorna SOLO il corpo (niente firma, niente link agency).
    Il link agency va mandato in un SECONDO messaggio separato."""
    if not msg:
        return msg
    import re
    testo = _no_accenti(msg).rstrip()
    # Rimuovi ripetutamente firma/agency residue dal corpo (se l'AI le ha messe)
    prev = None
    while prev != testo:
        prev = testo
        testo = re.sub(r"https://agency-empire[^\s]*", "", testo).rstrip()
        testo = re.sub(r"[\s,;:.\-—|]*\bMax\b[.\s]*$", "", testo).rstrip()
    return testo.strip()


def _get_link_message() -> str:
    """Ritorna il secondo messaggio: firma + link agency.
    Viene inviato come messaggio SEPARATO subito dopo il primo DM (IG e LinkedIn solo).
    Per email, la firma sta alla fine del corpo nello stesso messaggio."""
    agency = os.getenv("AGENCY_URL_OVERRIDE", AGENCY_URL)
    return f"Maximilian - Agency | Digital Empire\nlink sito web: {agency}"


def generate_dm(lead: dict) -> str:
    nd    = NICCHIE[get_nicchia(lead.get("bio", "") + " " + lead.get("nicchia", ""))]
    brief = run_strategist(lead, nd)
    msg   = run_writer(lead, brief, nd, "primo")
    msg   = _pulisci(msg)

    # Hard check: il messaggio DEVE iniziare con "Ciao" e contenere il link presentazione
    def _valido(m: str) -> bool:
        return m.strip().lower().startswith("ciao") and PRESENTATION_URL in m

    if not _valido(msg):
        msg2 = run_writer(lead, brief, nd, "primo")
        msg2 = _pulisci(msg2)
        if _valido(msg2):
            msg = msg2
        else:
            msg = _fallback(lead, nd, "primo")  # fallback deterministico sempre valido

    _, score, fix = run_humanizer(msg, lead)

    if score < 6.5 and _AI_OK and fix and _valido(msg):
        username = lead.get("username", "")
        nicchia  = lead.get("nicchia", "")
        prodotto = nd.get("prodotto", "Outreach Factory")
        nome = _estrai_nome(lead.get("bio", ""), username)
        saluto = f"Ciao {nome}" if nome else "Ciao"
        retry = _ai(
            f"Riscrivi questo DM Instagram. Problema: {fix}\n\n"
            f"ORIGINALE:\n{msg}\n\n"
            f"REGOLE ASSOLUTE: inizia con '{saluto}', ZERO virgolette iniziali, "
            f"ZERO trattini (-), ZERO esclamativi (!), ZERO lettere accentate (usa l'apostrofo: gia', piu', e'), "
            f"INCLUDI il nome prodotto '{prodotto}', INCLUDI il link {PRESENTATION_URL}, "
            f"tra 55 e 85 parole, frasi complete mai telegrafiche, NESSUNA firma. "
            f"Nicchia: {nicchia}. Solo il messaggio.",
            max_tokens=200
        )
        if retry:
            retry_clean = _pulisci(retry)
            if _valido(retry_clean):
                msg = retry_clean
    # Corpo pulito (senza firma) + link_msg separato per secondo messaggio
    corpo = _enforce_corpo(msg)
    return {"corpo": corpo, "link_msg": _get_link_message()}


def generate_followup1(lead: dict) -> dict:
    """Ritorna dict {corpo, link_msg}. Followup1 include il link presentazione nel corpo."""
    nd = NICCHIE[get_nicchia(lead.get("bio", "") + " " + lead.get("nicchia", ""))]
    msg = _pulisci(run_writer(lead, {}, nd, "followup1"))
    corpo = _enforce_corpo(msg)
    return {"corpo": corpo, "link_msg": _get_link_message()}


def generate_followup2(lead: dict, agency_url: str = AGENCY_URL) -> dict:
    """Ritorna dict {corpo, link_msg}. Followup2 è il breakup — non include link agency nel corpo."""
    os.environ["AGENCY_URL_OVERRIDE"] = agency_url
    nd = NICCHIE[get_nicchia(lead.get("bio", "") + " " + lead.get("nicchia", ""))]
    msg = _pulisci(run_writer(lead, {}, nd, "followup2"))
    corpo = _enforce_corpo(msg)
    return {"corpo": corpo, "link_msg": _get_link_message()}


def classify_and_reply(username: str, nicchia: str, loro_msg: str, nostro_msg: str) -> dict:
    """Classifica la risposta ricevuta e genera la replica.
    Obiettivo: prenotare la call / far guardare la presentazione."""
    if not _AI_OK:
        return _fallback_reply(loro_msg)

    prompt_class = f"""Classifica questo DM Instagram ricevuto dopo la nostra proposta di
un'implementazione AI (workflow installato sui server del cliente, automazione 100%).

NOSTRO ULTIMO MESSAGGIO: {nostro_msg[:200]}
LORO RISPOSTA: {loro_msg[:300]}

Categoria:
- POSITIVO: interessato, vuole info, aperto a call
- OBIEZIONE: resistenza (fiducia, prezzo, tempo, "lo faccio già")
- DOMANDA: chiede dettagli, come funziona, costi
- NON_INTERESSATO: no chiaro

JSON: {{"categoria": "X", "sintesi": "<5 parole>"}}"""

    categoria = "POSITIVO"
    resp_class = _ai(prompt_class, max_tokens=80)
    if resp_class:
        try:
            data = json.loads(resp_class.strip().lstrip("```json").rstrip("```"))
            categoria = data.get("categoria", "POSITIVO")
        except Exception:
            pass

    prompt_reply = f"""Sei Max su Instagram. Rispondi a @{username} ({nicchia}).
Vendiamo un'implementazione AI: workflow installato sui server del cliente, codice incluso,
zero canoni, automazione 100%. L'unica obiezione vera e' la fiducia: per questo la mostri live.

LORO MESSAGGIO: {loro_msg[:300]}
CATEGORIA: {categoria}

REGOLE:
- Prima persona singolare — MAI noi/offriamo
- MAX 55 parole
- ZERO esclamativi, ZERO "Grazie per la risposta"
- OBIETTIVO: prenotare una call gratuita di 20 minuti in cui mostro il workflow live
- Puoi rimandare alla presentazione: {PRESENTATION_URL}
- POSITIVO: proponi 2-3 slot concreti per la call
- OBIEZIONE: e' solo questione di fiducia, te lo mostro live in 20 minuti, gratis
- DOMANDA: rispondi breve + call per vederlo girare
- NON_INTERESSATO: max 15 parole, porta aperta

Solo il messaggio."""

    testo = _ai(prompt_reply, max_tokens=150)
    if not testo:
        testo = _fallback_reply(loro_msg)["testo"]

    return {"categoria": categoria, "testo": testo.strip()}


# ── FALLBACK ──────────────────────────────────────────────────────────────────

def _fallback(lead: dict, nd: dict, tipo: str) -> str:
    nome = _estrai_nome(lead.get("bio", ""), lead.get("username", ""))
    saluto = f"Ciao {nome}" if nome else "Ciao"
    opener = nd.get("barnum", "")
    prodotto = nd.get("prodotto", "Outreach Factory")

    if tipo == "primo":
        # La soluzione inizia con "ti installo {prodotto} sui tuoi server: ...":
        # taglio la testa per evitare ripetizioni e tengo la parte descrittiva.
        soluzione = nd.get('soluzione', '')
        sep = ":"
        descr = soluzione.split(sep, 1)[1].strip() if sep in soluzione else soluzione
        if not descr:
            descr = "automatizza la tua operativita' al 100%, codice tuo e zero canoni"
        problema = nd.get("niche_term", nd.get("problema", ""))
        garanzie = "" if "canoni" in descr.lower() else ", codice tuo, zero canoni"
        return (
            f"{saluto}, {opener.lower() if opener else 'chi manda avanti un business online ha sempre un processo operativo che ruba ore e non scala.'} "
            f"Il punto e' uno: {problema[:90].rstrip('.')}. "
            f"Ti installo {prodotto} sui tuoi server e lo fa al 100%: {descr[:130].rstrip('.')}{garanzie}, pronto in 7 giorni. "
            f"L'unica vera domanda e' la fiducia, per questo te lo mostro. "
            f"Te la mostro qui: {PRESENTATION_URL} "
            f"C'e' lo {LAUNCH_OFFER}. {nd['cta']}"
        )
    elif tipo == "followup1":
        return (
            f"{saluto}, un punto rapido: {nd.get('niche_term', nd['problema'][:60])}. "
            f"Te lo mostro qui: {PRESENTATION_URL} "
            f"{nd['cta']}"
        )
    else:
        return (
            f"{saluto}, ultimo messaggio da parte mia. "
            f"{nd.get('proof_hint', nd['danno'])}. "
            f"La presentazione e' qui: {PRESENTATION_URL} "
            f"C'e' ancora lo {LAUNCH_OFFER}. "
            f"Si o no, rispetto entrambe."
        )


def _fallback_reply(msg: str) -> dict:
    tl = msg.lower()
    if any(w in tl for w in ["no grazie", "non interess", "rimuovi", "smettila", "basta"]):
        return {"categoria": "NON_INTERESSATO", "testo": "Capito, nessun problema. Se mai cambia qualcosa, sai dove trovarmi."}
    return {
        "categoria": "POSITIVO",
        "testo": (
            "Ho disponibilita' martedi alle 10, giovedi alle 15 o venerdi alle 11. "
            "In 20 minuti gratuiti ti faccio vedere il workflow girare live. "
            f"Intanto la presentazione e' qui: {PRESENTATION_URL}. Ti va uno di questi slot?"
        ),
    }


# ── TEST ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    leads = [
        {"username": "growthlab_agency", "bio": "Andrea | Agenzia marketing digitale | Lead gen B2B | Milano", "nicchia": "agenzia"},
        {"username": "marco.businesscoach", "bio": "Marco | Business coach per imprenditori | Mindset e scaling", "nicchia": "coach"},
        {"username": "giulia_smm", "bio": "Giulia | Social media manager freelance | Brand e personal branding", "nicchia": "smm_freelance"},
        {"username": "formazione.luca", "bio": "Luca | Formatore e corsi online | Lancio del mio nuovo corso", "nicchia": "info_product"},
        {"username": "atelier.shop", "bio": "Sara | Brand e-commerce moda | Shopify | spedizioni in tutta Italia", "nicchia": "ecommerce"},
    ]
    print(f"AI disponibile: {_AI_OK}\n")
    for lead in leads:
        nicchia_key = get_nicchia(lead.get("bio", "") + " " + lead.get("nicchia", ""))
        prodotto = NICCHIE[nicchia_key].get("prodotto", "?")
        print(f"=== @{lead['username']} -> nicchia '{nicchia_key}' -> {prodotto} ===")
        print("-- PRIMO DM --")
        print(generate_dm(lead))
        print("-- FOLLOW-UP 1 --")
        print(generate_followup1(lead))
        print("-- FOLLOW-UP 2 --")
        print(generate_followup2(lead, AGENCY_URL))
        print()
