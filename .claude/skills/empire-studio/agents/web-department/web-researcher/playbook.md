# web-researcher - Playbook

## Flusso operativo
1. Formulare ricerche efficaci per il focus (operatori, query multiple).
2. Navigare i risultati con Playwright e raccogliere candidati URL.
3. Valutare autorevolezza/pertinenza prima di approfondire.
4. Produrre sources.json con URL + motivo di selezione.

## Esempi
- Happy: input valido -> web-researcher produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
