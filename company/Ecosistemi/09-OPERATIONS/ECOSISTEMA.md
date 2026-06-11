# 🔧 09 — OPERATIONS · Runtime & Cost Guard della Holding

> **Livello:** L1 · **Priorità:** TRASVERSALE (core) · **Stato:** parziale (ruflo installato, swarm non inizializzato, run outreach attive ma lanciate a mano)
> **Dossier vincolante:** `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §09 OPERATIONS
> **Supervisione C-Suite:** COO (operatività) + CFO (budget) · **Topologia swarm:** mesh (vedi `BACKBONE.md`)

## 1. Missione

OPERATIONS è il **runtime di EMPIRE OS**: esegue la produzione di massa (swarm),
schedula i flussi ricorrenti (cron/loop), fa da **guardiano dei costi di TUTTA la
holding** (budget guard + cost attribution per agente/ecosistema/commessa), gestisce
storage e asset, monitora i processi e dà alla Board una dashboard unica.

**OPERATIONS non decide COSA produrre** (lo decidono i 5 ecosistemi business) **ma COME
gira e QUANTO costa.** È la metafora OS di "scheduler + power management": senza di lui
costi fuori controllo, run manuali, zero osservabilità.

### DONE WHEN (misurabili — dal dossier)

1. Ogni run (outreach, build siti, ingestioni, content) emette evento standard
   `{ecosistema, workflow, costo, durata, esito}` raccolto in un **ledger unico**.
2. **Budget guard attivo**: nessun workflow può sforare il budget dichiarato — blocco
   PRIMA dello sforo (pattern #9), dry-run default (pattern #3).
3. Le run outreach giornaliere (`avvia-email`, `avvia-ig`, `avvia-parallel`) girano
   **schedulate e monitorate**, non più lanciate a mano.
4. **Dashboard unica**: stato run, costi per ecosistema, alert sentinels — leggibile
   in 30 secondi dalla Board.

## 2. Posizione nella holding — handoff

| Da → A | Contratto di handoff |
|---|---|
| QUALSIASI → OPERATIONS | `{workflow, parametri, budget_max, schedule}` → run eseguita/schedulata + report `{esito, costo, durata}` |
| OPERATIONS → QUALSIASI | alert: budget all'80%, run fallita, drift di costo, processo zombie |
| OPERATIONS → INTELLIGENCE | log e metriche delle run → ReasoningBank + wiki (post-mortem) |
| OPERATIONS → Board (L0) | report costi settimanale per ecosistema + dashboard |
| FORGE → OPERATIONS | nuovo agente/team → registrazione nel cost model (tier, costo stimato/run) |
| OPERATIONS → PLATFORM | richieste tooling (script scheduling, dashboard) — OPERATIONS le usa, PLATFORM le scrive |
| OPERATIONS → MEMORY | ogni run chiusa → HC-ME-POST con costi (il CP include la voce "Costi") |

**Regola d'oro dei core:** OPERATIONS è multi-tenant per definizione (pattern #11) —
misura i costi di DE stessa, dei clienti agency, dei canali YouTube, dei libri KDP,
con attribution per `brand_kit`/commessa.

## 3. Organigramma L2 → L5

```
09-OPERATIONS  (ops-director — L1)
├─ L2 RUNTIME                       → Reparti/RUNTIME/
│   ├─ L3 WF-SWARM-RUN              → Workflow/WF-SWARM-RUN/
│   │     L4: T-fanout · T-worker-pool · T-merge-results · T-retry-failed → Funzioni/
│   └─ L3 WF-QUEUE                  → Workflow/WF-QUEUE/
├─ L2 SCHEDULING                    → Reparti/SCHEDULING/
│   ├─ L3 WF-CRON                   → Workflow/WF-CRON/
│   └─ L3 WF-LOOP                   → Workflow/WF-LOOP/
├─ L2 COST-GUARD (guardiano della holding intera) → Reparti/COST-GUARD/
│   ├─ L3 WF-BUDGET                 → Workflow/WF-BUDGET/
│   ├─ L3 WF-ATTRIBUTION            → Workflow/WF-ATTRIBUTION/
│   └─ L3 WF-TIER-ROUTING           → Workflow/WF-TIER-ROUTING/
├─ L2 STORAGE-ASSETS                → Reparti/STORAGE-ASSETS/
│   ├─ L3 WF-ASSET-MGMT             → Workflow/WF-ASSET-MGMT/
│   └─ L3 WF-BACKUP                 → Workflow/WF-BACKUP/
└─ L2 MONITORING-DASHBOARD          → Reparti/MONITORING-DASHBOARD/
    ├─ L3 WF-WATCH                  → Workflow/WF-WATCH/
    └─ L3 WF-DASHBOARD              → Workflow/WF-DASHBOARD/
