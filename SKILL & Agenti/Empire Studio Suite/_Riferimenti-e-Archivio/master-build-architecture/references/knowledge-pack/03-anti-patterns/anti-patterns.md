# Anti-Patterns — 9 Anti-Patterns da Evitare

> **Fonte:** Knowledge Pack 03-anti-patterns + estrazioni da Content-Forge, Ruflo, Context-Engineering-Advisor.

## AP01 — Scaffold-as-Deliverable
**Sintomo:** File stub (README vuoti, agenti con solo 1 file) spacciati per completi.
**Prevenzione:** Gate di completezza (PT05: 7 file minimi per agente).
**Rilevamento:** `validator.py` controlla file count e contenuto minimo.
**Recupero:** Completare i file mancanti prima di procedere.

---

## AP02 — Permissive-Schemas
**Sintomo:** Accettare output che non rispettano la forma canonica.
**Prevenzione:** PT06 Schema-Tightening-Loop (schema evolve v1→vN).
**Rilevamento:** `target-schema-validator-agent` valida ogni output.
**Recupero:** Stringere schema, ri-validare, fix target.

---

## AP03 — User-Driven-Overhead
**Sintomo:** Troppi step manuali richiesti all'utente.
**Prevenzione:** Automazione canonica (CP auto, INDEX auto, memory_manager.py).
**Rilevamento:** Contare step manuali per sessione.
**Recupero:** Automatizzare con script Python.

---

## AP04 — LLM-Speak-Output
**Sintomo:** Output vago, generico, "LLM-style" senza concretezza.
**Prevenzione:** Esempi specifici, codice reale, numeri precisi.
**Rilevamento:** Review umana o humanizer-agent.
**Recupero:** Riscrivere con contenuto concreto.

---

## AP05 — Monolithic-Skill-MD
**Sintomo:** SKILL.md >500 righe, illeggibile.
**Prevenzione:** Progressive disclosure (P02) — SKILL.md lean, dettagli in references/.
**Rilevamento:** `wc -l SKILL.md` > 500 = allarme.
**Recupero:** Spostare dettagli in references/knowledge-pack/.

---

## AP06 — Feature-Creep
**Sintomo:** Aggiungere funzionalità/senzza giustificazione.
**Prevenzione:** Scope definito nel PLAN-v1, gate di approvazione per aggiunte.
**Rilevamento:** Confrontare PLAN-v1 vs output finale.
**Recupero:** Rimuovere feature non nello scope o aggiornare scope con ADR.

---

## AP07 — Skipping-the-Plan
**Sintomo:** Partire direttamente con il build senza PLAN-v1.
**Prevenzione:** P01/P04 — PLAN-v1 obbligatorio prima di BUILD.
**Rilevamento:** Check esistenza PLAN-v1.md.
**Recupero:** Tornare a fase 1, creare PLAN-v1.

---

## AP08 — No-Failure-Mode-Doc
**Sintomo:** Agenti senza failure-modes.md.
**Prevenzione:** P09 — failure-modes è file canonico obbligatorio.
**Rilevamento:** `failure-mode-validator-agent` scansiona tutti gli agenti.
**Recupero:** Creare failure-modes.md con ≥5 entry.

---

## AP09 — Premature-Optimization
**Sintomo:** Ottimizzare prima di avere profondità (P08).
**Prevenzione:** Depth-first: costruire profondità, poi ottimizzare.
**Rilevamento:** Review: "Questo agente ha 7 file completi? Sì → ottimizza."
**Recupero:** Completare profondità, poi ottimizzare.

---

## Connessioni
- **Principi correlati:** P02 (progressive disclosure), P06 (shapes), P08 (depth), P09 (failure-modes)
- **Pattern correlati:** PT05 (canonical files), PT06 (schema-tightening)
- **Case Studies:** CS03 (SI without observer = AP08), CS04 (bugs from AP01/AP02)
- **Agenti QA:** coverage-verifier, failure-mode-validator, target-schema-validator
