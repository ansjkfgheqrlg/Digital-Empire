> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A5 + sez. 6 + sez. 8 (Gate Bibbia)

# WF-COPY-OUTREACH — Refresh Template Copy Outreach

> Workflow L3 di A5-COPYWRITING-INTERNO · Triggered: KPI in calo / Gate Bibbia in serie
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A5

## Cosa è

Workflow periodico per il **refresh dei template** dei 3 canali outreach (email, LinkedIn, Instagram).
Non produce copy da zero (quelli grandi vengono da 04 MARKETING via `HC-MK-AG-01`) — produce
varianti APSOC ancorate ai dati reali di performance di A2 e le valida con il Gate Bibbia.

## Flusso

```
TRIGGER: A2 segnala reply rate in calo (baseline 2 cicli) OPPURE
         Gate Bibbia boccia in serie lo stesso template OPPURE
         A5-COORD pianifica refresh periodico (cadenza definita con dati)

INPUT: {canale, template_attuale, reply_rate_storico, obiezioni_ricorrenti, dati_nicchia}

[T-apsoc-writer] analizza dati → produce 2-3 varianti APSOC per il canale
  Struttura APSOC:
    A = hook che cattura il problema specifico del target
    P = descrizione del problema con impatto quantificato (dati reali da A1/A3)
    S = soluzione (Outreach Factory / Content Factory / Second Brain) senza promesse inventate
    O = risposta alla 1 obiezione più comune (dalla libreria T-objection-handler)
    C = CTA univoca: presentazione-empire.vercel.app

[T-objection-handler] verifica che le varianti usino solo risposte con prove reali
  → se un'obiezione non ha risposta verificata in libreria → non inclusa

[T-copy-qa] Gate Bibbia su ogni variante (bibbia_team.py — 3 checker):
  → PASS: variante approvata per rollout
  → FAIL: note specifiche → rework [T-apsoc-writer] → nuovo ciclo

ROLLOUT GRADUALE:
  Variante nuova: test su 10% del batch → confronto reply rate dopo 3 run
  → Se meglio: rollout completo → template sostituito in agency/outreach
  → Se peggio: rollout annullato → vecchio template mantenuto + pattern in agency/reasoning
```

## I/O

| | Dettaglio |
|---|---|
| **Input** | dati performance da `agency/outreach`, obiezioni da `agency/conversations` (anonimizzate), brief da A2/A5-COORD |
| **Output** | template aggiornati in `agency/outreach`; esito rollout loggato; pattern in `agency/reasoning` se variante peggiora |

## Regole Gate Bibbia (gate condiviso A2-A5 — pattern #6)

I 3 checker di `bibbia_team.py` verificano su ogni template:
1. Struttura APSOC rispettata (hook → problema → soluzione → obiezione → CTA)
2. CTA = `presentazione-empire.vercel.app` (invariata)
3. Nessuna promessa non provata (Mandato Empire: zero claim senza prova reale)
4. Lunghezza e tono conformi al canale (email vs LinkedIn vs DM)
5. Firma DE corretta

Un solo checker boccia → template NON esce.

## Failure

| Evento | Risposta |
|---|---|
| Gate Bibbia boccia 3 cicli | escalation a AG-A5-COORD → brief difettoso? Richiesta consulto a 04 MARKETING |
| Nessun dato di performance disponibile | refresh NON parte senza dati reali; segnalare gap a 09 OPS |
| Rollout peggiora KPI | rollback immediato al template precedente; pattern in agency/reasoning |

## Connessioni

- [`../Reparti/A5-Copywriting-Interno/`](../Reparti/A5-Copywriting-Interno/) — reparto owner
- [`../Funzioni/T-apsoc-writer/`](../Funzioni/T-apsoc-writer/) · [`T-objection-handler/`](../Funzioni/T-objection-handler/) · [`T-copy-qa/`](../Funzioni/T-copy-qa/)
- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/) (fornitore dati; cliente template aggiornati)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
