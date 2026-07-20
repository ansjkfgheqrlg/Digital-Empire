# 📐 PLAN v6 — Depth Architecture (Phase 9)

> **Cosa cambia rispetto a v5:**
> 1. ➕ **Pipeline a 9 stage** (era 8): nuovo Stage 7 — Depth & Optimization Pass
> 2. ➕ **5 nuovi agenti optimizer** in `agents/optimizers/` (team Ox)
> 3. ➕ **Schema tightening**: JSON Schema più stringenti per agent/skill/team (forza output ricco)
> 4. ➕ **Builder improvements**: B2-B6 ora "depth-aware", scrivono output completi fin dall'inizio
> 5. ➕ **C3 più rigoroso**: blocca skill con <3 reference, agenti senza playbook, ecc.
> 6. ➕ **`humanizer-agent` (O4)** condizionale via tag KG (human-facing content)
> 7. ➕ **`formula-validator-agent` (O5)** — verifica framework/formule del sorgente

---

## 0. Perché v6 (causa di radice)

L'utente ha eseguito 2 test reali della skill v1.0 e ha trovato 3 problemi convergenti:

### Test #1 — `beast-preventivi` (target=skill)
- Output: skill funzionante, 8 file, ma **0 agenti interni**
- Problema: skill complesse beneficiano di agenti specializzati (operativi, verificatori, formulari, humanizer)
- Severity: ⚠️ medio (manca un layer di qualità)

### Test #2 — `copy-workflow` (target=orchestration)
- Output: 25 file, ottima architettura macro
- Problema 1: **6 sub-skill con UN SOLO `.md` ciascuna** (no reference/, scripts/, evals/)
- Problema 2: **8 agenti tutti corti**, mai con tutti i 7 file canonici
- Severity: 🔥 alto (output magro = skill installabile ma poco usabile)

### Diagnosi: 3 strati di causa

```
Strato 1 — UPSTREAM (la causa)
  └─ I builder producono "scaffold minimi viable" invece di output rich
     ↓
Strato 2 — VALIDATION GAP (cosa lo lascia passare)
  └─ Schema JSON troppo permissivi (additionalProperties: true, required minimi)
  └─ C3 non blocca skill con 1 file, agenti senza playbook
     ↓
Strato 3 — DOWNSTREAM (cosa ottieni)
  └─ Output sintatticamente valido ma operativamente magro
```

v6 attacca tutti e 3 gli strati insieme.

---

## 1. Pipeline a 9 stage (nuovo Stage 7)

```
[Stage 1] Ingestion                       (invariato)
[Stage 2] Deep Analysis                   (invariato)
[Stage 3] Knowledge Graph                 (invariato)
[Stage 4] 🌟 MASTER KNOWLEDGE DOCUMENT    (invariato — sempre prodotto)
[Stage 5] Target Selection                (invariato)
[Stage 6] Interactive Build (Bx → DRAFT)  (BUILDER MIGLIORATI, vedi §4)
[Stage 7] 🆕 DEPTH & OPTIMIZATION PASS    (team Ox, vedi §2)
[Stage 8] External QA (C1 + C3+)          (C3 PIÙ RIGOROSO, vedi §5)
[Stage 9] Packaging                       (invariato)
```

**Stage 7 è OBBLIGATORIO** per i target che producono artefatti contenenti sub-componenti (skill, team, workflow, orchestration). Opzionale (skip) per `doc`/`wiki`/`custom` se l'utente preferisce velocità.

---

## 2. Team Ox — 5 agenti optimizer

Tutti in `agents/optimizers/`, governati da un **Depth Conductor** (estensione del Conductor principale).

### O1 — `skill-depth-agent` 🎯

**Scope**: Garantire che ogni skill prodotta (anche sub-skill nested in workflow/orchestration) abbia struttura completa.

**Cosa fa**:
- Per ogni `SKILL.md` trovato nell'output del builder:
  1. Verifica struttura: `references/`, `scripts/` (se serve), `evals/`, `assets/`
  2. Se mancano `references/` o < 3 file in essa → **espande** generando 3-7 reference reali
  3. Se la skill ha "procedural content" → suggerisce script Python utili e li genera
  4. Aggiorna routing in `SKILL.md` per puntare ai nuovi file

**Quando attivo**: Sempre se output contiene ≥1 skill (root o nested).

**Output**: Modifiche in-place + report `o1-depth-report.json`.

### O2 — `agent-depth-agent` 🤖

**Scope**: Per ogni agente prodotto, verifica i 7 file canonici. Se mancano, li crea con contenuto reale.

