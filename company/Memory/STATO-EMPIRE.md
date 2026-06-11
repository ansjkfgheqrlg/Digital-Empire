# STATO EMPIRE -- aggiornato 2026-06-11 (pomeriggio)

## Fase roadmap corrente
**F1-bis — ARRICCHIMENTO MASSIVO `company/` — INTERROTTO A METÀ (session limit Claude,
reset 19:50 Europe/Rome, 2026-06-11).** Tutti e 6 gli agenti swarm morti sul limite.
⚠️ L'account Claude è CONDIVISO Max+Gael: fino alle 19:50 nessuno dei due può lavorare con Claude.

**RIPRESA (dopo le 19:50) — rilanciare swarm arricchimento, prompt IDEMPOTENTI
(verificano l'esistente prima di scrivere). Stato atterrato per cartella:**
| Cartella | File | Stato |
|---|---|---|
| 07-FORGE 8 · 09-OPERATIONS 7 · Board-CSuite 8 · Backbone 10 | — | parziali buoni |
| 01-AGENCY 6 · 03-CONTENT-FACTORY 5 · Sentinels 6 · Guilds 6 | — | parziali |
| 02-INFO-BUSINESS 3 · 04-MARKETING 3 · 05-MULTI-BUSINESS 3 · 06-PLATFORM 3 · 08-INTELLIGENCE 3 · Mandato 2 · 10-MEMORY 2 · Gerarchia 1 | — | quasi vuoti |
Gate finale invariato: 0 cartelle vuote, 0 file <15 righe, schede agente complete.
Fonti: dossier PIANO-MAESTRO 0X corrispondenti. Vietato toccare Memory/ e wiki/log.md (agenti).

Obiettivo fase: 0 cartelle vuote, 0 file magri, ogni agente con scheda
completa stile CF (identità, responsabilità, I/O, come ragiona, KPI, escalation).

## ⚠️ COORDINAMENTO (anti-collisione)
- **MAX SI FERMA (2026-06-11 pomeriggio). IL TESTIMONE PASSA A GAEL.** Il blocco
  "Max scrive in company/" è RIMOSSO: dopo il reset delle 19:50, `company/` è di Gael.

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

## Cosa e' stato fatto (ultimo evento in cima)
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
5. **F4 B1 COMPLETATO** -- gate PASS 97/97.
   Infrastruttura AGENCY live pronta: 6 reparti, 4 HC intra-agency, state.json, 9 skill.
6. **Prossime azioni F4 (B2-B7):**
   - SBLOCCARE: rinnovare Token FB (Max) -- WF-OUTREACH-INSTAGRAM sospeso
   - SBLOCCARE: decidere prezzo Manuale Claude Code (Max) -- blocca lancio 02-INFO-BUSINESS
   - B2: wrap formale WF outreach come team L3 con trace.jsonl events
   - B3: primo preventivo reale con discovery-call-brief + proposal-gate
   - Gate F4 definitivo: primo ciclo reale tracciato in state.json
7. **YouTube ingestion** @Legamidiamore + @dosementale -- task 7.0/F-MB1, sessione dedicata
