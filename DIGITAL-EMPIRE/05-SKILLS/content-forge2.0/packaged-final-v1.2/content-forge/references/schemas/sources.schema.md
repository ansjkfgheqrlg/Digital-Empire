# `sources.schema` — Human-Readable Version

> Schema canonico per `sources.json` prodotto da `A1 ingestion-agent` in Stage 1.
> Documenta i sorgenti di input (file singolo o cartella multi-source) per garantire tracciabilità lungo l'intero pipeline.

## Scopo

Quando l'utente passa una cartella o lista di file, `sources.json` permette a tutti gli stage successivi di:
- Sapere quale file ha generato quale chunk / atomo
- Citare la fonte negli esempi del MKD ("come spiegato in [video 3]")
- Consolidare formulazioni multiple dello stesso concetto in dedup (A3)

## Campi principali

| Campo | Significato |
|---|---|
| `total_sources` | numero di file processati |
| `total_words` | parole totali pre-cleaning |
| `total_words_after_cleaning` | post-cleaning (in genere -10/15%) |
| `input_mode` | come l'utente ha passato l'input |
| `input_root` | path passato dall'utente (file singolo o cartella) |
| `sources[]` | array con metadata per ogni sorgente |
| `skipped_files[]` | file ignorati con motivo |

## `range_in_cleaned`

Cruciale per la tracciabilità: dato un offset in `cleaned.md`, permette di risalire al sorgente originale.

```python
def find_source_for_offset(offset: int, sources: list) -> dict:
    for src in sources:
        start, end = src["range_in_cleaned"]
        if start <= offset < end:
            return src
    return None
```

## Validazione

```bash
python scripts/schema_validator.py --target sources --output-dir <workspace>/stage-01/
```
