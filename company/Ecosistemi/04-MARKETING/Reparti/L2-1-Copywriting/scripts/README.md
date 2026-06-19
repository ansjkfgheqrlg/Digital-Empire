---
Type: CONCEPT
Status: Active
Tags: #scripts #copywriting #L2-1 #wrap
Created: 2026-06-18
Last updated: 2026-06-18
---

# SCRIPTS — L2.1 Copywriting

> **NOTA ADR-003:** gli script REALI che eseguono il copy vivono nel motore esistente
> (`SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/`) e NON si riscrivono. Questa cartella
> contiene solo il **layer di invocazione** (wrapper) + pochi script di supporto deterministici
> nuovi (Tier 0). Il giudizio è degli agenti; il deterministico è degli script.
> Dossier: `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §5.1.

---

## Wrapper di invocazione del motore

### `copy-workflow-invoke` [WRAPPA-ESISTENTE — NON MODIFICARE IL MOTORE]

**Scopo:** punto di ingresso v2 che riceve il contratto handoff standard (§1.2 dossier) da
MKT-Conductor e lo gira al Copy Workflow Orchestration Layer esistente, recuperando l'output gated.
**Input:** contratto JSON `{committente, formato, awareness_level, icp, obiettivo, deadline}`.
**Output:** output del motore + score A8 + brand gate, riformattato nel contratto di risposta v2.
**Regola ferrea:** legge/invoca il motore, non ne tocca i file.

---

## Script di supporto nuovi (target V2, deterministici — Tier 0)

### `score-aggregator.py` [TARGET-V2]
**Scopo:** aggrega gli score A8 per copy_id e periodo, calcola il first-pass rate (KPI di
COPY-QA-LEAD). Lettura da `marketing/copy/scores`, nessun giudizio.
**Output:** `marketing/copy/scores/aggregato-YYYY-MM.json` + first-pass rate per formato.
**Owner:** COPY-QA-LEAD · **Tier:** 0.

### `pattern-loader.py` [TARGET-V2]
**Scopo:** prima di ogni run, carica i pattern vincenti per `{icp}` da `marketing/copy/patterns/{icp}`
e li passa a COPY-MASTER come contesto (il "recall" del loop §4b). Lookup, nessun ragionamento.
**Output:** set di pattern ICP per il prompt di COPY-MASTER.
**Owner:** COPY-MASTER · **Tier:** 0.

---

## Dipendenze (motore esistente — [WRAPPA-ESISTENTE, NON MODIFICARE])

| Asset motore | Uso nel reparto | Stato |
|---|---|---|
| `copy-workflow/` (copy-master, A1-A8, S1-S3, 6 workflow, template) | Eseguito via `copy-workflow-invoke` | ATTIVO — intoccabile |
| sub-skill del motore (6) | Invocate dal motore, non da L2.1 | ATTIVO — intoccabile |

**REGOLA:** gli script L2.1 leggono `marketing/copy/...` e invocano il motore. MAI scrivono nei
file del motore. Ogni evoluzione del motore = ADR dedicato.

---

## Connessioni

- [[copy-master]] · `agenti/copy-master.md`
- [[copy-qa-lead]] · `agenti/copy-qa-lead.md`
- [[REGOLE]] · `regole/REGOLE.md` (R1 motore intoccabile)
- [[state/README]] · `state/README.md`
