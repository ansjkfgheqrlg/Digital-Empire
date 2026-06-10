"""
APSOC Framework + Triple Tap + Template A/B/C + CPB + Direct Response Principles
+ Deliverability Rules + LinkedIn DM Framework
Fonte: wiki/concepts/Concept_Copywriting_Framework.md + regole/04_drafta_email.md
       + NotebookLM: "Outreach + Claude Code", "Multi-AI Outreach and CRO", "Cold Outreach LinkedIn"

AGGIORNATO 2026-06-04 — PIVOT STRATEGICO.
Digital Empire NON vende più landing page / CRO.
Vende 3 PRODOTTI = IMPLEMENTAZIONI AI installate sui server del cliente
(codice sorgente incluso, €0 canoni mensili, setup 7 giorni, automazione 100%):
  - TEMPLATE_A = Outreach Factory  (automatizza l'outreach al 100%)
  - TEMPLATE_B = Content Factory   (genera copy + grafiche + script video)
  - TEMPLATE_C = Second Brain      (memoria a grafo per l'LLM — Context Engineering)

Questo file è il "cervello copy" del sistema.
Ogni agente che deve scrivere o valutare email carica queste costanti.
"""

# ─────────────────────────────────────────────────────────────────────────────
# COSTANTI DI CONTRATTO — link e offerta (condivise con tutti gli agenti)
# ─────────────────────────────────────────────────────────────────────────────

PRESENTATION_URL = "https://presentazione-empire.vercel.app/"
AGENCY_URL = "https://agency-empire-landing.vercel.app"
LAUNCH_OFFER = "sconto early-adopter per i primi clienti che partono questo mese"

# ─────────────────────────────────────────────────────────────────────────────
# DELIVERABILITY RULES — PRIORITÀ ASSOLUTA (viola queste e le email non arrivano)
# Fonte: NotebookLM "Outreach + Claude Code" — framework professionisti reali
# AGGIORNATO: con il pivot il PRIMO messaggio porta il link presentazione.
# ─────────────────────────────────────────────────────────────────────────────

DELIVERABILITY_RULES = """
REGOLE DELIVERABILITY — NON NEGOZIABILI

NUOVA POLICY (pivot 2026): il primo messaggio PORTA il link.
Il prodotto si vende mostrando una presentazione di qualità estrema (la prova di
professionalità che genera fiducia). Per questo il link presentazione e il link
agency sono AMMESSI già nel primo messaggio. Il prezzo da pagare è tecnico:
con un link nel corpo servono dominio caldo + volume basso, altrimenti finisci in spam.

VOLUME:
- Fino a 1000 email/giorno per mailbox, con CAP di 100/ora (drip obbligatorio anti-spam)
- Gmail personale @gmail.com regge ~500/giorno: per 1000/giorno serve Google Workspace o più mailbox in round-robin
- Nuovi account/dominio: warm-up 2-4 settimane (parti basso e sali), poi 100/ora fino a 1000/giorno
- Il warm-up resta OBBLIGATORIO: un dominio freddo + un link = spam quasi garantito

PRIMA EMAIL — COSA È AMMESSO ORA:
- AMMESSO: un link alla presentazione (PRESENTATION_URL) nel CTA
- AMMESSO: il link agency (AGENCY_URL) nella riga firma
- UN SOLO link "forte" nel corpo (la presentazione). L'agency sta in firma, non conta come CTA.
- ZERO immagini nella prima email (peso + filtri)
- ZERO tracking pixel (open rate = 0 accettabile se la deliverability migliora)
- Testo pulito, niente HTML pesante: il link in chiaro o un'unica ancora testuale

DOMINIO CALDO = PRE-REQUISITO PER IL LINK:
- SPF, DKIM, DMARC configurati sul dominio custom (NON usare un @gmail.com nudo per volumi seri)
- Reputazione costruita con 2-4 settimane di warm-up prima di inserire link
- Se la deliverability cala, togli temporaneamente il link e usalo solo dal follow-up

SEGNALI DI ACCOUNT IN PERICOLO:
- Bounce "Message blocked" / "Message rejected": STOP 48-72h, poi riprendi a volume ridotto e SENZA link
- Limite Gmail raggiunto: aspetta 24h prima di qualsiasi invio
- Mai inviare la stessa email a un indirizzo già rimbalzato
"""

# ─────────────────────────────────────────────────────────────────────────────
# TRIPLE TAP FRAMEWORK — I 3 obiettivi sequenziali di ogni email
# Fonte: NotebookLM "Outreach + Claude Code"
# ─────────────────────────────────────────────────────────────────────────────

