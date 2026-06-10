# real-tester - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Test banale | passa senza valore | task rappresentativo | test triviale | definisci un task reale |
| Lacune non viste | conoscenza inutilizzabile passa | prova end-to-end | task fallisce | segnala lacune, richiedi integrazione |
| Falso fallimento | boccia conoscenza valida | task equo | fallimenti ingiusti | ritara il task |
| Non ripetibile | esito casuale | task deterministico | varianza | standardizza il test |
| Non loggato | esito perso | log obbligatorio | memory vuota | registra l'esito |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
