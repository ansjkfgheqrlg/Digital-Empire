# repo-deep-study - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Si perde nei file | analisi dispersiva | prioritizza entrypoint/README/config | nessun filo conduttore | parti dall'architettura di alto livello |
| Binari/vendored | rumore da node_modules/.git | ignora cartelle note | file irrilevanti | escludi vendored/binari |
| Modifica accidentale | repo cambiata | sola lettura | diff/git status | ripristina |
| Linguaggio sconosciuto | codice non interpretabile | analizza struttura+commenti | sintassi ignota | descrivi a livello strutturale |
| Trace mancante | osservazioni senza file | trace obbligatoria | trace vuota | ancora a file:riga |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