TRIPLE_TAP_FRAMEWORK = """
TRIPLE TAP — 3 step sequenziali, ognuno dipende dal precedente
(ricalibrato sui 3 prodotti AI: Outreach Factory, Content Factory, Second Brain)

TAP 1 — APERTURA (obiettivo: far aprire l'email) → HYPE
  Strumenti: oggetto + prima riga (testo anteprima)
  L'aggancio è l'HYPE dell'automazione AI di QUEL processo, non un complimento generico.
  Regole oggetto che funzionano:
  - Hype operativo: "Ho automatizzato l'outreach al 100% — gira da solo ogni mattina"
  - Curiosità sul risultato: "300 email personalizzate al giorno, zero mani umane"
  - Suona come collega/founder, non come brochure: niente capitali, niente esclamativi
  - VIETATO: oggetti che "segnalano la vendita" o promesse vuote prima dell'apertura

TAP 2 — LETTURA (obiettivo: far leggere tutto il corpo) → UN PROBLEMA SOLO
  Strumenti: prima frase + brevità + UN problema operativo preciso
  Regole corpo:
  - Nomina UN SOLO problema operativo (l'outreach fatto a mano / i contenuti a mano /
    l'AI che dimentivca tutto). Non elencare 3 dolori: la forza è la chiarezza assoluta.
  - Niente jargon inutile, ma il vocabolario AI/automazione ora è ammesso e anzi atteso.
  - Parla del LORO processo, non di te. La soluzione arriva dopo.
  - Crea contrasto: "lo fai a mano X ore a settimana" → "questo lo fa un workflow da solo".

TAP 3 — AZIONE (obiettivo: portare alla presentazione + call) → CTA DOPPIA-MORBIDA
  Strumenti: link presentazione + invito a prenotare una call
  Regole CTA prima email:
  - UNA sola CTA logica: "guarda la presentazione (link) e se ha senso prenotiamo una call"
  - Il link presentazione (PRESENTATION_URL) è AMMESSO e consigliato qui
  - La call non è un form da compilare: è un invito a vedere il workflow DAL VIVO (demo live)
  - L'obiezione è SOLO fiducia → la demo live + la presentazione di qualità la sciolgono
  - Menziona lo sconto lancio (LAUNCH_OFFER) come motivo per muoversi ora, senza urgenza falsa
"""

# ─────────────────────────────────────────────────────────────────────────────
# LINKEDIN DM FRAMEWORK — 5 step per outreach LinkedIn
# Fonte: NotebookLM "Mastering the Art of Cold Outreach on LinkedIn"
# ─────────────────────────────────────────────────────────────────────────────

LINKEDIN_DM_FRAMEWORK = """
LINKEDIN COLD DM — Framework 5 Step (pivot: implementazioni AI)
Vantaggi vs Email: no filtri spam, arriva nel feed, più personale
Target nuovo: agenzie marketing, info business, marketing pro freelance, ecommerce.

TASSI ATTESI (benchmark reali):
- Primo messaggio: ~20% risposte
- Secondo messaggio (follow-up): ~40% risposte (il grosso è qui)
- Terzo messaggio: ~30% risposte

STEP 1 — PERSONALIZZAZIONE (Barnum Effect + Rainbow Trick)
  Non usare "personalizzazione AI generica" (riconoscibile e ignorata).
  Usa tecniche psicologiche ancorate al LORO lavoro:
  - Effetto Barnum: "Chi gestisce un'agenzia con qualche cliente fisso ha sempre lo stesso
    collo di bottiglia: l'acquisizione nuova resta indietro perché la fai a mano."
  - Rainbow Trick: "Sei uno che cura ogni dettaglio del lavoro cliente — ed è proprio per
    questo che il tuo outreach a freddo resta sempre l'ultima cosa in lista."
  Nella pratica: commenta qualcosa di REALE del loro profilo/post recente.

STEP 2 — CHIAREZZA (chi sei e perché scriverti vale il loro tempo)
  Primi 3 secondi (1.5 righe visibili): dichiara il prodotto-gancio con chiarezza assoluta.
  "Io ho costruito un sistema che automatizza l'outreach al 100% — codice tuo, sui tuoi server."
  Non devi essere famoso — devi essere CHIARO e RILEVANTE.

STEP 3 — VALORE PRIMA (mostra, non promettere)
  La moneta accettata da sconosciuti ora è la PRESENTAZIONE + la demo live.
  - Offri il link alla presentazione del workflow (PRESENTATION_URL) → è AMMESSO nel primo DM
  - Offri di mostrarlo girare dal vivo in 20 minuti
  - La qualità estrema della presentazione È il valore: dimostra professionalità = fiducia

STEP 4 — MICRO-COMMITMENT (chiedi un passo piccolo)
  CTA minima = "Ti mando il link della presentazione, dai un'occhiata quando hai 5 minuti?"
  NON: "Prenotiamo subito una call di un'ora".

STEP 5 — BASSO ATTRITO
  Zero rischio, zero fatica: guardare un link e rispondere. Nessun form, nessuna registrazione.

VOLUME SICURO LINKEDIN:
- Connection request: max 20-25/giorno (oltre = rischio ban temporaneo)
- DM: max 30-50/giorno (incluse le risposte a connection accettate)
- Sequenza: connection request → attesa accettazione → DM entro 24h
"""

# ─────────────────────────────────────────────────────────────────────────────
# FOLLOW-UP SEQUENCE — timing e struttura ottimali
# Fonte: NotebookLM "Outreach + Claude Code" + "Multi-AI Outreach and CRO"
# ─────────────────────────────────────────────────────────────────────────────

