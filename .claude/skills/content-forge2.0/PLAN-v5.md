# 📐 PLAN v5 — Skill `content-forge` (comando `/forge`)

> **Cosa cambia rispetto a v4:**
> 1. ➕ **Nuovo Stage 4 — Master Knowledge Document (MKD)**: il "documento perfetto" ampliato è prodotto SEMPRE come passaggio intermedio, indipendentemente dal target finale.
> 2. ➕ **Input multi-source / cartella**: A1 ora gestisce nativamente cartelle con multipli file (Opzione B: ogni file = sorgente parallelo, KG unificato con tracciabilità per file di origine).
> 3. ➕ **Limiti di dimensione documentati** chiaramente nel SKILL.md.
> 4. 🔄 **Renumber stages**: 8 stage totali (era 7). Old 4-7 diventano 5-8.

---

## 0. L'insight che ha portato a v5

In v1-v4, il `doc` (documento ampliato) era **uno degli 8 target**. Se l'utente chiedeva `agent`, il builder leggeva direttamente il KG e ci costruiva sopra l'agente.

L'utente ha fatto notare che questo è **architettonicamente sbagliato**:
- Il KG è strutturato ma "asciutto" (atomi + edge + cluster, senza prosa).
- Costruire un agente direttamente dal KG salta una fase di **perfezionamento del contenuto**.
- La stessa skill che ha bisogno di ampliare/spiegare/esemplificare deve farlo SEMPRE, non solo se il target è `doc`.

Soluzione: introdurre il **Master Knowledge Document (MKD)** come stage intermedio canonico. Da MKD si generano POI tutti i target.

Bonus: con il MKD come base, il target `doc` diventa quasi una "esposizione" del MKD (formattazione + frontmatter + handoff), molto più snello.

---

## 1. Nuovo pipeline (8 stage)

```
┌─────────────────────────────────────────────────────────────┐
│ INVOCAZIONE /forge <source> [--target=X]                    │
│   source può essere: file singolo / cartella                │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 1 — INGESTION & NORMALIZATION                         │
│  Detect: singolo file | cartella | misto                    │
│  Cleaning + chunking per ogni sorgente                      │
│  Output: cleaned.md (concatenato con separatori) + chunks   │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 2 — DEEP ANALYSIS (parallel, P1-P9 rilevanti)         │
│  Output: atoms-*.json (con campo source_file per multi-src) │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 3 — KNOWLEDGE GRAPH BUILD                             │
│  Dedup cross-source, cluster, edge, gap                     │
│  Output: kg.json + kg.md + gaps.md (kg.md è VISTA SINTETICA)│
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 🆕 STAGE 4 — MASTER KNOWLEDGE DOCUMENT (MKD)                │
│  Spawnato SEMPRE, qualunque sia il target finale.           │
│  Trasforma KG in DOCUMENTO PERFETTO ampliato:               │
│   • copertura 100% atomi                                    │
│   • ogni atomo espanso in spiegazione canonica + estesa     │
│   • esempi dal sorgente + ➕ esempi aggiuntivi              │
│   • schemi (mermaid/ASCII/tabelle) dove applicabile         │
│   • controesempi & steel-manning per claim non banali       │
│   • cross-reference interni fitti                           │
│   • glossario + indice + FAQ                                │
│   • lunghezza ≥ lunghezza sorgente (expansion principle)    │
│  Output: master.md + glossary.md + faq.md + schemas.md      │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 5 — TARGET SELECTION (era 4)                          │
│  Spawnato solo se target non specificato                    │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 6 — INTERACTIVE BUILD (era 5)                         │
│  PLAN → ASK → BUILD → SELF-CRITIQUE → ITERATE               │
│  I builder ora leggono: KG + MKD + user_answers             │
│  (MKD è la fonte primaria di prosa, KG quella di struttura) │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 7 — EXTERNAL QA (era 6, C1+C3 parallel)               │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 8 — PACKAGING & DELIVERY (era 7)                      │
│  L'output finale include SEMPRE il MKD come bonus           │
│  (l'utente ottiene il documento perfetto anche se ha chiesto│
│   target=agent o altro)                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Il nuovo agente: A5 `mkd-builder-agent`

**Famiglia**: pipeline (NON builders — i builders sono per i target finali)
**File**: `agents/pipeline/mkd-builder-agent.md`
**Stage**: 4
**Spawned by**: conductor (sempre, sequenziale dopo A3)

### Responsabilità

Trasformare il `kg.json` in **un documento markdown completo e ampliato** che rappresenti la conoscenza del sorgente nella forma più ricca, leggibile e completa possibile.

NON è un riassunto. NON è una vista del KG (quella è `kg.md`). È **il documento perfetto** che l'utente avrebbe voluto avere fin dall'inizio, costruito ampliando ogni atomo del KG.

### Input

```
inputs:
  - stage-03/kg.json
  - stage-03/kg.md
  - stage-01/cleaned.md       # serve per citazioni verbatim
  - state.json                 # per conoscere lingua/audience se già noti
