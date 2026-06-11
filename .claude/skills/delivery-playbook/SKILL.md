---
name: delivery-playbook
description: "Runbook operativo per consegnare uno dei 3 prodotti in <=7 giorni sul server del cliente. Usa questa skill all'avvio di ogni delivery dopo aver ricevuto HC-A3-A4-contratto. Produce checklist giorno per giorno, verifica Gate Delivery, segnala se ambiente non e' conforme. 3 playbook: Outreach Factory, Content Factory, Second Brain."
---

# Skill: delivery-playbook

> Reparto: A4-DELIVERY | Team: T-env-setup, T-config-tenant, T-uat-runner | Tier: sonnet
> Kernel <=500 righe. Per il dettaglio: references/delivery-playbook/

## Scopo

Runbook eseguibile per delivery <=7gg. Il countdown 7gg parte quando l'ambiente cliente
e' verificato conforme. Prima del countdown: solo check ambiente.

## Input atteso

`HC-A3-A4-contratto` payload:
- `prodotto`: outreach_factory | content_factory | second_brain
- `brief_tecnico.ambiente_server`: OS, hosting, accessi
- `brand_kit` + `icp_cliente`
- `client_id`

## Playbook — Outreach Factory (EUR 4.000)

### Pre-giorno-1: verifica ambiente
- [ ] OS identificato (Windows/Linux/Mac)
- [ ] Python 3.10+ installabile
- [ ] Accesso SSH o RDP al server confermato
- [ ] Account email dedicate al dominio pronte (o configurabili)
- [ ] Credenziali SMTP/API email disponibili
- [ ] LinkedIn account cliente (se nel perimetro)
- [ ] .env template condiviso (NO via git — upload sicuro)
SE AMBIENTE NON CONFORME: stop; documenta blocker; avvisa AG-A4-COORD

### Giorno 1: setup infrastruttura
- [ ] Clone pipeline outreach DE sul server cliente (branch privato cliente)
- [ ] Crea .env con credenziali cliente (mai nel repo)
- [ ] Verifica installazione dipendenze (pip install -r requirements.txt)
- [ ] Parametrizza brand_kit + icp nel config cliente
- [ ] Run di smoke test (dry-run, 0 invii reali)

### Giorno 2: configurazione canali
- [ ] Email: verifica deliverability (SPF/DKIM/DMARC se gestibili)
- [ ] Carica leads test (5-10 lead fittizi per test QA)
- [ ] Run bibbia_team.py su template cliente -> gate Bibbia PASS
- [ ] LinkedIn: configura credenziali se nel perimetro

### Giorno 3-4: run pilota
- [ ] Run reale con batch piccolo (20-30 email)
- [ ] Verifica log: nessun errore critico
- [ ] Verifica rate limiting rispettato (cap 100/h)
- [ ] Monitora bounces (target <5%)

### Giorno 5-6: ottimizzazione + training
- [ ] Aggiusta configurazioni in base ai risultati pilota
- [ ] Sessione training con cliente: run da zero, lettura log, gestione risposte
- [ ] Consegna runbook operativo + FAQ scritta

### Giorno 7: handover
- [ ] Il CLIENTE esegue una run completa da solo (Gate Delivery: autonomia dimostrata)
- [ ] Checklist UAT compilata e firmata dal cliente
- [ ] Handover pack consegnato (skill client-handover)
- [ ] Supporto 90gg attivato (skill support-90)

## Playbook — Content Factory (EUR 3.500)

### Pre-giorno-1
- [ ] Richiesta motore parametrizzato a 03-CONTENT-FACTORY via HC-AG-CF-01
- [ ] brand_kit cliente pronto (nome, tono, target, formati richiesti)
- [ ] Ambiente cliente: Node.js o accesso API sufficiente

### Giorno 1-2: setup + parametrizzazione
- [ ] Ricezione asset da 03-CF (gate QA CF verificato)
- [ ] Setup sul server cliente con brand_kit iniettato
- [ ] Run test: genera 3 caroselli demo con brand del cliente

### Giorno 3-5: validazione + training
- [ ] Cliente approva output di esempio
- [ ] Training: come usare il sistema, come modificare prompt
- [ ] Runbook consegnato

### Giorno 6-7: handover
- [ ] Cliente genera contenuto autonomamente (Gate Delivery)
- [ ] UAT firmata
- [ ] Handover pack (client-handover)

## Playbook — Second Brain (EUR 2.500)

### Pre-giorno-1
- [ ] Richiesta template second-brain a 08-INTELLIGENCE via HC-IN-AG-01
- [ ] Identificato tool cliente: Obsidian / Notion / altro
- [ ] Definito scope: dominio di conoscenza da strutturare

### Giorno 1-2: setup vault + skill Claude
- [ ] Setup vault/workspace sul sistema cliente
- [ ] Installazione skill memory-empire o equivalente
- [ ] Import conoscenza esistente cliente (se disponibile)

### Giorno 3-5: personalizzazione + training
- [ ] Struttura wiki personalizzata per nicchia/business cliente
- [ ] Training: come aggiornare, interrogare, collegare note
- [ ] Template popolati con esempi reali del cliente

### Giorno 6-7: handover
- [ ] Cliente usa il sistema autonomamente (Gate Delivery)
- [ ] UAT firmata
- [ ] Handover pack

## Gate Delivery — checklist finale (tutti DEVONO essere PASS)

- [ ] Workflow/sistema funzionante SUL SERVER DEL CLIENTE (non solo locale DE)
- [ ] Run di test REALE passata
- [ ] Training erogato e materiale consegnato
- [ ] Handover pack completo (codice/config, README, credenziali, licenza)
- [ ] UAT FIRMATA dal cliente
- [ ] Cliente ha dimostrato autonomia operativa nella sessione UAT
- [ ] Nessuna dipendenza residua da DE

## Connessioni

- `company/01-agency/A4-DELIVERY/BACKBONE.md`
- Skill `client-handover` — genera il pack finale
- Skill `support-90` — attivata dopo Gate Delivery
- `company/01-agency/A3-PREVENTIVI/handoffs/HC-A3-A4-contratto.json`
