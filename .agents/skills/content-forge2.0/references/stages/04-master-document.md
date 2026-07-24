# Stage 4 — Master Knowledge Document (MKD)

> 🆕 Stage **sempre attivo** (introdotto in PLAN-v5). Prodotto del KG diventa il documento perfetto ampliato, base canonica per i builder dei target finali.

## Obiettivo

Trasformare il `kg.json` (struttura asciutta machine-readable) in un **documento markdown completo e ampliato** che:
- copre il 100% degli atomi
- è più lungo del sorgente (`expansion principle`)
- include spiegazioni canoniche + estese, esempi (sorgente + ➕ aggiuntivi), schemi, controesempi (FAQ), cross-reference
- è la **base canonica** da cui i builder dei target finali (Stage 6) attingono

NON sostituisce il `doc` target — il `doc` target è una versione **stilisticamente customizzata** del MKD (con audience/registro/lingua adattati).

## Agente principale

**A5 `mkd-builder-agent`** — vedi `agents/pipeline/mkd-builder-agent.md` per SP completo.

## Pattern applicati

Tutti i 9 pattern P1-P9 in modalità "scrittura massima":

| Pattern | Dove nel MKD |
|---|---|
| P1 (atomic) | una sezione per atomo |
| P2 (claim/evidence/example) | ogni sezione: definizione + esempio sorgente + ➕ esempio aggiuntivo |
| P3 (hierarchy) | ordinamento cluster (topological sort) |
| P4 (steel-manning) | sezione FAQ generata |
| P5 (procedural decomposition) | procedure ampliate con step espliciti |
| P6 (mental model) | sezione "Modello mentale implicito" per atomi rilevanti |
| P7 (schema) | mermaid/ASCII/tabelle per ogni atomo strutturato |
| P8 (cross-ref) | link interni `[label](#anchor)` fitti |
| P9 (target-shape) | MKD È la shape canonica |

## Input attesi

```
<workspace>/forge-run-<ts>/
├── stage-01/cleaned.md       # per citazioni verbatim
├── stage-01/sources.json     # per tracciabilità multi-source
├── stage-03/kg.json          # struttura primaria
├── stage-03/kg.md            # vista umana del KG (riferimento)
└── state.json                # se lingua/audience già noti
```

## Output canonici

```
<workspace>/forge-run-<ts>/stage-04/
├── master.md           # documento principale (≥ sorgente)
├── glossary.md         # estratto: termini definiti
├── faq.md              # generata da steel-manning
├── schemas.md          # raccolta schemi
├── changelog.md        # tracciabilità iterazioni
└── mkd-report.json     # stats
```

Schema completo: `references/schemas/mkd.schema.{md,json}`.

## Quando questo stage si attiva

**SEMPRE** dopo Stage 3, qualunque sia il target finale dichiarato dall'utente.

```python
def should_run_stage_4():
    return True   # incondizionato
```

## Quando si conclude

`master.md` esiste, valida lo schema, coverage degli atomi = 100%, ratio lunghezza ≥ 1.0.

## Quality bar

```python
mkd_quality_thresholds = {
    "atoms_coverage": 1.0,        # 100% (massimo)
    "length_ratio_vs_source": 1.2, # min 1.2x; target 1.5x
    "added_examples_rate": 0.5,    # ≥50% atomi non banali hanno ➕
    "schemas_for_structured": 1.0, # 100% cluster procedurali hanno schema
    "cross_refs_per_cluster": 2,   # min 2
    "faq_min_questions": 5,        # min 5 per sorgenti medi
}
```

## Failure modes specifici

| Failure | Sintomo | Mitigazione |
|---|---|---|
| Coverage <100% | Atomi orfani | Capitolo "Atomi orfani" forzato in coda |
| Ratio <1.0 | Output più corto del sorgente | Forzare ampliamento via `➕` esempi e schemi |
| MKD enorme (>50k parole) | Sorgenti grandi, ratio >2x | Review: forse over-expansion; benchmark di sanity |
| Schemi mermaid rotti | Sintassi invalida | Validazione pre-commit + ASCII fallback |
| Multi-source confuso | Esempi senza fonte | Force `*(da <file>)*` se sources_count > 1 |

## Contratto con Stage 5/6

- **Stage 5 (Target Selection)**: legge `mkd-report.json` per statistiche + `master.md` per esempi nelle proposte di target. Può suggerire `doc` come "facile, abbiamo già la base" o `wiki` se cross-ref sono molti.
- **Stage 6 (Build target)**: TUTTI i builder leggono `stage-04/master.md` come fonte primaria di prosa (insieme a `stage-03/kg.json` per struttura).

  Esempio per `B2 agent-builder`:
  - `kg.json` → identifica tool, procedure, failure modes (struttura)
  - `master.md` → estrae spiegazioni canoniche, mental models surface (prosa per system_prompt.md)
  - `faq.md` → entry per failure_modes.md

## Note operative

- È lo stage più "scrittura-pesante" del pipeline: aspettati 30-90s per sorgenti medi.
- Il MKD è incluso nel deliverable finale (Stage 8) come bonus, anche se l'utente ha scelto un altro target. L'utente paga il costo cognitivo una volta, ottiene 2 artefatti.
- Per multi-source: il MKD può consolidare diverse formulazioni dello stesso concetto in una versione canonica, citando le sorgenti.