```

### Output

```
stage-04/
├── master.md           # il documento principale (≥ sorgente in lunghezza)
├── glossary.md         # estratto, una entry per termine definito
├── faq.md              # generata da steel-manning (P4)
├── schemas.md          # raccolta degli schemi mermaid/ascii generati
├── changelog.md        # tracciabilità tra iterazioni MKD
└── mkd-report.json     # stats per Conductor
```

### Pattern applicati

Tutti i 9 pattern P1-P9, in modalità "scrittura massima":
- P1 (atomic) → ogni atomo → almeno una sezione
- P2 (claim/evidence/example) → ogni claim ampliata + esempio dal sorgente + ➕ esempio aggiuntivo
- P3 (hierarchy) → ordinamento dei capitoli
- P4 (steel-manning) → contro-argomenti per claim non banali (in FAQ)
- P5 (procedural) → procedure dettagliate
- P6 (mental model) → frame interpretativi
- P7 (schema) → diagrammi
- P8 (cross-ref) → link interni `[label](#anchor)`
- P9 (target-shape) → la "forma canonica" del MKD

### Differenza con il target `doc`

| Aspetto | MKD (Stage 4) | `doc` target (Stage 6 se richiesto) |
|---|---|---|
| Quando prodotto | SEMPRE | Solo se utente sceglie target=doc |
| Scopo | Base intermedia per tutti i builder | Output finale consegnabile |
| Frontmatter | Minimo (interno) | Completo (audience, register, ecc. da ASK) |
| Formato | "Tutto il contenuto possibile" senza vincoli stile | Adattato a registro/audience scelti |
| Customizzazione | Nessuna (deterministico dal KG) | Adattato a risposte ASK utente |

**Implicazione semplificante**: il `doc-builder-agent` (B1) ora diventa molto più snello — è essenzialmente un "MKD adapter" che prende il MKD e lo riformatta in base alle preferenze utente (registro, audience, lingua se diversa, ecc.).

---

## 3. Input multi-source / cartella (modifica A1)

### Input supportati

| Tipo | Esempio | Comportamento |
|---|---|---|
| Singolo file `.md`/`.txt` | `/forge transcript.md` | Sorgente unico, pipeline standard |
| Cartella con N file flat | `/forge ./yt-transcripts/` | Ogni `.md`/`.txt` = sorgente parallelo |
| Cartella ricorsiva | `/forge ./materiale/ --recursive` | Cammina sotto-cartelle |
| Lista esplicita | `/forge file1.md,file2.md,file3.md` | Sorgenti elencati |

### Filtraggio

- Default: `*.md`, `*.txt`, `*.markdown`
- Opzionale `--ext=md,txt,pdf` per estensioni custom (PDF richiede preprocessing extra, vedi §4)
- Rispetta `.forgeignore` (sintassi gitignore) se presente nella cartella

### Output di A1 con multi-source

```
stage-01/
├── cleaned.md              # CONCATENAZIONE di tutti i sorgenti con separatori
├── chunks.json             # chunk con campo source_file
└── sources.json            # mappatura file originale → range in cleaned.md
```

`cleaned.md` ha separatori espliciti:
```markdown
<!-- FORGE_SOURCE_BOUNDARY id="src-001" file="transcript_video1.md" -->
... contenuto pulito del primo file ...

<!-- FORGE_SOURCE_BOUNDARY id="src-002" file="transcript_video2.md" -->
... contenuto pulito del secondo file ...
```

I separatori sono **invisibili nel rendering markdown** (commenti HTML) ma riconoscibili da A2 e dal MKD-builder per:
- Tracciabilità: ogni atomo ha `source_file`
- Citazioni: il MKD può dire "come spiegato in [video 1]"
- Dedup: A3 sa identificare lo stesso concetto presente in 2+ sorgenti

### Shape `sources.json`

```python
{
    "total_sources": int,
    "total_words": int,
    "sources": [
        {
            "id": "src-001",
            "path": "<original-path>",
            "size_bytes": int,
            "word_count": int,
            "language_detected": str,
            "type_detected": str,
            "range_in_cleaned": [int, int]  # offset start/end in cleaned.md
        }
    ]
}
```

---

## 4. Limiti di dimensione (documentati)

```python
SOURCE_SIZE_LIMITS = {
    "comfort_zone": {
        "single_file_words": (500, 200_000),
        "folder_total_words": (1_000, 500_000),
        "folder_total_files": (1, 30),
    },
    "hard_limit_per_run": {
        "single_file_words": 500_000,
        "folder_total_words": 1_000_000,
        "folder_total_files": 100,
    },
    "warnings": {
        "<500 words": "pipeline overkill — proponi modalità leggera o decline",
        ">100k words single": "richiederà 60-120s solo per stage 1-2",
        ">300k words single": "consigliato splittare in più run",
        ">50 files folder": "consigliato run separati per gruppi",
    },
}
```

A1 esegue questo check PRIMA di Stage 1 e segnala al Conductor che decide come avvisare l'utente.

### Estensioni input (Phase 4+, opzionale)

- PDF: richiede `pdfplumber` o equivalente in `scripts/transcript_cleaner.py`
- DOCX: richiede `python-docx`
- HTML/blog: richiede `trafilatura` o BeautifulSoup
- YouTube URL diretto: richiede `youtube-transcript-api` (estrae senza scaricare video)

Tutto opzionale, attivato da estensione del file di input.

---

## 5. Modifiche ai file esistenti

### Renumber stages

```
references/stages/
├── 01-ingestion.md          (aggiornato: folder support)
├── 02-analysis.md           (aggiornato: campo source_file)
├── 03-knowledge-graph.md    (aggiornato: cross-source dedup)
├── 04-master-document.md    (🆕 NUOVO)
├── 05-target-selection.md   (era 04)
├── 06-interactive-build.md  (era 05, builder ora leggono KG+MKD)
├── 07-coverage-check.md     (era 06)
└── 08-packaging.md          (era 07, include MKD nel deliverable)
```

### Agents modificati

- `agents/pipeline/ingestion-agent.md` (A1) — sezione folder/multi-source
- `agents/pipeline/mkd-builder-agent.md` (🆕 A5) — nuovo agente
- `agents/conductor.md` — pipeline a 8 stage + decision tree per cartelle
- `agents/builders/doc-builder-agent.md` (B1) — semplificato: ora è "MKD adapter"
- Altri 7 builder (B2-B8) — aggiungo riga negli `reads_inputs`: `stage-04/master.md`

### Schemas

- 🆕 `references/schemas/mkd.schema.{md,json}` per validare il Master Document
- 🆕 `references/schemas/sources.schema.{md,json}` per `sources.json` di A1

### SKILL.md

- Aggiornato il loop principale (8 stage)
- Aggiunta sezione "Input supportati" (file singolo / cartella / lista)
- Aggiunti limiti di dimensione

### ARCHITECTURE.md

- Mappa file aggiornata
- Conteggi aggiornati

---

## 6. Nuovo conteggio file (post-v5)

| Categoria | Pre-v5 | Post-v5 | Δ |
|---|---|---|---|
| Agenti totali | 12 (11 + Conductor) | 13 (12 + Conductor) | +1 |
| Pipeline agents | 4 (A1-A4) | 5 (A1-A4 + A5 mkd) | +1 |
| Stages | 7 | 8 | +1 |
| Schemas | 10 (md+json = 20 file) | 12 (md+json = 24 file) | +2 entries, +4 file |
| **Totale file** | 187 | **~193** | +6 |

---

## 7. Roadmap aggiornata

| Fase | Cosa | Stato |
|---|---|---|
| 0-2 | PLAN v1-v4, scaffolding, contenuti operativi | ✅ |
| **2.5** | **Refactor v5: MKD + multi-source** | ⏳ **in corso** |
| 4 | Implementazione Python (scripts + lib + test) | ⏭ next dopo refactor |
| 5 | Rifinitura SKILL.md | |
| 6 | Esempi reali nei templates | |
| 7 | Test end-to-end reali | |
| 8 | Packaging `.skill` finale | |

---

## 8. Decisioni di design ratificate in v5

1. **MKD come stage intermedio obbligatorio**: sì.
2. **MKD prodotto da agente dedicato (A5)** invece di riusare doc-builder: sì (separa preoccupazioni — MKD è pipeline cognitiva, doc-builder è "adattatore stilistico").
3. **Multi-source nativo (Opzione B)** invece di solo concatenazione (A): sì (tracciabilità è valore aggiunto chiaro).
4. **MKD incluso nell'output finale anche per target ≠ doc**: sì (è un bonus per l'utente — paga il costo cognitivo una volta, ottiene 2 artefatti).
5. **Renumber esplicito degli stage** (anziché tenere 4 vecchio e aggiungere 4.5): sì (più pulito, anche se costa qualche modifica).
