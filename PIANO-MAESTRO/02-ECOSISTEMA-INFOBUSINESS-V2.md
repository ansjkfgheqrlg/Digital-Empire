# 📚 02 — ECOSISTEMA INFO-BUSINESS V2 (Digital Empire Group)

> Dossier v2 (V2-2, ADR-007) — amplia il v1 `02-ECOSISTEMA-INFOBUSINESS.md` a scala CF-grade (MEGA-reparto). Fonte: 11-PIANO-V2 §2.
>
> Questo dossier SUPERA il v1 dove in conflitto con la direttiva di scala. Il v1 resta riferimento
> per gli asset reali e i workflow di base — qui tutto viene portato a standard CF-grade. INFO-BUSINESS
> non è un "reparto" ma un'AZIENDA INTERNA a Digital Empire con gerarchia propria a livelli, capi area,
> coordinatori, verificatori. Corpus Maximilian 2026-06-11: "Il reparto Info Business è enorme, deve essere
> come un'azienda intera. Reparti enormi, come intere aziende dentro l'azienda: un leader, dei capi,
> una gerarchia solida a livelli, coordinatori, verificatori."
>
> Versione: 2.0 · Creato: 2026-06-16 · Fase: V2-2 (dossier architetturali) · Build effettiva: V2-6 (reparti v2).
> Stato: PROGETTATO — architettura target v2 descritta. Ciò che wrappa asset esistenti: [WRAPPA-ESISTENTE];
> ciò che è interamente nuovo: [TARGET-V2].

---

## 0. Missione + DONE WHEN

**Missione.** INFO-BUSINESS è la macchina industriale di Digital Empire per la produzione, il lancio e
la vendita continua di prodotti informativi: corsi, ebook, webinar, community, guide. Non è un reparto
di supporto — è un ecosistema revenue autonomo che genera fatturato proprio e alimenta l'autorità del brand
con ogni prodotto pubblicato. Ogni prodotto nasce da materiale raw già posseduto, attraversa gate di qualità
misurabili, viene lanciato con un sistema orchestrato e poi vive in evergreen — alimentando in parallelo la
pipeline AGENCY con lead caldi che vogliono la versione "fatta per loro".

A livello V2, INFO-BUSINESS è un'organizzazione a pieno titolo: non un set di workflow ma una gerarchia
a 4 livelli con 5 aree distinte, team di agenti da 6 a 10 per area, workflow CF-grade con state/trace/gate,
e loop di auto-miglioramento che impara da ogni lancio.

**Standard V2 di riferimento:** un workflow CF-grade di INFO-BUSINESS ha la stessa densità strutturale
del Content Factory di Exponium — quello che in v1 era "un'intera azienda" è qui uno dei workflow di un'area.

**DONE WHEN — la build V2-6 di INFO-BUSINESS è completa quando:**

1. Le 5 aree L2 esistono in `company/02-infobusiness/` come strutture-cartella con: `BACKBONE.md`,
   cartella `agenti/` (6-10 schede millimetriche), cartella `workflow/` (1-5 WF CF-grade), `principi/`,
   `scripts/`, `kpi/`, `state/`.
2. Il catalogo prodotti (`InfoBusiness/CATALOGO`) è senza campi vuoti: ogni prodotto ha ruolo deciso
   (lead magnet o prodotto a pagamento), prezzo assegnato dal team-prezzi (B-003, ADR-005), target,
   promessa verificabile, funnel assegnato.
3. WF-CORSO produce un corso completo da cartella raw → MKD → curriculum → lezioni → piattaforma
   Supabase senza intervento manuale tranne i gate: il corso "Vendi la Skill n.1" è il banco di prova.
4. WF-LANCIO esegue un lancio end-to-end con calendario T-30→T+7, copy gate APSOC ≥80/100,
   dry-run completo prima del go: il primo lancio orchestrato corrisponde al gate F6 del Piano Maestro.
5. Funnel evergreen attivo: lead magnet → sequenza nurture → sales page → checkout → tracking, percorso
   cliccabile end-to-end con eventi in analytics.
6. Ogni acquirente entra in onboarding automatico ≤24h; i lead caldi passano ad AGENCY via handoff contract
   con segnale documentato e consenso verificato.
7. Debrief post-lancio scritto in ReasoningBank; zero asset Info-Business orfani (tabella §6 completa).
8. Dashboard KPI per tutte e 5 le aree visibile e alimentata da dati reali (non stimati).
9. Review MAXIMILIAN (passo 5-bis, da V2-3) ha approvato l'architettura: "abbastanza grande? millimetrica?
   si vede nell'Explorer?"

**OUT OF SCOPE (v2):** ads a pagamento senza ok esplicito di Max; pubblicazione automatica senza review
umana nei primi 2 lanci; affiliazioni; prodotti high-ticket con sales call (fase successiva); training
automatico del neural su dati < 3 lanci reali.

---

## 1. Posizione nella holding — handoff espliciti con gli altri ecosistemi

INFO-BUSINESS è ecosistema **revenue** (come AGENCY) e **moltiplicatore di autorità**: ogni prodotto
pubblicato rafforza il posizionamento "AI che implementa" e prepara il cross-sell verso AGENCY. I due
ecosistemi non competono: INFO-BUSINESS serve chi vuole imparare, AGENCY serve chi vuole delegar fare.
Il ciclo ottimale è studente → cliente AGENCY → referral.

Il v1 documenta i handoff contract base (HC-IB-AG-01 ecc.). In v2 si porta ogni handoff a livello di
interfaccia esplicita `{from, to, payload, acceptance_criteria, fallback}` sul BUS corporativo.

### 1.1 Handoff in INGRESSO

| Contract | Da | A (area IB) | Payload | Acceptance criteria |
|---|---|---|---|---|
| `HC-CF-IB-01` | 03 CONTENT-FACTORY | Area Prodotto | Moduli video corso (script approvato → video montato), caroselli pre-lancio, thumbnail | formato/durata da brief; brand voice gate passato; Zero asset senza brief di origine |
| `HC-MK-IB-01` | 04 MARKETING | Area Lanci | Sequenze email lancio (pre-lancio, cart open, cart close), copy sales page, ad copy | APSOC ≥80/100; CTA univoca; zero claim non provabili; nomenclatura file da brief |
| `HC-IN-IB-01` | 08 INTELLIGENCE | Area Prodotto + Lanci | Customer research, trend nicchia, ingest fonti, pattern da ReasoningBank | atomi archiviati in wiki + namespace `infobusiness/intel`; fonte citata |
| `HC-PL-IB-01` | 06 PLATFORM | Area Prodotto | Piattaforma corso (Supabase + Next.js), checkout, paywall tecnico, fix bug | deploy verde + smoke test studente; uptime 99%; handoff con credentials |
| `HC-FO-IB-01` | 07 FORGE | Tutte le aree | Nuovi agenti/skill su richiesta | skill passa skill-creator eval; scheda agente millimetrica conforme standard V2 |
| `HC-OP-IB-01` | 09 OPERATIONS | Area Lanci + Prodotto | Budget approvato per lancio, scheduling run, cost report | approvazione scritta prima del go/no-go; stima costi dry-run inclusa |

### 1.2 Handoff in USCITA

| Contract | Da (area IB) | A | Payload | Acceptance criteria |
|---|---|---|---|---|
| `HC-IB-AG-01` | Area Community | 01 AGENCY (Acquisizione) | Lead caldi cross-sell: acquirenti con segnale esplicito di bisogno di implementazione | `{lead_id, fonte_prodotto, segnale_esplicito, score, consenso}`; nessun outreach automatico senza consenso |
| `HC-IB-CF-01` | Area Lanci | 03 CONTENT-FACTORY | Brief contenuti pre-lancio (angoli, hook, calendario, ICP) | brief con ICP + obiettivo per pezzo + scadenza T-21 |
| `HC-IB-MK-01` | Area Vendite | 04 MARKETING | Briefing funnel evergreen: offer stack, sales page, email nurture | offer stack approvato dall'Area Vendite prima del briefing |
| `HC-IB-MB-01` | Area Prodotto | 05 MULTI-BUSINESS (Publishing/KDP) | Contenuto corso/ebook riconfezionabile per KDP | diritti verificati; formato conforme; decision scritto nel catalogo |
| `HC-IB-OP-01` | Area Lanci | 09 OPERATIONS | Stima costi lancio (dry-run), scheduling sequenze, report post-lancio | budget approvato prima del go; reale vs piano nel debrief |

**Regola invariata:** INFO-BUSINESS non produce tooling in-house né campagne media grandi — li richiede via
contract ai rispettivi ecosistemi. Produce in-house solo ciò che è quotidiano e operativo (le 5 aree, §3).

---

## 2. Gerarchia a livelli del MEGA-REPARTO

INFO-BUSINESS è organizzato su **4 livelli gerarchici** interni, tutti sotto il Mandato Empire e il Board:

```
LIVELLO 0 — Board C-Suite (COO, CEO, CRO-Revenue)
│   ↓ direttive, obiettivi trimestrali, approvazioni budget grandi
LIVELLO 1 — IB-DIRECTOR (ib-director)
│   Lead assoluto dell'ecosistema. Opera su Opus. Coordina le 5 Aree.
│   Riporta al Board; emette ordini ai 5 Capi Area. Decisore finale go/no-go lancio.
│
├── LIVELLO 2 — 5 CAPI AREA (Coordinator L2) — uno per ogni Area
│   ├── IB-COORD-PRODOTTO — capo Area Prodotto
│   ├── IB-COORD-LANCI — capo Area Lanci
│   ├── IB-COORD-VENDITE — capo Area Vendite/Funnel
│   ├── IB-COORD-COMMUNITY — capo Area Community & Retention
│   └── IB-COORD-STRATEGIA — capo Area Strategia & Intelligence
│       Ogni capo orchestra i workflow della sua area; riporta a ib-director;
│       può bloccare o escalare al director.
│
├── LIVELLO 3 — COORDINATORI DI WORKFLOW (Lead L3)
│   Un coordinatore per ogni workflow CF-grade. Gestisce il flusso giorno per giorno.
│   Riporta al Capo Area. Esempi: ib-corso-lead, ib-lancio-lead, ib-funnel-lead.
│
└── LIVELLO 4 — VERIFICATORI QA + WORKER SPECIALISTI (L4)
    Un QA per area (verificatore indipendente, non in gerarchia con i worker).
    Worker specialisti per ogni funzione: mkd-forger, curriculum-architect, lesson-writer,
    launch-planner, copy-liaison, asset-checker, onboarder, engagement-runner, ecc.
```

