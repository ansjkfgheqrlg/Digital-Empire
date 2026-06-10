# 🏢 01 — ECOSISTEMA AGENCY (Digital Empire Group)

> Dossier dell'ecosistema L1 #01 di EMPIRE OS. Coerente con `00-PIANO-MAESTRO.md`
> (gerarchia LX→L5, 13 pattern non negoziabili, Corporate Backbone, integrazione Ruflo).
> Versione: 1.0 · Creato: 2026-06-10 · Stato base: outreach 3 canali GIÀ ATTIVO,
> landing + presentazione live, skill di vendita installate.

---

## 0. Missione + DONE WHEN

**Missione:** acquisire e servire clienti delle 3 implementazioni AI di Digital Empire —
**Outreach Factory €4.000 · Content Factory €3.500 · Second Brain €2.500 · bundle Engine Room €8.000** —
con modello one-time, €0 canoni, codice di proprietà del cliente, setup in 7 giorni,
supporto 90 giorni. Posizionamento: **"l'agenzia progettata per essere licenziata"**.
AGENCY è il pilastro revenue della holding: tutto il resto di EMPIRE OS lo alimenta o lo amplifica.

**DONE WHEN (misurabili):**

1. I 6 reparti L2 esistono in `company/01-agency/` con BACKBONE.md, team L3/L4 documentati a schema canonico (coordinator, I/O, acceptance criteria, failure handling, shared_state).
2. La pipeline outreach esistente (email 500/gg cap 100/h, LinkedIn 20+20+30/gg, Instagram 30 DM/gg) gira INVARIATA ma wrappata come team L3 con handoff contract e log in memoria Ruflo — zero regressioni sulle run reali.
3. Ogni discovery call produce un preventivo problem-first entro 48h, passato dal Gate Preventivo, generato dal flusso A3 (non a mano).
4. Esiste un Delivery Playbook eseguibile per ciascuno dei 3 prodotti: discovery call → setup sul server del cliente → training → handover codice, completabile in ≤7 giorni, con checklist UAT firmabile.
5. Il flusso end-to-end lead→outreach→call→preventivo→contratto→delivery→supporto 90gg→testimonianza è percorribile e tracciato (ogni step ha owner, gate e record in `agency/*`).
6. Dashboard KPI per reparto visibile (evoluzione di `outreach-dashboard-premium`).
7. ReasoningBank riceve ogni fallimento (email bounce, preventivo perso, delivery in ritardo) come pattern distillato.

**OUT OF SCOPE (ora):** aumento dei cap outreach senza dati; nuovi prodotti/pricing; automazione della discovery call (resta umana); riscrittura della pipeline email attiva.

---

## 1. Posizione nella holding — input/output verso gli altri 8 ecosistemi

Ogni passaggio è un **handoff contract** `{from, to, payload, acceptance_criteria}` sul BUS.

