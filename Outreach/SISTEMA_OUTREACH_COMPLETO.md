# Digital Empire — Sistema Outreach Completo

**Versione:** `run_parallel.py v5.0 (pivot Implementazioni AI) | Instagram v3.0 (sub-agents)`
**Comando di avvio:** `python run_parallel.py`
**Directory:** `c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach`

---

## Posizionamento — Cosa Vende il Sistema (Pivot 2026-06-04)

> **Il sistema NON vende più "landing page / CRO".** Vende **3 prodotti = implementazioni AI**: workflow installati sui server del cliente, **codice sorgente incluso**, **€0 canoni mensili**, **setup 7 giorni**, **automazione 100%**.

### I 3 prodotti
1. **Outreach Factory** — automatizza l'outreach al 100% (300+ email/giorno via Gmail + canali social).
2. **Content Factory** — l'AI genera copy CRO + costruisce grafiche/caroselli social e script video in automatico.
3. **Second Brain** — knowledge base a grafo che dà memoria/contesto permanente all'LLM (Context Engineering, scuola Karpathy).

### Tesi del pivot
- Un workflow risolve **UN problema al 1000%** → unica obiezione residua = la **fiducia**.
- Prodotto **in hype** (AI applicata), **ticket alto** (€10k accettabile perché automazione 100%).
- Collega i due business più potenti: **Agency** e **Info Business**.
- La leva NON è più "le tue conversioni" (offende chi fa marketing) ma **"ti stravolgo l'operatività"**.

### Nuovo target
- **IN**: Agency, Info Business (info-product, coach, formatori), Marketing pros (SMM, copywriter, freelance ads), ecommerce.
- **OUT**: professionisti locali (dentisti, avvocati, ristoranti, artigiani, salute) — rimossi da scraper SETTORI, hashtag Instagram, ricerche LinkedIn, keyword bio.
- **Chiavi settore canoniche**: `agenzia`, `info_product`, `coach`, `smm_freelance`, `ecommerce`, `consulente`, `default`.

### Link nel primo messaggio (Email + LinkedIn + Instagram)
- CTA con link presentazione: `PRESENTATION_URL = https://presentazione-empire.vercel.app/`.
- Firma con link agenzia: `AGENCY_URL = https://agency-empire-landing.vercel.app`.
- **Rimosso il vecchio HARD-BLOCK** che scartava le email con link (in `bibbia_team.py`) e la regola "link = HARD FAIL" nella Bibbia.
- Deliverability mitigata con **volume basso (25-30 email/giorno)**.

Riferimento concettuale completo: pagina wiki `Concept_Pivot_Implementazioni_AI`.

---

## Mappa Completa degli Agenti

### INSTAGRAM — `Instagram Automation/agents/`

| Agente | File | Ruolo | Stato |
|---|---|---|---|
| Hashtag Scout | `agents/hashtag_scout.py` | Scansiona 10 hashtag × 25 profili = 250 candidati grezzi. Scroll aggressivo (10 round), API intercept. | ✅ Attivo |
| Profile Qualifier | `agents/profile_qualifier.py` | Visita profili in bulk, analizza bio con 60+ keyword (incluse forme femminili), verifica bottone DM. Score 1-10. Stop a 30 qualificati. | ✅ Attivo |
| Similar Accounts Scout | `agents/similar_accounts_scout.py` | Dai top lead qualificati, estrae "Profili simili" suggeriti algoritmicamente da Instagram. Lead ad altissima qualità. | ✅ Attivo |
| DM Orchestrator | `run_today.py` | Coordina FASE 0 (sub-agents) → FASE 1 (backup) → FASE 2 (DM) → FASE 3 (F1) → FASE 4 (F2). | ✅ Attivo |
| Personalizer | `personalize.py` | Genera DM, F1, F2 con framework Barnum/Rainbow. Max 50 parole per DM. | ✅ Attivo |
| Reply Checker | `check_replies.py` | Legge DM inbox, classifica risposte, genera suggerimenti. Modalità `--autoinvia`. | ✅ Attivo |

---

### EMAIL — `Outreach Workflow/agents/`