**Regola di escalation:** ogni gate bloccante non superato sale di un livello. Un worker non può
sbloccare da solo: coinvolge il coordinatore workflow → capo area → director → Board se necessario.

**Regola di indipendenza QA:** i verificatori (uno per area) non riportano al Capo Area ma direttamente
a ib-director. Nessun QA si trova sotto il coordinatore dei workflow che valuta: indipendenza garantita.

---

## 3. Aree L2 v2 — 5 organizzazioni dentro l'organizzazione

Il v1 aveva 4 "reparti L2" (Prodotto, Lanci, Vendite/Funnel, Community). La direttiva §2 richiede al
rialzo: ogni area è un'organizzazione con team 6-10 agenti, workflow CF-grade, QA indipendente, namespace
propri. Si aggiunge l'Area Strategia & Intelligence che in v1 era assente come struttura dedicata (gap critico).

| ID | Nome | Tipo | N. agenti | N. WF CF-grade | Razionale v2 |
|---|---|---|---|---|---|
| IB-L2-PROD | Produzione Prodotti | WRAPPA-ESISTENTE + TARGET-V2 | 10 | 3 | cuore operativo; va portato da team 4 a 10 con QA dedicato |
| IB-L2-LANC | Lanci & Campagne | WRAPPA-ESISTENTE + TARGET-V2 | 9 | 4 | orchestrazione militare; aggiungere Webinar + Debrief CF-grade |
| IB-L2-VEND | Vendite & Funnel | WRAPPA-ESISTENTE + TARGET-V2 | 8 | 3 | evergreen + sales page + CRO; pricing da team-prezzi (B-003) |
| IB-L2-COMM | Community & Retention | WRAPPA-ESISTENTE + TARGET-V2 | 8 | 3 | onboarding + community + cross-sell; gap v1: solo 4 funzioni |
| IB-L2-STRA | Strategia & Intelligence | TARGET-V2 | 7 | 2 | mancava in v1; product backlog, trend, concorrenti, roadmap |

---

### IB-L2-PROD — AREA PRODUZIONE PRODOTTI [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Trasformare materiale raw già posseduto (registrazioni, PDF, manuali, transcript in
`Formazzione/`) in prodotti finiti: ebook, corsi su piattaforma, guide, webinar recording. Nessun
prodotto si crea senza validazione idea (score ≥60/100 da WF-VALIDAZIONE). Il materiale grezzo non
si butta mai: si ingesta, si struttura, si valida, poi si produce.

**Principi non negoziabili:**
1. Zero produzione senza gate WF-VALIDAZIONE passato (idea score ≥60 + MVP test).
2. Il MKD (Master Knowledge Document) copre il 100% degli atomi informativi della fonte: nessun contenuto
   si perde nella trasformazione (verifica quantitativa da parte del QA).
3. Ogni lezione ha 1 outcome verificabile e misurabile dichiarato; nessuna lezione "teorica" senza esercizio.
4. Il corso esiste sulla piattaforma reale del cliente prima di qualsiasi lancio: nessun lancio di ombre.

**Team agenti (10):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| IB-COORD-PRODOTTO | Capo Area Prodotto — L2 coordinator | sonnet | Orchestra i 3 WF; priorità di produzione; escalation a ib-director; riporta KPI settimanale |
| IB-PROD-QA | Verificatore Prodotto — QA area (indipendente) | sonnet | Controlla gate qualità prodotto: 100% atomi fonte, outcome per lezione, smoke test; blocca, non suggerisce |
| IB-PROD-VALID | Product Idea Validator | sonnet | WF-VALIDAZIONE: scoring /100 su 5 criteri, MVP test 7gg, brief validato — gate d'ingresso di tutta l'area |
| IB-PROD-MKD | MKD Forger | sonnet | Esegue content-forge su cartella raw → MKD (Master Knowledge Document); log atomi coperti vs fonte |
| IB-PROD-CURRIC | Curriculum Architect | sonnet | MKD → struttura moduli/lezioni con obiettivi di apprendimento misurabili, prerequisiti, durata, esercizi |
| IB-PROD-WRITER | Lesson Writer | sonnet | Scrive script lezioni/capitoli dal curriculum; voce DE; consegna a CONTENT-FACTORY per video |
| IB-PROD-PLATFORM | Platform Integrator | sonnet | Coordina `HC-PL-IB-01` verso PLATFORM; verifica deploy Supabase+Next.js; log errori ambienti |
| IB-PROD-DESIGN | Asset Designer | sonnet | Copertine ebook, slide, workbook, certificato; handoff brief a CONTENT-FACTORY per grafiche |
| IB-PROD-EBOOK | Ebook Specialist | sonnet | Pipeline ebook: raw → MKD → capitoli → impaginazione → export PDF/ePub (Manuale Claude Code: prototipo) |
| IB-PROD-LEARN | Product Pattern Learner | sonnet | Ogni ciclo produzione → pattern: cosa ha rallentato, quale formato converte, difetti ricorrenti → `infobusiness/reasoning` |

**Workflow CF-grade (3):**

**WF-VALIDAZIONE** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: filtrare le idee prodotto con gate quantitativo prima di produrre. Niente entra in WF-CORSO o
  WF-EBOOK senza aver passato questo workflow. Kernel estratto da `Lancio corso skill beast/processo lancio.txt`.
- Flusso:
  ```
  IB-PROD-VALID riceve idea → scoring su 5 criteri:
  (1) problema reale e misurabile /20
  (2) materiale raw già disponibile /20
  (3) ICP chiaro e raggiungibile /20
  (4) differenziazione da offerta esistente /20
  (5) allineamento posizionamento DE /20
  → TOTALE /100
  Gate 1: score ≥60 → avanza a MVP test
  Gate 2: MVP test — 5 "sì, lo comprerei" reali da persone ICP in 7gg
  → PASS: brief validato → IB-COORD-PRODOTTO approva avvio produzione
  → FAIL: idea in BACKLOG (ADR-005); mai in produzione; motivo registrato
  ```
- Gate BLOCCANTE: score ≥60 + MVP test → senza PASS nulla entra in produzione.
- State: `company/02-infobusiness/prodotto/validazione/state.json` — idea, score, MVP result, esito, data.
- Script: `infobusiness/scripts/idea_scorer.py` [TARGET-V2] — scoring automatico dei 5 criteri con input da brief.

**WF-CORSO** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: produrre un corso completo da materiale raw → corso live su piattaforma pronto al lancio.
  Il "Vendi la Skill n.1" è il primo banco di prova; gli agenti `formazione-*` esistenti sono wrappati
  come team L3 di questo workflow.
- Flusso:
  ```
  INPUT: brief validato (WF-VALIDAZIONE PASS) + cartella raw (es. Formazzione/Claude code/)
  ─────────────────────────────────────────────────────────────────────────
  1. IB-PROD-MKD → content-forge sull'intera cartella → MKD
     GATE QA: MKD copre 100% atomi fonte (checklist quantitativa: n. sezioni fonte vs n. atomi MKD)
  2. IB-PROD-CURRIC → MKD → curriculum: moduli, lezioni, obiettivi misurabili, esercizi, durata totale
     GATE QA: ogni lezione ha 1 outcome verificabile dichiarato; durata totale stimata presente
  3. IB-PROD-WRITER → script lezione per lezione (testo per ebook, script video per corso video)
     GATE: brand voice gate (Mandato Empire) + zero contenuto generico + nessun claim senza prova
  4. HANDOFF HC-CF-IB-01 → 03 CONTENT-FACTORY: script video → moduli video montati
     Acceptance: durata da brief; formato MP4; qualità audio ≥44kHz; thumbnail inclusa
  5. IB-PROD-PLATFORM → coordina HC-PL-IB-01: formazione-orchestrator (carica schema+contenuti
     su Supabase), formazione-admin (accessi e iscrizioni), formazione-design (UI corso),
     formazione-student (percorso studente + progress tracking)
     GATE: smoke test "studente fantasma" — completa modulo 1 end-to-end senza errori
  6. IB-PROD-DESIGN → copertina, workbook, certificato
     GATE QA: brand conforme; nessun asset con placeholder
  OUTPUT: corso live su piattaforma + asset vendita preliminari → handoff a IB-L2-VEND
  ```
- State: `company/02-infobusiness/prodotto/corso/state.json` — per ogni corso: fase corrente, gate superati, errori bloccanti, log.
- Script: `infobusiness/scripts/content_forge_runner.py` [WRAPPA] — orchestrazione content-forge su cartella.

**WF-EBOOK** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: trasformare materiale raw in ebook impaginato pronto alla vendita o come lead magnet.
  Il Manuale Claude Code (203 pagine esistente) è il prototipo validato di questo workflow.
- Flusso:
  ```
  INPUT: brief validato + cartella/file raw
  ─────────────────────────────────────────────────────────────────────────
  1. IB-PROD-MKD → content-forge → MKD (stesse regole WF-CORSO)
  2. IB-PROD-EBOOK → capitoli: struttura ebook (introduzione, sezioni, conclusione, call-to-action)
     GATE: 1 CTA chiara per capitolo; nessun capitolo senza esercizio pratico
  3. IB-PROD-WRITER → testo capitolo per capitolo; brand voice DE
     GATE QA: "prove non promesse" su ogni claim (Mandato Art.2)
  4. IB-PROD-DESIGN → impaginazione PDF/ePub + copertina professionale
     GATE: versione finale leggibile su mobile; link funzionanti; nessun placeholder
  5. IB-PROD-PLATFORM → carica ebook su storage sicuro; link con accesso protetto; checkout se a pagamento
  OUTPUT: file ebook (PDF + ePub) + pagina download + asset lancio → handoff a IB-L2-VEND
  ```
