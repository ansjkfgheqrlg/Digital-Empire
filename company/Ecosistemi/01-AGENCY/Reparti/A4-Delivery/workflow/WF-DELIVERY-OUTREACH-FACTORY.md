---
Type: WORKFLOW
Status: Active
Tags: #workflow #agency #delivery #outreach #handover #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# WF-DELIVERY-OUTREACH-FACTORY — Delivery Pipeline Outreach

> **ID:** WF-A4-001 · **Owner:** `ag-a4-coord` · **Reparto:** A4 Delivery & Implementazione
> **Trigger:** handoff da A3 (contratto firmato + scope congelato + prerequisiti ambiente)
> **Standard:** CF-grade (ADR-007) · **ADR-003:** wrap del motore outreach esistente, mai rewrite

---

## Scopo

Clonare e parametrizzare la pipeline outreach di Digital Empire **sul server del cliente** in
≤7 giorni, renderla multi-tenant (brand_kit + icp del cliente, pattern 11), formare il cliente,
fargli eseguire una run da solo in UAT, e consegnare un handover pack con **zero dipendenza
residua da DE**. Il workflow chiude solo dopo Gate Delivery verde (AG-A4-QA).

---

## Attori

| Step | Agente A4 | Esterno |
|---|---|---|
| Validazione handoff + piano | `ag-a4-coord` | A3 (fornitore contratto) |
| G+0 verifica ambiente | `ag-a4-env` | cliente |
| G+1 setup repo + secrets | `ag-a4-env` | cliente (server) |
| G+2 tenant injection | `ag-a4-tenant` | — |
| G+3-4 test run | `ag-a4-coord` + `ag-a4-env` | — |
| G+5 training | `ag-a4-train` | cliente |
| G+6 UAT | `ag-a4-uat` | cliente |
| G+7 handover | `ag-a4-hand` | cliente |
| Gate Delivery | `ag-a4-qa` | — |
| Distillazione pattern | `ag-a4-learn` | — |

---

## Flusso passo-passo

