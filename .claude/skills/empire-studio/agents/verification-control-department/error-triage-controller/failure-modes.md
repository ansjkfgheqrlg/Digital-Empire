# error-triage-controller - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Errori non classificati | caos di segnalazioni | schema di triage | errori sparsi | classifica per gravita' |
| Priorita' errata | blocco ignorato | regole di priorita' | problema critico in coda | ripriorizza |
| Recovery mancante | errore non risolto | assegnazione owner | errore persiste | riassegna/escala |
| Doppia gestione | stesso errore due volte | dedup errori | duplicati | unifica |
| Non loggato | nessuna traccia errore | registra sempre | memory vuota | registra con bug-error-tracker |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
