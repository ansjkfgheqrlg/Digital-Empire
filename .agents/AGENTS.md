# REGOLE ASSOLUTE DI PROGETTO E DEL MANDATO EMPIRE (ADR-008 / Art. 8)

## 1. REGOLA SUPREMA DEL WORKFLOW REALE E AUTOCONTENUTO (Articolo 8 del Mandato Empire)
**Ogni volta che si crea un workflow o quando l'utente (Max) chiede di vedere o creare un workflow (es. `WORKFLOW-ESTATE/`), DEVE essere creata o mantenuta una singola cartella principale radice e autocontenuta nel monorepo che racchiude l'intera sua struttura a 360 gradi.**
Non è mai permesso creare un workflow fatto solo di un file di testo `.md` che punta ad asset sparsi, teorici o inesistenti.

Ogni cartella di workflow suprema DEVE contenere al suo interno i 6 pilastri operativi e tangibili:
1. **Flussi & Piani (`01-FLUSSI-E-PIANI/`):** Tutti i file `.md` e `workflows.yaml` di orchestrazione e sequenza logica.
2. **Automazioni & Scripts (`02-AUTOMAZIONI-E-SCRIPTS/`):** Tutti gli script in Python (`.py`), Bash (`.sh`) e PowerShell (`.ps1`, `.bat`) eseguibili che fanno girare concretamente il workflow (es. `memory_manager.py`, script invio email/WA, scraping, render).
3. **Agenti & Ruoli (`03-AGENTI-E-RUOLI/`):** Tutti gli agenti (`.md`/`.yaml`) con i loro ruoli precisi, i prompt e i confini di responsabilità (es. Max, Gael, Claude, Chief-Forge, closer-a8, cro-copy-architect).
4. **Skills & Reference (`04-SKILLS-E-REFERENCE/`):** Tutte le skill collegate (`SKILL.md`) e le reference operative/metodologiche (es. `checklist_APSOC.md`, `playbook.md`).
5. **Templates & Kit (`05-TEMPLATES-E-KIT/`):** I kit di vendita, i preventivi brandizzati, i caroselli pronti, i copy e le sequenze email di delivery.
6. **Dashboard & Metriche (`06-DASHBOARD-E-METRICHE/`):** Le tabelle di monitoraggio e i KPI quantificati e reali (`DASHBOARD.md`, `LISTA-LEAD.md`).

## 2. BRAND VOICE E PROVA TANGIBILE (CPB / APSOC)
- Mai fare affermazioni, promesse o stime percentuali senza dati verificabili (Struttura CPB: Claim -> Proof -> Benefit).
- Nelle comunicazioni e nel copy applicare sempre il framework APSOC (Attention -> Problem -> Solution -> Offer -> Close) superando lo score >= 92% della Checklist APSOC di Andrei Pascu.