```
[TRIGGER]
Handoff A3 → AG-A4-COORD
  {delivery_id, cliente_ref, prodotto=outreach-factory, scope_congelato, prerequisiti_ambiente, contratto_firmato}
         │
         ▼
[STEP 0] AG-A4-COORD — validazione handoff + piano
  → contratto firmato? scope congelato? prerequisiti raccolti? Campo mancante → richiesta ad A3
  → memory_search("agency/a4/reasoning") — runbook/pattern per outreach su questo ambiente?
  → apre state in agency/a4/delivery/{delivery_id}; pianifica G+0→G+7
  → GATE-0: handoff completo → prosegui; incompleto → blocca

         │
         ▼
[STEP 1 · G+0] AG-A4-ENV — verifica ambiente cliente (env-precheck.py)
  → OS, Python>=3.11, permessi, rete uscita verso API outreach
  → BIVIO ROLLBACK: ambiente conforme → countdown parte (countdown_start=oggi)
                    non conforme → AG-A4-COORD decide rollback: countdown NON parte,
                    runbook requisiti al cliente, alert a Max (R3, promise 7gg protetta)

         │
         ▼
[STEP 2 · G+1] AG-A4-ENV — setup repo + secrets SUL SERVER CLIENTE
  → clona il motore outreach esistente (ADR-003: wrap, non rewrite) sul server del cliente
  → configura i secrets (SMTP, API) nell'ambiente del cliente — mai nel namespace DE (R6)

         │
         ▼
[STEP 3 · G+2] AG-A4-TENANT — iniezione brand_kit + icp (pattern 11)
  → tenant-injector.py: tono di voce, claim, segmento ICP, linguaggio nei template outreach
  → verifica isolamento: nessun dato/secret di altri tenant; secrets sul server cliente
  → tenant_injected=true

         │
         ▼
[STEP 4 · G+3-4] AG-A4-COORD + AG-A4-ENV — test run su campione piccolo
  → run su un campione ridotto di lead sullo stack parametrizzato del cliente
  → fallisce? debug in dry-run prima di ogni retry (pattern 3); incompatibilità ambiente → issue
  → test_run_passata=true

         │
         ▼
[STEP 5 · G+5] AG-A4-TRAIN — training kit + sessione (delivery-playbook)
  → video walkthrough + runbook operativo + FAQ parametrizzati sul setup del cliente
  → sessione: mostra una run, poi esecuzione guidata; verifica comprensione
  → training_erogato=true

         │
         ▼
[STEP 6 · G+6] AG-A4-UAT — run di accettazione (uat-checklist-builder.py)
  → checklist firmabile dallo scope congelato + check del Gate Delivery
  → run di accettazione con il cliente; poi il cliente esegue 1 RUN DA SOLO
  → firma cliente; uat_firmata=true, run_autonoma_cliente=true
  → fallisce un check → rework verso lo step responsabile → ripeti UAT

         │
         ▼
[STEP 7 · G+7] AG-A4-HAND — handover pack (client-handover)
  → codice completo + README operativo + riferimento credenziali (server cliente) + licenza d'uso
  → verifica zero-dipendenza-DE; se trova key/nodo DE → rework verso AG-A4-TENANT
  → manifest di consegna

         │
         ▼
[STEP 8 · G+7] AG-A4-QA — Gate Delivery (BLOCCANTE)
  → 6 check: gira su server cliente · run reale passata · training erogato · UAT firmata ·
    run autonoma cliente · zero dipendenza residua DE
  → GATE-FINALE: tutti PASS → delivery chiusa · anche uno FAIL → rework mirato → re-gate

         │
         ▼
[STEP 9] Chiusura
  → segnale "delivery chiusa" ad A6 (case study)
  → AG-A4-LEARN distilla pattern → agency/a4/reasoning
  → state aggiornato (stato_finale=handover_completo); entry wiki/log.md
  → avvio finestra supporto 90gg (WF-SUPPORTO-90GG)
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| GATE-0 — Handoff completo | Contratto firmato + scope congelato + prerequisiti presenti | AG-A4-COORD | Apertura delivery |
| GATE-ENV — Ambiente conforme | OS/Python/permessi/rete OK | AG-A4-ENV | Avvio countdown 7gg (R3) |
| GATE-FINALE — Gate Delivery | 6 check PASS (incl. zero dipendenza + run autonoma) | AG-A4-QA | Chiusura handover (R1, R2) |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "delivery_id": "DEL-001",
  "cliente_ref": "CLI-001",
  "prodotto": "outreach-factory",
  "scope_congelato": "riferimento scope",
  "prerequisiti_ambiente": ["OS supportato", "Python>=3.11", "permessi", "rete uscita API"],
  "contratto_firmato": true
}
```

**Output finale:**
```json
{
  "delivery_id": "DEL-001",
  "countdown_start": "2026-07-01",
  "tenant_injected": true,
  "uat_firmata": true,
  "run_autonoma_cliente": true,
  "zero_dipendenza_de": true,
  "gate_delivery": "PASS",
  "stato_finale": "handover_completo",
  "namespace_state": "agency/a4/delivery/DEL-001"
}
```

---

## State

File: `agency/a4/delivery/{delivery_id}/state.json` (+ `agency/a4/uat/{delivery_id}.json`)
- Aggiornato ad ogni step G+0→G+7.
- Ripartibilità a freddo: un agente riprende dal `step_corrente` senza riestrarre il contesto.
- `gate_delivery: PASS` è condizione necessaria per `stato_finale: handover_completo` (R1).

---

## Connessioni

- [[ag-a4-coord]] · `agenti/ag-a4-coord.md`
- [[ag-a4-qa]] · `agenti/ag-a4-qa.md`
- [[WF-DELIVERY-CONTENT-FACTORY]] · `workflow/WF-DELIVERY-CONTENT-FACTORY.md` — stesso schema G+0→G+7
- [[WF-SUPPORTO-90GG]] · `workflow/WF-SUPPORTO-90GG.md` — supporto post-handover
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4`
