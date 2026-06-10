# department-lead - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Modifica accidentale | file originale cambiato | solo lettura, mai write sull'originale | diff sull'originale | ripristina, lavora su copia/indice in sola lettura |
| Analisi superficiale | manca il 'perche'' | richiedi decisioni+rationale | analisi generica | approfondisci architettura e scelte |
| Repo enorme | troppi file | prioritizza per rilevanza | migliaia di file | campiona i file chiave, segnala scope |
| Trace mancante | atomi senza file:riga | trace obbligatoria | trace vuota | riassocia a file/sezione |
| Binari/asset | file non testuali | salta binari | estensioni binarie | analizza solo testo/codice/doc |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
