# GATE VERBALE — youtube-lead-machine — 2026-07-20 — **PASS** (7/7)

Gate eseguito da fas-qa-gate su build fas-skill-smith (WF-SKILL-NEW steps 1-5 completati).
Piano: `FORGE-AGENT-SKILL/memory/plans/PLAN-youtube-lead-machine.md` ·
MKD: `FORGE-AGENT-SKILL/memory/mkd/MKD-youtube-lead-machine.md`

| # | Controllo (checklist bloccante) | Esito | Evidenza |
|---|---|---|---|
| 1 | Formato skill completo, 0 stub/TODO | ✅ PASS | kernel 118r ≤550 + 6 references + evals + failure-modes; grep stub/TODO/placeholder = 0 |
| 2 | MKD esiste, coverage atomi ≥95% (campione 20) | ✅ PASS | MKD tabella 25/25 atomi mappati a file = 100%; campione 20/20 |
| 3 | failure-modes ≥5 righe + evals ≥5 casi con atteso | ✅ PASS | failure-modes.md 8 righe (F1-F8) + evals 7 scenari attesa + 5 guard-rail |
| 4 | Intestazione ADR-008 reale in testa | ✅ PASS | frontmatter+blocco: proprietario FORGE-AGENT-SKILL, controllore fas-qa-gate, origine MIR-11/sorgente Formazzione, governo ADR/R1-R4 |
| 5 | No collisioni slug; nessun esistente reso obsoleto | ✅ PASS | `youtube-lead-machine` assente da skills-map/REGISTRO prima della registrazione; RECALL documentato: script-factory e copy-workflow RESTANO e vengono delegati (anti-doppione) |
| 6 | Motori/sorgenti intatti (ADR-003) | ✅ PASS | `git status` su copy-workflow/, content-forge2.0/, master-build-architecture/, Formazzione/, SKILL & Agenti/ = 0 modifiche |
| 7 | Memoria: piano + verbale + CP globale | ✅ PASS | questo file + PLAN + MKD; CP-20260720-005 predisposto |

## Evals loop (step 5) — verificato in gate
- Attivazione: 6/6 corretta (E5 negativa rispettata: copy landing → copy-workflow, non questa skill).
- Livello: deleghe esplicite funzionanti (script → factory con vincoli; QA copy → /copywriting review).
- Ritocchi applicati dal giro evals: description +trigger lead-response/DM (E3); kernel §3 delega esplicita.

## Difetti trovati e chiusi durante il gate
1. MKD mancante allo step 2 (cartella memory/mkd/ non esisteva) → creato prima del verbale, coverage verificata.
2. Ritocchi evals descritti ma non ancora applicati al kernel → applicati (description righe trigger, §3).

## Anti-recidiva
Nessun FAIL ripetuto su questa build. Regole reparto invariate.
**Via libera alla registrazione** (step 7): skills-map v1.3 · REGISTRO-IMPRESA §3 · wiki · STATO/INDEX · CP-20260720-005.