- State: `company/02-infobusiness/prodotto/ebook/state.json`.
- Nota [VINCOLO REALE]: il ruolo del Manuale Claude Code (lead magnet gratuito vs prodotto a pagamento)
  è ANCORA INDECISO → B-002 BACKLOG; la decisione spetta al team-prezzi (B-003, ADR-005).
  Questo workflow è pronto, ma il routing verso funnel gratuito o a pagamento attende quella decisione.

**Namespace memoria area:** `infobusiness/prodotto/` — MKD, curriculum, decisioni di prodotto, smoke test log.
**KPI (da misurare, non inventare):** lead time corso (giorni da brief validato → corso live); % idee che
superano gate validazione; % gate QA superati al primo giro; difetti trovati in smoke test per corso.

---

### IB-L2-LANC — AREA LANCI & CAMPAGNE [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Orchestrare ogni lancio come operazione militare a calendario: pre-lancio, cart open,
cart close, post-lancio. Un lancio = un workflow CF-grade con dry-run obbligatorio e go/no-go formale
approvato dal director. Nessun lancio parte senza tutti i gate verdi.

**Principi non negoziabili:**
1. Nessun lancio senza prodotto che ha superato il gate qualità prodotto (WF-CORSO o WF-EBOOK PASS).
2. Nessun lancio senza budget approvato da 09-OPERATIONS (dry-run con stima costi a T-1).
3. Scarcity REALE o nessuna scarcity: deadline e bonus a scadenza devono essere reali; le false scarce
   sono vietate dal Mandato Empire (Art.2 — "prove non promesse").
4. Copy gate APSOC ≥80/100 su OGNI elemento scritto del lancio (email, sales page, ad) prima di inviarlo.
5. Dry-run completo (simulazione invii + stima costi) obbligatorio a T-1, prima del go/no-go.

**Team agenti (9):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| IB-COORD-LANCI | Capo Area Lanci — L2 coordinator | opus | Regista lancio: pianifica, coordina i 4 WF, emette go/no-go (con consensus), riporta a ib-director |
| IB-LANC-QA | Verificatore Lanci — QA area (indipendente) | opus | Gate copy (APSOC ≥80), gate asset-complete, gate dry-run: blocca se non conforme; mai suggerisce |
| IB-LANC-PLANNER | Launch Planner | sonnet | Costruisce timeline T-30→T+7 con dipendenze, owner per task, buffer e contingencies |
| IB-LANC-COPY-LIAISON | Copy Liaison | sonnet | Prepara handoff HC-IB-MK-01 a MARKETING; valida i rientri contro acceptance criteria; escalation se APSOC < 80 |
| IB-LANC-ASSET | Asset Checker | haiku | Checklist asset 100%: sales page live, checkout testato, email caricate, tracking attivo, link verificati |
| IB-LANC-WEBINAR | Webinar Producer | sonnet | Script webinar + struttura apertura (base: PDF `InfoBusiness/Webinar/`) + replay funnel |
| IB-LANC-TRACKER | Launch Tracker | haiku | Monitoraggio giornaliero conversioni per step durante cart open; report a IB-COORD-LANCI |
| IB-LANC-DEBRIEF | Post-Launch Analyst | sonnet | Post-mortem strutturato: piano vs reale, root cause, pattern → `infobusiness/reasoningbank` |
| IB-LANC-DRY | Dry-Run Conductor | sonnet | Esegue simulazione completa lancio a T-1; produce stima costi; log risultati; input per go/no-go |

**Workflow CF-grade (4):**

**WF-LANCIO** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: orchestrare un lancio completo end-to-end con calendario T-30→T+7, gate bloccanti a ogni step.
- Flusso:
  ```
  INPUT: prodotto con gate qualità prodotto PASS + budget approvato da OPERATIONS
  ─────────────────────────────────────────────────────────────────────────
  PRE-LANCIO (T-30 → T-1)
    T-30: IB-LANC-PLANNER → calendario completo + dipendenze + owner per task
    T-28: handoff HC-IN-IB-01 → INTELLIGENCE: customer research / angoli (Thought Leader Funnel)
    T-21: handoff HC-IB-CF-01 → CONTENT-FACTORY: contenuti organici pre-lancio (brief per pezzo, ICP)
    T-14: handoff HC-IB-MK-01 → MARKETING: sales page + sequenza pre-lancio
          GATE IB-LANC-QA: APSOC ≥80/100 su TUTTO il copy ricevuto
    T-7:  IB-LANC-COPY-LIAISON: tutte le email cart open/close rientrate e validate
    T-3:  IB-LANC-ASSET: checklist 100% (page live, checkout testato, tracking attivo, email caricate)
    T-1:  IB-LANC-DRY → dry-run completo (simulazione invii + stima costi) → report a IB-COORD-LANCI
          GATE: stima costi approvata da Cost-Sentinel + OPERATIONS
    T-0-ε: GO/NO-GO: hive-mind consensus (ib-director + IB-LANC-QA + Quality-Sentinel + Brand-Voice-Sentinel
           + Cost-Sentinel). UN solo NO blocca il lancio.

  CART OPEN (T0 → T+4/6)
    T0:    apertura: email 1 + post organico + webinar (se WF-WEBINAR schedulato)
    T+1..n: sequenza cart open: obiezioni (1 email = 1 obiezione, pattern APSOC), social proof, FAQ
    ogni 24h: IB-LANC-TRACKER → conversioni per step (opt-in, click sales page, checkout avviato, acquisto)
              → micro-aggiustamenti solo copy (non offerta, non prezzo) pre-approvati da IB-COORD-LANCI

  CART CLOSE (ultime 48h)
    scarcity REALE (deadline/bonus verificabile — mai finta: Mandato Art.2)
    email close ×3 (urgenza, FAQ finale, last call)
    chiusura checkout all'ora stabilita (non posticipabile)

  POST-LANCIO (T+7)
    onboarding acquirenti ≤24h → handoff a IB-L2-COMM (WF-ONBOARDING-STUDENTE)
    IB-LANC-DEBRIEF: numeri reali vs piano, cosa rifare/evitare → ReasoningBank
    IB-COORD-LANCI: report a ib-director; update CATALOGO con metriche reali del lancio

  OUTPUT: lancio chiuso + debrief + coorte studenti in onboarding + metriche nel catalogo
  ```
- State: `company/02-infobusiness/lanci/<lancio-id>/state.json` — ogni step: status, gate, timestamp, errori.
- Script: `infobusiness/scripts/launch_calendar.py` [TARGET-V2] — genera timeline T-30→T+7 da parametri lancio.

**WF-WEBINAR** [TARGET-V2]
- Scopo: webinar di vendita come asset di lancio: script, live o registrazione, replay funnel.
  Base esistente: PDF in `InfoBusiness/Webinar/` (3 script apertura storytelling).
- Flusso:
  ```
  1. IB-LANC-WEBINAR → struttura webinar (apertura storytelling da template Webinar/, contenuto valore,
     pitch APSOC, Q&A, call-to-action), durata 60-90 minuti
     GATE IB-LANC-QA: script conforme APSOC + brand voice; CTA chiara; zero promesse senza prova
  2. Produzione: coordinamento con 03-CONTENT-FACTORY per setup tecnico (video/audio)
  3. Esecuzione: live o registrazione (Max prende il microfono; agenti preparano slide, timer, chat)
  4. Replay: IB-LANC-WEBINAR configura replay funnel (link protetto → opt-in → accesso replay →
     scarcity reale sulla disponibilità del replay)
  OUTPUT: webinar registrato + replay funnel live + metriche registrati/partecipanti
  ```
- State: `company/02-infobusiness/lanci/webinar/state.json`.

**WF-DEBRIEF-LANCIO** [TARGET-V2]
- Scopo: apprendere da ogni lancio (win o loss, grandi o piccoli) e scrivere i pattern in ReasoningBank.
  Nessun lancio è "finito" finché il debrief non è scritto e validato.
- Flusso:
  ```
  IB-LANC-DEBRIEF raccoglie entro T+7:
  - Piano vs reale: ogni KPI (conversione per step, n. acquirenti, AOV)
  - Root cause di ogni scarto ≥10% (positivo o negativo)
  - Cosa ha funzionato (pattern da replicare)
  - Cosa non ha funzionato (pattern da evitare o correggere)
  - Raccomandazione skill/agente da aggiornare
  → Distillato scritto in `infobusiness/reasoningbank` (namespace `infobusiness/lanci`)
  → Aggiornamento CATALOGO con metriche reali del prodotto
  GATE: debrief scritto entro T+7; almeno 3 pattern distillati; nessun numero approssimato
  ```
- State: integrato nel state.json del lancio padre.

**WF-FOLLOWUP-COPY** [TARGET-V2]
- Scopo: dopo ogni lancio chiuso, aggiornare la libreria copy (email, hook, obiezioni) con i pezzi
  che hanno performato meglio, per rendere il prossimo lancio più efficace.
- Flusso:
  ```
  IB-LANC-DEBRIEF → top 3 email per conversione + top 3 hook → IB-LANC-COPY-LIAISON →
  handoff ad Area Vendite (libreria evergreen) + segnalazione a 04-MARKETING per update template
  GATE: solo copy con metriche reali documentate entra nella libreria
  ```

**Namespace memoria area:** `infobusiness/lanci/` — calendari, copy approvati, numeri reali per lancio,
pattern debrief, stato gate per ogni lancio.
**KPI (da misurare):** aderenza calendario (% task completati entro la data pianificata); conversione
lancio (% lista → acquisto); scarto piano vs reale; n. pattern ReasoningBank per lancio.

---

