> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A4 + sez. 4 (step 7) + sez. 8 (Gate Delivery)

# WF-DELIVERY-OUTREACH-FACTORY — Delivery Outreach Factory €4.000

> Workflow L3 di A4-DELIVERY · SLA: ≤7 giorni da ambiente conforme
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A4 + §8

## Cosa è

Delivery del prodotto **Outreach Factory €4.000**: clone della pipeline outreach DE,
parametrizzata multi-tenant (`brand_kit` + `icp` del cliente), installata e funzionante
sul server/macchina del cliente. Il cliente esce autonomo: sa eseguire da solo ogni run.

## Flusso giorno per giorno (skill `delivery-playbook`)

```
INPUT: contratto firmato + scope congelato + {prerequisiti_ambiente, brand_kit, icp} da A3

GIORNO 1 — Verifica ambiente (T-env-setup):
  - OS, Python versione, permessi cartelle
  - Accesso SMTP / credenziali email
  - Sessioni LinkedIn / Instagram disponibili (locale cliente)
  - Secrets manager o .env configurato
  *** Il countdown 7gg parte SOLO se ambiente conforme ***
  *** Se non conforme → runbook requisiti al cliente, countdown in pausa ***

GIORNO 2 — Clone e parametrizzazione (T-config-tenant):
  - Clone della pipeline da repo DE (versione stabile, non main)
  - Iniezione brand_kit: nome azienda, firma email, CTA, tono
  - Iniezione icp: settore target, pain point primari, regole di qualifica
  - Config cap: email ≤500/gg cap 100/h · LI 20+20+30/gg · IG 30 DM/gg (INVARIATI)

GIORNO 3-4 — Run di test (T-config-tenant + T-uat-runner):
  - Dry-run su batch piccolo (10 lead): anteprima messaggi, nessun invio reale
  - Run reale su batch 20 lead: verifica invio, log, dashboard
  - Verifica Gate Bibbia sul messaggio parametrizzato del cliente (brand voice cliente)

GIORNO 5-6 — Training (T-training-kit):
  - Video walkthrough: avvio run, monitoraggio dashboard, gestione risposte
  - Runbook operativo: checklist giornaliera, cosa fare se errore
  - FAQ: domande più comuni post-training

GIORNO 7 — UAT e Handover (T-uat-runner + T-handover-pack):
  - Il CLIENTE esegue da solo una run da 20 lead (UAT certificata)
  - UAT checklist firmata dal cliente
  - Handover pack: codice completo, README, credenziali, licenza d'uso perpetua

OUTPUT: Outreach Factory installata e funzionante sul server del cliente
        UAT firmata → Gate Delivery PASS → segnale ad A6 per testimonianza
```

## Gate Delivery (bloccante)

- Workflow funzionante SUL SERVER DEL CLIENTE (non in locale DE)
- Run di test reale passata con log verificabile
- Training erogato e materiale consegnato
- Il cliente ha eseguito almeno 1 run autonoma durante UAT
- UAT checklist firmata dal cliente
- Nessuna dipendenza residua da DE (nessun tool, API key o accesso che il cliente non controlla)
- Handover pack completo consegnato

## I/O

| | Dettaglio |
|---|---|
| **Input** | contratto firmato + `{brand_kit, icp, prerequisiti_ambiente}` da A3 |
| **Output** | UAT firmata + handover pack + segnale a A6; record delivery in `agency/clients` + `agency/delivery` |

## Failure

| Evento | Risposta |
|---|---|
| Ambiente non conforme G1 | countdown in pausa; runbook requisiti al cliente; alert a Max; SLA riparte da ambiente conforme |
| Run di test fallisce | debug in dry-run; se incompatibilità OS → matrice fallback in `delivery-playbook` |
| Cliente non disponibile per UAT | ripianifica entro 48h; oltre 48h → alert a Max (countdown scade comunque) |
| Dipendenza residua scoperta in UAT | bloccante: risolta prima della firma UAT |

## Note multi-tenant (pattern #11)

Ogni cliente ha il suo namespace: `agency/clients/{client_id}` con `{brand_kit, icp, milestone_delivery}`.
Le credenziali del cliente NON vanno in repo né in namespace condivisi. Il codice consegnato
è **di proprietà del cliente** (licenza d'uso perpetua, zero canoni DE).

## Connessioni

- [`../Reparti/A4-Delivery/`](../Reparti/A4-Delivery/) — reparto owner
- [`./WF-DELIVERY-CONTENT-FACTORY.md`](./WF-DELIVERY-CONTENT-FACTORY.md) · [`./WF-DELIVERY-SECOND-BRAIN.md`](./WF-DELIVERY-SECOND-BRAIN.md)
- [`../Funzioni/T-env-setup/`](../Funzioni/T-env-setup/) · [`T-config-tenant/`](../Funzioni/T-config-tenant/) · [`T-uat-runner/`](../Funzioni/T-uat-runner/) · [`T-handover-pack/`](../Funzioni/T-handover-pack/)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
