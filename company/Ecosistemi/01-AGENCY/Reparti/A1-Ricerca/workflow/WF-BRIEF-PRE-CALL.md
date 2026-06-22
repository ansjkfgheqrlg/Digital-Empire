---
Type: WORKFLOW
Status: Active
Tags: #workflow #ricerca #brief #pre-call #dossier #closing #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-BRIEF-PRE-CALL — Dossier Pre-Call per Discovery [TARGET-V2]

> **ID:** WF-A1-003 · **Owner:** `ag-a1-coord` · **Reparto:** A1 Ricerca & Market Intelligence
> **Trigger:** A8-Closing richiede dossier pre-call per un lead, prima di una discovery call

---

## Scopo

Produrre il dossier pre-call che Max (o A8-Closing) usa prima di ogni discovery call: profilo
lead + score, audit problema quantificato, 3 competitor, ICP match, contesto nicchia.
Il dossier si consegna ≥2h prima della call (SLA, R6) e non ha campi vuoti (P6): un dato
mancante è dichiarato come [DM] + motivo, mai lasciato in bianco. Output: documento MD/PDF
strutturato consegnato ad A8.

---

## Attori

| Step | Agente A1 | Asset / Reparto esterno |
|---|---|---|
| Avvio + verifica SLA | `ag-a1-coord` | A8-Closing (richiesta) |
| Audit problema + competitor | `ag-a1-comp` | `competitor.py`, `cro_audit.py`, `market-audit` |
| Aggregazione dossier | `ag-a1-brief` | `agency/leads`, `agency/a1/icp`, `agency/a1/intel` |
| Gate completezza | `ag-a1-qa` | — |
| Consegna | `ag-a1-brief` | A8-Closing |

---

## Flusso passo-passo

```
[TRIGGER]
A8-Closing → AG-A1-COORD
  {lead_id, call_prevista (data/ora)}
         │
         ▼
[STEP 1] AG-A1-COORD — verifica margine SLA (R6)
  → call_prevista - ora_attuale ≥ 2h? → prosegui prioritario
  → <2h → modalita best-effort + dichiarazione esplicita di cosa manca (non bypass del gate)
  → assegna AG-A1-COMP (audit problema) + AG-A1-BRIEF (aggregazione)
         │
         ▼
[STEP 2] AG-A1-COMP — audit problema + competitor del prospect
  → cro_audit.py + market-audit sul sito del lead → problemi quantificabili (o [DM])
  → competitor.py + competitor-profiling → 3 competitor (posizionamento, offerta, gap)
  → ogni claim cita la fonte (R4)
  → (può innescare WF-MARKET-INTEL modalita audit_prospect se l'audit è profondo)
         │
         ▼
[STEP 3] AG-A1-BRIEF — aggregazione dossier
  → profilo lead + score (da agency/leads)
  → audit problema + 3 competitor (da AG-A1-COMP)
  → ICP match (da agency/a1/icp) — perché questo lead è ICP
  → contesto nicchia (da agency/a1/intel)
  → propone un angolo di vendita per il closer
  → verifica campi_vuoti: dato mancante → [DM] + motivo (P6), mai vuoto
         │
         ▼
[STEP 4] AG-A1-QA — GATE brief (G-BRIEF)
  → nessun campo "da compilare" vuoto?
  → SLA 2h rispettata (o best-effort dichiarato)?
  → PASS → prosegui; FAIL → campo vuoto → rework BRIEF/COMP
         │
         ▼
[STEP 5] AG-A1-BRIEF — consegna ad A8
  → documento MD/PDF strutturato → A8-Closing ≥2h prima della call
  → record in agency/a1/dossier (consegnato_a8, sla_2h_rispettata)
  → notifica AG-A1-COORD: dossier consegnato
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G-SLA | Margine ≥2h (o best-effort dichiarato per call <2h) | AG-A1-COORD | Avvio standard (R6) |
| G-BRIEF | Nessun campo vuoto; ogni claim con fonte | AG-A1-QA | Consegna ad A8 (P6/R4) |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "lead_id": "LEAD-0001",
  "call_prevista": "2026-06-25T15:00:00Z",
  "richiedente": "A8-Closing"
}
```

**Output finale:**
```json
{
  "dossier_id": "DOSS-001",
  "lead_id": "LEAD-0001",
  "profilo_lead": "score + dati chiave",
  "problema_quantificato": "audit problema (o [DM] + motivo)",
  "competitor": ["...", "...", "..."],
  "icp_match": "perché ICP",
  "angolo_vendita": "leva per il closer",
  "campi_vuoti": [],
  "consegnato_a8": "2026-06-25T12:30:00Z",
  "sla_2h_rispettata": true,
  "gate_qa": "PASS"
}
```

---

## State

File: `agency/a1/dossier/{dossier_id}.json`
- Aggiornato fino alla consegna ad A8; archiviato dopo la call.
- Ripartibilità: un dossier interrotto riprende dall'aggregazione mancante (audit / competitor / ICP).
- `consegnato_a8` non valorizzabile finché `campi_vuoti` non è vuoto (regola di integrità).

---

## Failure & escalation

- Audit problema non producibile (sito prospect down) → [DM] + motivo nel dossier (P6), non blocco.
- Call <2h di preavviso → best-effort + dichiarazione esplicita; AG-A1-COORD avvisa A8.
- Dato lead mancante in `agency/leads` → AG-A1-COORD valuta re-run sourcing prioritario sul lead.
- Ogni mancata SLA → distillata in `agency/reasoning` per migliorare il margine futuro.

---

## Connessioni

- [[ag-a1-brief]] · `agenti/ag-a1-brief.md`
- [[ag-a1-comp]] · `agenti/ag-a1-comp.md`
- [[ag-a1-qa]] · `agenti/ag-a1-qa.md` — gate no-campi-vuoti + SLA
- [[WF-MARKET-INTEL]] · `workflow/WF-MARKET-INTEL.md` — fornisce audit prospect e contesto nicchia
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1`
