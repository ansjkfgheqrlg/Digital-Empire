# update-propagator - Playbook

## Flusso operativo
1. Rilevare quando un aggiornamento ha impatti su altri stati.
2. Propagare le modifiche a workflow-state/knowledge-state/agent-state.
3. Registrare la propagazione in memory/updates/.
4. Garantire la coerenza (nessuno stato divergente).

## Esempi
- Happy: input valido -> update-propagator produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
