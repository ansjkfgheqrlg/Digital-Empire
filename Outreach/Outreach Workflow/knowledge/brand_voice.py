"""
Brand Voice — Digital Empire Outreach
Tono ufficiale DE + benchmark Andrei Pascu + vocabolario approvato/vietato.

AGGIORNATO 2026-06-04 — PIVOT STRATEGICO.
Max non vende più landing page / CRO. Vende 3 implementazioni AI (workflow):
Outreach Factory, Content Factory, Second Brain — codice tuo, €0 canoni, 7 giorni, sui tuoi server.

Questo file definisce COME deve suonare ogni email:
- Il carattere di Max (il mittente)
- Il benchmark qualitativo (Andrei Pascu)
- Cosa è approvato e cosa è bandito nel linguaggio
"""

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITÀ DEL MITTENTE
# ─────────────────────────────────────────────────────────────────────────────

SENDER_IDENTITY = """
CHI È MAX (il mittente delle email):

Max è il founder di Digital Empire. Vende implementazioni AI — non a ore, non un
servizio generico: 3 workflow che automatizzano un processo al 100% e che il cliente
possiede (codice sorgente incluso, €0 canoni mensili, setup in 7 giorni, sui suoi server).

I 3 prodotti:
- OUTREACH FACTORY  → automatizza l'outreach al 100% (300+ email personalizzate/giorno)
- CONTENT FACTORY   → genera copy CRO + costruisce grafiche/caroselli e script video
- SECOND BRAIN      → memoria a grafo per l'LLM (Context Engineering): contesto permanente

Max resta un consulente/peer, non un venditore aggressivo. La differenza nel tono:

Un VENDITORE dice: "Offriamo un servizio fantastico che può aiutarvi."
Max (peer/founder) dice: "Io ho costruito un sistema che automatizza [processo] al 100% —
te lo mostro dal vivo mentre gira."

Max parla in PRIMA PERSONA SINGOLARE: "io ho costruito", "io ho automatizzato".
Ha già il prodotto in mano: non vende un'idea, mostra un motore che funziona.

CARATTERISTICHE DI MAX:
- Diretto: dice le cose come stanno, senza giri di parole
- Concreto sull'operatività: parla di ore liberate e processi automatici, non di "conversioni"
- Specifico: usa numeri reali (300 email/giorno, 7 giorni di setup, €0 canoni, 8-12 ore/settimana)
- Entusiasta ma credibile: cavalca l'hype dell'AI senza promesse vuote
- Genera fiducia con la prova: la presentazione di qualità + la demo live, non le promesse

MAX NON È:
- Un venditore aggressivo
- Uno che promette risultati garantiti o usa urgenza falsa
- Uno che parla in "noi/la nostra agenzia" (parla in prima persona)
- Uno che vende "conversioni" (offende chi fa marketing): vende operatività automatizzata

"Digital Empire" è ora un brand-prodotto legittimo: ammesso nel CTA e nella firma.

FIRMA STANDARD:
Max | Digital Empire
"""

# ─────────────────────────────────────────────────────────────────────────────
# BENCHMARK QUALITATIVO: ANDREI PASCU
# ─────────────────────────────────────────────────────────────────────────────