FOLLOW_UP_SEQUENCE = """
SEQUENZA FOLLOW-UP OTTIMALE (3 email totali dopo la prima)
NUOVA POLICY: link presentazione/call AMMESSI da subito, in ogni step.

EMAIL 1 (fredda):
- Struttura: Triple Tap + APSOC (hype → 1 problema → workflow 100% → fiducia/demo → CTA)
- Lunghezza: 160-260 parole
- CTA: guarda la presentazione (PRESENTATION_URL) + proposta di call breve
- Firma con riga AGENCY_URL + "Max | Digital Empire"
- Personalizzazione: min 2 elementi specifici reali sul loro processo

FOLLOW-UP 1 — Giorno 3-4 (NUDGE):
- Stesso thread Gmail (stesso oggetto, risposta al thread) → importantissimo per i filtri
- Lunghezza: 50-100 parole — breve
- Struttura: "Volevo assicurarmi che avessi visto la presentazione. [Una riga di curiosità]. [CTA]"
- Il link presentazione può restare (è già stato visto nel thread)
- Tono: genuino, non disperato

FOLLOW-UP 2 — Giorno 7 (NUOVO ANGOLO):
- Stesso thread
- Lunghezza: 90-150 parole
- Struttura: cambia prodotto-gancio o porta un mini-caso d'uso concreto + ri-linka la presentazione
- Esempio: se la #1 era Outreach Factory, qui accenni a Content Factory o Second Brain
- Ribadisci che l'unica obiezione è la fiducia → "te lo mostro dal vivo, 20 minuti"
- Tono: "Capisco se non è il momento — ti lascio comunque il link per quando vorrai vederlo"

FOLLOW-UP 3 — Giorno 14 (BREAK-UP):
- Stesso thread
- Lunghezza: 30-50 parole MAX
- Struttura: domanda binaria di chiusura. Smetto se la risposta è no.
- Es: "Ultima cosa prima di chiudere il thread: l'automazione di [processo] è qualcosa
  che vuoi guardare adesso, sì o no? In ogni caso ti lascio la presentazione qui."

DOPO IL GIORNO 14:
- Se nessuna risposta: passa al canale LinkedIn (DM separato, non thread email)
- Non inviare più di 4 email totali allo stesso indirizzo

RISPOSTA RICEVUTA:
- Rispondi entro 5-10 minuti se possibile (il tasso da risposta a call crolla dopo 1 ora)
- L'obiettivo della risposta è fissare la DEMO LIVE, non chiudere la vendita via email
"""

# ─────────────────────────────────────────────────────────────────────────────
# APSOC — Framework completo per cold email (ricalibrato sul pivot)
# ─────────────────────────────────────────────────────────────────────────────

APSOC_FULL_FRAMEWORK = """
FRAMEWORK APSOC PER COLD EMAIL — Digital Empire (PIVOT: implementazioni AI)

Il framework APSOC è la struttura obbligatoria per ogni email di outreach.
La leva NON è più "le tue conversioni" (offende chi fa marketing) ma
"ti stravolgo l'operatività" (entusiasma). Un workflow risolve UN problema al 1000%.

═══════════════════════════════════════════════════════════════
A — ATTENZIONE / HYPE (prima riga/oggetto)
═══════════════════════════════════════════════════════════════
Obiettivo: agganciare con l'HYPE dell'automazione AI di quel processo.
Regole:
- NON iniziare con "Ciao, mi chiamo..." o "Spero che tu stia bene"
- Aggancia col prodotto-gancio giusto per il target:
  1. OUTREACH FACTORY: "Ho automatizzato l'outreach al 100%: 300 email personalizzate
     al giorno via Gmail + social, gira da solo ogni mattina."
  2. CONTENT FACTORY: "Ho un'AI che mi scrive il copy e mi costruisce caroselli e script
     video in automatico — i contenuti di una settimana in un pomeriggio."
  3. SECOND BRAIN: "Ho dato all'AI una memoria permanente: conosce clienti, processi e
     brand voice e non dimentica più nulla tra una chat e l'altra."

═══════════════════════════════════════════════════════════════
P — PROBLEMA OPERATIVO (uno solo, preciso)
═══════════════════════════════════════════════════════════════
Obiettivo: far sentire il peso di UN problema operativo specifico.
Regole:
- UN SOLO problema per email. La chiarezza assoluta è la leva: niente liste di dolori.
  • Outreach Factory → l'outreach manuale (ore perse a cercare lead e scrivere a mano)
  • Content Factory → i contenuti fatti a mano (copy + grafiche + video che divorano tempo)
  • Second Brain → l'AI che dimentica tutto e va ri-istruita ogni volta
- Quantifica l'ora persa, non i "clienti persi" (non parliamo più di conversioni)
- Max 2-3 righe — è operatività, non filosofia

═══════════════════════════════════════════════════════════════
S — SOLUZIONE: IL WORKFLOW AL 100% (la "S" centrale di APSOC)
═══════════════════════════════════════════════════════════════
Obiettivo: presentare il workflow che automatizza quel processo al 100%.
Regole:
- Vendi il workflow, non un servizio a ore: "un sistema che lo fa girare da solo"
- I 4 garanti del prodotto, sempre presenti: codice sorgente TUO, €0 canoni mensili,
  setup in 7 giorni, gira sui TUOI server (autonomia totale, nessun lock-in)
- Collegalo al problema che hai appena nominato (un workflow = un problema risolto al 1000%)
- Regge ticket alti perché automatizza al 100%: €10k non sembra folle se elimina il processo

═══════════════════════════════════════════════════════════════
O — OBIEZIONE = SOLO FIDUCIA
═══════════════════════════════════════════════════════════════
Obiettivo: l'unica vera obiezione è la fiducia ("funzionerà davvero per me?").
Il prodotto è chiaro al 1000%, quindi non resta altro dubbio che la fiducia.
Regole:
- Sciogli la fiducia con la prova, non con le promesse: "te lo mostro DAL VIVO, demo live"
- La presentazione di qualità estrema È la prova di professionalità → genera fiducia
- "Non ti chiedo di fidarti sulla parola: guardi il sistema girare e decidi"
- Niente garanzie gonfiate, niente urgenza falsa

═══════════════════════════════════════════════════════════════
C — CTA (presentazione + call, con sconto lancio)
═══════════════════════════════════════════════════════════════
Obiettivo: portarli a guardare la presentazione e prenotare una call.
Regole:
- UNA sola CTA logica: guarda la presentazione (PRESENTATION_URL) → poi call breve
- Il link presentazione è AMMESSO e consigliato nel CTA della prima email
- AGENCY_URL va nella riga firma, non come seconda CTA
- Menziona LAUNCH_OFFER (sconto early-adopter) come motivo per partire ora
- Esempi approvati:
  • "Ti lascio la presentazione qui: PRESENTATION_URL — se ha senso, ci prendiamo 20 minuti."
  • "Guarda come gira (link sotto) e dimmi se vuoi vederlo dal vivo sul tuo caso."
- Firma: "Max | Digital Empire" con riga AGENCY_URL sopra
"""

# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE A — OUTREACH FACTORY (flagship)
# ─────────────────────────────────────────────────────────────────────────────

TEMPLATE_A = """
TEMPLATE A — OUTREACH FACTORY (prodotto flagship)

CONTESTO TARGET: agenzie marketing, coach/consulenti, social media manager,
copywriter e ads specialist freelance. Gente che VIVE di acquisizione clienti
ma fa l'outreach a mano: cerca lead, scrive una per una, segue i follow-up a memoria.

COSA VENDE: un workflow che automatizza l'outreach al 100% — 300+ email personalizzate
al giorno via Gmail + social, scraping e qualifica lead inclusi, gira ogni mattina da solo.
Codice sorgente tuo, €0 canoni mensili, setup in 7 giorni, sui tuoi server.

STRUTTURA EMAIL:
─────────────────
OGGETTO (hype operativo — max 9 parole):
- "Ho automatizzato l'outreach al 100% — gira da solo ogni mattina"
- "300 email personalizzate al giorno, zero mani umane"
- "Il tuo outreach può girare mentre dormi"

APERTURA (1-2 righe — HYPE):
"Io ho costruito un sistema che fa l'outreach al posto mio: ogni mattina scova i lead,
scrive 300 email personalizzate e parte da solo via Gmail e social."

PROBLEMA OPERATIVO (2-3 righe — UNO SOLO):
"Se gestisci [agenzia/clienti], l'acquisizione a freddo è il collo di bottiglia: trovare
i lead e scrivere a mano divora 8-12 ore a settimana, e appena ti fermi si ferma tutto."

SOLUZIONE / WORKFLOW (3-4 righe):
"Questo workflow lo fa girare al 100%: scraping lead, qualifica, scrittura personalizzata,
invio e follow-up. Te lo installo sui tuoi server in 7 giorni, il codice è tuo,
zero canoni mensili. Non noleggi un tool: possiedi un motore."

OBIEZIONE = FIDUCIA + DEMO (2 righe):
"L'unica domanda vera è 'funziona davvero per me?'. Non ti chiedo di crederci sulla parola:
te lo mostro dal vivo mentre gira, in 20 minuti."

CTA (2 righe + firma):
"Ti lascio la presentazione qui: PRESENTATION_URL — se ha senso, prenotiamo una call breve.
C'è uno sconto early-adopter per chi parte questo mese."
[riga firma] AGENCY_URL
Max | Digital Empire

─────────────────
LUNGHEZZA CORPO: 160-260 parole
VOCE: prima persona singolare ("io ho costruito…")
TONO: founder a founder / collega a collega, entusiasta ma concreto
"""

# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE B — CONTENT FACTORY
# ─────────────────────────────────────────────────────────────────────────────

