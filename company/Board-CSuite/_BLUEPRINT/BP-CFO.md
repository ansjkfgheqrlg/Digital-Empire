# BLUEPRINT — CFO (figura C-level = workflow CF-grade)

> Prodotto da ARCHITETTURA (WF-ARCH-DESIGN, ARCH-BOARD-20260616). Per FORGE. Forma: cartella-workflow (PESANTE).

## Forma scelta + perché
Il controllo costi della holding (budget guard, attribution, 3-tier routing, approvazione spese) è
un sistema always-on con blocco pre-sforo. Serve un team con sentinel costi + accountant + router → cartella-workflow ≥10 agenti.

## Missione della figura
Guardiano dei costi di TUTTA la holding: budget guard con blocco PRIMA dello sforo, cost attribution
per agente/run/commessa, enforcement 3-tier (WASM/Haiku/Sonnet-Opus), approvazione spese API reali,
forecast finanziario, ROI per ecosistema. NON decide COSA produrre: dice QUANTO costa e blocca gli sprechi.

## Struttura cartella (FORGE)
```
Board-CSuite/CFO/  ├── README.md ARCHITETTURA.md ├── agenti/(10) principi/ regole/ skills/ scripts/ workflow/(≥2) kpi/ state/
```

## Roster agenti (10)
| Agente | Ruolo | Tier |
|---|---|---|
| cfo-conductor | coordina la finanza, riporta al CEO | opus |
| cfo-budget-guard | blocco pre-sforo per workflow/ecosistema (always-on) | sonnet |
| cfo-cost-accountant | ledger attribution per agente/run/commessa | haiku |
| cfo-tier-router | enforcement 3-tier (modello giusto per task) | haiku |
| cfo-spend-approver | ok esplicito su spese API reali (pattern #3) | sonnet |
| cfo-forecast-finance | forecast costi + runway | sonnet |
| cfo-roi-analyst | ROI per ecosistema (costo vs valore prodotto) | sonnet |
| cfo-runway-tracker | risorse di sessione residue, budget-guard 20% (ADR-006) | haiku |
| cfo-cost-sentinel | alert all'80% del budget, drift di costo | haiku |
| cfo-memoria | storico costi, pattern di spreco | haiku |

## Workflow CF-grade (≥2)
- `WF-BUDGET` — workflow dichiara budget → cfo-budget-guard approva/blocca → run → attribution nel ledger.
- `WF-COST-REPORT` — ledger → report settimanale costi per ecosistema al CEO/Board.
- `WF-SPEND-APPROVAL` — spesa API reale → stima dry-run → ok esplicito (mai autonomo).

## Skill proprie (FORGE)
`budget-guard` (blocco pre-sforo) · `cost-ledger` (attribution + report) · `tier-router`.

## Handoff
← tutti gli ecosistemi (eventi costo), ↔ **COO** (run/costi), ↔ **CRO** (margini/forecast), → **CEO** (report), → **09-OPERATIONS** (cost guard runtime).

## KPI presidiati
0 sforamenti budget (blocco funziona) · copertura ledger ≥98% · quota task su tier economico ≥70% · alert 80% tempestivi.

## Struct-gate checklist
- [ ] ≥10 agenti · [ ] ≥2 workflow · [ ] principi/regole · [ ] ≥3 skill · [ ] scripts · [ ] kpi/state · [ ] 0 magri/0 vuote

## Note per la FORGE
Base dal v1 `CFO.md`. Collegare a 09-OPERATIONS (cost guard runtime) e alle skill budget-guard/cost-ledger previste. cfo-runway-tracker applica l'ADR-006 (budget-guard 20%).

## Connessioni
- [[BP-INDEX]] · [[BP-CEO]] · [[BP-COO]] · [[BP-CRO]]