| Agente | File | Ruolo | Stato |
|---|---|---|---|
| Orchestrator | `orchestrator.py` | Pipeline principale email: coordina tutti i sotto-agenti in sequenza. | ✅ Attivo |
| Scraper | `scraper.py` | Scraping lead da Apify / Google / Outscraper. | ✅ Attivo |
| Qualifier | `qualifier.py` | Qualifica i lead prima di generare email (filtro nicchia, email valida). | ✅ Attivo |
| Copy Knowledge | `copy_knowledge.py` | Estrae termine tecnico anti-AI-slop specifico per nicchia. | ✅ Attivo |
| Strategist | `strategist.py` | Decide framework email (Barnum/Rainbow), angolo di attacco, personalizzazione per nicchia + città. | ✅ Attivo |
| Writer | `writer.py` | Genera email completa (5 Pilastri: Pain Hook, Analisi, Solution, Social Proof, Action). | ✅ Attivo |
| Humanizer | `humanizer.py` | QA automatico (punteggio 1-10 su 5 criteri). Retry se media < 7.0. | ✅ Attivo |
| Sender | `sender.py` | Gmail SMTP sender con rate limiting. | ✅ Attivo |
| Followup Writer | `followup_writer.py` | Genera F1 (giorno 3) e F2 (giorno 7) con angolo alternativo alla prima email. | ✅ Attivo |
| Reply Monitor | `reply_monitor.py` | IMAP scan Gmail, rileva risposte dai lead, estrae testo pulito. | ✅ Attivo |
| Conversation Manager | `conversation_manager.py` | Classifica risposta (POSITIVO/OBIEZIONE/DOMANDA/NON_INTERESSATO), genera risposta verso call. | ✅ Attivo |
| Research | `research.py` | Ricerca info aggiuntive sul lead (sito, settore, contesto). | ✅ Attivo |
| Lead Analyzer | `lead_analyzer.py` | Analizza profilo del lead per personalizzazione avanzata. | ✅ Attivo |
| Insight | `insight.py` | Genera insight personalizzati dal sito del lead. | ✅ Attivo |
| CRO Audit | `cro_audit.py` | Audit CRO della landing page / sito del lead (per personalizzare il pitch). | ✅ Attivo |
| Extractor | `extractor.py` | Estrae dati strutturati dalle pagine web dei lead. | ✅ Attivo |
| AI Client | `ai_client.py` | Wrapper unificato OpenRouter + Groq con retry e fallback. | ✅ Attivo |
| Apify Leads Finder | `apify_leads_finder.py` | Trova lead qualificati via Apify (code_crafter/leads-finder). | ✅ Attivo |
| Apify Scraper | `apify_scraper.py` | Scraper Apify per hashtag / search. | ✅ Attivo |
| Google Scraper | `google_scraper.py` | Scraper Google Maps/Search per lead locali. | ✅ Attivo |
| Outscraper Scraper | `outscraper_scraper.py` | Outscraper.com per lead business italiani. | ✅ Attivo |
| Competitor | `competitor.py` | Analisi competitor del lead per angolo di differenziazione. | ✅ Attivo |

---

### LINKEDIN — `LinkedIn Automation/`

| Script | File | Ruolo | Stato |
|---|---|---|---|
| Comment Warmer | `comment_posts.py` | 100 commenti AI su post target LinkedIn (warming visibilità). | ✅ Attivo |
| Connection Requester | `run_today.py` | 50 connection requests giornaliere con nota Barnum/Rainbow (300 char). | ✅ Attivo |
| Personalizer | `personalize.py` | Genera note connessione, DM post-accettazione, follow-up F1/F2. | ✅ Attivo |
| DM Checker | `check_replies.py` | Legge DM inbox LinkedIn, classifica, genera suggerimenti risposta. Modalità `--autoinvia`. | ✅ Attivo |
| Direct DM | `direct_dm.py` | DM diretti a Open Profile (utenti premium o 1° grado). | ✅ Attivo |
| Session Manager | `refresh_session.py` | Login + salvataggio sessione Playwright. | ✅ Attivo |

---

**Totale agenti/script operativi:** 6 Instagram + 22 Email + 6 LinkedIn = **34 componenti attivi**

---

## Sequenza giornaliera (3 comandi in ordine)

**Passo 1 — Attiva la sessione LinkedIn** (apre browser, fai login manuale, poi chiudi)
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach"
python "LinkedIn Automation\refresh_session.py" 
& 
python "Instagram Automation\refresh_session.py"

```
> Le virgolette intorno al percorso sono OBBLIGATORIE — il nome della cartella ha uno spazio.

**Passo 1b — Attiva la sessione Instagram** (solo se non ancora attiva)
```
python "Instagram Automation\refresh_session.py"
```
> Da fare una volta sola (o quando la sessione scade). Se il file `instagram_session.json` esiste già, salta questo step.

**Passo 2 — Lancia il flusso principale** (nella stessa cmd, stessa cartella)
```
python run_parallel.py
```

---

## Pre-requisiti

| Requisito | Verifica |
|---|---|
| Sessione LinkedIn attiva | `LinkedIn Automation/linkedin_session.json` deve esistere |
| Variabili d'ambiente email | `Outreach Workflow/.env` con `OPENROUTER_API_KEY`, `GMAIL_USER`, `GMAIL_APP_PASSWORD` |
| CSV lead freschi | `Outreach Workflow/leads_freschi_validated.csv` (target: 100 lead) |
| DB leads email | `Outreach Workflow/output/leads.db` (si crea automaticamente al primo run) |

---

## Struttura del Flusso — Tre Catene Indipendenti

Le tre catene partono insieme e non si aspettano a vicenda.

```
python run_parallel.py
│
├── CATENA LINKEDIN (veloce, ~20-30 min totali)
│   ├── [COMMENTI]    → 100 commenti warming LinkedIn    (~20 min)
│   ├── [CONNESSIONI] → 50 connection requests           (~10 min)
│   └── appena COMMENTI + CONNESSIONI finiscono:
│       ├── [FOLLOWUP]    → F1 (giorno 3) + F2 (giorno 7) per email senza risposta
│       ├── [REPLY-MGR]   → scansiona Gmail, risponde ai lead via AI
│       └── [LI-REPLIES]  → legge DM LinkedIn non letti, stampa suggerimenti
│           (FOLLOWUP + REPLY-MGR + LI-REPLIES partono in parallelo tra loro)
│
├── CATENA EMAIL (lenta, ~35-45 min totali)
│   ├── [EMAIL-GEN]   → genera 52 email cold con AI      (~30-40 min)
│   └── appena EMAIL-GEN finisce:
│       └── [EMAIL-INVIA] → invia le email generate      (~3-5 min)
│
└── CATENA INSTAGRAM (parte 5s dopo, ~35-45 min totali)
    ├── [IG-DM]       → FASE 0: 3 sub-agents scout+qualify+similar (~15 min)
    │                   FASE 1-4: DM + follow-up garantiti 15/giorno (~20 min)
    └── appena IG-DM finisce:
        └── [IG-REPLIES] → legge DM non letti, genera/invia risposte (~5 min)
