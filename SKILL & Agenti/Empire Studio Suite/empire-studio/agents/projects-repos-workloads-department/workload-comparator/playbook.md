# workload-comparator - Playbook

## Flusso operativo
1. Confrontare gli atomi del progetto con workflow-state/knowledge-state esistenti.
2. Individuare pattern del progetto applicabili ai workflow dell'utente.
3. Proporre update concreti (cosa cambiare, dove) con trace al progetto studiato.
4. Non modificare nulla: solo proposte (cross-dept).

## Esempi
- Happy: input valido -> workload-comparator produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
