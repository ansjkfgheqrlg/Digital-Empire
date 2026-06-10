# session-archiver - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Sessione non archiviata | run non ricostruibile | SES per run | nessun SES | archivia retroattivamente |
| Log troppo grezzo | rumore | log significativo | SES illeggibile | sintetizza il log |
| Non collegato | SES isolato | link a CP/DEC | nessun collegamento | collega |
| Short-term perso | stato run sparito | salva lo stato | stato assente | ricostruisci dai file run |
| Privacy/segreti | dati sensibili nel log | filtra i segreti | credenziali nel SES | rimuovi i segreti |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
