# content-forge-invoker - Playbook

## Flusso operativo
1. Assemblare runs/<run-id>/forge-input/ (analysis + atoms + transcript + frame refs).
2. Invocare la skill content-forge con --target=wiki e il nome corretto.
3. Verificare che venga prodotto l'MKD e le note atomiche con trace.
4. Consegnare le note grezze al wiki-writer.

## Esempi
- Happy: input valido -> content-forge-invoker produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
