---
Type: ENTITY
Status: Active
Tags: #reparto #infobusiness #lanci #campagne #launch #IB-L2-LANC
Created: 2026-06-18
Last updated: 2026-06-18
---

# IB-L2-LANC — Lanci & Campagne

> **Livello:** IB-L2-LANC — Reparto di 02-INFO-BUSINESS
> **Namespace AgentDB:** `infobusiness/lanci/`
> **Coordinator:** `IB-COORD-LANCI` (Opus durante sessione lancio attiva)
> **Roster:** 9 agenti · 4 workflow CF-grade
> **Missione-in-una-riga:** orchestrare ogni lancio come operazione militare a calendario
> T-30→T+7 — dry-run obbligatorio, go/no-go formale, gate APSOC verso 04-MARKETING.

---

## Missione

IB-L2-LANC è il **regista operativo del lancio**. Trasforma un prodotto che ha superato il
gate qualità prodotto (WF-CORSO o WF-EBOOK PASS) e un budget approvato da 09-OPERATIONS in
un lancio eseguito al millimetro: pre-lancio (T-30→T-1), cart open (T0→T+4/6), cart close
(ultime 48h), post-lancio (T+7). Un lancio = un workflow CF-grade con dry-run obbligatorio
e go/no-go formale approvato dal director via hive-mind consensus.

**Il reparto NON scrive copy né produce asset creativi.** Quello è di 04-MARKETING (copy)
e 03-CONTENT-FACTORY (asset). IB-L2-LANC dirige la macchina: pianifica il calendario,
compone gli handoff cross-ecosistema, verifica i rientri contro acceptance criteria, esegue
il dry-run e tiene la timeline. Il confine è netto: orchestrazione lancio → IB-L2-LANC;
execution copy → 04-MARKETING; produzione asset → 03-CF.

**Connessione con il Mandato:** ogni copy del lancio passa il gate APSOC ≥80 (≥85 sales page),
ogni scarcity è REALE (Mandato Art.2 — "prove non promesse"), ogni stima costi è approvata
prima del go. Nessun lancio parte con un solo gate rosso.

---

## Posizione nella gerarchia

```
02-INFO-BUSINESS (L1) — ib-director
  └── IB-L2-LANC LANCI & CAMPAGNE ← questo reparto
        │
        ├── riceve da: IB-L2-PROD (prodotto con gate qualità PASS)
        ├── handoff a: 08-INTELLIGENCE (HC-IN-IB-01 — customer research / angoli)
        ├── handoff a: 03-CONTENT-FACTORY (HC-IB-CF-01 — contenuti organici pre-lancio)
        ├── handoff a: 04-MARKETING (HC-IB-MK-01 — sales page + sequenze, gate APSOC)
        ├── handoff a: 09-OPERATIONS (stima costi dry-run, approvazione budget)
        ├── handoff a: IB-L2-COMM (acquirenti post-cart close → WF-ONBOARDING-STUDENTE)
        └── riporta a: ib-director (go/no-go, report lancio, update CATALOGO)
```

---

## Roster agenti (9)

| ID | Agente | Tier | Ruolo sintetico |
|---|---|---|---|
| `IB-COORD-LANCI` | Capo Area Lanci — L2 coordinator | Opus | Regista lancio: pianifica, coordina i 4 WF, emette go/no-go (consensus), riporta a ib-director |
| `IB-LANC-QA` | Verificatore Lanci — QA indipendente | Opus | Gate copy (APSOC ≥80), gate asset-complete, gate dry-run: blocca; mai suggerisce copy |
| `IB-LANC-PLANNER` | Launch Planner | Sonnet | Timeline T-30→T+7 con dipendenze, owner per task, buffer e contingencies |
| `IB-LANC-COPY-LIAISON` | Copy Liaison | Sonnet | Handoff HC-IB-MK-01 a MARKETING; valida rientri vs acceptance; escalation se APSOC <80 |
| `IB-LANC-ASSET` | Asset Checker | Haiku | Checklist asset 100%: page live, checkout testato, email caricate, tracking attivo, link verificati |
| `IB-LANC-WEBINAR` | Webinar Producer | Sonnet | Script webinar + apertura storytelling (base `InfoBusiness/Webinar/`) + replay funnel |
| `IB-LANC-TRACKER` | Launch Tracker | Haiku | Monitoraggio giornaliero conversioni per step durante cart open; report a IB-COORD-LANCI |
| `IB-LANC-DEBRIEF` | Post-Launch Analyst | Sonnet | Post-mortem strutturato: piano vs reale, root cause, pattern → `infobusiness/reasoningbank` |
| `IB-LANC-DRY` | Dry-Run Conductor | Sonnet | Simulazione completa lancio a T-1; stima costi; log risultati; input per go/no-go |

> `IB-COORD-LANCI` riusa e WRAPPA l'agente esistente `IB-LAUNCH-coordinator`
> (`company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-LAUNCH-coordinator.md`, ADR-003): stessa
> identità e missione, promosso a coordinator L2 con gerarchia e workflow CF-grade.

---

