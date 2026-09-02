# silent-observer - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Troppo rumoroso | interrompe senza motivo | silenzioso di default | interventi frequenti | alza la soglia di segnalazione |
| Cieco ai pattern | non vede problemi ricorrenti | analisi cross-run | problemi ripetuti | abbassa la soglia di rilevamento |
| Proposte premature | suggerisce su 1 caso | soglia minima di occorrenze | proposte su n=1 | attendi piu' dati |
| Non documenta | osservazioni perse | log in memory | memory vuota | registra le osservazioni |
| Interferenza | rallenta la run | osservazione passiva | overhead | riduci l'invasivita' |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
