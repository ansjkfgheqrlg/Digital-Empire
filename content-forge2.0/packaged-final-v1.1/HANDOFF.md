# 🎉 `content-forge` v1.1 — Phase 9 Depth Architecture

> Deliverable di Phase 9. Generata: 2026-05-26.
> Risolve i 3 bug reali identificati dall'utente nei test di v1.0.

---

## 📦 Cosa hai qui

| File | Cosa è | Dimensione |
|---|---|---|
| **`content-forge-v1.1.skill`** | Skill installabile (zip rinominato) — **207 file** | 364 KB |
| **`content-forge-v1.1.zip`** | Stesso contenuto, formato neutro | 364 KB |
| **`content-forge/`** | Cartella espansa per ispezione | 1.4 MB |

Stesso contenuto in tutti e 3, solo formato diverso.

---

## 🆕 Cosa cambia rispetto a v1.0

Phase 9 risolve i 3 bug reali che hai trovato nei tuoi 2 test:

### Bug 1: Skill complesse senza agenti interni (`beast-preventivi`)

**Causa**: nessun check forzava l'aggiunta di agenti per skill multi-stage.

**Fix v1.1**:
- Nuovo check `complex-skill-no-agents` in `schema_validator.py` (rileva skill con ≥3 stages senza agenti)
- Nuovo agente `O1 skill-depth-agent` che espande skill nested

### Bug 2: Sub-skill nested con UN SOLO file (`copy-workflow`)

**Causa**: schema permissivo, builder produceva scaffold accettati.

**Fix v1.1**:
- `skill.schema.v0.3` ora richiede `references_min_files: 3` (era senza minimo)
- C3 fallisce se sub-skill ha <3 reference
- O1 espande automaticamente in Stage 7

### Bug 3: Agenti con file canonici mancanti

**Causa**: schema agent permissivo, builder produceva agenti con 2-3 file invece di 7.

**Fix v1.1**:
- `agent.schema.v0.3` richiede tutti i 7 file canonici + min content (agent.md ≥400w, SP ≥500w, playbook ≥5 conv, failure_modes ≥7)
- Nuovo agente `O2 agent-depth-agent` che completa agenti incompleti
- C3 fallisce se agente <5/7 file o content sotto soglia

---

## 🏗️ Architettura v1.1 (9 stage)

```
[Stage 1] Ingestion             A1
[Stage 2] Deep Analysis         A2 (xN parallel)
[Stage 3] Knowledge Graph       A3
[Stage 4] 🌟 MASTER KNOWLEDGE   A5  (sempre)
[Stage 5] Target Selection      A4
[Stage 6] Interactive Build     D1+Bx → DRAFT
[Stage 7] 🆕 DEPTH PASS         Team Ox (NUOVO)
              ├─ O1 skill-depth (parallel)
              ├─ O2 agent-depth (parallel)
              ├─ O3 reference-expander
              ├─ O5 formula-validator (condizionale)
              └─ O4 humanizer (condizionale)
[Stage 8] External QA           C1+C3 (più stringenti)
[Stage 9] Packaging             scripts/
```

### Team Ox (5 nuovi optimizer)

| Agente | Cosa fa | Quando attivo |
|---|---|---|
| **O1 skill-depth-agent** | Espande skill nested magre (≥3 references, evals, optional scripts) | Sempre se output contiene skill |
| **O2 agent-depth-agent** | Completa agenti con 7/7 file canonici | Sempre se output contiene agenti |
| **O3 reference-expander-agent** | Arricchisce reference scheletriche (150→300 righe avg) | Sempre |
| **O4 humanizer-agent** | Elimina LLM-speak (no "leverage", "comprehensive", ecc.) | Condizionale via tag KG (default: ON per output human-facing) |
| **O5 formula-validator-agent** | Verifica che formule del sorgente (APSOC, CPB, AIDA) siano applicate completamente | Condizionale (solo se KG contiene framework) |

---

## ✅ Regression test results

Eseguito su sorgente reale fornito dall'utente (7 transcript YouTube + 1 guida = 20k parole su come fare preventivi).

### Test #1 — target=skill (replica `beast-preventivi`)

| Metrica | v1.0 baseline | v1.1 Phase 9 |
|---|---|---|
| File totali | 12 | 40 (**+28**) |
| Agenti interni | **0** ❌ | **4** (discovery + pricing + qa + humanizer) ✅ |
| Schema validator | WARN | **PASS** |
| Phase 9 issues | 1 | **0** |

### Test #2 — target=orchestration (replica `copy-workflow`)

| Metrica | v1.0 baseline | v1.1 Phase 9 |
|---|---|---|
| File totali | 24 | 101 (**+77**) |
| Files per sub-skill (6 skills) | 1 ❌ | **5** ✅ |
| Files per agent (8 agents) | 2/7 ❌ | **7/7** ✅ |
| Schema validator | FAIL (31 errori) | **PASS** (0 errori) |
| Phase 9 issues | 31 | **0** |