TEMPLATE_B = """
TEMPLATE B — CONTENT FACTORY

CONTESTO TARGET: info business (info-product, coach-formatori che producono contenuti),
creator, ecommerce. Gente che ha bisogno di sfornare copy e contenuti in continuazione
e oggi li fa a mano (o paga freelance a costi che non scalano).

COSA VENDE: un workflow dove l'AI genera copy CRO-ottimizzato e costruisce in automatico
grafiche, caroselli social e script video. I contenuti di una settimana in un pomeriggio.
Codice sorgente tuo, €0 canoni mensili, setup in 7 giorni, sui tuoi server.

STRUTTURA EMAIL:
─────────────────
OGGETTO (hype operativo — max 9 parole):
- "Un'AI che mi scrive copy e mi costruisce i caroselli"
- "I contenuti di una settimana in un pomeriggio"
- "Ho automatizzato la produzione contenuti — copy, grafiche, script"

APERTURA (1-2 righe — HYPE):
"Io ho costruito un motore che genera il copy e mi tira fuori caroselli, grafiche e
script video in automatico — quello che prima era una settimana di lavoro, ora un pomeriggio."

PROBLEMA OPERATIVO (2-3 righe — UNO SOLO):
"Se vendi [corsi/prodotti], i contenuti sono il motore della crescita ma anche il buco nero
del tempo: scrivere, impaginare, montare gli script ti porta via interi pomeriggi ogni settimana."

SOLUZIONE / WORKFLOW (3-4 righe):
"Questo workflow produce tutto in pipeline: copy ottimizzato per convertire, caroselli e
grafiche pronte, script video. Te lo installo in 7 giorni, gira sui tuoi server, il codice
è tuo, zero canoni mensili. Non un tool a abbonamento: un motore di contenuti che possiedi."

OBIEZIONE = FIDUCIA + DEMO (2 righe):
"L'unico dubbio sensato è la qualità dell'output. Per questo non te lo racconto:
te lo mostro dal vivo mentre genera un carosello sul tuo brand, in 20 minuti."

CTA (2 righe + firma):
"Qui la presentazione: PRESENTATION_URL — se ti convince, ci prendiamo 20 minuti per una demo.
Per chi parte questo mese c'è uno sconto early-adopter."
[riga firma] AGENCY_URL
Max | Digital Empire

─────────────────
LUNGHEZZA CORPO: 160-260 parole
VOCE: prima persona singolare
TONO: da creator/operatore a creator/operatore, concreto sull'output
"""

# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE C — SECOND BRAIN (upsell trasversale)
# ─────────────────────────────────────────────────────────────────────────────

TEMPLATE_C = """
TEMPLATE C — SECOND BRAIN (Context Engineering)

CONTESTO TARGET: organizzazioni strutturate / con team / che usano molto l'AI —
agenzie con più persone, info business con processi, aziende che hanno già adottato
l'AI ma la trovano "smemorata". È l'upsell trasversale, spesso dopo Outreach o Content.

COSA VENDE: una knowledge base interconnessa a grafo che dà memoria e contesto permanente
all'LLM (clienti, processi, brand voice, decisioni). È "Context Engineering" (Andrej Karpathy):
l'AI smette di ripartire da zero e lavora con il contesto di tutta l'azienda.
Codice sorgente tuo, €0 canoni mensili, setup in 7 giorni, sui tuoi server.

STRUTTURA EMAIL:
─────────────────
OGGETTO (hype operativo — max 9 parole):
- "Ho dato all'AI una memoria permanente di tutta l'azienda"
- "La tua AI dimentica tutto: ho risolto con un Second Brain"
- "Context Engineering: l'AI che conosce davvero i tuoi processi"

APERTURA (1-2 righe — HYPE):
"Io ho costruito un Second Brain a grafo che dà all'AI una memoria permanente:
conosce clienti, processi, brand voice e decisioni, e non riparte più da zero ogni volta."

PROBLEMA OPERATIVO (2-3 righe — UNO SOLO):
"Se il team usa l'AI ogni giorno, il problema vero è uno: dimentica tutto. Ogni chat
riparte da zero, devi ri-spiegare contesto e brand voice, e il risultato resta generico."

SOLUZIONE / WORKFLOW (3-4 righe):
"Questo è Context Engineering (lo chiama così Andrej Karpathy): una knowledge base a grafo
che collega tutto e la dai in pasto all'LLM. Te la installo in 7 giorni, gira sui tuoi server,
il codice è tuo, zero canoni. Da quel momento l'AI lavora con la memoria di tutta l'azienda."

OBIEZIONE = FIDUCIA + DEMO (2 righe):
"L'unico dubbio è se cambia davvero il risultato. Per questo te lo mostro dal vivo:
faccio due domande all'AI prima e dopo il Second Brain, e vedi la differenza in 20 minuti."

CTA (2 righe + firma):
"Ti lascio la presentazione: PRESENTATION_URL — se ti interessa, organizziamo una demo live.
Per i primi che partono questo mese c'è uno sconto early-adopter."
[riga firma] AGENCY_URL
Max | Digital Empire

─────────────────
LUNGHEZZA CORPO: 160-260 parole
VOCE: prima persona singolare
TONO: tecnico ma accessibile, peer-to-peer con chi gestisce un team/azienda
"""

