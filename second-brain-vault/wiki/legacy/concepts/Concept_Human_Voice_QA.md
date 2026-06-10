---
Type: CONCEPT
Status: Active
Tags: #quality-assurance #ai-writing #humanness #cold-email #framework
Created: 2026-04-30
Last updated: 2026-04-30
---

# Concept: Human Voice QA

## Overview

Il Human Voice QA è il framework di controllo qualità del linguaggio che garantisce che le email generate da AI sembrino scritte da un essere umano. Nato nel sistema outreach DE v2.0, è applicabile a qualsiasi contenuto testuale generato da AI.

## Il Problema che Risolve

I modelli AI tendono a produrre pattern linguistici riconoscibili:
- Aperture formali e generiche ("Spero che stia bene")
- Corporate jargon ("sinergie", "trasformazione digitale", "soluzione innovativa")
- Strutture troppo simmetriche e prevedibili
- Assenza di specificità concreta (numeri, osservazioni dirette)
- Tono da venditore invece che da consulente

Questi pattern abbassano drasticamente i tassi di risposta nelle cold email.

## I 3 Check in Sequenza

### Check 1 — Humanness Detector (score 1-10)

Valuta se il testo sembra scritto da un umano reale.

**Pattern che abbassano il punteggio:**
- "Spero che stia bene", "Mi permetto di contattarla"
- "In qualità di esperto", "In questo contesto"
- Aggettivi vuoti: eccellente, straordinario, rivoluzionario
- Struttura rigida template intro→body→chiusura formale

**Pattern che alzano il punteggio:**
- Apertura con osservazione specifica e verificabile
- Frasi brevi e dirette
- Uso naturale del "tu/voi"
- Specificità con numeri credibili
- Una sola domanda finale

### Check 2 — Direct Response Compliance (score 1-10)

Verifica la compliance con il framework APSOC.

**Elementi valutati:**
- A: prima riga specifica e concreta?
- P: problema quantificato con impatto reale?
- P: soluzione collegata al problema?
- S: riferimento settoriale come social proof?
- O: obiezione anticipata (anche brevemente)?
- C: una sola CTA morbida?

**Penalità automatiche:**
- Più di 1 CTA: -3 punti
- Nessuna specificità nella prima riga: -2 punti
- Corpo > 150 parole: -2 punti

### Check 3 — Brand Voice Validation (score 1-10)

Confronta con il benchmark qualitativo: Andrei Pascu.

**Criteri:**
- Il mittente sembra un consulente che ha già fatto i compiti? (+2)
- Ogni frase porta informazione nuova? (+2)
- Tono paritario, non speranzoso/servile? (+2)
- Vocabolario approvato, zero corporate jargon? (+2)
- Lunghezza appropriata (100-130 parole)? (+2)

## Decisione Finale

```
Media dei 3 score:
  ≥ 7.0 → APPROVATA → passa all'invio
  < 7.0 → RESPINTA → feedback dettagliato → 1 retry writer
              → secondo check
              → se passa: invio
              → se non passa: SCARTATA (non inviare)
```

**Tasso di scarto atteso**: < 5% con prompt ben costruiti.

## Check Deterministici Pre-AI

Prima ancora di passare agli scorer AI, vengono eseguiti check deterministici:
- Lista di 30+ frasi vietate (ricerca esatta nel testo)
- Lista di 20+ termini corporate banditi
- Conteggio parole (soglia: 150 parole)

Questi check sono istantanei e gratuiti (Python puro).

## Principio del Revision Loop

Il sistema ammette **massimo 1 revisione** per email. Questo perché:
1. Se un'email necessita più di 1 revisione, il problema è nel prompt del writer
2. Il costo di multipli retry con AI free è comunque time-cost
3. Meglio scartare e sostituire con un'altra email di qualità

## Applicazione oltre l'Outreach

Il framework Human Voice QA è riutilizzabile per:
- Contenuti social media generati da AI
- Newsletter e email marketing
- Articoli di blog con AI assist
- Script video/podcast

Il principio è sempre lo stesso: un contenuto AI efficace non deve sembrare AI.

## Connessioni

- [[Tool_Outreach_MultiTeam_System]] — prima implementazione di questo framework
- [[Concept_APSOC_Email_Application]] — il check 2 verifica compliance APSOC
- [[Andrei_Pascu]] — benchmark per il check 3 (Brand Voice)
- [[Concept_Copywriting_Framework]] — framework copy di riferimento
