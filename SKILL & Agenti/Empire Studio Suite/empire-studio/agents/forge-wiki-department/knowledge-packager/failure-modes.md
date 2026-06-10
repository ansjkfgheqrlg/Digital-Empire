# knowledge-packager - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Report incompleto | mancano percorsi wiki | raccogli da run state | sezioni vuote | ricostruisci dai file run |
| Trace non leggibili | trace tecniche grezze | formato umano | trace criptiche | riformatta in modo comprensibile |
| Report troppo lungo | muro di testo | struttura a sezioni | lunghezza eccessiva | sintesi + dettaglio in appendice |
| Link rotti | percorsi wiki errati | verifica esistenza file | path inesistenti | correggi i percorsi |
| Manca update proposals | report senza proposte | includi sempre la sezione | sezione assente | recupera da update-proposer |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