**File canonici obbligatori per ogni agente**:
1. `agent.md` — spec
2. `system_prompt.md` — SP pronto
3. `tools.md` — tool con schema
4. `playbook.md` — 5-10 conversazioni
5. `failure_modes.md` — 7+ failure mode
6. `eval_cases.json` — 8-15 casi
7. `README.md` — installazione/uso

**Cosa fa**:
- Per ogni agente trovato (in `agents/` root o nested):
  1. Verifica presenza file
  2. Se manca `playbook.md` → genera 5-10 conversazioni realistiche basate su SP + dominio
  3. Se manca `failure_modes.md` → genera 7+ failure con prevenzione/rilevamento/recupero
  4. Se manca `eval_cases.json` → genera 8-15 casi bilanciati (happy/edge/failure/constraint)
  5. Se manca `tools.md` ma SP cita tool → estrae e formalizza
  6. Se file presente ma magro (<200 parole) → arricchisce

**Quando attivo**: Sempre se output contiene ≥1 agente.

### O3 — `reference-expander-agent` 📚

**Scope**: Trasforma reference "scheletriche" (50-100 righe) in operative (200-400 righe).

**Cosa fa**:
- Per ogni file in `references/`:
  1. Conta righe e measure depth
  2. Se <150 righe E non è un index/TOC → **arricchisce**:
     - Aggiunge 1-2 esempi reali per concept
     - Aggiunge schema/diagramma mermaid o ASCII se applicabile
     - Aggiunge anti-pattern correlato
     - Aggiunge snippet di codice se è tecnico
     - Aggiunge cross-reference a altri reference
  3. Lascia in pace se già denso (>200 righe) o se è un index legittimamente breve

**Quando attivo**: Sempre.

### O4 — `humanizer-agent` 💬

**Scope**: Rende l'output **più umano**, meno LLM-speak.

**Anti-pattern LLM-speak da eliminare**:
- "It's important to note that..."
- "In summary..." / "In conclusione..."
- Liste con bullet per qualunque cosa (anche dove la prosa flow è meglio)
- "Let's dive into..."
- "Stay tuned for..."
- Apertura con "Welcome to..."
- Ripetizione formulaica della stessa struttura per ogni sezione
- Eccesso di "powerful", "leverage", "robust", "comprehensive"

**Cosa fa**:
- Rilegge ogni file di testo e:
  1. Identifica frasi/aperture LLM-speak
  2. Riscrive in stile più diretto, vario, naturale
  3. Mantiene il significato 100% (no perdita di info)
  4. Adatta al "voice" del sorgente (informale se il sorgente è informale, tecnico se tecnico)
  5. Riduce ripetitività strutturale tra sezioni

**Quando attivo**: **Condizionale via tag KG**.

```python
# Logica di attivazione
def humanizer_should_run(kg: dict) -> bool:
    """True se l'output è 'human-facing' (escluso: code, config, validator)."""
    tags = set()
    for atom in kg.get("atoms", []):
        tags.update(atom.get("tags", []))
    EXCLUSION_TAGS = {"code-only", "config", "validator", "schema-only"}
    return not (tags & EXCLUSION_TAGS)
```

> Decisione utente Phase 9: humanizer **attivo per default** salvo tag espliciti di esclusione → maximum coverage.

### O5 — `formula-validator-agent` 🧮

**Scope**: Verifica che le formule/framework del sorgente siano applicate **correttamente e completamente** nell'output.

**Cosa fa**:
1. Estrae dal KG tutti gli atomi `category: framework` o con tag `formula`, `framework`, `method`
2. Per ognuna identifica la **shape canonica** (es. CPB = Claim+Proof+Benefit; APSOC = Attention+Problem+Solution+Objections+CTA; AIDA = Attention+Interest+Desire+Action)
3. Cerca le applicazioni della formula nell'output
4. Verifica che TUTTI i pezzi della formula siano presenti
5. Se manca un pezzo → segnala o (se trivial) aggiunge

**Esempio sul Test #1 (preventivi)**:
- KG identifica formula "Preventivo perfetto in 5 step" (struttura+brand+contenuti+metodo+prezzo)
- Output skill cita solo 4 step → O5 segnala il pezzo mancante (es. metodo di lavoro)

**Quando attivo**: Sempre se KG contiene ≥1 atomo `framework`.

---

## 3. Spawn order del team Ox (Depth Conductor)

