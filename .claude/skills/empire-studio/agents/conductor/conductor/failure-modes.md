# conductor - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Salta memory bootstrap | run senza CP-000 | checklist Stage 0 | nessun checkpoint run | bootstrap retroattivo + nota |
| Instradamento errato | reparto sbagliato per l'input | classificazione input robusta | reparto non pertinente | re-instrada al reparto giusto |
| Output grezzo all'utente | l'utente vede JSON/log interni | sempre filtra/riformula | messaggio tecnico crudo | riassumi in linguaggio chiaro |
| Dichiara 'fatto' senza verifica | claim non confermato | gate Verification+validator | nessun pass di verifica | esegui verifica prima di comunicare |
| Strategia non applicata | pipeline generica | Manifest obbligatorio | nessun manifest nello stato | richiama Strategy Coordinator |
| Run bloccata | stage fermo | timeout + escalation | nessun avanzamento | registra in errors, ripiana o avvisa l'utente |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
