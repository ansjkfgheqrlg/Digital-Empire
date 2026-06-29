---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #delivery #second-brain #handover #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-DELIVERY-SECOND-BRAIN — Delivery Vault Second Brain

> **ID:** WF-A4-003 · **Owner:** `ag-a4-coord` · **Reparto:** A4 Delivery & Implementazione
> **Trigger:** handoff da A3 + richiesta template a 08-INTELLIGENCE (`HC-IN-AG-01`)
> **Standard:** CF-grade (ADR-007) · **ADR-003:** wrap del template SB esistente, mai rewrite

---

## Scopo

Setup di un vault Second Brain + le sue skill **sul sistema del cliente** in ≤7 giorni. Il
template arriva da 08-INTELLIGENCE via handoff `HC-IN-AG-01`. Lo schema segue G+0→G+7 con un
accento sul workflow **memory-first**: il cliente deve saper navigare il vault e interrogarlo
autonomamente, senza alcuna dipendenza da credenziali DE.

---

## Attori

| Step | Agente A4 | Esterno |
|---|---|---|
| Richiesta template | `ag-a4-coord` | 08-INTELLIGENCE (`HC-IN-AG-01`) |
| G+0 verifica ambiente | `ag-a4-env` | cliente |
| G+1 config vault | `ag-a4-env` + `ag-a4-tenant` | cliente (sistema) |
| G+2 tenant + skill | `ag-a4-tenant` | — |
| G+3-4 test indicizzazione/query | `ag-a4-coord` | — |
| G+5 training memory-first | `ag-a4-train` | cliente |
| G+6 UAT navigazione autonoma | `ag-a4-uat` | cliente |
| G+7 handover | `ag-a4-hand` | cliente |
| Gate Delivery | `ag-a4-qa` | — |

---

## Flusso passo-passo

```
[TRIGGER]
Handoff A3 → AG-A4-COORD (prodotto=second-brain)
         │
         ▼
[STEP 0] AG-A4-COORD — validazione handoff + richiesta template
  → valida contratto/scope/prerequisiti
  → apre handoff HC-IN-AG-01 a 08-INTELLIGENCE per il template second-brain
  → GATE-0: handoff completo + template ricevuto → prosegui

         │
         ▼
[STEP 1 · G+0] AG-A4-ENV — verifica ambiente cliente (env-precheck.py)
  → sistema cliente (OS, spazio disco, runtime, eventuali API embedding)
  → BIVIO ROLLBACK: non conforme → countdown NON parte, runbook al cliente, alert a Max (R3)

         │
         ▼
[STEP 2 · G+1] AG-A4-ENV + AG-A4-TENANT — config vault SUL SISTEMA CLIENTE
  → configura il vault dal template ricevuto da 08 sul sistema del cliente (ADR-003)
  → eventuali secrets (es. embedding) nell'ambiente del cliente, mai nel namespace DE (R6)

         │
         ▼
[STEP 3 · G+2] AG-A4-TENANT — iniezione brand_kit + icp + skill (pattern 11)
  → struttura cartelle/tag e skill second-brain parametrizzate sul dominio del cliente
  → verifica isolamento tenant; tenant_injected=true

         │
         ▼
[STEP 4 · G+3-4] AG-A4-COORD — test indicizzazione + query
  → indicizza un set ridotto di documenti del cliente; esegue query di test
  → fallisce? debug in dry-run prima di ogni retry (pattern 3); test_run_passata=true

         │
         ▼
[STEP 5 · G+5] AG-A4-TRAIN — training workflow memory-first (delivery-playbook)
  → walkthrough: aggiungi nota → indicizza → interroga → manutieni; runbook + FAQ
  → enfasi memory-first: il vault è la memoria viva del cliente; training_erogato=true

         │
         ▼
[STEP 6 · G+6] AG-A4-UAT — UAT navigazione autonoma
  → il cliente NAVIGA il vault e fa 1 query DA SOLO dopo il training (Gate dossier SB)
  → nessuna dipendenza da credenziali DE per navigare/interrogare
  → firma; uat_firmata=true, run_autonoma_cliente=true

         │
         ▼
[STEP 7 · G+7] AG-A4-HAND — handover pack (client-handover)
  → vault completo + skill + README + credenziali cliente + licenza; verifica zero-dipendenza-DE

         │
         ▼
[STEP 8 · G+7] AG-A4-QA — Gate Delivery (BLOCCANTE)
  → 6 check, con focus su: cliente naviga il vault autonomamente · nessuna credenziale DE
  → tutti PASS → delivery chiusa · uno FAIL → rework → re-gate

         │
         ▼
[STEP 9] Chiusura → segnale A6 (case study) · AG-A4-LEARN distilla pattern ·
         avvio WF-SUPPORTO-90GG · entry wiki/log.md
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| GATE-0 — Handoff + template | Contratto/scope OK + template ricevuto da 08 | AG-A4-COORD | Apertura delivery |
| GATE-ENV — Ambiente conforme | Sistema cliente conforme | AG-A4-ENV | Avvio countdown (R3) |
| GATE-NAV — Navigazione autonoma | Il cliente naviga e interroga il vault da solo, senza credenziali DE | AG-A4-UAT + AG-A4-QA | Gate Delivery (dossier SB) |
| GATE-FINALE — Gate Delivery | 6 check PASS (incl. zero dipendenza) | AG-A4-QA | Chiusura handover (R1, R2) |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "delivery_id": "DEL-003",
  "cliente_ref": "CLI-003",
  "prodotto": "second-brain",
  "scope_congelato": "riferimento scope",
  "handoff_template": "HC-IN-AG-01",
  "contratto_firmato": true
}
```

**Output finale:**
```json
{
  "delivery_id": "DEL-003",
  "template_ricevuto": true,
  "uat_firmata": true,
  "run_autonoma_cliente": true,
  "naviga_vault_autonomamente": true,
  "zero_dipendenza_de": true,
  "gate_delivery": "PASS",
  "stato_finale": "handover_completo"
}
```

---

## State

File: `agency/a4/delivery/{delivery_id}/state.json` (+ `agency/a4/uat/{delivery_id}.json`)
- Campo aggiuntivo `template_ricevuto` (handoff 08) e `naviga_vault_autonomamente`.
- Ripartibilità a freddo dal `step_corrente`; `gate_delivery: PASS` richiede navigazione autonoma.

---

## Connessioni

- [[ag-a4-coord]] · `agenti/ag-a4-coord.md`
- [[ag-a4-uat]] · `agenti/ag-a4-uat.md` — verifica la navigazione autonoma del vault
- [[WF-DELIVERY-OUTREACH-FACTORY]] · `workflow/WF-DELIVERY-OUTREACH-FACTORY.md` — schema G+0→G+7 base
- [[WF-SUPPORTO-90GG]] · `workflow/WF-SUPPORTO-90GG.md` — supporto post-handover
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4`
