# Regole — Workflow First

1. **Ogni app parte da un workflow.** Prima di wireframe, schema dati, endpoint o codice, WF deve mappare almeno: trigger, attore, obiettivo, passi, decisioni, dati usati/creati, errori, uscita e criterio di successo.
2. Il workflow deve descrivere l'esperienza utente e il processo di business, non soltanto le schermate.
3. Ogni requisito RF deve collegarsi a uno o più workflow; ogni schermata, API e tabella deve dichiarare il workflow che supporta.
4. Per ogni workflow critico definire happy path, empty state, errore recuperabile, errore bloccante, autorizzazione e audit/evento quando pertinente.
5. Un workflow non approvato non può essere implementato. Cambiamenti di flusso richiedono aggiornamento, test di regressione e gate SUP.
6. Il workflow è valido solo se ha un owner di business, un criterio di successo misurabile e un punto di inizio/fine non ambiguo.

## Template WF

```markdown
# WF-[ID] — [nome]
- Stato: proposta | approvato | deprecato
- Owner business: [ruolo]
- Priorità: Must / Should / Could
- Trigger: [evento iniziale]
- Attore/i: [ruoli]
- Obiettivo: [risultato per l'utente/business]
- Precondizioni: [condizioni]
- Dati: [input, output, PII/classificazione]
- Success metric: [metrica]

## Flusso
1. [passo + responsabile]
2. [decisione / ramo]
3. [risultato]

## Varianti e failure modes
- Empty/loading:
- Errore recuperabile:
- Errore bloccante:
- Autorizzazioni:
- Audit/notifiche:

## Tracciabilità
- RF: [RF-ID]
- UI: [screen/component]
- API: [endpoint/event]
- Dati: [entità]
- Test: [test-ID]
```
