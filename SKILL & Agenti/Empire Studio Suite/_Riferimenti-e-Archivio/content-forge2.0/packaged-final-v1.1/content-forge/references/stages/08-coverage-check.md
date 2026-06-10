# Stage 8 — External QA (Coverage + Schema)

> Verifica indipendente della qualità dell'output del builder. Due check in **parallelo**: coverage degli atomi (C1) + conformità schema (C3).

## Obiettivo

Validare che l'output di Stage 5:
1. **Copre** tutti gli atomi del KG (≥ soglia per target).
2. **Rispetta** la forma canonica del target (file presenti, frontmatter valido, integrità referenziale, custom checks).

È un check **indipendente dal builder** (altri agenti, occhi nuovi) → cattura issue che la self-critique interna del builder potrebbe perdere.

## Agenti principali (eseguiti in PARALLELO)

- **C1 `coverage-verifier-agent`** — vedi `agents/qa/coverage-verifier-agent.md`
- **C3 `target-schema-validator-agent`** — vedi `agents/qa/target-schema-validator-agent.md`

## Script di supporto

- `scripts/coverage_check.py` (usato da C1)
- `scripts/schema_validator.py` (usato da C3)
- `scripts/no_summary_lint.py` (usato in self-critique builder + C2 logica interna ai builder)
- `scripts/length_check.py` (per `doc` e `wiki`)
- `scripts/validate_dag.py` (per `workflow`)
- `scripts/obsidian_packager.py --check-only` (per `wiki`)

## Input attesi

```
<workspace>/forge-run-<ts>/
├── stage-03/kg.json
├── stage-06/output/<artifact-slug>/
└── references/schemas/<target>.schema.json
```

## Output canonici

```
<workspace>/forge-run-<ts>/stage-06/
├── coverage-report.json
├── coverage-report.md
├── schema-report.json
├── schema-report.md
└── qa-report.md             # sintesi unificata per Conductor/utente
```

## Soglie di coverage per target

```python
COVERAGE_THRESHOLDS = {
    "doc":           0.95,
    "wiki":          0.95,
    "skill":         0.90,
    "agent":         0.90,
    "team":          0.90,
    "workflow":      0.90,
    "orchestration": 0.85,
    "custom":        0.85,
}
```

## Quando questo stage si attiva

Quando team Ox (Stage 7) completa con `ready_for_external_qa: true`.

## Quando si conclude

Entrambi C1 e C3 hanno scritto i loro report. Il Conductor consolida in `qa-report.md`:

- **PASS** (entrambi PASS) → procede a Stage 8
- **WARN** (PASS con warnings) → procede ma annota
- **FAIL** (almeno uno FAIL) → handoff back a Stage 6 (regenerate) OR Stage 7 (re-optimize)

## Failure modes specifici

| Failure | Mitigazione |
|---|---|
| Coverage <soglia | Bx riprende, lavora sugli atomi mancanti specifici |
| Schema fail (file mancante) | Bx riprende, produce il file mancante |
| Schema fail (integrità referenziale) | Bx riprende, fixa i pointer rotti |
| Loop infinito (>3 iterazioni QA fail) | Conductor escalation all'utente |



## 🆕 Nuove soglie post-Stage 7 (PLAN-v6)

Dopo l'introduzione del Depth & Optimization Pass (Stage 7), Stage 8 ora valida con soglie più stringenti che riflettono ciò che gli optimizer Ox hanno garantito:

### C3 (target-schema-validator) nuovi check bloccanti

- `every_skill_has_min_3_references` — bloccante se skill ha <3 file in references/
- `every_agent_has_min_5_canonical_files` — bloccante se agente ha <5/7 file
- `every_agent_md_min_400_words` — bloccante se agent.md è scaffold
- `every_system_prompt_min_500_words` — bloccante se SP è troppo magro
- `every_playbook_min_5_conversations` — bloccante se playbook ha <5 conv
- `every_failure_modes_min_7` — bloccante se failure_modes.md ha <7 entry

Se uno di questi fallisce DOPO Stage 7, significa che gli optimizer non hanno potuto fare il loro lavoro (KG insufficiente o errore upstream) → escalation utente.


## Contratto con Stage 9

Stage 8 (packaging) procede solo se `qa-report.md` è PASS (eventualmente con WARN). Se FAIL persistente, packaging non parte e l'utente deve decidere.

## Note operative

- C1 e C3 vengono spawnati nello stesso turno (parallelo).
- C1 (coverage) tipicamente impiega più di C3 (per semantic match).
- Quando `obsidian_packager.py --check-only` riporta wikilink rotti, C3 li riporta come FAIL strutturale (non WARN).
