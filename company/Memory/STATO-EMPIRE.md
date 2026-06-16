# STATO EMPIRE -- aggiornato 2026-06-11 (sera — DIRETTIVA V2)

## 🚨 PIVOT V2 (ADR-007 — leggere PRIMA di qualsiasi cosa)
Max ha dettato la **Direttiva di Scala**: `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md`.
In sintesi: 1 workflow = Content Factory Exponium intero · Board C-Suite = 7 workflow da
≥10 agenti l'uno · ogni reparto = team 6-10 agenti + 1-5 workflow CF-grade · Mandato =
ecosistema di governo · Sentinelle multi-workflow · Guilds ricche · nuovo organo
**MAXIMILIAN** (team che incarna Max, corpus in `Memory/maximilian-corpus/`) · knowledge
ingestion delle cartelle formazione · roadmap V2-0…V2-8. **Lo standard v1 è superato.**
→ Per GAEL: il tuo F1-bis in corso VALE (è la base, completalo pure) — ma la fase dopo
NON è più F5: è **V2-2 (dossier v2)** poi **V2-3 (organo MAXIMILIAN)**, vedi roadmap §10
del piano V2. Niente nuove strutture a standard v1 da ora in poi.

## Fase roadmap corrente
**V2-2 — DOSSIER v2 — IN CORSO (2026-06-16, Gael).** F1-bis ✅ COMPLETATO (CP-002).

**V2-2 fatto finora:**
- ✅ Dossier **MAXIMILIAN** (`PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md`, CP-003): blueprint
  organo LX (8 agenti, review-gate 5-bis, 2 workflow, 2 skill) — da costruire in V2-3.

**V2-2 prossimi deliverable:**
1. Dossier **MANDATO-ecosistema** (§3 piano V2) — l'altra nuova struttura v2.
2. Riscrittura/ampliamento dossier 01-09 a scala v2 (swarm quando budget regge; naming
   Title-Case fisso, prompt idempotenti, mai 2 swarm grossi insieme).
3. Poi V2-3 (build organo MAXIMILIAN dal dossier 12 — priorità alta, attiva il 5-bis).
Vedi `PIANO-MAESTRO/11-PIANO-V2-DIRETTIVA-SCALA.md` §10 (roadmap V2-0…V2-8).

## ⚠️ COORDINAMENTO (anti-collisione)
- Nessuno swarm attivo. F1-bis chiuso. company/ libera.
- REGOLA NAMING swarm (lezione CP-20260616-001): grafia file FISSA (Title-Case), mai
  mischiare MAIUSCOLO/Title-Case → su Windows (core.ignorecase) genera doppioni che
  bloccano i commit. Allowlist progetto include già `Write(company/**)` per gli swarm.

## ▶️ ISTRUZIONI PER GAEL (prossima sessione, dopo le 19:50)
**Task: completare F1-bis (arricchimento massivo company/) col NUOVO METODO.**
1. NOVITÀ da leggere prima (pull automatico già fatto dagli hook):
   `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` (metodo a 9 passi, ADR-006 — sostituisce
   "fase→controllo→avanti"), ADR-005 (minori→BACKLOG), CLAUDE.md aggiornato.
2. Esegui il ciclo a 9 passi su F1-bis: RECALL (questo file) → SPEC (DONE WHEN: 0 cartelle
   vuote, 0 file <15 righe, schede agente complete per TUTTI i roster dei dossier) →
   PRE-MORTEM (lezione CP-005: agenti muoiono → prompt idempotenti; budget-guard 20%) →
   BUILD: **swarm 6 agenti in background** su cartelle disgiunte, stessi compiti della
   tabella sotto, prompt che VERIFICANO L'ESISTENTE prima di scrivere → GATE (scan vuote/
   magri) → REVIEW indipendente (1 agente legge 5 file a caso vs dossier) → TEST amnesia →
   COMMIT (CP + questo file + wiki log + push) → RETRO.
