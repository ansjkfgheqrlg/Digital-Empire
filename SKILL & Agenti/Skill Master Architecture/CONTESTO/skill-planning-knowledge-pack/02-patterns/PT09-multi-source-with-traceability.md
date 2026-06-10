# PT09 — Multi-Source with Traceability

> **Shape canonica**: Skill accetta input multi-source (cartelle, liste, glob). Ogni source ha ID univoco, range nel file pulito concatenato, metadata. Tutta la pipeline downstream preserva la provenance: ogni atomo, ogni esempio, ogni componente dell'output sa **da quale source proviene**. Output può citare ("come spiegato in [video 3]").

## Quando applicarlo

✅ **Applica se**:
- Skill processa contenuto che può venire da multiple sources (transcript, articoli, doc multipli)
- Utente vuole sapere "da dove viene quest'info"
- Output deve essere onesto sulle fonti

❌ **NON applicare se**:
- Skill processa sempre singolo file
- Provenance non rilevante per il dominio (es. trasformazioni puramente strutturali)
- Overhead di tracking sproporzionato rispetto al beneficio

## Perché funziona

### 1. Onestà delle fonti = trust
Quando l'utente vede "esempio (da video 3)" sa esattamente da dove viene quell'esempio. Può verificare. Confidence aumenta.

Senza traceability: tutto sembra "uscito dal nulla" → trust più basso, soprattutto per contenuto controverso o tecnico.

### 2. Dedup intelligente cross-source
Se 3 video diversi spiegano lo stesso concetto, lo skill può consolidare in 1 atomo del KG ("questa idea compare in src-001, src-003, src-007") invece di 3 atomi duplicati.

Senza source tracking: dedup non è possibile o è cieco (perdi quale source aveva quale formulazione).

### 3. Output può adattare tono per source mix
Se sources sono tutti formali → output formale. Se mix formali + informali → output mid-register o segnala difference. Tracking permette decisioni informate.

## Esempio dal nostro percorso

content-forge implementa multi-source in Stage 1:

```python
# sources.json (output di A1)
{
    "total_sources": 7,
    "total_words": 20080,
    "input_mode": "list",
    "input_root": "test1-preventivi.md",
    "sources": [
        {
            "id": "src-001",
            "path": "transcript_video_federico.md",
            "relative_path": "transcript_video_federico.md",
            "word_count_original": 2400,
            "word_count_cleaned": 2150,
            "language_detected": "it",
            "type_detected": "youtube_transcript",
            "range_in_cleaned": [0, 12800]  # offset in cleaned.md
        },
        {
            "id": "src-002",
            "path": "transcript_marke_design.md",
            ...
            "range_in_cleaned": [12800, 19200]
        },
        ...
    ]
}
```

`cleaned.md` ha boundary markers invisibili:

```markdown
<!-- FORGE_SOURCE_BOUNDARY id="src-001" file="transcript_video_federico.md" -->

[contenuto pulito di video 1]

<!-- FORGE_SOURCE_BOUNDARY id="src-002" file="transcript_marke_design.md" -->

[contenuto pulito di video 2]
```

A2 (analyst) annota in ogni atomo il `source_file_id`. A3 (KG) preserva.
A5 (MKD) può citare: "**Esempio (da video di Federico)**: ..."

## Pattern operativi

### 1. Boundary markers nel cleaned source

Markers invisibili (HTML comments) che resistono al rendering markdown ma sono detection-friendly:

```markdown
<!-- FORGE_SOURCE_BOUNDARY id="src-NNN" file="<path>" -->
```

### 2. Atom annotation con source_file_id

```python
{
    "id": "a-007",
    "title": "Few-shot prompting",
    "source_file_id": "src-001",  # ← tracking
    "source_offsets": [[460, 690]],
    ...
}
```

### 3. KG con multi-source aggregation

Se un atomo emerge da multiple sources (concetto comune), KG può fare merge:

```python
{
    "id": "a-007",
    "title": "Few-shot prompting",
    "source_excerpts": [
        "Few-shot vuol dire dare 2-5 esempi...",   # da src-001
        "Mostra al modello esempi prima del task..."   # da src-003
    ],
    "source_file_ids": ["src-001", "src-003"],
    ...
}
```

### 4. Output con citazione

```markdown
**Esempio (sorgente, da video Federico)**:
> "Few-shot vuol dire dare al modello 2-5 esempi..."

**➕ Esempio aggiuntivo** (generato, ispirato da Andrei Pascu, video src-003):
> Classificazione email con 4 esempi misti...
```

### 5. Coverage check per source

```python
# Per ogni source, verifica che almeno N atomi compaiano nell'output
{
    "src-001": "covered (7 atomi presenti su 8)",
    "src-002": "covered (5/5)",
    "src-003": "partial (3/9) — potresti voler approfondire",
    ...
}
```

## ➕ Esempio in altri domini

**Academic paper bibliography**: ogni claim → citation. Tracciabilità a fonte primaria.

**Software dependency graph**: ogni package importato è tracked. `requirements.txt` + `pip freeze` mantengono provenance.

**News aggregators (Google News)**: ogni "story" è aggregato da multiple sources. Trackeano fonti, mostrano "vedi 12 fonti".

**ML training data provenance**: dataset cards documentano da dove viene ogni esempio. GDPR + auditability.

## Anti-pattern correlato

**Source soup**: concatenare multi-source in 1 blob senza markers. Risultato: impossibile sapere da dove viene cosa.

**Anti-pattern duale**: **Over-citation** — output 50% citazioni, illeggibile. Fix: citazioni per atomi importanti, narrative flow per il resto.

## Trade-off

| Pro | Contro |
|---|---|
| Trust + verifiability | Overhead di tracking |
| Dedup cross-source | Schema più complesso |
| Citation in output | Storage cresce (sources.json) |
| Auditability | Dependency su path stabili |

## Decision tree

```
La tua skill accetta input multi-source?
├─ NO → no traceability needed, skip
└─ SÌ → continua
   ├─ Utente userà output in contesti dove fonte importa?
   │  ├─ NO (output puramente strumentale) → traceability light
   │  └─ SÌ → full traceability
   │
   └─ Implementa:
      1. sources.json schema (id, path, ranges, metadata)
      2. Boundary markers in cleaned.md
      3. Atom annotation con source_file_id
      4. KG dedup intelligente (consolida atomi cross-source)
      5. Output con citation pattern ("(da src-NNN)" o equivalente)
      6. Coverage per source (non solo total)
```

## Quando NON applicare

- Input sempre singolo file → traceability è solo file→output, niente di complicato
- Output è transformation puramente strutturale (es. format conversion) — source preserved by structure
- Privacy constraints (in alcuni contesti tracking source è problema GDPR/HIPAA)

## Connessioni

- Implementa: P12 (Traceability Source-to-Output) per multi-source
- Combina con: PT02 (Pipeline Stages) — traceability deve attraversare tutti gli stage
- Validato da: scripts/coverage_check.py + per-source breakdown
- Esempio reale: content-forge Stage 1 sources.json + Stage 4 MKD con citazioni

## Riferimenti

- Academic citation standards (APA, MLA)
- W3C PROV (provenance vocabulary)
- ML Data Cards (Google, *Datasheets for Datasets*)
- npm package-lock.json (dependency tracking)