# ─────────────────────────────────────────────────────────────────────────────
# CPB — Claim → Proof → Benefit (esempi sui 3 prodotti)
# ─────────────────────────────────────────────────────────────────────────────

CPB_FRAMEWORK = """
CPB FRAMEWORK — Claim, Proof, Benefit

Usato per costruire ogni affermazione importante nell'email.
Ogni claim deve superare il test "E quindi?" (So What? test).

STRUTTURA:
  CLAIM   → cosa stai affermando
  PROOF   → perché dovrebbero crederti
  BENEFIT → cosa significa concretamente per loro

ESEMPIO — OUTREACH FACTORY (Template A):
  CLAIM:   "Il tuo outreach può girare al 100% da solo"
  PROOF:   "Un workflow che ogni mattina scova lead, scrive 300 email personalizzate e invia"
  BENEFIT: "Recuperi 8-12 ore a settimana e l'acquisizione non si ferma mai, anche quando sei in delivery"

ESEMPIO — CONTENT FACTORY (Template B):
  CLAIM:   "Puoi produrre i contenuti di una settimana in un pomeriggio"
  PROOF:   "Una pipeline AI che genera copy, costruisce caroselli/grafiche e script video"
  BENEFIT: "Smetti di scegliere tra creare e vendere: pubblichi costante senza bruciare i pomeriggi"

ESEMPIO — SECOND BRAIN (Template C):
  CLAIM:   "La tua AI può avere memoria permanente di tutta l'azienda"
  PROOF:   "Una knowledge base a grafo (Context Engineering) collegata all'LLM"
  BENEFIT: "Niente più ri-spiegare contesto: ogni risposta arriva già allineata a clienti, processi e brand voice"

REGOLA: Non usare mai solo il CLAIM senza PROOF o senza BENEFIT.
Il CLAIM da solo suona come hype. CPB completo suona come dimostrazione.

TEST DI VALIDITÀ:
1. "Perché dovrebbero credermi?" → aggiungi PROOF (e ricorda: la demo live è la prova finale)
2. "E quindi cosa cambia per loro?" → aggiungi BENEFIT (in ore/operatività, non in conversioni)
"""

# ─────────────────────────────────────────────────────────────────────────────
# DIRECT RESPONSE PRINCIPLES — principi psicologici di persuasione
# ─────────────────────────────────────────────────────────────────────────────

DR_PRINCIPLES = """
DIRECT RESPONSE PRINCIPLES — Psicologia della persuasione (pivot: implementazioni AI)

1. HYPE-FIRST (cavalca il momento)
   L'automazione AI è il prodotto più in hype del momento: l'aggancio è l'entusiasmo
   per ciò che il workflow fa girare da solo, non un problema di conversioni.
   SBAGLIATO: "La vostra pagina converte poco"
   GIUSTO:    "Ho automatizzato l'outreach al 100% — 300 email al giorno, da solo"

2. UN PROBLEMA AL 1000% (chiarezza assoluta)
   Un workflow risolve UN problema operativo preciso, al 1000%. La chiarezza è la leva.
   SBAGLIATO: elencare 4 dolori e 4 servizi
   GIUSTO:    "Risolvo una cosa sola: l'outreach manuale. Lo automatizzo al 100%."

3. OPERATIVITÀ, NON CONVERSIONI (non offendere il marketer)
   "Ti miglioro le conversioni" offende chi fa marketing di mestiere.
   "Ti stravolgo l'operatività" entusiasma. Parla di ore liberate e processi automatici.
   SBAGLIATO: "Aumento il tuo conversion rate"
   GIUSTO:    "Ti tolgo di mano il processo: lo fa il workflow, tu recuperi il tempo"

4. SPECIFICITÀ (la specificità crea credibilità)
   Numeri specifici e concreti sull'operatività.
   SBAGLIATO: "Risparmi tantissimo tempo"
   GIUSTO:    "8-12 ore a settimana", "300 email/giorno", "setup in 7 giorni", "€0 canoni"

5. OBIEZIONE = SOLO FIDUCIA → DEMO LIVE
   Il prodotto è chiaro: l'unico dubbio è "funziona per me?". Si scioglie mostrandolo.
   SBAGLIATO: promettere risultati garantiti
   GIUSTO:    "Te lo mostro dal vivo mentre gira, 20 minuti, decidi tu"

6. POSSESSO, NON NOLEGGIO (i 4 garanti)
   Codice sorgente tuo + €0 canoni + 7 giorni + sui tuoi server.
   È ciò che regge il ticket alto: non affitti un tool, possiedi un motore.

7. ONE CTA (una sola azione richiesta)
   Una sola CTA: guarda la presentazione (PRESENTATION_URL) e poi, se ha senso, una call.
   AGENCY_URL sta in firma, non è una seconda CTA.
"""