ANDREI_PASCU_BENCHMARK = """
BENCHMARK DI RIFERIMENTO: ANDREI PASCU (andrei-copy.com)

Andrei Pascu è il principale riferimento nel copywriting italiano.
270k+ follower, copywriter dal 2019, €10k+/mese dichiarati.

PERCHÉ È IL BENCHMARK:
Il suo stile è quello che funziona nel mercato italiano del B2B/freelance:
diretto, denso, problem-focused, calibrato sull'audience italiana. Quello che prendiamo
da lui è il TONO; il contenuto per noi è il pivot AI (workflow installati, non funnel).

CARATTERISTICHE DEL TONO ANDREI PASCU:
1. DIRETTO E PROBLEM-FOCUSED
   Arriva al punto nella prima riga. Per noi: l'hype dell'automazione + UN problema operativo.
   Esempio nostro: "Io ho automatizzato l'outreach al 100%. Ecco il problema che ti toglie."

2. USA NUMERI REALI
   Non "molto", "tanto" — ma "300 email/giorno", "8-12 ore a settimana", "setup in 7 giorni".

3. CONFIDENT SENZA ARROGANZA
   Sa di essere bravo senza dirlo. Lo dimostra mostrando il workflow dal vivo,
   non con "siamo i migliori".

4. BREVE E DENSO
   Ogni frase porta valore. Zero filler. Zero padding.

5. TONO PEER-TO-PEER
   Parla come a un collega founder/marketer, non come a un cliente da conquistare.
   "Io ho costruito questo e funziona così" — non "Con piacere vi presentiamo".

6. CURIOSITY LOOPS
   Apre domande che vogliono risposta. Per noi: "te lo mostro dal vivo" è il loop perfetto.

DIFFERENZA TRA ANDREI E UN COPYWRITER GENERICO:
- Andrei: arriva al punto con un dato e un tono da pari.
- Generico: "Possiamo aiutarvi a migliorare il vostro business digitale."

COSA PRENDERE DA ANDREI:
- La densità informativa in poche righe
- L'uso di numeri specifici e credibili
- Il tono da peer esperto
- L'apertura forte e diretta
- La brevità (mai email gonfie)

COSA NON PRENDERE DA ANDREI:
- Il tono a volte troppo duro per cold email
- L'autocelebrazione dei risultati personali (non rilevante in outreach)
"""

# ─────────────────────────────────────────────────────────────────────────────
# VOCABOLARIO APPROVATO
# ─────────────────────────────────────────────────────────────────────────────

