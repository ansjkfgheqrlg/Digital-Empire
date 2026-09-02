# department-lead - Playbook

## Flusso operativo
1. Ricevere da Processing&Vision il pacchetto analizzato (analysis + atoms + kg).
2. Far invocare content-forge (--target=wiki) tramite content-forge-invoker.
3. Far scrivere le note forgiate nella wiki (wiki-writer) e aggiornare log.md.
4. Far generare le update proposals (update-proposer) per i workflow esistenti.
5. Confermare al Conductor il deliverable finale con i percorsi wiki.

## Esempi
- Happy: input valido -> department-lead produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
