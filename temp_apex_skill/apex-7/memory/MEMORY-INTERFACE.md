# MEMORY INTERFACE — 6 Operazioni Canoniche

> Ogni agente usa SOLO queste operazioni per interagire con la memoria. **Mai accesso diretto.**

---

## OPERAZIONE 1: MEMORY.RECALL(context, max_results)

```
Cerca in tutti i layer ciò che è rilevante per il context fornito.
Ritorna i top max_results ordinati per:
  relevance_score * confidence * recency_weight

USO: Tutti gli agenti, all'inizio di ogni task
LAYER: Tutti (Working Memory + Decision Log + Strategy Store + Snapshots + Knowledge)
```

### Parametri
| Param | Tipo | Default | Descrizione |
|---|---|---|---|
| `context` | string | required | Query di ricerca semantica |
| `max_results` | integer | 5 | Numero massimo risultati |

### Response Schema
```json
{
  "results": [
    {
      "layer": "working_memory | decision_log | strategy_store | snapshots | knowledge",
      "record_id": "WM-sess-xxx | DEC-xxx | STR-xxx | SNAP-xxx | LL-xxx",
      "content": "...",
      "relevance_score": 0.95,
      "confidence": 0.87,
      "recency_weight": 0.92,
      "composite_score": 0.91
    }
  ],
  "total_found": 12,
  "search_depth": "full"
}
```

---

## OPERAZIONE 2: MEMORY.DECISION_LOOKUP(description)

```
Cerca nel Decision Log decisioni simili.
Ritorna decisioni con similarity > 0.75 con il loro esito reale.

USO: PLANNER e ORCHESTRATOR prima di decidere
LAYER: Decision Log (Layer 2)
```

### Parametri
| Param | Tipo | Default | Descrizione |
|---|---|---|---|
| `description` | string | required | Descrizione della decisione da cercare |
| `min_similarity` | float | 0.75 | Soglia minima similarità |

### Response Schema
```json
{
  "matches": [
    {
      "decision_id": "DEC-xxx",
      "decision": "...",
      "reasoning": "...",
      "actual_outcome": "...",
      "outcome_score": 0.92,
      "similarity": 0.88
    }
  ],
  "recommendation": "Basato su 3 decisioni simili con outcome positivo, suggerisco di procedere con..."
}
```

---

## OPERAZIONE 3: MEMORY.STRATEGY_FETCH(problem, constraints)

```
Cerca nel Strategy Store la strategia migliore per il tipo di problema,
rispettando i constraints.

USO: PLANNER all'inizio, META AGENT per evoluzioni
LAYER: Strategy Store (Layer 3)
```

### Parametri
| Param | Tipo | Default | Descrizione |
|---|---|---|---|
| `problem` | string | required | Tipo di problema da risolvere |
| `constraints` | object | {} | Vincoli da rispettare |

### Strategy Ranking
```
rank = success_rate * 0.5 + times_used_normalized * 0.2 + avg_quality_improvement * 0.3
```

---

## OPERAZIONE 4: MEMORY.WRITE(layer, content, author, importance)

```
Scrive un record in un layer specifico.
Aggiunge automaticamente tutti i metadata.
Check duplicati (similarity > 0.95 → skip).

USO: Tutti gli agenti, dopo ogni output significativo
```

### Parametri
| Param | Tipo | Default | Descrizione |
|---|---|---|---|
| `layer` | enum | required | `working_memory`, `decision_log`, `strategy_store`, `snapshots`, `knowledge` |
| `content` | object | required | Contenuto da salvare (schema varia per layer) |
| `author` | string | required | Agente che scrive |
| `importance` | float | 0.5 | Importanza del record (0.0-1.0) |

---

## OPERAZIONE 5: MEMORY.UPDATE(record_id, updates)

```
Aggiorna un record esistente.
Crea versione (version += 1).
Mantiene storico delle versioni.

USO: ORCHESTRATOR per aggiornare esiti decisioni, META AGENT per evoluzioni
```

---

## OPERAZIONE 6: MEMORY.ARCHIVE(record_id, reason, superseded_by)

```
Marca un record come ARCHIVED.
Non cancella mai. Solo archivia.

USO: META AGENT per gestire obsolescenza
```

---

## Compression Rules (eseguite da META AGENT)

```
→ Sessioni > 30 giorni → comprimi in lesson_learned
→ Decisione ripetuta ≥ 5 volte → diventa policy
→ Strategia con success_rate ≥ 0.85 per ≥ 10 usi → promossa a best_practice
→ Strategia con success_rate < 0.30 per ≥ 5 usi → archiviata come anti_pattern
→ Mai cancellare. Sempre archiviare con "superseded_by" e "archived_reason"
```

---

## Strategie Pre-Caricate

| ID | Nome | Categoria | Success Rate |
|---|---|---|---|
| STR-001 | Piramide Evolutiva | PLANNING | 0.87 |
| STR-002 | Critique-Before-Output | GENERAL | 0.92 |
| STR-003 | Memory-First Design | GENERAL | 0.85 |
| STR-004 | Parallel Execution | ORCHESTRATION | 0.78 |
