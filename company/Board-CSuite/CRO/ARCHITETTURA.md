---
Type: CONCEPT
Status: Active
Tags: #architettura #cro #revenue #swarm #topologia
Created: 2026-06-17
Last updated: 2026-06-17
---

# ARCHITETTURA — CRO (Chief Revenue Officer)

> Cartella-workflow CF-grade. Standard: Content Factory Exponium = 1 workflow (corpus Maximilian §41-42).
> Blueprint: `company/Board-CSuite/_BLUEPRINT/BP-CRO.md`

---

## Topologia del team

```
                        ┌─────────────────────────────┐
                        │       cro-conductor (Opus)   │
                        │  riporta al CEO-conductor    │
                        └────────────┬────────────────-┘
                                     │
          ┌──────────────────────────┼───────────────────────────┐
          │                          │                           │
  ┌───────▼────────┐     ┌───────────▼──────┐      ┌────────────▼──────┐
  │ cro-agency-    │     │ cro-infobusiness- │      │ cro-deal-desk     │
  │ pipeline       │     │ launches          │      │ (Sonnet)          │
  │ (Sonnet)       │     │ (Sonnet)          │      └────────────┬──────┘
  └───────┬────────┘     └───────────┬──────┘                   │
          │                          │                   ┌───────▼──────┐
  ┌───────▼────────┐     ┌───────────▼──────┐           │ cro-pricing- │
  │ cro-pipeline-  │     │ cro-cross-sell-   │           │ arbiter      │
  │ health (Haiku) │     │ mapper (Haiku)    │           │ (Sonnet)     │
  └───────┬────────┘     └───────────┬──────┘           └──────────────┘
          │                          │
  ┌───────▼────────┐     ┌───────────▼──────┐      ┌────────────────────┐
  │ cro-forecast-  │     │ cro-retention-    │      │ cro-memoria        │
  │ analyst        │     │ revenue (Sonnet)  │      │ (Haiku)            │
  │ (Sonnet)       │     └──────────────────┘      └────────────────────┘
  └────────────────┘
```

**Topologia:** star da `cro-conductor` → tutti i worker in parallelo per monitoring; pipeline sequenziale
su WF-DEAL (agency-pipeline → deal-desk → pricing-arbiter) e WF-FORECAST (pipeline-health + infobusiness
→ forecast-analyst → conductor → CEO).

---

## Livelli gerarchici

| Livello | Agente(i) | Tier | Funzione |
|---|---|---|---|
| L0 — Coordinator | `cro-conductor` | Opus | Coordina il team, riporta al CEO |
| L1 — Engine | `cro-agency-pipeline` · `cro-infobusiness-launches` · `cro-forecast-analyst` · `cro-retention-revenue` · `cro-deal-desk` · `cro-pricing-arbiter` | Sonnet | Presidio per fonte di ricavo |
| L2 — Monitor | `cro-pipeline-health` · `cro-cross-sell-mapper` · `cro-memoria` | Haiku | Alta frequenza, basso costo computazionale |

---

## Flussi principali

### WF-DEAL (pipeline Agency)
```
Lead qualificato (da A1/A2) → cro-agency-pipeline (stato pipeline)
  → cro-deal-desk (struttura offerta, dossier preventivo)
  → cro-pricing-arbiter (conferma pricing catalogo)
  → Proposta → chiusura → handoff HC-AG-AM-01 ad A7
```

### WF-FORECAST (cadenza trimestrale)
```
cro-pipeline-health (dati stadio conversione)
  + cro-infobusiness-launches (revenue lanci in cantiere)
  → cro-forecast-analyst (forecast trimestrale per fonte)
  → cro-conductor (sintesi + priorità revenue)
  → CEO-conductor (input per OKR trimestre)
```

### WF-PRICING (su richiesta)
```
Richiesta di variazione prezzo (interna o da prospect)
  → cro-pricing-arbiter (verifica catalogo Mandato Art.3)
  → team-prezzi B-003 (istruttoria)
  → ok lotto: MAXIMILIAN/CEO (delega esplicita)
  → cro-conductor (aggiornamento catalogo)
  → cro-memoria (tracciamento versione prezzi)
```

---

## Handoff contract

| Contract | Da → A | Payload | Acceptance |
|---|---|---|---|
| `HC-CRO-CEO-01` | CRO → CEO | Forecast trimestrale + priorità revenue | Forecast con fonti documentate; nessun numero inventato |
| `HC-CRO-AG-01` | CRO → 01-AGENCY | Deal aperti priorità, KPI conversion per stadio | KPI con data rilevazione |
| `HC-CRO-IB-01` | CRO → 02-INFO-BUSINESS | Pipeline lanci, cross-sell signal | Lista lead caldi con score |
| `HC-CRO-CFO-01` | CRO → CFO | Revenue forecast, margini per fonte | Separazione per prodotto |
| `HC-AG-CRO-01` | 01-AGENCY → CRO | Pipeline update (lead, preventivi, contratti) | Schema standardizzato |
| `HC-IB-CRO-01` | 02-INFO-BUSINESS → CRO | Lanci pianificati, revenue attesa, esiti | Cadenza settimanale |
| `HC-CMO-CRO-01` | CMO → CRO | Lead da campagne, funnel performance | Numero lead + costo acquisizione |

---

## Namespace memoria

```
board/cro/
├── pipeline/         → stato pipeline per stadio (lead→deal→chiuso)
├── deals/            → storico deal (win/loss/in corso, motivi)
├── pricing/          → versioni catalogo, decisioni lotto, variazioni autorizzate
├── forecast/         → forecast per trimestre, confronto vs reale
├── launches/         → lanci InfoBusiness pianificati e conclusi
├── cross-sell/       → segnali lead caldi info→agency
└── retention/        → LTV, churn, win-back attivi
```

---

## Skill proprie (CF-grade)

| Skill | File | Funzione |
|---|---|---|
| `deal-desk` | `skills/SKILLS.md` | Struttura offerta problem-first, verifica scope e pricing |
| `revenue-forecast` | `skills/SKILLS.md` | Forecast per fonte con scenario pessimistico/base/ottimistico |
| `pricing-arbiter` | `skills/SKILLS.md` | Verifica pricing vs catalogo; blocca sconti non autorizzati |

---

## Connessioni

- [[README]] · `company/Board-CSuite/CRO/README.md`
- [[BP-CRO]] · `company/Board-CSuite/_BLUEPRINT/BP-CRO.md`
- [[WF-DEAL]] · `company/Board-CSuite/CRO/workflow/WF-DEAL.md`
- [[WF-FORECAST]] · `company/Board-CSuite/CRO/workflow/WF-FORECAST.md`
- [[WF-PRICING]] · `company/Board-CSuite/CRO/workflow/WF-PRICING.md`
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md`
