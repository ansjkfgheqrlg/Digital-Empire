# CANTIERE — presa di costruzione del Workflow Estate sui modelli operativi

> Generato da `empire cantiere` il 2026-07-29. Non modificare a mano: si rigenera.

Il cervello (WORKFLOW-ESTATE) governa questi modelli operativi. Per ognuno: dove sta il
prossimo passo di costruzione, chi lo possiede, se e' bloccato, se il codice esiste davvero.

## YOUTUBE-AUTOMATION-FACTORY  (`youtube`)

- **Ruolo:** Genera video YouTube in automatico (pipeline APEX-7 a 6 fasi F1-F6).
- **Owner:** Gael
- **Avanzamento:** task board: 4/7 fatti
- **Entrypoint:** `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS` — presente
- **Prossimo task board:** TASK-YT-005 — YT-Factory: Dashboard riflette l'esito reale (PASS/FAIL) della run corrente (owner Gael)
- **Prossimo passo:** TASK-YT-005 (Dashboard): write_dashboard() riflette PASS/FAIL reale della run corrente (oggi la dashboard e scritta da run_youtube_apex7.py, percorso fantasma, sempre PASS). F1-F6 gia reali (F4/F5/F6 chiuse 2026-07-29). Poi P2: TASK-YT-006 (ritiro APEX-7 duplicato) e TASK-YT-007 (docs).

## 12-STREAM-S7-BOT  (`stream-s7`)

- **Ruolo:** Bot trading Solana su segnali stream (paper trading per design).
- **Owner:** Gael/Claude
- **Avanzamento:** task nel board: nessuno con questi prefissi
- **Entrypoint:** `company/Ecosistemi/12-STREAM-S7-BOT/main.py` — presente
- **Prossimo passo:** L2->L3: collegare analysis_engine/execution_engine al ciclo Orchestrator->Gate->Memory; tarare le soglie gate su esecuzioni misurate; far scrivere al bot le sue metriche nel layer memoria.
- **BLOCCO:** B-010 (BACKLOG.md): serve un RPC provider a pagamento prima di qualunque LIVE reale. Decisione capitale = Max.

## Outreach (concessionari preventa + content/outreach factory)  (`outreach`)

- **Ruolo:** Contatto concessionari (email/IG/LinkedIn via Playwright) + scraper preventa Maps -> lead reali su Areus.
- **Owner:** Claude/Max
- **Avanzamento:** task board: 1/1 fatti
- **Entrypoint:** `Outreach/run_parallel.py` — presente
- **Prossimo passo:** Rinfrescare sessioni social (IG 54gg, LinkedIn 71gg) poi lanciare contatti via Playwright su target approvato (dry-run prima). Email SMTP gia' pronta: parte con 'via' + dry-run.
- **BLOCCO:** Invii a persone reali: irreversibili -> serve 'via' esplicito di Max + dry-run. Re-login social: atto fisico di Max (2FA).
