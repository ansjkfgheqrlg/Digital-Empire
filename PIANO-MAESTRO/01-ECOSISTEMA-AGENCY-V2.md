# 🏢 01 — ECOSISTEMA AGENCY V2 (Digital Empire Group)

> Dossier v2 (V2-2, ADR-007) — amplia il v1 `01-ECOSISTEMA-AGENCY.md` a scala CF-grade. Fonte: 11-PIANO-V2 §2.
>
> Questo dossier SUPERA il v1 dove in conflitto con la direttiva di scala. Il v1 resta riferimento per i cap
> reali, gli asset esistenti e la topologia del funnel — qui tutto viene portato a standard CF-grade: ogni reparto
> è un'organizzazione con team 6-10 agenti + workflow propri. Standard di un workflow fatto bene = Content Factory
> Exponium (corpus Maximilian 2026-06-11, riga 41-42: "io lo paragono a UN workflow. Quello è lo standard.").
>
> Versione: 2.0 · Creato: 2026-06-16 · Fase: V2-2 (dossier architetturali) · Build effettiva: V2-6 (reparti v2).
> Stato: PROGETTATO — l'architettura target v2 è qui descritta. Ciò che wrappa asset esistenti è marcato
> [WRAPPA-ESISTENTE]; ciò che è interamente nuovo è marcato [TARGET-V2].

---

## 0. Missione + DONE WHEN

**Missione.** AGENCY acquisisce e serve clienti delle 3 implementazioni AI di Digital Empire —
**Outreach Factory €4.000 · Content Factory €3.500 · Second Brain €2.500 · bundle Engine Room €8.000** —
con modello one-time, €0 canoni, codice di proprietà del cliente, setup in ≤7 giorni, supporto 90 giorni.
Posizionamento: **"l'agenzia progettata per essere licenziata"** (Mandato Art.1).

AGENCY è il pilastro revenue della holding: tutto il resto di EMPIRE OS lo alimenta o lo amplifica.
A livello V2, AGENCY è un'organizzazione a pieno titolo — non un set di script wrappati ma una struttura
gerarchica con reparti che sono essi stessi organizzazioni, workflow CF-grade, team di agenti millimetrici
e cicli di auto-miglioramento continuo.

**DONE WHEN — la build V2-6 di AGENCY è completa quando:**

1. I 10 reparti L2 esistono in `company/01-agency/` ognuno come struttura-cartella con: `BACKBONE.md`,
   cartella `agenti/` (6-10 schede millimetriche), cartella `workflow/` (1-5 WF CF-grade), `principi/`,
   `scripts/`, `kpi/`, `state/`.
2. I 4 workflow outreach esistenti (email/LinkedIn/Instagram/reply) girano INVARIATI ma wrappati come
   team L3 con handoff contract, log in `agency/outreach` e dry-run disponibile. Zero regressioni.
3. I 4 reparti TARGET-V2 (Account Management, Closing, Partnership, QA-Cliente) esistono con team 6-10
   agenti e almeno 1 workflow CF-grade operativo ciascuno.
4. Il flusso end-to-end lead→outreach→call→preventivo→contratto→delivery→supporto 90gg→testimonianza
   è percorribile, tracciato e orchestrato dal sistema (ogni step: owner agente, gate, record in AgentDB).
5. Dashboard KPI per tutti e 10 i reparti visibile e alimentata da dati reali (evoluzione di `outreach-dashboard-premium`).
6. ReasoningBank riceve ogni fallimento (bounce, preventivo perso, delivery ritardata, ticket SLA violato)
   come pattern distillato — loop chiuso.
7. Review MAXIMILIAN (passo 5-bis, da V2-3) ha approvato l'architettura: "abbastanza grande? millimetrica?
   si vede nell'Explorer?"

**OUT OF SCOPE (v2):** aumento dei cap outreach senza dati reali; nuovi prodotti/pricing; automazione
della discovery call (resta umana: Max); riscrittura della pipeline email attiva prima che il wrapper sia validato.

---

## 1. Posizione nella holding — input/output verso gli altri 9 ecosistemi

AGENCY è il nodo di monetizzazione centrale della holding. Tutti gli altri ecosistemi o la alimentano
(generano lead, asset, tooling, intelligence) o vengono alimentati da essa (revenue → budget operativo).
Ogni passaggio è un **handoff contract** `{from, to, payload, acceptance_criteria}` sul BUS corporativo.

Il v1 documenta i 16 handoff contract attivi (HC-AG-IB-01 … HC-AG-OP-01): restano validi e sono
riportati per intero in `01-ECOSISTEMA-AGENCY.md §1`. In questa sezione v2 si aggiungono i flussi
nuovi che i 4 reparti TARGET-V2 introducono.

### Nuovi handoff contract V2

