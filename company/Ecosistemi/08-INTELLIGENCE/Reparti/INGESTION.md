> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 08 L2 INGESTION

# Reparto L2.1 — INGESTION (= Empire Studio)

**Ecosistema:** 08-INTELLIGENCE · **Livello:** L2 · **Owner:** `int-director`
**Vincolo cardinale:** Empire Studio si ingloba **COSÌ COM'È** — non si riscrive, non si tocca internamente.
INTELLIGENCE lo *organizza* sotto di sé come servizio, qualsiasi evoluzione passa per la FORGE con eval prima/dopo.

Collega: [[08-INTELLIGENCE/ECOSISTEMA.md]] · [[08-INTELLIGENCE/BACKBONE.md]]

---

## Cosa fa

INGESTION è il motore di acquisizione della conoscenza esterna: qualsiasi link, video,
canale YouTube, sito, file o cartella passato da qualsiasi ecosistema viene **ingerito
integralmente** e archiviato in `knowledge/` e nella wiki. Nessun riassunto: contenuto
integrale (pattern #1 INTELLIGENCE: G-INTEGRAL).

Motore reale: **Empire Studio** (`SKILL & Agenti/Empire Studio Suite/empire-studio/`)
con i suoi 9 reparti interni e ~50 agenti. L'agente di contatto è `int-studio-conductor`.

**Tre linee di lavoro:**
1. **WF-INGEST-VIDEO** — video/canale YouTube: frame densi + analisi visiva Claude → knowledge + wiki
2. **WF-INGEST-WEB** — link/sito/repo/articolo: estrazione strutturata → knowledge + wiki
3. **WF-INGEST-DOC** — file/cartelle/libri: ingestione documentale (variante: book-to-skill quando target è una skill)

---

## Come si collega

| Con | Relazione |
|---|---|
| FORGE / WF-FORGE-PIPELINE | fornitore primario di materia prima: materiale ingerito → input content-forge |
| SECOND-BRAIN | ogni ingestione produce una o più pagine wiki (con cross-link e log obbligatori) |
| MEMORY (Memory Empire v3) | il router di Memory Empire decide se una richiesta va a INGESTION o ad altri reparti |
| LEARNING | i pattern di fallimento dell'ingestione vanno al ReasoningBank |
| MULTI-BUSINESS (roadmap F7) | ingestione 2 canali YouTube di riferimento per YouTube Automation |

---

## Asset (WRAPPA — non riscrivere)

| Asset | Azione |
|---|---|
| `SKILL & Agenti/Empire Studio Suite/empire-studio/` (agents, skills, strategies, runs, memory, evals, packaged) | **USA COSÌ COM'È** — esporre come servizio via `int-studio-conductor` |
| skill `book-to-skill` | **USA** (ponte INGESTION → FORGE quando il target è una skill) |

---

## Handoff contract (ingresso)

```json
{
  "from": "qualsiasi ecosistema",
  "to": "INGESTION/int-studio-conductor",
  "payload": {
    "tipo": "video | web | doc | cartella",
    "sorgente": "URL | path",
    "target_wiki": "path pagina wiki di destinazione",
    "namespace_memoria": "intelligence/"
  },
  "acceptance_criteria": [
    "Contenuto integrale (non riassunto) archiviato in knowledge/",
    "Pagina wiki creata/aggiornata con cross-link ≥ 2",
    "Entry in wiki/log.md"
  ]
}
```

---

## KPI

| Metrica | Target |
|---|---|
| Ingestioni completate senza intervento manuale | ≥ 90% |
| Contenuto archiviato integrale (G-INTEGRAL) | 100% |
| Pagine wiki generate con ≥ 2 cross-link | 100% |
| Tempo ingestione → disponibile in wiki | ≤ 24h |
