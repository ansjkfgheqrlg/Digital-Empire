---
Type: CONCEPT
Status: Active
Tags: #workflow #cfo #report #ecosistema #ceo #board #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-COST-REPORT — Workflow Report Settimanale Costi

> **Tipo:** CF-grade · **Figura:** CFO
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CFO.md`
> **Connessioni:** [[WF-BUDGET]] · [[WF-SPEND-APPROVAL]] · [[cfo-forecast-finance]] · [[cfo-roi-analyst]]

---

## Scopo

Produrre il report settimanale dei costi della holding per il CEO e il Board. Il report aggrega
il ledger della settimana, calcola ROI per ecosistema, aggiorna il forecast di runway, identifica
anomalie e pattern, e propone azioni correttive. Non è un report passivo: ogni report include
raccomandazioni concrete e alert su rischi imminenti.

---

## Trigger

- Schedule settimanale (es. ogni lunedì mattina, o al primo avvio di sessione della settimana).
- Richiesta esplicita del CEO o di una figura C-Suite.
- Alert critico da `cfo-cost-sentinel` che richiede una sintesi immediata.
- Fine di un ciclo di budget (fine mese / fine trimestre).

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `cfo-memoria` | 1 | Carica ledger storico della settimana + pattern attivi |
| `cfo-cost-accountant` | 2 | Aggrega ledger per ecosistema / tier / commessa |
| `cfo-roi-analyst` | 3 | Calcola ROI per ecosistema (se output misurato disponibile) |
| `cfo-forecast-finance` | 4 | Aggiorna forecast costi + runway residua |
| `cfo-cost-sentinel` | 5 | Verifica alert aperti + genera alert finali |
| `cfo-conductor` | 6 | Sintetizza, redige il report, dispatcha al CEO |

---

## Flusso passo-passo

```
STEP 1 — LOAD LEDGER STORICO
├─ cfo-memoria: estrae il ledger dell'ultima settimana (YYYY-MM-DD → YYYY-MM-DD)
├─ Carica: pattern attivi + alert irrisolti da sessioni precedenti
└─ Output: { ledger_settimana, pattern_attivi, alert_irrisolti }

STEP 2 — AGGREGAZIONE COSTI
├─ cfo-cost-accountant: aggrega il ledger per:
│   (a) ecosistema: costo totale settimana per ciascuno
│   (b) tier: distribuzione haiku / sonnet / opus / wasm
│   (c) commessa: se run legati a commessa cliente
│   (d) agente: top 5 agenti per volume di costo
├─ Identifica scostamenti stima vs. effettivo per tier
└─ Output: { costi_per_ecosistema, tier_distribution, top_agenti, scostamenti }

STEP 3 — ROI PER ECOSISTEMA
├─ cfo-roi-analyst: per ogni ecosistema con output misurabile:
│   calcola costo per unità (cliente / contenuto / email / ricavo)
├─ Confronta con settimana precedente → trend
├─ Ecosistemi senza output misurabile → flag [DM]
└─ Output: { roi_per_ecosistema, trend_roi, ecosistemi_senza_metrica }

STEP 4 — FORECAST E RUNWAY
├─ cfo-forecast-finance: con il ledger settimana appena aggregato:
│   aggiorna le proiezioni mensili per ogni ecosistema
├─ Calcola runway residuo per ecosistema e holding totale
├─ Identifica ecosistemi con runway < soglia [DM] → rischio
└─ Output: { forecast_mensile, runway_per_ecosistema, ecosistemi_a_rischio }

STEP 5 — ALERT CONSOLIDATI
├─ cfo-cost-sentinel: legge alert aperti + genera nuovi se necessario
├─ Aggrega: alert soglia_80 + drift + anomalie tier + pattern
├─ Priorità: critica / alta / media
└─ Output: { alert_consolidati, nessun_alert: boolean }

STEP 6 — SINTESI E DISPATCH
├─ cfo-conductor: riceve tutti gli output dei passi 1-5
├─ Redige il report Board in formato standard (sezioni sotto)
├─ Aggiunge raccomandazioni concrete (non generiche)
├─ Dispatcha report al CEO via HC-CFO-CEO-01
├─ Se alert critici: notifica CEO anche in alert separato
└─ Output: report_Board_YYYYMMDD.md + dispatch log
```

---

## Struttura del report prodotto

```markdown
# Report Costi Holding — YYYY-MM-DD

## Riepilogo Esecutivo
[2-3 righe: stato budget holding, anomalie principali, azione richiesta]

## Costi per Ecosistema (settimana)
| Ecosistema | Costo Sett. | Envelope | % Usato | Runway (gg) |
|---|---|---|---|---|
| 01-AGENCY | X | Y | Z% | N |
...

## Distribuzione Tier
| Tier | n. Run | % Run | Costo |
|---|---|---|---|
| Haiku (T1) | ... | ...% | ... |
...

## ROI per Ecosistema
| Ecosistema | Costo Unità | Tipo Unità | Trend |
|---|---|---|---|
| 01-AGENCY | X | cliente acquisito | miglioramento |
...

## Alert Aperti
- [CRITICO] Ecosistema 04-MARKETING: budget al 87%, runway 3gg
- [ALTO] Anomalia tier: 02-CONTENT usa Opus 35% dei run

## Forecast Prossimo Mese
[Proiezione + ecosistemi a rischio sforo]

## Raccomandazioni
1. [Azione concreta con owner e deadline]
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Ledger disponibile | Step 1 | Bloccante | Almeno 1 sessione di ledger disponibile per il periodo |
| ROI con fonte dichiarata | Step 3 | Non bloccante (tag DM) | Ogni ROI cita la fonte; se manca → [DM] |
| Forecast con dati reali | Step 4 | Non bloccante (tag DM) | Proiezioni basate su ledger reale; se < 7gg → [DM] |
| Dispatch al CEO | Step 6 | Bloccante | Report deve includere sezione Raccomandazioni |

---

## Input del workflow

```json
{
  "tipo": "settimanale | richiesta_esplicita | fine_ciclo",
  "periodo": "YYYY-MM-DD / YYYY-MM-DD",
  "richiedente": "CEO | Board | cfo-conductor | schedule",
  "urgenza": "standard | alta (alert critico)"
}
```

## Output del workflow

```json
{
  "report_id": "REPORT-CFO-YYYYMMDD",
  "periodo": "YYYY-MM-DD / YYYY-MM-DD",
  "report_path": "state/reports/report_Board_YYYYMMDD.md",
  "dispatched_a": "CEO",
  "handoff_id": "HC-CFO-CEO-YYYYMMDD-001",
  "alert_critici_n": "number",
  "ecosistemi_a_rischio": ["string"],
  "runway_holding_giorni": "number | [DM]"
}
```

---

## State

- Report archiviati in `state/reports/`.
- Handoff log in `state/dispatches/`.
- Alert consolidati aggiornati in `board/cfo/cost-alerts`.

---

## Connessioni

- [[cfo-conductor]] · `agenti/cfo-conductor.md`
- [[cfo-memoria]] · `agenti/cfo-memoria.md`
- [[cfo-cost-accountant]] · `agenti/cfo-cost-accountant.md`
- [[cfo-roi-analyst]] · `agenti/cfo-roi-analyst.md`
- [[cfo-forecast-finance]] · `agenti/cfo-forecast-finance.md`
- [[cfo-cost-sentinel]] · `agenti/cfo-cost-sentinel.md`
- [[WF-BUDGET]] · `workflow/WF-BUDGET.md`
- [[KPI]] · `kpi/KPI.md`
