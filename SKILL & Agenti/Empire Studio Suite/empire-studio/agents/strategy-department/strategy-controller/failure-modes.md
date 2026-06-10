# strategy-controller - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Audit superficiale | violazioni non viste | check puntuali per regola | qualita' bassa a valle | audit piu' rigoroso |
| Nessun log | audit non tracciato | log obbligatorio | memory-auditor | registra l'audit |
| Falsi positivi | blocca a torto | soglie calibrate | reparti corretti bloccati | ritara le soglie |
| Niente escalation | violazione ignorata | escalation su grave | problema persiste | escala a coordinator/improver |
| Manifest non letto | audit a vuoto | carica il Manifest | regole assenti | richiedi il Manifest |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