```

## 4. Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | RUNTIME | produzione di massa via swarm: fan-out, worker pool, merge, retry; render/job queue | `Reparti/RUNTIME/` |
| L2.2 | SCHEDULING | run ricorrenti (cron) e loop su condizione; le run outreach passano di qui | `Reparti/SCHEDULING/` |
| L2.3 | COST-GUARD | budget per workflow/ecosistema, blocco pre-sforo, attribution, 3-tier routing | `Reparti/COST-GUARD/` |
| L2.4 | STORAGE-ASSETS | asset (immagini, video, export): naming, dedup, retention + backup/restore | `Reparti/STORAGE-ASSETS/` |
| L2.5 | MONITORING-DASHBOARD | health check processi + dashboard unica della holding per la Board | `Reparti/MONITORING-DASHBOARD/` |

## 5. Roster agenti L5 (10 — il più Haiku-heavy della holding)

| ID | Ruolo | Reparto | Tier | Scheda |
|---|---|---|---|---|
| `ops-director` | Direttore OPERATIONS — SLA run, priorità code, report Board | tutto l'ecosistema | Opus | `Agenti/ops-director.md` |
| `ops-swarm-marshal` | Orchestrazione swarm: fan-out, parallel N, merge | RUNTIME | Sonnet | `Agenti/ops-swarm-marshal.md` |
| `ops-scheduler` | Cron/loop: pianifica e lancia run ricorrenti | SCHEDULING | Haiku | `Agenti/ops-scheduler.md` |
| `ops-cost-sentinel` | Sentinel always-on: budget guard, blocco pre-sforo, alert 80% | COST-GUARD | Sonnet | `Agenti/ops-cost-sentinel.md` |
| `ops-cost-accountant` | Ledger: attribution per agente/run/commessa/ecosistema | COST-GUARD | Haiku | `Agenti/ops-cost-accountant.md` |
| `ops-tier-router` | Enforcement 3-tier routing + Thompson Sampling (via Ruflo) | COST-GUARD | Haiku | `Agenti/ops-tier-router.md` |
| `ops-asset-keeper` | Storage, naming, dedup, retention asset | STORAGE-ASSETS | Haiku | `Agenti/ops-asset-keeper.md` |
| `ops-backup-op` | Backup + restore test periodico | STORAGE-ASSETS | Haiku | `Agenti/ops-backup-op.md` |
| `ops-watchdog` | Health check: run, daemon, token, processi zombie | MONITORING-DASHBOARD | Haiku | `Agenti/ops-watchdog.md` |
| `ops-dashboard-builder` | Mantiene dashboard (con PLATFORM per il codice) | MONITORING-DASHBOARD | Sonnet | `Agenti/ops-dashboard-builder.md` |

**Nota tier (dal dossier):** OPERATIONS deve costare poco per definizione — lavoro
ripetitivo e schematico → 6 agenti su 10 sono Haiku. Predica col proprio esempio.

## 6. Asset esistenti → reparto (regola: WRAP, mai riscrittura — ADR-003)

| Path | Reparto | Azione |
|---|---|---|
| `Outreach/` run scripts (`run_parallel.py`, `run_ig_email.py`, `run_all.bat`, `AVVIA-*.bat`) | SCHEDULING | **WRAPPA** — schedulare e monitorare SENZA modificare (workflow attivi: 6 team Nemotron $0/giorno) |
| skill `avvia-email`, `avvia-ig`, `avvia-linkedin`, `avvia-parallel`, `avvia-scraper` | SCHEDULING / WF-CRON | **USA** — trigger ufficiali delle run |
| `Outreach/outreach-dashboard-premium/` + `start-dashboard.bat` | MONITORING / WF-DASHBOARD | **EVOLVI** — da dashboard outreach a dashboard holding |
| Pattern CF `swarm.sh --parallel N --budget N` (repo Content Factory Exponium) | RUNTIME | **PORTA** — riscrivere versione DE (si porta il pattern, non il file) |
| Pattern CF render queue + cost attribution | RUNTIME / COST-GUARD | **PORTA** — idem |
| Ruflo: `task_orchestrate`, `swarm_init`, 3-tier routing, daemon | RUNTIME / COST-GUARD | **USA** — con fallback bash auto-riparante (rischio #5: daemon Windows) |
| skill `loop`, `schedule` (cloud agents cron) | SCHEDULING | **USA** |
| skill `hooks-automation`, `workflow-automation`, `update-config` | SCHEDULING / MONITORING | **USA** |
| `Outreach/SISTEMA_OUTREACH_COMPLETO.md` | MONITORING | **USA** come runbook di riferimento |
| `scripts/empire-sync.ps1` (sync Max↔Gael, ADR-004) | MONITORING / WF-WATCH | **USA** — già attivo, il watchdog ne verifica l'esito |

## 7. Skill: esistenti + da forgiare (ordini alla FORGE)

**Esistenti:** avvia-email, avvia-ig, avvia-linkedin, avvia-parallel, avvia-scraper,
loop, schedule, hooks-automation, workflow-automation, update-config.

| Skill nuova | Scopo | Priorità |
|---|---|---|
| `empire-swarm` | swarm.sh versione DE: `--parallel N --budget N --dry-run`, fan-out + merge + retry | ALTA |
| `cost-ledger` | ledger eventi costo + report settimanale per ecosistema | ALTA |
| `budget-guard` | dichiarazione budget per workflow + blocco pre-sforo + ok umano per spese API | ALTA |
| `empire-watchdog` | health check schedulato: run, daemon Ruflo, token (es. FB scaduto), disco | MEDIA |
| `asset-vault` | convenzioni storage + dedup + retention per asset multi-ecosistema | MEDIA |

## 8. KPI + Quality Gates

| KPI | Target |
|---|---|
| Sforamenti budget | 0 (il blocco pre-sforo funziona) |
| Run schedulate completate senza intervento | ≥ 95% |
| Costo attribuito / costo totale (copertura ledger) | ≥ 98% |
| Tempo rilevazione run fallita (watchdog) | ≤ 15 min |
| Quota task su tier economico (WASM/Haiku) | ≥ 70% |
| Restore backup testato | 1/mese, verde |

**Gates (non bypassabili):**
`G-DRYRUN` (ogni workflow nuovo gira prima in dry-run con stima costi) →
`G-BUDGET` (budget dichiarato e approvato prima della run reale) →
`G-ATTRIBUTION` (run senza evento costo = run NON valida) →
`G-RUNBOOK` (ogni workflow schedulato ha runbook e procedura di rollback).

## 9. Fasi di build

| Fase | Cosa | Gate |
|---|---|---|
| O1 | `cost-ledger` + eventi costo dai flussi esistenti (outreach, build siti) | primo report settimanale reale |
| O2 | `budget-guard` su tutti i workflow censiti; dry-run default | un blocco pre-sforo testato |
| O3 | Scheduling outreach: avvia-* sotto WF-CRON + `empire-watchdog` (incl. alert token FB) | 7 giorni di run senza lancio manuale |
| O4 | `empire-swarm` (pattern CF portato): prima produzione di massa reale | batch completato entro budget |
| O5 | Dashboard holding (evoluzione outreach-dashboard-premium) + report Board automatico | dashboard live |

## 10. Nota di allineamento al dossier

Lo scheletro iniziale di questa pagina elencava 4 reparti (Swarm Engine, Budget Guard,
Scheduling, Storage). Il dossier `06-ECOSISTEMI-CORE.md` §09 — fonte vincolante — ne
definisce **5** (RUNTIME, SCHEDULING, COST-GUARD, STORAGE-ASSETS, MONITORING-DASHBOARD):
questa pagina e le sottocartelle seguono il dossier. Il "Monitoring & Dashboard",
assente nello scheletro, è il reparto che rende OPERATIONS osservabile dalla Board.

## Connessioni

- `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §09 — dossier completo
- `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md` — Bus, Brain, topologie, 3-tier routing
- `company/Ecosistemi/10-MEMORY/` — ogni run chiusa scrive CP con costi (pattern #13)
- `company/Sentinels/Cost-Sentinel/` — la sentinella LX che OPERATIONS alimenta col ledger
- `company/Board-CSuite/CFO.md` + `COO.md` — supervisori C-Suite

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` · Aggiornato: 2026-06-11*
