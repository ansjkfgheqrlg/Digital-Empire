---
Type: STATE
Status: Active
Tags: #state #namespace #memoria #agency #delivery #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# State — A4 Delivery & Implementazione

> Definizione dei namespace memoria, struttura dei file di stato, regole di integrità,
> e lifecycle degli artefatti del reparto.
> **Nessun PII/segreto cliente nello schema** (Regola R6): solo riferimenti e flag.

---

## Namespace memoria del reparto

| Namespace | Path AgentDB | Contenuto | Owner scrittura | Chi legge |
|---|---|---|---|---|
| Delivery | `agency/a4/delivery/` | Delivery attive/chiuse: piano G+0→G+7, stato per step, esito Gate | AG-A4-COORD | AG-A4-QA, AG-A4-LEARN |
| UAT | `agency/a4/uat/` | Checklist UAT firmabili/firmate; esito run autonoma cliente | AG-A4-UAT | AG-A4-QA, AG-A4-COORD |
| Environments | `agency/a4/environments/` | Profili ambiente cliente: flag conformità (no secrets) | AG-A4-ENV | AG-A4-COORD, AG-A4-LEARN |
| Support | `agency/a4/support/` | Ticket 90gg: classe, SLA, stato, conferma cliente, check settimanali | AG-A4-SUPP | AG-A4-COORD, A7 |
| Reasoning | `agency/a4/reasoning/` | Pattern delivery distillati: ambienti critici, errori ricorrenti | AG-A4-LEARN | AG-A4-COORD, AG-DIR |

---

## Struttura file di stato

### Delivery state (`agency/a4/delivery/{delivery_id}/state.json`)

```json
{
  "delivery_id": "DEL-001",
  "cliente_ref": "CLI-001",
  "prodotto": "outreach-factory | content-factory | second-brain",
  "ambiente_conforme": false,
  "countdown_start": "YYYY-MM-DD | null",
  "step_corrente": "G+0 | G+1 | G+2 | G+3-4 | G+5 | G+6 | G+7",
  "tenant_injected": false,
  "test_run_passata": false,
  "training_erogato": false,
  "uat_firmata": false,
  "run_autonoma_cliente": false,
  "zero_dipendenza_de": false,
  "gate_delivery": "pending | PASS | FAIL",
  "gate_fail_motivo": "optional — dettaglio se FAIL",
  "stato_finale": "in_progress | handover_completo | archiviato",
  "last_updated": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### UAT state (`agency/a4/uat/{delivery_id}.json`)

```json
{
  "delivery_id": "DEL-001",
  "checklist_id": "UAT-001",
  "data_uat": "YYYY-MM-DD",
  "checks": [
    {"check": "workflow gira sul server cliente", "esito": "PASS | FAIL"},
    {"check": "run reale passata", "esito": "PASS | FAIL"},
    {"check": "cliente esegue 1 run da solo", "esito": "PASS | FAIL"}
  ],
  "uat_firmata": false,
  "firma_riferimento": "riferimento documento firmato (no PII inline)",
  "run_autonoma_cliente": false
}
```

### Support state (`agency/a4/support/{ticket_id}.json`)

```json
{
  "ticket_id": "TKT-001",
  "delivery_id": "DEL-001",
  "data_ingresso": "YYYY-MM-DDTHH:MM:SSZ",
  "classe": "bug | domanda | fuori_scope",
  "sla_target_h": 24,
  "risolto_entro_sla": false,
  "stato": "aperto | in_lavorazione | risolto | chiuso",
  "conferma_cliente": false,
  "proposta_upsell_a6": "optional — se fuori_scope",
  "giorno_dei_90": 12
}
```

### Environment profile (`agency/a4/environments/{cliente_ref}.json`)

```json
{
  "cliente_ref": "CLI-001",
  "os": "linux | windows | macos",
  "python_presente": true,
  "python_versione_ok": true,
  "permessi_ok": true,
  "rete_uscita_ok": true,
  "ambiente_conforme": true,
  "note_issue": "lista issue bloccanti — nessun secret, nessuna credenziale"
}
```

---

## Regole di integrità dei namespace

1. **Delivery senza `gate_delivery: PASS`** — una delivery in `stato_finale: handover_completo`
   deve avere `gate_delivery: "PASS"`. Se è `FAIL` o `pending`, non può essere `handover_completo`.
   AG-A4-QA è responsabile (Regola R1).

2. **Countdown su ambiente non conforme** — `countdown_start` non può essere valorizzato se
   `ambiente_conforme: false`. Anomalia segnalata da AG-A4-COORD (Regola R3).

3. **Zero dipendenza residua** — `gate_delivery` non può essere `PASS` se `zero_dipendenza_de: false`
   o `run_autonoma_cliente: false`. È il cuore dell'identità DE (Regola R2).

4. **Ticket senza conferma cliente** — un ticket in `stato: "chiuso"` deve avere
   `conferma_cliente: true`. AG-A4-SUPP è responsabile (Regola R5).

5. **Nessun secret/PII** — nessun file di stato contiene secrets, credenziali o dati personali
   del cliente: solo flag, versioni e riferimenti (Regola R6).

6. **Ripartibilità a freddo** — tutti i file di stato hanno `last_updated`. Un agente che riprende
   una delivery interrotta legge lo state per sapere a quale step (G+N) riprendere.

---

## Lifecycle degli artefatti

| Artefatto | Creazione | Aggiornamento | Archiviazione |
|---|---|---|---|
| Delivery state | Apertura delivery (handoff A3) | Ad ogni step G+0→G+7 | Dopo `handover_completo`; non eliminato |
| UAT state | Step G+6 (UAT) | Alla firma | Archiviato con la delivery |
| Support state | Ingresso ticket | Ad ogni cambio stato + check settimanale | Chiuso con conferma cliente; non eliminato |
| Environment profile | Step G+0 | Se ambiente cambia | Conservato come riferimento per pattern (LEARN) |

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md §4` — namespace e integrazione con i fornitori di motore
- [[WF-DELIVERY-OUTREACH-FACTORY]] · `workflow/WF-DELIVERY-OUTREACH-FACTORY.md` — produce delivery + uat state
- [[WF-SUPPORTO-90GG]] · `workflow/WF-SUPPORTO-90GG.md` — produce support state
- [[kpi/KPI]] · `kpi/KPI.md` — i KPI si misurano a partire da questi namespace