```

**Vantaggio:** i controlli follow-up e risposte non aspettano le 30-40 minuti di EMAIL-GEN — partono subito dopo LinkedIn (~10-15 min), quando ci sono già risultati freschi da gestire. Instagram gira in parallelo su un canale completamente separato.

---

## CATENA LINKEDIN

I tre processi LinkedIn partono con 3 secondi di stagger tra loro.

---

### [COMMENTI] — LinkedIn Comment Warming

**Script:** `LinkedIn Automation/comment_posts.py`
**Log:** `LinkedIn Automation/comments_log.txt`

Apre LinkedIn via Playwright con sessione salvata e lascia 100 commenti su post rilevanti nel feed. Scopo: aumentare la visibilità organica del profilo e preparare il terreno per le connection requests. I commenti sono generati via AI per sembrare autentici e contestuali al post.

---

### [CONNESSIONI] — LinkedIn Connection Requests

**Script:** `LinkedIn Automation/run_today.py`
**Log:** `LinkedIn Automation/run_today_log.txt`
**Lead DB:** `LinkedIn Automation/leads.json`

Invia fino a 50 connection requests giornaliere con nota personalizzata. La nota usa l'**Effetto Barnum** o **Rainbow** (alternati) per massimizzare i tassi di accettazione:

- **Barnum**: affermazione universale con cui chiunque nel settore si identifica
- **Rainbow**: combinazione paradossale di tratto positivo + opposto, il 99% si riconosce in entrambi

Dopo l'invio delle connessioni (`run_today.py`) gestisce anche i follow-up LinkedIn (flusso interno):
- **LinkedIn F1** (giorno 3-4 dall'accettazione): messaggio diretto ai nuovi connessi che non hanno risposto
- **LinkedIn F2** (giorno 7-8): messaggio di chiusura/break-up

---

## CATENA EMAIL

### [EMAIL-GEN] — Generazione Email Cold

**Script:** `Outreach Workflow/run.py --csv leads_freschi_validated.csv --mode genera --target 100`
**Output:** `Outreach Workflow/output/leads.db` (tabella `leads_contattati`)

Questo è il processo più lungo (~75-90 minuti per 100 lead). La pipeline interna ha **7 sotto-fasi** — aggiornata v5.0 con Team DEEP-INTEL:

```
CSV leads → [1. Qualifica] → [2. DEEP-INTEL] → [3. Copy Knowledge] → [4. Strategist] → [5. Writer] → [6. Humanizer] → [7. Salva DB]
```

#### 7 fasi interne (v5.0)

**1. Qualifier** (~0.3s/lead)
Scoring 0-100 e selezione template A/B/C. Lead con score < 40 scartati. Lead con score ≥ 60 + sito web → eleggibili per analisi DEEP-INTEL.

---

**2. TEAM DEEP-INTEL** ← **NUOVO v5.0** (~15-25s/lead hot/warm)

Il cuore dell'upgrade: il sistema **visita davvero il sito del lead** e raccoglie dati reali prima di scrivere. Invece di Barnum generico, l'email inizia: *"Ho aperto il tuo sito stamattina — non c'è un bottone per prenotare, solo un numero nel footer."*

Architettura: 3 sub-agent paralleli + 1 synthesis agent:

```
Lead (score ≥ 60 + sito)
│
├─ Sub-Agent A: ResearchAgent    ← research.py
│  Visita sito (no AI, BeautifulSoup): load time, H1, CTA, form, telefono,
│  social proof, mobile viewport, sistema prenotazione
│
├─ Sub-Agent B: CROAuditAgent    ← cro_audit.py  (dipende da Research)
│  AI analizza i dati → 3 problemi CRO specifici con evidenza reale + CRO score 0-10
│
└─ Sub-Agent C: CompetitorAgent  ← competitor.py  (parallelo a Research)
   Lookup nel DB leads → 2-3 competitor stessa nicchia/città → intelligence competitiva
   
   ▼ (dopo i 3)
   
InsightAgent                     ← insight.py
Sintetizza tutto → insight_brief:
  • problema_principale (con dato reale verificato)
  • problema_2 / problema_3
  • apertura_email: "Ho aperto il tuo sito…"
  • insight_score 1-10
