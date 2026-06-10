# strategy-improver - Playbook

## Flusso operativo
1. Analizzare i dati reali in memory (esiti, coverage, deviazioni, bug).
2. Individuare debolezze ricorrenti di una strategia.
3. Proporre versioni migliori (v1.1, v2.0) con razionale basato sui dati.
4. Salvare le proposte in strategy-versions e notificare il meta-strategy-manager.

## Esempi
- Happy: input valido -> strategy-improver produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
