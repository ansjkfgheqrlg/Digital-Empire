# 📊 OBSERVABILITY — Metriche, dashboard, auto-miglioramento

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 1.5
> **Backbone component.** Misura tutto, attribuisce i costi, alimenta l'apprendimento,
> predice i colli di bottiglia prima che blocchino.
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/README.md]]

---

## Sistema di metriche

**File di stato principale:** `company/metrics/runs.jsonl` — append-only, audit trail completo.

**Schema evento standard:**
```json
{
  "ts": "2026-06-11T15:30:00Z",
  "tipo": "run_done | gate_passed | gate_failed | handoff_rejected | swarm_done | lead_generated | content_published | sale_closed | evolution",
  "eco": "01-AGENCY",
  "reparto": "Acquisizione",
  "team": "WF-OUTREACH-EMAIL",
  "agente": "AGY-ACQ-email-writer-01",
  "brand_kit": "DE | <cliente>",
  "tier_modello": 2,
  "costo_usd": 0.04,
  "durata_sec": 12,
  "output_size": 150,
  "gate_result": "pass | fail",
  "note": "..."
}
```

**Tipi di evento da emettere:**
- `run_done` — ogni invocazione LLM completata
- `gate_passed` / `gate_failed` — ogni check di Governance
- `handoff_rejected` — ogni handoff rifiutato con motivo
- `swarm_done` — completamento di un task multi-agente
- `lead_generated` — output di business reale AGENCY (DONE WHEN §0 Piano Maestro)
- `content_published` — output di business reale CONTENT-FACTORY
- `sale_closed` — revenue reale (DONE WHEN §0)
- `evolution` — evento FORGE (hire/retire/evolve)

---

## Cost Attribution Multi-Tenant

Aggregazioni rigenerabili dallo script `costs.sh`:
```
company/metrics/cost/
├── by-agent.json       ← costo per agente (top spenders)
├── by-team.json        ← costo per team/workflow
├── by-eco.json         ← costo per ecosistema (vs envelope)
└── by-brand.json       ← costo per brand_kit/cliente (multi-tenant)
```

Risponde a: "quanto costa servire il cliente X?" · "quanto costa produrre un email?" · "qual è il ROI del workflow outreach?"

---

## Dashboard (da costruire F8)

`company/orchestrator/dashboard.sh` — vista CLI unica:

| Sezione | Contenuto |
|---|---|
| Stato 10 ecosistemi | verde/giallo/rosso per ecosistema |
| Agenti attivi/idle | con costo cumulativo 30g |
| Backlog bus | messaggi pending per ecosistema |
| Ultimi gate | pass/fail rate ultime 24h |
| Costo giornaliero | vs envelope mensile rimanente |
| Alert Sentinels | interventi attivi o recenti |
| Output reale | lead generati, contenuti pubblicati, vendite (DONE WHEN) |

---

## Learning Loop (da costruire F8)

```
metrics/runs.jsonl (osserva)
    ↓
neural_train (identifica pattern nelle metriche)
    ↓
autopilot_predict (predice bottleneck e drift)
    ↓
ReasoningBank distilla (trajectory → pattern confermato)
    ↓
FORGE propone hire/retire/evolve (agisce)
```

**Alert proattivi (esempi):**
- "AGENCY ha reply rate < 3% da 5 giorni → diagnosi CMO"
- "WF-OUTREACH-EMAIL usa Opus su task di classificazione → downgrade raccomandato (risparmio 80%)"
- "Quality-Sentinel ha bloccato 5 output in 24h dallo stesso team → rivedi prompt"

---

## Differenza vs CF Exponium

CF misura produzioni video e swarm; DE aggiunge:
- (a) eventi di **revenue** reale (`lead_generated`, `sale_closed`) — i criteri DONE WHEN
- (b) cost-attribution **per brand/cliente** (multi-tenant) — "quanto costa servire il cliente X?"

CF non ha il campo `brand_kit` nei metrici.

---

## Fasi di build

| Build | Cosa | Quando |
|---|---|---|
| B2.10 (F2) | `runs.jsonl` + emettitori negli script principali + `cost/by-eco.json` parziale | F2 |
| B4 (F4) | `dashboard.sh` + cost-attribution completa per brand | F4 |
| B5 (F8) | `neural_train` + `autopilot` wired + alert proattivi | F8 |
| B6 (F8) | loop auto-miglioramento FORGE completo | F8 |

---

## KPI

| Metrica | Target |
|---|---|
| Costo attribuito (eventi con costo e brand_kit) | ≥ 95% (KPI Backbone) |
| Revenue eventi tracciati (lead, vendite) | 100% |
| Dashboard disponibile (uptime CLI) | 99% da F4 |
| Alert proattivi con lead time > 0 | obiettivo F8 |

---

## Stato

- `company/metrics/` struttura — ⏳ da creare (F2, task 2.10)
- `costs.sh` script — ⏳ da creare (F2)
- `dashboard.sh` — ⏳ da costruire (F4)
- `neural_train` + `autopilot` — ⏳ da costruire (F8)
