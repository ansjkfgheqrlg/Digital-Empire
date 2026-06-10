# P9 — Target-Shape Mapping

> Ogni target ha una **forma canonica** (file, sezioni, campi obbligatori). P9 è il pattern che conosce queste forme e mappa il KG sopra di esse. È la specializzazione del builder.

## Cosa fa

Per ogni target, P9 definisce:
1. **La struttura di file canonica** (cosa deve esistere).
2. **Le sezioni obbligatorie** dei file principali.
3. **I campi obbligatori** di ogni schema.
4. **Le regole di mappatura** "atomo del KG → componente del target".

Senza P9 i builder produrrebbero output strutturati a caso. Con P9 producono output che sono **immediatamente utilizzabili** e **validabili** (da `target-schema-validator-agent` + `scripts/schema_validator.py`).

## Chi lo applica

**Tutti i builder (B1-B8)**, ognuno per il proprio target. Ogni builder ha una "shape conoscenza" specifica.

## Quando applicarlo

Sempre, in Stage 5 (BUILD). È il pattern operativo principale dei builder.

## La "shape conoscenza" per target (riferimento sintetico)

Per la versione completa di ogni shape, vedi `references/processes/<target>.md §2 (Forma canonica)` + `references/schemas/<target>.schema.json`.

### `doc`
- File principali: `document.md`, `glossary.md`, `faq.md`, `README.md`
- Sezioni doc: frontmatter, TOC, premessa, capitoli (uno per cluster KG), cross-ref, glossario rapido
- Mappatura: cluster KG → capitolo; atomo → sezione

### `agent`
- File: `agent.md`, `system_prompt.md`, `tools.md`, `playbook.md`, `failure_modes.md`, `eval_cases.json`, `README.md`
- Mappatura:
  - cluster procedurali (P5) → "How to act" del SP
  - cluster mental model (P6) → "How to think" del SP
  - tools menzionati → `tools.md`
  - failure mentions → `failure_modes.md`
  - examples (P2) → `playbook.md`

### `team`
- File: `topology.md`, `coordinator.md`, `agents/<role>.{md,system_prompt.md}`, `communication_protocol.md`, `handoff_rules.md`, `failure_handling.md`, `shared_state.md`, `team_eval_cases.json`, `README.md`
- Mappatura: assi di specializzazione del KG → ruoli del team (RACI strict)

### `skill`
- File: `SKILL.md`, `references/`, `agents/`, `scripts/`, `assets/templates/`, `evals/evals.json`, `README.md`
- Mappatura: KG → "skill shape" (trigger, output canonico, subagents needed, scripts needed)
- Vincoli: `SKILL.md` ≤500 righe; description "pushy"

### `workflow`
- File: `flow.md`, `flow.mermaid`, `state.md`, `triggers.md`, `steps/`, `agents/`, `skills/`, `scripts/`, `error_handling.md`, `observability.md`, `runbook.md`, `eval_scenarios.json`, `README.md`
- Mappatura: sequenze procedurali (P5) → step del DAG
- Vincoli: DAG no-cycle, state schema strict

### `orchestration`
- File: `supervisor.md`, `routing.md`, `registry.{md,json}`, `policies.md`, `observability.md`, `failure_modes.md`, `escalation.md`, `eval_scenarios.json`, `README.md`
- Mappatura: existing_components.json + KG → registry; principi di routing → rules; policies menzionate → policies.md
- **Precondition obbligatoria**: `existing_components.json` presente

### `wiki` (Obsidian)
- File: `MOC - <topic>.md`, `_Index.md`, `concepts/`, `examples/`, `frameworks/`, `procedures/`, `glossary/`, `_meta/{source,import-log}.md`, `README.md`
- Mappatura: 1 atomo del KG → 1 nota atomica (target 1:1)
- Cartella per categoria atomo
- Vincoli: wikilink integrity, frontmatter valido, slug consistency

### `custom`
- File OBBLIGATORI: `spec.md`, `coverage_map.md`, `README.md`
- File LIBERO: `artifact/...`
- Mappatura: dinamica, su misura
- Vincoli: spec.md ha sezioni minime obbligatorie; coverage_map onesta

## Algoritmo (pseudo)

```python
def apply_target_shape(target: str, kg: dict, user_answers: dict) -> dict[str, str]:
    """Mappa il KG sulla shape canonica del target. Ritorna dict path→content."""
    shape = load_shape_spec(target)  # da references/processes/<target>.md + schemas

    # 1. Verifica preconditions specifiche del target
    precond_issues = check_preconditions(shape, kg, user_answers)
    if precond_issues:
        return needs_user_input(precond_issues)

    # 2. Per ogni file canonico previsto, decidi se applicabile
    files_to_produce = {}
    for canonical_file in shape["canonical_files"]:
        if is_applicable(canonical_file, kg, user_answers):
            files_to_produce[canonical_file["path"]] = render_file(canonical_file, kg, user_answers)

    # 3. Map atoms → components
    mapping = map_atoms_to_components(kg["atoms"], shape["component_types"], user_answers)
    for component_path, atoms in mapping.items():
        files_to_produce[component_path] = render_component(atoms, component_path, kg)

    # 4. Wire references (per i target che hanno hierarchy interna: skill, workflow)
    if shape["has_internal_refs"]:
        files_to_produce = resolve_internal_refs(files_to_produce, shape)

    # 5. Validate against schema (preview check)
    issues = validate_against_schema(files_to_produce, shape["schema"])
    if issues:
        for issue in issues:
            files_to_produce = auto_fix_if_possible(files_to_produce, issue)
        # le issues rimaste vanno a self-critique

    return files_to_produce
```

## Validazione P9 (cosa controlla schema_validator.py)

```python
# Per ogni target, lo schema validator controlla
validation_checklist = {
    "files_exist": "Tutti i file canonici presenti?",
    "frontmatter_valid": "Frontmatter YAML parsabile e con campi richiesti?",
    "schema_compliant": "Output strutturato (json) valida contro JSON Schema?",
    "referential_integrity": "Ogni pointer interno risolve a un file esistente?",
    "target_custom_checks": "Check specifici del target (es. DAG no-cycle per workflow)",
}
```

## Anti-pattern

- **Shape ignorata**: builder produce file fuori dalla forma canonica → C3 fail.
- **Shape compilata meccanicamente**: builder riempie ogni placeholder anche dove non ha senso → output "vuoto" / fake.
- **Atomi non mappati**: cluster del KG che non finiscono in nessun componente del target → C1 fail (coverage).
- **Shape inventata**: builder inventa file extra non previsti → confonde lo schema validator e l'utente.

## Riferimenti

- "Shape" è ispirato al concetto di *Domain Shape* in Domain-Driven Design.
- La forma canonica per `skill` deriva dalla guida ufficiale `skill-creator` di Anthropic (in `references/external/skill-creator.md`).
