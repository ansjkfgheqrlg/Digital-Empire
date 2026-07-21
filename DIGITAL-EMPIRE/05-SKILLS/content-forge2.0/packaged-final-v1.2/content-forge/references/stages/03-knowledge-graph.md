# Stage 3 — Knowledge Graph Build

> Assembla tutti gli atomi prodotti da Stage 2 in **un grafo coerente**: dedup, edge inference, clustering, gap detection.

## Obiettivo

Trasformare N file `atoms-chunk-*.json` (con possibili duplicati, atomi correlati distribuiti, granularità incoerente) in UN `kg.json` con:
- atomi deduplicati e ID globali
- cluster tematici
- edge tipizzati (prerequisite, contrasts, applies_in, see_also, ...)
- lacune dichiarate (concetti menzionati ma non spiegati)

Il KG è la **lingua franca** del pipeline: ogni stage successivo lo legge.

## Agente principale

**A3 `knowledge-graph-agent`** — 1 istanza singola, sequenziale dopo Stage 2. Vedi `agents/pipeline/knowledge-graph-agent.md`.

## Pattern applicati

- **P3 — Hierarchy & Dependency** — formalizza gli edge prerequisite/depends_on
- **P8 — Cross-reference** — assembla gli edge sibling_of / see_also / contrasts / applies_in

## Input attesi

```
<workspace>/forge-run-<ts>/stage-02/atoms-chunk-*.json
```

## Output canonici

```
<workspace>/forge-run-<ts>/stage-03/
├── kg.json         # machine-readable (forma canonica)
├── kg.md           # vista umana per Conductor/utente
└── gaps.md         # lacune (atomi menzionati ma non definiti)
```

Schema completo di `kg.json` in `references/schemas/kg.schema.{md,json}` + vedi `agents/pipeline/knowledge-graph-agent.md §3`.

## Algoritmo (vista alto livello)

```python
def build_kg(atoms_files: list[Path]) -> dict:
    # 1. Load tutti gli atomi
    atoms = []
    for f in atoms_files:
        atoms.extend(json.load(open(f))["atoms"])

    # 2. Dedup (high lexical/semantic similarity → merge preservando source_excerpts)
    atoms = merge_duplicates(atoms, threshold=0.85)

    # 3. Re-ID globale (a-001 a-002 ...)
    atoms = reassign_global_ids(atoms)

    # 4. Edge inference (P3 + P8)
    edges = []
    edges.extend(infer_prerequisites(atoms))       # term overlap + hints
    edges.extend(infer_contrasts(atoms))           # P4 hints
    edges.extend(infer_applies_in(atoms))          # example_of inverse
    edges.extend(infer_see_also(atoms))            # sibling_of via clustering

    # 5. Cluster atoms (topic modeling soft + heuristics)
    clusters = build_clusters(atoms, edges)

    # 6. Gap detection (concetti riferiti ma non definiti)
    gaps = detect_gaps(atoms)

    # 7. Validation
    if has_cycle(prereq_edges, [a["id"] for a in atoms]):
        edges = break_lowest_weight_cycles(edges)

    return {"atoms": atoms, "clusters": clusters, "edges": edges, "gaps": gaps, ...}
```

## Quality bar (da `agents/pipeline/knowledge-graph-agent.md §6`)

- `edge_count >= atom_count / 2` (se troppo basso, sotto-collegato)
- `atomi review_needed < 15%` del totale
- `cluster_count` tra 3 e 15 per sorgenti medi

## Quando questo stage si attiva

Dopo Stage 2 (tutti i file `atoms-chunk-*.json` esistono e validi).

## Quando si conclude

`kg.json` esiste, valida `kg.schema.json`, ha `atoms`, `clusters`, `edges`, `gaps` non vuoti.

## Failure modes specifici

| Failure | Mitigazione |
|---|---|
| Dedup eccessivo (merge troppo aggressivo) | Threshold default 0.85; abbassare a 0.8 se utente segnala perdita di sfumature |
| Edge inference scarsa (KG "atomistico") | Verificare ricchezza `related_concepts_hints` da A2; eventualmente girare un secondo pass |
| Cluster troppo grandi (1 cluster con 80% atomi) | Splittare via topic modeling; richiede possibile review utente |
| Gap eccessivi (>30% atomi referenced ma not defined) | Avvisa: sorgente forse incompleto, suggerisci materiale supplementare |

## Contratto con Stage 4

Stage 4 (A4 target-advisor) legge `kg.json` per analizzare:
- distribuzione di `category` (concept/procedure/framework/...) → segnali per target
- presenza di metafore/modelli mentali → segnali per target=agent
- struttura procedurale → segnali per target=workflow
- granularità → segnali per target=wiki vs target=doc

## Note operative

- Per sorgenti molto grandi (200+ atomi), il KG può eccedere 1 MB. È OK ma considera che alcuni file `kg.md` (vista umana) andranno troncati o paginati per lettura veloce.
