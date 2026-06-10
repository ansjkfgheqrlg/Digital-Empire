# compliance-auditor - Playbook

## Flusso operativo
1. Eseguire validator.py e interpretarne l'esito.
2. Cercare segnali di uso di API/servizi a pagamento (vietati).
3. Verificare nomi file Windows-safe e assenza di stub.
4. Controllare l'aderenza al Strategy Manifest (con strategy-controller).

## Esempi
- Happy: input valido -> compliance-auditor produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
