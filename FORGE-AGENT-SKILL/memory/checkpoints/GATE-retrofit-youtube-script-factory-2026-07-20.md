# GATE VERBALE — retrofit youtube-script-factory (MIR-5 sprint 1)

- **Data:** 2026-07-20 · **Gate:** fas-qa-gate (modalità RETROMODE: deliverable = wrap di asset vivo, non nuova forgia)
- **Piano:** `memory/plans/PLAN-retrofit-youtube-script-factory.md` · **MKD:** `memory/mkd/MKD-retrofit-youtube-script-factory.md`

## Checklist 7 punti
1. **File completi:** spec.md · tools.md · playbook.md · evals.md (7 casi E1-E7: 2 happy, 1 gate, 3 boundary, 1 ops) ·
   failure-modes.md (7 righe F1-F7) · memory/INDEX.md · niente stub/TODO — **PASS**
2. **MKD ≥95%:** 17/17 atomi strutturali = 100% (mappa righe per righe delle 9 sezioni; contenuto non spostato, ADR-003) — **PASS**
3. **Failure-modes ≥5 + evals ≥5:** 7 + 7, con boundary anti-sconfinamento espliciti (E5/E6 sui confini di delega) — **PASS**
4. **Intestazione ADR-008:** presente e reale in spec.md (proprietario 04-MARKETING W7 uso + reparto retrofit,
   controllore qa-gate+METHOD-GUARD, origine pre-Impero→wrap, governo ADR-002/003/008/009) — **PASS**
5. **No collisioni slug:** `youtube-script-factory` assente da skills-map e REGISTRO prima della registrazione
   (era orfana attiva — proprio questo il motivo dello sprint) — **PASS**
6. **Motori intatti (ADR-003):** `git diff` su `Skill-youtube.md` = **zero** (master markdown intoccato);
   i 3 `tools/*.py` sono ESTRATTI additivi delle sezioni 7-9, regola deriva dichiarata (md vince) — **PASS**
7. **Memoria:** PLAN con **sezione `## ASK` compilata** (MIR-3 — Q1 slug con raccomandazione+default;
   T2-T4 documentati assenti) · verbale presente · CP globale predisposto (CP-20260720-014) — **PASS**

## Delta dichiarati (onestà, no greenwashing)
- **D1 R2 kernel oversize:** kernel sorgente 5.166 righe (>550 canonico). Mitigazioni: SEZ 6 = kernel
  operativo (~215r) + indice in spec.md; v2 ristrutturazione SOLO dopo validazione nuova-vs-vecchia (ADR-003).
- **D2 Doppia scala scoring:** "30+" (§1) vs 45pt (SEZ 5/8) → dichiarata canonica la 45pt (tool = fonte).
- **D3 Verifica tool:** `py_compile` 3/3 ✅; esecuzione end-to-end non fatta (CLI interattive, ambiente sandbox) —
  lo dichiaro, non chiamo "testati" dei file solo compilati.

## Esito: **PASS 7/7 (retromode)** — registrazione autorizzata.
Attivazione evals E7-pratica verificata sul campo: dalla cartella dell'asset si trovano in ≤2 minuti
ruolo, tool, scoring e deleghe SENZA leggere le 5.166 righe (prima: impossibile).

**Lezione anti-recidiva registrata:** estrazione da markdown multi-sezione con marker corti ha prodotto
3 file identici (indice interno confuso per header) — regola pratica: marker di sezione COMPLETI
(titolo pieno) + verifica md5 prima della dichiarazione di completamento. Applicata e risolta in sessione.
