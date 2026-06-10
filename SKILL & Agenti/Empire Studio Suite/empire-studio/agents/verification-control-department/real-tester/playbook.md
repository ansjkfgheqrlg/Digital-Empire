# real-tester - Playbook

## Flusso operativo
1. Definire un mini-task che usa la conoscenza appena ingerita.
2. Verificare se le note wiki bastano a svolgere quel task.
3. Segnalare lacune pratiche (conoscenza presente ma non azionabile).
4. Dare il via libera finale solo se il real test passa.

## Esempi
- Happy: input valido -> real-tester produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
