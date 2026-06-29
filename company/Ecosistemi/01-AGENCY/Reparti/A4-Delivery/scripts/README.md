---
Type: SCRIPTS
Status: Planned (target V2)
Tags: #scripts #agency #delivery #uat #handover #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# Script — A4 Delivery & Implementazione

> Script di supporto del reparto. Target V2 — deterministici, nessuna spesa API autonoma.
> Standard: ogni script accetta input strutturato, produce output JSON o MD, nessun side-effect
> senza input esplicito, eseguibile da AG-A4-COORD senza approvazione aggiuntiva.
> ADR-003: gli script wrappano i motori esistenti, non li riscrivono.

---

## Script pianificati (build in V2)

### `env-precheck.py`

**Scopo:** esegue il check di conformità ambiente cliente prima del countdown 7gg. Verifica
prerequisiti (OS, versione Python, permessi, rete in uscita verso le API necessarie) e produce
il verdetto di conformità. Supporto a AG-A4-ENV al G+0.

**Input:** `{delivery_id, prerequisiti_attesi[], output_check_cliente.json}`
**Output:** `env_report_{delivery_id}.json` con flag PASS/FAIL per prerequisito + verdetto
`ambiente_conforme` (bool) + lista issue bloccanti. Mai secrets: solo flag presenza/versione.
**Prerequisiti:** lista prerequisiti raccolta da A3 in discovery; output del check eseguito
sul server del cliente (nessuna connessione autonoma da DE).

---

### `tenant-injector.py`

**Scopo:** genera la configurazione multi-tenant (pattern 11) iniettando `brand_kit` + `icp`
del cliente nei template dei workflow. Produce i file di config parametrizzati pronti per
il deploy sul server cliente. Supporto a AG-A4-TENANT al G+2.

**Input:** `{delivery_id, brand_kit.json, icp.json, workflow_templates[]}`
**Output:** `tenant_config_{delivery_id}/` con i file di config per ogni workflow + manifest
di iniezione. I valori vivono nei file destinati al server cliente, non nel namespace DE.
**Prerequisiti:** brand_kit + icp del cliente (da A3/discovery); template workflow del motore.

---

### `uat-checklist-builder.py`

**Scopo:** genera la checklist UAT firmabile a partire dal prodotto consegnato e dallo scope
congelato. Produce il documento di accettazione con i check obbligatori (incl. "run autonoma
cliente eseguita"). Supporto a AG-A4-UAT al G+6 e a AG-A4-QA per il Gate Delivery.

**Input:** `{delivery_id, prodotto, scope_congelato, gate_checks[]}`
**Output:** `uat_checklist_{delivery_id}.md` firmabile + `uat_state_{delivery_id}.json`
con campi `uat_firmata`, `run_autonoma_cliente`, `gate_delivery`.
**Prerequisiti:** scope congelato da A3; lista check del Gate Delivery (ARCHITETTURA §3).

---

## Convenzioni

- Tutti gli script producono file in `agency/a4/` (namespace corretto) — mai fuori.
- Nessun script fa chiamate API esterne autonome senza input esplicito dell'operatore.
- Nessun secret o PII cliente negli output: solo flag, versioni, riferimenti (Regola R6).
- Output JSON segue lo schema del namespace corrispondente (vedi `state/README.md`).
- Versione: i file output hanno suffisso `_v{N}` per tracciare le iterazioni.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §4` — namespace memoria su cui gli script scrivono
- [[WF-DELIVERY-OUTREACH-FACTORY]] · `workflow/WF-DELIVERY-OUTREACH-FACTORY.md` — usa `env-precheck.py` + `tenant-injector.py`
- [[WF-SUPPORTO-90GG]] · `workflow/WF-SUPPORTO-90GG.md` — produce log ticket nel namespace support
- [[state/README]] · `state/README.md` — schema degli output JSON