| Direzione | Contract | Payload | Acceptance criteria |
|---|---|---|---|
| AGENCY → 02 INFO-BUSINESS | `HC-AG-IB-01` lead non pronto | lead qualificato ma "non ora / budget basso" + storico conversazione | lead taggato con motivo, consenso contatto valido |
| 02 INFO-BUSINESS → AGENCY | `HC-IB-AG-01` upsell student | cliente corso/community con segnali agency (chiede implementazione) | profilo ICP compilato, fonte tracciata |
| AGENCY → 03 CONTENT-FACTORY | `HC-AG-CF-01` richiesta asset cliente | `{client_brand_kit, icp, formati, deadline}` per delivery Content Factory €3.500 e per case study | asset conformi al brand gate del CLIENTE (multi-tenant, pattern 11) |
| 03 CONTENT-FACTORY → AGENCY | `HC-CF-AG-01` consegna asset | pacchetto contenuti pronto per setup su server cliente | passato QA gate CF + brand gate |
| AGENCY → 04 MARKETING | `HC-AG-MK-01` brief copy | brief APSOC (target, problema, prova, obiezioni) + dati performance reali (reply rate, win rate) | brief completo, numeri reali, no metriche inventate |
| 04 MARKETING → AGENCY | `HC-MK-AG-01` copy maggiore | sales page, sequenze, refresh template outreach, copy preventivi | passato Copy/APSOC Guild + gate Bibbia |
| AGENCY → 05 MULTI-BUSINESS | `HC-AG-MB-01` know-how delivery | playbook setup/handover riusabili per i business paralleli | playbook versionato in wiki |
| 05 MULTI-BUSINESS → AGENCY | `HC-MB-AG-01` proof | demo reali (es. canale YT automatizzato) come prova nelle vendite Content Factory | "prove non promesse": solo risultati verificabili |
| 06 PLATFORM → AGENCY | `HC-PL-AG-01` tooling | dashboard, fix landing (`agency-empire-landing`), infra, siti cliente | build verde, deploy verificato |
| AGENCY → 06 PLATFORM | `HC-AG-PL-01` feature request | richieste su dashboard/landing/script con priorità e KPI atteso | ticket con acceptance criteria misurabile |
| 07 FORGE → AGENCY | `HC-FG-AG-01` nuovi agenti/skill | team/skill creati quando un KPI di reparto cala sotto soglia per 2 cicli | team a schema canonico, skill ≤500 righe kernel |
| AGENCY → 07 FORGE | `HC-AG-FG-01` richiesta organico | gap funzionale documentato + KPI che lo dimostra | gap non coperto da skill esistente (verifica registro) |
| 08 INTELLIGENCE → AGENCY | `HC-IN-AG-01` intelligence | ricerca ICP/nicchie/trend, template second-brain per delivery Second Brain €2.500 | fonti citate, ingest in wiki completato |
| AGENCY → 08 INTELLIGENCE | `HC-AG-IN-01` dati campo | obiezioni reali, motivi di rifiuto, domande ricorrenti dalle conversazioni outreach/call | anonimizzati (aidefence has_pii), tag per nicchia |
| 09 OPERATIONS → AGENCY | `HC-OP-AG-01` runtime | scheduling run giornaliere (email/LinkedIn/IG), cost guard, backup `leads.db` | run loggata, budget rispettato, dry-run disponibile |
| AGENCY → 09 OPERATIONS | `HC-AG-OP-01` job | nuovi job da schedulare (follow-up, report settimanale) | job idempotente, con kill-switch |

**Regola:** AGENCY non produce contenuti marketing "grandi" né tooling in-house: li **richiede**
via contract. Produce in-house solo ciò che è quotidiano e operativo (sez. 2, reparti A5/A6).

---

## 2. Reparti L2

Struttura: `company/01-agency/{A1..A6}/`. Ogni team L3 = workflow end-to-end; ogni team L4 = singola funzione (pattern 1: un team per funzionalità).

### A1 — RICERCA (Lead & Market Intelligence)

**Missione:** alimentare il funnel con lead qualificati e dare a Preventivi/Delivery l'intelligence di nicchia per vendere e consegnare meglio.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-LEAD-SOURCING` | scraping (Maps/Apify/Outscraper) → estrazione → arricchimento → qualifica → `leads.db` |
| L3 | `WF-MARKET-INTEL` | nicchia/competitor/trend → report per Acquisizione e Preventivi (regole esistenti `01_ricerca_no_sito.md`, `02_ricerca_ads_funnel_scarsi.md`, `06_ricerca_ai_prospects.md`) |
| L4 | `T-scraper` | run scraper (maps_browser_scraper, apify_scraper, outscraper_scraper, google_scraper) |
| L4 | `T-extractor` | estrazione contatti/dati dal raw (extractor.py) |
| L4 | `T-qualifier` | scoring lead vs ICP (qualifier.py + regola `03_qualifica_lead.md`) |
| L4 | `T-icp-profiler` | definizione/aggiornamento ICP per nicchia (input da 08 INTELLIGENCE) |
| L4 | `T-competitor-profiler` | dossier competitor del prospect (competitor.py, cro_audit.py, skill market-audit) |

### A2 — ACQUISIZIONE / OUTREACH

