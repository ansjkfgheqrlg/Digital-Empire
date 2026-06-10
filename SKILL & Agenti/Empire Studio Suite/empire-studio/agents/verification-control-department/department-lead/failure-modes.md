# department-lead - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Verifica solo a fine | problemi scoperti tardi | checkpoint per stage | errori accumulati | verifica proattiva tra i reparti |
| Blocco eccessivo | pipeline ferma su inezie | soglie calibrate | stalli frequenti | distingui blocco vs warning |
| Escalation mancante | problema grave ignorato | regole di escalation | problema persiste | escala al Conductor |
| Report poco chiaro | Conductor non capisce l'esito | report strutturato | ambiguita' | riformula chiaro |
| Controllori non coordinati | verifiche sovrapposte/buchi | assegnazione chiara | ridondanza/gap | ridistribuisci i controlli |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
