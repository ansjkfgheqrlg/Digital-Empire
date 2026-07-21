# Conductor Evals

**Success Criteria (Skill-Creator style + own invariants):**
- All 10 invariants satisfied in outputs (checked by qa + validator).
- >25 agents produced with (plan for) 7 files each.
- Memory/ structure complete + INDEX updated live after every simulated step.
- Traceability: 100% atom coverage from sources in KG + final docs.
- User can run the output architecture in Ruflo/Content-Forge without modification.
- At least one full interactive ASK-BUILD-ITERATE cycle logged.
- No major AP01/AP07 etc. (explicit callouts in critique).
- Quantitative: Increasing depth across PLAN-vN, token efficiency via Research-Plan-Reset.

**Test Prompts (in evals/evals.json):**
- Basic swarm with memory from day one.
- Meta-transform of the knowledge-pack.
- Full AION-like ecosystem with Ruflo integration.

**Grading:** Use coverage_check.py + human review of artifacts + memory log integrity.