| Contract | Da → A | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-AG-AM-01` | AGENCY (Delivery) → A7 Account Mgmt | `{client_id, prodotto, milestone, contatti_referenti}` alla firma contratto | profilo cliente aperto in `agency/clients`; KAM assegnato |
| `HC-AG-CL-01` | AGENCY (Acquisizione) → A8 Closing | `{lead_id, call_transcript, dossier_pre-call, preventivo_id}` dopo risposta positiva | preventivo inviato; slot call chiusura proposto |
| `HC-AG-PT-01` | AGENCY → A9 Partnership | `{lead_non-icp, settore, motivo_esclusione}` quando un lead qualificato non rientra nei 3 prodotti DE | lead taggato; consenso contatto valido; nessun dato PII nudo |
| `HC-AG-QC-01` | AGENCY (Delivery/Supporto) → A10 QA-Cliente | `{client_id, delivery_id, UAT_checklist}` dopo Gate Delivery | QA indipendente assegnato; checklist firmata |
| `HC-PT-AG-01` | A9 Partnership → AGENCY | `{referral_lead, partner_id, commission_rate}` quando un partner invia un prospect | profilo ICP precompilato; fonte tracciata |
| `HC-MK-AG-02` | 04 MARKETING → A8 Closing | script di chiusura ottimizzato (APSOC, obiezioni post-preventivo) | passato Copy/APSOC Guild + gate Bibbia |

**Regola invariata:** AGENCY non produce contenuti marketing grandi né tooling in-house — li
richiede via contract. Produce in-house solo ciò che è quotidiano e operativo (reparti A1→A10, sez. 2).

---

## 2. Reparti L2 v2 — la lista al rialzo

Il v1 aveva 6 reparti (A1-A6). La direttiva §2.3 richiede l'aggiunta minima di: Account Management &
Supporto, Closing/Sales-call, Partnership, QA-Cliente. Analizzando la pipeline revenue completa, la lista
v2 porta AGENCY a **10 reparti L2**, ognuno organizzazione a sé:

| ID | Nome | Tipo | Razionale v2 |
|---|---|---|---|
| A1 | Ricerca & Market Intelligence | WRAPPA-ESISTENTE + TARGET-V2 | già in v1; team e workflow CF-grade da scalare a 6-10 agenti |
| A2 | Acquisizione / Outreach | WRAPPA-ESISTENTE + TARGET-V2 | pipeline esistente; wrapper CF-grade + 2 WF nuovi |
| A3 | Preventivi | WRAPPA-ESISTENTE + TARGET-V2 | flusso parziale in v1; 5 workflow a regime |
| A4 | Delivery & Implementazione | WRAPPA-ESISTENTE + TARGET-V2 | playbook esistenti; aggiungere QA delivery e multi-tenant CF-grade |
| A5 | Copywriting Interno | WRAPPA-ESISTENTE | in v1; scala a team 6 + workflow refresh |
| A6 | Marketing Interno & Proof | WRAPPA-ESISTENTE | in v1; scala a team 6 + workflow case-study CF-grade |
| A7 | Account Management & Customer Success | TARGET-V2 | mancava in v1; gestisce relazione post-firma → upsell |
| A8 | Closing / Sales-Call | TARGET-V2 | mancava in v1; il gap tra preventivo e contratto era non presidiato |
| A9 | Partnership & Referral | TARGET-V2 | mancava in v1; lead non-ICP e lead da partner non avevano casa |
| A10 | QA-Cliente & Audit Qualità | TARGET-V2 | mancava in v1; il gate Delivery era in A4 senza indipendenza |

### A1 — RICERCA & MARKET INTELLIGENCE [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Alimentare il funnel con lead qualificati e dare a Closing/Preventivi/Delivery
l'intelligence di nicchia per vendere e consegnare meglio. In v2: team di 9 agenti, 3 workflow CF-grade.

**Team agenti (9):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A1-COORD | Coordinatore Ricerca — lead del reparto | sonnet | Orchestra i 3 workflow; decide priorità nicchie; riporta ad AG-DIR |
| AG-A1-QA | Verificatore Dati — QA del reparto | sonnet | Valida score ICP, freschezza dati, conformità GDPR-light; blocca lead incompleti |
| AG-A1-SCRAPE | Runner scraper multi-fonte | haiku | Esegue Maps/Apify/Outscraper/Google; log per fonte in `agency/leads` |
| AG-A1-EXTRACT | Estrattore strutturato | haiku | Trasforma raw HTML/JSON in schede lead (nome, email, telefono, sito, settore) |
| AG-A1-QUAL | Qualificatore ICP | sonnet | Score lead vs ICP corrente; triage: qualificato / nurture / scarta |
| AG-A1-ICP | ICP Profiler per nicchia | sonnet | Crea/aggiorna profili ICP (skill `icp-radar`) per nicchia; alimenta A9 |
| AG-A1-COMP | Analista Competitor/Audit | sonnet | Dossier competitor per prospect (competitor.py, cro_audit.py, market-audit) |
| AG-A1-INTEL | Analista di mercato | sonnet | Trend di nicchia, report per Acquisizione e Preventivi; sourcing da 08-INTELLIGENCE |
| AG-A1-BRIEF | Brief pre-call preparer | sonnet | Aggrega dossier lead+competitor+ICP prima della discovery call per A8-Closing |

**Workflow CF-grade (3):**

**WF-LEAD-SOURCING** [WRAPPA-ESISTENTE]
- Scopo: scraping multi-fonte → estrazione → qualifica → caricamento in `leads.db` + `agency/leads`
- Flusso: AG-A1-SCRAPE (fonti parallele: Maps / Apify / Outscraper / Google) → AG-A1-EXTRACT →
  AG-A1-QUAL (score ICP) → AG-A1-QA (gate: completezza dati ≥80%, no duplicati) → store in `agency/leads`
- Gate: qualifier score ≥ soglia per nicchia corrente; AG-A1-QA blocca se dati incompleti
- Script: `scraper/*.py`, `extractor.py`, `qualifier.py` [WRAPPA-ESISTENTE]
- State: `agency/01-ricerca/sourcing/state.json` — ogni run tracciata (fonte, n. lead raw, n. qualificati, errori)

**WF-MARKET-INTEL** [TARGET-V2]
- Scopo: monitorare nicchie attive, competitor, trend e produrre report per A2/A3/A8
- Flusso: AG-A1-INTEL (ricerca trend) + AG-A1-COMP (audit competitor per prospect specifico) →
  AG-A1-ICP (aggiorna profilo ICP nicchia) → AG-A1-QA (verifica fonti citate) → report in `agency/intel`
- Cadenza: settimanale per report nicchia; on-demand per audit prospect
- Gate: fonti citate e verificabili (ADR-002: wiki-first); nessuna metrica inventata (Mandato Art.2)
- Output: `{nicchia, trend, competitor_top3, ICP_aggiornato, opportunita}` → ingest in 08-INTELLIGENCE

**WF-BRIEF-PRE-CALL** [TARGET-V2]
- Scopo: produrre dossier pre-call per Max prima di ogni discovery (A8 Closing lo richiede)
- Flusso: AG-A1-BRIEF aggrega → lead score (da sourcing) + audit problema (competitor.py, cro_audit.py) +
  ICP match + contesto nicchia → documento PDF/MD strutturato → consegnato ad A8 ≥2h prima della call
- Gate: dossier consegnato prima della call; nessun campo "da compilare" vuoto

**Namespace memoria:** `agency/01-ricerca/` — leads, score, ICP per nicchia, dossier pre-call, report intel.
**KPI:** lead qualificati/gg; % qualifica su scraped; freschezza dati media; dossier pre-call entro SLA.

---

### A2 — ACQUISIZIONE / OUTREACH [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Convertire lead qualificati in discovery call prenotate su 3 canali, dentro i cap reali.
CTA standard: **presentazione-empire.vercel.app**. In v2: team di 10 agenti, 4 workflow CF-grade.
La pipeline email esistente gira INVARIATA — il wrapper la avvolge senza toccare il runtime.

**Team agenti (10):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A2-COORD | Coordinatore Acquisizione | sonnet | Orchestra i 4 WF; priorità canali; riporta ad AG-DIR |
| AG-A2-QA | Verificatore Bibbia — QA del reparto | sonnet | Il gate Bibbia: 3 check sequenziali su ogni messaggio; blocca, non suggerisce |
| AG-A2-STRAT | Strategist angolo di attacco | sonnet | Angolo APSOC per lead specifico (strategist.py, insight.py) [WRAPPA] |
| AG-A2-WRITE | Writer APSOC messaggi | sonnet | Scrittura/variazione copy (writer.py, humanizer.py, copy_knowledge.py) [WRAPPA] |
| AG-A2-SEND | Sender + rate limiter | haiku | Invio + cap (≤500/gg email, cap 100/h); log in `agency/outreach` [WRAPPA] |
| AG-A2-TRIAGE | Triage risposte | haiku | Classifica: interessato / obiezione / no / out-of-office (skill `outreach-reply-triage`) |
| AG-A2-FUP | Follow-up writer | sonnet | Sequenze multi-touch; non risponde ai "no" (followup_writer) [WRAPPA] |
| AG-A2-LI | Operatore LinkedIn | haiku | 20 connessioni + 20 messaggi + 30 commenti/gg (scripts 01→05 + comment_posts.py) [WRAPPA] |
| AG-A2-IG | Operatore Instagram | haiku | 30 DM/gg, pattern 2 messaggi (corpo + link) + follow-up [WRAPPA] |
| AG-A2-BOOK | Booking coordinator | sonnet | Da "interessato" → proposta slot call → conferma → passaggio ad A8-Closing |

**Workflow CF-grade (4):**

**WF-OUTREACH-EMAIL** [WRAPPA-ESISTENTE — RUNTIME INTOCCABILE]
- Scopo: email fredde a lead qualificati (≤500/gg, cap 100/h); CTA: presentazione-empire.vercel.app
- Flusso: AG-A2-STRAT → AG-A2-WRITE → AG-A2-QA (gate Bibbia, 3 check) → AG-A2-SEND → log `agency/outreach`
- Gate BLOCCANTE: Gate Bibbia (bibbia_team.py). Blocca se: no APSOC, no CTA corretta, dipendency-language
- Runtime: orchestrator.py, run.py, run_500.py, batch_send.py [WRAPPA — zero modifiche fino a validazione wrapper]
- State: `agency/02-acquisizione/email/state.json` — ogni batch: n. inviati, bounce, gate pass/fail

**WF-OUTREACH-LINKEDIN** [WRAPPA-ESISTENTE]
- Scopo: 20 connessioni + 20 messaggi + 30 commenti/gg; max engagement su profili target
- Flusso: AG-A2-LI esegue scripts 01→05 + comment_posts.py → log + triage risposta → AG-A2-TRIAGE
- Gate: cap giornalieri non superabili; commenti umani (pattern umanizzazione); nessun invio in bulk non approvato
- State: `agency/02-acquisizione/linkedin/state.json`

**WF-OUTREACH-INSTAGRAM** [WRAPPA-ESISTENTE]
- Scopo: 30 DM/gg, pattern 2 messaggi (corpo + link presentazione), follow-up automatico
- Flusso: AG-A2-IG → DM → attesa risposta → follow-up → triage (AG-A2-TRIAGE)
- Gate: cap 30/gg; no doppio DM se già risposto; PII-scan prima di store conversazione

**WF-REPLY-BOOKING** [TARGET-V2 — evolve il WF-REPLY-FOLLOWUP del v1]
- Scopo: da risposta positiva a call discovery prenotata (passaggio ad A8-Closing)
- Flusso: AG-A2-TRIAGE (classifica risposta) → se "interessato": AG-A2-FUP gestisce conversazione →
  AG-A2-BOOK propone slot → conferma → `HC-AG-CL-01` ad A8 + `HC-AG-AM-01` ad A7 (anagrafica aperta)
- Gate: nessuna risposta a "no" definitivo; nessun passaggio ad A8 senza slot confermato
- State: `agency/02-acquisizione/reply/state.json` — thread per lead, stato triage, esito

**Namespace memoria:** `agency/02-acquisizione/` — template attivi, performance per variante, esiti Bibbia,
thread risposte (PII-scan prima di ogni store: `aidefence_has_pii`).
**KPI:** inviati/gg per canale; reply rate; positive reply rate; call prenotate/settimana.
**Cap reali (invariati):** email ≤500/gg cap 100/h · LI 20 conn+20 msg+30 commenti/gg · IG 30 DM/gg.

---

### A3 — PREVENTIVI [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Trasformare ogni discovery call in una proposta problem-first inviata entro 48h,
con pricing a catalogo (mai sconti improvvisati), che vende l'autonomia del cliente. In v2: team di
8 agenti, 3 workflow CF-grade. Il flusso beat-preventivi + proposal-gate già in v1 viene portato a
struttura CF-grade con state, trace e loop di apprendimento.

**Team agenti (8):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A3-COORD | Coordinatore Preventivi | opus | Orchestra il WF-PREVENTIVO; riporta ad AG-DIR; approva invio finale |
| AG-A3-QA | Verificatore Gate — QA del reparto | opus | Gate Preventivo (skill `proposal-gate`): blocca se non conforme; mai suggerisce solo |
| AG-A3-BRIEF | Discovery Brief Builder | sonnet | Trascrizione/appunti call → brief strutturato (skill `discovery-call-brief`) |
| AG-A3-AUDIT | Problem Auditor | sonnet | Quantifica il problema cliente (market-audit, cro_audit.py) |
| AG-A3-PROP | Proposal Writer | opus | Costruisce preventivo problem-first (skill `beast-preventivi` + market-proposal) |
| AG-A3-PRICE | Pricing Configurator | haiku | Seleziona prodotto/bundle a catalogo fisso; mai sconto non autorizzato |
| AG-A3-FUP | Follow-up commerciale | sonnet | Sequenza follow-up post-invio: 3 touch in 10gg → esito (win/loss) |
| AG-A3-LEARN | Pattern Learner | sonnet | Registra ogni win/loss con causa in `agency/reasoning`; alimenta ReasoningBank |

**Workflow CF-grade (3):**

**WF-PREVENTIVO** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: da brief call a proposta inviata entro 48h; flusso lineare con gate finale bloccante
- Flusso: AG-A3-BRIEF (brief strutturato) → AG-A3-AUDIT (quantifica problema) →
  AG-A3-PROP (preventivo problem-first) → AG-A3-PRICE (prodotto/bundle catalogo) →
  AG-A3-QA (Gate Preventivo — BLOCCA se non conforme) → AG-A3-COORD (approva invio) → invio
- Gate BLOCCANTE: Gate Preventivo (skill `proposal-gate`). Controlla: problema apre il doc;
  awareness level corretto; solo pricing catalogo; promesse = prove verificabili; scope 7gg;
  clausola proprietà codice + €0 canoni; supporto 90gg; brand voice.
- State: `agency/03-preventivi/state.json` — ogni preventivo: id, lead, prodotto, esito gate, data invio

**WF-FOLLOWUP-COMMERCIALE** [TARGET-V2]
- Scopo: presidio dei 10gg dopo invio preventivo; 3 touch non invasivi; chiusura win/loss
- Flusso: AG-A3-FUP (D+3 primo touch, D+7 secondo, D+10 terzo) → esito → se win: `HC-AG-AM-01` ad A7
  + contratto; se loss: AG-A3-LEARN registra motivo → `HC-AG-IN-01` ad 08-INTELLIGENCE
- Gate: nessun touch invasivo; rispetto dei segnali "no"; motivo loss SEMPRE registrato

**WF-LOSS-ANALYSIS** [TARGET-V2]
- Scopo: analisi strutturata di ogni preventivo perso per migliorare la pipeline
- Flusso: AG-A3-LEARN aggrega loss ultimi 30gg → pattern (prezzo? scope? competitor?) →
  report mensile → ad A5 (aggiorna libreria obiezioni) + a 08-INTELLIGENCE
- Gate: almeno 5 loss per pattern significativo; nessuna conclusione su n < 3

**Namespace memoria:** `agency/03-preventivi/` — preventivi: stato, win/loss, motivi, patterns.
**KPI:** tempo call→preventivo (target ≤48h); win rate; valore medio preventivo; loss pattern mensile.
**Pricing fisso:** Outreach Factory €4.000 / Content Factory €3.500 / Second Brain €2.500 / Engine Room €8.000.

---

### A4 — DELIVERY & IMPLEMENTAZIONE [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Consegnare i 3 prodotti in ≤7 giorni sul server del cliente — non in locale,
non in staging: **sul server del cliente**, con la sua macchina, con i suoi dati. Training incluso.
Handover: il cliente deve poter licenziare DE. In v2: team di 9 agenti, 4 workflow CF-grade.

**Team agenti (9):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A4-COORD | Coordinatore Delivery | opus | Orchestra le delivery attive; riporta ad AG-DIR; decide rollback se giorno-1 ambiente fallisce |
| AG-A4-QA | Verificatore Delivery — QA del reparto | sonnet | Gate Delivery: UAT checklist firmata; autonomia cliente verificata; nessuna dipendenza residua |
| AG-A4-ENV | Env Setup | sonnet | Verifica prerequisiti ambiente cliente (OS, Python, permessi, rete); installazione; secrets |
| AG-A4-TENANT | Config Multi-tenant | sonnet | Iniezione `brand_kit` + `icp` cliente in ogni workflow (pattern 11 multi-tenant) |
| AG-A4-UAT | UAT Runner | sonnet | Run di accettazione con il cliente; checklist UAT firmabile; log esito |
| AG-A4-TRAIN | Training Kit Builder | sonnet | Materiale: video walkthrough, runbook operativo, FAQ cliente; skill `delivery-playbook` |
| AG-A4-HAND | Handover Pack Builder | sonnet | Pacchetto: codice completo, README, credenziali, licenza d'uso; skill `client-handover` |
| AG-A4-SUPP | Support Triage 90gg | haiku | Classificazione ticket (bug/domanda/fuori scope); SLA; check proattivo settimanale |
| AG-A4-LEARN | Delivery Pattern Learner | sonnet | Ogni delivery → pattern (ambienti critici, errori ricorrenti) → `agency/reasoning` |

**Workflow CF-grade (4):**

**WF-DELIVERY-OUTREACH-FACTORY** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: clonare + parametrizzare la pipeline outreach DE sul server cliente in ≤7gg
- Flusso: G+0 Verifica ambiente (AG-A4-ENV) → G+1 Setup repo + secrets → G+2 Iniezione brand_kit+icp
  (AG-A4-TENANT) → G+3-4 Test run su campione piccolo → G+5 Training (AG-A4-TRAIN) → G+6 UAT con cliente
  (AG-A4-UAT) → G+7 Handover (AG-A4-HAND) + Gate Delivery (AG-A4-QA)
- Gate BLOCCANTE: Gate Delivery. Controlla: workflow girante sul server cliente (non DE); run reale passata;
  training erogato; handover pack completo; UAT firmata; cliente ha eseguito 1 run da solo in UAT

**WF-DELIVERY-CONTENT-FACTORY** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: setup motore Content Factory parametrizzato sul server cliente
- Flusso: richiesta `HC-AG-CF-01` a 03-CONTENT-FACTORY → ricezione motore → stesso schema G+0→G+7
- Gate: come WF-DELIVERY-OUTREACH-FACTORY + QA-Cliente (A10) indipendente post-UAT

**WF-DELIVERY-SECOND-BRAIN** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: setup vault + skill Second Brain sul sistema cliente
- Flusso: richiesta template a 08-INTELLIGENCE (`HC-IN-AG-01`) → configurazione vault → training workflow
  memory-first → UAT → handover
- Gate: cliente naviga autonomamente il vault dopo training; nessuna dipendenza da credenziali DE

**WF-SUPPORTO-90GG** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: supporto post-handover per 90 giorni; obiettivo decrescente di ticket (cliente sempre più autonomo)
- Flusso: intake ticket (AG-A4-SUPP triage) → classificazione → fix (se bug) / risposta (se domanda) /
  "fuori scope" (se nuovo feature) → log + SLA → check proattivo settimanale → report a A7-Account Mgmt
- Gate: SLA rispettato (risposta ≤24h bug, ≤48h domanda); nessun ticket chiuso senza conferma cliente;
  a 90gg: review con A7, proposta upsell da A6

**Namespace memoria:** `agency/04-delivery/` — delivery attive/chiuse, checklist UAT, ambienti, ticket 90gg.
**KPI:** giorni delivery (target ≤7); UAT pass primo giro; ticket risolti in SLA; NPS fine 90gg.

---

### A5 — COPYWRITING INTERNO [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Copy operativo quotidiano dell'agency (template email/DM, micro-copy preventivi, script call)
con framework APSOC. I pezzi grandi si chiedono a 04-MARKETING. In v2: team di 6 agenti, 2 workflow.

**Team agenti (6):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A5-COORD | Coordinatore Copy | sonnet | Orchestra i 2 WF; priorità refresh; riporta ad AG-DIR |
| AG-A5-QA | Verificatore Gate Bibbia | sonnet | Gate Bibbia applicato all'output di A5 (stesso gate di A2, riusato — pattern 6) |
| AG-A5-WRITE | APSOC Writer | sonnet | Scrittura/variazione copy (skill `cro-copy-architect`, market-copy) |
| AG-A5-OBJ | Objection Librarian | sonnet | Libreria obiezioni reali (da `HC-AG-IN-01`) → risposte testate con prove reali |
| AG-A5-SCRIPT | Script Writer Call | sonnet | Script per discovery call e call di chiusura (per A8-Closing) |
| AG-A5-LEARN | Copy Performance Analyst | sonnet | Analizza reply rate per template → suggerisce varianti → alimenta `agency/outreach` |

**Workflow CF-grade (2):**

**WF-COPY-REFRESH** [TARGET-V2 — evolve WF-COPY-OUTREACH del v1]
- Scopo: refresh periodico template 3 canali basato su dati reali di performance
- Flusso: AG-A5-LEARN analizza reply rate ultimi 30gg → AG-A5-WRITE produce 3 varianti per canale →
  AG-A5-QA (gate Bibbia) → rollout graduale (10% leads) → confronto A/B → adozione o scarto
- Gate: ogni variante passa Gate Bibbia prima del test; nessun rollout universale senza dati A/B

**WF-SCRIPT-CALL** [TARGET-V2]
- Scopo: script discovery call e script chiusura per Max (consegnato ad A8-Closing)
- Flusso: AG-A5-OBJ (obiezioni attese per nicchia) + AG-A5-SCRIPT (struttura script APSOC) →
  AG-A5-QA (verifica: no claim senza proof, no dependency-language) → consegna ad A8
- Gate: brand voice conforme; "prove non promesse" verificato (Mandato Art.2)

**Namespace memoria:** `agency/05-copy/` — template attivi, performance per variante, libreria obiezioni.
**KPI:** % copy passato Gate Bibbia primo giro; reply rate media varianti; tempo brief→copy.

---

### A6 — MARKETING INTERNO & PROOF [WRAPPA-ESISTENTE + TARGET-V2]

**Missione.** Vetrina e prova sociale dell'agency: landing, presentazione, case study, testimonianze.
Genera inbound e munizioni per outreach e preventivi. In v2: team di 6 agenti, 3 workflow CF-grade.

**Team agenti (6):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A6-COORD | Coordinatore Marketing Interno | sonnet | Orchestra i 3 WF; coordina con 04-MARKETING e 06-PLATFORM |
| AG-A6-QA | Verificatore Brand Gate | sonnet | Gate brand: no claim senza proof; conformità Mandato Art.1-2 su ogni asset pubblico |
| AG-A6-PROOF | Proof Collector | haiku | Raccolta testimonianze/metriche reali a fine 90gg ("prove non promesse") |
| AG-A6-CASE | Case Study Writer | sonnet | Scrittura case study APSOC (skill `case-study-forge`) |
| AG-A6-UPSELL | Upsell Mapper | sonnet | Matrice cliente→offerta successiva (skill `upsell-mapper`); attiva SOLO dopo Gate Delivery + NPS positivo |
| AG-A6-INBOUND | Inbound Analyst | sonnet | Traccia lead da inbound (landing/presentazione); misura tasso conversione; suggerisce ottimizzazioni ad AG-A6-COORD |

**Workflow CF-grade (3):**

**WF-CASE-STUDY** [WRAPPA-ESISTENTE + TARGET-V2]
- Scopo: ogni delivery chiusa → case study APSOC pubblicato con metriche reali del cliente
- Flusso: AG-A6-PROOF raccoglie testimonianza + metriche (dopo 90gg) → AG-A6-CASE scrive (skill
  `case-study-forge`) → AG-A6-QA (gate: solo metriche verificate, no claim inventati) →
  richiesta asset a 03-CONTENT-FACTORY (`HC-AG-CF-01`) → pubblicazione su landing
- Gate: metriche verificate dal cliente; nessun numero approssimato; brand voice conforme

**WF-ASSET-VETRINA** [WRAPPA-ESISTENTE]
- Scopo: manutenzione `agency-empire-landing` + presentazione-empire.vercel.app
- Flusso: AG-A6-COORD identifica gap (caso studio mancante, social proof da aggiornare) →
  ticket ad AG-A6-CASE o a 06-PLATFORM (`HC-AG-PL-01`) → review AG-A6-QA → deploy
- Gate: ogni modifica della landing passa Brand Gate (Sentinel Brand-Voice); deploy solo via 06-PLATFORM

**WF-UPSELL-REFERRAL** [TARGET-V2]
- Scopo: mappare cliente verso offerta successiva (singolo prodotto → Engine Room €8.000 → referral)
- Flusso: AG-A6-UPSELL attivato da A7-Account Mgmt (segnale: 90gg finiti + NPS ≥8) →
  mappa prodotto attuale → proposta next → se no upsell: referral ask → AG-A3-COORD per preventivo
- Gate: mai upsell durante supporto attivo; solo su segnale positivo; referral ask = solo dopo review positiva

**Namespace memoria:** `agency/06-marketing/` — case study, asset landing, upsell proposals, lead inbound.
**KPI:** case study per cliente chiuso; call da inbound; testimonianze raccolte; referral generati.

---

### A7 — ACCOUNT MANAGEMENT & CUSTOMER SUCCESS [TARGET-V2]

**Missione.** Presidiare la relazione con il cliente dalla firma del contratto fino al termine del supporto 90gg
e oltre (upsell, referral, reingaggio). Il v1 aveva questo gap: nessuno era proprietario della relazione post-firma.
Il cliente veniva "consegnato" e poi non aveva più un interlocutore strutturato. In v2: team di 7 agenti, 2 workflow.

**Team agenti (7):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A7-COORD | KAM Lead (Key Account Manager) | sonnet | Assegnato a ogni cliente alla firma; proprietario della relazione; riporta ad AG-DIR |
| AG-A7-QA | Verificatore Customer Success | sonnet | Controlla SLA ticket (A4), milestone delivery, NPS; segnala rischi a AG-A7-COORD |
| AG-A7-ONBOARD | Onboarding Specialist | sonnet | Prima settimana post-firma: introduce il cliente al processo, spiega le milestone |
| AG-A7-MID | Mid-Point Reviewer | sonnet | Check a metà delivery (G+3-4): clima cliente, eventuali aggiustamenti di scope |
| AG-A7-CLOSE | Closure Manager | sonnet | Fine 90gg: NPS survey, raccolta feedback, proposta upsell/referral → passaggio ad A6 |
| AG-A7-HEALTH | Account Health Monitor | haiku | Dashboard salute cliente: milestone, ticket aperti, NPS trend, rischio churn; alert automatici |
| AG-A7-COMM | Comunicatore Cliente | sonnet | Drafta comunicazioni formali (aggiornamenti milestone, notifiche anomalie) su voce di Max |

**Workflow CF-grade (2):**

**WF-CUSTOMER-LIFECYCLE** [TARGET-V2]
- Scopo: presidiare ogni cliente dalla firma al termine dei 90gg con touchpoint strutturati
- Flusso: G+0 Onboarding (AG-A7-ONBOARD presenta processo) → ogni settimana AG-A7-HEALTH monitora →
  G+3 Mid-point review (AG-A7-MID) → G+7 Gate Delivery (check con A10-QA) → settimane 2-12 supporto
  (ticket via A4, AG-A7-COORD supervisiona) → G+90 Closure (AG-A7-CLOSE + NPS + upsell/referral)
- Gate: NPS raccolto entro G+90; milestone loggate; nessun cliente senza KAM assegnato

**WF-RETENTION-ALERT** [TARGET-V2]
- Scopo: intercettare rischi di churn PRIMA che diventino perdita del cliente
- Flusso: AG-A7-HEALTH monitora segnali (ticket multipli aperti, risposta lenta, NPS intermedio ≤6) →
  alert ad AG-A7-COORD → azione correttiva (check call, fix urgente, coinvolgimento Max se necessario)
- Gate: alert entro 24h da segnale; azione registrata in `agency/clients`

**Namespace memoria:** `agency/07-account/` — anagrafica clienti, milestone, NPS, alert, touchpoint log.
**KPI:** NPS medio fine 90gg; % clienti con upsell/referral attivato; SLA ticket rispettato (da A4).

---

### A8 — CLOSING / SALES-CALL [TARGET-V2]

**Missione.** Presidiare il momento più critico della pipeline revenue: la call di chiusura tra invio del
preventivo e firma del contratto. Il v1 aveva questo gap: da "preventivo inviato" a "contratto firmato"
non c'era struttura — era tutto su Max senza supporto. In v2: team di 7 agenti, 2 workflow CF-grade.

**Team agenti (7):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A8-COORD | Coordinatore Closing | opus | Gestisce il pipeline post-preventivo; riporta ad AG-DIR; prepara Max per ogni call |
| AG-A8-QA | Verificatore Prep Call | sonnet | Controlla che il dossier pre-call sia completo prima di passarlo a Max |
| AG-A8-PREP | Call Preparation Specialist | opus | Aggrega: preventivo, dossier lead (da A1), obiezioni attese (da A5), script (da A5) |
| AG-A8-OBJ | Obiezioni Anticipatore | sonnet | Simula le domande/obiezioni che il prospect farà; prepara Max con risposte a prova |
| AG-A8-SCRIPT | Script Coach | sonnet | Personalizza lo script standard (da A5) per il prospect specifico e il prodotto |
| AG-A8-DEBRIEF | Post-Call Analyst | sonnet | Dopo call Max: raccoglie esito, obiezioni emerse, motivazione → log + pattern learner |
| AG-A8-LEARN | Closing Pattern Learner | sonnet | Analizza win/loss call di chiusura; pattern → ad A5 per script e A3 per preventivi |

**Workflow CF-grade (2):**

**WF-CLOSING-PREP** [TARGET-V2]
- Scopo: preparare Max per ogni call di chiusura con tutto il necessario
- Flusso: `HC-AG-CL-01` da A2 → AG-A8-PREP aggrega dossier lead + preventivo + ICP +
  AG-A8-OBJ (obiezioni attese) + AG-A8-SCRIPT (script personalizzato) → AG-A8-QA (gate:
  dossier completo ≥2h prima call) → consegnato a Max
- Gate: dossier consegnato entro SLA; nessun campo vuoto; script conforme Brand Voice (Mandato Art.2)

**WF-CLOSING-DEBRIEF** [TARGET-V2]
- Scopo: apprendere da ogni call di chiusura (win o loss) per migliorare la pipeline
- Flusso: post-call Max → AG-A8-DEBRIEF raccoglie esito + motivazioni → se win: attiva `HC-AG-AM-01`
  ad A7 + contratto; se loss: AG-A8-LEARN registra pattern → ad A3 (WF-LOSS-ANALYSIS) + a 08-INTELLIGENCE
- Gate: debrief completato entro 2h dalla call; motivo SEMPRE registrato (win o loss)

**Namespace memoria:** `agency/08-closing/` — pipeline post-preventivo, dossier prep call, esiti, script libreria.
**KPI:** tasso conversione preventivo→contratto; tempo preventivo→firma; pattern obiezioni ricorrenti.

---

### A9 — PARTNERSHIP & REFERRAL [TARGET-V2]

**Missione.** Presidiare i lead che non rientrano nei 3 prodotti DE (lead non-ICP) e costruire un
ecosistema di partner che inviano referral. Il v1 non aveva questa casa: lead non-ICP andavano persi.
In v2: team di 6 agenti, 2 workflow CF-grade.

**Team agenti (6):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A9-COORD | Coordinatore Partnership | sonnet | Gestisce relazioni partner; riporta ad AG-DIR |
| AG-A9-QA | Verificatore Partner Gate | sonnet | Controlla che i referral entrino con profilo ICP compilato; no lead freddi |
| AG-A9-QUALIFY | Lead Non-ICP Router | sonnet | Riceve lead non-ICP da A2; valuta: partner potenziale / lead nurture / archivio |
| AG-A9-OUTREACH | Partner Outreach | sonnet | Contatta potenziali partner (agenzie complementari, consulenti); proposta referral |
| AG-A9-MGMT | Partner Relationship Manager | sonnet | Mantiene la relazione con partner attivi; aggiornamenti, commissioni, report |
| AG-A9-INTEL | Partnership Intelligence | haiku | Monitora referral ricevuti, tasso conversione per partner, commissioni maturate |

**Workflow CF-grade (2):**

**WF-PARTNER-ONBOARDING** [TARGET-V2]
- Scopo: identificare + onboardare partner complementari (agenzie no-AI, consulenti HR, commercialisti)
- Flusso: AG-A9-QUALIFY identifica candidati da lead non-ICP o da ricerca proattiva (A1) →
  AG-A9-OUTREACH contatta → accordo referral (commissione fissa da catalogo, mai improvvisata) →
  AG-A9-MGMT registra in `agency/partners` → briefing sul prodotto DE
- Gate: accordo scritto prima dell'invio lead; commissione in linea con catalogo; partner briefato su ICP

**WF-REFERRAL-PIPELINE** [TARGET-V2]
- Scopo: gestire ogni lead che arriva da partner (HC-PT-AG-01) fino alla chiusura
- Flusso: lead da partner (`HC-PT-AG-01`) → AG-A9-QA (verifica ICP compilato) →
  se ICP match: passa ad A2 (fast-track outreach) o direttamente ad A8 (se già caldo) →
  AG-A9-INTEL traccia conversione → commissione a partner
- Gate: nessun lead partner senza ICP compilato; nessuna commissione senza contratto firmato

**Namespace memoria:** `agency/09-partnership/` — profili partner, accordi, referral tracciati, commissioni.
**KPI:** lead da referral/mese; tasso conversione referral vs outreach diretto; commissioni maturate.

---

### A10 — QA-CLIENTE & AUDIT QUALITÀ [TARGET-V2]

**Missione.** Garantire che ogni delivery passi una review indipendente PRIMA che il cliente firmi l'UAT.
Il v1 non aveva QA indipendente: il Gate Delivery era in A4 (chi consegna si auto-valuta). In v2: team
di 6 agenti separato da A4, 2 workflow CF-grade.

**Team agenti (6):**

| ID | Ruolo | Tier | Funzione |
|---|---|---|---|
| AG-A10-COORD | QA Lead | opus | Assegna reviewer per ogni delivery; riporta ad AG-DIR (non ad A4-Coord: indipendenza) |
| AG-A10-REVIEW | Delivery Reviewer | sonnet | Verifica che il workflow giri sul server cliente; testa ogni componente |
| AG-A10-UAT | UAT Facilitator | sonnet | Facilitatore dell'UAT: guida il cliente nei test, verifica comprensione |
| AG-A10-BRAND | Brand Compliance Checker | sonnet | Verifica che il brand_kit cliente sia iniettato correttamente in tutti gli output |
| AG-A10-HANDOVER | Handover Completeness Checker | sonnet | Verifica che il pacchetto handover sia completo: README, codice, credenziali, licenza |
| AG-A10-LEARN | Quality Pattern Learner | sonnet | Pattern di difetti ricorrenti → `agency/reasoning` → A4 e FORGE per miglioramenti |

**Workflow CF-grade (2):**

**WF-QA-DELIVERY** [TARGET-V2]
- Scopo: review indipendente di ogni delivery prima di Gate Delivery formale
- Flusso: richiesta `HC-AG-QC-01` da A4 → AG-A10-COORD assegna team → AG-A10-REVIEW testa workflow
  sul server cliente → AG-A10-BRAND verifica brand_kit → AG-A10-HANDOVER verifica pacchetto →
  AG-A10-UAT facilita UAT cliente → AG-A10-COORD emette: PASS o FAIL con lista difetti
- Gate: PASS solo se: workflow gira in autonomia sul server cliente; UAT completata; handover completo;
  nessuna dipendenza da credenziali DE; cliente ha eseguito 1 run autonoma

**WF-QUALITY-AUDIT** [TARGET-V2]
- Scopo: audit mensile della qualità complessiva delle delivery e del supporto
- Flusso: AG-A10-LEARN campiona delivery ultimi 30gg → AG-A10-REVIEW analizza pattern difetti →
  AG-A10-COORD produce report → ad AG-DIR (per A4, A5, A7) + a 07-FORGE se gap strutturale
- Gate: audit cadenza mensile; report condiviso entro 5gg da fine mese

**Namespace memoria:** `agency/10-qa/` — review delivery, difetti, pattern qualità, audit mensili.
**KPI:** % delivery PASS al primo review; difetti per categoria; tempo QA (dal `HC-AG-QC-01` alla risposta).

---

## 3. Roster agenti consolidato

Convenzione id: `AG-<reparto>-<ruolo>`. Tier: haiku = meccanico/alto-volume · sonnet = analisi/scrittura ·
opus = ragionamento critico/gate bloccanti.

**AG-DIR** — Direttore Ecosistema AGENCY (riporta a Board C-Suite): coordinator · opus. Supervisiona tutti
i 10 coordinatori di reparto; gestisce handoff verso altri ecosistemi; presidio KPI globali; coordina con
COO/CEO nelle decisioni cross-ecosistema.

| Reparto | N. Agenti | Ruoli chiave |
|---|---|---|
| A1 Ricerca | 9 | COORD(sonnet), QA(sonnet), SCRAPE(haiku), EXTRACT(haiku), QUAL(sonnet), ICP(sonnet), COMP(sonnet), INTEL(sonnet), BRIEF(sonnet) |
| A2 Acquisizione | 10 | COORD(sonnet), QA(sonnet), STRAT(sonnet), WRITE(sonnet), SEND(haiku), TRIAGE(haiku), FUP(sonnet), LI(haiku), IG(haiku), BOOK(sonnet) |
| A3 Preventivi | 8 | COORD(opus), QA(opus), BRIEF(sonnet), AUDIT(sonnet), PROP(opus), PRICE(haiku), FUP(sonnet), LEARN(sonnet) |
| A4 Delivery | 9 | COORD(opus), QA(sonnet), ENV(sonnet), TENANT(sonnet), UAT(sonnet), TRAIN(sonnet), HAND(sonnet), SUPP(haiku), LEARN(sonnet) |
| A5 Copywriting | 6 | COORD(sonnet), QA(sonnet), WRITE(sonnet), OBJ(sonnet), SCRIPT(sonnet), LEARN(sonnet) |
| A6 Marketing | 6 | COORD(sonnet), QA(sonnet), PROOF(haiku), CASE(sonnet), UPSELL(sonnet), INBOUND(sonnet) |
| A7 Account Mgmt | 7 | COORD(sonnet), QA(sonnet), ONBOARD(sonnet), MID(sonnet), CLOSE(sonnet), HEALTH(haiku), COMM(sonnet) |
| A8 Closing | 7 | COORD(opus), QA(sonnet), PREP(opus), OBJ(sonnet), SCRIPT(sonnet), DEBRIEF(sonnet), LEARN(sonnet) |
| A9 Partnership | 6 | COORD(sonnet), QA(sonnet), QUALIFY(sonnet), OUTREACH(sonnet), MGMT(sonnet), INTEL(haiku) |
| A10 QA-Cliente | 6 | COORD(opus), REVIEW(sonnet), UAT(sonnet), BRAND(sonnet), HANDOVER(sonnet), LEARN(sonnet) |
| **TOTALE** | **75** | (incluso AG-DIR) |

**Topologia swarm (Ruflo):**

| Reparto | Topologia | Razionale |
|---|---|---|
| AGENCY root | hierarchical (AG-DIR → 10 coordinator) | gerarchia a 10 reparti |
| A1 Ricerca | star (COORD → scraper/extractor/qualifier/intel paralleli) | fan-out su fonti indipendenti |
| A2 Acquisizione | pipeline (STRAT→WRITE→QA→SEND) + star per 3 canali | pipeline email sequenziale; canali paralleli |
| A3 Preventivi | pipeline (BRIEF→AUDIT→PROP→PRICE→QA) | flusso lineare con gate finale |
| A4 Delivery | hierarchical (COORD + team giornaliero per delivery attiva) | un delivery = progetto multi-giorno |
| A5 Copy | mesh piccolo (WRITE↔OBJ↔SCRIPT↔QA) | iterazione su varianti |
| A6 Marketing | star | task indipendenti a bassa frequenza |
| A7 Account Mgmt | star + pipeline per lifecycle | touchpoint pianificati + alert paralleli |
| A8 Closing | pipeline (PREP→OBJ→SCRIPT→QA) | preparazione sequenziale call |
| A9 Partnership | star | partner indipendenti |
| A10 QA | pipeline (REVIEW→BRAND→HANDOVER→UAT) | checklist sequenziale |

---

## 4. Workflow chiave CF-grade — la pipeline revenue v2

```
[A1] LEAD ──► [A2] OUTREACH (3 canali) ──► [A2] REPLY/BOOKING ──► [A8] CLOSING PREP ──► CALL (MAX)
                                                                                              │
   [A6] PROOF+UPSELL ◄── [A7] ACCOUNT MGMT ◄── [A10] QA-DELIVERY ◄── [A4] DELIVERY ≤7GG ◄─┘
         │
   [A3] PREVENTIVO ──► [A8] DEBRIEF ──► CONTRATTO
```

| # | Step | Owner | Input → Output | Gate |
|---|---|---|---|---|
| 1 | Sourcing & qualifica | A1 WF-LEAD-SOURCING | fonti → lead qualificato in leads.db + agency/leads con score | Gate QA: completezza + score ICP |
| 2 | Brief pre-call | A1 WF-BRIEF-PRE-CALL | lead qualificato → dossier competitor+ICP+audit | Consegnato ≥2h prima call |
| 3 | Outreach multicanale | A2 (3 WF) | lead → messaggi inviati (cap reali invariati) | Gate Bibbia BLOCCANTE |
| 4 | Reply & booking | A2 WF-REPLY-BOOKING | risposta → call prenotata → HC-AG-CL-01 ad A8 | Slot confermato |
| 5 | Prep chiusura | A8 WF-CLOSING-PREP | lead+preventivo+obiezioni → dossier Max | Dossier completo ≤SLA |
| 6 | Discovery call | MAX (umano) + A3-BRIEF | call → trascrizione/appunti → brief strutturato | Brief entro 4h da call |
| 7 | Preventivo | A3 WF-PREVENTIVO | brief → proposta problem-first inviata ≤48h | Gate Preventivo BLOCCANTE |
| 8 | Followup commerciale | A3 WF-FOLLOWUP-COMMERCIALE | preventivo inviato → 3 touch in 10gg | No touch invasivo |
| 9 | Call chiusura | MAX (umano) + A8 prep | call chiusura → win o loss | Debrief entro 2h |
| 10 | Contratto | MAX + T-pricing-config | win → firma + pagamento one-time | Pagamento verificato; scope congelato |
| 11 | Onboarding cliente | A7 WF-CUSTOMER-LIFECYCLE | firma → KAM assegnato; cliente introdotto al processo | Profilo aperto in agency/clients |
| 12 | Delivery ≤7gg | A4 WF-DELIVERY-* | setup sul server cliente → run test → training → handover | Gate Delivery (A10 indipendente) |
| 13 | QA indipendente | A10 WF-QA-DELIVERY | review terza parte → PASS o FAIL con difetti | PASS richiesto per UAT |
| 14 | UAT e Gate Delivery | A4 + A10 | UAT con cliente → firma checklist | UAT firmata; autonomia dimostrata |
| 15 | Supporto 90gg | A4 WF-SUPPORTO-90GG + A7 | ticket → fix → check settimanale | SLA rispettato; KPI decrescenti |
| 16 | Closure + upsell/referral | A7 WF-CUSTOMER-LIFECYCLE chiusura + A6 WF-UPSELL-REFERRAL | NPS + proposta next → upsell o referral | NPS raccolto; "prove non promesse" su ogni upsell |

Ogni step: fallimento → record in `agency/reasoning` con causa distillata. Loop chiuso.

---

## 5. Asset esistenti wrappati (ADR-003 — wrap, mai riscrittura)

Regola: `usa-così` (invariato, solo registrato) · `wrappa` (invariato + interfaccia contract/log) · `evolvi`
(modifiche pianificate DOPO validazione del wrapper).

| Path | Reparto v2 | Azione |
|---|---|---|
| `Outreach/Outreach Workflow/` (run.py, orchestrator.py, agents/: scraper, qualifier, strategist, writer, bibbia_team, sender, reply_monitor, followup_writer) | A1 + A2 | **wrappa** come WF-LEAD-SOURCING + WF-OUTREACH-EMAIL + WF-REPLY-BOOKING [RUNTIME INTOCCABILE] |
| `Outreach/Outreach Workflow/leads.db` | A1 (storage via 09-OPS) | **usa-così** + backup schedulato (`HC-AG-OP-01`) |
| `Outreach/LinkedIn Automation/` (01→05 + comment_posts.py) | A2 | **wrappa** come WF-OUTREACH-LINKEDIN |
| `Outreach/Instagram Automation/` | A2 | **wrappa** come WF-OUTREACH-INSTAGRAM |
| `Outreach/outreach-dashboard-premium/` (Next.js + API) | A2 + tutti + Observability | **evolvi**: da dashboard outreach a dashboard KPI 10 reparti (build via 06-PLATFORM) |
| `Agenti/Agency/orchestrator/` (AGENT.md, run.py, run_500.py, batch_send.py) | A2 | **wrappa** dentro AG-A2-COORD |
| `Agenti/Agency/sub-agents/` (ai-implementation, cro-funnel, no-website) | A1 + A3 | **evolvi**: profili → AG-A1-ICP / AG-A3-AUDIT |
| `Agenti/Agency/outreach/rules/` (01_ricerca_no_sito…06_ricerca_ai_prospects) | A1 + A2 | **usa-così** (knowledge layer dei team) |
| `Agenti/Agency/skills/` (15 skill market-*) | A5 + A6 + A3 | **usa-così** |
| `agency-empire-landing/` | A6 (build: 06-PLATFORM) | **usa-così / evolvi** (case study quando arrivano) |
| presentazione-empire.vercel.app | A6 | **usa-così** (CTA standard di ogni canale outreach) |
| Skill `beast-preventivi` | A3 | **usa-così** (cuore di AG-A3-PROP) |
| Skill `agency-scalping` (129 file) | tutti i reparti | **usa-così** (knowledge layer trasversale) |
| Skill `cold-email` | A2 + A5 | **usa-così** |
| Skill `market-proposal`, `market-audit` | A3 + A1 | **usa-così** |
| Skill `cro-copy-architect` (APSOC) | A5 + A6 | **usa-così** |
| Script `script_chiamata_freddo.md`, `genera_tabella_chiamate.py` | A8 (call prep) | **evolvi** dentro AG-A8-PREP + WF-CLOSING-PREP |
| Skill `discovery-call-brief` | A3 | **usa-così** (AG-A3-BRIEF) |
| Skill `proposal-gate` | A3 | **usa-così** (AG-A3-QA) |
| Skill `delivery-playbook` | A4 | **usa-così** (AG-A4-TRAIN) |
| Skill `client-handover` | A4 | **usa-così** (AG-A4-HAND) |
| Skill `outreach-reply-triage` | A2 | **usa-così** (AG-A2-TRIAGE) |
| Skill `icp-radar` | A1 | **usa-così** (AG-A1-ICP) |
| Skill `case-study-forge` | A6 | **usa-così** (AG-A6-CASE) |
| Skill `upsell-mapper` | A6 | **usa-così** (AG-A6-UPSELL) |
| Skill `support-90` | A4 | **usa-così** (AG-A4-SUPP) |

**Nuove skill da forgiare in V2-6 (via 07-FORGE, kernel ≤500 righe, references/ per il dettaglio):**

| Skill | Scopo | Reparto |
|---|---|---|
| `account-lifecycle` | gestione touchpoint KAM dalla firma ai 90gg + NPS survey | A7 |
| `closing-prep` | aggregazione dossier chiusura + script personalizzato per Max | A8 |
| `partner-agreement` | template accordo referral + calcolo commissione da catalogo | A9 |
| `qa-delivery-gate` | checklist QA indipendente (A10): componenti, brand_kit, handover, UAT | A10 |
| `loss-analysis` | analisi strutturata preventivi persi: pattern obiezioni, competitore, prezzo | A3 |

---

## 6. KPI per reparto + quality gates

**Principio:** nessun target inventato. I CAP sono reali (attivi). I TASSI si misurano dal giorno 1
e diventano baseline. La FORGE interviene quando un KPI cala per 2 cicli consecutivi (ADR-007).

| Reparto | KPI (misurare, non inventare) | Cap/vincolo reale |
|---|---|---|
| A1 Ricerca | lead qualificati/gg; % qualifica su scraped; freschezza dati; dossier pre-call nel SLA | — |
| A2 Acquisizione | inviati/gg per canale; reply rate; positive reply rate; call prenotate/sett | email ≤500/gg cap 100/h · LI 20+20+30/gg · IG 30 DM/gg |
| A3 Preventivi | tempo call→preventivo (target ≤48h); win rate; valore medio; loss pattern mensile | pricing fisso a catalogo |
| A4 Delivery | giorni delivery (target ≤7); UAT pass primo giro; ticket SLA rispettato | setup ≤7gg + 90gg supporto |
| A5 Copywriting | % copy passato Gate Bibbia primo giro; reply rate media varianti; tempo brief→copy | — |
| A6 Marketing | case study per cliente chiuso; call da inbound; testimonianze raccolte; referral | — |
| A7 Account Mgmt | NPS medio fine 90gg; % clienti con upsell/referral; SLA ticket rispettato | — |
| A8 Closing | tasso conversione preventivo→contratto; tempo preventivo→firma; pattern obiezioni | — |
| A9 Partnership | lead da referral/mese; tasso conversione referral; commissioni maturate | — |
| A10 QA-Cliente | % delivery PASS al primo review; difetti per categoria; tempo QA | — |

**Quality gates (pattern 4 — niente esce senza gate):**

1. **Gate Bibbia** [ESISTENTE, `bibbia_team.py`] — ogni messaggio outreach prima dell'invio (A2) e ogni copy
   interno (A5). Blocca se: no APSOC, no CTA corretta, dependency-language, claim non verificati. *Blocca, non suggerisce.*
2. **Gate Preventivo** [skill `proposal-gate`, A3] — prima dell'invio di ogni proposta. Verifica: problema apre
   il documento; awareness level corretto; pricing solo a catalogo; promesse = prove verificabili; scope 7gg;
   proprietà codice + €0 canoni; supporto 90gg; brand voice. *Blocca, non suggerisce.*
3. **Gate Delivery A4** [dentro `delivery-playbook`, A4] — verifica che il workflow giri SUL SERVER CLIENTE;
   run reale passata; training erogato; handover pack completo; UAT firmata.
4. **Gate QA Indipendente A10** [skill `qa-delivery-gate`, A10] — review separata da A4 (chi consegna non
   si auto-valuta). PASS prima che l'UAT venga firmata. *Gate nuovo in v2: colma il gap del v1.*
5. **Gate Brand** [Sentinel Brand-Voice, corporativo] — trasversale su tutto l'output esterno. "Prove non promesse."
6. **Gate Partner** [AG-A9-QA] — nessun lead referral senza ICP compilato; nessuna commissione senza contratto.

---

## 7. Memoria / namespace

**Namespace AgentDB** (prefisso `agency/`):

| Namespace | Contenuto | Reparto owner |
|---|---|---|
| `agency/leads` | lead, score, stato funnel (specchio semantico leads.db, non sostituto) | A1 |
| `agency/intel` | report nicchie, dossier competitor, aggiornamenti ICP | A1 |
| `agency/outreach` | template attivi, performance per variante, esiti Bibbia, batch log | A2 |
| `agency/conversations` | thread risposta, obiezioni, esiti triage (PII-scan prima di ogni store) | A2 |
| `agency/proposals` | preventivi: stato, win/loss, motivi distillati | A3 |
| `agency/closing` | pipeline post-preventivo, dossier prep call, script, esiti call | A8 |
| `agency/clients` | anagrafica clienti, prodotto, brand_kit, icp, milestone, KAM assegnato | A7 |
| `agency/delivery` | checklist UAT, ambienti, ticket 90gg | A4 |
| `agency/qa` | review delivery, difetti, pattern qualità | A10 |
| `agency/partners` | profili partner, accordi, referral tracciati, commissioni | A9 |
| `agency/kpi` | metriche per reparto per ciclo (alimenta dashboard) | AG-DIR |
| `agency/reasoning` | pattern distillati da fallimenti → ReasoningBank corporate | tutti i LEARN |

**Regole operative:**
- `aidefence_has_pii` prima di ogni store in `agency/conversations` e `agency/leads`.
- Dry-run obbligatorio (pattern 3) su ogni WF prima di ogni run reale.
- Ogni workflow: `state.json` + trace per ogni esecuzione (test amnesia: ripartibile a freddo).
- Indici a 2 livelli: `agency/INDEX.md` (reparti) + `agency/<reparto>/INDEX.md` (per reparto).
- Log ReasoningBank: ogni fallimento distillato entro 24h dall'evento.

---

## 8. Build plan V2-6 (ordine fasi, con gate)

Allineato a V2-6 del Piano Maestro (§10). Un ciclo a 9 passi (ADR-006) per ogni fase; passo 5-bis
REVIEW MAXIMILIAN attivo da V2-3.

| Fase | Cosa | Gate di validazione |
|---|---|---|
| **B0** | Inventario asset AGENCY (tabella sez. 5 verificata file per file); ingest in wiki; fix operativi noti | Zero orfani; wiki/log aggiornato |
| **B1** | Scaffolding `company/01-agency/` — 10 reparti come strutture-cartella con BACKBONE.md, cartella agenti/ (placeholder schede), workflow/, principi/, scripts/, state/ | Struttura navigabile Explorer; verify Empire verde |
| **B2** | Wrap 4 WF outreach esistenti (email/LI/IG/reply) come team L3 con interfaccia contract + log memoria; runtime INVARIATO | Run reale email/LI/IG identica a prima del wrap; eventi in `agency/outreach` |
| **B3** | A3 live: AG-A3-BRIEF + AG-A3-PROP (beast-preventivi orchestrato) + AG-A3-QA (proposal-gate) | 1 preventivo reale prodotto dal flusso ≤48h; gate passato |
| **B4** | A4: delivery-playbook per i 3 prodotti + client-handover + support-90 + schede agenti A4 | Dry-run delivery Outreach Factory su ambiente test (non-DE) con UAT compilata |
| **B5** | A7 + A8: schede agenti + WF-CUSTOMER-LIFECYCLE + WF-CLOSING-PREP; script call su A5 | 1 prep call reale prodotta dal sistema prima di una call Max |
| **B6** | A9 + A10: Partnership + QA indipendente; skill `qa-delivery-gate` forgiate | 1 review A10 indipendente su delivery B4 |
| **B7** | A1 potenziata (icp-radar, WF-BRIEF-PRE-CALL); A6 (case-study-forge, upsell-mapper, WF-UPSELL-REFERRAL); dashboard KPI 10 reparti | KPI sez. 6 visibili e alimentati da dati reali |
| **B8** | Agenti reali: `agent_spawn` coordinator; hive-mind per decisioni cross-reparto; ReasoningBank loop attivo | Gate F-finale Piano Maestro: flusso end-to-end lead→contratto orchestrato, tracciato in memoria |
| **B9** | Primo delivery cliente reale gestito dal sistema end-to-end + primo case study | Gate Delivery firmato; QA A10 PASS; case study pubblicato; pattern in ReasoningBank |

**Regola ferrea su B2:** la pipeline email è ATTIVA e produce valore. Il wrapper si valida in dry-run e
su batch piccolo (10 email) prima di toccare la run da 500. Rollback = rimozione wrapper (runtime intatto).

---

## 9. Rischi specifici + mitigazioni (aggiornati v2)

| Rischio | Mitigazione |
|---|---|
| Rompere la pipeline outreach attiva durante il wrap | Pattern wrap-mai-riscrivere; staging separato; dry-run; rollback = rimozione wrapper (runtime intatto) |
| Ban/limitazioni canali social (LinkedIn/Instagram) | Cap conservativi già attivi, mai aumentati senza dati; pattern umanizzazione esistenti; email come canale primario; Sentinel Quality su error rate |
| Deliverability email degradata | Cap 100/h esistente; Gate Bibbia su ogni email; bounce in `agency/outreach`; ReasoningBank su pattern bounce |
| Token/credenziali scadute | Pre-flight check su ogni run (job `HC-AG-OP-01`); alert dashboard; runbook rinnovo |
| Collo di bottiglia su Max (discovery call + firma + call chiusura) | A1 prepara dossier pre-call; A3 produce preventivo ≤48h automatizzato; A8 prepara script chiusura; A7 gestisce la relazione — Max interviene solo dove deve |
| Delivery su ambienti cliente eterogenei (Windows/Linux, antivirus) | Prerequisiti raccolti in discovery; playbook con matrice OS; G+0 = solo verifica ambiente; countdown 7gg parte da ambiente conforme |
| Promesse non verificabili nel copy/preventivi | Gate Bibbia + Gate Preventivo bloccanti; Sentinel Brand-Voice; libreria obiezioni con sole prove reali (A5-OBJ) |
| Cliente dipendente da DE dopo handover | Gate Delivery richiede autonomia dimostrata (run da solo in UAT); training obbligatorio; supporto 90gg con obiettivo decrescente di ticket; A10 QA verifica autonomia |
| Auto-valutazione in A4 (chi consegna si auto-promuove) | A10 QA indipendente: gate separato, diverso coordinator, diverso namespace [colma gap v1] |
| Partner che invia lead non qualificati | AG-A9-QA blocca lead senza ICP compilato; accordo partner richiede briefing su ICP; commissione solo su contratto firmato |
| Upsell aggressivo brucia fiducia post-delivery | AG-A6-UPSELL attivo SOLO dopo Gate Delivery + NPS ≥8; mai upsell durante supporto; AG-A7-CLOSE gestisce il timing |
| Costi agenti in crescita con scaling | 3-tier routing (haiku sui meccanici: 26 agenti haiku su 74); spawn on-demand; Cost Sentinel + budget guard 09-OPERATIONS; dry-run default |
| PII lead/clienti nella memoria condivisa | `aidefence_has_pii` prima di ogni store in conversations/leads; leads.db resta storage locale primario; namespace non esportati cross-ecosistema senza contract |
| Swarm che muore sul limite crediti durante build | Build a lotti idempotenti (ADR-006); naming Title-Case fisso; checkpoint STATO-EMPIRE dopo ogni fase; lezione da CP-005 |

---

## Connessioni

- [[11-PIANO-V2-DIRETTIVA-SCALA]] §2 — la direttiva che governa questo dossier (fonte suprema)
- [[01-ECOSISTEMA-AGENCY]] — il v1 (riferimento per cap reali, asset esistenti, handoff contract HC-* base)
- [[12-DOSSIER-MAXIMILIAN]] — review 5-bis attiva da V2-3; standard di giudizio applicato a questo dossier
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] — enforcement Articoli 1-7 su ogni output esterno di AGENCY
- [[00-PIANO-MAESTRO]] — gerarchia LX→L5; AGENCY = ecosistema L1 #01; pilastro revenue
- `04-ECOSISTEMA-MARKETING.md` · `03-ECOSISTEMA-CONTENT-FACTORY.md` — fornitori principali via HC-AG-CF-01, HC-AG-MK-01
- `07-ECOSISTEMA-FORGE.md` — crea team/skill quando un KPI cala per 2 cicli (ADR-007)
- `09-ECOSISTEMA-OPERATIONS.md` — scheduling run giornaliere, cost guard, backup leads.db
- `company/Memory/maximilian-corpus/direttiva-20260611-scala-v2.md` — standard di scala (corpus)
- ADR-007 (pivot V2) · ADR-006 (ciclo 9 passi + 5-bis) · ADR-005 (minuzie → BACKLOG) · ADR-003 (wrap, non riscrittura) · ADR-002 (memory-first)
