> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 08 · Reparto L2 INGESTION · WF-INGEST-WEB

# T-INGEST-WEB — Ingestione Link / Sito / Repository

> Funzione L4 · Reparto: L2 INGESTION (Empire Studio) · Ecosistema: 08-INTELLIGENCE
> Riferimento ecosistema: `company/Ecosistemi/08-INTELLIGENCE/ECOSISTEMA.md`

---

## Scopo

Estrarre e archiviare INTEGRALMENTE il contenuto di URL web (articoli, pagine, repository
GitHub, thread social) dentro `knowledge/` e `second-brain-vault/wiki/`. Empire Studio
gestisce i 50 agenti interni — questa funzione espone il punto di ingresso unificato.

---

## Input

```json
{
  "source": "URL | lista URL | path repo",
  "tipo": "articolo | sito | repo | thread",
  "target_ecosistema": "08-INTELLIGENCE | 01-AGENCY | ...",
  "depth": 1
}
```

## Output

```json
{
  "knowledge_path": "knowledge/<slug>/",
  "wiki_page": "second-brain-vault/wiki/sources/<slug>.md",
  "entita_estratte": ["competitor X", "framework Y"],
  "log_entry": "wiki/log.md aggiornato"
}
```

---

## Processo step-by-step

1. **Fetch contenuto** — estrazione testo integrale (no paywall bypass; segnalare se accesso negato).
2. **Estrazione entità** — persone, aziende, tool, metriche: marcati come entità candidate per wiki/entities/.
3. **Archivio knowledge** — `knowledge/<slug>/raw.md` + `knowledge/<slug>/structured.json`.
4. **Indicizzazione AgentDB** — `memory_store` namespace `intelligence/web` per recall semantico futuro.
5. **Creazione/aggiornamento pagina wiki** — se esiste una pagina per il dominio, aggiunge sezione; altrimenti crea nuova Source.
6. **Cross-link automatici** — collega alle entità/concept wiki già esistenti (≥2 link obbligatori).
7. **Log** — entry in `wiki/log.md` con data, URL, n. chunk, agente chiamante.

---

## Regole critiche

- **G-INTEGRAL**: mai riassumere; archivio testo integrale nella knowledge/.
- **G-LOG**: log entry obbligatoria dopo ogni ingestione.
- **G-LINK**: nuova pagina wiki → ≥2-3 cross-link a pagine esistenti.
- Se il sito è multi-pagina (sito intero): piano batch con limite pagine e approvazione int-director.
- Repository GitHub: README + file principali + CHANGELOG archiviati; codice solo se esplicitamente richiesto.

---

## Connessioni

- Agente gestore: `int-studio-conductor`
- Skill di supporto: `book-to-skill` (variante per documenti lunghi → skill)
- Cross-link: [[T-INGEST-VIDEO]] · [[T-RESEARCH]] · [[08-INTELLIGENCE/ECOSISTEMA.md]]
- Output verso: `int-librarian` per garden check cross-link
