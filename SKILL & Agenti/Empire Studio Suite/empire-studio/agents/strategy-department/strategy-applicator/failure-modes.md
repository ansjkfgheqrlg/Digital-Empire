# strategy-applicator - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Vincoli non iniettati | reparti ignorano la strategia | handoff include sempre le regole | output non conforme | re-inietta i vincoli |
| Vincoli troppo rigidi | reparti bloccati | regole come guida, non gabbia | stallo | ammorbidisci dove sensato |
| Deviazioni non loggate | nessun audit trail | log obbligatorio | memory vuota | registra retroattivamente |
| Conflitto tra regole | regole incompatibili | valida il Manifest prima | contraddizione | escala a coordinator |
| Manifest assente | niente da applicare | richiedi il Manifest | stato vuoto | chiedi al coordinator |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