```

**Lead senza sito o score < 60:** fast-pass diretto al Strategist, nessun rallentamento.

**File:** `agents/research.py` · `agents/cro_audit.py` · `agents/competitor.py` · `agents/insight.py` · `agents/lead_analyzer.py`

---

**3. Copy Knowledge** (~2s/lead)
Estrae il termine tecnico di nicchia specifico per settore (anti-AI-slop): un termine che solo un esperto del settore userebbe, che segnala conoscenza reale.

**4. Strategist** (~8s/lead)
Decide quale framework usare per questo lead specifico:
- Se **insight_brief disponibile** → usa dati reali dal sito come angolo primario (citazione diretta)
- Se **no insight_brief** (lead fast-pass) → Framework **Barnum** o **Rainbow**
- Angolo di attacco (pain, opportunità, social proof)
- Personalizzazione per settore + città

**5. Writer** (~5s/lead)
Genera l'email completa seguendo il framework **APSOC ricalibrato sul pivot** (vendita di implementazioni AI). Il prodotto-gancio (`prodotto_guida`) deciso dal qualifier determina l'angolo. Se insight_brief disponibile, il blocco [A] ATTENZIONE può citare un dato reale del lead a supporto dell'hype automazione.

**APSOC ricalibrato (offerta = 3 implementazioni AI):**

| Blocco | Contenuto |
|---|---|
| [A] ATTENZIONE | Hype dell'automazione AI (non più Barnum generico di settore) |
| [P] PROBLEMA | UN solo problema operativo concreto del prospect |
| [S] SOLUZIONE | Il workflow che lo risolve al 100% — codice tuo, €0 canoni, 7 giorni |
| [O] OBIEZIONE | Resta UNA sola: la fiducia → demo live + presentazione di qualità estrema |
| [C] CTA | Guarda la presentazione (link `PRESENTATION_URL`) + prenota call, con sconto lancio |

**Match prodotto ↔ target** (template del qualifier, campo `prodotto_guida`):

| Template | Prodotto guida | Target tipico |
|---|---|---|
| A | Outreach Factory | agency, freelancer marketing (acquisizione clienti) |
| B | Content Factory | info-business, coach, SMM, copywriter (produzione contenuti) |
| C | Second Brain | consulenti, team (memoria/contesto operativo) |

**Regole assolute di stile (invariate):**
- Prima persona singolare: solo "io", "ho", "mi", "mio" — MAI "noi"
- Zero trattini nel corpo (solo punti fermi e virgole)
- Paragrafi separati da riga vuota
- CTA con link presentazione (`PRESENTATION_URL`) + link agenzia in firma (`AGENCY_URL`) — il vecchio hard-block "link = FAIL" è stato rimosso
- 230-340 parole nel corpo

**6. Humanizer** (~1s/lead)
3 sub-checker in parallelo (HumannessChecker, DirectResponseReviewer, BrandValidator). Score medio < 7.0 → retry automatico.

**7. Salva DB**
Salva in blocco nella tabella `leads_contattati` con stato `generata`.

**Nota:** con l'analisi DEEP-INTEL attiva su 100 lead, i tempi salgono a ~80-90 minuti totali. Il DB si popola alla fine come prima.

---

### [EMAIL-INVIA] — Invio Email

**Script:** `Outreach Workflow/run.py --mode invia`

Parte automaticamente appena EMAIL-GEN completa con successo (exit code 0). Se EMAIL-GEN fallisce, viene saltato.

Legge tutte le email con stato `generata` dal DB e le invia via Gmail SMTP. Aggiorna lo stato a `inviata` per ogni email consegnata. Include rate limiting per rispettare i limiti Gmail (max ~500/giorno, tipicamente 50-100/sessione).

Ogni email inviata ha:
- Oggetto personalizzato (generato dal Writer)
- Corpo APSOC ricalibrato sul prodotto-gancio, CTA con link presentazione + link agenzia in firma
- Firma "Max" (senza cognome, tono da consulente personale non da agenzia)

**Deliverability:** con i link reintrodotti nel primo messaggio, il volume è tenuto basso (**25-30 email/giorno**) per mitigare il rischio spam. Non aumentare senza warming del dominio.

---

## CATENA LINKEDIN — Seconda parte (checks)

I tre processi partono in parallelo (2 secondi di stagger) appena COMMENTI + CONNESSIONI finiscono.

---

### [FOLLOWUP] — Email Follow-up F1/F2

**Script:** `Outreach Workflow/run_followup.py`
**Vincolo orario:** lun-ven, 08:00–19:00 (non invia il weekend né fuori orario)

Controlla il DB ogni mattina e identifica chi inviare F1 e F2.

#### Logica di selezione

**F1 (primo follow-up):**
```sql
WHERE stato = 'inviata'
  AND f1_inviata IS NULL
  AND risposta_ricevuta IS NULL
  AND giorni_da_invio >= 3
LIMIT 80
```

**F2 (secondo follow-up, break-up):**
```sql
WHERE f1_inviata IS NOT NULL
  AND f2_inviata IS NULL
  AND risposta_ricevuta IS NULL
  AND giorni_da_F1 >= 4