**Missione:** convertire lead qualificati in discovery call prenotate, su 3 canali, dentro i cap reali. CTA standard: **presentazione-empire.vercel.app**.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-OUTREACH-EMAIL` | **ESISTENTE, NON SI TOCCA**: scraper → qualifier → strategist → writer (APSOC) → **Bibbia 3-checker QA** → sender. Fino a 500/gg, cap 100/h |
| L3 | `WF-OUTREACH-LINKEDIN` | 20 connessioni + 20 messaggi + 30 commenti/gg (script 01→05 + comment_posts.py) |
| L3 | `WF-OUTREACH-INSTAGRAM` | 30 DM/gg, pattern 2 messaggi (corpo + link), follow-up |
| L3 | `WF-REPLY-FOLLOWUP` | reply_monitor → triage risposta → conversation_manager → follow-up (followup_writer) → booking call |
| L4 | `T-strategist` | angolo di attacco per lead (strategist.py, insight.py) |
| L4 | `T-writer-apsoc` | scrittura messaggio (writer.py, humanizer.py, copy_knowledge.py) |
| L4 | `T-bibbia-qa` | gate qualità 3-checker pre-invio (bibbia_team.py) — BLOCCA, non suggerisce |
| L4 | `T-sender` | invio + rate limiting + log (sender.py) |
| L4 | `T-reply-triage` | classificazione risposte: interessato / obiezione / no / out-of-office |
| L4 | `T-followup` | sequenze follow-up multi-touch (run_followup.py, skill cold-email) |
| L4 | `T-li-engage` | commenti + connessioni LinkedIn |
| L4 | `T-ig-dm` | DM Instagram + follow-up 2 step |

### A3 — PREVENTIVI

**Missione:** trasformare ogni discovery call in una proposta problem-first inviata entro 48h, con pricing a catalogo (mai sconti improvvisati), che vende l'autonomia del cliente.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-PREVENTIVO` | trascrizione/appunti call → brief strutturato → audit problema → outline problem-first → documento completo → Gate Preventivo → invio → follow-up commerciale |
| L4 | `T-discovery-brief` | da call a brief: problema, awareness level (aware/unaware), stack attuale, vincoli server/ambiente |
| L4 | `T-problem-audit` | quantifica il problema del cliente (skill market-audit, cro_audit) |
| L4 | `T-proposal-writer` | costruisce il preventivo (skill **beast-preventivi** + market-proposal) |
| L4 | `T-pricing-config` | seleziona prodotto/bundle: Outreach Factory €4.000 / Content Factory €3.500 / Second Brain €2.500 / Engine Room €8.000 — one-time, €0 canoni |
| L4 | `T-proposal-qa` | Gate Preventivo (sez. 8) |

### A4 — OPERATIVITÀ / DELIVERY

**Missione:** consegnare i 3 prodotti in ≤7 giorni con il **processo reale**: discovery call → setup workflow sul server/macchina del cliente → training → handover del codice. Poi 90 giorni di supporto. Il cliente deve poterci "licenziare": autonomia totale a fine handover.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-DELIVERY-OUTREACH-FACTORY` | clona la pipeline outreach DE, la parametrizza multi-tenant (`brand_kit` + `icp` del cliente), setup sul server cliente, run di test, training, handover |
| L3 | `WF-DELIVERY-CONTENT-FACTORY` | richiede a 03 CONTENT-FACTORY il motore parametrizzato (`HC-AG-CF-01`), setup, training, handover |
| L3 | `WF-DELIVERY-SECOND-BRAIN` | richiede a 08 INTELLIGENCE il template second-brain (`HC-IN-AG-01`), setup vault+skill sul sistema cliente, training, handover |
| L3 | `WF-SUPPORTO-90GG` | intake ticket → triage → fix → log; check proattivo settimanale; chiusura a 90gg con review |
| L4 | `T-env-setup` | verifica prerequisiti ambiente cliente (raccolti in discovery), installazione, secrets |
| L4 | `T-config-tenant` | iniezione `brand_kit` + `icp` cliente in ogni workflow (pattern 11) |
| L4 | `T-uat-runner` | run di accettazione con il cliente, checklist UAT firmabile |
| L4 | `T-training-kit` | materiale training: video walkthrough, runbook operativo, FAQ |
| L4 | `T-handover-pack` | pacchetto handover: codice completo, README, credenziali, licenza d'uso |
| L4 | `T-support-triage` | classificazione ticket 90gg (bug / domanda / fuori scope) |

### A5 — COPYWRITING-INTERNO

**Missione:** copy operativo quotidiano dell'agency (template email/DM, micro-copy preventivi, script call) con framework APSOC. I pezzi grandi (sales page, sequenze lunghe) si chiedono a 04 MARKETING via `HC-AG-MK-01`; A5 è il consumatore-adattatore locale.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-COPY-OUTREACH` | refresh periodico template 3 canali: analisi reply reali → varianti APSOC → gate Bibbia → rollout graduale |
| L4 | `T-apsoc-writer` | scrittura/variazione copy (skill **cro-copy-architect**, market-copy) |
| L4 | `T-objection-handler` | libreria obiezioni reali (da `HC-AG-IN-01`) → risposte testate |
| L4 | `T-copy-qa` | stesso gate Bibbia di A2, riusato (pattern 6: una skill, molti reparti) |

### A6 — MARKETING-INTERNO

