# FORGE-PLAN — MIR-5 sprint 1: retrofit canonico di `youtube-script-factory`

- **Data:** 2026-07-20 · **Owner:** fas-conductor · **Gate:** fas-qa-gate (verbale in memory/checkpoints/)
- **Trigger MIR-5 (P3 dossier 18):** retrofit formato canonico sui reparti/figli pre-impero, 1 figlio/sprint.

## Scelta del primo figlio (motivata)
`Skill CRO - Youtube - Lead magnet/Skill-youtube.md` perché: ① è **attiva e delegata** dalla skill neonata
`/youtube-lead-machine` (ritorna in ogni script del canale) ② era **orfana ADR-008** (assente da skills-map
e REGISTRO pur essendo in uso) ③ i suoi 3 tool Python erano **embed-only** nel markdown (imbrogli operativi:
il comando citato non esisteva su disco) ④ retrofit = alto valore, rischio bassissimo (wrap additivo).

## Diamond (cosa produce lo sprint)
- Satelliti canonici nella cartella dell'asset (wrap ADR-003, markdown **mai** modificato):
  spec.md · tools.md · playbook.md · evals.md (7 casi) · failure-modes.md (7 righe) · memory/INDEX.md
- `tools/*.py` — 3 script estratti dalle SEZ 7-9 + verifica `py_compile` (3/3) + regola deriva (md vince).
- MKD (questo folder `memory/mkd/`) con coverage atomi 17/17=100%.
- Registrazione: skills-map (+entry), REGISTRO §3, wiki tool page, dossier 18 (MIR-5 avanzamento sprint 1).
- GATE retro-mode con delta R2 dichiarato (kernel 5.166r > 550 → wrap-legacy, debito documentato in spec).

## ASK (MIR-3 — ASK-PROTOCOL)
| # | Domanda (1 decisione) | Opzioni | Raccomandazione | Default [ASSUNZIONE] | Trigger |
|---|---|---|---|---|---|
| Q1 | Slug di registrazione ufficiale in skills-map/REGISTRO? | A) `youtube-script-factory` (name nel frontmatter) · B) rinominare canonico `skill-cro-youtube-script-factory` | **A** — stabilità del nome già vissuto dall'asset; il rename romperebbe riferimenti per zero valore | A | T1 (naming/registry) |

*(T2-T4 assenti: contenuto completo e vivo, niente scelte economiche, wrap additivo senza conflitti.
Nota operativa: estrarre i tool in `tools/` vs lasciarli embedded — deciso internamente: estrarre, valore
concreto e additivo; non merita una delle 3 domande di Max.)*

## Handoff
Build inline (conductor). Gate: verbale retro-mode. Registrazione + CP globale `CP-20260720-014`.
Prossimo figlio MIR-5 (sprint 2, da decidere col censimento): candidati `SKILL & Agenti/` altre skill
pre-impero o agenti Empire Studio — da valutare a valle di questo gate.