# ─────────────────────────────────────────────────────────────────────────────
# FRASI VIETATE — mai usare in nessuna email
# (RIMOSSI i divieti su "AI"/"Intelligenza Artificiale" e quelli landing-centrici)
# ─────────────────────────────────────────────────────────────────────────────

PROHIBITED_PHRASES = [
    # Aperture robotiche (restano vietate)
    "Spero che tu stia bene",
    "Spero che questa email ti trovi bene",
    "Mi permetto di contattarti",
    "Mi chiamo Max e lavoro",
    "Sono il responsabile di",
    "Vi scrivo in merito a",
    "Come va?",
    "Buongiorno, mi chiamo",

    # Linguaggio robotico/da brochure (restano vietati — ma "AI" ora è AMMESSO)
    "Nel contesto attuale",
    "In questa email voglio",
    "È un piacere contattarvi",
    "Sono lieto di",
    "Ho il piacere di presentarvi",
    "In qualità di",
    "Siamo specializzati in",
    "La nostra soluzione innovativa",
    "Offriamo servizi di altissima qualità",
    "Siamo leader nel settore",

    # Promesse esagerate / urgenza falsa (restano vietate)
    "Garantiamo risultati",
    "Risultati garantiti",
    "Aumentiamo le conversioni del 300%",
    "Non potete permettervi di perdere questa opportunità",
    "Offerta limitata",
    "Non aspettare oltre",
    "Ultima possibilità",

    # Superlativi vuoti (restano vietati)
    "eccellente",
    "straordinario",
    "rivoluzionario",

    # Genericità (restano vietate)
    "La vostra azienda",  # usa sempre il nome reale
    "Il vostro business",  # idem
    "Come molte aziende del settore",
    "In un mercato sempre più competitivo",
    "Nell'era digitale",
    "La trasformazione digitale",
]

# ─────────────────────────────────────────────────────────────────────────────
# APERTURE APPROVATE — opener su automazione/hype/operatività (target nuovi)
# ─────────────────────────────────────────────────────────────────────────────

APPROVED_OPENERS = [
    # Outreach Factory (agenzie, coach, SMM, freelance)
    "Io ho costruito un sistema che fa l'outreach al 100% da solo: 300 email personalizzate al giorno.",
    "Ogni mattina un workflow scova i miei lead, scrive le email una per una e parte — senza che io tocchi nulla.",
    "Se vivi di acquisizione clienti, immagina l'outreach a freddo che gira mentre sei in delivery.",

    # Content Factory (info-product, creator, ecommerce)
    "Io ho un motore AI che mi genera il copy e mi costruisce caroselli e script video in automatico.",
    "I contenuti di una settimana, prodotti in un pomeriggio: copy ottimizzato, grafiche, script.",
    "Se i contenuti sono il tuo motore di crescita, ho automatizzato la parte che ti ruba i pomeriggi.",

    # Second Brain (org strutturate / chi usa molto l'AI)
    "Io ho dato all'AI una memoria permanente: conosce clienti, processi e brand voice e non riparte più da zero.",
    "Se il team usa l'AI ogni giorno, il problema è che dimentica tutto: l'ho risolto con un Second Brain a grafo.",
    "Context Engineering: ho collegato tutta la conoscenza dell'azienda all'LLM, così smette di essere generico.",
]

# ─────────────────────────────────────────────────────────────────────────────
# LINKEDIN AUTOMATION — PROFESSIONAL WORKFLOWS
# Fonte: NotebookLM "Outreach + Claude Code" + "Mastering LinkedIn" + "Multi-AI"
# AGGIORNATO — messaggistica su implementazioni AI, link presentazione ammesso nel primo DM
# ─────────────────────────────────────────────────────────────────────────────

