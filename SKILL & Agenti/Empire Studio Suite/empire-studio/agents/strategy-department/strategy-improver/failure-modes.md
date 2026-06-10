# strategy-improver - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Proposte senza dati | miglioramenti inventati | solo da memory reale | nessuna fonte dati | rifiuta, richiedi dati |
| Non versiona | modifica in-place | sempre nuova versione | nessun vN | crea versione esplicita |
| Miglioramento non misurabile | claim vago | metrica attesa (es +15% coverage) | nessuna metrica | definisci la metrica |
| Regressione | nuova versione peggiore | confronto pre/post | metriche calano | rollback alla versione precedente |
| Dati insufficienti | poche run | soglia minima run | <3 run | attendi piu' dati |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
