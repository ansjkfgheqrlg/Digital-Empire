# visual-verifier - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Allucinazione non rilevata | descrizione finta passa | confronto frame-descrizione | claim non ancorato | fail + re-watch |
| Frame falsi accettati | PNG identici/neri ok | check size+varianza | frame uguali | richiedi nuova estrazione |
| Genericita' tollerata | descrizioni vaghe passano | soglia di specificita' | frasi generiche | richiedi dettaglio |
| Falsi negativi | blocca descrizioni valide | criteri equi | blocchi a torto | ritara i criteri |
| Trace non verificata | atomi senza frame | controlla la trace | trace assente | richiedi trace |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
