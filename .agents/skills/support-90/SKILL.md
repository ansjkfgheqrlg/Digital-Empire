---
name: support-90
description: "Gestione supporto 90 giorni post-delivery. Usa questa skill per: aprire/chiudere ticket, triage, SLA, check proattivi settimanali, report di chiusura a 90gg. Obiettivo: risolvere e ridurre la dipendenza, non aumentarla."
---

# Skill: support-90

> Reparto: A4-DELIVERY | Team: T-support-triage, WF-SUPPORTO-90GG | Tier: haiku (triage) / sonnet (fix)

## Scopo

Gestire il supporto 90 giorni post-delivery rispettando la promessa commerciale
e riducendo progressivamente il numero di ticket (il cliente diventa sempre piu' autonomo).

## Lifecycle supporto

```
Gate Delivery PASS -> supporto_started_at
  |
  +--> Check proattivo settimanale (ogni 7gg)
  |
  +--> Ticket inbound -> triage -> fix/risposta -> chiusura
  |
  +--> 90gg scaduti -> Review finale -> Chiusura ufficiale
```

## Triage ticket

| Tipo | SLA risposta | SLA risoluzione | Note |
|---|---|---|---|
| Bug critico (sistema fermo) | 4h | 24h | Priorita' assoluta |
| Bug non critico | 24h | 72h | |
| Domanda operativa | 24h | 48h | Risposta nel runbook; aggiorna FAQ |
| Fuori scope | 24h | N/A | Informa cliente; offri upsell se applicabile |

"Fuori scope" include: nuove funzionalita', integrazioni non nel contratto, domande su altri sistemi.

## Check proattivo settimanale (output)

```
Check settimanale — [nome_azienda] — settimana [N]/13

Sistema operativo: SI / NO
Log ultimi 7gg: [summary breve]
Ticket aperti: [N]
Anomalie rilevate: [lista o "nessuna"]
Prossima azione: [o "nessuna"]
```

## Report chiusura 90gg

Da produrre quando `supporto_90gg_ends_at` e' raggiunto:

- Riepilogo delivery (cosa e' stato consegnato)
- Ticket totali aperti vs risolti in SLA
- Metriche di utilizzo (se disponibili, solo prove reali)
- Livello autonomia cliente (1-5: 5 = usa il sistema senza aiuto)
- Proposta upsell (se livello_autonomia >= 4 e segnale positivo -> upsell-mapper)
- Storico inviato ad A6 via HC-A4-A6-testimonianza

## Regole anti-dipendenza

- NON risolvere cio' che il cliente potrebbe risolvere da solo con il runbook
- Ogni risposta a "domanda operativa" aggiorna la FAQ del cliente
- Se lo stesso problema si ripresenta 2 volte: aggiorna runbook (causa radicale, non sintomo)
- Upsell SOLO a 90gg + segnale positivo: mai durante il supporto attivo

## Connessioni

- `company/01-agency/A4-DELIVERY/BACKBONE.md`
- Skill `client-handover` — il runbook e' la base per le risposte
- Skill `upsell-mapper` — attivata a fine supporto se segnale positivo
- `company/01-agency/A4-DELIVERY/BACKBONE.md` — agency/delivery namespace
