# workflow-deep-analyzer - Playbook

## Flusso operativo
1. Leggere il report/descrizione nei minimi dettagli (sola lettura).
2. Ricostruire l'architettura e le decisioni, spiegando il 'perche''.
3. Valutare come e quanto bene funziona (forza, debolezza, anti-pattern).
4. Confrontare con i principi noti (master-build, content-forge) e annotare gli scostamenti.

## Esempi
- Happy: input valido -> workflow-deep-analyzer produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
