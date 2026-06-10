# update-propagator - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Propagazione mancante | stati incoerenti | regole di propagazione | stati divergenti | propaga |
| Propagazione eccessiva | tocca stati irrilevanti | ambito mirato | modifiche superflue | limita l'ambito |
| Loop di update | propagazione ciclica | guard anti-loop | ripetizioni | interrompi il ciclo |
| Non registrata | update non tracciato | log in updates/ | memory vuota | registra |
| Conflitto | update contraddittori | risoluzione conflitti | incoerenza | concilia |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
