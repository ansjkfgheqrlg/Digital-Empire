---
Type: ENTITY
Status: Active
Tags: #cro #board #revenue #pipeline #agency #infobusiness #pricing #forecast
Created: 2026-06-17
Last updated: 2026-06-17
---

# CRO — Chief Revenue Officer

> **Livello:** L0 — Board/C-Suite
> **Namespace AgentDB:** `board/cro`
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CRO.md`
> **Conductor:** `cro-conductor` (Opus)
> **Roster:** 10 agenti · 3 workflow · cartella-workflow CF-grade

---

## Missione

Il CRO governa tutto il fatturato della holding: presidiando la pipeline Agency (01-AGENCY),
i lanci InfoBusiness (02-INFO-BUSINESS), il pricing tramite team-prezzi (B-003), il forecast
trimestrale e il cross-sell info→agency. NON scrive copy (CMO), NON esegue le call (Max):
assicura che il revenue **entri e cresca** in modo strutturato e tracciato.

**In una frase:** *"Non mi interessa quante opportunità esistono — mi interessa quante si chiudono,
a quale prezzo, con quale margine, e cosa stiamo imparando da ogni win e da ogni loss."*

---

## Perché cartella-workflow (CF-grade)

Il revenue della holding attraversa più motori indipendenti (pipeline Agency, lanci InfoBusiness,
pricing, retention/LTV). Serve un team con liaison per ciascuna fonte di ricavo + deal desk +
forecast. A file singolo non basta: ci vogliono ≥10 agenti con schede millimetriche, ≥2 workflow
CF-grade, state tracciato e skill proprie. Standard: Content Factory Exponium = 1 workflow.

---

## Roster agenti (10)

| Agente | Tier | Ruolo sintetico |
|---|---|---|
| `cro-conductor` | Opus | Coordina il revenue, riporta al CEO |
| `cro-agency-pipeline` | Sonnet | Salute pipeline 01-AGENCY (lead→deal) |
| `cro-infobusiness-launches` | Sonnet | Revenue lanci 02-INFO-BUSINESS |
| `cro-deal-desk` | Sonnet | Preventivi/proposal-gate, struttura offerte |
| `cro-pricing-arbiter` | Sonnet | Decisioni prezzo via team-prezzi (B-003) |
| `cro-forecast-analyst` | Sonnet | Forecast revenue per fonte |
| `cro-pipeline-health` | Haiku | Conversion per stadio, colli di bottiglia |
| `cro-cross-sell-mapper` | Haiku | Lead caldi info→agency |
| `cro-retention-revenue` | Sonnet | Churn/LTV/win-back (con 02 + SaaS) |
| `cro-memoria` | Haiku | Storico deal, prezzi, motivi win/loss |

---

## Workflow CF-grade (3)

| Workflow | Scopo |
|---|---|
| `WF-DEAL` | Lead → discovery → preventivo → proposal-gate → chiusura → handoff delivery |
| `WF-FORECAST` | Pipeline + lanci → forecast trimestrale → priorità revenue al CEO |
| `WF-PRICING` | Richiesta prezzo → team-prezzi → ok lotto → catalogo aggiornato |

---

## Handoff

| Direzione | Ecosistema | Payload |
|---|---|---|
| → | 01-AGENCY | Pipeline deal aperti, win/loss, KPI conversion |
| ↔ | 02-INFO-BUSINESS | Lanci + cross-sell info→agency |
| ↔ | CMO (04-MARKETING) | Campagne→lead in ingresso; brief briefing copy commerciale |
| → | CFO | Forecast/margini per budget |
| → | CEO | Priorità revenue, escalation decisioni di pricing |

---

## Offerta corrente (Mandato Art.3 — invariante fino a nuovo ADR)

| Prodotto | Prezzo | Stato |
|---|---|---|
| Outreach Factory | €4.000 | ATTIVO |
| Content Factory | €3.500 | ATTIVO |
| Second Brain | €2.500 | ATTIVO |
| Engine Room (bundle tutti e 3) | €8.000 | ATTIVO |

**Regola pricing:** nessuno sconto non autorizzato dal lotto (B-003). Ogni modifica di prezzo
passa per `WF-PRICING` e richiede ok da MAXIMILIAN/CEO.

---

## KPI presidiati

- Deal chiusi/mese [DM]
- Conversion per stadio pipeline [DM]
- Revenue forecast vs reale [DM]
- Cross-sell info→agency [DM]
- LTV/churn clienti [DM]

*[DM] = da misurare: KPI operativo attivo, valore target si fissa dopo primi 60 giorni di dati reali.*

---

## Connessioni

- [[BP-CRO]] · `company/Board-CSuite/_BLUEPRINT/BP-CRO.md`
- [[CRO-v1]] · `company/Board-CSuite/CRO.md`
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md`
- [[12-DOSSIER-MAXIMILIAN]] · `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`
- [[13-DOSSIER-MANDATO]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
- [[CEO-Empire-Conductor]] · `company/Board-CSuite/CEO-Empire-Conductor/`