**Missione:** vetrina e prova sociale dell'agency: landing, presentazione, case study, testimonianze. Genera inbound e munizioni per outreach e preventivi.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-ASSET-VETRINA` | manutenzione `agency-empire-landing` + presentazione-empire.vercel.app (build via 06 PLATFORM) |
| L3 | `WF-CASE-STUDY` | delivery chiusa → raccolta testimonianza → case study APSOC → produzione asset via 03 CF → pubblicazione |
| L4 | `T-proof-collector` | raccolta testimonianze/metriche reali a fine 90gg ("prove non promesse") |
| L4 | `T-case-writer` | scrittura case study (cro-copy-architect) |
| L4 | `T-upsell-mapper` | mappa cliente→prossima offerta (singolo prodotto → Engine Room €8.000; cliente → referral) |

---

## 3. Roster agenti L5

Convenzione id: `AG-<reparto>-<team>-<ruolo>`. Tier secondo 3-tier routing del Backbone:
**haiku** = meccanico/alto volume · **sonnet** = scrittura/analisi standard · **opus** = ragionamento critico/gate.

| ID | Ruolo | Tipo | Tier |
|---|---|---|---|
| AG-DIR | Direttore ecosistema AGENCY (riporta a C-Suite) | coordinator | opus |
| AG-A1-COORD | Coordinatore Ricerca | coordinator | sonnet |
| AG-A1-SCRAPE-W | Runner scraper multi-fonte | worker | haiku |
| AG-A1-EXTRACT-W | Estrattore contatti/dati | worker | haiku |
| AG-A1-QUAL-W | Qualificatore lead vs ICP | worker | sonnet |
| AG-A1-ICP-W | Profiler ICP/nicchia | worker | sonnet |
| AG-A1-COMP-W | Analista competitor/audit prospect | worker | sonnet |
| AG-A2-COORD | Coordinatore Acquisizione (orchestrator.py oggi) | coordinator | sonnet |
| AG-A2-STRAT-W | Strategist angolo di attacco | worker | sonnet |
| AG-A2-WRITE-W | Writer APSOC messaggi | worker | sonnet |
| AG-A2-BIBBIA-C1/C2/C3 | I 3 checker del gate Bibbia | worker ×3 | sonnet |
| AG-A2-SEND-W | Sender + rate limiter (≤500/gg, 100/h) | worker | haiku |
| AG-A2-TRIAGE-W | Triage risposte | worker | haiku |
| AG-A2-FUP-W | Follow-up writer | worker | sonnet |
| AG-A2-LI-W | Operatore LinkedIn (20+20+30/gg) | worker | haiku |
| AG-A2-IG-W | Operatore Instagram (30 DM/gg) | worker | haiku |
| AG-A3-COORD | Coordinatore Preventivi | coordinator | opus |
| AG-A3-BRIEF-W | Discovery brief builder | worker | sonnet |
| AG-A3-AUDIT-W | Problem auditor | worker | sonnet |
| AG-A3-PROP-W | Proposal writer (beast-preventivi) | worker | opus |
| AG-A3-PRICE-W | Pricing configurator (catalogo fisso) | worker | haiku |
| AG-A3-QA-W | Gate Preventivo | worker | opus |
| AG-A4-COORD | Coordinatore Delivery | coordinator | opus |
| AG-A4-ENV-W | Env setup su server cliente | worker | sonnet |
| AG-A4-TENANT-W | Config multi-tenant (brand_kit+icp) | worker | sonnet |
| AG-A4-UAT-W | UAT runner + checklist | worker | sonnet |
| AG-A4-TRAIN-W | Training kit builder | worker | sonnet |
| AG-A4-HAND-W | Handover pack builder | worker | sonnet |
| AG-A4-SUPP-W | Support triage 90gg | worker | haiku |
| AG-A5-COORD | Coordinatore Copy interno | coordinator | sonnet |
| AG-A5-COPY-W | APSOC writer/variator | worker | sonnet |
| AG-A5-OBJ-W | Objection librarian | worker | sonnet |
| AG-A6-COORD | Coordinatore Marketing interno | coordinator | sonnet |
| AG-A6-PROOF-W | Proof collector | worker | haiku |
| AG-A6-CASE-W | Case study writer | worker | sonnet |
| AG-A6-UPSELL-W | Upsell mapper | worker | sonnet |

Sentinels (Cost, Quality, Drift, Security, Brand-Voice) sono **corporate** (LX/Backbone), non duplicati qui: osservano AGENCY via Observability.

---

## 4. Workflow chiave end-to-end (la pipeline revenue)

