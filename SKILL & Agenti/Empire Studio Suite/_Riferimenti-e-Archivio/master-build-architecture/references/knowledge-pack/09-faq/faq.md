# FAQ — Domande Frequenti

> **Fonte:** Knowledge Pack 09-faq + esperienze build Master-Build-Architecture.

## Domande Generali

### D01: Cos'è Master-Build-Architecture?
**R:** È una skill per Claude Code che guida la progettazione e costruzione di architetture multi-agente complete, con memoria persistente, self-improvement e tracciabilità totale.

---

### D02: Come si invoca la skill?
**R:** `/master-architect <vision-o-path> [--target=plan|swarm|skill|full-ecosystem] [--name=slug] [--memory-first]`

Oppure con trigger naturali: "Architetta questo...", "Crea lo swarm per...", "Forgia i miei appunti in agenti con memoria".

---

### D03: Quanti agenti produce?
**R:** La skill stessa ha 18 agenti operativi. Per progetti utente, il numero dipende dal Decision Tree DT02: Minimal (≤10), Standard (10-25), Large (25+).

---

### D04: Qual è la differenza con altre skill di architettura?
**R:** Master-Build-Architecture integra:
- **Ruflo** (swarm coordination, memory AgentDB, federation)
- **Content-Forge 2.0** (9-stage pipeline, MKD, no-summary-expansion)
- **Context-Engineering-Advisor** (two-layer memory, Research→Plan→Reset→Implement)
- **Skill-Creator** (evals loop, progressive disclosure, iteration)
- **Knowledge Pack** (15 principi, 11 pattern, 9 anti-pattern, 4 case studies)

Nessun'altra skill integra tutte queste fonti con tracciabilità P12.

---

## Domande Tecniche

### D05: Come funziona la memoria persistente?
**R:** Due strati (Context-Engineering-Advisor):
- **Short-term:** Conversazione corrente (session)
- **Long-term:** File system (memory/checkpoints/, decisions/, sessions/, plans/, architectures/, MEMORY-INDEX.md)

Ogni step crea CP (checkpoint), aggiorna INDEX, fa sync. Python auto-update con `memory_manager.py`.

---

### D06: Cosa sono i 7 file canonici per agente?
**R:** PT05 (Canonical Files per Target):
1. `spec.md` — Ruolo, missione, invarianti
2. `system-prompt.md` — Prompt dettagliato con invarianti, handoff, procedure
3. `tools.md` — Strumenti con implementazione Python
4. `playbook.md` — Steps operativi + esempi
5. `evals.md` — Test cases + benchmark
6. `failure-modes.md` — Tabella failure/symptom/prevention/detection/recovery
7. `memory.md` — Mandate memoria, shared_state, update protocol

---

### D07: Come si validano gli output?
**R:** PR04 (Validation Cycle):
1. **Schema check** (target-schema-validator) — forma canonica
2. **Coverage check** (coverage-verifier) — tracciabilità P12
3. **FM validation** (failure-mode-validator) — failure-modes presenti

Gate: 100% compliant su tutti e 3.

---

### D08: Cos'è il "no-summary-expansion"?
**R:** P03 (No-Summary-Expansion): ogni atomo dalla fonte diventa **più ricco**, mai più povero. Mai riassumere: espandere con dettagli, esempi, implementazioni. Label inventions con ➕.

---

### D09: Come funziona il self-improvement?
**R:** PR06 (Self-Improvement Cycle):
1. **Failure detect** (failure-detector-agent)
2. **Triage** (triage-agent)
3. **Silent observe** (silent-observer-agent)
4. **Plan fix** (plan-builder)
5. **Apply fix**
6. **Verify** (PR04 validation)

CS03: SI without observer = drift → silent-observer obbligatorio.

---

## Domande Operative

### D10: Quanto tempo serve per un'architettura completa?
**R:** Dipende dalla complessità:
- **Minimal (≤10 agenti):** 30-60 min
- **Standard (10-25 agenti):** 60-120 min
- **Large (25+ agenti):** 120-240 min

Include: PLAN-v1 → ASK → BUILD → CRITIQUE → ITERATE → VALIDATE → PACKAGE.

---

### D11: Posso usare la skill senza Ruflo?
**R:** Sì. Ruflo è opzionale per memoria avanzata (AgentDB HNSW). Senza Ruflo: two-layer memory (file system) funziona completamente.

---

### D12: Come gestisco i conflitti tra principi?
**R:** Priorità:
1. **P10** (Memory-first) — sempre
2. **P12** (Traceability) — sempre
3. **P09** (Failure-modes) — sempre
4. **P03** (No-summary) — sempre
5. Altri principi: contesto-dipendente

In caso di conflitto: creare DEC (Decision Record) con rationale.

---

### D13: La skill può migliorare se stessa?
**R:** Sì, PT08 (Meta-Recursive). La skill ha meta-recursive-builder che può:
- Migliorare la skill stessa (auto-miglioramento)
- Produrre varianti della skill
- Applicare lesson learned (P10) alla prossima versione

Esempio reale: CP-026+ (autonomous continuation) = meta-recursive in azione.

---

## Domande Troubleshooting

### D14: La skill non trova gli agenti nel file system
**R:** Verificare path: `agents/<category>/<agent-name>/`. Ogni agente deve avere 7 file .md. Usare `validator.py` per check.

---

### D15: Coverage report mostra orfani
**R:** Orfani = atomi fonte non citati in output. Soluzioni:
- Handoff a reference-expander-agent (O3) per aggiungere citazioni
- Oppure aggiornare output per includere riferimenti

---

### D16: Validation FAIL
**R:** Cause comuni:
- Agenti con <7 file → completare con agent-spec-builder
- Coverage <90% → reference-expander
- FM validation FAIL → aggiungere failure-modes.md

Soluzione: PR04 (Validation Cycle) con fix iterativi.

---

## Connessioni
- **Principi correlati:** Tutti (P01-P15)
- **Pattern correlati:** Tutti (PT01-PT11)
- **Agenti:** Tutti (conductor, builders, pipeline, domain, qa, optimizers, self-improvement)
- **Reference:** SKILL.md, README.md, ANALYSIS-AND-IMPROVEMENT-PLAN.md