LINKEDIN_AUTOMATION_PROFESSIONALS = """
WORKFLOW PROFESSIONISTI REALI — LinkedIn Automation con Claude Code
(pivot: vendi i 3 workflow AI — Outreach Factory, Content Factory, Second Brain)

═══════════════════════════════════════════════════════
OLEG MELNIKOV — 35% response rate
═══════════════════════════════════════════════════════
APPROCCIO: Claude Cowork (app desktop) + Chrome Extension controlla il browser
come un umano. NON usa Selenium/Playwright direttamente.

WORKFLOW ESATTO:
1. Lead sourcing: LinkedIn Sales Navigator → liste filtrate per nicchia
   (agenzie marketing, info business, marketing pro freelance, ecommerce)
2. Connection: Claude Cowork invia richieste SENZA nota
   → "Senza nota = meno salesy = acceptance rate +30-40%"
3. Data export: Apify (con cookie LinkedIn) scarica CSV nuove connessioni
4. Lead scoring: Claude Code in VS Code assegna score 1-10 per ogni lead
5. Valore = la PRESENTAZIONE: nel primo DM condividi il link presentazione del workflow
   (PRESENTATION_URL) — è AMMESSO, ed è la prova di professionalità che genera fiducia
6. Primo messaggio: "Io ho automatizzato l'outreach al 100% — ti lascio la presentazione,
   dai un'occhiata: PRESENTATION_URL"

INSIGHT CHIAVE: ora il "lead magnet" è la presentazione di qualità estrema + la demo live.
Non un banner gratis: la prova che il workflow esiste e funziona.

═══════════════════════════════════════════════════════
BEN AI — Workflow basato su Claude Code Skills
═══════════════════════════════════════════════════════
APPROCCIO: Skills personalizzate (.md files) che trasformano Claude Code
in un sales agent con comandi slash.

WORKFLOW ESATTO:
1. Slash command /LinkedIn post engagers → attiva skill
2. Skill usa Apify per estrarre chi ha commentato/liked post di founder/marketer del settore
3. Claude Code arricchisce ogni lead: bio, sito, descrizione attività
4. Multi-channel: Uniflow integra LinkedIn + WhatsApp + X in un unico flusso

INSIGHT CHIAVE: targettare chi interagisce con post su AI/automazione = warm leads
(già caldi sul tema, già in hype).

═══════════════════════════════════════════════════════
ZUBAIR TRABZADA — $80k in revenue via 14 skills
═══════════════════════════════════════════════════════
APPROCCIO: 14 slash commands in VS Code coprono l'intero ciclo di vendita.

WORKFLOW ESATTO:
1. /sales-prospect → lancia 5 sub-agenti in parallelo:
   - Agente 1: ricerca azienda
   - Agente 2: trova decision maker
   - Agente 3: analizza il loro stack/processi (quale dei 3 workflow serve di più)
   - Agente 4: valuta opportunità
   - Agente 5: crea strategia outreach
2. Output: sequenza di 5 messaggi con LinkedIn touchpoints intercalati:
   - Giorno 1: Messaggio LinkedIn + link presentazione
   - Giorno 3: Email con angolo operativo (un problema, un workflow)
   - Giorno 7: Nuovo angolo / secondo prodotto-gancio + ri-link presentazione
   - Giorno 10: LinkedIn follow-up con invito a demo live
   - Giorno 14: Email finale binaria (break-up)

TOOL STACK COMPLETO (citato nei notebook):
- IDE: VS Code (Claude Code gira qui)
- Scraping LinkedIn: Apify (attori per profili/post)
- Browser control: Claude Cowork (invece di Selenium) — agisce come utente umano
- Data enrichment: Crunchbase, Apollo
- Database: Supabase (lead tracking)
- Orchestration: Make.com o n8n
- Multi-channel: Uniflow (LinkedIn + WhatsApp + X)

SISTEMA MULTI-AI (dal notebook Multi-AI Outreach):
- Fase 1 PARSE: ChatGPT Custom GPT → normalizza lead CSV in JSON
- Fase 2 RESEARCH: Perplexity (dati LinkedIn pubblici) + Gemini (stack/contenuti del lead)
- Fase 3 SYNTHESIZE: NotebookLM → Research Brief senza allucinazioni
- Fase 4 GENERATE: Claude → scrive il messaggio basato sul brief (hype → 1 problema → workflow → demo)
- Fase 5 QA: verifica tono umano, max 1 CTA, min 2 elementi personalizzati, link presentazione presente

REGOLE QA MESSAGGI:
- Lunghezza: 60-120 parole primo DM, 40-90 follow-up
- Human-sounding test: ZERO "Spero che questo messaggio ti trovi bene"
- Min 2 elementi di personalizzazione reale obbligatori
- 1 sola CTA per messaggio (guarda la presentazione)
- Link presentazione (PRESENTATION_URL) ammesso già nel primo DM
"""

LINKEDIN_AUTOMATION_RULES = """
REGOLE OPERATIVE LINKEDIN AUTOMATION — Digital Empire (pivot: implementazioni AI)

ACCOUNT SAFETY (account nuovo):
- Settimana 1-2: solo connessioni manuali (5-10/giorno)
- Settimana 3-4: aumenta a 15-20/giorno
- Mese 2+: puoi usare automazione a 20-25/giorno
- MAI superare 25 connection requests/giorno con account < 3 mesi

SEGNALI DI PERICOLO:
- LinkedIn mostra "Sembra che tu stia usando questa funzione troppo velocemente"
- Restrictions su account (no inviti per X giorni)
- FIX: stop 48h, poi riprendi a volume dimezzato

DETECTION EVASION (Playwright):
- SEMPRE headless=False (browser visibile, non headless)
- Delay random 8-20 secondi tra azioni (non delay fisso)
- User agent realistico (Chrome + Windows)
- Scorri la pagina come un umano prima di cliccare
- Non aprire troppi tab in parallelo

CONTENUTO MESSAGGI:
- Link presentazione (PRESENTATION_URL) AMMESSO già nel primo messaggio (è la nuova policy)
- Un solo link forte (la presentazione); AGENCY_URL eventualmente in chiusura, non come seconda CTA
- Messaggio max 90 parole
- Voce in prima persona singolare ("io ho costruito…")
- Nome del destinatario personalizzato SEMPRE
- Almeno 1 elemento specifico sul loro processo/settore/ruolo
- Aggancio = hype dell'automazione; corpo = UN problema operativo; chiusura = guarda la presentazione
"""
