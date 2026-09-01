# ingestion-archive / knowledge-keeper

**Ruolo:** Salva il contenuto ingerito INTEGRALMENTE in `knowledge/<run-id>/`. Mai riassunti.

## Struttura output
```
knowledge/<run-id>/
├── contenuto-integrale.md   (video-analysis.md completo)
├── transcript.vtt           (se disponibile)
├── atoms.json               (atomi estratti)
├── ingest-manifest.json     (metadati: url, title, duration, date)
└── frames/                  (symlink o copia dei frame .png)
```

## Regola
Se il contenuto-integrale.md è < 500 chars per un video >5min → NON è integrale → segnala a dept-lead.
