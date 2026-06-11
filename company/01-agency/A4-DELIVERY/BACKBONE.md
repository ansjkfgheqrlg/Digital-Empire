# BACKBONE — A4 DELIVERY + SUPPORTO 90GG

> Reparto L2 di 01-AGENCY. Schema canonico: coordinator, I/O, acceptance_criteria, failure_handling, shared_state.

## Coordinator

**AG-A4-COORD** (opus) — orchestratore reparto.
Responsabilita': consegnare i 3 prodotti in <=7 giorni sul SERVER DEL CLIENTE, poi 90gg supporto.
Promessa commerciale: setup su macchina cliente, training, handover codice — autonomia totale.

## Team L3 / L4

| ID | Livello | Tipo | Flusso |
|---|---|---|---|
| WF-DELIVERY-OUTREACH-FACTORY | L3 | workflow | clona pipeline outreach DE, parametrizza multi-tenant, setup server cliente, run test, training, handover |
| WF-DELIVERY-CONTENT-FACTORY | L3 | workflow | richiede motore a 03-CONTENT-FACTORY (HC-AG-CF-01), setup, training, handover |
| WF-DELIVERY-SECOND-BRAIN | L3 | workflow | richiede template a 08-INTELLIGENCE (HC-IN-AG-01), setup vault+skill, training, handover |
| WF-SUPPORTO-90GG | L3 | workflow | intake ticket -> triage -> fix -> log; check proattivo settimanale; chiusura a 90gg |
| T-env-setup | L4 | worker (sonnet) | verifica prerequisiti ambiente cliente, installazione, secrets |
| T-config-tenant | L4 | worker (sonnet) | iniezione brand_kit + icp cliente in ogni workflow (pattern 11 multi-tenant) |
| T-uat-runner | L4 | worker (sonnet) | run accettazione con cliente, checklist UAT firmabile |
| T-training-kit | L4 | worker (sonnet) | materiale training: video walkthrough, runbook operativo, FAQ |
| T-handover-pack | L4 | worker (sonnet) | pacchetto: codice completo, README, credenziali, licenza d'uso |
| T-support-triage | L4 | worker (haiku) | classificazione ticket: bug / domanda / fuori scope + SLA |

## I/O

**Input:**
- Contratto firmato + pagamento confermato da A3 via `HC-A3-A4-contratto`
  Payload: client_id, prodotto, brief_tecnico, brand_kit, icp

**Output:**
- Delivery completata -> A6 via `HC-A4-A6-testimonianza`
  Payload: client_id, metriche_reali, uat_firmata, prodotto_consegnato
- Know-how delivery -> 05-MULTI-BUSINESS via `HC-AG-MB-01`
- Ticket supporto -> loggati in agency/delivery

## Acceptance Criteria (Gate Delivery)

1. Workflow funzionante SUL SERVER DEL CLIENTE (non solo in locale DE)
2. Run di test reale passata (non simulata)
3. Training erogato e materiale consegnato (runbook operativo)
4. Handover pack completo: codice, README, credenziali, licenza
5. Checklist UAT FIRMATA dal cliente
6. Nessuna dipendenza residua da DE (il cliente puo' operare autonomamente)
7. Completato in <=7 giorni (dal momento in cui l'ambiente e' conforme)

## Regola autonomia cliente

"L'agenzia progettata per essere licenziata": il cliente DEVE saper eseguire una run da solo
durante la sessione UAT. Solo allora il Gate Delivery si considera PASS.
Upsell attivo SOLO dopo Gate Delivery + segnale positivo a fine 90gg.

## Failure Handling

| Failure | Azione |
|---|---|
| Ambiente cliente non conforme il giorno 1 | Giorno 1 = solo verifica; il countdown 7gg parte da ambiente conforme; log ritardo |
| UAT non firmata dopo 7gg | Escalation a AG-DIR + Max; log motivo; piano di rimedio |
| Bug in delivery | Fix immediato; log ticket in agency/delivery; conta verso SLA 90gg |
| Delivery > 7gg | Log in agency/reasoning come pattern; analisi causa; notifica FORGE se ricorrente |
| Cliente dipendente da DE a fine 90gg | Training extra; log come failure di autonomia; aggiorna delivery-playbook |

## Shared State (AgentDB)

Namespace: `agency/clients` (PII — sempre aidefence_has_pii prima dello store)

```json
{
  "client_id": "string",
  "cycle_id": "CY-YYYYMMDD-NNN",
  "prodotto": "outreach_factory | content_factory | second_brain | engine_room",
  "brand_kit": { "nome": "", "tono": "", "target": "" },
  "icp": { "nicchia": "", "size": "", "problema_principale": "" },
  "ambiente_cliente": { "os": "", "server": "", "note": "" },
  "delivery_started_at": null,
  "delivery_completed_at": null,
  "uat_signed_at": null,
  "supporto_ends_at": null,
  "gate_delivery": "pending | pass | fail"
}
```

Namespace: `agency/delivery`

```json
{
  "ticket_id": "string",
  "client_id": "string",
  "tipo": "bug | domanda | fuori_scope",
  "aperto_at": "ISO 8601",
  "chiuso_at": null,
  "in_sla": true,
  "risoluzione": ""
}
```

## Connessioni

- `A3-PREVENTIVI/BACKBONE.md` — contratto in ingresso
- `A6-MARKETING-INTERNO/BACKBONE.md` — testimonianza in uscita
- `company/Backbone/Bus/contracts/` — HC-A3-A4-contratto.json, HC-A4-A6-testimonianza.json
- `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` sez. 2 (A4) + sez. 8 (Gate Delivery)
