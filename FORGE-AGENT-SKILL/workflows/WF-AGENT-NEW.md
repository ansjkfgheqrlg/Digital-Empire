# WF-AGENT-NEW — Pipeline "nuovo agente/team" (step-by-step)

**Trigger:** richiesta capability da un ecosistema/reparto/Max ("ci serve un agente che fa X").
**Owner:** fas-conductor · **Gate:** fas-qa-gate · **Tempo target:** 1 sessione per lotto ≤4 agenti.

| # | Step | Chi | Output |
|---|---|---|---|
| 1 | Intake + RECALL (niente duplicati: skills-map + REGISTRO) | conductor | richiesta validata |
| 2 | Raccolta sorgente (transcript/dossier/brief; se assente → mini-MKD dalla richiesta, ➕ marcate) | conductor | `sources/` nota |
| 3 | `/forge <sorgente>` → **MKD** (mai riassunti; coverage 100%) | agent-smith | MKD |
| 4 | FORGE-PLAN (slug, 7-file plan, handoff, criteri gate) | conductor | piano in `memory/plans/` |
| 5 | **ASK (MIR-3, obbligatorio):** sezione `## ASK` nel FORGE-PLAN compilata per `ASK-PROTOCOL.md` — max 3 domande mirate con raccomandazione+default, oppure "0 domande" motivata. Default `[ASSUNZIONE]` propagati nel piano | conductor | sezione ASK compilata |
| 6 | BUILD 7 file canonici (write-early; swarm se >1 agente) | agent-smith | cartella agente/team |
| 7 | Self-review dello smith (1 giro) | agent-smith | v0.9 |
| 8 | GATE bloccante (checklist 7 punti; punto 7 verifica sezione `## ASK`) | qa-gate | verbale PASS/FAIL |
| 9 | Registrazione ADR-008 (REGISTRO-IMPRESA + skills-map se skill) + CP globale | conductor | artefatto intestato |
| 10 | Consegna al richiedente + nota retro | conductor | handoff |

**Escalation:** FAIL×2 stesso difetto → conductor decide (fix rapido vs ADR vs stop).
**Kill-criteria:** se in step 2 emerge che esiste già → wrap dell'esistente (ADR-003), mai rebuild.