```
[A1] LEAD ──► [A2] OUTREACH ──► [A2] REPLY/FOLLOW-UP ──► CALL ──► [A3] PREVENTIVO ──► CONTRATTO
                                                                                          │
   TESTIMONIANZA / UPSELL [A6] ◄── SUPPORTO 90GG [A4] ◄── DELIVERY ≤7GG [A4] ◄────────────┘
```

| # | Step | Owner | Input → Output | Gate |
|---|---|---|---|---|
| 1 | Sourcing & qualifica | A1 `WF-LEAD-SOURCING` | fonti → lead qualificato in `leads.db` con score ICP | qualifier score ≥ soglia |
| 2 | Outreach multicanale | A2 (3 WF) | lead → messaggi inviati (email ≤500/gg cap 100/h · LI 20+20+30 · IG 30 DM). CTA: presentazione-empire.vercel.app | **Gate Bibbia** (blocca invio) |
| 3 | Reply & follow-up | A2 `WF-REPLY-FOLLOWUP` | risposta → conversazione gestita → call prenotata | triage corretto; no risposta a "no" |
| 4 | Discovery call | **UMANO (Max)** + AG-A3-BRIEF-W prepara dossier pre-call (lead + audit + competitor) | call → trascrizione/appunti | dossier pre-call consegnato prima della call |
| 5 | Preventivo | A3 `WF-PREVENTIVO` | brief → proposta problem-first inviata ≤48h | **Gate Preventivo** |
| 6 | Contratto | UMANO + T-pricing-config | proposta → firma + pagamento one-time | pagamento verificato; scope congelato |
| 7 | Delivery ≤7gg | A4 `WF-DELIVERY-*` | discovery tecnica → **setup workflow sul server del cliente** → run test → **training** → **handover codice** | **Gate Delivery** (UAT firmata) |
| 8 | Supporto 90gg | A4 `WF-SUPPORTO-90GG` | ticket/check settimanali → risoluzioni loggate | SLA rispettato; log completo |
| 9 | Testimonianza & upsell | A6 `WF-CASE-STUDY` + T-upsell-mapper | cliente a fine supporto → testimonianza + case study + proposta upsell (→ Engine Room / referral) | "prove non promesse": solo metriche reali del cliente |

Ogni freccia = handoff contract sul BUS intra-ecosistema; ogni fallimento (bounce, ghosting,
preventivo perso, delivery in ritardo) → record ReasoningBank con causa distillata (pattern 5).

---

## 5. Asset esistenti → reparto di destinazione

Regola F3 del Piano Maestro: **migrazione = mappatura + wrapper, mai riscrittura**. Azioni: `usa-così` (invariato, solo registrato) · `wrappa` (invariato + interfaccia contract/memoria) · `evolvi` (modifiche pianificate dopo wrap).

