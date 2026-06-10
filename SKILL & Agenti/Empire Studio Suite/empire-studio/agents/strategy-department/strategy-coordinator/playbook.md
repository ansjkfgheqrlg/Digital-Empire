# strategy-coordinator - Playbook

## Flusso operativo
1. Leggere il STRATEGY-REGISTRY e le strategie specifiche disponibili.
2. Consultare department-strategist e content-type-strategist per i casi complessi.
3. Selezionare la combinazione: strategia di reparto + tipo contenuto + stile wiki.
4. Generare il Strategy Manifest (generate_strategy_manifest.py) e salvarlo in memory.

## Esempi
- Happy: input valido -> strategy-coordinator produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