### IB-L2-VEND — AREA VENDITE & FUNNEL [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Costruire e ottimizzare l'infrastruttura di vendita che genera revenue sia durante i
lanci sia nei 365 giorni tra un lancio e l'altro. Il funnel evergreen non è un ripiego post-lancio ma
un reparto dedicato con workflow propri. L'offer stack (pricing, bonus, garanzie) è gestito qui; i numeri
di prezzo vengono dal team-prezzi (B-003, ADR-005) — questo reparto li recepisce e costruisce l'architettura.

**Principio critico [VINCOLO B-002/B-003]:** il prezzo del Manuale Claude Code NON è deciso. Il team-prezzi
(B-003) proporrà i numeri per tutti i prodotti. Questo reparto NON inventa prezzi: slot l'offer stack pronto,
ma i valori numerici arrivano da B-003 prima del go live. Né questo dossier né nessun agente IB può
pubblicare prezzi non approvati.

**Team agenti (8):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| IB-COORD-VENDITE | Capo Area Vendite — L2 coordinator | sonnet | Orchestra i 3 WF; coordina con MARKETING/PLATFORM; escalation a ib-director |
| IB-VEND-QA | Verificatore Vendite — QA area (indipendente) | sonnet | Gate copy APSOC + gate brand ("prove non promesse") su ogni elemento della sales page e del funnel |
| IB-VEND-OFFER | Offer Architect | sonnet | Costruisce value stack, bonus, garanzia, order bump, upsell, naming — attende prezzi da team-prezzi (B-003) |
| IB-VEND-SALESPAGE | Sales Page Builder | sonnet | Sales page: copy APSOC + build empire-premium-style (skill `cro-copy-architect` + `empire-premium-style`) |
| IB-VEND-CHECKOUT | Checkout Technician | haiku | Pagina pagamento, recupero carrelli abbandonati, ricevute; coordina con PLATFORM |
| IB-VEND-CRO | CRO Analyst | sonnet | Test A/B su step del funnel (skill `ab-testing`, `cro`); 1 test alla volta; no rollout senza dati |
| IB-VEND-TRACK | Tracking Analyst | haiku | Eventi, UTM, attribution, report conversioni per step; input per CRO e debrief lancio |
| IB-VEND-LEAD | Lead Magnet Specialist | sonnet | Opt-in page, lead magnet (ebook gratuito o altro), integrazione lista email; skill `lead-magnets` |

**Workflow CF-grade (3):**

**WF-SALESPAGE** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: costruire la sales page canonica per ogni prodotto — da brief a pagina live con gate APSOC.
  Asset esistenti in `Lancio corso skill beast/` (Leanding Page CCM, Page, Sale pag, smerd) vengono
  CONSOLIDATI in UNA sola pagina canonica per prodotto; duplicati archiviati, non cancellati (ADR-003).
- Flusso:
  ```
  1. IB-VEND-OFFER → offer stack: value stack + bonus + garanzia + order bump + upsell
     GATE: prezzi da catalogo approvato da team-prezzi (B-003); nessun numero placeholder in produzione
  2. IB-VEND-SALESPAGE → copy APSOC: problema → agitazione → soluzione → proof → offerta → CTA
     GATE IB-VEND-QA: APSOC ≥80/100; "prove non promesse" verificato; nessun claim senza documentazione
  3. Handoff HC-PL-IB-01 → PLATFORM: build pagina con skill `empire-premium-style`; deploy
     GATE: pagina caricata ≤5s; mobile responsive; ogni link funzionante; checkout collegato
  4. IB-VEND-TRACK → tracking: eventi pixel (view, add-to-cart, purchase) + UTM su ogni fonte traffico
     GATE: test eventi in debug mode verde prima del lancio
  OUTPUT: sales page live + tracking attivo → ready per WF-LANCIO (T-14)
  ```
- State: `company/02-infobusiness/vendite/salespage/state.json`.

**WF-FUNNEL-EVERGREEN** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: sistema di vendita continua che gira 365 giorni senza dipendere dai lanci. Modello di
  riferimento: `InfoBusiness/Funnel Unico Perfetto – ....pdf` (ingestito come blueprint).
  Un lancio valida l'offerta; il funnel evergreen la scala.
- Flusso:
  ```
  1. Lead magnet: ebook Manuale Claude Code (o altro asset deciso dal team-prezzi B-003) →
     IB-VEND-LEAD → opt-in page (APSOC + brand voice) → utente in lista email
  2. IB-VEND-SALESPAGE → sequenza nurture (frame Founder Authority Stack, da intelligence Beggiato):
     valore → autorità → offerta (5-7 email; skill `emails`)
     GATE IB-VEND-QA: ogni email APSOC verificata; nessuna email con più di 1 CTA
  3. Sales page evergreen (variante della page lancio, senza deadline finte — Mandato Art.2)
     GATE: "permanente" significa senza scarcity artificiale; se c'è un bonus a scadenza, deve essere reale
  4. IB-VEND-CHECKOUT → checkout + order bump + upsell (prezzi da team-prezzi B-003)
  5. Acquirente → WF-ONBOARDING-STUDENTE (IB-L2-COMM) → community → cross-sell scout
  6. Loop: IB-VEND-TRACK misura ogni step (opt-in rate, open rate email, click sales page, conversione)
           → IB-VEND-CRO propone 1 test A/B alla volta → risultato in ≥14 giorni → adozione o scarto
  OUTPUT: revenue continua + pipeline lead per AGENCY senza dipendere dai lanci
  ```
- State: `company/02-infobusiness/vendite/evergreen/state.json` — step attivi, metriche per step, A/B test in corso.

**WF-CRO-OTTIMIZZAZIONE** [TARGET-V2]
- Scopo: ciclo continuativo di ottimizzazione del funnel basato su dati reali. 1 test A/B alla volta;
  nessuna conclusione su campione < minimo statistico (calcolato da IB-VEND-CRO).
- Flusso:
  ```
  IB-VEND-TRACK → analisi settimanale → identifica step con conversione più bassa
  IB-VEND-CRO → formula ipotesi (non "proviamo a vedere" ma ipotesi falsificabile) →
  propone variante (solo 1 elemento cambiato per test) → approvazione IB-COORD-VENDITE →
  rollout su % traffico (non su tutto) → attesa dati → analisi → adozione o scarto
  GATE: test non dichiarato "conclusivo" fino a campione minimo; risultati in `infobusiness/funnel`
  ```

**Namespace memoria area:** `infobusiness/funnel/` — configurazione evergreen, esiti A/B, metriche step,
offer stack corrente.
**KPI (da misurare):** conversione evergreen (% visitatori → acquisto); opt-in rate lead magnet; AOV
(effetto bump/upsell); email open rate; revenue per lead.

---

### IB-L2-COMM — AREA COMMUNITY & RETENTION [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Il prodotto inizia DOPO l'acquisto. Onboarding studenti, community attiva, completamento
corsi, raccolta testimonianze, identificazione lead caldi per AGENCY. La retention non è un nice-to-have:
uno studente che completa il corso è il miglior venditore del prossimo e il candidato ideale per diventare
cliente AGENCY.

**Principi non negoziabili:**
1. Onboarding ≤24h dall'acquisto: nessun acquirente aspetta il giorno dopo.
2. Cross-sell verso AGENCY SOLO su segnale esplicito e consenso: mai outreach automatico sugli studenti.
3. Testimonianze raccolte SOLO su metriche reali e verificabili (Mandato Art.2 — "prove non promesse").
4. La community esiste per gli studenti, non per vendere: i rituali devono generare valore prima di chiedere.

**Team agenti (8):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| IB-COORD-COMMUNITY | Capo Area Community — L2 coordinator | sonnet | Orchestra i 3 WF; gestisce piano community; escalation a ib-director |
| IB-COMM-QA | Verificatore Community — QA area (indipendente) | sonnet | Gate segnali cross-sell (consenso verificato, segnale documentato); gate testimonianze (metriche reali) |
| IB-COMM-ONBOARDER | Onboarding Specialist | haiku | Sequenza benvenuto + attivazione: acquisto → email benvenuto ≤1h → accesso piattaforma ≤24h → primo modulo ≤7gg |
| IB-COMM-HEALTH | Student Health Monitor | haiku | Dashboard salute studente: progress, ultimo accesso, moduli completati; alert abbandono precoce |
| IB-COMM-ENGAGE | Engagement Runner | haiku | Rituali community: prompt discussione settimanale, Q&A pianificati, contenuto bonus, moderazione |
| IB-COMM-RETENTION | Retention Specialist | sonnet | Segnali abbandono → win-back; sequenze recovery; skill `churn-prevention`; mai invasivo |
| IB-COMM-SOCIAL | Social Proof Collector | sonnet | Raccolta testimonianze a milestone di completamento: reale, verificabile, non sollecitata prima del milestone |
| IB-COMM-CROSSSELL | Cross-Sell Scout | sonnet | Scoring segnali "vuole l'implementazione fatta" → handoff contract HC-IB-AG-01 → AGENCY; skill `crosssell-bridge` |

**Workflow CF-grade (3):**

**WF-ONBOARDING-STUDENTE** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: portare ogni acquirente dalla conferma d'ordine al primo modulo completato in ≤7 giorni,
  con esperienza fluida e zero friction tecnica.
- Flusso:
  ```
  T=0:   Acquisto confermato → IB-COMM-ONBOARDER trigger:
         email benvenuto APSOC entro 1h (skill `onboarding`): "ecco cosa ti aspetta, ecco come accedere"
  T≤24h: Accesso piattaforma attivo (formazione-admin); email #2: "il tuo percorso inizia qui"
         GATE: accesso verificato (log da formazione-student); se errore → alert IB-COORD-COMMUNITY
  T≤72h: Email #3: "hai guardato la lezione 1? Ecco cosa imparerai in questa settimana"
         check progress in piattaforma da IB-COMM-HEALTH
  T≤7gg: Se modulo 1 non completato → email gentile di recovery (IB-COMM-RETENTION: "hai bisogno di aiuto?")
  T=7gg: IB-COMM-HEALTH report settimanale: % acquirenti con modulo 1 completato → a IB-COORD-COMMUNITY
  OUTPUT: studente attivato + dati base progress tracciati in piattaforma + `infobusiness/community`
  ```