LIMIT 80
```

#### Caratteristiche F1 (giorno 3-4)

- **Opener Rainbow** — variante OPPOSTA a quella usata nella prima email (se originale era Barnum, F1 usa Rainbow)
- **Termine tecnico alternativo** — diverso dall'originale, stesso settore
- **Nuovo pain** con dato numerico credibile
- **Value reminder** — ricorda l'offerta gratuita in modo diverso
- **CTA binaria diversa** dall'originale
- Max 80 parole — link CTA obbligatorio
- QA automatico (media >= 7.0 per approvazione)

**Esempio F1 per agency / freelancer marketing:**
> "Di solito chi gestisce un'agenzia è sia chi porta i clienti che chi li serve — l'outreach regge finché non arriva il mese pieno di delivery."
>
> Il collo di bottiglia non è il talento, è il tempo speso a mandare email e DM a mano.
>
> Ho un workflow che automatizza quel pezzo al 100% — codice tuo, zero canoni. Vale uno sguardo rapido?
>
> [link presentazione] Vale uno sguardo?
>
> Max

#### Caratteristiche F2 (giorno 7-8, break-up)

- Stile "break-up email" — definitivo ma rispettoso
- 1 solo dato concreto di prova per la nicchia
- Nessuna pressione, porta aperta
- Max 55 parole — la brevità È il messaggio
- Non ripete il pitch

**Esempio F2 per agency / info-business:**
> Presumo che il timing non sia giusto. Rispetto.
>
> Ti lascio solo la presentazione: in 7 giorni installo il workflow sui tuoi server, codice tuo, zero canoni mensili.
>
> [link presentazione]
>
> Se cambia qualcosa, sai dove trovarmi.
>
> Max

#### DB update dopo invio

Dopo ogni F1 inviato → salva `f1_inviata` (datetime), `f1_oggetto`, `f1_corpo`, `stato='f1_inviata'`
Dopo ogni F2 inviato → salva `f2_inviata`, `f2_oggetto`, `f2_corpo`, `stato='f2_inviata'`

---

### [REPLY-MGR] — Email Reply Manager

**Script:** `Outreach Workflow/run_reply_manager.py`

Pipeline in 5 step:

```
[1] IMAP scan Gmail → [2] Segna nel DB → [3] Classifica + Genera risposta → [4] Invia via SMTP → [5] Aggiorna stato DB
```

#### Step 1 — ReplyMonitorAgent (IMAP scan)

Apre connessione `imap.gmail.com:993` con SSL.
Legge le ultime **200 email** in INBOX.
Per ogni email: estrae il mittente, controlla se è nella lista lead contattati (stato `inviata`, `f1_inviata`, `f2_inviata` con `risposta_ricevuta IS NULL`).
Se match → estrae il testo pulito (rimuove quoted text con `>` e header precedenti).
Dedup: se lo stesso lead ha più email, prende solo la più recente.

#### Step 2 — Segna risposta ricevuta

Aggiorna DB: `risposta_ricevuta = datetime, risposta_testo, risposta_oggetto, conversazione_stato = 'risposto'`

#### Step 3 — ConversationManagerAgent (classifica + genera)

**Classificazione** dell'intenzione del lead in 4 categorie:

| Categoria | Descrizione | Risposta generata |
|---|---|---|
| POSITIVO | Interessato, vuole info, aperto alla call | Propone 2-3 slot orari concreti per call di 20 min |
| OBIEZIONE | Resistenza (prezzo, tempo, "ci penso", "già lo fa qualcuno") | Riframe verso call gratuita, risponde all'obiezione specifica |
| DOMANDA | Chiede dettagli tecnici, referenze, come funziona | Risponde brevemente + guida verso call per approfondire |
| NON_INTERESSATO | No chiaro, "rimuovimi" | Uscita rispettosa, 40 parole, porta aperta |

**Regole risposta** identiche all'email originale:
- Prima persona singolare — max 100 parole
- Zero trattini — zero formule di cortesia ("Grazie per la risposta", "Perfetto")
- Inizia direttamente col contenuto
- Link CTA obbligatorio prima della firma
- Obiettivo dichiarato: call gratuita di 20 minuti

#### Step 4 — EmailSenderAgent

Invia la risposta via Gmail SMTP allo stesso lead.

#### Step 5 — Aggiorna DB

- Se risposta inviata → `conversazione_stato = 'in_conversazione'`
- Se NON_INTERESSATO → `conversazione_stato = 'esaurito'`

---

### [LI-REPLIES] — LinkedIn DM Check

**Script:** `LinkedIn Automation/check_replies.py`
**Log:** `LinkedIn Automation/linkedin_replies_log.txt`

Apre `linkedin.com/messaging` via Playwright (browser visibile, headless=False).
Scorre le conversazioni. Per ogni conversazione con **badge non letto**: apre il thread, estrae il testo del messaggio ricevuto e dell'ultimo nostro messaggio come contesto.

**Modalità default: READ-ONLY — non invia nulla.**

Per ogni risposta trovata, genera via AI:
1. Classificazione (POSITIVO / OBIEZIONE / DOMANDA / NON_INTERESSATO)
2. Testo di risposta suggerito (max 60 parole, stile LinkedIn — più informale dell'email)
3. CTA sempre verso la call di 20 minuti — **zero link** (su LinkedIn il link si dà a voce)

Stampa tutto a schermo + salva in `linkedin_replies_log.txt` per copia-incolla manuale.

**Modalità auto-invio (opzionale):**
```
python "LinkedIn Automation/check_replies.py" --autoinvia
```
Con `--autoinvia`: invia automaticamente le risposte, aggiorna `leads.json` con `status = 'reply_gestita'`, attende 30-60 secondi tra un invio e l'altro per comportamento umano.

---

## CATENA INSTAGRAM

---

### [IG-DM] — Instagram Direct Message

**Script:** `Instagram Automation/run_today.py`
**Log:** `Instagram Automation/run_today_log.txt`
**Lead DB:** `Instagram Automation/instagram_leads.json`
**Sub-agents:** `Instagram Automation/agents/` (3 agenti)

Fasi interne in sequenza:

---

**FASE 0 — Sub-agents: Pool massivo garantito** *(v3 — nuovo)*

Risolve il problema root "2 DM invece di 15": prima scopre, poi invia.
Tre sub-agent lavorano in sequenza nella stessa sessione browser:

*Sub-Agent A — Hashtag Scout (`agents/hashtag_scout.py`)*
- Scansiona **10 hashtag** (shuffle casuale dalla lista di 30 configurati)
- **25 profili per hashtag** (era 5 nella v2) = **250 candidati grezzi**
- Scroll aggressivo (10 round per hashtag) per triggerare API calls lazy
- Intercetta le risposte JSON di rete (70-103 username per hashtag dalla API)

*Sub-Agent B — Profile Qualifier (`agents/profile_qualifier.py`)*
- Visita fino a **60 profili** dal pool del Sub-Agent A
- Bio analysis con **60+ keyword** (incluse forme femminili: "formatrice", "imprenditrice", professioni: "fotografo", "psicologo", "avvocato", ecc.)
- Verifica presenza bottone **Messaggio** (account pubblico con DM abilitato)
- Score bio 1-10 per prioritizzare i migliori
- Stop automatico a **30 qualificati** trovati
- Salva in DB con `status = 'qualified'`

*Sub-Agent C — Similar Accounts Scout (`agents/similar_accounts_scout.py`)*
- Visita i **5 profili qualificati** con score più alto
- Estrae la sezione **"Profili simili"** / "Suggeriti per te" da Instagram
- Lead ad altissima qualità: algoritmo Instagram li considera target equivalenti
- Aggiunge come candidati con `status = 'new'` per il ciclo DM

**Matematica garantita:**
```
Scout:    10 hashtag × 25  = 250 candidati grezzi
Qualify:  max 60 visitati   → ~15-20% pass → 9-12 qualified
Similar:  5 profili top     → 30-50 candidati bonus
Pool DM:  30+ lead certi    → garantisce 15 DM/giorno
```

---

**FASE 1 — Scoperta legacy (backup)**
Se FASE 0 ha prodotto meno di 15 lead qualificati, la scoperta legacy è un backup:
- 8 hashtag (era 4) × 20 profili (era 5) = 160 ulteriori candidati
- Stessa logica di scraping con metodi a cascata (API → script → URL → modal)

---

**FASE 2 — Invia DM ai lead qualificati/nuovi**

Priorità: `qualified` (già pre-screenati, nessun filtro bio) → poi `new` (filtra al volo).

Per ogni lead:
1. Naviga al profilo (se `new`; i `qualified` hanno già la bio confermata)
2. Per `new`: filtra privati e non-target con keyword estese (target post-pivot: agency, info-business, coach, SMM, ecommerce)
3. Genera DM con angolo **APSOC ricalibrato** sul prodotto-gancio (max 50 parole) + link presentazione (`PRESENTATION_URL`) nel CTA
4. Clicca "Messaggio" → digita carattere per carattere → invia
5. Aggiorna status: `dm_sent`

Limite giornaliero: **15 DM** (Instagram penalizza l'invio massivo).

---

**FASE 3 — Follow-up F1 (giorno 2-3)**
Per chi non ha risposto al primo DM dopo 2-3 giorni.
Nuovo insight + CTA binaria. Max 25 parole. Zero link.

**FASE 4 — Follow-up F2 (giorno 6-7, break-up)**
Per chi non ha risposto a F1 dopo 4 giorni.
Break-up message con link agenzia. Max 35 parole.

---

**Differenze rispetto a LinkedIn:**
- Nessuna connection request: il DM è diretto
- Profili pubblici non richiedono accettazione
- Messaggi più corti (50 parole vs 75 LinkedIn)
- **Link presentazione nel primo DM** (post-pivot): il vecchio divieto "zero link" è stato rimosso. Volume basso per limitare il rischio penalizzazione
- Il messaggio arriva in "Richieste" se non si segue a vicenda — viene comunque recapitato

---

### [IG-REPLIES] — Instagram DM Reply Check

**Script:** `Instagram Automation/check_replies.py`
**Log:** `Instagram Automation/instagram_replies_log.txt`

Apre `instagram.com/direct/inbox/` via Playwright.
Scorre le conversazioni cercando messaggi non letti.

**Modalità default: READ-ONLY — non invia nulla.**

Per ogni risposta trovata, genera via AI:
1. Classificazione (POSITIVO / OBIEZIONE / DOMANDA / NON_INTERESSATO)
2. Testo di risposta suggerito (max 55 parole, stile Instagram — informale)
3. CTA verso la call gratuita di 20 minuti — **zero link** nel messaggio

Stampa tutto a schermo + salva in `instagram_replies_log.txt` per copia-incolla manuale.

**Modalità auto-invio (opzionale):**
```
python "Instagram Automation/check_replies.py" --autoinvia
```

---

### Progressione Stato Instagram (`instagram_leads.json`)

```
qualified         → Pre-qualificato da Profile Qualifier (bio ✓ + DM button ✓) — PRIORITÀ
new               → Trovato da hashtag/similar, non ancora processato
    ↓
