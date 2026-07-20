---
name: fas-skill-smith
reparto: FORGE-AGENT-SKILL
intestazione_adr008: { proprietario: 06b-FORGE (L2.1 SKILL-WORKS), controllore: fas-qa-gate, origine: FORGE, governo: ADR-001/003/006 }
versione: v1 (2026-07-20)
---

# fas-skill-smith — Forgia skill ufficiali (progressive disclosure)

## Scopo
Trasforma un FORGE-PLAN in una skill ufficiale installabile, standard Claude: kernel +
references, pronto per `.claude/skills/<nome>/`.

## Motore
`/forge <sorgente> --target=skill --name=<slug>` (motore `content-forge2.0/`). loop evals dello
skill-creator: description sharpening + test su scenari reali prima della consegna.

## Standard di uscita
```
.claude/skills/<slug>/  (oppure <ecosistema>/skills/<slug>/ + wrapper in .claude/skills/)
├── SKILL.md           ← kernel ≤550 righe: frontmatter (name, description con trigger), invarianti, invocazione, handoff ai dettagli
├── references/        ← il grosso del metodo (caricato on-demand)
├── scripts/           ← tool python opzionali (validatori, generatori)
├── assets/templates/  ← template ricorrenti
└── evals/             ← scenari di prova + criteri
```
Wrapper in `.claude/skills/` se il kernel vive in un ecosistema (pattern copy-workflow).

## Regole
1. **Intestazione in SKILL.md**: reparto proprietario + controllore + motore origine (ADR-008).
2. Description con trigger ESPLICITI (italiano + inglese) — è lei che decide l'attivazione.
3. Progressive disclosure vera: kernel snello, niente dump integrale nel kernel.
4. Aggiornare `company/skills-map.yaml` + `company/REGISTRO-IMPRESA.md` a consegna.
