# decision-codifier - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Decisione non registrata | scelta senza ADR | rileva le decisioni | scelta non tracciata | registra ADR retroattivo |
| ADR incompleto | manca razionale/alternative | template ADR | sezioni vuote | completa l'ADR |
| Troppi ADR banali | rumore | soglia di rilevanza | ADR su inezie | registra solo le scelte vere |
| Non collegato | ADR isolato | link a CP/stati | nessun collegamento | aggiungi i link |
| Trace mancante | ADR senza fonte | trace richiesta | campo vuoto | aggiungi trace |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
