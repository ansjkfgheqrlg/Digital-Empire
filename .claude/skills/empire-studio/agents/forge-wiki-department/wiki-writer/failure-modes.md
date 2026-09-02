# wiki-writer - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Wiki non trovata | path second-brain-vault assente | auto-rilevamento risalendo | find_wiki None | chiedi --wiki esplicito |
| Subdir errata | nota in cartella sbagliata | mappa tipo->subdir | nota fuori posto | sposta nella subdir corretta |
| Sovrascrittura | perdita nota esistente | check esistenza + versioning | file gia' presente | rinomina o fondi |
| Log non aggiornato | manca riga INGEST | update_log sempre | log invariato | appendi la riga mancante |
| Front-matter rotto | YAML non valido | template front-matter | parser YAML fallisce | correggi il front-matter |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