3. Assegnazione swarm (fonte = dossier PIANO-MAESTRO corrispondente):
   A1: Ecosistemi/01+02 · A2: 03+04 · A3: 05+06 · A4: 07+08 · A5: 09+10+Gerarchia ·
   A6: Mandato+Board-CSuite+Backbone+Sentinels+Guilds+GRUPPO.md+org.
   Vietato agli agenti: toccare Memory/, 01-agency/, skills-map.yaml, wiki/log.md.
4. Dopo F1-bis: prossima fase = F4 B2 (wrap formale WF outreach come team L3, SENZA
   bisogno del token FB — slot pronto, ADR-005).
   **NOTA GAEL 20:30: B2 GIÀ COMPLETATO (CP-006) + gate F4 VERDE con ciclo dry (CP-007),
   fatti in parallelo prima di ricevere questo handover. Dopo F1-bis si va a B3/F5.**

## Cosa e' stato fatto (ultimo evento in cima)
- 2026-06-13 — **FIX ARCHITETTURA EMPIRE STUDIO** (Max, CP-20260613-001):
  Errore critico: Memory Empire omesso dal pipeline in sessione studio Andrei Pascu.
  Fix: RULES.md creato (checklist non negoziabili + KNOWN ERRORS registry),
  compliance-auditor + error-triage-controller + silent-observer aggiornati con
  Memory Empire guard esplicito + WATCH-001 counter video vs ME calls.
  SKILL.md aggiornato: invariante #0 (session-init) + invariante #8 (Memory Empire).
  Run Andrei Pascu andrei-pascu-001: fermata a Stage 2 video 1 (9CuQI0Cr4Pg, 545 frame pronti).
  Studio da riprendere: Cat 1-7 YouTube @Andrei Pascu (323 video totali, ~270 da studiare).
- 2026-06-11 — **F4 GATE VERDE** (Gael, CP-20260611-007): ciclo dry-run CY-20260611-001
  end-to-end (19 eventi trace.jsonl, 4 HC attraversati, 3 gate PASS) registrato in
  state.json. Criterio ADR-005 (slot pronto + test dry). verify: PASS 113/113.
  Lavorato SOLO in Memory/, scripts/, .claude/skills/ (rispettato blocco swarm).
- 2026-06-11 — **F4 B2 WRAP OUTREACH COMPLETATO** (Gael, CP-20260611-006): 4 team L3
  in company/01-agency/A2-ACQUISIZIONE/L3/ (creati prima del blocco swarm, file NUOVI)
  + scripts/agency-trace.ps1 (logger trace testato). Runtime outreach INVARIATO (ADR-003).
- 2026-06-11 — **F4 B1 AGENCY LIVE INFRASTRUTTURA COMPLETATO** (Gael, CP-20260611-004):
  company/01-agency/ con 6 reparti L2 (BACKBONE.md + handoffs), state.json + trace.jsonl schema,
  4 HC intra-agency, 9 nuove skill FORGE. Gate: PASS 97/97.
- 2026-06-11 — **F3 MIGRAZIONE ASSET COMPLETATO** (Gael, CP-20260611-003):
  51 skill/workflow mappate in skills-map.yaml, 35 cartelle in inventario-asset.yaml,
  8 wrapper L3 (Ecosistemi/<eco>/Workflow/). Gate: PASS 70/70.
- 2026-06-11 — **F2 BACKBONE OPERATIVO COMPLETATO** (Gael, CP-20260611-002):
  ruflo v3.10.41 installato, BUS (handoffs+HC-template), BRAIN (10 namespace),
  registro-agenti.yaml (19 agenti), verify-empire.ps1 PASS 59/59.
- 2026-06-11 — **F1 SCAFFOLDING EMPIRE OS COMPLETATO** (Gael, CP-20260611-001):
  task 1.1–1.7 completati. `company/` navigabile: GRUPPO.md, Mandato, Board-CSuite (7 agenti),
  10 Ecosistemi (ECOSISTEMA.md + BACKBONE.md + 4 sottocartelle ognuno), Backbone (6 componenti),
  Guilds (5), Sentinels (5), Gerarchia, `scripts/gen-empire.py`.
  Gate F1: `python scripts/gen-empire.py --check` → PASS 92/92.
