# Stage 1 — Ingestion & Normalization

> Primo stadio del pipeline `content-forge`. Letto dal **Conductor** quando deve preparare il sorgente per l'analisi.

## Obiettivo

Trasformare il sorgente grezzo (con timestamp, filler vocali, ripetizioni, formattazione disomogenea) in un testo **pulito e segmentato in chunk semantici**, pronto per l'analisi parallela di A2.

Non perde informazione: la pulizia è cosmetica (timestamp, filler vocali), mai semantica.

## Agente principale

**A1 `ingestion-agent`** — vedi `agents/pipeline/ingestion-agent.md` per system prompt completo.

## Script di supporto

**`scripts/transcript_cleaner.py`** — pulizia deterministica (regex, dedupe ripetizioni vocali, normalizzazione markdown).

## Input attesi

```
<workspace>/forge-run-<ts>/inputs/
└── source.{md,txt,...}     # il sorgente grezzo
```

Detect del tipo di sorgente:
- YouTube transcript (con timestamp `00:01:23`, formattazione SRT/VTT spesso convertita)
- Articolo / blog post
- Brief / documento aziendale
- Misto (concatenazione di più sorgenti)

## Output canonici

```
<workspace>/forge-run-<ts>/stage-01/
├── cleaned.md          # sorgente pulito (no timestamp, no filler, MD normalizzato)
└── chunks.json         # segmentazione semantica
```

Shape di `chunks.json` (vedi `agents/pipeline/ingestion-agent.md §3`):

```python
{
  "source_path": str,
  "total_chunks": int,
  "language_detected": str,
  "source_type_detected": str,
  "chunks": [
    {"id": str, "start_offset": int, "end_offset": int,
     "title_heuristic": str, "word_count": int}
  ]
}
```

## Quando questo stage si attiva

Sempre, immediatamente dopo l'invocazione `/forge`. Il Conductor lo lancia per primo, indipendentemente dal target scelto.

## Quando questo stage si conclude

Il Conductor verifica:
- `stage-01/cleaned.md` esiste e non è vuoto
- `stage-01/chunks.json` valida lo schema
- `status` dell'agente è `ok`

Poi aggiorna `state.json`:
```python
state["current_stage"] = "stage-02"
state["completed_stages"].append("stage-01")
```

## Failure modes specifici

| Failure | Sintomo | Cosa fa il Conductor |
|---|---|---|
| Sorgente illeggibile/corrotto | A1 ritorna `failed` | Mostra all'utente l'errore tecnico, chiedi nuovo path |
| Lingue mescolate 50/50 | A1 ritorna `needs_user_input` | Chiedi all'utente "quale lingua tenere" |
| Sorgente già pulito | A1 segnala in summary | Procedi normalmente, conta come success |
| Sorgente <500 parole | Trigger upstream del Conductor | Avvisa che il pipeline è overkill, proponi modalità leggera |
| Sorgente >300k token | Trigger upstream | Avvisa, chiedi se limitare/procedere a chunk |

## Contratto con Stage 2

Stage 2 (A2 analyst-agent) consuma `chunks.json` e `cleaned.md`, processando in parallelo 1 istanza per chunk. Per garantire la parallelizzazione, A1 DEVE produrre chunks **indipendenti semanticamente** (nessun chunk richiede contesto da un altro per essere analizzato).

## Note operative

- Per sorgenti molto grandi (>100k token), Stage 1 può richiedere 30-60s. Mostra spinner all'utente.
- Il chunking deve preservare blocchi di codice/lista/tabella interi (mai spezzare a metà).
- Se l'utente passa un singolo file `.md` già strutturato (heading H1/H2 visibili), preferisci spezzare lì.
