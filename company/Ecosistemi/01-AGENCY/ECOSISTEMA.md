# 🏢 01 — AGENCY (Ecosistema L1 di EMPIRE OS)

> **Livello:** L1 · **Priorità:** ALTA · **Stato:** ATTIVO (outreach 3 canali live, landing + presentazione live)
> Dossier vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` · Runtime operativo: `company/01-agency/` (Gael — NON toccare)
> Questo file è la carta d'identità organizzativa dell'ecosistema dentro `company/Ecosistemi/`.

---

## 1. Missione

Acquisire e servire clienti delle 3 implementazioni AI di Digital Empire —
**Outreach Factory €4.000 · Content Factory €3.500 · Second Brain €2.500 · bundle Engine Room €8.000** —
con modello **one-time, €0 canoni, codice di proprietà del cliente, setup in 7 giorni, supporto 90 giorni**.

Posizionamento: **"l'agenzia progettata per essere licenziata"** — il cliente esce dal delivery
autonomo, non dipendente. AGENCY è il pilastro revenue della holding: tutti gli altri 9 ecosistemi
la alimentano (lead, copy, asset, tooling, intelligence) o la amplificano (case study, autorità).

## 2. DONE WHEN (criteri misurabili — dal dossier §0)

| # | Criterio | Verifica |
|---|---|---|
| 1 | 6 reparti L2 esistono in `company/01-agency/` con BACKBONE.md e team L3/L4 a schema canonico | struttura navigabile, schema coordinator+I/O+acceptance+failure+shared_state |
| 2 | Pipeline outreach esistente (email 500/gg cap 100/h · LinkedIn 20+20+30/gg · IG 30 DM/gg) gira INVARIATA, wrappata come team L3 con handoff contract + log Ruflo | zero regressioni sulle run reali |
| 3 | Ogni discovery call → preventivo problem-first entro 48h, dal flusso A3 (non a mano), passato dal Gate Preventivo | timestamp call→invio ≤48h |
| 4 | Delivery Playbook eseguibile per i 3 prodotti: discovery → setup server cliente → training → handover, in ≤7gg, con checklist UAT firmabile | dry-run completo su ambiente di test |
| 5 | Flusso end-to-end lead→outreach→call→preventivo→contratto→delivery→supporto 90gg→testimonianza percorribile e tracciato | ogni step ha owner, gate e record in `agency/*` |
| 6 | Dashboard KPI per reparto visibile (evoluzione di `outreach-dashboard-premium`) | KPI sez. 6 alimentati da dati reali |
| 7 | ReasoningBank riceve ogni fallimento (bounce, preventivo perso, delivery in ritardo) come pattern distillato | entry in `agency/reasoning` |

**OUT OF SCOPE (ora):** aumento cap outreach senza dati · nuovi prodotti/pricing ·
automazione della discovery call (resta umana, su Max) · riscrittura della pipeline email attiva.

## 3. Org chart testuale L2 → L5

```
AG-DIR (Direttore ecosistema, opus) ── riporta a L0 Board/C-Suite
│
├── A1 RICERCA ─────────────── AG-A1-COORD (sonnet)
│     L3  WF-LEAD-SOURCING · WF-MARKET-INTEL
│     L4  T-scraper · T-extractor · T-qualifier · T-icp-profiler · T-competitor-profiler
│     L5  AG-A1-SCRAPE-W · AG-A1-EXTRACT-W · AG-A1-QUAL-W · AG-A1-ICP-W · AG-A1-COMP-W
│
├── A2 ACQUISIZIONE/OUTREACH ─ AG-A2-COORD (sonnet, oggi orchestrator.py)
│     L3  WF-OUTREACH-EMAIL (ESISTENTE, NON SI TOCCA) · WF-OUTREACH-LINKEDIN ·
│         WF-OUTREACH-INSTAGRAM · WF-REPLY-FOLLOWUP
│     L4  T-strategist · T-writer-apsoc · T-bibbia-qa · T-sender · T-reply-triage ·
│         T-followup · T-li-engage · T-ig-dm
│     L5  AG-A2-STRAT-W · AG-A2-WRITE-W · AG-A2-BIBBIA-C1/C2/C3 · AG-A2-SEND-W ·
│         AG-A2-TRIAGE-W · AG-A2-FUP-W · AG-A2-LI-W · AG-A2-IG-W
│
├── A3 PREVENTIVI ──────────── AG-A3-COORD (opus)
│     L3  WF-PREVENTIVO
│     L4  T-discovery-brief · T-problem-audit · T-proposal-writer · T-pricing-config · T-proposal-qa
│     L5  AG-A3-BRIEF-W · AG-A3-AUDIT-W · AG-A3-PROP-W · AG-A3-PRICE-W · AG-A3-QA-W
│
├── A4 OPERATIVITÀ/DELIVERY ── AG-A4-COORD (opus)
│     L3  WF-DELIVERY-OUTREACH-FACTORY · WF-DELIVERY-CONTENT-FACTORY ·
│         WF-DELIVERY-SECOND-BRAIN · WF-SUPPORTO-90GG
│     L4  T-env-setup · T-config-tenant · T-uat-runner · T-training-kit · T-handover-pack · T-support-triage
│     L5  AG-A4-ENV-W · AG-A4-TENANT-W · AG-A4-UAT-W · AG-A4-TRAIN-W · AG-A4-HAND-W · AG-A4-SUPP-W
│
├── A5 COPYWRITING-INTERNO ─── AG-A5-COORD (sonnet)
│     L3  WF-COPY-OUTREACH
│     L4  T-apsoc-writer · T-objection-handler · T-copy-qa (riusa il gate Bibbia di A2)
│     L5  AG-A5-COPY-W · AG-A5-OBJ-W
│
└── A6 MARKETING-INTERNO ───── AG-A6-COORD (sonnet)
      L3  WF-ASSET-VETRINA · WF-CASE-STUDY
      L4  T-proof-collector · T-case-writer · T-upsell-mapper
      L5  AG-A6-PROOF-W · AG-A6-CASE-W · AG-A6-UPSELL-W
```

Roster completo: 38 schede in `Agenti/` (AG-DIR + 6 coordinator + 31 worker, di cui i 3 checker
Bibbia censiti come C1/C2/C3). I Sentinels (Cost, Quality, Drift, Security, Brand-Voice) sono
**corporate** (LX/Backbone): osservano AGENCY via Observability, NON sono duplicati qui.

## 4. Offerta e reparti

| Prodotto | Prezzo | Delivery |
|---|---|---|
| Outreach Factory | €4.000 | `WF-DELIVERY-OUTREACH-FACTORY` (clone pipeline DE, multi-tenant) |
| Content Factory | €3.500 | `WF-DELIVERY-CONTENT-FACTORY` (motore da 03 CF via `HC-AG-CF-01`) |
| Second Brain | €2.500 | `WF-DELIVERY-SECOND-BRAIN` (template da 08 INTELLIGENCE via `HC-IN-AG-01`) |
| Engine Room (bundle) | €8.000 | i 3 delivery in sequenza coordinata |

| # | Reparto | Missione sintetica | Path |
|---|---|---|---|
| A1 | Ricerca | lead qualificati + intelligence di nicchia per vendere e consegnare meglio | `Reparti/A1-Ricerca/` |
| A2 | Acquisizione/Outreach | lead → discovery call prenotate su 3 canali, dentro i cap reali | `Reparti/A2-Acquisizione/` |
| A3 | Preventivi | call → proposta problem-first ≤48h, pricing a catalogo, Gate Preventivo | `Reparti/A3-Preventivi/` |
| A4 | Delivery | 3 prodotti consegnati in ≤7gg + supporto 90gg, cliente autonomo a fine handover | `Reparti/A4-Delivery/` |
| A5 | Copywriting-interno | copy operativo quotidiano APSOC; i pezzi grandi si chiedono a 04 MARKETING | `Reparti/A5-Copywriting-Interno/` |
| A6 | Marketing-interno | vetrina, case study, testimonianze, upsell mapping | `Reparti/A6-Marketing-Interno/` |

## 5. Flusso operativo tipo (la pipeline revenue — dossier §4)

```
[A1] LEAD ──► [A2] OUTREACH ──► [A2] REPLY/FOLLOW-UP ──► CALL ──► [A3] PREVENTIVO ──► CONTRATTO
                                                                                          │
   TESTIMONIANZA / UPSELL [A6] ◄── SUPPORTO 90GG [A4] ◄── DELIVERY ≤7GG [A4] ◄────────────┘
```

| # | Step | Owner | Input → Output | Gate |
|---|---|---|---|---|
| 1 | Sourcing & qualifica | A1 `WF-LEAD-SOURCING` | fonti → lead qualificato in `leads.db` con score ICP | qualifier score ≥ soglia |
| 2 | Outreach multicanale | A2 (3 WF) | lead → messaggi inviati (email ≤500/gg cap 100/h · LI 20+20+30 · IG 30 DM). CTA: presentazione-empire.vercel.app | **Gate Bibbia** (blocca invio) |
| 3 | Reply & follow-up | A2 `WF-REPLY-FOLLOWUP` | risposta → conversazione gestita → call prenotata | triage corretto; mai rispondere a un "no" |
| 4 | Discovery call | **UMANO (Max)** + AG-A3-BRIEF-W (dossier pre-call) | call → trascrizione/appunti | dossier pre-call consegnato prima della call |
| 5 | Preventivo | A3 `WF-PREVENTIVO` | brief → proposta problem-first inviata ≤48h | **Gate Preventivo** |
| 6 | Contratto | UMANO + T-pricing-config | proposta → firma + pagamento one-time | pagamento verificato; scope congelato |
| 7 | Delivery ≤7gg | A4 `WF-DELIVERY-*` | discovery tecnica → setup sul server del cliente → run test → training → handover codice | **Gate Delivery** (UAT firmata) |
| 8 | Supporto 90gg | A4 `WF-SUPPORTO-90GG` | ticket/check settimanali → risoluzioni loggate | SLA rispettato; log completo |
| 9 | Testimonianza & upsell | A6 `WF-CASE-STUDY` + T-upsell-mapper | fine supporto → testimonianza + case study + proposta upsell | "prove non promesse": solo metriche reali |

Ogni freccia = handoff contract sul BUS intra-ecosistema; ogni fallimento → record
ReasoningBank in `agency/reasoning` con causa distillata (pattern #5).

## 6. KPI per reparto (misurare, non inventare — dossier §8)

| Reparto | KPI | Cap/vincolo reale |
|---|---|---|
| A1 | lead qualificati/gg · % qualifica su scraped · freschezza dati | — |
| A2 | inviati/gg per canale · reply rate · positive reply rate · call prenotate/sett | email ≤500/gg cap 100/h · LI 20 connect+20 msg+30 commenti/gg · IG 30 DM/gg |
| A3 | tempo call→preventivo (≤48h) · win rate · valore medio preventivo | pricing a catalogo: 4.000/3.500/2.500/8.000 € |
| A4 | giorni delivery (≤7) · UAT pass al primo giro · ticket in SLA · NPS fine 90gg | setup ≤7gg, supporto 90gg (promessa commerciale) |
| A5 | % copy passato al gate Bibbia al primo giro · tempo brief→copy | — |
| A6 | case study per cliente chiuso · call da inbound · testimonianze raccolte | — |

I CAP sono limiti operativi attivi e reali; i TASSI si misurano dal giorno 1 e diventano
baseline. La FORGE interviene (via `HC-AG-FG-01`) quando un KPI cala sotto soglia per 2 cicli.

## 7. Quality gates (pattern #4 — niente esce senza gate)

| Gate | Stato | Cosa blocca |
|---|---|---|
| **Gate Bibbia** | ESISTENTE (`bibbia_team.py`, 3 checker) | ogni messaggio outreach pre-invio: conformità copy, struttura, firma/CTA. Esteso come servizio ad A5. *Blocca, non suggerisce.* |
| **Gate Preventivo** | skill `proposal-gate` (installata) | problem-first verificato, awareness corretto, pricing solo a catalogo, promesse = solo prove, scope 7gg esplicito, clausola proprietà codice + €0 canoni, supporto 90gg definito, brand voice |
| **Gate Delivery** | dentro skill `delivery-playbook` (installata) | workflow funzionante SUL SERVER DEL CLIENTE, run test reale, training erogato, handover pack completo, UAT firmata, zero dipendenze residue da DE |
| **Brand gate corporate** | Sentinel Brand-Voice (LX) | trasversale su tutto l'output esterno (Mandato Empire) |

## 8. Fasi di build (dossier §9 — allineate a F3-F4 del Piano Maestro)

| Fase | Cosa | Gate di validazione |
|---|---|---|
| **B0** | Inventario asset (tabella dossier §5 file-per-file), ingest doc in wiki, fix operativi (rinnovo token FB) | zero orfani; wiki/log aggiornato |
| **B1** | Scaffolding `company/01-agency/` — 6 reparti, BACKBONE, handoff contract scritti come schema | struttura navigabile; verify Empire verde |
| **B2** | Wrap dei 4 WF outreach come team L3 (contract + log memoria attorno al runtime INVARIATO) | run reale identica a prima del wrap; eventi in `agency/outreach` |
| **B3** | A3 live: `discovery-call-brief` + beast-preventivi orchestrato + `proposal-gate` | 1 preventivo reale dal flusso, gate passato, ≤48h dalla call |
| **B4** | A4: `delivery-playbook` ×3 prodotti + `client-handover` + `support-90` | dry-run delivery Outreach Factory su server non-DE con UAT compilata |
| **B5** | A1 potenziata (`icp-radar`) + A6 (`case-study-forge`, `upsell-mapper`) + dashboard KPI 6 reparti | KPI sez. 6 visibili e alimentati da dati reali |
| **B6** | Agenti reali: `agent_spawn` dei coordinator, hive-mind cross-reparto, ReasoningBank loop | **= Gate F4 Piano Maestro**: end-to-end lead→preventivo orchestrato e tracciato |
| **B7** | Primo delivery cliente reale gestito dal sistema + primo case study | Gate Delivery firmato; case study pubblicato; pattern in ReasoningBank |

Regola ferrea su B2: il sistema outreach è ATTIVO e produce valore — ogni wrapper si valida
in dry-run e su batch piccolo prima di toccare la run da 500.

## 9. Sistemi attivi (NON toccare — ADR-003)

| Sistema | Path | Azione F3 |
|---|---|---|
| Pipeline email (scraper→qualifier→strategist→writer→Bibbia→sender) | `Outreach/Outreach Workflow/` | **wrappa** (WF-LEAD-SOURCING + WF-OUTREACH-EMAIL + WF-REPLY-FOLLOWUP) |
| LinkedIn Automation (script 01→05 + comment_posts.py) | `Outreach/LinkedIn Automation/` | **wrappa** (WF-OUTREACH-LINKEDIN) |
| Instagram Automation | `Outreach/Instagram Automation/` | **wrappa** (WF-OUTREACH-INSTAGRAM) |
| leads.db | `Outreach/Outreach Workflow/leads.db` | **usa-così** + backup via `HC-AG-OP-01` |
| Dashboard Next.js | `Outreach/outreach-dashboard-premium/` | **evolvi** → dashboard KPI 6 reparti (via 06 PLATFORM) |
| Landing + presentazione | `agency-empire-landing/` + presentazione-empire.vercel.app | **usa-così** (CTA standard outreach) |

## 10. Blocchi noti

- **Token FB scaduto** → rinnovo in fase B0 (runbook in `HC-AG-OP-01`, check pre-flight di ogni run).
- **Collo di bottiglia umano**: discovery call e firma restano su Max — mitigato dal dossier pre-call
  automatico (A3) e dal preventivo ≤48h; il resto del funnel non aspetta l'umano.
- Dashboard KPI: ancora outreach-only, evoluzione pianificata in B5.

---

## Connessioni

- `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` — dossier vincolante (fonte di questo file)
- `BACKBONE.md` (questa cartella) — namespace, topologie swarm, handoff contract con gli altri ecosistemi
- `Reparti/` · `Workflow/` · `Funzioni/` · `Agenti/` — articolazione L2→L5
- `company/01-agency/` — runtime operativo (Gael) — non modificare da qui
- [[Concept_Pivot_Implementazioni_AI]] · [[Agency_Empire_Landing]] — wiki

*Fonte: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` v1.0 · Aggiornato: 2026-06-11*
