> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 08 · Reparto L2 INGESTION · WF-INGEST-VIDEO

# T-INGEST-VIDEO — Ingestione Video/Canale

> Funzione L4 · Reparto: L2 INGESTION (Empire Studio) · Ecosistema: 08-INTELLIGENCE
> Riferimento ecosistema: `company/Ecosistemi/08-INTELLIGENCE/ECOSISTEMA.md`

---

## Scopo

Ingerire un video o un intero canale YouTube/video: estrae frame reali con visione Claude,
trascrive audio, indicizza ogni chunk in knowledge/ e produce la pagina wiki corrispondente.
Empire Studio è il motore sottostante — questa funzione lo invoca; NON lo riscrive.

---

## Input

```json
{
  "source": "URL video | URL canale | path file locale",
  "tipo": "video | canale | clip",
  "target_ecosistema": "08-INTELLIGENCE | 02-INFO | ...",
  "note_contestuali": "focus su X (facoltativo)"
}
```

## Output

```json
{
  "knowledge_path": "knowledge/<slug>/",
  "wiki_page": "second-brain-vault/wiki/sources/<slug>.md",
  "chunks_n": 42,
  "log_entry": "wiki/log.md aggiornato"
}
```

---

## Processo step-by-step

1. **Ricezione URL** — verifica accessibilità e tipo (video singolo vs canale).
2. **Estrazione frame** — Empire Studio campiona frame a intervalli regolari; Claude Vision descrive ogni frame.
3. **Trascrizione audio** — testo integrale + timing (mai solo sommario: archivio INTEGRALE — gate G-INTEGRAL).
4. **Chunking semantico** — suddivisione per argomento; ogni chunk → `knowledge/<slug>/chunk-NNN.md`.
5. **Indicizzazione AgentDB** — `memory_store` namespace `intelligence/video` per recall semantico.
6. **Creazione pagina wiki** — template Source con ≥2 cross-link; entry in `wiki/log.md`.
7. **Notifica committente** — path knowledge/ e ID wiki restituiti via handoff.

---

## Regole critiche

- **G-INTEGRAL**: contenuto archiviato INTEGRALE, mai solo riassunto.
- **G-LOG**: ogni operazione loggata in `wiki/log.md`.
- **G-LINK**: ≥2-3 cross-link nella pagina wiki prodotta.
- Se il video è >2h → dividere in sessioni di ingestione separate con checkpoint CP intermedi.
- Canale con >20 video → piano batch approvato da int-director prima di avviare.

---

## Connessioni

- Agente gestore: `int-studio-conductor`
- Motore: Empire Studio (`SKILL & Agenti/Empire Studio Suite/`)
- Wiki: `second-brain-vault/wiki/sources/`
- Cross-link: [[T-INGEST-WEB]] · [[T-WIKI-CONTEXT]] · [[08-INTELLIGENCE/ECOSISTEMA.md]]
