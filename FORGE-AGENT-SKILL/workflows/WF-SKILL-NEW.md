# WF-SKILL-NEW — Pipeline "nuova skill ufficiale" (step-by-step)

**Trigger:** esigenza di un metodo ripetibile multi-contesto ("ci serve la skill X").
**Owner:** fas-conductor · **Build:** fas-skill-smith · **Gate:** fas-qa-gate.

| # | Step | Chi | Output |
|---|---|---|---|
| 1 | Intake + RECALL (skill simili esistenti in `.claude/skills/`, `SKILL & Agenti/SKILL/`) | conductor | richiesta validata |
| 2 | `/forge <sorgente> --target=skill --name=<slug>` → MKD + bozza kernel | skill-smith | bozza |
| 3 | PLAN: cosa sta nel kernel (≤550r) vs references/ vs scripts/ vs evals/ | conductor+smith | piano |
| 4 | **ASK (MIR-3, obbligatorio):** sezione `## ASK` nel PLAN compilata per `ASK-PROTOCOL.md` — max 3 domande mirate con raccomandazione+default, oppure "0 domande" motivata. Default `[ASSUNZIONE]` propagati nel piano | conductor | sezione ASK compilata |
| 5 | BUILD struttura completa + description con trigger (IT+EN) | skill-smith | skill v0.9 |
| 6 | **Evals loop**: 3 scenari reali → attivazione corretta? output al livello? → ritocca description/kernel (criterio skill-creator) | skill-smith | report evals |
| 7 | GATE bloccante (checklist 7 punti + progressive-disclosure vera; punto 7 verifica sezione `## ASK`) | qa-gate | verbale |
| 8 | Installazione `.claude/skills/<slug>/` (o wrapper se kernel in ecosistema) + skills-map + REGISTRO + CP | conductor | skill attiva |

**Regola d'oro:** una skill senza evals passati NON esiste (regola 6 è bloccante come il gate).
