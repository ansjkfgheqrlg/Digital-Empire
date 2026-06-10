# Empire Studio - Uso diretto con Claude Code (senza estrazione)

**Aggiornamento importante (2026-06-07):** 

Utente: "senti ma forse non serve neanche che faccio l'estrazione claude code può guardare dentro i file .zip"

**Soluzione:** Sì. Non serve estrarre su Windows.

**Come fare:**

1. Scarica **SOLO** `empire-studio-clean.zip` dalla lista file della piattaforma (nella directory /home/user/).

2. Non estrarre nulla.

3. Carica o punta Claude Code direttamente sul file `empire-studio-clean.zip`.

4. Claude Code può:
   - Navigare dentro lo zip (molti tool AI coding come Claude Code / Cursor supportano browsing di zip senza estrarre).
   - Leggere tutti i file .md, .py, script, SKILL.md, playbook, 7-file agents, etc.
   - Analizzare la struttura completa (4 reparti, 15+ skills, workflow-deep-analyzer-agent con tutti i 7 file, strategie, memory, etc.).
   - Fare modifiche concettuali o generare patch basate su quanto c'è dentro lo zip.

**Vantaggi:**
- Eviti completamente l'errore Windows 0x80070057 e problemi di estrazione.
- Hai l'intera "immensità della struttura d'archettatura, tutti gli agenti, tutte le decine e decine di skill, tutti i file, tutti i flussi" in un singolo file pulito.
- Claude Code può "guardare dentro" e lavorare direttamente sul contenuto.

**Se il tuo Claude Code locale non supporta zip nativo:**
- Estrai solo con 7-Zip in un path corto (C:\EmpireStudio).
- Oppure chiedi qui e preparo una versione "flat" o tarball ancora più semplice.

**Contenuto del zip (Empire Studio completo):**
- Tutti i 4 reparti simmetrici (YouTube, TikTok, Web, Projects-Repos-Workloads)
- workflow-deep-analyzer-agent con **tutti i 7 file canonici** (inclusi playbook, tools, failure-modes, memory con le tue frasi esatte)
- 15+ skills complete (frame-extractor, repo-parser, atomic-note-creator, memory-checkpoint, visual-analyzer, projects-deep-study, etc.)
- Conductor, Strategy Department (full 7 files per Coordinator/Controller/Improver)
- Strategie multiple dettagliate + generate_strategy_manifest.py
- Memory ecosystem (checkpoints safe, projects-state)
- README, CATALOG, SKILL.md aggiornati e sanitizzati
- Tutto CLI-only, trace full, content-forge ready, 4th dept per deep study senza modificare originali

**Prossimo:**
Scarica il .zip, aprilo in Claude Code, e mandami il primo report di workflow/repo da far studiare al quarto reparto (usando il workflow-deep-analyzer-agent completo).

Tutto è lì dentro, pronto.

**Trace:** Risponde direttamente alla tua osservazione su estrazione non necessaria.
