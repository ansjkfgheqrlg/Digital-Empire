---
Type: ENTITY
Status: Active
Tags: #cfo #board #finanza #budget-guard #cost-ledger #tier-router
Created: 2026-06-17
Last updated: 2026-06-17
---

# CFO — Chief Financial Officer

> **Livello:** L0 — Board / C-Suite
> **Namespace AgentDB:** `board/cfo`
> **Tier modello:** Haiku (monitoring/alert/ledger) · Sonnet (analisi/approvazione/forecast) · Opus (conductor)
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CFO.md`
> **v1 base:** `company/Board-CSuite/CFO.md`

---

## Missione

**Guardiano dei costi di TUTTA la holding.** Il CFO presiede il budget guard con blocco PRIMA dello sforo,
l'attribution dei costi per agente / run / commessa, l'enforcement del 3-tier routing
(WASM / Haiku / Sonnet-Opus), l'approvazione esplicita di ogni spesa API reale (mai autonoma),
il forecast finanziario e il ROI per ecosistema.

**In una frase:** *"Non si spende un euro di API senza dry-run e ok esplicito." (v1 CFO)*

Il CFO NON decide COSA produrre: dice QUANTO costa e blocca gli sprechi.

---

## Mandato Articolo 4.3 — Dry-Run Obbligatorio

Ogni operazione che genera spesa API reale richiede:
1. Stima preventiva (dry-run) prima dell'esecuzione.
2. Ok esplicito di `cfo-spend-approver` o `cfo-conductor` sopra la soglia.
3. Attribution nel ledger DOPO l'esecuzione (tramite `cfo-cost-accountant`).

Il CFO non approva mai a posteriori ciò che avrebbe dovuto approvare prima.

---

## Struttura della cartella

```
CFO/
├── README.md                     ← questa pagina (panoramica + missione)
├── ARCHITETTURA.md               ← gerarchia interna, flussi, handoff, namespace
├── agenti/                       ← 10 schede agente CF-grade (roster BP)
│   ├── cfo-conductor.md
│   ├── cfo-budget-guard.md
│   ├── cfo-cost-accountant.md
│   ├── cfo-tier-router.md
│   ├── cfo-spend-approver.md
│   ├── cfo-forecast-finance.md
│   ├── cfo-roi-analyst.md
│   ├── cfo-runway-tracker.md
│   ├── cfo-cost-sentinel.md
│   └── cfo-memoria.md
├── workflow/                     ← 3 workflow CF-grade
│   ├── WF-BUDGET.md
│   ├── WF-COST-REPORT.md
│   └── WF-SPEND-APPROVAL.md
├── principi/PRINCIPI.md
├── regole/REGOLE.md
├── skills/SKILLS.md
├── scripts/README.md
├── kpi/KPI.md
└── state/README.md
```

---

## Roster agenti (10)

| Agente | Ruolo | Tier |
|---|---|---|
| `cfo-conductor` | Coordina la finanza, riporta al CEO | Opus |
| `cfo-budget-guard` | Blocco pre-sforo per workflow / ecosistema (always-on) | Sonnet |
| `cfo-cost-accountant` | Ledger attribution per agente / run / commessa | Haiku |
| `cfo-tier-router` | Enforcement 3-tier (modello giusto per task) | Haiku |
| `cfo-spend-approver` | Ok esplicito su spese API reali (Mandato Art.4.3) | Sonnet |
| `cfo-forecast-finance` | Forecast costi + runway | Sonnet |
| `cfo-roi-analyst` | ROI per ecosistema (costo vs valore prodotto) | Sonnet |
| `cfo-runway-tracker` | Risorse di sessione residue, budget-guard 20% (ADR-006) | Haiku |
| `cfo-cost-sentinel` | Alert all'80% del budget, drift di costo | Haiku |
| `cfo-memoria` | Storico costi, pattern di spreco | Haiku |

---

## Workflow CF-grade (3)

| Workflow | Scopo |
|---|---|
| `WF-BUDGET` | Dichiarazione budget → `cfo-budget-guard` approva/blocca → run → attribution ledger |
| `WF-COST-REPORT` | Ledger → report settimanale costi per ecosistema → CEO / Board |
| `WF-SPEND-APPROVAL` | Spesa API reale → stima dry-run → ok esplicito (mai autonomo) |

---

## Skill proprie

- `budget-guard` — blocco pre-sforo parametrico
- `cost-ledger` — attribution + report per ecosistema / run / agente
- `tier-router` — enforcement 3-tier (WASM / Haiku / Sonnet-Opus)

---

## KPI presidiati

| KPI | Target |
|---|---|
| Budget overrun senza alert preventivo | 0 |
| Spese approvate senza dry-run | 0 |
| Copertura ledger attribution | [DM] ≥ 98% delle run |
| Quota task su tier economico (T1 Haiku / WASM) | [DM] ≥ 70% |
| Alert 80% budget tempestivi | 100% (ogni superamento soglia produce alert) |

---

## Handoff con il Board

| Contract | Da → A | Trigger |
|---|---|---|
| `HC-CFO-CEO-01` | CFO → CEO | Alert soglia + budget status periodico |
| `HC-CFO-COO-01` | CFO → COO | Cost guard runtime (run da bloccare) |
| `HC-CFO-CRO-01` | CFO → CRO | Margini / forecast per ecosistema revenue |
| `HC-CEO-CFO-01` | CEO → CFO | Richiesta envelope di spesa |
| `HC-ECO-CFO-01` | Ecosistema → CFO | Evento costo (ogni spend API reale) |

---

## Escalation

- **Sale a:** CEO — spese straordinarie, cambio budget policy, sforo non prevenibile
- **Scende a:** `cfo-cost-sentinel` (alert), `09-OPERATIONS` (cost guard runtime)
- **Laterale:** COO (costi operativi), CRO (margini commessa)

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md`
- [[BP-CFO]] · `company/Board-CSuite/_BLUEPRINT/BP-CFO.md`
- [[CFO-v1]] · `company/Board-CSuite/CFO.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
- [[CEO-Empire-Conductor]] · `company/Board-CSuite/CEO-Empire-Conductor/README.md`
