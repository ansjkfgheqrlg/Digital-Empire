# department-lead - Playbook

## Flusso operativo
1. Ricevere il path al report/repo/workflow dal Conductor.
2. Coordinare workflow-deep-analyzer e repo-deep-study per l'analisi profonda.
3. Assicurare la regola di sola lettura (nessuna modifica all'originale).
4. Far estrarre gli atomi (project-knowledge-extractor) con trace a file:riga.
5. Far confrontare con i workflow esistenti (workload-comparator) per update proposals.

## Esempi
- Happy: input valido -> department-lead produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
