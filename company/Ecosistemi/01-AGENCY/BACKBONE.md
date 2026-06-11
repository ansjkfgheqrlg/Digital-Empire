# BACKBONE — 🏢 01-AGENCY

> Come AGENCY si collega al Corporate Backbone di EMPIRE OS.
> Fonti vincolanti: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §1+§7 · `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md` §1.
> Org chart completo: `ECOSISTEMA.md` (questa cartella) · dettagli tecnici Backbone: `company/Backbone/`.

---

## 1. BRAIN — Namespace AgentDB (prefisso `agency/`)

Dichiarati qui come richiesto dal Piano Maestro §5 ("ogni ecosistema dichiara nel suo BACKBONE.md
quali namespace di memoria e quale topologia swarm usa"). Init: `ruflo memory init` in `company/`.

| Namespace | Contenuto | Note |
|---|---|---|
| `agency/leads` | lead, score, stato funnel | specchio semantico di `leads.db`, NON sostituto |
| `agency/outreach` | template attivi, performance per variante, esiti Bibbia | alimentato dai wrapper B2 |
| `agency/conversations` | thread risposta, obiezioni, esiti triage | **PII-scan (`aidefence_has_pii`) prima dello store** |
| `agency/proposals` | preventivi: stato, win/loss, motivi | input del ReasoningBank commerciale |
| `agency/clients` | anagrafica clienti, prodotto, brand_kit, icp, milestone delivery | pattern #11 multi-tenant |
| `agency/delivery` | checklist UAT, ambienti, ticket 90gg | |
| `agency/kpi` | metriche per reparto per ciclo | alimenta dashboard B5 |
| `agency/reasoning` | pattern distillati da fallimenti | alimenta ReasoningBank corporate |

Regole operative (dossier §7): `hooks_route` pre-task carica pattern da `agency/reasoning`;
`memory_search` obbligatorio prima di ogni preventivo/template nuovo; **dry-run obbligatorio**
(pattern #3) su ogni WF: stima costo + anteprima output senza invii reali.
Fallback senza daemon: mirror `company/runtime/brain/agency.jsonl` + `brain.sh recall` (ADR-005).

## 2. COORDINATION — Topologia swarm

**Topologia ecosistema: `hierarchical`** (dossier 07 §1.6: catena di comando, delivery clienti =
anti-drift, responsabilità chiare per SLA). Root: **AG-DIR** → 6 coordinator di reparto.
Sotto-topologie per reparto (dossier 01 §7):

| Reparto | Topologia | Razionale |
|---|---|---|
| AGENCY (root) | `hierarchical` (AG-DIR → 6 coordinator) | default Piano Maestro |
| A1 Ricerca | `star` (coordinator → scraper/extractor/qualifier paralleli) | fan-out su fonti indipendenti |
| A2 Acquisizione | `pipeline` (strategist→writer→bibbia→sender) + `star` per i 3 canali | la pipeline email è sequenziale per natura; i canali sono paralleli |
| A3 Preventivi | `pipeline` (brief→audit→writer→pricing→gate) | flusso lineare con gate finale |
| A4 Delivery | `hierarchical` per delivery attiva; `star` per ticket 90gg | un delivery = progetto; ticket = code parallele |
| A5 Copy | `mesh` piccolo (writer ↔ objection ↔ qa) | iterazione su varianti |
| A6 Marketing-interno | `star` | task indipendenti a bassa frequenza |

Spawn: `swarm_init` a livello ecosistema in fase B6, poi `agent_spawn` per i coordinator.
Routing modelli 3-tier (dossier 07 §2.3): haiku = meccanico/alto volume, sonnet = scrittura/analisi
standard, opus = ragionamento critico/gate (AG-DIR, AG-A3-COORD, AG-A3-PROP-W, AG-A3-QA-W, AG-A4-COORD).

## 3. BUS — Handoff contract con gli altri ecosistemi (dossier 01 §1)

Ogni passaggio è un contract `{from, to, payload, acceptance_criteria}` sul gbus (livello INTER).
Formato completo: dossier 07 §1.1. Handoff "pesanti" (multi-file) viaggiano come
`H-<id>.json` in `handoffs/{inbox,outbox,archive}/` (cartelle create in fase B2 del Backbone).

### 3.1 In USCITA (AGENCY chiede / fornisce)

| Contract | Verso | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-AG-IB-01` lead non pronto | 02 INFO-BUSINESS | lead qualificato ma "non ora / budget basso" + storico conversazione | lead taggato con motivo; consenso contatto valido |
| `HC-AG-CF-01` richiesta asset cliente | 03 CONTENT-FACTORY | `{client_brand_kit, icp, formati, deadline}` per delivery Content Factory €3.500 e case study | asset conformi al brand gate del CLIENTE (multi-tenant, pattern #11) |
| `HC-AG-MK-01` brief copy | 04 MARKETING | brief APSOC (target, problema, prova, obiezioni) + dati performance reali (reply rate, win rate) | brief completo, numeri reali, no metriche inventate |
| `HC-AG-MB-01` know-how delivery | 05 MULTI-BUSINESS | playbook setup/handover riusabili per i business paralleli | playbook versionato in wiki |
| `HC-AG-PL-01` feature request | 06 PLATFORM | richieste su dashboard/landing/script con priorità e KPI atteso | ticket con acceptance criteria misurabile |
| `HC-AG-FG-01` richiesta organico | 07 FORGE | gap funzionale documentato + KPI che lo dimostra | gap non coperto da skill esistente (verifica registro) |
| `HC-AG-IN-01` dati campo | 08 INTELLIGENCE | obiezioni reali, motivi di rifiuto, domande ricorrenti da outreach/call | anonimizzati (`aidefence_has_pii`), tag per nicchia |
| `HC-AG-OP-01` job | 09 OPERATIONS | nuovi job da schedulare (follow-up, report settimanale, backup leads.db) | job idempotente, con kill-switch |

### 3.2 In INGRESSO (gli altri ecosistemi servono AGENCY)

| Contract | Da | Payload | Acceptance criteria |
|---|---|---|---|
| `HC-IB-AG-01` upsell student | 02 INFO-BUSINESS | cliente corso/community con segnali agency (chiede implementazione) | profilo ICP compilato, fonte tracciata |
| `HC-CF-AG-01` consegna asset | 03 CONTENT-FACTORY | pacchetto contenuti pronto per setup su server cliente | passato QA gate CF + brand gate |
| `HC-MK-AG-01` copy maggiore | 04 MARKETING | sales page, sequenze, refresh template outreach, copy preventivi | passato Copy/APSOC Guild + gate Bibbia |
| `HC-MB-AG-01` proof | 05 MULTI-BUSINESS | demo reali (es. canale YT automatizzato) come prova nelle vendite Content Factory | "prove non promesse": solo risultati verificabili |
| `HC-PL-AG-01` tooling | 06 PLATFORM | dashboard, fix landing (`agency-empire-landing`), infra, siti cliente | build verde, deploy verificato |
| `HC-FG-AG-01` nuovi agenti/skill | 07 FORGE | team/skill creati quando un KPI cala sotto soglia per 2 cicli | team a schema canonico, skill ≤500 righe kernel |
| `HC-IN-AG-01` intelligence | 08 INTELLIGENCE | ricerca ICP/nicchie/trend, template second-brain per delivery Second Brain €2.500 | fonti citate, ingest in wiki completato |
| `HC-OP-AG-01` runtime | 09 OPERATIONS | scheduling run giornaliere (email/LI/IG), cost guard, backup `leads.db` | run loggata, budget rispettato, dry-run disponibile |

**Regola di confine (dossier §1):** AGENCY non produce contenuti marketing "grandi" né tooling
in-house — li **richiede** via contract. Produce in-house solo ciò che è quotidiano e operativo
(reparti A5/A6). Un handoff senza acceptance criteria misurabili è INVALIDO (dossier 07 §1.1);
2 reject consecutivi → escalation automatica via gbus.

## 4. GOVERNANCE — Gate di ecosistema

| Gate | Implementazione | Quando |
|---|---|---|
| Gate Bibbia | `bibbia_team.py` (3 checker, ESISTENTE) | ogni messaggio outreach pre-invio + servizio per A5 |
| Gate Preventivo | skill `proposal-gate` | ogni proposta prima dell'invio |
| Gate Delivery | dentro skill `delivery-playbook` | chiusura di ogni delivery (UAT firmata) |
| Brand gate | Sentinel Brand-Voice (corporate, LX) | ogni output esterno |
| verify.sh Empire | `company/orchestrator/verify.sh` (build F2) | struttura, sicurezza, APSOC, costi |

I gate **bloccano, non suggeriscono**: exit 1 = fermo con note correttive. Nessun `--skip`.

## 5. IDENTITY-HR — Registro agenti

I 38 agenti di AGENCY (schede in `Agenti/`) vengono anagrafati in
`company/Backbone/Identity-HR/registro-agenti.yaml` con schema `<ECO>-<REPARTO>-<ruolo>-<seq>`,
tier modello, costo e performance (dossier 07 §1.4). Assunzione/ritiro SOLO via 07 FORGE
(`HC-AG-FG-01` per chiedere organico; la FORGE registra alla creazione). Stato attuale:
roster di ruolo documentato (questa cartella), spawn reale in fase B6.

## 6. OBSERVABILITY — eventi e costi

Eventi standard emessi da AGENCY su `company/metrics/runs.jsonl`: `lead_generated`,
`gate_passed/gate_failed` (Bibbia, Preventivo, Delivery), `handoff_rejected`, `sale_closed`,
`run_done` (per ogni run outreach). Ogni evento porta `{eco: AGENCY, reparto, team, agente,
brand_kit, costo}` — la cost-attribution multi-tenant risponde a "quanto costa servire il
cliente X?". Dashboard: evoluzione di `outreach-dashboard-premium` (fase B5, build via 06 PLATFORM).

---

*Fonti: dossier 01 §1/§7, dossier 07 §1. Divergenze scheletro→dossier risolte a favore del dossier
(namespace completi a 8, topologia per-reparto esplicitata). Aggiornato: 2026-06-11.*