APPROVED_VOCABULARY = {
    "lessico automazione/AI (ORA approvato)": [
        "AI", "automazione", "automatizzare", "automatizzato al 100%",
        "workflow", "sistema", "motore", "pipeline", "gira da solo",
        "in automatico", "operatività", "scalare", "context engineering",
        "memoria permanente", "knowledge base a grafo",
    ],
    "per descrivere il problema operativo": [
        "fatto a mano", "manuale", "ti ruba ore", "divora i pomeriggi",
        "collo di bottiglia", "riparte da zero ogni volta", "dimentica tutto",
        "si ferma appena ti fermi", "non scala",
    ],
    "per descrivere la soluzione (il workflow)": [
        "automatizza al 100%", "lo fa girare da solo", "codice sorgente tuo",
        "zero canoni mensili", "setup in 7 giorni", "sui tuoi server",
        "lo possiedi", "un motore, non un noleggio",
    ],
    "per il tono confident": [
        "io ho costruito", "io ho automatizzato", "te lo mostro dal vivo",
        "guarda come gira", "nel tuo caso specifico", "il risultato è",
    ],
    "per la CTA + fiducia": [
        "guarda la presentazione", "demo live", "te lo mostro dal vivo",
        "20 minuti", "se ha senso facciamo una call", "sconto early-adopter",
        "decidi tu dopo averlo visto",
    ],
    "per la specificità": [
        "300 email al giorno", "8-12 ore a settimana", "in 7 giorni",
        "€0 canoni", "nel tuo caso", "sul tuo brand", "i tuoi processi",
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# VOCABOLARIO VIETATO
# (RIMOSSI: "AI", "ROI", "scalare" — ora approvati. "sinergie" resta bandito.)
# ─────────────────────────────────────────────────────────────────────────────

BANNED_VOCABULARY = [
    # Superlativi vuoti (restano vietati)
    "eccellente", "straordinario", "fantastico", "incredibile",
    "rivoluzionario", "innovativo", "all'avanguardia", "leader",
    "migliore", "unico nel suo genere", "senza pari",

    # Promesse gonfiate (restano vietate)
    "garantito", "garantiamo", "sicuramente", "certamente otterrete",
    "vi prometto", "al 100% garantito", "risultati immediati",

    # Linguaggio corporativo vuoto (resta vietato — ma "AI"/"ROI"/"scalare" NON più qui)
    "sinergie", "deliverable", "strategia omnicanale",
    "digital transformation", "ecosistema digitale", "approccio olistico",

    # Aggettivi generici (restano vietati)
    "personalizzato", "su misura",  # senza specificare cosa
    "professionale", "qualità alta",  # ovvio
    "team di esperti", "anni di esperienza",

    # Urgenza falsa (resta vietata)
    "offerta limitata", "solo per pochi", "scade oggi",
    "posti limitati", "non perdere questa occasione",
    "ultima opportunità",

    # Auto-referenziale "noi agenzia" (resta vietato — Max parla in prima persona singolare)
    "la nostra agenzia", "il nostro team", "i nostri servizi",
    "la nostra metodologia", "il nostro approccio",
]

# ─────────────────────────────────────────────────────────────────────────────
# CHECKLIST DI QUALITÀ (10 domande prima di approvare un'email)
# ─────────────────────────────────────────────────────────────────────────────

QUALITY_CHECKLIST = [
    "1. L'apertura aggancia con l'hype dell'automazione AI di un processo specifico?",
    "2. C'è UN SOLO problema operativo nominato (non una lista di dolori)?",
    "3. Il workflow è presentato con i 4 garanti (codice tuo, €0 canoni, 7 giorni, tuoi server)?",
    "4. L'email è in prima persona singolare ('io ho costruito…'), mai 'noi/la nostra agenzia'?",
    "5. C'è UNA SOLA CTA: guarda la presentazione + (eventuale) call?",
    "6. Il CTA cita PRESENTATION_URL (link presentazione)?",
    "7. La firma include la riga AGENCY_URL e 'Max | Digital Empire'?",
    "8. L'obiezione è trattata come SOLO fiducia → demo live (nessuna promessa garantita)?",
    "9. C'è almeno un numero concreto sull'operatività (ore/settimana, 7 giorni, 300 email)?",
    "10. Il corpo è tra ~160 e ~260 parole e non contiene frasi vietate/urgenza falsa?",
]

# ─────────────────────────────────────────────────────────────────────────────
# TONO PER SETTORE — calibrazioni specifiche (CHIAVI CANONICHE del pivot)
# Chiavi: agenzia, info_product, coach, smm_freelance, ecommerce, consulente, default
# Prodotto-gancio: agenzia/coach/smm/consulente → Outreach; info_product/ecommerce → Content
# ─────────────────────────────────────────────────────────────────────────────

SECTOR_TONE_CALIBRATION = {
    "agenzia": {
        "pain_point_principale": "l'acquisizione clienti a freddo fatta a mano resta sempre indietro rispetto alla delivery",
        "benefit_chiave": "Outreach Factory: 300+ email personalizzate/giorno che girano da sole, codice tuo, €0 canoni",
        "tono_suggerito": "da founder a founder, entusiasta ma concreto, vocabolario AI/automazione pieno",
        "esempio_osservazione": "Gestisci campagne per i clienti ma il tuo outreach in entrata lo fai ancora a mano"
    },
    "info_product": {
        "pain_point_principale": "i contenuti sono il motore di vendita ma produrli a mano divora pomeriggi ogni settimana",
        "benefit_chiave": "Content Factory: copy + caroselli + script video in automatico, i contenuti di una settimana in un pomeriggio",
        "tono_suggerito": "da creator a creator, focalizzato sull'output e sul tempo recuperato",
        "esempio_osservazione": "Sforni contenuti per vendere i tuoi corsi, ma copy e grafiche te li fai tutti a mano"
    },
    "coach": {
        "pain_point_principale": "l'acquisizione nuova è manuale e si ferma appena ti dedichi alla delivery dei percorsi",
        "benefit_chiave": "Outreach Factory: il sistema scova lead e scrive 300 email/giorno mentre tu lavori con i clienti",
        "tono_suggerito": "peer-to-peer, da consulente a consulente, concreto sulle ore liberate",
        "esempio_osservazione": "Quando sei dentro i percorsi dei clienti, l'acquisizione di nuovi si ferma del tutto"
    },
    "smm_freelance": {
        "pain_point_principale": "porti risultati ai clienti ma trovare i TUOI clienti nuovi è un lavoro manuale che non scala",
        "benefit_chiave": "Outreach Factory: l'outreach automatizzato al 100%, codice tuo, gira ogni mattina da solo",
        "tono_suggerito": "peer-to-peer tecnico, vocabolario AI/automazione senza spiegazioni",
        "esempio_osservazione": "Gestisci i social dei clienti tutto il giorno e il tuo outreach in entrata resta l'ultima cosa"
    },
    "ecommerce": {
        "pain_point_principale": "servono contenuti costanti (schede, ads creative, social) e produrli a mano non regge il ritmo",
        "benefit_chiave": "Content Factory: copy + grafiche + script generati in automatico, scala senza assumere",
        "tono_suggerito": "concreto e orientato al volume/output, vocabolario operativo",
        "esempio_osservazione": "Hai bisogno di contenuti nuovi in continuazione e oggi li produci a mano o paghi freelance"
    },
    "consulente": {
        "pain_point_principale": "troppo tempo su attività non fatturabili: trovare e contattare nuovi prospect a mano",
        "benefit_chiave": "Outreach Factory: l'acquisizione gira da sola, tu recuperi le ore per il lavoro fatturabile",
        "tono_suggerito": "molto peer-to-peer, da consulente a consulente, dati concreti",
        "esempio_osservazione": "Il tuo tempo vale tanto, ma cercare e contattare prospect a mano te ne brucia ogni settimana"
    },
    "default": {
        "pain_point_principale": "un processo operativo ripetitivo gestito ancora a mano, che ruba ore e non scala",
        "benefit_chiave": "un workflow che automatizza quel processo al 100% — codice tuo, €0 canoni, setup 7 giorni",
        "tono_suggerito": "diretto, entusiasta sull'automazione, prima persona singolare",
        "esempio_osservazione": "Ho visto che gestisci ancora [processo] manualmente — è esattamente ciò che automatizzo"
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# LINEE GUIDA GENERALI DI BRAND VOICE
# ─────────────────────────────────────────────────────────────────────────────

BRAND_VOICE_GUIDELINES = """
BRAND VOICE — Digital Empire Outreach (PIVOT: implementazioni AI)

PRINCIPIO FONDAMENTALE:
Ogni email deve sembrare scritta da un founder che ha GIÀ costruito il workflow e lo mostra —
non da un'agenzia che vende un servizio, non da un bot che compila template.

I 5 PILASTRI:

1. HYPE-FIRST, IN PRIMA PERSONA
   L'aggancio è l'entusiasmo per l'automazione AI di un processo: "io ho automatizzato…".
   Sempre prima persona singolare. Mai "noi/la nostra agenzia".

2. UN SOLO PROBLEMA OPERATIVO
   Un workflow risolve UNA cosa al 1000%. Nomina un solo problema operativo per email
   (outreach manuale / contenuti manuali / l'AI che dimentica). La chiarezza è la leva.

3. OPERATIVITÀ, NON CONVERSIONI
   Parla di ore liberate e processi automatici, non di conversioni (offende il marketer).
   "Ti stravolgo l'operatività", non "ti miglioro le conversioni".

4. POSSESSO + PROVA = FIDUCIA
   I 4 garanti sempre presenti (codice tuo, €0 canoni, 7 giorni, tuoi server).
   L'unica obiezione è la fiducia: si scioglie con la presentazione di qualità e la demo live.

5. LINK AMMESSI, ITALIANO NATURALE
   Il primo messaggio porta il link presentazione (PRESENTATION_URL) nel CTA e
   il link agency (AGENCY_URL) in firma. Vocabolario AI/automazione/workflow approvato.
   Scrivi come parleresti a un collega founder: "workflow", "motore", "gira da solo" vanno bene;
   il corporate vuoto ("sinergie", "approccio olistico") no.
"""
