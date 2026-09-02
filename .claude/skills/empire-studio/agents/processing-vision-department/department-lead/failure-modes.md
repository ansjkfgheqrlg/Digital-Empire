# department-lead - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Run senza video (solo audio/web) | niente da visionare | rileva il tipo di contenuto | ingest kind != video | salta i frame, vai diretto agli atomi testuali |
| Sovraccarico (molti video in coda) | latenza alta | coda con priorita' dal lead | workflow-state lungo | processa in batch, prioritizza per strategia |
| Visione incompleta | frame non guardati tutti | checklist per frame nel video-watcher | frames_seen < estratti | ripianifica i frame mancanti |
| Atomi senza trace | knowledge-extractor produce atomi nudi | schema atoms con trace obbligatoria | atomi con trace vuota | rimanda a knowledge-extractor con il manifest frame |
| Handoff disallineato col Forge | il Forge non trova i file | percorsi standard nella run | Forge segnala file mancanti | consolida i percorsi e ripassa l'handoff |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
