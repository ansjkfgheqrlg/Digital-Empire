# PT10 — Master Document as Intermediate Stage

> **Shape canonica**: Tra l'analisi (Knowledge Graph) e la generazione del target finale, sempre uno **stage intermedio dedicato** che produce un Master Document ampliato e completo del sorgente. Il MKD è la base canonica da cui tutti i builder dei target attingono. Garantisce coerenza, riduce drift, dà all'utente un bonus deliverable.

## Quando applicarlo

✅ **Applica se**:
- Skill processa contenuto ricco (transcripts, docs lunghi, multi-source)
- Vuoi che target diversi (es. agent, skill, wiki) condividano stessa base content
- Vuoi dare all'utente un asset narrativo navigabile come bonus

❌ **NON applicare se**:
- Skill produce trasformazioni structurali pure (no contenuto narrativo)
- Input sempre molto piccolo (overhead MKD non vale)
- Tutti i target sono varianti minori dello stesso layout

## Perché funziona

### 1. Single source of truth per i builder
Tutti i builder dei target attingono dal **stesso MKD**. Coerenza garantita. Senza MKD, ogni builder rielaborerebbe il KG indipendentemente → output divergent.

### 2. Espansione una volta, riuso N volte
MKD è l'espansione canonica del sorgente. Generata una volta in Stage 4. I builder downstream non rifanno il lavoro di espansione, lo riformulano per il loro target.

Cost: 1x espansione. Beneficio: ogni target ottiene base ricca.

### 3. Bonus deliverable per l'utente
L'utente ha chiesto target=skill, ma ottiene anche il MKD nel pacchetto finale. **Asset gratis** che può archiviare/consultare. Aumenta valore percepito.

### 4. Debug intermedio
Se output finale ha problemi, MKD intermedio aiuta a localizzare: "il problema è nel MKD (espansione) o nel builder (target shaping)?". Senza MKD, il debug è opaco.

## Esempio dal nostro percorso

content-forge Stage 4 — Master Knowledge Document:

```
Stage 3 (KG) produces kg.json + kg.md (struttura asciutta)
       ↓
Stage 4 (MKD)  ← SEMPRE prodotto, qualunque sia target
   A5 mkd-builder-agent produces:
   - master.md (ratio ≥1.2x sorgente, 100% atomi coperti)
   - glossary.md
   - faq.md
   - schemas.md (raccolta schemi mermaid/ascii)
       ↓
Stage 5+ (Target Selection, Build, ...)
   Builder dei target leggono BOTH kg.json (struttura) AND master.md (prosa)
       ↓
Stage 9 (Packaging) includes MKD as BONUS
   Output finale: <target>/ + master-knowledge-document/
```

Caso reale Phase 7 (sorgente Manuale APSOC):
- Sorgente: 3041 parole
- KG: 18 atomi
- MKD: 5743 parole (1.88x sorgente)
- Output skill `objection-handler`: skill creata + master.md incluso come bonus

## Differenza con il target `doc`

Sottile ma importante:

| MKD (Stage 4) | doc target (Stage 6) |
|---|---|
| Sempre prodotto | Solo se utente sceglie target=doc |
| Stile neutro, max content | Adattato a audience/register/lingua scelti |
| Base intermedia | Deliverable finale |
| Frontmatter minimo interno | Frontmatter completo customizzato |

In pratica: il `doc-builder` (B1) in Stage 6 è essenzialmente un "MKD adapter" — prende il MKD e lo riformatta per l'utente. Molto più snello degli altri builder.

## Lo schema canonico del MKD

```python
{
    "required_files": ["master.md", "glossary.md", "faq.md", "schemas.md",
                       "changelog.md", "mkd-report.json"],
    "master_md": {
        "frontmatter_required_keys": ["title", "generated_by", "generated_at",
                                       "sources_count", "atoms_count"],
        "required_top_sections": ["Overview", "Indice", "Cross-reference",
                                   "Indice analitico"],
        "min_length_ratio_vs_source": 1.2,
        "min_atoms_coverage": 1.0  # 100% mandatory per MKD
    },
    "quality_thresholds": {
        "atoms_coverage": 1.0,
        "added_examples_rate": 0.5,
        "schemas_for_structured_clusters": 1.0,
        "min_cross_refs_per_cluster": 2,
        "min_faq_questions": 5
    }
}
```

