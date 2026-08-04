# 🎉 `content-forge` — Skill pronta

> Deliverable finale di Phase 8 (packaging).
> Generata: 2026-05-24
> Versione: 1.0 (post-v5 architecture + Phase 4 Python implementation + Phase 7 real-world validation)

---

## 📦 Cosa hai qui

| File | Cosa è | Quando usarlo |
|---|---|---|
| **`content-forge.skill`** | Skill installabile (zip rinominato) | Quando l'ambiente supporta `.skill` (Claude Code skill loader, package_skill.py ecc.) |
| **`content-forge.zip`** | Stesso contenuto, formato neutro | Per distribuire/archiviare ovunque |
| **`content-forge/`** | Cartella espansa (estratta) | Per ispezionare la struttura senza scompattare |

Tutti e tre hanno **lo stesso contenuto**: 198 file, ~320 KB compressi, 1.2 MB espansi.

---

## 🚀 Installazione

### Opzione A — Claude Code (con `.skill` loader)

```bash
# Copia il .skill nella directory delle skill di Claude Code
cp content-forge.skill ~/.claude/skills/

# OPPURE se il loader vuole la cartella estratta:
unzip content-forge.skill -d ~/.claude/skills/
```

Verifica:
```
ls ~/.claude/skills/
# Dovrebbe mostrare: content-forge.skill   (o)   content-forge/
```

### Opzione B — Skill scoperta automaticamente da Claude Code

Se Claude Code monta skill da una directory specifica del progetto:

```bash
cd my-project
mkdir -p .claude/skills
unzip content-forge.zip -d .claude/skills/
```

Dopo questo, le frasi tipo "ho dei transcript da trasformare in...", "voglio fare una skill dal mio materiale" attiveranno automaticamente content-forge.

### Opzione C — Uso manuale (qualunque ambiente)

```bash
unzip content-forge.zip
cd content-forge
# Leggi SKILL.md per capire il pipeline, poi esegui:
python3 scripts/transcript_cleaner.py <source> --out cleaned.md
python3 scripts/atomizer.py cleaned.md --out chunks.json
# ... gli altri stage richiedono coordinamento LLM (vedi SKILL.md)
```

---

## 🎯 Cosa fa la skill (recap rapido)

Prende contenuto raw (transcript YouTube, workshop, articoli, anche **cartelle multi-file**) e lo trasforma in uno di 8 artefatti operativi:

| Target | Output |
|---|---|
| `doc` | Documento markdown ampliato e strutturato |
| `agent` | Agente AI completo (spec + SP + tools + playbook + eval) |
| `team` | Team multi-agente coordinato (topology + ruoli + handoff) |
| `skill` | Skill ufficiale Anthropic (meta: usa skill-creator) |
| `workflow` | Workflow eseguibile (DAG + stato + step + runbook) |
| `orchestration` | Orchestration layer (registry + routing + policies) |
| `wiki` | Note Obsidian atomiche con MOC e backlink integri |
| `custom` | Forma su misura (system prompt injection, knowledge pack RAG, ecc.) |

**Sempre** produce in mezzo un **Master Knowledge Document (MKD)** — il "documento perfetto" ampliato che diventa la base canonica per il target finale. È un bonus incluso in ogni run.

---

## ✅ Validazione (state of the art al packaging)

| Check | Risultato |
|---|---|
| File totali nella skill | 198 |
| Markdown | 138 |
| Python | 29 |
| JSON | 21 |
| **Pytest** | **56/56 passati** |
| **JSON Schemas** (Draft 2020-12) | **12/12 validi** |
| **YAML frontmatter** | **36/36 validi** |
| **Pointer integrity** | **OK** (2 falsi positivi documentati) |
| **Trigger eval heuristic** | **20/20** (100% accuracy su 20 query realistiche) |
| **Smoke test post-install** | **PASSATO** |
| **End-to-end Phase 7 su contenuto reale** | **PASSATO** (Manuale APSOC → skill `objection-handler`, coverage 94.4%) |

---

## 🐛 Bug trovati e fixati durante validazione

Lista trasparente di tutti i bug reali emersi durante Phase 6/7/8, fixati prima del package finale:

| Bug | Dove | Fix |
|---|---|---|
| Wikilink path-based non riconosciuti `[[folder/note]]` | `lib/obsidian.py` | Aggiunto path-based resolution |
| README.md sempre flagged come slug issue | `obsidian_packager.py` | Whitelisted |
| Coverage sottostima per contenuti italiani narrativi (72% falsamente FAIL) | `lib/atom_matcher.py` | Include title+extended in source terms + dedup + soglia 0.55 |
| qa-summary non normalizzava formato coverage-report.json | `package_target.py` | Riconosce sia `qa-summary` che `coverage-report` nativo |
| **Timestamp leading (`00:01:23 testo`) non rimossi** | `transcript_cleaner.py` | **Aggiunto `LEADING_TIMESTAMP_RE` + test regression** (scoperto in questo Phase 8) |

---

## 📚 Documentazione interna

Una volta installata/estratta, leggi (in ordine):

1. `SKILL.md` — kernel (225 righe, ≤500 raccomandato Anthropic)
2. `README.md` — overview
3. `ARCHITECTURE.md` — mappa navigabile completa
4. `agents/conductor.md` — system prompt del coordinatore principale
5. `references/processes/<target>.md` — ognuno degli 8 processi end-to-end
6. `assets/examples/` — esempi simulati per ogni target

---

## 🎁 Architettura (snapshot)

- **1 Conductor** (L1, il caller stesso)
- **12 specialist agents** (L2, spawnati via Task tool):
  - 5 Pipeline: ingestion, analyst (xN parallel), knowledge-graph, **MKD-builder** (sempre), target-advisor
  - 8 Builders: doc, agent, team, skill, workflow, orchestration, wiki, custom
  - 2 QA: coverage-verifier, schema-validator
  - 1 Meta: question-designer
- **9 Python scripts** (L3, deterministic operations):
  - transcript_cleaner, atomizer, coverage_check, no_summary_lint, length_check, schema_validator, obsidian_packager, package_target, validate_dag
- **5 lib modules** condivisi (kg_loader, atom_matcher, frontmatter, markdown_tools, obsidian)
- **14 test pytest** (56 test cases)
- **34 reference markdown** (stages, patterns, processes, schemas, conventions, external)
- **24 schema files** (12 entities × 2: md + json)
- **57 template files** (8 set per target)
- **31 example files** in `assets/examples/` (1 per target + shared)

---

## 🛣️ Storia delle versioni (skill-internal)

| Phase | Cosa | Esito |
|---|---|---|
| 0 | Planning (4 iterazioni, PLAN-v1..v4) | ✅ Architettura validata |
| 1 | Scaffolding completo | ✅ 187 file con audit |
| 2 | Espansione operativa (builders + patterns + stages) | ✅ Contenuti reali |
| 2.5 | Refactor v5: stage MKD obbligatorio + multi-source | ✅ |
| 4 | Implementazione Python vera + 55 test | ✅ Tutti gli script eseguibili |
| 5 | Rifinitura SKILL.md (description pushy, trigger eval) | ✅ 100% accuracy heuristic |
| 6 | Esempi end-to-end nei templates | ✅ 31 file di reference |
| 7 | Test end-to-end REALE su Manuale APSOC | ✅ Bug trovati + fixati |
| **8** | **Packaging finale `.skill`** | **✅ QUESTO DELIVERABLE** |

---

## 🤔 Note di onestà

**Cosa è validato per davvero:**
- Tutti gli script Python eseguono e producono output verificabili
- Il pipeline end-to-end è stato eseguito su contenuto reale (Manuale 4 APSOC)
- 56 test pytest catturano regressioni sui moduli core

**Cosa non è ancora validato:**
- Il triggering real-world della description (heuristic 100% ≠ Claude real triggering)
- Il comportamento dei builder LLM in produzione (simulati a mano in Phase 7)
- Compatibilità con tutti gli ambienti (Claude.ai mobile, ecc.)

**Cosa è "scaffold riconoscibile":**
- Gli esempi in `assets/examples/<target>/` sono simulati, non frutto di run real-time
- I JSON Schema sono validi ma alcuni campi sono ancora `additionalProperties: true` (rilassati)
- Alcune reference (es. patterns/) hanno spazio per più esempi

**Raccomandazione**: usa questa v1.0 in produzione su task reali e raccoglie feedback per v1.1 (auto-improvement via Phase 7 multi-iteration).

---

## 📞 Come continuare

Quando vuoi iterare:
1. Estrai `content-forge.zip` in una working directory
2. Usa la skill su task reali
3. Annota dove "funziona meno bene" (output di builder X poco utile, prompt utente Y non triggera)
4. Itera i system prompt corrispondenti (sono tutti in `agents/`)
5. Re-package con `python3 scripts/package_target.py <dir> --skill`

La skill è **auto-modificabile**: contiene gli strumenti per migliorarsi.