dm_sent           → Primo DM inviato (giorno 0)
    ↓
f1_sent           → Follow-up F1 inviato (giorno 2-3)
    ↓
f2_sent           → Follow-up F2 inviato (giorno 6-7, break-up)
    ↓
reply_gestita     → Lead ha risposto, risposta gestita
    ↓
private           → Profilo privato (DM non inviabile) — skip
skip_no_target    → Bio non contiene parole chiave professione — skip
no_dm_button      → Profilo pubblico ma senza bottone Messaggio — skip
not_found         → Profilo inesistente/rimosso — skip
```

> **Nota v3:** i lead con status `qualified` saltano il filtro bio in FASE 2 — sono già stati
> verificati dal Profile Qualifier con bio score ≥ 1 e bottone DM confermato.

---

## Progressione dello Stato DB (email)

```
CSV input
    ↓
generata          → Email generata dall'AI, non ancora inviata
    ↓
inviata           → Email inviata al lead (giorno 0)
    ↓
f1_inviata        → Follow-up F1 inviato (giorno 3-4, se nessuna risposta)
    ↓
f2_inviata        → Follow-up F2 inviato (giorno 7-8, se nessuna risposta a F1)
    ↓
risposta          → Lead ha risposto (risposta_ricevuta viene settata)
    ↓