## Workflow CF-grade (4)

| Workflow | Scopo sintetico | File |
|---|---|---|
| `WF-LANCIO` | Lancio completo end-to-end T-30→T+7, gate bloccanti a ogni step, go/no-go consensus | `workflow/WF-LANCIO.md` |
| `WF-WEBINAR` | Webinar di vendita come asset di lancio: script, live/registrazione, replay funnel | `workflow/WF-WEBINAR.md` |
| `WF-DEBRIEF-LANCIO` | Post-mortem strutturato → pattern in ReasoningBank, update CATALOGO | `workflow/WF-DEBRIEF-LANCIO.md` |
| `WF-FOLLOWUP-COPY` | Top copy per conversione → libreria evergreen + update template 04-MARKETING | `workflow/WF-FOLLOWUP-COPY.md` |

---

## Skill del reparto

| Skill | Tipo | Priorità | Descrizione |
|---|---|---|---|
| `launch-runbook` | Propria P0 | Nuova da forgiare | Genera calendario T-30→T+7 deterministico + checklist gate per ogni step del lancio |
| `launch` | Ausiliaria esistente | P1 | Playbook lancio — mappata a IB-COORD-LANCI e IB-LANC-PLANNER |
| `market-launch` | Ausiliaria esistente | P1 | Orchestrazione lancio lato marketing — ausiliaria per IB-LANC-COPY-LIAISON |
| `emails` | Ausiliaria esistente | P2 | Supervisione sequenze lancio (cart open/close) — ausiliaria per IB-LANC-COPY-LIAISON |
| `cro-copy-architect` | Ausiliaria esistente | P1 | Riferimento APSOC per il gate IB-LANC-QA (audit, non scrittura) |

Skill `launch-runbook` (P0): da forgiare via 07-FORGE con PRD + architettura prima della build.
Rende deterministico il calendario T-30→T+7 e la checklist gate. Vedi `skills/SKILLS.md`.

---

## KPI presidiati

| KPI | Definizione |
|---|---|
| Aderenza calendario | % task lancio completati entro la data pianificata |
| Conversione lancio | % lista email → acquisto durante cart open |
| Scarto piano vs reale | delta % tra KPI pianificati e KPI reali per ogni step |
| Pattern ReasoningBank / lancio | n. pattern distillati e validati per lancio (min. 3) |
| Delta budget dry-run | scostamento % tra stima costi a T-1 e costo reale (target <10%) |

---

## Handoff principali

| Direzione | Ecosistema/Reparto | Payload tipico |
|---|---|---|
| ← IB-L2-PROD | Prodotto | prodotto con gate qualità PASS (course_id/ebook_id, offer_stack, ICP) |
| → 08-INTELLIGENCE | Intelligence | HC-IN-IB-01: customer research, angoli, language map (Thought Leader Funnel) |
| → 03-CONTENT-FACTORY | Content Factory | HC-IB-CF-01: brief contenuti organici pre-lancio (per pezzo, ICP) |
| → 04-MARKETING | Marketing | HC-IB-MK-01: sales page + sequenze pre-lancio/cart (gate APSOC ≥80) |
| → 09-OPERATIONS | Operations | stima costi dry-run + richiesta approvazione budget (gate Cost-Sentinel) |
| → IB-L2-COMM | Community | coorte acquirenti post-cart close → WF-ONBOARDING-STUDENTE (≤24h) |
| → ib-director | Coordinatore L1 | go/no-go, report lancio, metriche reali per CATALOGO |

**Regola handoff:** nessun lancio parte senza prodotto con gate qualità PASS e budget approvato.
Se il prodotto non ha passato il gate o il budget non è approvato → IB-COORD-LANCI blocca.

---

## Escalation

- **APSOC <80 su copy rientrato:** rework automatico via IB-LANC-COPY-LIAISON, non si pubblica.
  Se 04-MARKETING non rientra entro T-7 → escalation a ib-director.
- **Dry-run con delta costi >10% sulla stima:** IB-LANC-DRY blocca il go/no-go; IB-COORD-LANCI
  rinegozia budget con 09-OPERATIONS o ridefinisce lo scope del lancio.
- **Go/no-go:** hive-mind consensus (ib-director + IB-LANC-QA + Quality-Sentinel +
  Brand-Voice-Sentinel + Cost-Sentinel). UN solo NO blocca il lancio — nessun override.
- **Scarcity non verificabile:** se una deadline o un bonus a scadenza non è reale →
  IB-LANC-QA blocca (Mandato Art.2). Niente scarcity falsa, mai.

---

## Connessioni

- [[02-ECOSISTEMA-INFOBUSINESS-V2]] · `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` §IB-L2-LANC
- [[IB-R2-LANCI]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-R2-LANCI.md` (base wrappata)
- [[IB-LAUNCH-coordinator]] · `company/Ecosistemi/02-INFO-BUSINESS/Agenti/IB-LAUNCH-coordinator.md`
- [[ARCHITETTURA]] · `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/ARCHITETTURA.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 — scarcity reale, prove non promesse)
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` (fornitore copy, gate APSOC)