- 2026-06-10 — **PIANO-MAESTRO completo**: 10 file in `Digital Empire/PIANO-MAESTRO/`
  (00 master, 01-05 ecosistemi business, 06 core, 07 backbone+ruflo+skills,
  08 roadmap 12 fasi, 09 MEMORY). Prodotto con swarm di 7 agenti paralleli + conductor.
- 2026-06-10 — **Ecosistema MEMORY** aggiunto su richiesta Max (urgenza massima):
  10° ecosistema, pattern #13 memory-first, costruzione ME-0/ME-1 in corso.
- 2026-06-08 — Studio approfondito repo Content Factory Exponium (AION GROUP) →
  wiki `projects/Exponium/Exponium_Content_Factory_Studio.md`.

## Lavori in corso
- **GitHub monorepo + sync Max↔Gael (ADR-004, CP-002): ✅ LIVE** — repo privato
  `ansjkfgheqrlg/Digital-Empire`, push iniziale 966.63 MiB completato (2026-06-10 21:27).
  PENDENTI: (a) Max incolla blocco hooks in `.claude/settings.json` (contenuto pronto,
  Claude non può editarlo per policy auto-mode), (b) Gael esegue SETUP-GAEL.md sul suo PC
  — DECISIONE Max 2026-06-10: Gael usa l'account GitHub di Max (ansjkfgheqrlg), niente
  invito collaborator; identità distinte solo via git user.name (Max/Gael).
- ✅ ME-0/ME-1 + review coerenza + wiki: COMPLETATI (CP-001).

## Blocchi / pending noti
- **NESSUN BLOCCO STRUTTURALE.** Item minori (token FB, prezzo manuale, team-prezzi, ecc.)
  → spostati in `BACKLOG.md` per direttiva Max (ADR-005): non fermano MAI la costruzione.
  Le fasi si riformulano per aggirarli (slot pronti + test dry).
- Ingestione Empire Studio canali YouTube riferimento (@Legamidiamore, @dosementale) —
  task 7.0 / F-MB1, sessione dedicata (questo è strutturale per F7, non per F4-F6).

## RIPRESA DA (per la prossima sessione)
1. Caricare questo file + INDEX.md (memory-first).
2. **F1 COMPLETATO** -- gate PASS 92/92.
3. **F2 COMPLETATO** -- gate PASS 59/59.
4. **F3 COMPLETATO** -- gate PASS 70/70.
5. **F4 GATE VERDE** -- verify PASS 113/113 (CP-004 B1, CP-006 B2, CP-007 ciclo dry).
   AGENCY live: 6 reparti, 4 HC, 4 wrap L3 outreach, state.json+trace.jsonl validati
   con ciclo dry CY-20260611-001, 9 skill F4, agency-trace.ps1 operativo.
6. **Prossime azioni:**
   - **PRIORITA' (handover Max): F1-bis arricchimento company/ col metodo 9 passi (ADR-006)**
     -- vedi ISTRUZIONI PER GAEL sopra. Il blocco swarm Max e' rimosso: company/ e' di Gael.
   - B3 reale: prima call vera -> discovery-call-brief -> beast-preventivi -> proposal-gate
   - Primo ciclo REALE: stesso pattern di CY-20260611-001 con dry_run: false
   - Backlog (ADR-005, non bloccanti): B-001 token FB (runbook in WF-OUTREACH-INSTAGRAM.md),
     B-002/B-003 prezzi via team-prezzi
   - F5: prossima fase roadmap (vedi PIANO-MAESTRO/08-ROADMAP-FASI.md) dopo fine swarm F1-bis
7. **YouTube ingestion** @Legamidiamore + @dosementale -- task 7.0/F-MB1, sessione dedicata
