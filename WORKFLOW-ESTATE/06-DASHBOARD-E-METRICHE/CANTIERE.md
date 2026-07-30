# CANTIERE — presa di costruzione del Workflow Estate sui modelli operativi

> Generato da `empire cantiere` il 2026-07-30. Non modificare a mano: si rigenera.

Il cervello (WORKFLOW-ESTATE) governa questi modelli operativi. Per ognuno: dove sta il
prossimo passo di costruzione, chi lo possiede, se e' bloccato, se il codice esiste davvero.

## YOUTUBE-AUTOMATION-FACTORY  (`youtube`)

- **Ruolo:** Genera video YouTube in automatico (pipeline APEX-7 a 6 fasi F1-F6).
- **Owner:** Gael
- **Avanzamento:** task board: 7/7 fatti
- **Entrypoint:** `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS` — presente
- **Prossimo passo:** AGGIORNATO 2026-07-30: TASK-YT-006 CHIUSA (non migrato, motivazione scritta - clausola esplicita del gate; verificato al merge che 12-STREAM-S7-BOT ha ancora la sua implementazione APEX-7 propria, zero import da 11-APEX-7-CORE). YouTube 7/7 lotti chiusi. NOTA MERGE: i lotti TASK-YT-001..007 risultano eseguiti DUE VOLTE in parallelo da due sessioni che non si vedevano; sopravvive l'orchestratore con dashboard_path overridabile (richiesto dal test mergiato) + il ritiro additivo di run_youtube_apex7.py (deprecato con banner, non cancellato). Operativo residuo per Max: pubblicare davvero un video (upload Playwright) per chiudere il loop di audit F6 con dati veri.

## 12-STREAM-S7-BOT  (`stream-s7`)

- **Ruolo:** Bot trading Solana su segnali stream (paper trading per design).
- **Owner:** Gael/Claude
- **Avanzamento:** task nel board: nessuno con questi prefissi
- **Entrypoint:** `company/Ecosistemi/12-STREAM-S7-BOT/main.py` — presente
- **Prossimo passo:** AGGIORNATO 2026-07-30: chiusa TASK-GAEL-20260730-STREAM-S7-NFT-METODO (layer NFT floor-rarity mismatch su Magic Eden, 78/78 controlli reali, CP-20260730-002..007). VERDETTO: bocciato per live anche sulla lane NFT - l'edge non e' statisticamente distinguibile da zero al 95% (IC95% -2.00%/+34.70% sull'unica collection con segnale). Resta valido il passo tecnico precedente: L2->L3 (collegare analysis_engine/execution_engine al ciclo Orchestrator->Gate->Memory, tarare le soglie su esecuzioni misurate). Per un eventuale pilot live servono 3 prerequisiti OGGI ASSENTI: (a) RPC Solana a pagamento per l'esecuzione, (b) tasso storico reale di rug/abbandono su collection blue-chip, (c) piu' storico/collection per un campione solido.
- **BLOCCO:** B-010 (BACKLOG.md): serve un RPC provider a pagamento prima di qualunque LIVE reale. Decisione capitale = Max.

## Outreach (concessionari preventa + content/outreach factory)  (`outreach`)

- **Ruolo:** Contatto concessionari (email/IG/LinkedIn via Playwright) + scraper preventa Maps -> lead reali su Areus.
- **Owner:** Claude/Max
- **Avanzamento:** task board: 1/1 fatti
- **Entrypoint:** `Outreach/run_parallel.py` — presente
- **Prossimo passo:** Rinfrescare sessioni social (IG 54gg, LinkedIn 71gg) poi lanciare contatti via Playwright su target approvato (dry-run prima). Email SMTP gia' pronta: parte con 'via' + dry-run.
- **BLOCCO:** Invii a persone reali: irreversibili -> serve 'via' esplicito di Max + dry-run. Re-login social: atto fisico di Max (2FA).
