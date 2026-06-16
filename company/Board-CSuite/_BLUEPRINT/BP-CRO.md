# BLUEPRINT — CRO (figura C-level = workflow CF-grade)

> Prodotto da ARCHITETTURA (WF-ARCH-DESIGN, ARCH-BOARD-20260616). Per FORGE. Forma: cartella-workflow (PESANTE).

## Forma scelta + perché
Il revenue della holding attraversa più motori (Agency pipeline, InfoBusiness lanci, pricing, retention).
Serve un team con liaison per fonte di ricavo + deal desk + forecast → cartella-workflow ≥10 agenti.

## Missione della figura
Governa il fatturato: pipeline 01-AGENCY (preventivi→proposal), lanci 02-INFO-BUSINESS, pricing (via
team-prezzi), forecast, salute pipeline, cross-sell (info→agency) e retention/LTV. NON scrive il copy
(CMO) né esegue le call: presidia che il revenue entri e cresca.

## Struttura cartella (FORGE)
```
Board-CSuite/CRO/  ├── README.md ARCHITETTURA.md ├── agenti/(10) principi/ regole/ skills/ scripts/ workflow/(≥2) kpi/ state/
```

## Roster agenti (10)
| Agente | Ruolo | Tier |
|---|---|---|
| cro-conductor | coordina il revenue, riporta al CEO | opus |
| cro-agency-pipeline | salute pipeline 01-AGENCY (lead→deal) | sonnet |
| cro-infobusiness-launches | revenue dei lanci 02-INFO-BUSINESS | sonnet |
| cro-deal-desk | preventivi/proposal-gate, struttura offerte | sonnet |
| cro-pricing-arbiter | decisioni prezzo via team-prezzi (B-003) | sonnet |
| cro-forecast-analyst | forecast revenue per fonte | sonnet |
| cro-pipeline-health | conversion per stadio, colli di bottiglia | haiku |
| cro-cross-sell-mapper | lead caldi info→agency | haiku |
| cro-retention-revenue | churn/LTV/win-back (con 02 + SaaS) | sonnet |
| cro-memoria | storico deal, prezzi, motivi win/loss | haiku |

## Workflow CF-grade (≥2)
- `WF-DEAL` — lead → discovery → preventivo (beast-preventivi) → proposal-gate → chiusura → handoff delivery.
- `WF-FORECAST` — pipeline + lanci → forecast trimestrale → priorità revenue al CEO.
- `WF-PRICING` — richiesta prezzo → team-prezzi → ok lotto (delega MAXIMILIAN/CEO) → catalogo aggiornato.

## Skill proprie (FORGE)
`deal-desk` · `revenue-forecast` · `pricing-arbiter` (catalogo fisso, no sconti improvvisati).

## Handoff
→ **01-AGENCY** (pipeline), ↔ **02-INFO-BUSINESS** (lanci+cross-sell), ↔ **CMO** (campagne→lead), → **CFO** (forecast/margini), → **CEO** (priorità revenue).

## KPI presidiati
Deal chiusi/mese · conversion per stadio · revenue forecast vs reale · cross-sell info→agency · LTV/churn.

## Struct-gate checklist
- [ ] ≥10 agenti · [ ] ≥2 workflow · [ ] principi/regole · [ ] ≥3 skill · [ ] scripts · [ ] kpi/state · [ ] 0 magri/0 vuote

## Note per la FORGE
Base dal v1 `CRO.md`. Collegare a 01-AGENCY (outreach pipeline già live) e alle skill beast-preventivi/proposal-gate/discovery-call-brief esistenti.

## Connessioni
- [[BP-INDEX]] · [[BP-CEO]] · [[BP-CMO]] · [[BP-CFO]]
