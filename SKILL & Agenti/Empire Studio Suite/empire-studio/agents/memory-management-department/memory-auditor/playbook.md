# memory-auditor - Playbook

## Flusso operativo
1. Controllare che esistano CP/DEC/SES per le azioni recenti.
2. Verificare che bug/errori siano nelle categorie giuste.
3. Controllare la propagazione (un update ha toccato gli stati attesi?).
4. Mantenere l'integrita' dell'INDEX e segnalare i gap.

## Esempi
- Happy: input valido -> memory-auditor produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
