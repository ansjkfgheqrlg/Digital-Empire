# Stage 2 — Deep Analysis (multi-pass, parallel)

> Stadio dell'analisi cognitiva profonda. Estrae **atomi** informativi dal sorgente pulito.

## Obiettivo

Per ogni chunk prodotto da Stage 1, applicare i pattern cognitivi P1-P9 rilevanti ed estrarre una lista di **atomi**: unità informative indivisibili con definizione canonica, evidenze, esempi, hint di collegamento.

L'analisi è **parallelizzata**: 1 istanza di A2 per chunk, in modo che sorgenti grandi non scalino linearmente nel tempo.

## Agente principale

**A2 `analyst-agent`** — N istanze in parallelo. Vedi `agents/pipeline/analyst-agent.md`.

## Pattern applicati (in questo stage)

| Pattern | Quando |
|---|---|
| **P1 — Atomic extraction** | Sempre, primo passo per ogni chunk |
| **P2 — Claim/Evidence/Example** | Per ogni atomo che è una claim |
| **P3 — Hierarchy** (hint) | Annotazioni `implied_prerequisites` |
| **P5 — Procedural decomposition** | Per atomi how-to |
| **P6 — Mental model surfacing** | Per atomi con metafore/frame impliciti |

P4, P7, P8, P9 NON sono di questo stage — sono dei builder (Stage 5).

## Input attesi

```
<workspace>/forge-run-<ts>/
├── stage-01/cleaned.md
└── stage-01/chunks.json     # uno per istanza A2
```

## Output canonici

```
<workspace>/forge-run-<ts>/stage-02/
├── atoms-chunk-001.json
├── atoms-chunk-002.json
├── ...
└── atoms-chunk-NNN.json     # uno per chunk
```

Shape di ogni file (vedi `agents/pipeline/analyst-agent.md §4` per dettagli completi):

```python
{
  "chunk_id": str,
  "atoms": [
    {"id": str, "title": str, "category": str,
     "canonical_definition": str, "extended_explanation": str,
     "source_excerpt": str, "source_offset": [int,int],
     "evidence": list, "examples_from_source": list,
     "generated_examples": list,
     "implied_prerequisites": list, "implied_mental_models": list,
     "related_concepts_hints": list,
     "confidence": float, "tags": list}
  ],
  "chunk_meta": {...}
}
```

## Modalità di esecuzione

- **Default**: parallelo. Conductor spawna N istanze A2 nello stesso turno.
- **Fallback sequenziale**: se l'ambiente ha problemi con subagenti paralleli (es. timeout aggregato), Conductor può eseguire in serie. È più lento ma sempre corretto.

## Quando questo stage si attiva

Subito dopo Stage 1, quando `chunks.json` è disponibile.

## Quando questo stage si conclude

Tutti gli N agenti A2 hanno restituito `status: ok` E hanno scritto `atoms-chunk-*.json`.

```python
def stage2_complete(workspace, chunks_count):
    files = list((workspace / "stage-02").glob("atoms-chunk-*.json"))
    return len(files) == chunks_count and all(valid_schema(f) for f in files)
```

## Failure modes specifici

| Failure | Mitigazione |
|---|---|
| 1 chunk fallisce in parallelo | Retry SOLO quel chunk (non tutti); se fallisce 2x, segnala all'utente e procedi senza |
| Subagenti A2 producono atomi con qualità molto eterogenea | Procedere; A3 (knowledge-graph) farà dedup + filtro confidence |
| Atomi a confidence <0.3 dominano | Soglia di alert; il Conductor avvisa l'utente prima di Stage 3 |
| Chunk produce 0 atomi (troppo brevi/vuoti) | OK se chunk era effettivamente vuoto, altrimenti review manuale |

## Contratto con Stage 3

Stage 3 (A3) consuma TUTTI i file `atoms-chunk-*.json`. È sensibile a:
- ID atomi univoci a livello globale dopo la deduplicazione (A3 si occupa di re-mapping)
- Schema strict (campi obbligatori)
- `source_offset` validi (devono puntare a `cleaned.md` correttamente)

## Note operative

- Con sorgenti grandi (20+ chunk), il parallelismo può saturare il context budget. Considera batch (10 chunk parallel, poi altri 10).
- Quando uno stesso concetto compare in più chunk, A2 NON cerca di unificare — produce atomi separati con `related_concepts_hints`. Sarà A3 a unificare.
