# Stage 6 — Interactive Build

> Lo stage centrale di `content-forge`. Loop **PLAN → ASK → BUILD → SELF-CRITIQUE → ITERATE** per il target scelto.

## Obiettivo

Costruire l'artefatto del target finale (`doc` / `agent` / `team` / `skill` / `workflow` / `orchestration` / `wiki` / `custom`) attraverso un dialogo strutturato con l'utente, non in un'unica botta.

## Agenti principali

- **D1 `question-designer-agent`** — genera le domande della fase ASK (adattive al KG).
- **Bx `<target>-builder-agent`** — uno dei 8 builder (vedi `agents/builders/`).

## Sotto-fasi (cicliche)

```
5a. PLAN          (Bx legge KG, propone piano)
5b. ASK           (D1 genera domande adattive; Conductor le porge all'utente)
5c. ARCH          (Bx scrive scaffold + contratti)
5d. BUILD         (Bx riempie i file canonici)
5e. SELF-CRITIQUE (Bx si rilegge come occhi nuovi)
5f. ITERATE       (se serve, riparti da 5d con feedback)
```

Vedi `references/processes/<target>.md` per il dettaglio sub-fasi target per target.

## Input attesi

```
<workspace>/forge-run-<ts>/
├── stage-01/cleaned.md          # per citazioni se servono
├── stage-01/sources.json        # multi-source tracciabilità
├── stage-03/kg.json             # struttura (atomi, cluster, edge)
├── stage-03/kg.md
├── stage-04/master.md           # 🆕 fonte PRIMARIA di prosa per i builder
├── stage-04/glossary.md         # 🆕 termini
├── stage-04/faq.md              # 🆕 da steel-manning, utile per failure_modes
└── state.json (target già definito)
```

**Importante**: dopo l'introduzione del MKD (Stage 4), i builder hanno DUE fonti:
- `kg.json` → struttura (lookup per atomi, edge, cluster)
- `master.md` → prosa (definizioni espanse, esempi, schemi già scritti)

I builder NON devono riscrivere ciò che il MKD già contiene — devono **estrarre e trasformare** per il target.

Per `orchestration`: anche `stage-06/existing_components.json` (precondizione).

## Output canonici

```
<workspace>/forge-run-<ts>/stage-06/
├── ask-set.json
├── ask-set.md
├── user_answers.json
└── output/<artifact-slug>/...   # struttura specifica al target
```

La struttura interna di `output/` è definita per ogni target in `references/processes/<target>.md §2`.

## Flusso di controllo (vista Conductor)

```
1. Conductor leggi state.json → target=<X>
2. Spawn Bx → riceve PLAN
3. Mostra PLAN all'utente (sintesi alta)
4. Spawn D1 → ask-set.json
5. Conductor porge domande all'utente, raccoglie user_answers.json
6. Spawn Bx con user_answers → BUILD
7. Bx fa SELF-CRITIQUE
8. Se SELF-CRITIQUE clean → handoff a Stage 6 (QA esterna)
   Se issues → Bx itera (loop interno, max 3 volte)
   Se issues persistenti → escalation all'utente
```

## Quando si conclude

`Bx` ritorna `status: ok` con `build_report.ready_for_external_qa: true`.

## Failure modes specifici

| Failure | Mitigazione |
|---|---|
| ASK sotto-specificata | Conductor riconosce risposte vaghe, ri-spawna D1 per follow-up |
| Build loop infinito (>3 self-critique iterations) | Conductor escalation: mostra all'utente i problemi residui, chiedi decisione |
| L'utente cambia idea sul target a metà | OK: salva il KG, spawna nuovo builder con stesso KG |
| L'utente vuole rivedere ASK durante BUILD | Conductor sospende, ri-spawna D1 con context dell'attuale BUILD |

## Contratto con Stage 6

Stage 6 (QA esterna C1+C3) legge `stage-06/output/<artifact-slug>/` e produce report. Se ritorna fail, il Bx **riprende** (Stage 5 non finisce mai veramente fino a quando QA non passa o utente accetta).

## Note operative

- Tracciamento: ogni iterazione del loop è loggata in `state.json["iteration"]`.
- I builder NON parlano all'utente. Tutte le interazioni passano per il Conductor.
- D1 genera domande in **batch** (max 6 per batch). Il Conductor le porge un batch per volta per non sovraccaricare.
