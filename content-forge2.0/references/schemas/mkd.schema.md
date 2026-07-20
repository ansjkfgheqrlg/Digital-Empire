# `mkd.schema` — Human-Readable Version

> Schema canonico per il **Master Knowledge Document** prodotto in Stage 4 da `A5 mkd-builder-agent`.
> Coppia con `mkd.schema.json`.

## Scopo

Validare che il MKD prodotto in Stage 4:
- abbia tutti i file canonici (`master.md`, `glossary.md`, `faq.md`, `schemas.md`, `changelog.md`, `mkd-report.json`)
- rispetti le quality thresholds (coverage 100%, ratio ≥1.2, ecc.)
- abbia struttura attesa in `master.md` (frontmatter + sezioni top obbligatorie)

## File canonici prodotti in stage-04/

| File | Scopo |
|---|---|
| `master.md` | Documento principale ampliato (≥1.2x sorgente) |
| `glossary.md` | Termini definiti estratti |
| `faq.md` | Domande generate da steel-manning (P4) |
| `schemas.md` | Raccolta schemi (mermaid/ASCII/tabelle) |
| `changelog.md` | Tracciabilità tra iterazioni MKD |
| `mkd-report.json` | Stats per Conductor + per Stage 6 builders |

## Quality thresholds (enforzate da self-critique di A5)

```python
{
    "atoms_coverage": 1.0,             # 100%, niente atomi orfani
    "length_ratio_vs_source": 1.2,     # minimo, target 1.5x
    "added_examples_rate": 0.5,        # ≥50% atomi non banali con ➕
    "schemas_for_structured_clusters": 1.0,  # 100% cluster procedurali/framework con schema
    "min_cross_refs_per_cluster": 2,
    "min_faq_questions": 5
}
```

## Validazione

```bash
python scripts/schema_validator.py --target mkd --output-dir <workspace>/stage-04/
```

(Nota: il MKD non è un "target" dell'utente, è uno stage interno. Il validator può comunque essere invocato manualmente.)
