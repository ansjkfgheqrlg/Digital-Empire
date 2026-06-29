---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #delivery #content-factory #handover #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-DELIVERY-CONTENT-FACTORY — Delivery Motore Content Factory

> **ID:** WF-A4-002 · **Owner:** `ag-a4-coord` · **Reparto:** A4 Delivery & Implementazione
> **Trigger:** handoff da A3 + richiesta motore a 03-CONTENT-FACTORY (`HC-AG-CF-01`)
> **Standard:** CF-grade (ADR-007) · **ADR-003:** wrap del motore CF esistente, mai rewrite

---

## Scopo

Setup del motore Content Factory **parametrizzato sul server del cliente** in ≤7 giorni. A
differenza dell'outreach (motore interno DE), qui il motore arriva da 03-CONTENT-FACTORY via
handoff `HC-AG-CF-01`. Da lì in poi lo schema è identico: G+0→G+7, multi-tenant, training, UAT
con run autonoma, handover zero-dipendenza. Gate Delivery di AG-A4-QA **+ QA-Cliente (A10)
indipendente post-UAT**.

---

## Attori

| Step | Agente A4 | Esterno |
|---|---|---|
| Richiesta motore | `ag-a4-coord` | 03-CONTENT-FACTORY (`HC-AG-CF-01`) |
| G+0 verifica ambiente | `ag-a4-env` | cliente |
| G+1 setup repo + secrets | `ag-a4-env` | cliente (server) |
| G+2 tenant injection | `ag-a4-tenant` | — |
| G+3-4 test run | `ag-a4-coord` + `ag-a4-env` | — |
| G+5 training | `ag-a4-train` | cliente |
| G+6 UAT | `ag-a4-uat` | cliente |
| G+7 handover | `ag-a4-hand` | cliente |
| Gate Delivery | `ag-a4-qa` | — |
| QA-Cliente indipendente | — | A10 (QA cliente) |

---

## Flusso passo-passo

```
[TRIGGER]
Handoff A3 → AG-A4-COORD (prodotto=content-factory)
         │
         ▼
[STEP 0] AG-A4-COORD — validazione handoff + richiesta motore
  → valida contratto/scope/prerequisiti (come WF-OUTREACH)
  → apre handoff HC-AG-CF-01 a 03-CONTENT-FACTORY per il motore parametrizzabile
  → motore non consegnato in tempo → escalation AG-DIR (delivery bloccata da reparto esterno)
  → GATE-0: handoff completo + motore ricevuto → prosegui

         │
         ▼
[STEP 1 · G+0] AG-A4-ENV — verifica ambiente cliente (env-precheck.py)
  → OS, Python, permessi, rete uscita verso le API del motore CF
  → BIVIO ROLLBACK: non conforme → countdown NON parte, runbook al cliente, alert a Max (R3)

         │
         ▼
[STEP 2 · G+1] AG-A4-ENV — setup repo motore CF + secrets SUL SERVER CLIENTE
  → installa il motore ricevuto da 03-CF sul server del cliente (ADR-003: wrap)
  → secrets nell'ambiente del cliente, mai nel namespace DE (R6)

         │
         ▼
[STEP 3 · G+2] AG-A4-TENANT — iniezione brand_kit + icp (pattern 11)
  → brand voice, palette, claim, segmento ICP nei template di generazione contenuti
  → verifica isolamento tenant; tenant_injected=true

         │
         ▼
[STEP 4 · G+3-4] AG-A4-COORD + AG-A4-ENV — test run su campione piccolo
  → genera un set ridotto di contenuti brandizzati; verifica pubblicazione sul CMS cliente
  → fallisce? debug in dry-run prima di ogni retry (pattern 3); test_run_passata=true

         │
         ▼
[STEP 5 · G+5] AG-A4-TRAIN — training kit + sessione (delivery-playbook)
  → walkthrough generazione+pubblicazione + runbook + FAQ sul setup cliente; training_erogato=true

         │
         ▼
[STEP 6 · G+6] AG-A4-UAT — run di accettazione + run autonoma cliente
  → checklist firmabile; il cliente genera e pubblica 1 contenuto DA SOLO
  → firma; uat_firmata=true, run_autonoma_cliente=true

         │
         ▼
[STEP 6b] QA-CLIENTE (A10) — verifica indipendente post-UAT
  → A10 verifica la qualità dell'output dal punto di vista del cliente, indipendente da A4
  → FAIL A10 → rework prima del Gate Delivery (doppio presidio qualità)

         │
         ▼
[STEP 7 · G+7] AG-A4-HAND — handover pack (client-handover)
  → codice motore CF + README + credenziali (server cliente) + licenza; verifica zero-dipendenza-DE

         │
         ▼
[STEP 8 · G+7] AG-A4-QA — Gate Delivery (BLOCCANTE)
  → 6 check (incl. zero dipendenza + run autonoma) + conferma esito QA-Cliente A10
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
| GATE-0 — Handoff + motore | Contratto/scope OK + motore ricevuto da 03-CF | AG-A4-COORD | Apertura delivery |
| GATE-ENV — Ambiente conforme | OS/Python/permessi/rete OK | AG-A4-ENV | Avvio countdown (R3) |
| GATE-A10 — QA-Cliente indipendente | Qualità output verificata da A10 post-UAT | A10 | Gate Delivery |
| GATE-FINALE — Gate Delivery | 6 check PASS + esito A10 | AG-A4-QA | Chiusura handover (R1, R2) |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "delivery_id": "DEL-002",
  "cliente_ref": "CLI-002",
  "prodotto": "content-factory",
  "scope_congelato": "riferimento scope",
  "handoff_motore": "HC-AG-CF-01",
  "contratto_firmato": true
}
```

**Output finale:**
```json
{
  "delivery_id": "DEL-002",
  "motore_ricevuto": true,
  "uat_firmata": true,
  "run_autonoma_cliente": true,
  "qa_cliente_a10": "PASS",
  "zero_dipendenza_de": true,
  "gate_delivery": "PASS",
  "stato_finale": "handover_completo"
}
```

---

## State

File: `agency/a4/delivery/{delivery_id}/state.json` (+ `agency/a4/uat/{delivery_id}.json`)
- Campo aggiuntivo `motore_ricevuto` (handoff 03-CF) e `qa_cliente_a10`.
- Ripartibilità a freddo dal `step_corrente`; `gate_delivery: PASS` richiede esito A10 PASS.

---

## Connessioni

- [[ag-a4-coord]] · `agenti/ag-a4-coord.md`
- [[WF-DELIVERY-OUTREACH-FACTORY]] · `workflow/WF-DELIVERY-OUTREACH-FACTORY.md` — schema G+0→G+7 base
- [[WF-DELIVERY-SECOND-BRAIN]] · `workflow/WF-DELIVERY-SECOND-BRAIN.md` — stesso pattern, motore da 08
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4`
- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md` — fornitore motore