---

## 🐛 Bug trovati durante Phase 9 implementation

Lista trasparente dei bug REALI fixati durante il regression test:

| Bug | Dove | Fix |
|---|---|---|
| **Schema validator non rilevava agenti con nome custom** (es. `briefing-analyst.md`) | `scripts/schema_validator.py` `run_phase9_checks` | Heuristic 3 estesa: qualunque file `.md` dentro `agents/` folder non-companion è un agente |
| **Schema validator non rilevava agenti in convention single-file con companions** (es. `discovery-agent.md` + `discovery-agent.system_prompt.md`) | `scripts/schema_validator.py` | Nuova funzione `check_agent_canonical_files_single_file` che cerca companion via suffix matching |
| **Filtro path `phase` troppo permissivo** (matchava `pytest-1/test_run_phase9_checks_...`) | `scripts/schema_validator.py` | Regex più stringente: `r"/(phase\d+-(run|regression)|packaged-final)/"` |
| **Mancava check `complex-skill-no-agents`** (skill multi-stage senza agenti passava silently) | `scripts/schema_validator.py` | Nuova funzione `check_complex_skill_has_agents` con heuristic (stages ≥3 o processes ≥2) |

Tutti i fix sono **stati validati con test pytest dedicati** (13 nuovi test in `test_phase9_checks.py`).

---

## 📊 Stato finale validato

```
✅ 206 file nella skill (esclusi test e cache)
✅ 22/22 JSON validi
✅ 30/30 Python compila (incluso schema_validator aggiornato)
✅ 41/41 YAML frontmatter validi
✅ 12/12 JSON Schemas Draft 2020-12 validi (5 schemi v0.3, 7 v0.2/0.1 legacy)
✅ 69/69 pytest passati (+13 nuovi test Phase 9)
✅ Regression test reale: 2 test su sorgente preventivi PASSANO
```

---

## 🚀 Come usarla

### Installazione

```bash
# Estrai e installa
unzip content-forge-v1.1.skill -d ~/.claude/skills/
# o equivalente per il tuo ambiente
```

### Verifica che funzioni

Dopo installazione, chiedi a Claude qualcosa come:

> "Ho dei transcript YouTube sui preventivi, voglio farne una skill ufficiale per Claude Code"

→ La skill dovrebbe triggerare e iniziare il pipeline 9-stage.

### Cosa aspettarti che sia diverso da v1.0

**Quando il pipeline finisce:**

1. **Skill output (target=skill)** ora include `agents/` con almeno 2-3 agenti specialisti (operativo, QA, humanizer)
2. **Workflow/Orchestration output** ora include sub-skill **complete** (con references/, evals/), non scaffold
3. **Agenti generati** hanno tutti i 7 file canonici (agent.md ≥400w, SP ≥500w, playbook con ≥5 conv, failure_modes con ≥7 entry, eval_cases ≥8, tools.md, README.md)
4. **Output testuale più umano** (no "leverage", "comprehensive", "In summary")
5. **Coverage delle formule** del sorgente garantita

### Trade-off

Phase 9 ha un **costo**: il pipeline è 2-3x più lungo (Stage 7 aggiunge 5-15 min per artifact medio). In cambio ottieni output **production-ready** invece di scaffold da rifinire a mano.

---

## 📚 Documentazione interna

Una volta installata, leggi (in ordine):

1. `SKILL.md` (236 righe, ≤500 raccomandato)
2. `ARCHITECTURE.md` — mappa completa
3. `PLAN-v6.md` — razionale Phase 9 in dettaglio
4. `references/stages/07-depth-optimization.md` — nuovo stage
5. `agents/optimizers/*.md` — i 5 nuovi agenti

---

## 🛣️ Storia completa delle versioni

| Phase | Cosa | Esito |
|---|---|---|
| 0 | PLAN v1-v5 (5 iterazioni) | ✅ |
| 1-2 | Scaffold + builder + pattern | ✅ |
| 4 | Implementazione Python | ✅ (56 test) |
| 5 | SKILL.md rifinitura | ✅ |
| 6 | Esempi end-to-end | ✅ |
| 7 | Test reale Manuale APSOC | ✅ (2 bug trovati) |
| 8 | Packaging .skill v1.0 | ✅ |
| **9** | **Depth Architecture (questa)** | **✅ 69 test, 4 bug trovati e fixati, regression test PASS** |

---

## 🎯 Quando aspettarsi v1.2

Usa v1.1 per qualche settimana su task reali. Annota:
- Cosa funziona meglio di v1.0 (dovrebbe essere quasi tutto)
- Cosa ancora funziona meno bene
- Nuovi failure mode che emergono

Quando hai 3-5 osservazioni concrete → Phase 10 (probabilmente focus su: tool real per O4 humanizer, multi-language support più rigoroso, cost optimization per O3).