```
Stage 6 → builder Bx produce DRAFT
              ↓
        Depth Conductor (sub-router)
              ↓
       ┌─────────────────────┐
       │ Spawn parallelo:    │
       │   O1 skill-depth    │  (lavora su SKILL.md nested)
       │   O2 agent-depth    │  (lavora su agenti)
       └─────────────────────┘
              ↓
       O3 reference-expander  (arricchisce reference appena creati da O1+O2)
              ↓
       O5 formula-validator   (valida formule sui contenuti finali)
              ↓
       O4 humanizer           (ultimo: humanizza output ormai stabile)
              ↓
Stage 8 → C1 + C3 (QA esterna)
```

**Razionale ordine**:
- O1+O2 paralleli: lavorano su tipi di file diversi (skill vs agent), no conflitto
- O3 dopo perché molti dei reference che arricchirà sono stati creati da O1+O2
- O5 dopo O3: valida formule sul contenuto finale arricchito
- O4 ultimo: humanizza tutto in una passata coerente (no rilavoro)

---

## 4. Builder improvements (Strato 1)

Aggiungo nei system prompt dei builder Bx queste regole:

### B2 `agent-builder-agent`
- Self-critique aggiunge check: "ho prodotto TUTTI i 7 file canonici? Ognuno ha content reale (>200 parole), non placeholder?"
- Se non riesce a generare tutti i 7 → **chiede a O2 di completare** invece di consegnare scaffold

### B3 `team-builder-agent`
- Ogni agente del team prodotto deve essere completo (delegando a O2 in Stage 7 se necessario)
- Non più "scaffold minimi" per agenti del team — devono essere come singoli `agent` target

### B4 `skill-builder-agent`
- Ogni skill (anche sub-skill se nested) DEVE avere:
  - SKILL.md
  - references/ con ≥3 file (delegando a O1 se necessario)
  - evals/ con ≥4 cases
  - assets/ se ha forme canoniche
- Se non riesce → produce SCAFFOLD + flag esplicito "TODO O1: expand to full skill"

### B5 `workflow-builder-agent` & B6 `orchestration-builder-agent`
- Quando producono workflow/orchestration con **skill/agent nested**, mettono **flag espliciti** per O1/O2 nel manifest
- Esempio: nel workflow manifest "step-03 uses agent X → spawn O2 in Stage 7 to expand X"

---

## 5. Schema tightening (Strato 2)

### `agent.schema.json` v0.3 (era v0.2 permissiva)

```python
# NUOVO — required stringente
"required": ["required_files", "agent_md_complete", "system_prompt_quality",
             "playbook_count", "failure_modes_count", "eval_cases_count"]

# Constraints reali
"properties": {
    "required_files": {
        "type": "array",
        "const": ["agent.md", "system_prompt.md", "tools.md", "playbook.md",
                  "failure_modes.md", "eval_cases.json", "README.md"]
    },
    "agent_md_min_words": {"const": 400},          # was 0
    "system_prompt_min_words": {"const": 500},     # was 0
    "system_prompt_max_words": {"const": 1500},    # invariato
    "playbook_min_conversations": {"const": 5},    # was missing
    "failure_modes_min_count": {"const": 7},       # was missing
    "eval_cases_min": {"const": 8},
    "eval_cases_max": {"const": 15},
}
# additionalProperties: False  ← era True
```

### `skill.schema.json` v0.3

```python
# NUOVO
"required": ["SKILL_md", "references", "evals"]

"properties": {
    "skill_md_max_lines": {"const": 500},
    "skill_md_min_lines": {"const": 80},        # nuovo: non troppo magro
    "references_min_files": {"const": 3},        # NUOVO — questo è il fix critico
    "references_min_total_lines": {"const": 300},
    "evals_min_count": {"const": 4},
    "frontmatter_required_keys": {"const": ["name", "description"]},
    "description_min_chars": {"const": 800},
    "description_max_chars": {"const": 2500},
    "description_pushy_markers_min": {"const": 3},
}
```

### `team.schema.json` v0.3

```python
# NUOVO
"properties": {
    "agents_min_files_each": {
        "const": 5,
        "description": "Ogni agente del team deve avere ≥5 dei 7 file canonici"
    },
    "agents_min_count": {"const": 2},
    "topology_md_required": {"const": True},
    "handoff_rules_required": {"const": True},
    "failure_handling_min_modes": {"const": 5},
}
```

### `workflow.schema.json` e `orchestration.schema.json` v0.3
- Workflow: ogni step di tipo `agent` deve linkare ad agente che rispetta `agent.schema.v0.3`
- Orchestration: ogni componente nel registry deve essere un artifact valido (skill/agent/team)

---

## 6. C3 (target-schema-validator-agent) potenziato

Aggiungo nel SP di C3 questi check **bloccanti** (oltre a quelli esistenti):