in_conversazione  → Risposta inviata (POSITIVO / OBIEZIONE / DOMANDA)
    ↓
chiamata_fissata  → [futuro] Lead ha confermato la call
    ↓
esaurito          → NON_INTERESSATO — conversazione chiusa con rispetto
```

---

## Target Supportati (post-pivot 2026-06-04)

Il sistema NON targetizza più professionisti locali (dentisti, avvocati, ristoranti, artigiani, salute): questi sono stati **rimossi** da scraper SETTORI, hashtag Instagram, ricerche LinkedIn e keyword bio.

Il target ora è composto da player del marketing e del digitale, con **chiavi settore canoniche**:

| Chiave settore | Target | Prodotto-gancio tipico |
|---|---|---|
| `agenzia` | Agency / agency owner | Outreach Factory |
| `info_product` | Info Business (info-product, formatori) | Content Factory |
| `coach` | Coach | Content Factory |
| `smm_freelance` | Marketing pros (SMM, copywriter, freelance ads) | Content Factory |
| `ecommerce` | Ecommerce | Outreach / Content Factory |
| `consulente` | Consulenti / team | Second Brain |
| `default` | Tutto il resto qualificato | match al volo |

Ogni chiave settore alimenta l'angolo APSOC e il match prodotto↔target nel qualifier (campo `prodotto_guida`).

---

## Framework di Qualità — Regole Universali

Queste regole si applicano a **ogni singolo testo generato** dal sistema (prima email, F1, F2, risposta a reply):

1. **Prima persona singolare** — solo "io", "ho", "mi", "mio". MAI "noi", "offriamo", "vogliamo"
2. **Zero trattini nel corpo** — ogni pausa è un punto fermo o una virgola
3. **Paragrafi separati** — riga vuota tra ogni blocco
4. **Link nel messaggio** — CTA con link presentazione `https://presentazione-empire.vercel.app/` + link agenzia `https://agency-empire-landing.vercel.app` in firma (su Email + LinkedIn + Instagram). Il vecchio HARD-BLOCK "link = FAIL" è stato rimosso; deliverability gestita a volume basso
5. **Zero scuse** — niente "Scusa il disturbo", "Spero non disturbi", "So che sei occupato"
6. **Zero esclamativi**
7. **Zero AI-slop** — termini generici come "soluzione innovativa", "ottimizzare la presenza digitale", "valore aggiunto" sono vietati
8. **QA automatico** — ogni email passa humanizer con soglia media >= 7.0; sotto soglia → retry con feedback
9. **Firma sempre "Max"** — senza cognome, tono da consulente personale

---

## Output e Log

