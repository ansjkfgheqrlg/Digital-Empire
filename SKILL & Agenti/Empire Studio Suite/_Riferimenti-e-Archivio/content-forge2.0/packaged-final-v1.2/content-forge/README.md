# `content-forge`

Skill ufficiale Anthropic (formato `skill-creator`) per **trasformare contenuto testuale grezzo in artefatti operativi di alto valore**.

> Comando: `/forge`
> Stato: **Phase 1 — Architecture** completata. Implementazione in corso.

---

## Cosa fa

Prende in input contenuto disordinato (transcript YouTube, workshop, articoli, brief) e produce — non riassumendo, ma **ampliando** — uno tra 8 target:

| Target | Output |
|---|---|
| `doc` | Documento markdown completo, ampliato e strutturato (TOC, esempi, schemi, glossario, FAQ) |
| `agent` | Agente AI operativo (spec + system prompt + tools + playbook + eval cases) |
| `team` | Team multi-agente coordinato (topologia + N agenti + handoff + failure handling) |
| `skill` | Nuova skill Anthropic ufficiale (meta — usa skill-creator) |
| `workflow` | Workflow end-to-end (DAG con step, stato, trigger, error handling, runbook) |
| `orchestration` | Orchestration layer (supervisor + registry + routing + policies) |
| `wiki` | Note Obsidian atomiche con MOC e wikilink integri (second brain) |
| `custom` | Forma custom (escape hatch — system prompt injection, config, knowledge pack) |

## Principi non negoziabili

1. **Mai riassunti.** L'output rispetta o supera la lunghezza del sorgente.
2. **Mai invenzione di fatti.** Tutto ciò che Forge genera (esempi propri, schemi, controesempi) è etichettato con `➕`.
3. **Coverage degli atomi misurabile.** Soglia per target (default 90%+), verificata da script.
4. **Interactive scaffolding** per target complessi: PLAN → ASK → ARCH → BUILD → CRITIQUE → ITERATE.

## Architettura (sintesi)

- **1 Conductor** (L1, te) coordina via Task tool
- **11 specialist agents** (L2): 4 pipeline + 8 builder + 2 QA + 1 question designer
- **8 script** Python + 5 moduli lib + 13 test
- **34 reference markdown** (stages, patterns, processes, conventions, external)
- **14 JSON Schema** (7 entities × md + json)
- **57 template** di scaffolding (8 set, uno per target)

Vedi `ARCHITECTURE.md` per la mappa navigabile completa.

## Come è organizzato il repo

- `SKILL.md` — kernel di routing
- `agents/` — system prompt di ogni agente
- `references/` — conoscenza on-demand (stages, patterns, processes, schemas, conventions)
- `assets/templates/` — scaffolding per gli output
- `scripts/` — script Python + lib + test
- `evals/evals.json` — test cases
- `PLAN-v4.md` — piano e decisioni di design
- `ARCHITECTURE.md` — mappa file

## Come è stata costruita (per chi vuole replicare)

1. **PLAN v1** — primo abbozzo
2. **PLAN v2** — aggiunto inventario multi-agente
3. **PLAN v3** — aggiunti processi end-to-end per ogni target (`references/processes/*.md`)
4. **PLAN v4** — policy "markdown + python embedded"; schemas dual file; `scripts/lib/`
5. **Phase 1 (this)** — scheletro completo di ~150 file
6. **Phase 2-8** — popolamento progressivo (vedi `ARCHITECTURE.md` §Roadmap)