| Path | Reparto | Azione |
|---|---|---|
| `Digital Empire/Outreach/Outreach Workflow/` (run.py, orchestrator.py, agents/: scraper, qualifier, strategist, writer, bibbia_team, sender, reply_monitor, followup_writer, conversation_manager…) | A1 + A2 | **wrappa** come `WF-LEAD-SOURCING` + `WF-OUTREACH-EMAIL` + `WF-REPLY-FOLLOWUP`. Runtime intoccabile finché il wrapper non è validato |
| `Digital Empire/Outreach/Outreach Workflow/leads.db` | A1 (storage via 09 OPS) | **usa-così** + backup schedulato (`HC-AG-OP-01`) |
| `Digital Empire/Outreach/LinkedIn Automation/` (01→05 + comment_posts.py) | A2 | **wrappa** come `WF-OUTREACH-LINKEDIN` |
| `Digital Empire/Outreach/Instagram Automation/` | A2 | **wrappa** come `WF-OUTREACH-INSTAGRAM` |
| `Digital Empire/Outreach/outreach-dashboard-premium/` (Next.js + API) | A2 + Observability | **evolvi**: da dashboard outreach a dashboard KPI 6 reparti (build via 06 PLATFORM) |
| `Digital Empire/Outreach/SISTEMA_OUTREACH_COMPLETO.md`, `Outreach Workflow/ARCHITETTURA_COMPLETA.md` | docs | **usa-così** → ingest wiki (08) |
| `Digital Empire/Agenti/Agency/orchestrator/` (AGENT.md, run.py, run_500.py, batch_send.py) | A2 | **wrappa** dentro AG-A2-COORD |
| `Digital Empire/Agenti/Agency/sub-agents/` (ai-implementation, cro-funnel, no-website) | A1 + A3 | **evolvi**: diventano profili di T-icp-profiler / T-problem-audit |
| `Digital Empire/Agenti/Agency/outreach/rules/` (01_ricerca_no_sito … 06_ricerca_ai_prospects) | A1 + A2 | **usa-così** (knowledge layer dei team) |
| `Digital Empire/Agenti/Agency/skills/` (15 skill market-*) | A5 + A6 + A3 | **usa-così** |
| `Digital Empire/agency-empire-landing/` | A6 (build: 06 PLATFORM) | **usa-così / evolvi** (case study quando arrivano) |
| presentazione-empire.vercel.app | A6 | **usa-così** (CTA standard di ogni canale outreach) |
| Skill globale `beast-preventivi` | A3 | **usa-così** (cuore di T-proposal-writer) |
| Skill globale `agency-scalping` (129 file: acquisizione/pricing/delivery) | tutti i reparti | **usa-così** (knowledge layer trasversale dell'ecosistema) |
| Skill globale `cold-email` | A2 + A5 | **usa-così** |
| Skill globali `market-proposal`, `market-audit` | A3 + A1 | **usa-così** |
| Skill globale `cro-copy-architect` (APSOC) | A5 + A6 | **usa-così** |
| Script `Agenti/Agency/outreach/script_chiamata_freddo.md`, `genera_tabella_chiamate.py` | A3 (pre-call) | **evolvi** dentro T-discovery-brief |

Zero orfani: qualsiasi file outreach/agency non in tabella va classificato in F3 o archiviato con motivo nel log wiki.

---

## 6. Skill — esistenti da usare + nuove da creare

**Esistenti (nessuna duplicazione — pattern 6):** `beast-preventivi` (A3), `agency-scalping` (tutti), `cold-email` (A2/A5), `market-proposal` (A3), `market-audit` (A1/A3), `cro-copy-architect` (A5/A6), suite `market-*` 15 skill (A5/A6/A3), `avvia-email`/`avvia-linkedin`/`avvia-ig`/`avvia-parallel`/`avvia-scraper` (A2 entrypoint operativi), `wiki-context` + `memory-empire` (contesto), `contradiction-analyzer` (QA Backbone).

**NUOVE da creare (via 07 FORGE, kernel ≤500 righe, references/ per il dettaglio):**

| Skill (kebab-case) | Scopo | Reparto |
|---|---|---|
| `discovery-call-brief` | trascrizione/appunti call → brief strutturato (problema, awareness, ambiente tecnico, budget signal) | A3 |
| `proposal-gate` | checklist eseguibile del Gate Preventivo (sez. 8) — blocca, non suggerisce | A3 |
| `delivery-playbook` | runbook setup 7gg per ciascuno dei 3 prodotti: prerequisiti, giorni 1-7, rollback | A4 |
| `client-handover` | genera handover pack: codice, README, credenziali, licenza, video-index training | A4 |
| `support-90` | gestione supporto 90gg: triage, SLA, check proattivi, report chiusura | A4 |
| `outreach-reply-triage` | classificatore risposte 4 classi + next action (riusabile dai clienti Outreach Factory) | A2 |
| `icp-radar` | crea/aggiorna profili ICP per nicchia con criteri di qualifica espliciti | A1 |
| `case-study-forge` | da delivery chiusa a case study APSOC con metriche verificate | A6 |
| `upsell-mapper` | matrice cliente→offerta successiva (prodotto singolo → Engine Room → referral) | A6 |

Nota multi-tenant: `delivery-playbook`, `client-handover`, `outreach-reply-triage` sono anche
**prodotto** — versioni parametrizzate finiscono nel pacchetto consegnato al cliente.

---

## 7. Integrazione Ruflo

`Ruflo coordina, Claude Code esegue.` Swarm init a livello ecosistema, poi per reparto:

| Reparto | Topologia swarm | Razionale |
|---|---|---|
| AGENCY (root) | `hierarchical` (AG-DIR → 6 coordinator) | default Piano Maestro |
| A1 Ricerca | `star` (coordinator → scraper/extractor/qualifier paralleli) | fan-out su fonti indipendenti |
| A2 Acquisizione | `pipeline` (strategist→writer→bibbia→sender) + `star` per i 3 canali | la pipeline email è sequenziale per natura; i canali sono paralleli |
| A3 Preventivi | `pipeline` (brief→audit→writer→pricing→gate) | flusso lineare con gate finale |
| A4 Delivery | `hierarchical` per delivery attiva; `star` per ticket 90gg | un delivery = progetto; ticket = code parallele |
| A5 Copy | `mesh` piccolo (writer ↔ objection ↔ qa) | iterazione su varianti |
| A6 Marketing-interno | `star` | task indipendenti a bassa frequenza |

**Namespace memoria AgentDB** (prefisso `agency/`):

| Namespace | Contenuto |
|---|---|
| `agency/leads` | lead, score, stato funnel (specchio semantico di leads.db, non sostituto) |
| `agency/outreach` | template attivi, performance per variante, esiti Bibbia |
| `agency/conversations` | thread risposta, obiezioni, esiti triage (PII-scan prima dello store) |
| `agency/proposals` | preventivi: stato, win/loss, motivi |
| `agency/clients` | anagrafica clienti, prodotto, brand_kit, icp, milestone delivery |
| `agency/delivery` | checklist UAT, ambienti, ticket 90gg |
| `agency/kpi` | metriche per reparto per ciclo |
| `agency/reasoning` | pattern distillati da fallimenti (alimenta ReasoningBank corporate) |

Operativo: `hooks_route` pre-task (carica pattern da `agency/reasoning`), `memory_search`
prima di ogni preventivo/template nuovo, `agent_spawn` per i coordinator in F-B6,
`aidefence_has_pii` prima di ogni store di conversazioni. **Dry-run obbligatorio** (pattern 3)
su ogni WF: stima costo + anteprima output senza invii reali.

---

## 8. KPI per reparto + quality gates

Nessun target inventato: i CAP sono reali (limiti operativi attivi), i TASSI si misurano
dal giorno 1 e diventano baseline — la FORGE interviene quando un KPI cala per 2 cicli.

| Reparto | KPI (misurare, non inventare) | Cap/vincolo reale |
|---|---|---|
| A1 | lead qualificati/gg; % qualifica su scraped; freschezza dati | — |
| A2 | inviati/gg per canale; reply rate; positive reply rate; call prenotate/sett | email ≤500/gg cap 100/h · LI 20 connect+20 msg+30 commenti/gg · IG 30 DM/gg |
| A3 | tempo call→preventivo (target ≤48h); win rate; valore medio preventivo | pricing a catalogo: 4.000/3.500/2.500/8.000 € |
| A4 | giorni delivery (target ≤7); UAT pass al primo giro; ticket risolti in SLA; NPS fine 90gg | setup ≤7gg, supporto 90gg (promessa commerciale) |
| A5 | % copy passato al gate Bibbia al primo giro; tempo brief→copy | — |
| A6 | case study per cliente chiuso; call da inbound; testimonianze raccolte | — |

**Quality gates (pattern 4 — niente esce senza gate):**

1. **Gate Bibbia** (ESISTENTE — `bibbia_team.py`, 3 checker): ogni messaggio outreach prima dell'invio. Verifica conformità copy, struttura, firma/CTA (presentazione-empire.vercel.app). Esteso come servizio anche ad A5. *Blocca, non suggerisce.*
2. **Gate Preventivo** (NUOVO — skill `proposal-gate`): problem-first verificato (il problema del cliente apre il documento); awareness level corretto; pricing solo a catalogo; promesse = solo prove verificabili (Mandato Empire); scope delivery 7gg esplicito; clausola proprietà codice + €0 canoni presente; supporto 90gg definito; brand voice conforme.
3. **Gate Delivery** (NUOVO — dentro `delivery-playbook`): workflow funzionante SUL SERVER DEL CLIENTE (non solo in locale); run di test reale passata; training erogato e materiale consegnato; handover pack completo (codice, README, credenziali); checklist UAT firmata dal cliente; nessuna dipendenza residua da DE.
4. **Brand gate corporate** (Mandato Empire, Sentinel Brand-Voice): trasversale su tutto l'output esterno.

---

## 9. Fasi di build (ordinate, con gate di validazione)

Allineate a F3-F4 del Piano Maestro. Una fase per ciclo, verify ad ogni step, checkpoint memoria.

| Fase | Cosa | Gate di validazione |
|---|---|---|
| **B0** | Inventario asset AGENCY (tabella sez. 5 verificata file-per-file), ingest doc in wiki, fix operativi noti (rinnovo token FB) | zero orfani; wiki/log aggiornato |
| **B1** | Scaffolding `company/01-agency/` — 6 reparti, BACKBONE.md (namespace+topologie), handoff contract sez. 1 scritti come schema | struttura navigabile; verify Empire verde |
| **B2** | Wrap dei 4 WF outreach esistenti come team L3 (interfaccia contract + log memoria attorno al runtime, runtime INVARIATO) | run reale email/LI/IG identica a prima del wrap; eventi in `agency/outreach` |
| **B3** | A3 live: `discovery-call-brief` + beast-preventivi orchestrato + `proposal-gate` | 1 preventivo reale prodotto dal flusso e passato dal gate ≤48h dalla call |
| **B4** | A4: `delivery-playbook` per i 3 prodotti + `client-handover` + `support-90` | dry-run delivery completo di Outreach Factory su ambiente di test (server non-DE) con UAT checklist compilata |
| **B5** | A1 potenziata (icp-radar) + A6 (case-study-forge, upsell-mapper) + dashboard KPI 6 reparti (evoluzione outreach-dashboard-premium via 06 PLATFORM) | KPI sez. 8 visibili e alimentati da dati reali |
| **B6** | Agenti reali: `agent_spawn` dei coordinator, hive-mind per decisioni cross-reparto, ReasoningBank loop su fallimenti | **= Gate F4 Piano Maestro**: flusso end-to-end lead→outreach→call→preventivo orchestrato dal sistema, tracciato in memoria |
| **B7** | Primo delivery cliente reale gestito dal sistema + primo case study | Gate Delivery firmato; case study pubblicato; pattern delivery in ReasoningBank |

Regola ferrea su B2: il sistema outreach è ATTIVO e produce valore — qualsiasi wrapper si
valida in dry-run e su batch piccolo prima di toccare la run da 500.

---

## 10. Rischi specifici + mitigazioni

| Rischio | Mitigazione |
|---|---|
| Rompere la pipeline outreach attiva durante la migrazione | pattern wrap-mai-riscrivere; staging separato; dry-run; rollback = rimozione wrapper (runtime intatto) |
| Ban/limitazioni canali social (LinkedIn/Instagram) | cap conservativi GIÀ attivi (20+20+30, 30 DM) mai aumentati senza dati; pattern umanizzazione esistenti; canale email come primario; Sentinel Quality su error rate |
| Deliverability email degradata (volumi 500/gg) | cap 100/h esistente; gate Bibbia su ogni email; monitoraggio bounce in `agency/outreach`; ReasoningBank su pattern di bounce |
| Token/credenziali scadute (es. token FB già scaduto) | check credenziali in pre-flight di ogni run (job `HC-AG-OP-01`); alert su dashboard; runbook rinnovo |
| Collo di bottiglia umano: discovery call e firma restano su Max | dossier pre-call automatico (A3) per call più corte; preventivo ≤48h automatizzato; calendario con slot protetti; tutto il resto del funnel non aspetta l'umano |
| Delivery 7gg su ambienti cliente eterogenei (Windows/Linux, permessi, antivirus) | prerequisiti ambiente raccolti IN discovery call (checklist in `discovery-call-brief`); `delivery-playbook` con matrice OS; giorno 1 = solo verifica ambiente; clausola: il countdown 7gg parte ad ambiente conforme |
| Promesse non verificabili nel copy/preventivi (drift dal Mandato "prove non promesse") | Gate Bibbia + Gate Preventivo bloccanti; Sentinel Brand-Voice; libreria obiezioni con sole prove reali |
| Cliente dipendente da DE dopo handover (tradisce il posizionamento "licenziaci") | Gate Delivery richiede autonomia dimostrata (cliente esegue una run da solo in UAT); training kit obbligatorio; supporto 90gg con obiettivo decrescente di ticket |
| Costi agenti reali in crescita con lo scaling | 3-tier routing (sez. 3: haiku sui meccanici); spawn on-demand; Cost Sentinel + budget guard di 09 OPERATIONS; dry-run default |
| PII di lead/clienti nella memoria condivisa | `aidefence_has_pii` prima di ogni store in `agency/conversations`; leads.db resta storage primario locale; namespace non esportati cross-ecosistema senza contract |
| Upsell aggressivo che brucia la fiducia post-delivery | upsell-mapper attiva SOLO dopo Gate Delivery + segnale positivo a fine 90gg; mai upsell durante il supporto |

---

## Connessioni

- [[00-PIANO-MAESTRO]] — architettura EMPIRE OS (questo dossier = ecosistema 01)
- [[Concept_Pivot_Implementazioni_AI]] — offerta 3 prodotti + Engine Room
- [[Tool_Copy_Workflow_Orchestration]] — motore APSOC (ecosistema 04)
- [[Agency_Empire_Landing]] — vetrina (reparto A6)
- `04-ECOSISTEMA-MARKETING.md` · `03-ECOSISTEMA-CONTENT-FACTORY.md` — fornitori principali via handoff contract
- `07-BACKBONE-RUFLO-SKILLS.md` — registro skill + namespace memoria
