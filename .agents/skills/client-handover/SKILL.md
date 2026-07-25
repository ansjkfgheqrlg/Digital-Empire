---
name: client-handover
description: "Genera il pacchetto handover completo per un cliente a fine delivery. Usa dopo Gate Delivery PASS (UAT firmata). Output: README operativo, indice credenziali, licenza d'uso, video-index training, checklist di autonomia post-handover."
---

# Skill: client-handover

> Reparto: A4-DELIVERY | Team: T-handover-pack | Tier: sonnet
> Nota: e' anche un PRODOTTO — la versione per il cliente Outreach Factory include questo pack.

## Scopo

Produrre il pacchetto handover che rende il cliente completamente autonomo da DE.
Questo pack e' la prova tangibile della promessa "l'agenzia progettata per essere licenziata".

## Input atteso

- `client_id` + `prodotto`
- `brand_kit` + `icp` del cliente
- Path del codice/config deployato sul server cliente
- Lista credenziali gestite (senza i valori — quelli vanno nell'env del cliente)
- Appunti sessione training

## Output — struttura pack

```
handover-<nome_azienda>-<data>/
├── README-operativo.md          (guida step-by-step per operare il sistema)
├── runbook-giornaliero.md       (check quotidiani, cosa monitorare, come interpretare i log)
├── faq.md                       (domande frequenti emerse in training)
├── credenziali-index.md         (elenco variabili .env — SENZA valori, solo nomi e descrizione)
├── licenza-uso.md               (codice di proprieta' del cliente, EUR 0 canoni, scope)
├── video-training-index.md      (indice dei video walkthrough registrati in sessione)
└── checklist-autonomia.md       (5 azioni che il cliente sa fare da solo -> firmabile)
```

## README-operativo — struttura minima

1. **Avvio rapido** (3 comandi per far girare il sistema)
2. **Operazioni quotidiane** (cosa fare ogni giorno, quanto tempo richiede)
3. **Come leggere i log** (cosa e' normale, cosa e' un errore)
4. **Come aggiornare i template** (senza toccare il codice core)
5. **Cosa NON fare** (list di azioni che rompono il sistema)
6. **Contatto supporto 90gg** (canale, tempi di risposta, scope)

## Checklist autonomia (Gate Delivery richiede tutte checked)

- [ ] Il cliente sa avviare una run da zero
- [ ] Il cliente sa leggere il report di esito
- [ ] Il cliente sa aggiungere/modificare un template
- [ ] Il cliente sa fermare il sistema in caso di errore
- [ ] Il cliente sa dove trovare i log e come interpretarli

## Regola sicurezza

I valori reali di .env, cookie di sessione, API key NON vanno nel pack.
Il pack documenta NOMI e SCOPO di ogni variabile. I valori rimangono nel .env del cliente.

## Connessioni

- `company/01-agency/A4-DELIVERY/BACKBONE.md`
- Skill `delivery-playbook` — questo pack e' l'output del giorno 7
- Skill `support-90` — attivata insieme a questo pack