- State: `company/02-infobusiness/community/onboarding/state.json` — per coorte: n. iscritti, attivati, check milestone.

**WF-COMMUNITY-ATTIVA** [TARGET-V2]
- Scopo: gestire la community come spazio di valore continuativo (WhatsApp/Discord previsto dal catalogo),
  con rituali settimanali, Q&A pianificati, e un ciclo di engagement che riduce il churn passivo.
- Flusso:
  ```
  Cadenza settimanale:
  Lunedì: IB-COMM-ENGAGE → prompt discussione (domanda aperta su applicazione pratica del corso)
  Mercoledì: IB-COMM-ENGAGE → contenuto bonus (snippet, tip, caso d'uso)
  Venerdì: IB-COMM-ENGAGE → Q&A live (30min) o risposta scritta alle top 3 domande della settimana
  Ogni 2 settimane: IB-COMM-SOCIAL → raccolta testimonianza da studente che ha raggiunto milestone
  Ogni mese: IB-COMM-HEALTH → report community: engagement rate, progress medio, segnali abbandono
             → IB-COORD-COMMUNITY → aggiornamento piano contenuti community per il mese successivo
  GATE IB-COMM-QA: nessuna testimonianza pubblicata senza metrica verificata; nessun claim di risultato
  OUTPUT: community attiva; testimonianze raccolte; report mensile; segnali cross-sell identificati
  ```

**WF-CROSSSELL-BRIDGE** [TARGET-V2]
- Scopo: identificare studenti pronti per la versione "fatta per loro" (AGENCY) e gestire il passaggio
  in modo non invasivo, basato su consenso esplicito e segnale documentato.
- Flusso:
  ```
  IB-COMM-CROSSSELL monitora segnali:
  - domande in community tipo "come faccio implementare questo nella mia azienda?"
  - completamento di moduli avanzati (>50% corso completato)
  - richieste dirette "avete qualcuno che lo fa per me?"
  - survey interna con domanda esplicita "sei interessato a un'implementazione personalizzata?"
  → Scoring: segnale identificato (3 pt) + completamento ≥50% (2 pt) + risposta survey positiva (5 pt)
  → Score ≥5: IB-COMM-CROSSSELL prepara dossier {lead_id, fonte_prodotto, segnale, score, consenso}
  GATE IB-COMM-QA: consenso esplicito verificato; segnale documentato; nessun outreach automatico
  → Handoff HC-IB-AG-01 → AGENCY (Acquisizione) con payload completo
  OUTPUT: lead qualificato per AGENCY + handoff documentato + relazione studente intatta
  ```
- State: `company/02-infobusiness/community/crosssell/state.json` — scoring per studente, esiti handoff.

**Namespace memoria area:** `infobusiness/community/` — segnali studenti, progress, testimonianze, lead cross-sell.
**KPI (da misurare):** % acquirenti con onboarding ≤24h; % con modulo 1 completato ≤7gg; % completamento
corso; engagement community (% studenti attivi per settimana); n. cross-sell qualificati per coorte.

---

### IB-L2-STRA — AREA STRATEGIA & INTELLIGENCE [TARGET-V2]

**Missione.** L'area che mancava completamente nel v1. Gestisce il product backlog, monitora trend e
concorrenti, produce la roadmap prodotti basata su dati, e assicura che INFO-BUSINESS si evolva con
il mercato anziché rincorrerlo. Lavora con 08-INTELLIGENCE e alimenta l'Area Prodotto con idee già
pre-validate prima che arrivino a WF-VALIDAZIONE.

