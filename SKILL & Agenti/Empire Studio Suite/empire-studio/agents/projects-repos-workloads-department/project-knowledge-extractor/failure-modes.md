# project-knowledge-extractor - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Atomi vaghi | concetti generici | 1 concetto specifico per atomo | atomi non azionabili | rendi specifici e concreti |
| Trace assente | atomi senza file | trace obbligatoria | trace vuota | riassocia a file:riga |
| Giudizi non marcati | opinioni come fatti | marca + le inferenze | valutazioni senza fonte | marca + e motiva |
| Riassunto | atomi poveri | espandi non comprimi | output<fonte | espandi con dettagli |
| Duplicati | stesso atomo ripetuto | dedup | atomi identici | fondi |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
