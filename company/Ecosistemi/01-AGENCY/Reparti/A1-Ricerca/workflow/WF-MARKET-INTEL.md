---
Type: WORKFLOW
Status: Active
Tags: #workflow #ricerca #intelligence #market #competitor #trend #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-MARKET-INTEL — Market Intelligence di Nicchia [TARGET-V2]

> **ID:** WF-A1-002 · **Owner:** `ag-a1-coord` · **Reparto:** A1 Ricerca & Market Intelligence
> **Trigger:** cadenza settimanale per report nicchia | on-demand per audit prospect

---

## Scopo

Monitorare nicchie attive, competitor e trend di mercato per produrre report utilizzabili da
Acquisizione (A2), Preventivi (A3) e Closing (A8), e per alimentare 08-INTELLIGENCE.
Ogni report cita le fonti (ADR-002 wiki-first); nessuna metrica inventata (Mandato Art.2 / R4).
Output: `{nicchia, trend, competitor_top3, ICP_aggiornato, opportunita}` → ingest in 08-INTELLIGENCE.

---

## Attori

| Step | Agente A1 | Asset / Reparto esterno |
|---|---|---|
| Avvio + scoping | `ag-a1-coord` | 08-INTELLIGENCE (segnali) |
| Trend di mercato | `ag-a1-intel` | skill `market-audit`, 08-INTELLIGENCE |
| Audit competitor | `ag-a1-comp` | `competitor.py`, `cro_audit.py`, `competitor-profiling` |
| Aggiornamento ICP | `ag-a1-icp` | skill `icp-radar` |
| Gate fonti | `ag-a1-qa` | — |
| Ingest + handoff | `ag-a1-coord` | 08-INTELLIGENCE, A2/A3 |

---

## Flusso passo-passo

```
[TRIGGER]
Cadenza settimanale (nicchia attiva) | richiesta on-demand (audit prospect) → AG-A1-COORD
  {nicchia, modalita: report_nicchia | audit_prospect}
         │
         ▼
[STEP 1] AG-A1-COORD — scoping
  → memory_search su 08-INTELLIGENCE: cosa è già noto a livello holding? (non duplicare)
  → assegna AG-A1-INTEL (trend) + AG-A1-COMP (competitor) in parallelo
         │
         ▼   ← PARALLELO (1a e 1b)
[STEP 2a] AG-A1-INTEL — ricerca trend
  → trend di nicchia, segnali di domanda, opportunità
  → cita la fonte per ogni claim (R4); assenza dato → [DM]
  → sourcing da 08-INTELLIGENCE (non riricerca ciò che esiste)

[STEP 2b] AG-A1-COMP — audit competitor
  → competitor.py + cro_audit.py + market-audit sul prospect (modalita audit)
     o competitor_top3 della nicchia (modalita report)
  → posizionamento / offerta / gap; ogni claim con fonte (R4)
         │
         ▼
[STEP 3] AG-A1-ICP — aggiorna profilo ICP nicchia
  → integra trend (da INTEL) + competitor (da COMP) nei criteri ICP
  → icp-radar; aggiorna agency/a1/icp con fonti citate
         │
         ▼
[STEP 4] AG-A1-QA — GATE intel (G-INTEL)
  → ogni claim ha fonti[] non vuoto e verificabile?
  → nessuna metrica inventata (Mandato Art.2 / R4)?
  → PASS → prosegui; FAIL → report non ingestabile → rework INTEL/COMP
         │
         ▼
[STEP 5] AG-A1-COORD — ingest + handoff
  → report {nicchia, trend, competitor_top3, ICP_aggiornato, opportunita} in agency/a1/intel
  → ingest in 08-INTELLIGENCE (conoscenza riusabile holding)
  → handoff ad A2 (angolo outreach) e A3 (framing preventivo)
  → entry wiki/log.md
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G-INTEL | Fonti citate e verificabili; nessuna metrica inventata | AG-A1-QA | Ingest in 08-INTELLIGENCE (R4) |
| G-ICP | ICP aggiornato con fonti citate | AG-A1-QA | Uso dell'ICP per scraping futuro (R2) |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "nicchia": "ristorazione-roma",
  "modalita": "report_nicchia | audit_prospect",
  "url_prospect": "optional — per audit_prospect",
  "cadenza": "settimanale | on-demand"
}
```

**Output finale:**
```json
{
  "report_id": "INTEL-001",
  "nicchia": "ristorazione-roma",
  "trend": "segnale qualitativo con fonte",
  "competitor_top3": ["...", "...", "..."],
  "ICP_aggiornato": "agency/a1/icp/ristorazione-roma",
  "opportunita": "...",
  "fonti": ["https://...", "08-intelligence:...", "skill:market-audit"],
  "gate_qa": "PASS",
  "ingest_08": true
}
```

---

## State

File: `agency/a1/intel/{report_id}.json`
- Creato allo step finale; non aggiornato dopo l'ingest.
- Linkato al profilo ICP aggiornato e ai record di 08-INTELLIGENCE.
- Ripartibilità: un report interrotto riprende dallo step incompleto (trend / competitor / ICP).

---

## Cadenza & escalation

- Report nicchia: settimanale per ogni nicchia attiva.
- Audit prospect: on-demand (tipicamente innescato da WF-BRIEF-PRE-CALL).
- Trend non supportato da fonte → G-INTEL FAIL → rework; mai ingest di claim non verificabile.
- Conflitto tra segnale 08 e dato A1 → AG-A1-COORD riconcilia citando entrambe le fonti.

---

## Connessioni

- [[ag-a1-intel]] · `agenti/ag-a1-intel.md`
- [[ag-a1-comp]] · `agenti/ag-a1-comp.md`
- [[ag-a1-icp]] · `agenti/ag-a1-icp.md`
- [[ag-a1-qa]] · `agenti/ag-a1-qa.md` — gate fonti citate
- [[WF-BRIEF-PRE-CALL]] · `workflow/WF-BRIEF-PRE-CALL.md` — consuma l'audit prospect
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1`
