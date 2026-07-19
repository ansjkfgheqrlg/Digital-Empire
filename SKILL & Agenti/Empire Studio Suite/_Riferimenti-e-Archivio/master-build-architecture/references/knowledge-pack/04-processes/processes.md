# Processi — 7 Processi Operativi

> **Fonte:** Knowledge Pack 04-processes + estrazioni da Content-Forge pipeline, Context-Engineering-Advisor cycle, Ruflo swarm.

## PR01 — Iterative Plan Creation
**Obiettivo:** Creare piani iterativi (PLAN-v1 → vN) con feedback loop.
**Steps:**
1. Vision/scope iniziale
2. PLAN-v1 (rough)
3. ASK (domande adattive, PT04)
4. BUILD (draft artifacts)
5. CRITIQUE (self + human)
6. PLAN-vN (iterare fino a soddisfazione)
**Quando:** Sempre, per ogni progetto/artefatto.
**Gate:** Ogni PLAN-vN deve avere: vision, scope, steps, agents, memory, validation.

---

## PR02 — Content-Forge Pipeline
**Obiettivo:** Pipeline 9-stadi per trasformazione contenuto (grezzo → confezionato).
**Steps:**
1. Ingestion (A1 — multi-source)
2. Analysis (A2 — principle extraction)
3. Knowledge Graph (A3 — traceability)
4. MKD Production (A5 — master document)
5. Build (B1-B8 — artifacts)
6. Depth Pass (O1-O5 — optimizers)
7. Self-Improvement (SI — failure detection)
8. Validation (C1-C3 — QA)
9. Packaging (PR07 — release)
**Quando:** Per ogni contenuto da trasformare.

---

## PR03 — Agent Construction
**Obiettivo:** Costruire agenti con 7 file canonici (PT05).
**Steps:**
1. Definire schema (target type)
2. Creare spec.md (ruolo, missione)
3. Creare system-prompt.md (invarianti, handoff)
4. Creare tools.md (strumenti, implementazione)
5. Creare playbook.md (steps, esempi)
6. Creare evals.md (test cases, benchmark)
7. Creare failure-modes.md (tabella, recovery)
8. Creare memory.md (mandate, shared_state, update protocol)
**Quando:** Per ogni nuovo agente.
**Gate:** 7 file completi, ≥5 entry in failure-modes, cross-refs a SI.

---

## PR04 — Validation Cycle
**Obiettivo:** Validare ogni output contro schema e coverage.
**Steps:**
1. Schema check (target-schema-validator)
2. Coverage check (coverage-verifier)
3. FM validation (failure-mode-validator)
4. Fix issues
5. Re-validate
**Quando:** Dopo ogni build batch.
**Gate:** 100% compliant su tutti e 3 i validator.

---

## PR05 — Memory Lifecycle
**Obiettivo:** Gestire memoria persistente (P10).
**Steps:**
1. Bootstrap (creare structure: checkpoints/, decisions/, sessions/, plans/, architectures/, MEMORY-INDEX.md)
2. CP/DEC dopo OGNI step significativo
3. INDEX update (append a MEMORY-INDEX.md)
4. Sync (tra top memory e embedded skill memory)
5. Consolidate (a fine sessione, creare RETRO)
**Quando:** Sempre, memory-first.
**Gate:** CP creato dopo ogni azione, INDEX aggiornato, sync eseguito.

---

## PR06 — Self-Improvement Cycle
**Obiettivo:** Auto-miglioramento continuo (P10/PT07).
**Steps:**
1. Failure detect (failure-detector-agent)
2. Triage (triage-agent)
3. Silent observe (silent-observer-agent)
4. Plan fix (plan-builder)
5. Apply fix
6. Verify (validation cycle PR04)
**Quando:** Continuo, dopo ogni errore/fallimento.
**Gate:** Failure logged, fix applied, verify PASS.

---

## PR07 — Packaging & Release
**Obiettivo:** Confezionare e rilasciare skill completa.
**Steps:**
1. Validate all (PR04 su tutto)
2. Bundle (SKILL.md + agents/ + references/ + scripts/ + memory/ + evals/)
3. Create .skill package
4. Test install (npx skills add)
5. Document (README, usage)
6. Release (push to repo)
**Quando:** Fine progetto.
**Gate:** All validation PASS, .skill created, install test OK.

---

## Connessioni
- **Principi correlati:** P01 (iterative), P04 (interactive), P08 (depth), P09 (failure-modes), P10 (memory)
- **Pattern correlati:** PT02 (pipeline), PT03 (builder-then-optimizer), PT05 (canonical files), PT06 (schema-tightening), PT07 (silent-observer)
- **Agenti:** plan-builder (PR01/PR04/PR06), agent-spec-builder (PR03), validators (PR04), memory-ecosystem-builder (PR05)
