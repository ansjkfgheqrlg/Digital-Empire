> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A4 + sez. 4 + sez. 8

# A4 — OPERATIVITÀ / DELIVERY

> Reparto L2 di 01-AGENCY · Coordinatore: `AG-A4-COORD` (opus) · Topologia: `hierarchical` (delivery attiva) + `star` (ticket 90gg)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A4

## Cosa fa

Consegna i 3 prodotti in **≤7 giorni** con il processo reale: discovery tecnica → setup workflow
sul **server/macchina del cliente** → training → handover del codice. Poi **90 giorni di supporto**.
Il cliente deve poterci "licenziare": autonomia totale a fine handover.

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-DELIVERY-OUTREACH-FACTORY` | clona la pipeline outreach DE, la parametrizza multi-tenant (brand_kit + icp del cliente), setup sul server cliente, run di test, training, handover |
| L3 | `WF-DELIVERY-CONTENT-FACTORY` | richiede a 03 CONTENT-FACTORY il motore parametrizzato (`HC-AG-CF-01`), setup, training, handover |
| L3 | `WF-DELIVERY-SECOND-BRAIN` | richiede a 08 INTELLIGENCE il template second-brain (`HC-IN-AG-01`), setup vault+skill sul sistema cliente, training, handover |
| L3 | `WF-SUPPORTO-90GG` | intake ticket → triage → fix → log; check proattivo settimanale; chiusura a 90gg con review |
| L4 | `T-env-setup` | verifica prerequisiti ambiente cliente (raccolti in discovery), installazione, secrets |
| L4 | `T-config-tenant` | iniezione brand_kit + icp cliente in ogni workflow (pattern #11 multi-tenant) |
| L4 | `T-uat-runner` | run di accettazione con il cliente, checklist UAT firmabile |
| L4 | `T-training-kit` | materiale training: video walkthrough, runbook operativo, FAQ |
| L4 | `T-handover-pack` | pacchetto handover: codice completo, README, credenziali, licenza d'uso |
| L4 | `T-support-triage` | classificazione ticket 90gg (bug / domanda / fuori scope) |

Agenti L5: `AG-A4-COORD` · `AG-A4-ENV-W` · `AG-A4-TENANT-W` · `AG-A4-UAT-W` ·
`AG-A4-TRAIN-W` · `AG-A4-HAND-W` · `AG-A4-SUPP-W` (schede in `../../Agenti/`).

## Come si collega

| Direzione | Con chi | Cosa passa |
|---|---|---|
| ← A3 Preventivi | intra-BUS | contratto firmato + scope congelato + prerequisiti ambiente raccolti in call |
| → A6 Marketing-interno | intra-BUS | segnale "delivery chiusa" → raccolta testimonianza + case study |
| → 03 CONTENT-FACTORY | `HC-AG-CF-01` | richiesta motore CF parametrizzato per il cliente |
| → 08 INTELLIGENCE | `HC-IN-AG-01` | richiesta template second-brain per il cliente |
| ← 09 OPERATIONS | `HC-OP-AG-01` | scheduling check settimanali 90gg, backup ambienti |
| Memoria | `agency/clients` · `agency/delivery` | brand_kit/icp per tenant; checklist UAT, ticket 90gg |

Skill operative: `delivery-playbook` (runbook 7gg per ciascuno dei 3 prodotti), `client-handover`
(genera pacchetto handover), `support-90` (gestione SLA ticket 90gg).

## Come si ATTIVA e RAGIONA

**Trigger.**
1. Contratto firmato + pagamento verificato → A3 apre handoff ad A4 con scope congelato.
2. Ticket in ingresso durante i 90gg → `WF-SUPPORTO-90GG` si attiva.
3. Check settimanale proattivo pianificato da 09 OPERATIONS.

**Decomposizione.** `AG-A4-COORD` (opus) pianifica la delivery in giorni:
- Giorno 1: `T-env-setup` verifica ambiente cliente (OS, permessi, Python, secrets) — il countdown
  7gg parte SOLO ad ambiente conforme (protezione commerciale esplicita nel contratto).
- Giorni 2-5: `T-config-tenant` injetta brand_kit + icp → run di test sullo stack parametrizzato.
- Giorno 6: `T-training-kit` consegna materiale; sessione training con il cliente.
- Giorno 7: `T-uat-runner` run UAT con il cliente; Gate Delivery → firma UAT.
- Stesso giorno: `T-handover-pack` consegna codice completo + README + credenziali + licenza.

**Gate Delivery (bloccante):** workflow funzionante SUL SERVER DEL CLIENTE (non solo in locale);
run di test reale passata; training erogato e materiale consegnato; UAT firmata dal cliente;
zero dipendenze residue da DE (il cliente deve saper eseguire una run da solo in UAT).

**Failure.**
- Ambiente non conforme a Giorno 1 → il countdown NON parte; alert a Max; runbook di
  requisiti inviato al cliente (la promise "7gg" è protetta contrattualmente).
- Run di test fallisce → debug in dry-run prima di ogni retry (pattern #3); se ambiente
  client ha incompatibilità → T-env-setup apre issue con path di risoluzione.
- Ticket 90gg fuori scope → risposta standard + proposta estensione a pagamento separato.
- NPS basso a fine 90gg → pattern distillato in `agency/reasoning`; se ripetuto → audit A4.

## KPI

| KPI | Target |
|---|---|
| Giorni delivery | ≤7 dall'ambiente conforme |
| UAT pass al primo giro | % — baseline dal primo delivery |
| Ticket risolti in SLA | % entro SLA definito nel contratto |
| NPS fine 90gg | misurato, non inventato |

## Connessioni

- [`../../Workflow/WF-DELIVERY-OUTREACH-FACTORY/`](../../Workflow/WF-DELIVERY-OUTREACH-FACTORY/) · [`WF-DELIVERY-CONTENT-FACTORY/`](../../Workflow/WF-DELIVERY-CONTENT-FACTORY/) · [`WF-DELIVERY-SECOND-BRAIN/`](../../Workflow/WF-DELIVERY-SECOND-BRAIN/)
- [`../../Funzioni/T-env-setup/`](../../Funzioni/T-env-setup/) · [`T-uat-runner/`](../../Funzioni/T-uat-runner/) · [`T-handover-pack/`](../../Funzioni/T-handover-pack/)
- [`../A3-Preventivi/`](../A3-Preventivi/) (fornitore contratto) · [`../A6-Marketing-Interno/`](../A6-Marketing-Interno/) (case study)
- [`../../BACKBONE.md`](../../BACKBONE.md) · [`../../ECOSISTEMA.md`](../../ECOSISTEMA.md)
