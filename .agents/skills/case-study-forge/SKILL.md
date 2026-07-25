---
name: case-study-forge
description: "Da delivery completata a case study APSOC con metriche verificate. Usa dopo Gate Delivery PASS + testimonianza raccolta. NON pubblicare senza prova reale verificata dal cliente. Output: case study strutturato pronto per landing/blog + asset brief per 03-CONTENT-FACTORY."
---

# Skill: case-study-forge

> Reparto: A6-MARKETING-INTERNO | Team: T-case-writer | Tier: sonnet

## Scopo

Trasformare una delivery completata in un case study APSOC autentico.
Regola ferrea: "prove non promesse" — ogni affermazione deve essere verificabile.

## Input atteso

- `HC-A4-A6-testimonianza` payload (metriche_reali, uat_firmata)
- Testimonianza diretta del cliente (citazione approvata o permesso firmato)
- Prodotto consegnato + nicchia

## Processo

### 1. Raccolta prove (T-proof-collector fa questo)
- Chiedi al cliente le metriche REALI (screenshot, dashboard, numeri specifici)
- Solo metriche che il cliente ha visto e puo' confermare
- Ottieni approvazione esplicita all'uso nel case study

### 2. Struttura APSOC

**A — Attenzione**
Hook: il problema specifico della nicchia, reso concreto
(NO generici come "vuoi piu' clienti?" — usa il problema reale di questa nicchia)

**P — Problema**
Situazione prima: cosa non funzionava, quantificato se possibile
Causa radice: perche' il problema esisteva (non limitarsi al sintomo)

**S — Soluzione**
Cosa abbiamo fatto: step reali della delivery
Come e' stata personalizzata per questo cliente

**O — Obiezioni (affrontate)**
Dubbi che il cliente aveva prima di partire
Come sono stati risolti

**C — CTA**
Risultati reali ottenuti (SOLO numeri verificati)
Testimonianza diretta del cliente (citazione)
CTA: link presentazione-empire.vercel.app

### 3. Regole "prove non promesse"

VIETATO:
- "Puo' aumentare le vendite di X%"
- "In media i clienti ottengono..."
- Qualsiasi proiezione futura

CONSENTITO:
- "In questo caso specifico, [nome_azienda] ha ottenuto X in Y settimane"
- "Secondo il report di [nome_azienda], il reply rate e' passato da X a Y"
- Citazioni dirette del cliente (con approvazione)

### 4. Asset brief per 03-CONTENT-FACTORY

Dopo aver scritto il case study, genera brief per asset social:
- Formato: carosello LinkedIn (5-7 slide)
- Elemento: la metrica piu' forte come hook
- Tone of voice: brand DE (diretto, provocatorio, con prova)

## Output

1. `case-study-<nome_azienda>-<data>.md` — testo completo
2. `social-brief-<nome_azienda>.json` — brief per 03-CF (HC-AG-CF-01)

## Connessioni

- `company/01-agency/A6-MARKETING-INTERNO/BACKBONE.md`
- `company/01-agency/A4-DELIVERY/handoffs/HC-A4-A6-testimonianza.json`
- `company/Mandato/MANDATO-EMPIRE.md` — "prove non promesse"