```python
new_blocking_checks = [
    "every_skill_has_min_3_references",
    "every_agent_has_min_5_canonical_files",
    "every_agent_has_playbook_with_min_5_convs",
    "every_agent_has_failure_modes_with_min_7",
    "every_agent_md_min_400_words",
    "every_system_prompt_min_500_words",
    "every_workflow_step_agent_links_to_valid_agent",
    "every_orchestration_component_in_registry_exists",
]
```

Se uno fallisce → C3 ritorna FAIL → Conductor itera Stage 6 (con feedback specifico al builder) o spawn diretto O1/O2.

---

## 7. Inventario file Phase 9 (cosa aggiungo/modifico)

| Categoria | Action | Conteggio |
|---|---|---|
| Nuovi agenti optimizer | CREATE in `agents/optimizers/` | +5 file |
| Nuovo stage doc | CREATE `references/stages/07-depth-optimization.md` + RENAME 07→08, 08→09 | +1 nuovo, 2 rename |
| Schema updates | MODIFY agent, skill, team, workflow, orchestration .schema.json | 5 file aggiornati |
| Builder updates | MODIFY B2-B6 system prompts (sezione self-critique) | 5 file aggiornati |
| C3 update | MODIFY `target-schema-validator-agent.md` | 1 file aggiornato |
| Conductor update | MODIFY `conductor.md` (pipeline 9-stage + Depth Conductor logic) | 1 file aggiornato |
| SKILL.md update | MODIFY kernel (8→9 stage) | 1 file aggiornato |
| ARCHITECTURE.md update | MODIFY mappa | 1 file aggiornato |
| Regression test outputs | CREATE in `phase9-regression/` | 2 test runs (pre+post v6) |

**Totale**: 5 nuovi file + ~15 file aggiornati + workspace test.

---

## 8. Sub-phase execution plan

| Sub-phase | Cosa | Stima |
|---|---|---|
| **9.1** | PLAN-v6 (questo) | ✅ fatto |
| **9.2** | 5 nuovi agenti optimizer in `agents/optimizers/` | 1h |
| **9.3** | Nuovo `references/stages/07-depth-optimization.md` + rename | 30min |
| **9.4** | Update `agents/conductor.md` per pipeline 9-stage | 30min |
| **9.5** | Schema tightening (5 schemi) | 1h |
| **9.6** | Update builder agents (B2-B6) | 1h |
| **9.7** | Update C3 con check stringenti + nuovi test pytest | 30min |
| **9.8** | Regression test reale su sorgente preventivi (test#1 + test#2 con target diversi) | 1-2h |
| **9.9** | Re-package v1.1 + HANDOFF aggiornato | 30min |

**Totale stimato**: 6-8 ore distribuite.

---

## 9. Test di successo (definito prima di partire)

Per dichiarare Phase 9 PASSED, dopo sub-phase 9.8 dobbiamo ottenere:

### Test #1 — `beast-preventivi v1.1` vs v1.0
- ✅ Skill prodotta contiene almeno 2-3 agenti (operativo + verificatore minimum)
- ✅ Ogni agente ha tutti i 7 file canonici
- ✅ Reference esistenti ora hanno >150 righe ognuna
- ✅ Schema validator C3 passa
- ✅ Coverage ≥90%

### Test #2 — `preventivi-orchestration v1.1` vs `copy-workflow v1.0`
- ✅ Sub-skill hanno minimo 3 reference + evals/ ognuna (non più 1 file solo)
- ✅ Tutti gli agenti del workflow hanno minimo 5/7 file canonici
- ✅ Reference espanse (>200 righe avg)
- ✅ Formula del sorgente (preventivo perfetto) tracciata e validata
- ✅ Output "humanizzato" (no "It's important to note", aperture LLM-speak)
- ✅ Schema validator C3 passa

Se questi target sono raggiunti → Phase 9 chiusa, packaging v1.1.

---

## 10. Decisioni ratificate

| Decisione | Valore |
|---|---|
| Approccio | ✅ Tutti e 3 gli strati (optimizer + schema + builder) |
| Optimizer team | ✅ Tutti e 5 (O1-O5) |
| Humanizer scope | ✅ Condizionale via tag KG (whitelist con esclusioni esplicite) |
| Regression test | ✅ Su sorgente preventivi reale (entrambi i target con stesso input, simulazione realistica) |
| Pipeline | ✅ 9 stage (era 8) |
| Stage 7 obbligatorio | ✅ Sì per skill/team/workflow/orchestration. Opzionale per doc/wiki/custom |
