# strategy-coordinator - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Strategia generica | Manifest 'default' | consulta sempre gli specialisti | controller segnala genericita' | riscegli con specialisti |
| Manifest non salvato | nessun file in strategy-applications | salvataggio obbligatorio | memory-auditor | salva retroattivamente + CP |
| Tipo contenuto ignorato | design trattato come marketing | content-type-strategist obbligatorio | coverage visiva bassa | ri-genera Manifest |
| Input ambiguo | scelta incerta | chiedi chiarimento al Conductor | match multiplo | richiedi disambiguazione |
| Registry non aggiornato | strategia mancante | meta-strategy-manager mantiene il registry | nessuna strategia adatta | usa la piu' vicina + segnala gap |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
