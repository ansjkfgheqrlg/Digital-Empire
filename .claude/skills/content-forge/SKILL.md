---
name: content-forge
description: "Motore di forgia contenuti→artefatti di Digital Empire. Usa /forge <sorgente> per trasformare transcript, appunti, brief o intere cartelle in documenti espansi, agenti, team, skill ufficiali, workflow, orchestrazioni o wiki. MAI riassunti: espande sempre (ogni atomo diventa piu' ricco, invenzioni etichettate +). Produce sempre il Master Knowledge Document (MKD). Motore vendored in content-forge2.0/ (ADR-003 wrap; ADR-009 adozione)."
---

# Content-Forge — Motore di forgia (wrapper)

> **Reparto proprietario:** `FORGE-AGENT-SKILL` (nuovo reparto operativo, ADR-009) — sotto l'egida di
> `06b-FORGE` (L2.1 SKILL-WORKS / L2.2 AGENT-WORKS).
> **Motore (sorgente eseguibile):** `content-forge2.0/` alla root del repo — clonato da
> `gh repo clone ansjkfgheqrlg/content-forge2.0` (2026-07-20). Kernel completo: `content-forge2.0/SKILL.md`;
> agenti: `content-forge2.0/agents/` (conductor, pipeline, builders, qa, optimizers, meta, self-improvement);
> versioni pacchettizzate: `content-forge2.0/packaged-final*`. **ADR-003: si WRAPPA, non si riscrive.**

## Quando usarla (obbligo)
Ogni trasformazione sorgente grezza → artefatto operativo (documento espanso, agente, team, skill,
workflow, orchestrazione, wiki, knowledge pack RAG). Il reparto FORGE-AGENT-SKILL la usa come motore
ufficiale per creare NUOVI AGENTI e NUOVE SKILL dell'impero.

## Invarianti cardinali (dal motore — non negoziabili)
1. **Mai riassunti.** Espansione ≥ sorgente. 2. Invenzioni marcate `➕`.
3. Coverage atomi (100% nel MKD). 4. MKD sempre prodotto (stage 4).
5. Scaffolding interattivo PLAN → ASK → BUILD → CRITIQUE → ITERATE per target complessi.
6. Progressive disclosure: dettagli in `content-forge2.0/references/`.

## Invocazione
`/forge <file-o-cartella> [--target=agent|team|skill|workflow|orchestration|wiki|doc|custom] [--name=slug] [--recursive]`
Comfort zone: file 500-200k parole; cartella 1-30 file / ≤500k parole. Oltre → split in più run.

## Adattamenti Digital Empire
- Output agenti/skill devono rispettare lo standard impero: **7 file canonici** (spec, system-prompt,
  tools, playbook, evals, failure-modes, memory) + intestazione ADR-008 (proprietario/controllore/origine/governo)
  → registrazione in `company/REGISTRO-IMPRESA.md` + `skills-map.yaml`.
- Memoria: ogni produzione apre checkpoint in `company/Memory/checkpoints/` (memory-first, ADR-002).
