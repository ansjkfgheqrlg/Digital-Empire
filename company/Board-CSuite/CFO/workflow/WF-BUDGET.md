---
Type: CONCEPT
Status: Active
Tags: #workflow #cfo #budget #approvazione #attribution #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-BUDGET — Workflow Dichiarazione Budget e Attribution

> **Tipo:** CF-grade · **Figura:** CFO
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CFO.md`
> **Connessioni:** [[WF-SPEND-APPROVAL]] · [[WF-COST-REPORT]] · [[cfo-budget-guard]] · [[cfo-cost-accountant]]

---

## Scopo

Gestire il ciclo completo di una spesa: dal momento in cui un ecosistema dichiara il budget
necessario per un workflow, fino all'attribution nel ledger dopo l'esecuzione. Garantisce che
OGNI euro speso abbia una catena tracciabile: dichiarazione → approvazione → esecuzione → attribution.
Questo workflow è il "cuore finanziario" della holding: ogni run che spende token passa qui.

---

## Trigger

- Ecosistema o agente dichiara di voler eseguire un run che genera spesa API.
- CEO alloca un nuovo envelope di budget per un ecosistema.
- `cfo-cost-sentinel` segnala sforo imminente → richiesta riallocazione.
- Inizio di un nuovo ciclo (es. nuovo mese) → rinnovo envelope per tutti gli ecosistemi attivi.

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `cfo-memoria` | 1 | Load contesto finanziario corrente |
| `cfo-runway-tracker` | 1 | Verifica risorse sessione disponibili (ADR-006) |
| `cfo-tier-router` | 2 | Verifica che il tier pianificato sia il minimo necessario |
| `cfo-spend-approver` | 2 | Esegue o valida il dry-run; emette approval_id |
| `cfo-budget-guard` | 3 | Check pre-run: budget disponibile per l'ecosistema? |
| `cfo-cost-accountant` | 5 | Attribution post-run nel ledger |
| `cfo-cost-sentinel` | 5 | Alert se soglia 80% raggiunta dopo attribution |
| `cfo-conductor` | 0, 4, 6 | Coordinamento; gate escalation; report |

---

## Flusso passo-passo

```
STEP 0 — LOAD CONTESTO
├─ cfo-memoria: carica storico costi ecosistema + envelope corrente
├─ cfo-runway-tracker: verifica risorse sessione (> 20%? Sì → ok. No → chiudi con commit)
└─ Output: brief finanziario al conductor

STEP 1 — DICHIARAZIONE BUDGET (ecosistema richiedente)
├─ Input: { ecosistema, task_descrizione, tier_pianificato, costo_stimato, metodo_stima }
├─ cfo-tier-router: il tier è corretto per il task? (verifica tabella canoniche 3-tier)
│   Anomalia → declassa e aggiorna la richiesta
│   Ok → procede
└─ Output: task validato con tier confermato

STEP 2 — DRY-RUN E APPROVAZIONE (Mandato Art.4.3)
├─ cfo-spend-approver: riceve la stima; verifica documentazione e metodo
├─ dry_run_completato: true? No → blocca. Sì → procede
├─ Sopra soglia? → scala al conductor con raccomandazione
├─ Conductor (se coinvolto): approva / rifiuta con rationale
└─ Output: approval_id APPR-YYYYMMDD-NNN | rifiuto con motivo

STEP 3 — CHECK BUDGET PRE-RUN
├─ cfo-budget-guard: legge envelope ecosistema → costo_stimato ≤ budget_residuo?
│   Sì → autorizza. No → BLOCCA con motivo + residuo attuale
│   Budget parziale → scala al conductor (split run?)
└─ Output: { autorizzato: boolean, budget_residuo_post_run }

STEP 4 — ESECUZIONE
├─ Il run avviene con approval_id e autorizzazione budget attivi
├─ Il run porta in output: costo_effettivo (dato reale, non stima)
└─ Output: { run_id, costo_effettivo, esito }

STEP 5 — ATTRIBUTION POST-RUN
├─ cfo-cost-accountant: crea entry ledger con tutti i campi obbligatori
│   (run_id, agente, ecosistema, commessa, tier, costo_effettivo, approval_id, timestamp)
├─ Aggiorna budget_usato nell'envelope ecosistema
├─ cfo-cost-sentinel: percentuale budget usato ≥ 80%? → alert al conductor
└─ Output: { entry_ledger_id, budget_usato_aggiornato, alert_soglia: boolean }

STEP 6 — CHIUSURA E REPORT
├─ cfo-conductor: aggiorna stato workflow nel log
├─ Se anomalie rilevate (tier sbagliato, stima vs. effettivo > soglia): nota in ledger
├─ cfo-memoria: aggiorna storico (per pattern analysis futuro)
└─ Output: workflow chiuso + ledger aggiornato
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Runway sessione | Step 0 | Bloccante (ADR-006) | Risorse sessione > 20% |
| Tier corretto | Step 1 | Bloccante | Tier pianificato = tier raccomandato dal router |
| Dry-run | Step 2 | Bloccante (Art.4.3) | `dry_run_completato: true` con metodo documentato |
| Budget disponibile | Step 3 | Bloccante | `costo_stimato ≤ budget_residuo` |
| Attribution | Step 5 | Verifica | Ogni run ha entry ledger con `approval_id` |

---

## Input del workflow

```json
{
  "tipo": "run_request | envelope_allocation | riallocazione",
  "ecosistema": "01-AGENCY | ...",
  "task_descrizione": "testo del task",
  "tier_pianificato": "haiku | sonnet | opus | wasm",
  "costo_stimato": "number",
  "metodo_stima": "token_count | analogia_run_precedente | stima_manuale",
  "commessa": "COMM-CLIENT-NNN | null",
  "urgenza": "alta | media | bassa"
}
```

## Output del workflow

```json
{
  "workflow_id": "WF-BUDGET-YYYYMMDD-NNN",
  "esito": "completato | bloccato_budget | bloccato_dry_run | bloccato_tier | escalato_conductor",
  "approval_id": "APPR-YYYYMMDD-NNN | null",
  "entry_ledger_id": "LEDGER-YYYYMMDD-NNN | null",
  "costo_effettivo": "number | null",
  "budget_residuo_post_run": "number",
  "alert_soglia_80": "boolean",
  "nota": "testo se anomalie"
}
```

---

## State

Lo stato del workflow è mantenuto in `board/cfo/` durante l'esecuzione:
- `board/cfo/approvals-pending` → approvazioni in attesa.
- `board/cfo/budget-envelope` → envelope per ecosistema (aggiornato a ogni step 5).
- `board/cfo/ledger-corrente` → ledger della sessione in corso.

---

## Connessioni

- [[cfo-budget-guard]] · `agenti/cfo-budget-guard.md`
- [[cfo-spend-approver]] · `agenti/cfo-spend-approver.md`
- [[cfo-cost-accountant]] · `agenti/cfo-cost-accountant.md`
- [[cfo-tier-router]] · `agenti/cfo-tier-router.md`
- [[WF-SPEND-APPROVAL]] · `workflow/WF-SPEND-APPROVAL.md`
- [[WF-COST-REPORT]] · `workflow/WF-COST-REPORT.md`
- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[REGOLE]] · `regole/REGOLE.md`