| Cosa | Dove |
|---|---|
| Email generate e inviate | `Outreach Workflow/output/leads.db` (SQLite) |
| Email F1/F2 | Stesso DB, colonne `f1_*` / `f2_*` |
| Risposte email ricevute | Stesso DB, colonne `risposta_*` e `conversazione_stato` |
| Log commenti LinkedIn | `LinkedIn Automation/comments_log.txt` |
| Log connessioni LinkedIn | `LinkedIn Automation/run_today_log.txt` |
| Log reply check LinkedIn | `LinkedIn Automation/linkedin_replies_log.txt` |
| Instagram DM + follow-up | `Instagram Automation/run_today_log.txt` |
| Instagram DM lead DB | `Instagram Automation/instagram_leads.json` |
| Instagram reply check | `Instagram Automation/instagram_replies_log.txt` |
| Report finale terminale | Stampato a schermo con ✓/✗ per ogni modulo |

---

## Report Finale

Al termine dell'intera esecuzione, il terminale stampa:

```
=================================================================
  REPORT FINALE  HH:MM:SS
=================================================================
  ✓  COMMENTI         OK
  ✓  CONNESSIONI      OK
  ✓  EMAIL-GEN        OK
  ✓  EMAIL-INVIA      OK
  ✓  FOLLOWUP         OK
  ✓  REPLY-MGR        OK
  ✓  LI-REPLIES       OK
  ✓  IG-DM            OK
  ✓  IG-REPLIES       OK
=================================================================
```

Ogni modulo che fallisce mostra `✗` con il codice di errore o l'eccezione.
I moduli successivi saltano se il prerequisito fallisce (es: EMAIL-INVIA salta se EMAIL-GEN ha errori).

---

## Timing Atteso

| Catena / Modulo | Durata stimata | Parte quando |
|---|---|---|
| COMMENTI | ~20 min | subito |
| CONNESSIONI | ~10 min | subito (+3s) |
| **→ FOLLOWUP + REPLY-MGR + LI-REPLIES** | **~5-15 min** | **appena COMMENTI+CONNESSIONI finiscono** |
| EMAIL-GEN | ~60-70 min | subito (+6s) |
| **→ EMAIL-INVIA** | **~5-8 min** | **appena EMAIL-GEN finisce** |
| IG-DM (FASE 0: Scout+Qualify+Similar) | **+12-18 min** | subito (+5s) |
| IG-DM (FASE 1-4: DM + Follow-up) | ~15-20 min | dopo FASE 0 |
| **IG-DM totale** | **~30-40 min** | subito (+5s) |
| **→ IG-REPLIES** | **~5 min** | **appena IG-DM finisce** |
| **Totale script** | **~75-85 min** | (tre catene in parallelo) |

> **Nota:** il DB email non mostra nulla durante EMAIL-GEN — il salvataggio avviene in blocco solo alla fine di tutti i 100 lead. È normale non vedere output per 60+ minuti.
>
> **Breakdown reale EMAIL-GEN (per lead):** sleep 10s + latenza API OpenRouter ~26s = ~36s/lead totali → 100 lead ≈ 60 min
>
> **Instagram v3 — FASE 0:** i 3 sub-agents aggiungono ~12-18 minuti al totale ma **garantiscono 15 DM/giorno**. Senza FASE 0 il sistema trovava solo 2-9 DM con alta varianza. Il trade-off è giustificato: +15 min → +6-13 DM/giorno.
>
> **Limite 15 DM/giorno:** intenzionalmente conservativo. Instagram penalizza fortemente gli account nuovi con molte azioni. Non aumentare prima di 3+ settimane di utilizzo regolare.
>
> **v4.0:** aggiunta catena Instagram. **v3.0 IG:** 3 sub-agents FASE 0 per garantire 15 DM.

---

## Comandi

### Flusso giornaliero completo (ogni mattina feriale)

**Passo 1 — Attiva la sessione LinkedIn** (apre browser, fai login manuale, poi chiudi)
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach"
python "LinkedIn Automation\refresh_session.py"
```
> Le virgolette sono OBBLIGATORIE — il percorso contiene uno spazio.

**Passo 2 — Lancia il flusso principale** (nella stessa cmd, stessa cartella)
```
python run_parallel.py
```

---

### Comandi singoli (esecuzione manuale separata)

**Solo follow-up email:**
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow"
python run_followup.py
```

**Solo reply manager email:**
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow"
python run_reply_manager.py
```

**Solo LinkedIn DM check (suggerimenti, no invio):**
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation"
python check_replies.py
```

**LinkedIn DM check con auto-invio risposte:**
```
python check_replies.py --autoinvia
```

**Refresh sessione LinkedIn (quando scade):**
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach"
python "LinkedIn Automation\refresh_session.py"
```

**Solo Instagram DM + follow-up:**
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Instagram Automation"
python run_today.py
```

**Solo Instagram reply check (suggerimenti, no invio):**
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Instagram Automation"
python check_replies.py
```

**Instagram reply check con auto-invio risposte:**
```
python check_replies.py --autoinvia
```

**Refresh sessione Instagram (prima volta o quando scade):**
```
cd "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach"
python "Instagram Automation\refresh_session.py"
```
