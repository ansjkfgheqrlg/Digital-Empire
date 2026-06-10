# knowledge-extractor - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Atomi troppo grossi | un atomo contiene 5 concetti | 1 concetto per atomo | atomi lunghi | spezza in atomi piu' fini |
| Riassunto invece di espansione | atomi poveri | regola no-summary | output < fonte | espandi con dettagli/esempi |
| Trace mancante | atomi senza fonte | schema obbligatorio | campo trace vuoto | riassocia al frame/segmento |
| Allucinazione | atomo non presente nella fonte | no-finto + marca + | atomo senza ancoraggio | rimuovi o marca + e verifica |
| Duplicati cross-video | stesso atomo da video diversi | dedup nel KG | atomi identici | fondi con trace multipla |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
