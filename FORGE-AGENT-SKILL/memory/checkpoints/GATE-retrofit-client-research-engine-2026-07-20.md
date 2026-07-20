# GATE VERBALE — retrofit skill-cro-ricerca / Client Research Engine (MIR-5 sprint 2, retro-mode)

- **Data:** 2026-07-20 · **Gate di:** fas-qa-gate · **Asset:** wrap additivo su asset vivo pre-impero (ADR-003).
- **Modalità:** retro-mode (il gate non valida una riscrittura: valida il WRAP + la dichiarazione onesta dei delta).

## Delta dichiarati (mai greenwashing)
- **D1 — Manifest fantasma (scoperto in MKD):** `SKILL.md` §KNOWLEDGE_FILES referenzia 5 template
  (`Template-Report-Ricerca` ★★★★★, `Checklist-Query-Piattaforme` ★★★★★, `Scheda-Analisi-Competitor`,
  `Template-Pain-Points-Scoring`, `Template-Obiezioni-Scoring`) **assenti dalla cartella**. Contenuti presenti
  inline nel master (R1-R5 + report) e nei 7 knowledge reali → asset funzionante, manifest desync.
  NON fixato: toccherebbe il master (ADR-003). Regola wrap: **il corpo vince sul manifest** (spec §debito 1).
- **D2 — Catena a monte/valle non censita:** Briefing Master Pro citato ma assente dal repo; CRO Copy Architect
  presente solo come knowledge dir non censita (candidata sprint 3). STEP 0 del master gestisce già
  il briefing mancante → non bloccante (spec §debito 2).
- **D3 — Pseudocodice narrante:** blocchi ```python non eseguibili usati come notazione procedurale;
  `tools: []` by design → dichiarato in tools.md, nessuna estrazione necessaria (lezione s1 applicata:
  niente estrazioni forzate dove non esiste codice reale).

## Checklist gate (7 punti, estensione MIR-9 + MIR-3)
| # | Punto | Esito |
|---|---|---|
| 1 | File canonici presenti: spec/tools/playbook/evals/failure-modes/memory-INDEX (topology.md NON richiesto: skill singola, non team) | ✅ 6/6 |
| 2 | MKD coverage ≥95% | ✅ **26/26 atomi = 100%** (MKD-retrofit-client-research-engine.md, righe citate per ogni atomo) |
| 3 | Failure modes ≥5 + evals ≥5 | ✅ failure 7 · evals 7 (E1-E7, tipi happy/gate/quality/boundary) |
| 4 | ADR-008: intestazioni + anagrafe | ✅ intestazione su tutti i satelliti · skills-map v1.6 (entry esistente aggiornata, niente duplicati) · REGISTRO §3 · CP-20260720-015 |
| 5 | Collisioni slug | ✅ nessuna: tenuto id censitura `skill-cro-ricerca`; alias "Client Research Engine" solo in note/spec (default Q1=B) |
| 6 | Diff su asset vivo = 0 | ✅ verificato: `git status` sulla cartella mostra SOLO nuovi file untracked, `git diff --stat` vuoto |
| 7 | Memoria completa: PLAN + ## ASK compilata | ✅ PLAN-retrofit-… con confronto candidati documentato + ASK Q1 (T1) con default [ASSUNZIONE] |

## Esito: **PASS (retro-mode)** ✅
Retrofit consegnato senza toccare l'asset vivo; debiti D1-D3 dichiarati; lezione sprint 1 (marker estrazione
deboli/md5) non applicabile perché zero estrazioni — verificato comunque che nessun file è stato duplicato.
**Firma:** fas-qa-gate · **Prossimo gate proposto:** MIR-5 sprint 3 (CRO Copy Architect knowledge dir — candidata).
