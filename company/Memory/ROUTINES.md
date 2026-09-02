# ROUTINES.md — Indice delle automazioni schedulate di Digital Empire

> Creato 2026-09-02, ingestione video `8NSyI-npJCU` (Jay E | RoboNuggets, "The NEW Agentic OS standard for Claude 5 Models is here"). Ispirato al pattern "Level 2 Memory — router files" mostrato nel video (indice puntatore, non documentazione) e alla UI nativa "Routines" di Claude Code mostrata a schermo (descrizione + status + repeats + istruzioni). Vedi `second-brain-vault/wiki/sources/Source_Jay_E_Agentic_OS_Claude5.md`.
>
> **Metodo:** ogni voce qui sotto è stata verificata di persona in questa sessione — cercando script di scheduling reali (`scripts/`, `EmpireDesk/`, `.claude/skills/`), leggendo `.claude/settings.json` per gli hook, e interrogando **Windows Task Scheduler reale** su questa macchina (`Get-ScheduledTask` via PowerShell). Non è un elenco di intenzioni: dove un meccanismo esiste solo come codice/spec ma non risulta attivo, è marcato esplicitamente. Nessuna automazione è stata inventata.
>
> **Regola di manutenzione (presa in prestito dal video sorgente, fonte: 8NSyI-npJCU, 13:30):** quando un'automazione viene aggiunta, rimossa o rinominata, questo file va aggiornato nello stesso turno — un indice vecchio è peggio di nessun indice.

---

## 1. Automazioni ATTIVE e verificate su questa macchina

### 1.1 Sync bidirezionale del repo (hook Claude Code — evento, non orario fisso)
- **Cosa fa:** `git pull` all'apertura di ogni sessione Claude Code in questa directory, `git commit` + `rebase` + `push` alla chiusura. Lock anti-sovrapposizione, mai distruttivo (niente `reset --hard`/force push), rate-limit push 1 ogni 90s, conflitti scritti in `SYNC-CONFLICT.txt` invece di essere risolti in automatico.
- **Dove:** script `scripts/empire-sync.ps1` (modalità `pull`/`push`/`full`).
- **Trigger:** hook nativi Claude Code in `.claude/settings.json` → `hooks.SessionStart` (mode `pull`, timeout 90s) e `hooks.Stop` (mode `push`, timeout 120s).
- **Prova che gira davvero:** i commit `sync(Max): aggiornamento automatico ...` visibili nel log git (es. `9953611a`, `a7bcceab`, `cc3ecaf5` del 2026-09-02) sono generati da questo hook.
- **Non è un cron:** scatta a ogni sessione/chiusura di Claude Code, non a un orario fisso — per questo è "evento periodico", non "schedulata" in senso stretto, ma è l'automazione più frequente e verificabile del sistema.

### 1.2 Emperator hook (evento — ogni prompt)
- **Cosa fa:** inietta contesto/attivazione dell'agente Emperator a ogni messaggio inviato da Max/Gael in questa directory.
- **Dove:** `scripts/emperator_hook.py`.
- **Trigger:** `.claude/settings.json` → `hooks.UserPromptSubmit` (timeout 15s, statusMessage "EMPERATOR...").
- **Nota:** non è schedulata nel senso di "orario", ma è un'automazione ricorrente reale (ogni prompt), quindi inclusa per completezza.

### 1.3 graphify hook-guard (evento — su Bash/Grep e Read/Glob)
- **Cosa fa:** guardia eseguita prima di ogni uso di Bash/Grep o Read/Glob (verifica/instrada verso il knowledge graph di graphify).
- **Dove:** eseguibile `graphify.exe hook-guard search` / `hook-guard read`.
- **Trigger:** `.claude/settings.json` → `hooks.PreToolUse`.
- **Nota:** guardia di permessi/contesto, non un'automazione di produzione — inclusa solo per completezza dell'inventario hook.

### 1.4 LinkedIn Daily Outreach (Windows Task Scheduler)
- **Cosa fa:** warming (30 commenti su post di professionisti target) + step connection requests/messaggi/follow-up (20 connessioni/giorno).
- **Dove:** task Windows **"LinkedIn Daily Outreach"** → esegue `C:\LinkedIn_Bot\run.bat`, che a sua volta lancia `comment_posts.py` e `run_today.py` dentro `Outreach/LinkedIn Automation/` di questo repo.
- **Schedule verificato:** ricorrente ogni giorno alle 09:00. Stato: **Ready** (attivo). Ultima esecuzione registrata da Windows: 31/08/2026 11:31. Prossima esecuzione: 03/09/2026 09:00.
- **⚠️ Da verificare — salute:** il log `Outreach/LinkedIn Automation/run_today_log.txt` mostra errori ricorrenti `[ERRORE] Sessione LinkedIn scaduta. Esegui: python refresh_session.py` (ultima riga leggibile: 2026-08-12). Il task risulta schedulato e attivo lato Windows, ma non è verificato in questa sessione se le run recenti abbiano effettivamente completato il lavoro o siano fallite silenziosamente per sessione scaduta.

---

## 2. Automazioni REGISTRATE ma DISABILITATE o SCADUTE (Windows Task Scheduler)

Trovate durante la verifica reale (`Get-ScheduledTask`), riportate per completezza dell'indice — non sono operative oggi:

| Task | Stato | Schedule | Script | Note |
|---|---|---|---|---|
| `DigitalEmpire_LinkedIn_Daily` | **Disabled** | giornaliero 09:00 | `Outreach/LinkedIn Automation/run_daily.bat` (stessi 2 step di §1.4) | Sembra il predecessore di "LinkedIn Daily Outreach" (§1.4), disabilitato probabilmente perché sostituito dal task esterno `C:\LinkedIn_Bot\run.bat` — **da verificare quale dei due è quello da tenere**. |
| `DigitalEmpire_FollowupB1` | Ready, ma **one-time scaduto** (nessun NextRunTime) | avvio unico 2026-05-09 09:00 | `Outreach/Outreach Workflow/send_followup_b1.py --auto` | Campagna follow-up una tantum, già eseguita (ultimo risultato: successo, codice 0). |
| `DigitalEmpire_FollowupB2` | Ready, **one-time scaduto** | avvio unico 2026-05-12 09:00 | `Outreach/Outreach Workflow/send_followup_b2.py --auto` | Come sopra, già eseguita con successo. |
| `DigitalEmpire_FollowupB3` | Ready, **one-time scaduto** | avvio unico 2026-05-10 09:00 | `Outreach/Outreach Workflow/send_followup_b3.py --auto` | Ultima esecuzione con codice di errore (non indagato in questa sessione). |
| `DigitalEmpire_SendRemaining` | Ready, **one-time scaduto** | avvio unico 2026-05-09 09:30 | `Outreach/Outreach Workflow/send_all_remaining.bat` | Ultima esecuzione con codice di errore (non indagato in questa sessione). |

---

## 3. Infrastruttura di scheduling PRONTA ma senza run attive registrate (da verificare)

### 3.1 EmpireDesk — scheduler interno per-tile
- **Cosa fa (per progetto):** run programmate per "tile" (giorni + ora ricorrenti), con persistenza in `EmpireDesk/state/scheduler.json` e loop interno (poll ogni 30s) che lancia la tile schedulata se non già in corso (mai in coda, salta il giro e logga).
- **Dove:** `EmpireDesk/modules/scheduler.py`, montato da `app.py::start_module_background_tasks()` quando un motore GUI reale è avviato (mai durante `--selftest`).
- **Stato verificato in questa sessione:** il file `EmpireDesk/state/scheduler.json` **non è stato trovato su disco** → nessuna run risulta attualmente registrata nello scheduler. Il meccanismo esiste ed è cablato nell'app, ma **gira solo se EmpireDesk è aperto e solo se qualcuno ha aggiunto almeno una entry dal pannello**. Da verificare con Gael (owner Half B, dossier 17 §5.3) se EmpireDesk viene tenuto aperto in background su una macchina.

### 3.2 Auto-publisher social (script pronto, task non registrato)
- **Cosa fa (se attivato):** pubblicazione automatica giornaliera su Instagram/TikTok via `run_daily.py`, orchestrato da `.claude/skills/workflow-pubblicazione-auto/setup_scheduler.py` (duplicato anche in `SKILL & Agenti/Workflow pubblicazione automatica/setup_scheduler.py`), che crea un task Windows chiamato `DigitalEmpire_AutoPublisher` (`schtasks /Create ... /SC DAILY`).
- **Stato verificato in questa sessione:** **nessun task con nome `DigitalEmpire_AutoPublisher` risulta registrato** in Windows Task Scheduler su questa macchina. Lo strumento CLI è pronto (`python setup_scheduler.py --time HH:MM`) ma non risulta attivato qui — **da verificare se è attivo sulla macchina di Gael o se è stato deliberatamente non attivato**.

### 3.3 Agente `ops-scheduler` (ruolo definito, trigger cron reale non trovato)
- **Cosa dovrebbe fare (da spec):** "Cron/loop: pianifica e lancia run ricorrenti" per l'intera holding, verifica pre-condizioni (token/daemon/disco) via `ops-watchdog`, invoca solo i trigger ufficiali `avvia-*` senza toccare gli script interni.
- **Dove:** `company/Ecosistemi/09-OPERATIONS/Agenti/ops-scheduler.md` — ruolo L5 del reparto L2 SCHEDULING, tier Haiku.
- **Stato verificato in questa sessione:** è una **specifica di agente** (documento di ruolo con KPI ed escalation), non un processo cron reale trovato in esecuzione. Nessun collegamento verificato in questa sessione tra `ops-scheduler` e un vero trigger temporale (né Windows Task Scheduler, né un loop Python attivo). **Da verificare** come/se viene invocato realmente oggi.

---

## 4. Esplicitamente ESCLUSE da questo indice (non sono automazioni schedulate)

Le seguenti skill sono lanciatori **on-demand** (aprono una finestra CMD quando invocati da Max/Gael o da Claude), non girano da sole a un orario: `avvia-email`, `avvia-ig`, `avvia-linkedin`, `avvia-scraper`, `avvia-parallel`, `avvia-outreach-preventa`, `avvia-estate-wk`. Sono escluse da questo indice perché non sono "schedulate" nel senso del video sorgente (routine con `Repeats`/`Status: Active`) — sono trigger manuali.

---

## 5. Dichiarazione onesta di copertura

Questa ricerca ha coperto: `scripts/`, `.claude/settings.json` (hook), `EmpireDesk/`, `.claude/skills/*/setup_scheduler.py` (o simili), `company/Ecosistemi/09-OPERATIONS/Agenti/`, e un'interrogazione reale di **Windows Task Scheduler** su questa macchina (non solo grep di codice). Non è stata verificata la macchina di Gael, né eventuali cron su server remoti/cloud (Hermes-equivalenti) se esistenti altrove nell'ecosistema DE. Se emergono altre automazioni schedulate in futuro, vanno aggiunte qui **nello stesso turno** in cui vengono create — non a posteriori.
