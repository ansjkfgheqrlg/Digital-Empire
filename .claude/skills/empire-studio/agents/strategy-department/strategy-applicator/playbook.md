# strategy-applicator - Playbook

## Flusso operativo
1. Leggere il Manifest e tradurlo in vincoli operativi per ogni reparto.
2. Iniettare le regole (es. 'frame su ogni capitolo', 'stile wiki X') negli handoff.
3. Monitorare in tempo reale l'aderenza durante l'esecuzione.
4. Registrare in memory le deviazioni rispetto al Manifest.

## Esempi
- Happy: input valido -> strategy-applicator produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
