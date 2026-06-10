# department-lead - Playbook

## Flusso operativo
1. Inserire checkpoint di verifica tra i reparti.
2. Coordinare visual-verifier, coverage-controller, compliance-auditor, real-tester.
3. Bloccare l'handoff se una verifica fallisce; aprire ticket di errore.
4. Produrre report di verifica per il Conductor.

## Esempi
- Happy: input valido -> department-lead produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