**Team agenti (7):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| IB-COORD-STRATEGIA | Capo Area Strategia — L2 coordinator | opus | Roadmap prodotti; analisi competitiva; propone next prodotto a ib-director; escalation se trend cambia |
| IB-STRA-QA | Verificatore Strategia — QA area (indipendente) | sonnet | Gate "prove non inventate": nessuna raccomandazione senza dati; fonti citate; nessuna metrica stimata presentata come reale |
| IB-STRA-INTEL | Market Intelligence Analyst | sonnet | Trend di mercato info-products AI; cosa vendono i competitor; angoli emergenti; ingest da 08-INTELLIGENCE |
| IB-STRA-COMP | Competitor Analyst | sonnet | Audit periodico offerta competitor (corsi, ebook, prezzi, posizionamento); dossier per Director |
| IB-STRA-BACKLOG | Product Backlog Manager | sonnet | Gestisce la coda idee prodotto con score, stato (idea/in-validazione/validato/in-produzione/live), e priorità |
| IB-STRA-ICP | ICP Profiler Info-Business | sonnet | Profilo ICP specifico per i prodotti info (diverso dall'ICP AGENCY); aggiorna con dati da community e lanci |
| IB-STRA-ROADMAP | Roadmap Builder | sonnet | Piano prodotti a 6-12 mesi; dipendenze, sequenza lanci, capacità produzione; rivisto dopo ogni lancio |

**Workflow CF-grade (2):**

**WF-PRODUCT-INTELLIGENCE** [TARGET-V2]
- Scopo: alimentare continuamente il product backlog con idee pre-validate basate su dati di mercato,
  pattern community e gap competitor. L'Area Prodotto non dovrebbe mai cercare idee: le riceve già
  qualificate da questo workflow.
- Flusso:
  ```
  Cadenza mensile (con trigger on-demand per eventi di mercato):
  1. IB-STRA-INTEL → scan trend (fonti: 08-INTELLIGENCE, community, newsletter, social) →
     identifica 3-5 temi emergenti nel mercato info-products AI
  2. IB-STRA-COMP → audit offerta competitor: nuovi prodotti, pricing, posizionamento →
     gap analysis: cosa non offrono che il nostro ICP chiede?
  3. IB-STRA-ICP → aggiorna profilo ICP con dati freschi (domande community, segnali cross-sell,
     obiezioni post-vendita) → pain points non ancora coperti dai prodotti attuali
  4. IB-STRA-BACKLOG → integra risultati → genera bozze idea prodotto con score iniziale /100 →
     top 3 idee proposta a IB-COORD-STRATEGIA
  5. IB-STRA-QA → verifica: fonti citate, dati reali, nessun numero inventato
  6. IB-COORD-STRATEGIA → presenta top idea a ib-director → se approved: entra in WF-VALIDAZIONE (IB-L2-PROD)
  GATE IB-STRA-QA: nessuna idea passa senza fonte reale che la supporta
  OUTPUT: backlog aggiornato + top idea approvata per WF-VALIDAZIONE
  ```
- State: `company/02-infobusiness/strategia/intelligence/state.json`.

**WF-ROADMAP-PRODOTTI** [TARGET-V2]
- Scopo: mantenere una roadmap prodotti a 6-12 mesi coerente con la capacità produttiva e i lanci
  pianificati. Non un documento statico: aggiornato dopo ogni lancio e ogni ciclo intelligence.
- Flusso:
  ```
  Cadenza trimestrale + aggiornamento dopo ogni lancio:
  1. IB-STRA-ROADMAP → import: catalogo prodotti live, backlog validato, capacità area prodotto (lead time),
     calendario lanci pianificati
  2. Sequenziamento: dipendenze prodotto→lancio, buffer tra lanci (≥30gg per lista recovery),
     allineamento con Content Factory per contenuti organici
  3. IB-STRA-ICP → check: i prodotti pianificati coprono ancora i pain point ICP attuali?
  4. IB-COORD-STRATEGIA → presenta roadmap a ib-director → approvazione → store in `infobusiness/strategia`
  GATE: roadmap non presentata senza stima lead time per ogni prodotto; nessun prodotto senza
  gap di ≥30gg dal lancio precedente (lista deve riprendersi)
  OUTPUT: roadmap aggiornata + calendario lanci approvato → guida per tutte e 5 le aree
  ```

**Namespace memoria area:** `infobusiness/strategia/` — backlog idee con score, roadmap, dossier competitor, ICP.
**KPI (da misurare):** n. idee nel backlog per score ≥60; lead time intelligence → idea validata → produzione;
% prodotti a roadmap che arrivano a lancio nei tempi; aggiornamenti ICP per trimestre.

---

## 4. Roster agenti consolidato (mega-reparto)

Convenzione id: `ib-` (director) / `IB-<area>-<ruolo>`. Tier: haiku = meccanico/alto-volume ·
sonnet = analisi/scrittura · opus = ragionamento critico/gate bloccanti/go-no-go.

### IB-DIRECTOR — Direttore Ecosistema INFO-BUSINESS

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| **ib-director** | Direttore INFO-BUSINESS (L1 — riporta a Board C-Suite) | opus | Riceve obiettivi dal Board (COO/CRO-Revenue); smista ai 5 Capi Area; emette go/no-go lancio finale; riporta KPI trimestrali; supervisiona i 5 QA indipendenti; è il solo che può sbloccare escalation di livello L3 |

### Roster completo per area

| Area | ID | Ruolo | Tier |
|---|---|---|---|
| **PRODOTTO (10)** | IB-COORD-PRODOTTO | Capo Area | sonnet |
| | IB-PROD-QA | Verificatore QA (indip.) | sonnet |
| | IB-PROD-VALID | Product Idea Validator | sonnet |
| | IB-PROD-MKD | MKD Forger | sonnet |
| | IB-PROD-CURRIC | Curriculum Architect | sonnet |
| | IB-PROD-WRITER | Lesson Writer | sonnet |
| | IB-PROD-PLATFORM | Platform Integrator | sonnet |
| | IB-PROD-DESIGN | Asset Designer | sonnet |
| | IB-PROD-EBOOK | Ebook Specialist | sonnet |
| | IB-PROD-LEARN | Product Pattern Learner | sonnet |
| **LANCI (9)** | IB-COORD-LANCI | Capo Area | opus |
| | IB-LANC-QA | Verificatore QA (indip.) | opus |
| | IB-LANC-PLANNER | Launch Planner | sonnet |
| | IB-LANC-COPY-LIAISON | Copy Liaison | sonnet |
| | IB-LANC-ASSET | Asset Checker | haiku |
| | IB-LANC-WEBINAR | Webinar Producer | sonnet |
| | IB-LANC-TRACKER | Launch Tracker | haiku |
| | IB-LANC-DEBRIEF | Post-Launch Analyst | sonnet |
| | IB-LANC-DRY | Dry-Run Conductor | sonnet |
| **VENDITE (8)** | IB-COORD-VENDITE | Capo Area | sonnet |
| | IB-VEND-QA | Verificatore QA (indip.) | sonnet |
| | IB-VEND-OFFER | Offer Architect | sonnet |
| | IB-VEND-SALESPAGE | Sales Page Builder | sonnet |
| | IB-VEND-CHECKOUT | Checkout Technician | haiku |
| | IB-VEND-CRO | CRO Analyst | sonnet |
| | IB-VEND-TRACK | Tracking Analyst | haiku |
| | IB-VEND-LEAD | Lead Magnet Specialist | sonnet |
| **COMMUNITY (8)** | IB-COORD-COMMUNITY | Capo Area | sonnet |
| | IB-COMM-QA | Verificatore QA (indip.) | sonnet |
| | IB-COMM-ONBOARDER | Onboarding Specialist | haiku |
| | IB-COMM-HEALTH | Student Health Monitor | haiku |
| | IB-COMM-ENGAGE | Engagement Runner | haiku |
| | IB-COMM-RETENTION | Retention Specialist | sonnet |
| | IB-COMM-SOCIAL | Social Proof Collector | sonnet |
| | IB-COMM-CROSSSELL | Cross-Sell Scout | sonnet |
| **STRATEGIA (7)** | IB-COORD-STRATEGIA | Capo Area | opus |
| | IB-STRA-QA | Verificatore QA (indip.) | sonnet |
| | IB-STRA-INTEL | Market Intelligence Analyst | sonnet |
| | IB-STRA-COMP | Competitor Analyst | sonnet |
| | IB-STRA-BACKLOG | Product Backlog Manager | sonnet |
| | IB-STRA-ICP | ICP Profiler Info-Business | sonnet |
| | IB-STRA-ROADMAP | Roadmap Builder | sonnet |
| **AGENTI WRAPPATI** | formazione-orchestrator | Platform coordinator (esistente) | sonnet |
| [WRAPPA-ESISTENTE] | formazione-database | Schema/dati Supabase (esistente) | sonnet |
| | formazione-admin | Pannello admin iscritti (esistente) | haiku |
| | formazione-student | Progress tracking studente (esistente) | haiku |
| | formazione-design | UI piattaforma (esistente) | sonnet |

**TOTALE: 48 agenti** (43 nuovi da creare via FORGE + 5 esistenti wrappati)
Incluso: 1 director + 5 capi area + 5 QA indipendenti + 32 worker specialisti + 5 agenti formazione-*.

### Topologia swarm (Ruflo)

| Livello | Topologia | Razionale |
|---|---|---|
| INFO-BUSINESS root | hierarchical (ib-director → 5 capi area) | gerarchia a 5 aree |
| Area Prodotto | pipeline (VALID → MKD → CURRIC → WRITER → PLATFORM → DESIGN) | WF-CORSO è sequenziale con gate bloccanti |
| Area Lanci | pipeline (PLANNER → COPY-LIAISON → ASSET → DRY → go/no-go) + star per T+N durante cart open | fase pre-lancio sequenziale; cart open con monitor parallelo |
| Area Vendite | mesh piccolo (OFFER → SALESPAGE ↔ QA ↔ CHECKOUT ↔ TRACK) | iterazione su offerta e copy |
| Area Community | star (COORD → ONBOARDER/HEALTH/ENGAGE/RETENTION paralleli) | studenti gestiti in parallelo |
| Area Strategia | pipeline (INTEL + COMP + ICP → BACKLOG → QA → COORD) | intelligence si integra prima della raccomandazione |
| Go/No-Go lancio | hive-mind consensus (raft) | ib-director + IB-LANC-QA + 3 Sentinel; UN NO = blocco |

---

## 5. Workflow chiave CF-grade — mappa end-to-end

```
[IB-L2-STRA] INTELLIGENCE ──► [IB-L2-PROD] WF-VALIDAZIONE ──► WF-CORSO / WF-EBOOK
                                                                        │
                                                             [IB-L2-VEND] WF-SALESPAGE
                                                                        │
                               [IB-L2-LANC] WF-LANCIO ◄────────────────┘
                                      │
              [IB-L2-COMM] WF-ONBOARDING ◄── acquirenti ──► WF-COMMUNITY-ATTIVA
                                      │
                         WF-CROSSSELL-BRIDGE ──► [01-AGENCY] Acquisizione
                                      │
                          [IB-L2-VEND] WF-FUNNEL-EVERGREEN (gira in parallelo, sempre)
```

| # | Step | Owner WF | Input → Output | Gate |
|---|---|---|---|---|
| 1 | Intelligence e backlog | IB-L2-STRA WF-PRODUCT-INTELLIGENCE | mercato → idea pre-validata | fonte citata; nessun dato inventato |
| 2 | Validazione idea | IB-L2-PROD WF-VALIDAZIONE | idea → brief validato | score ≥60/100 + MVP test |
| 3 | Produzione corso | IB-L2-PROD WF-CORSO | raw → corso live piattaforma | MKD 100%, smoke test verde |
| 4 | Sales page | IB-L2-VEND WF-SALESPAGE | brief → page live + tracking | APSOC ≥80, tracking verde |
| 5 | Lancio orchestrato | IB-L2-LANC WF-LANCIO | T-30 → cart close → debrief | go/no-go consensus unanime |
| 6 | Onboarding studenti | IB-L2-COMM WF-ONBOARDING | acquisto → modulo 1 ≤7gg | accesso ≤24h, log verde |
| 7 | Community attiva | IB-L2-COMM WF-COMMUNITY-ATTIVA | studenti → engagement continuo | rituali cadenza rispettata |
| 8 | Cross-sell AGENCY | IB-L2-COMM WF-CROSSSELL-BRIDGE | segnale studente → lead AGENCY | consenso verificato, score ≥5 |
| 9 | Evergreen continuo | IB-L2-VEND WF-FUNNEL-EVERGREEN | traffico → acquisti H24 | A/B dati reali; scarcity vera |
| 10 | Debrief lancio | IB-L2-LANC WF-DEBRIEF-LANCIO | numeri reali → ReasoningBank | entro T+7; ≥3 pattern |
| 11 | Roadmap aggiornata | IB-L2-STRA WF-ROADMAP-PRODOTTI | lancio chiuso → prossimo pianificato | ogni lancio riaggiorna |

---

## 6. Asset esistenti wrappati (ADR-003 — wrap, mai riscrittura)

Regola: `usa-così` (invariato, solo registrato) · `wrappa` (invariato + interfaccia contract/log) ·
`evolvi` (modifiche pianificate DOPO validazione del wrapper).

| Path (relativo a `Digital Empire/`) | Area v2 | Azione | Marcatura |
|---|---|---|---|
| `Formazzione/Claude code/MANUALE COMPLETO DI CLAUDE CODE PER IL BUSINESS.md/.pdf` (203pp) | IB-L2-PROD (WF-EBOOK) + IB-L2-VEND | **evolvi**: è il prodotto #1; ruolo (lead magnet vs a pagamento) da decidere team-prezzi B-003; packaging finale + offer stack pronto ma SENZA prezzo fino a B-003 | WRAPPA-ESISTENTE |
| `InfoBusiness/CATALOGO PRODOTTI ATTUALE — Info-Bu.md` | IB-L2-STRA (BACKLOG) | **evolvi**: diventa il registro ufficiale prodotti; colmare campi vuoti (prezzo → B-003, metriche → post-lancio) | WRAPPA-ESISTENTE |
| `InfoBusiness/Funnel Unico Perfetto – ....pdf` | IB-L2-VEND (WF-FUNNEL-EVERGREEN) | **ingest**: blueprint del funnel evergreen; estratto in `infobusiness/strategia/` come riferimento; non riscrivere | WRAPPA-ESISTENTE |
| `InfoBusiness/Webinar/` (3 PDF script/apertura) | IB-L2-LANC (WF-WEBINAR) | **evolvi**: base del WF-WEBINAR (template apertura storytelling); ingest via content-forge → MKD → kernel skill `webinar-funnel` | WRAPPA-ESISTENTE |
| `Lancio corso skill beast/processo lancio.txt` | IB-L2-PROD (WF-VALIDAZIONE) | **evolvi**: contiene Product Creation Lab pipeline + scoring ≥60; diventa il kernel di WF-VALIDAZIONE e `idea_scorer.py` | WRAPPA-ESISTENTE |
| `Lancio corso skill beast/Framework_ICRO_Digital_Empire.pdf` | IB-L2-VEND (WF-CRO) | **ingest**: riferimento per IB-VEND-CRO; framework CRO come knowledge layer | WRAPPA-ESISTENTE |
| `Lancio corso skill beast/Leanding Page CCM`, `Page`, `Sale pag`, `smerd` | IB-L2-VEND (WF-SALESPAGE) | **consolida**: audit → UNA sales page canonica per prodotto (WF-SALESPAGE); duplicati in archivio, non cancellati | WRAPPA-ESISTENTE |
| `Lancio corso skill beast/lezione n.1.mp4` | IB-L2-PROD (WF-CORSO) | **usa-così**: lezione pilota esistente → modulo 1 del corso "Vendi la Skill n.1"; riusare senza riscrivere | WRAPPA-ESISTENTE |
| `Lancio corso skill beast/content-carousels.html` | IB-L2-LANC + 03-CONTENT-FACTORY | **wrappa**: caroselli pre-lancio esistenti → handoff CF per aggiornamento brand; non riscrivere | WRAPPA-ESISTENTE |
| `Lanco ebook/Sito- Leanding page` | IB-L2-VEND | **consolida**: landing ebook nel funnel evergreen (opt-in o sales page); audit brand voice; UNA pagina canonica | WRAPPA-ESISTENTE |
| `Formazzione/Agency Scalping/`, `Outreach/`, `Storytelling/`, `Youtube/` + 2 PDF root | IB-L2-PROD (WF-VALIDAZIONE) | **ingest via content-forge**: materia prima per WF-VALIDAZIONE → candidati corsi futuri; niente si cancella | WRAPPA-ESISTENTE |
| `~/.claude/agents/formazione-{orchestrator,database,admin,student,design}.md` | IB-L2-PROD (WF-CORSO) | **wrappa**: arruolati as-is nel roster §4 come team piattaforma; registrati in IDENTITY-HR; zero riscrittura | WRAPPA-ESISTENTE |
| Wiki: `Framework_Cold_Outreach_APSOC` + brand voice guide v2.0 | trasversale (gate copy) | **usa-così**: fonte del gate APSOC ≥80 e del brand gate per ogni area | WRAPPA-ESISTENTE |
| Wiki/knowledge: Thought Leader Funnel + Founder Authority Stack (ingest Beggiato 2026-06-09) | IB-L2-LANC + IB-L2-VEND | **usa-così**: frame strategico pre-lancio e nurture evergreen; knowledge layer per IB-LANC-COPY-LIAISON e IB-VEND-SALESPAGE | WRAPPA-ESISTENTE |

**Nuove skill da forgiare in V2-6 (via 07-FORGE, kernel ≤500 righe + references/):**

| Skill | Scopo | Area |
|---|---|---|
| `course-architect` | Standardizza MKD → curriculum: moduli, outcome misurabili, esercizi, durata; kernel + references/ | IB-L2-PROD |
| `idea-scorer` | Scoring /100 delle 5 dimensioni di un'idea prodotto + logica MVP test | IB-L2-PROD |
| `launch-runbook` | Calendario T-30→T+7 come macchina: genera timeline, checklist asset, gate, dry-run | IB-L2-LANC |
| `webinar-funnel` | Script webinar di vendita (apertura storytelling da PDF esistenti) + replay funnel | IB-L2-LANC |
| `launch-debrief` | Post-mortem strutturato: piano vs reale, root cause, pattern → ReasoningBank | IB-L2-LANC |
| `offer-stack` | Costruzione offerta: value stack, bonus, garanzia, bump/upsell — separata da `pricing` (che decide i numeri) | IB-L2-VEND |
| `student-success` | Playbook onboarding+completamento: milestone, nudge, raccolta testimonianze | IB-L2-COMM |
| `crosssell-bridge` | Criteri e scoring per identificare lead caldi corso→agency + handoff contract standard | IB-L2-COMM |
| `product-intelligence` | Framework analisi mercato info-products: trend, competitor, gap → idea backlog | IB-L2-STRA |
| `ib-roadmap` | Piano prodotti a 6-12 mesi: sequenziamento lanci, dipendenze, capacità | IB-L2-STRA |

**Skill esistenti assegnate (già installate):**

| Skill | Area | Uso |
|---|---|---|
| `content-forge` | IB-L2-PROD | raw → MKD → corso/skill (cuore di WF-CORSO e WF-EBOOK) |
| `launch` + `market-launch` | IB-L2-LANC | playbook lancio + orchestrazione marketing |
| `cro-copy-architect` (APSOC) | IB-L2-LANC + IB-L2-VEND | scrittura e audit ogni copy a conversione; giudice del gate ≥80 |
| `pricing` | IB-L2-VEND | decisione prezzo prodotti (porta i numeri da B-003) |
| `paywalls` | IB-L2-VEND | upgrade path, order bump, upsell |
| `emails` | IB-L2-LANC + IB-L2-COMM | sequenze lancio + nurture + win-back |
| `lead-magnets` | IB-L2-VEND | creazione lead magnet evergreen |
| `signup` + `onboarding` | IB-L2-COMM | opt-in flow + attivazione studente |
| `churn-prevention` | IB-L2-COMM | retention community |
| `referrals` | IB-L2-COMM | passaparola studenti |
| `community-marketing` | IB-L2-COMM | strategia community WhatsApp/Discord |
| `customer-research` + `marketing-psychology` | IB-L2-PROD + IB-L2-STRA | ICP, angoli, leve persuasive |
| `ab-testing` + `cro` + `analytics` | IB-L2-VEND | test funnel + tracking |
| `empire-premium-style` / `site-*` | IB-L2-VEND (con PLATFORM) | build sales page premium |
| `icp-radar` | IB-L2-STRA | crea/aggiorna profili ICP per nicchia |

---

## 7. KPI per area + quality gates

### 7.1 KPI (da misurare — nessun target inventato; baseline = primo ciclo)

| Area | KPI | Definizione operativa |
|---|---|---|
| IB-L2-PROD | Lead time corso | giorni da brief validato → corso live su piattaforma |
| IB-L2-PROD | Tasso gate QA primo giro | % gate superati senza rework al primo tentativo |
| IB-L2-PROD | Tasso validazione idea | % idee presentate che superano score ≥60 + MVP test |
| IB-L2-LANC | Aderenza calendario | % task lancio completati entro la data pianificata (no slittamenti) |
| IB-L2-LANC | Conversione lancio | % lista email → acquisto durante cart open |
| IB-L2-LANC | Piano vs reale | scarto % tra conversione prevista e reale (baseline da primo lancio) |
| IB-L2-VEND | Conversione evergreen | % visitatori sales page → acquisto; % opt-in su traffico |
| IB-L2-VEND | AOV (Average Order Value) | valore medio ordine incluso effetto bump/upsell |
| IB-L2-VEND | A/B hit rate | % test A/B con variante vincente che batte il controllo |
| IB-L2-COMM | Attivazione | % acquirenti che completano modulo 1 entro 7gg |
| IB-L2-COMM | Completamento corso | % studenti che finiscono il corso entro 90gg |
| IB-L2-COMM | Cross-sell rate | n. lead qualificati passati ad AGENCY per coorte / n. acquirenti coorte |
| IB-L2-STRA | Backlog score medio | score medio delle idee nel backlog (segnale di qualità del pipeline idee) |
| IB-L2-STRA | Lead time intelligence → lancio | giorni da idea identificata da Strategia → lancio prodotto |

### 7.2 Quality Gates (bloccanti — "blocca, non suggerisce")

| Gate | Quando | Criterio | Owner |
|---|---|---|---|
| **Gate Validazione Idea** | prima di produrre qualsiasi prodotto | score ≥60/100 + ≥5 "sì, lo comprerei" reali (MVP test) | IB-PROD-QA |
| **Gate Qualità Prodotto** | fine WF-CORSO o WF-EBOOK | 100% atomi fonte coperti; ogni lezione ha outcome verificabile; smoke test studente verde; brand voice conforme | IB-PROD-QA |
| **Gate Copy APSOC** | ogni copy a conversione (page, email, ad) | audit `cro-copy-architect` ≥80/100; sotto 80 = rework obbligatorio, mai pubblica | IB-LANC-QA / IB-VEND-QA |
| **Gate Asset Completo** | T-3 di ogni lancio | checklist 100%: page live, checkout testato, tracking attivo, email caricate, link verificati | IB-LANC-ASSET |
| **Gate Dry-Run + Costi** | T-1 di ogni lancio | simulazione completa OK + budget approvato da Cost-Sentinel + OPERATIONS | IB-LANC-DRY |
| **Gate Go/No-Go Lancio** | T-0 ε prima del cart open | hive-mind consensus unanime: ib-director + IB-LANC-QA + Quality-Sentinel + Brand-Voice-Sentinel + Cost-Sentinel; UN NO blocca | ib-director |
| **Gate Brand ("prove non promesse")** | ogni output esterno | "prove non promesse": zero claim di guadagno non documentati; scarcity solo reale; no dipendency-language | Brand-Voice-Sentinel (trasversale) |
| **Gate Handoff Cross-Sell** | invio lead ad AGENCY | lead consenziente + segnale documentato + score ≥5 + profilo {lead_id, fonte, segnale, score, consenso} | IB-COMM-QA |
| **Gate Testimonianza** | pubblicazione di ogni case study o quote | metriche verificabili; confermata per iscritto dallo studente; nessun risultato approssimato | IB-COMM-QA |
| **Gate Intelligenza Fonti** | ogni raccomandazione strategica | fonte citata e verificabile; nessun dato stimato presentato come reale | IB-STRA-QA |

---

## 8. Memoria / namespace

**Namespace AgentDB** (prefisso `infobusiness/`):

| Namespace | Contenuto | Area owner |
|---|---|---|
| `infobusiness/catalogo` | stato prodotti, ruolo (lead magnet/a pagamento), offer stack, prezzi approvati B-003 | IB-L2-STRA |
| `infobusiness/prodotto` | MKD, curriculum, decisioni di prodotto, smoke test log, gate status | IB-L2-PROD |
| `infobusiness/lanci` | calendari, copy approvati, numeri reali per lancio, debrief | IB-L2-LANC |
| `infobusiness/funnel` | configurazione evergreen, esiti test A/B, metriche step funnel | IB-L2-VEND |
| `infobusiness/community` | progress studenti, segnali abbandono, testimonianze, scoring cross-sell | IB-L2-COMM |
| `infobusiness/strategia` | backlog idee con score, roadmap, dossier competitor, ICP aggiornato | IB-L2-STRA |
| `infobusiness/intel` | report trend mercato, audit competitor, note intelligence da 08-INTELLIGENCE | IB-L2-STRA |
| `infobusiness/reasoningbank` | pattern distillati dai debrief: errori → regole; un entry per lancio entro T+7 | IB-LANC-DEBRIEF |
| `infobusiness/kpi` | metriche per area per ciclo (alimenta dashboard) | ib-director |

**Regole operative:**
- `aidefence_has_pii` prima di ogni store in `infobusiness/community` (dati studenti).
- Dry-run obbligatorio (pattern 3 — Piano Maestro) su ogni WF prima di ogni run reale con investimento.
- Ogni workflow: `state.json` + trace per ogni esecuzione (test amnesia: ripartibile a freddo).
- Indici a 2 livelli: `infobusiness/INDEX.md` (aree) + `infobusiness/<area>/INDEX.md` (per area).
- ReasoningBank: ogni fallimento/pattern distillato entro T+7 dall'evento.
- `infobusiness/catalogo`: campi prezzo NON compilati fino ad approvazione B-003 — mai placeholder numerico.
- `neural_train` sui pattern di conversione SOLO dopo ≥3 lanci reali (non prima: regola "niente training su dati inventati").

---

## 9. Build plan V2-6 (ordine fasi, con gate)

Allineato a V2-6 del Piano Maestro (§10). Ogni fase: ciclo a 9 passi (ADR-006); passo 5-bis REVIEW
MAXIMILIAN attivo da V2-3.

| Fase | Cosa si costruisce | Gate di validazione |
|---|---|---|
| **B0 — Inventario** | Tabella §6 verificata file per file: ogni asset mappato all'area e all'azione (usa-così / wrappa / evolvi / consolida). Registrazione agenti `formazione-*` in IDENTITY-HR. | Zero asset orfani; catalogo senza campi vuoti tranne prezzi (attendono B-003) |
| **B1 — Scaffolding struttura** | `company/02-infobusiness/` con 5 aree come strutture-cartella: BACKBONE.md, agenti/ (placeholder schede millimetriche), workflow/, principi/, scripts/, state/ | Struttura navigabile Explorer; verify Empire verde; cartelle create |
| **B2 — Team-prezzi + catalogo** | B-003 eseguito: ib-director + team-prezzi propongono prezzi → Max approva → catalogo aggiornato con prezzi reali. Risoluzione B-002 (ruolo Manuale Claude Code). | Catalogo senza campi vuoti (inclusi prezzi); ADR-005 B-002/B-003 chiusi |
| **B3 — WF-VALIDAZIONE live** | Area Prodotto: IB-PROD-VALID + `idea_scorer.py` + gate /100 operativo. Prima validazione su 3 idee da backlog reale. | 3 idee processate; almeno 1 PASS e 1 FAIL con log corretto |
| **B4 — WF-CORSO: "Vendi la Skill n.1"** | WF-CORSO end-to-end: content-forge → MKD → curriculum → lesson writer → piattaforma (formazione-* wrappati) | Smoke test studente fantasma verde; corso accessibile su piattaforma reale |
| **B5 — WF-SALESPAGE + WF-FUNNEL-EVERGREEN minimo** | Area Vendite: sales page con offer stack (prezzi da B2) + opt-in page + sequenza nurture (5 email) + checkout + tracking | Percorso end-to-end cliccabile; gate copy ≥80; eventi tracciati in debug; APSOC ≥80 |
| **B6 — WF-LANCIO: primo lancio orchestrato** | Area Lanci: WF-LANCIO su "Vendi la Skill n.1"; calendario T-30→T+7 reale; handoff a MARKETING/CF reali; dry-run; go/no-go | Gate F6 Piano Maestro: lancio eseguito con tutti i gate verdi; debrief scritto |
| **B7 — WF-ONBOARDING + WF-COMMUNITY** | Area Community: WF-ONBOARDING-STUDENTE live per coorte lancio B6; WF-COMMUNITY-ATTIVA con rituali settimanali | % onboarding ≤24h ≥90%; almeno 1 sessione community erogata |
| **B8 — WF-CROSSSELL + WF-STRATEGIA** | Area Community: WF-CROSSSELL-BRIDGE; Area Strategia: WF-PRODUCT-INTELLIGENCE + WF-ROADMAP-PRODOTTI | Primo handoff HC-IB-AG-01 → AGENCY con payload completo; roadmap Q3 approvata |
| **B9 — Auto-miglioramento** | WF-DEBRIEF-LANCIO → ReasoningBank → aggiornamento skill/agenti via FORGE; WF-CRO-OTTIMIZZAZIONE attivo | Entry ReasoningBank con ≥3 pattern; almeno 1 skill arricchita da dati reali lancio |

**Ordine vincolante:**
- B2 (prezzi) prima di B5 (funnel con prezzi reali) — mai costruire un checkout su prezzi placeholder.
- B4 (corso su piattaforma) prima di B6 (lancio) — non si lancia un corso che non esiste in piattaforma.
- B6 (primo lancio) prima di B7 (onboarding coorte reale) — l'onboarding serve studenti reali.

---

## 10. Rischi specifici + mitigazioni

| Rischio | Mitigazione |
|---|---|
| **Prodotto senza decisioni commerciali** (prezzo B-002, ruolo lead magnet/pagamento B-003 aperti) | B2 è bloccante: nessun funnel va live senza catalogo completo con prezzi approvati; `pricing` + `offer-stack` con decision scritta e datata da team-prezzi |
| **Lancio su lista fredda/inesistente** — il funnel organico non è ancora costruito | B5 (evergreen + lead magnet) prima di B6; il primo lancio dimensiona le attese sulla lista reale, non su numeri ipotetici; nessun target di vendita inventato nel piano |
| **Copy hype che brucia il brand** (mercato "guru" saturo) | Doppio gate: APSOC ≥80 + Brand-Voice-Sentinel; gate "prove non promesse" bloccante; scarcity solo reale; IB-LANC-QA a opus per massima severità |
| **Dipendenza dai lanci (revenue a denti di sega)** | WF-FUNNEL-EVERGREEN come area dedicata (IB-L2-VEND), non ripiego post-lancio; KPI evergreen tracciati in parallelo ai KPI lancio |
| **Frammentazione asset** (4+ versioni di landing in `Lancio corso skill beast/`) | B0 consolida: UNA pagina canonica per prodotto; duplicati in archivio datato; wiki-first come fonte di verità (ADR-002) |
| **Piattaforma corso incompleta al lancio** | Gate B4 (smoke test studente) obbligatorio e bloccante prima del go/no-go B6; fallback dichiarato nel dry-run: delivery via link protetti se piattaforma non pronta |
| **Cross-sell invadente rompe fiducia studenti** | Gate handoff: solo segnale esplicito + consenso; scoring ≥5; mai outreach automatico; IB-COMM-QA valida ogni handoff; relazione studente sempre prioritaria |
| **Costi orchestrazione lancio (Opus + swarm)** | Opus solo per ib-director, IB-COORD-LANCI, IB-LANC-QA; haiku per funzioni meccaniche (tracker, asset-checker, onboarder); dry-run con stima costi a T-1; Cost-Sentinel con potere di NO |
| **Area Strategia che inventa trend** (rischio dossier non fondati) | IB-STRA-QA bloccante: nessuna raccomandazione senza fonte verificabile; gate "prove non inventate" applicato a ogni output strategico |
| **Mancanza di WF-WEBINAR experience** | Template esistenti in `InfoBusiness/Webinar/` come base provata; IB-LANC-WEBINAR parte da lì, non da zero; primo webinar con dry-run tecnico 48h prima |
| **Conoscenza di lancio che evapora** | `launch-debrief` obbligatorio entro T+7; pattern in ReasoningBank `infobusiness/reasoningbank`; nessun lancio "chiuso" senza debrief scritto e validato da IB-LANC-QA |
| **Swarm che muore sul limite crediti durante build** | Build a lotti idempotenti (ADR-006); naming Title-Case fisso; checkpoint STATO-EMPIRE dopo ogni fase; budget-guard <20% risorse sessione → commit immediato (lezione CP-005) |
| **Agenti formazione-* non allineati allo standard V2** | Wrappati as-is per ora (ADR-003); le schede millimetriche V2 vengono create come interfaccia esterna; la riscrittura interna solo dopo validazione del wrapper |

---

## Connessioni

- [[11-PIANO-V2-DIRETTIVA-SCALA]] §2 + §7 — la direttiva che governa questo dossier e lo standard mega-reparto
- [[02-ECOSISTEMA-INFOBUSINESS]] — il v1 (riferimento per asset reali, handoff base, workflow v1)
- [[01-ECOSISTEMA-AGENCY-V2]] — destinatario lead caldi cross-sell via HC-IB-AG-01; eguaglia questo livello come esempio di dossier v2
- [[00-PIANO-MAESTRO]] — architettura holding, 13 pattern non negoziabili, roadmap F6; gate F6 = B6 di questo dossier
- [[12-DOSSIER-MAXIMILIAN]] — review 5-bis attiva da V2-3; standard di giudizio
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] — enforcement Articoli 1-7 su ogni output esterno; "prove non promesse" (Art.2) è gate trasversale
- `04-ECOSISTEMA-MARKETING.md` — fornitore copy/email (gate APSOC): HC-IB-MK-01
- `03-ECOSISTEMA-CONTENT-FACTORY.md` — fornitore moduli video e contenuti pre-lancio: HC-CF-IB-01 / HC-IB-CF-01
- `06-ECOSISTEMA-PLATFORM.md` — piattaforma corso (Supabase + Next.js), checkout, deploy: HC-PL-IB-01
- `07-ECOSISTEMA-FORGE.md` — crea team/skill quando un KPI cala per 2 cicli; forgia 10 skill nuove elencate in §6
- `08-ECOSISTEMA-INTELLIGENCE.md` — fornisce trend, customer research, pattern ReasoningBank: HC-IN-IB-01
- `09-ECOSISTEMA-OPERATIONS.md` — scheduling run, cost guard, approvazione budget lancio: HC-OP-IB-01
- `company/Memory/maximilian-corpus/direttiva-20260611-scala-v2.md` — standard di scala: "Il reparto Info Business è enorme, deve essere come un'azienda intera"
- ADR-007 (pivot V2) · ADR-006 (ciclo 9 passi + 5-bis) · ADR-005 (B-002/B-003 BACKLOG — prezzi e ruolo Manuale Claude Code) · ADR-003 (wrap, non riscrittura) · ADR-002 (memory-first, wiki-first)
