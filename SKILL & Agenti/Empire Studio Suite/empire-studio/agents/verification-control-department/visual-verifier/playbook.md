# visual-verifier - Playbook

## Flusso operativo
1. Verificare che i PNG dei frame esistano e non siano vuoti/neri.
2. Confrontare le descrizioni del video-watcher con i frame (anti-allucinazione).
3. Segnalare descrizioni generiche ('mostra una UI') come insufficienti.
4. Bloccare il forge se la visione e' finta o assente.

## Esempi
- Happy: input valido -> visual-verifier produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
