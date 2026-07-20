# Stage 7 — Depth & Optimization Pass

> 🆕 Stage introdotto in PLAN-v6 (Phase 9) per rispondere ai 3 failure mode reali identificati nei test v1.0:
> 1. Skill prodotte senza agenti interni
> 2. Sub-skill nested con un solo `SKILL.md`
> 3. Agenti con file canonici mancanti

## Obiettivo

Trasformare il **DRAFT** del builder (Stage 6) in un **artefatto operativo ricco e completo**, garantendo:
- Skill (root e nested) con struttura piena (`references/` ≥3 file, `evals/`, opzionali scripts/assets)
- Agenti con tutti i 7 file canonici (agent.md, system_prompt.md, tools.md, playbook.md, failure_modes.md, eval_cases.json, README.md)
- Reference espanse (≥150 righe ognuna, con esempi, schemi, anti-pattern, cross-ref)
- Formule del sorgente applicate completamente
- Output "umano" (senza LLM-speak)

## Agente principale

**Depth Conductor** (sub-router del Conductor principale) coordina il team Ox:

| Optimizer | Cosa fa | File |
|---|---|---|
| **O1 skill-depth-agent** | Skill complete (references/, evals/, ecc.) | `agents/optimizers/skill-depth-agent.md` |
| **O2 agent-depth-agent** | Agenti con 7 file canonici | `agents/optimizers/agent-depth-agent.md` |
| **O3 reference-expander-agent** | Reference dense (150-400 righe) | `agents/optimizers/reference-expander-agent.md` |
| **O4 humanizer-agent** | Eliminazione LLM-speak (condizionale) | `agents/optimizers/humanizer-agent.md` |
| **O5 formula-validator-agent** | Formule del sorgente complete | `agents/optimizers/formula-validator-agent.md` |

## Spawn order

```
Stage 6 (Bx) → DRAFT
       │
       ▼
[Depth Conductor]
       │
       ├─► O1 skill-depth ──┐
       │                    ├─► (parallelo, lavorano su file diversi)
       └─► O2 agent-depth ──┘
                            │
                            ▼
                       O3 reference-expander
                            │
                            ▼
                       O5 formula-validator  (se KG contiene framework)
                            │
                            ▼
                       O4 humanizer (se KG non ha tag di esclusione)
                            │
                            ▼
                 Stage 8 (External QA) →
```

## Quando questo stage si attiva

**Obbligatorio** per target:
- `skill`
- `team`
- `workflow`
- `orchestration`

**Opzionale** (skip default) per:
- `doc` (Stage 4 MKD è già ricco)
- `wiki` (l'output sono note atomiche, struttura diversa)
- `custom` (forma libera, optimizer poco rilevante)

Il Conductor decide in base al target dichiarato.

## Quando si conclude

Quando **tutti gli optimizer attivi** hanno completato (status: ok|ok_with_warnings|skipped).

Output cumulativo in `stage-07/`:
- `o1-depth-report.json`
- `o2-depth-report.json`
- `o3-depth-report.json`
- `o4-depth-report.json` (se humanizer attivo)
- `o5-formula-report.json` (se formula validator attivo)
- `depth-summary.md` (consolidato dal Depth Conductor)

## Input attesi

```
<workspace>/forge-run-<ts>/
├── stage-03/kg.json              # per attivazione condizionale O4/O5
├── stage-04/master.md            # per arricchimento contenuti
└── stage-06/output/<artifact>/   # DRAFT da elevare
```

## Output

Modifiche **in-place** dentro `stage-06/output/<artifact>/`. Gli optimizer non scrivono in `stage-07/output/` separato — arricchiscono direttamente il DRAFT del builder.

In `stage-07/` solo i report JSON.

## Quality thresholds (post-Stage 7)

Dopo Stage 7, l'output dovrebbe rispettare:

```python
post_stage_7_quality = {
    "skills_with_min_3_refs": 1.0,            # 100%
    "agents_with_min_5_canonical_files": 1.0, # 100%
    "agents_with_min_7_canonical_files": 0.85, # 85% (alcuni accettabili a 5/7)
    "references_avg_lines": 180,              # min 150, target 200-300
    "examples_per_reference_avg": 2,
    "formula_completeness": 1.0,              # 100% se O5 attivo
    "llm_speak_smells_per_file": 0,           # 0 se O4 attivo
}
```

Stage 8 (QA esterna C1+C3) ora ha soglie corrispondenti più stringenti per **bloccare** se Stage 7 non ha fatto il suo lavoro.

## Failure modes specifici

| Failure | Sintomo | Mitigazione |
|---|---|---|
| O1 non riesce a espandere skill (KG povero) | Skill restano magre | Manual flag per Conductor + warning all'utente "sorgente insufficiente per skill ricca" |
| O2 genera playbook irrealistici | Pattern stereotipato | O4 humanizer fa cleanup downstream |
| O3 over-expansion (file >500 righe) | File ingestibili | Hard cap O3: se >500 righe, splittare in 2 file invece |
| O5 segnala formula incompleta non-fixabile | Manual review needed | Conductor escalate all'utente con razionale |
| O4 cambia significato | Validation post-write fallisce | Rollback automatico + flag in report |
| Pipeline troppo lenta | >10 min totali su artifact medio | Salta O3/O4 per artifact piccoli (<10 file) |

## Contratto con Stage 8

Stage 8 (C1+C3) ora valida l'output con **soglie corrispondenti a Stage 7**:
- C3 fallisce se skill ha <3 reference (anche dopo O1)
- C3 fallisce se agente ha <5/7 file canonici (anche dopo O2)
- C1 fallisce se coverage <90% e gli optimizer non hanno mitigato

Se C1/C3 ritorna FAIL, il Conductor decide:
- **Iterate Stage 7**: spawn di nuovo O1/O2/O3 con istruzioni mirate sul gap
- **Iterate Stage 6**: regenerate dal builder (se il problema è strutturale a monte)
- **Escalation utente**: se 2 iterazioni hanno fallito

## Note operative

- Stage 7 può richiedere 5-15 minuti per artifact medio (5-10 skill/agent nested)
- Costo token: ~2-3x rispetto a Stage 6 (gli optimizer leggono e riscrivono)
- Per artifact molto grandi (>50 file), considera spawn batch (10 file alla volta per optimizer)
- I report JSON sono cumulativi: leggere tutti e 5 dà la storia completa dell'optimization

## Riferimenti

- PLAN-v6 §2 (team Ox dettagliato)
- PLAN-v6 §3 (spawn order)
- `agents/optimizers/*.md` (system prompt di ogni Ox)
