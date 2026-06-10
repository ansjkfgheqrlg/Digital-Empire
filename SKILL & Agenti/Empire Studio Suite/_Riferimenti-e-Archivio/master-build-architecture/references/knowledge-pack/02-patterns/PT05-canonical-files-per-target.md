# PT05 — Canonical Files per Target

> **Shape canonica**: Ogni tipo di output (target) ha una **lista fissa di file canonici** che DEVONO esistere per dirsi completo. Schema enforce questo. Builder produce esattamente questi file, non improvvisa. Esempio: un "agente" = 7 file specifici (agent.md, system_prompt.md, tools.md, playbook.md, failure_modes.md, eval_cases.json, README.md).

## Quando applicarlo

✅ **Applica se**:
- Skill produce artifact di tipo strutturato (non output narrativo libero)
- Vuoi che artifact sia "installabile" / "usabile" senza completion manuale
- Più builder potrebbero produrre lo stesso tipo di output

❌ **NON applicare se**:
- Output narrativo creativo (forzare file canonici uccide flexibility)
- Output è 1 file solo
- Skill custom one-off

## Perché funziona

### 1. Elimina ambiguità "è completo?"
"Questo agente è pronto per produzione?" → senza canonical files = giudizio. Con: "ha tutti i 7 file? sì/no". Binario, automatizzabile.

### 2. Codifica expertise di dominio
La lista canonica NON è arbitraria. È il risultato di esperienza: per avere un agente production-ready servono SP + tool spec + playbook + failure handling + eval + README. Mancano uno = scaffold.

### 3. Consistenza tra artifact dello stesso tipo
Tutti gli agenti hanno stessa struttura. Onboarding nuovo agente = aprire i 7 file noti. Senza canonical files: ogni agente ha layout diverso, friction enorme.

## Esempio dal nostro percorso

content-forge ha 8 target, ognuno con shape canonica fissata in `references/schemas/<target>.schema.json`:

| Target | File canonici |
|---|---|
| **doc** | document.md, glossary.md, faq.md, changelog.md, README.md |
| **agent** | agent.md, system_prompt.md, tools.md, playbook.md, failure_modes.md, eval_cases.json, README.md |
| **team** | topology.md, coordinator.md (se applicabile), agents/<role>.md (×N), communication_protocol.md, handoff_rules.md, failure_handling.md, shared_state.md, team_eval_cases.json, README.md |
| **skill** | SKILL.md, references/ (≥3), evals/evals.json, README.md, opzionali: agents/, scripts/, assets/ |
| **workflow** | flow.md, flow.mermaid, state.md, triggers.md, steps/, agents/, scripts/, error_handling.md, observability.md, runbook.md, eval_scenarios.json, README.md |
| **orchestration** | supervisor.md (condizionale), routing.md, registry.{md,json}, policies.md, observability.md, failure_modes.md, escalation.md, eval_scenarios.json, README.md |
| **wiki** | MOC - <topic>.md, _Index.md, concepts/, examples/, frameworks/, procedures/, glossary/, _meta/source.md, README.md |
| **custom** | spec.md, coverage_map.md, artifact/, README.md |

## Validation tramite schema v0.3

```python
# In agent.schema.json v0.3
{
  "required_files": {
    "type": "array",
    "const": ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
              "failure_modes.md", "eval_cases.json", "README.md"]
  },
  "agent_md_min_words": {"const": 400},
  "system_prompt_min_words": {"const": 500},
  "system_prompt_max_words": {"const": 1500},
  "playbook_min_conversations": {"const": 5},
  "failure_modes_min_count": {"const": 7},
  "eval_cases_min": {"const": 8},
  "eval_cases_max": {"const": 15}
}
```

Builder produce → C3 valida → se manca file canonico o content sotto soglia, FAIL bloccante.

## ➕ Esempio in altri domini

**Maven/Gradle project structure**: `src/main/java`, `src/test/java`, `pom.xml`, `README.md`. Canonical files convention.

**Python package**: `setup.py`/`pyproject.toml`, `<pkg>/__init__.py`, `tests/`, `README.md`, `LICENSE`. Standardizzato.

**npm package**: `package.json`, `index.js`, `README.md`, `LICENSE`. Stesso pattern.

**Django app structure**: `models.py`, `views.py`, `urls.py`, `templates/`, ecc. Convention-over-configuration.

## Anti-pattern correlato

**Free-form output**: ogni run produce file diversi a discrezione del builder. Risultato: artifact inconsistenti, utente deve indovinare struttura.

**Anti-pattern duale**: **Over-canonicalize** — forzare canonical files per output naturalmente non-strutturato (es. saggio creativo). Risultato: padding inutile, file vuoti.

## Trade-off

| Pro | Contro |
|---|---|
| Consistenza tra artifact | Meno flessibilità per casi edge |
| Validation automatizzabile | Schema da mantenere per ogni target |
| "Completo?" = check binario | Forzatura iniziale per piccoli artifact |
| Onboarding accelerato | Convention rigida può sembrare burocratica |

## Decision tree

```
Stai progettando un nuovo target?
├─ NO → riusa shape esistente
└─ SÌ → continua
   ├─ Avrà ≥3 file?
   │  ├─ NO → 1-2 file, convention informale, no schema
   │  └─ SÌ → continua
   ├─ Vuoi che tutti i builder producano stesso layout?
   │  ├─ NO → meno canonical, più optional
   │  └─ SÌ → strict canonical files
   │
   └─ Procedi:
      1. Lista files obbligatori (3-9 di solito)
      2. Lista files opzionali (con trigger)
      3. Content minimums per file principali (words, sections)
      4. references/schemas/<target>.schema.{md,json}
      5. references/processes/<target>.md (operativo per builder)
```

## Connessioni

- Necessario per: P06 (Shapes & Canonical Forms)
- Validato da: PT06 (Schema Tightening Loop)
- Combina con: P09 (Failure Modes First-Class) — failure_modes.md è file canonico
- Vedi anche: convention-over-configuration in Rails/Django

## Riferimenti

- Maven Standard Directory Layout
- Python Packaging User Guide
- Convention over Configuration (DHH, Rails)
- npm package.json spec
