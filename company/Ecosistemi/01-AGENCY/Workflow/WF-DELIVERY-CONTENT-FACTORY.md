> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A4 + sez. 1 (HC-AG-CF-01)

# WF-DELIVERY-CONTENT-FACTORY — Delivery Content Factory €3.500

> Workflow L3 di A4-DELIVERY · SLA: ≤7 giorni da ambiente conforme · Dipende da: 03 CONTENT-FACTORY
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A4 + §1

## Cosa è

Delivery del prodotto **Content Factory €3.500**: motore di produzione contenuti AI (caroselli,
script, caption) parametrizzato con `brand_kit` + `icp` del cliente, installato sul suo sistema.
A differenza di Outreach Factory, il motore viene richiesto a 03 CONTENT-FACTORY via handoff
`HC-AG-CF-01` — A4 non produce il motore in-house.

## Flusso

```
INPUT: contratto firmato + {brand_kit, icp, formati_richiesti, deadline}

PRE-DELIVERY:
[HANDOFF VERSO 03 CF — HC-AG-CF-01]
  payload: {client_brand_kit, icp, formati: [caroselli, script_video, caption], deadline: G0}
  acceptance_criteria: motore parametrizzato per cliente, asset conformi brand gate CLIENTE

  → 03 CF produce il motore parametrizzato e lo restituisce via HC-CF-AG-01

GIORNO 1 — Verifica ambiente (T-env-setup):
  - Dipendenze: Python, Node.js (per componenti Next.js), API keys client (es. Canva, Midjourney)
  - Accesso cartella output e struttura brand client
  *** Countdown 7gg parte da ambiente conforme ***

GIORNO 2-3 — Installazione e parametrizzazione (T-config-tenant):
  - Deploy motore CF ricevuto da 03 CF sul server cliente
  - Iniezione brand_kit cliente (palette, tone of voice, template grafici)
  - Iniezione icp cliente (target, pain point, angoli per formato)
  - Run su batch di test: 3 caroselli pilota + 2 script

GIORNO 4-5 — Validazione e revisione (T-uat-runner):
  - Il cliente rivede il batch di test → feedback → 1 ciclo di aggiustamento
  - Gate brand: asset conformi brand gate cliente (approvato dal cliente, non solo da DE)
  - Run completa su calendario contenuti 2 settimane

GIORNO 6 — Training (T-training-kit):
  - Video walkthrough: come generare batch settimanale, come personalizzare template
  - Runbook: aggiornamento brand_kit, aggiunta nuovi formati, gestione errori
  - FAQ specifiche per Content Factory

GIORNO 7 — UAT e Handover (T-uat-runner + T-handover-pack):
  - Il cliente genera autonomamente 1 batch (UAT certificata)
  - UAT firmata → Gate Delivery PASS
  - Handover pack: codice + README + credenziali + licenza d'uso perpetua

OUTPUT: Content Factory live sul sistema cliente, cliente autonomo
```

## Acceptance criteria handoff a 03 CF (HC-AG-CF-01)

- Motore parametrizzato per brand_kit e icp del cliente (multi-tenant, pattern #11)
- Asset conformi brand gate del CLIENTE (non DE)
- Formati corrispondenti a quelli richiesti nel contratto
- Consegnato entro deadline concordata (prima di G1 delivery)

## Gate Delivery (identico agli altri prodotti — A4)

Workflow sul server cliente, run test reale, training erogato, UAT cliente autonomo firmata, nessuna dipendenza residua da DE, handover pack completo.

## Failure

| Evento | Risposta |
|---|---|
| 03 CF non consegna motore in tempo | A4-COORD scala a AG-DIR; delay comunicato a cliente con nuova data |
| Motore CF non conforme acceptance criteria | reject HC-CF-AG-01 con motivazione; 03 CF rework; max 1 reject prima di escalation |
| Brand gate cliente non raggiunto nel batch test | ciclo aggiustamento template; A4 coordina con 03 CF se necessario |

## Connessioni

- [`../Reparti/A4-Delivery/`](../Reparti/A4-Delivery/) — reparto owner
- [`./WF-DELIVERY-OUTREACH-FACTORY.md`](./WF-DELIVERY-OUTREACH-FACTORY.md) · [`./WF-DELIVERY-SECOND-BRAIN.md`](./WF-DELIVERY-SECOND-BRAIN.md)
- [`../Funzioni/T-env-setup/`](../Funzioni/T-env-setup/) · [`T-config-tenant/`](../Funzioni/T-config-tenant/) · [`T-uat-runner/`](../Funzioni/T-uat-runner/)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