## Sezione canoniche di `master.md`

```markdown
---
title: <topic>
generated_by: <agent>
sources_count: N
atoms_count: N
ratio_vs_source: 1.5
---

# <Title>

## Indice

[TOC navigabile]

## Overview

[Cosa contiene, da dove viene, modello mentale di base]

## <Cluster 1>

### <Atom 1> {#a-001}

**Definizione canonica**: [1-3 frasi]

**Spiegazione estesa**: [paragrafo]

**Esempio (sorgente)**: > [citazione verbatim]

**➕ Esempio aggiuntivo**: [generato]

**Schema**: [mermaid/ASCII se applicabile]

**Connessioni**:
- Prerequisito: [[<atom>]]
- Vedi anche: [[<atom>]]

### <Atom 2> {#a-002}
...

## <Cluster 2>
...

## Cross-reference (visione d'insieme)
[mappa concettuale globale]

## Indice analitico
[termini chiave + dove sono]
```

## ➕ Esempio in altri domini

**Technical writing**: "knowledge base article" prima del "tutorial" o "API reference". KB article è MKD-equivalent: comprensione canonica del topic. Tutorial/reference attingono da lì.

**Compilation intermediate representation (IR)**: LLVM IR è MKD-equivalent. Source code → IR → multiple targets (x86, ARM, WASM). IR è base canonica per multiple backends.

**Academic surveys**: paper di "survey" su un campo è MKD del field. Subsequent paper specifici attingono dal survey come comprehensive base.

## Anti-pattern correlato

**Skip-MKD shortcut**: builder direttamente dal KG → output thin perché manca step di espansione. Esattamente il problema che ha fatto nascere PT10 in PLAN-v5 di content-forge.

**Anti-pattern duale**: **MKD bloat** — MKD diventa 50k parole, include tutto. Builder downstream sommersi. Fix: MKD ha ratio target 1.2-1.5x, hard cap a 2x sorgente.

## Trade-off

| Pro | Contro |
|---|---|
| Single source of truth per builders | Stage in più nel pipeline |
| Bonus deliverable per utente | Token cost per generation MKD |
| Debug intermedio possibile | MKD può diventare bottleneck se troppo lungo |
| Coerenza tra target | Workflow più complesso |

## Decision tree

```
La tua skill processa contenuto ricco e produce multiple target tipi?
├─ NO → no MKD, builder direct from KG
└─ SÌ → continua
   ├─ I target diversi necessitano stessa base content?
   │  ├─ NO → builder indipendenti OK
   │  └─ SÌ → strong fit for MKD pattern
   │
   ├─ Hai bandwidth per Stage dedicato?
   │  ├─ NO → considera MKD come step interno di un builder
   │  └─ SÌ → MKD dedicated stage
   │
   └─ Implementa:
      1. Stage dedicato (es. Stage 4) post-KG, pre-Target-Selection
      2. Agente A5 mkd-builder-agent
      3. Schema canonical MKD (master.md + glossary + faq + schemas)
      4. Quality thresholds (ratio ≥1.2x, coverage 100%, ecc.)
      5. Builder downstream legge BOTH kg.json AND master.md
      6. Packaging include MKD as bonus in output finale
```

## Connessioni

- Implementa: P03 (No-Summary, Always Expansion) at intermediate stage
- Implementa: P12 (Traceability Source-to-Output) — MKD è anchor point
- Combina con: PT02 (Pipeline Stages with Handoff)
- Esempio reale: Stage 4 MKD di content-forge (PLAN-v5)

## Riferimenti

- Compiler Intermediate Representation pattern (LLVM IR)
- Single Source of Truth principle (DRY in software)
- "Knowledge Base" pattern in tech writing
- Anthropic skill-creator menzioni implicite del pattern
