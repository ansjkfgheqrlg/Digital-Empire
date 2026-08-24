---
Type: SOURCE
Status: Active
Tags: #email-copywriting #merge-tag #personalizzazione #andrei-pascu #short-form #crm
Created: 2026-08-23
Last updated: 2026-08-23
---

# Source: Andrei Pascu — Merge Tag nell'email marketing

## Overview
Reel talking-head 91s con overlay grafici densi (chat bubble finte stile UI messaggistica, testo animato, 1 clip di repertorio da *The Wolf of Wall Street*, 1 foto stock meme). Spiega cosa sono i merge tag (campi email dinamici tipo {{nome}}), poi va oltre la definizione base mostrando come gestire con un CRM il caso in cui il dato manca: invece di lasciare uno spazio vuoto dopo "Ciao,", si può impostare un **fallback concatenato** (es. "nome/iscritto") che stampa un valore di riserva coerente quando il campo primario è assente — tecnica generalizzabile a qualsiasi altro punto dell'email (CTA, riferimenti allo stato utente). Video 15/29 del run cat1-copywriting andrei-pascu-001.

## Dati Tecnici

- **Video ID:** yX0XZh2PSYo
- **Durata:** 91s
- **Formato:** Talking-head selfie/POV + overlay chat-bubble UI densi, 1 clip repertorio, 1 foto stock
- **Lingua:** ITA
- **Frame:** 46 @2s | Frame letti: 46/46 (coverage 100%) | NO-FINTO: PASS
- **KA:** 7 | VP: 20 | Sezioni: 7 | Pattern: 3
- **Processing:** 2026-08-23

## Sezioni e Contenuto

| Sezione | Timestamp | Contenuto |
|---------|-----------|-----------|
| S1 | 0:00-0:15 | Hook — esempio Decathlon ("Ciao Andrei" / "Ciao Maria") |
| S2 | 0:15-0:30 | Definizione merge tag (campo dinamico da dato di iscrizione) |
| S3 | 0:30-0:40 | Livello base vs "top G" — sostituti/fallback ai merge tag |
| S4 | 0:40-1:00 | Problema campo vuoto + soluzione fallback CRM |
| S5 | 1:00-1:06 | Interludio pop-culture (Andro8 / Wolf of Wall Street) |
| S6 | 1:06-1:24 | Generalizzazione: fallback chain su CTA/altri campi |
| S7 | 1:24-1:31 | Chiusura — "modifica semplice da fare oggi" |

## Key Quotes

> "Quelli si chiamano merge tag e sono campi che vengono cambiati in automatico in base alla persona a cui è destinata la mail"

> "Email marketer basilari sanno cos'è un merch tag, ma i top G [...] sanno che esistono dei sostituti ai merch tag"

> "Se tu metti Ciao virgola nome e se non c'è il nome per qualche motivo quello spazio rimane vuoto, ma con alcuni CRM puoi metterci un'altra cosa, ad esempio Ciao virgola nome slash iscritto — quindi se c'è il nome viene 'Ciao Andrei', se non c'è il nome viene 'Ciao iscritto'"

> "Questo funziona molto meglio ed è una semplice modifica che puoi fare oggi stesso al tuo email marketing o del tuo cliente per fare più soldi"

## Meccanismo Fallback Chain (dal video)

```
Sintassi dimostrata: [campo_primario/valore_fallback]
Esempio saluto:  [nome/iscritto]  → "Ciao, Andrei"  (se nome presente)
                                  → "Ciao, Iscritto" (se nome assente)
Esempio CTA:     [nome/CTA] / [nome/Senti] / [nome/Ascolta] → stessa logica applicata
                  a un punto diverso del copy, non solo al saluto
```

## Connessioni

- [[Source_Andrei_Pascu_10_Strategie_Email_Copywriting]] — video 12 del run, tratta la posizione di {{nome}} nell'OGGETTO (character limit); questo video tratta la gestione del dato MANCANTE nel CORPO — problema diverso, stesso creator
- [[Source_Andrei_Pascu_Formule_Cliche_Copywriting]] — stesso canale, stesso registro comico/didattico breve
- [[Source_Andrei_Pascu_Email_Povero_Vs_Ricco]] — stesso formato short-form comparativo su email marketing
- [[Concept_CTR_vs_CR_Trappola_Metriche]] — altro concetto tecnico email estratto dallo stesso run
- [[Concept_Merge_Tag_Fallback_Chain]] — concetto estratto da questo video
