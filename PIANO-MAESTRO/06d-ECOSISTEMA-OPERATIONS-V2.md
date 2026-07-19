# ⚙️ 06d — ECOSISTEMA OPERATIONS V2 (Dossier EMPIRE OS)

> Dossier v2 (V2-2, ADR-007) — amplia a scala CF-grade la sezione "09 · OPERATIONS"
> del v1 `06-ECOSISTEMI-CORE.md` (righe ~381-495). Fonte: `11-PIANO-V2-DIRETTIVA-SCALA.md` §2.
>
> **Origine di questo file:** il v1 `06-ECOSISTEMI-CORE.md` copriva in un solo dossier i
> 4 ecosistemi core trasversali (PLATFORM · FORGE · INTELLIGENCE · OPERATIONS). In V2-2
> Lotto 3 è stato deciso di SPLITTARLI in 4 dossier V2 indipendenti — uno per ecosistema,
> come già fatto per i business 01-05. Questo file copre **solo OPERATIONS**; gli altri tre
> sono [[06a-ECOSISTEMA-PLATFORM-V2]], [[06b-ECOSISTEMA-FORGE-V2]] e
> [[06c-ECOSISTEMA-INTELLIGENCE-V2]] (quest'ultimo scritto in coppia con questo). La matrice
> di dipendenza tra i 4 core resta quella del v1 (Chiusura, righe ~508-521):
> `INTELLIGENCE → FORGE → PLATFORM`, con **OPERATIONS trasversale a tutti e tre** (fornisce
> runtime, cost guard, scheduling e osservabilità a INTELLIGENCE, FORGE e PLATFORM insieme,
> oltre che ai 5 ecosistemi business). Il v1 resta intatto come riferimento.
>
> **Ecosistema L1 #09 della holding Digital Empire Group.** Metafora OS: *scheduler + power
> management*. Versione: 2.0 · Creato: 2026-07-19 · Fase roadmap: V2-2 Lotto 3
> Standard: CF-grade (§0 piano V2 `11-PIANO-V2-DIRETTIVA-SCALA.md`).

---

## 0. Missione + DONE WHEN

**MISSIONE:** essere il runtime della holding: eseguire la produzione di massa (swarm),
schedulare i flussi ricorrenti (cron/loop), **fare da guardiano dei costi di TUTTA la
holding** (budget guard + cost attribution per agente/ecosistema/commessa), gestire storage e
asset, monitorare i processi e dare alla Board una dashboard unica leggibile in 30 secondi.
OPERATIONS non decide COSA produrre (lo decidono i business) ma COME gira e QUANTO costa.

**Principio ereditato dal v1, non negoziabile in v2:** OPERATIONS è **l'ecosistema più
Haiku-heavy della holding** — lavoro ripetitivo e schematico, deve costare poco per
definizione (predica col proprio esempio). In v2 questo si traduce in una regola di roster
esplicita: **tier Haiku/WASM per la maggioranza degli agenti operativi, Sonnet/Opus riservati
solo a coordinatori di reparto e a decisioni che richiedono giudizio** (budget guard, gate,
dashboard building). Il roster §3 rispetta questo principio: su 37 agenti totali, 24 sono
Haiku (~65%).

**DONE WHEN (misurabili):**
1. I 5 reparti L2 hanno org L3/L4 documentata, team 6-10 agenti a schede millimetriche, e
   almeno un workflow CF-grade eseguito end-to-end ciascuno.
2. Ogni run (outreach, build siti, ingestioni, content) emette evento standard
   `{ecosistema, workflow, costo, durata, esito}` raccolto in un ledger unico (namespace
   `operations/cost/ledger`).
3. Budget guard attivo su tutti i workflow censiti: nessun workflow può sforare il budget
   dichiarato — blocco PRIMA dello sforo (pattern #9 Piano Maestro), dry-run di default
   (pattern #3).
4. Le run outreach giornaliere (`avvia-email`, `avvia-ig`, `avvia-parallel`) girano
   schedulate e monitorate, non più lanciate a mano — 7 giorni consecutivi senza intervento.
5. Dashboard unica: stato run, costi per ecosistema, alert sentinels — leggibile in 30 secondi
   (evoluzione di `outreach-dashboard-premium`, verificato su disco in `Outreach/`).
6. Quota di task eseguiti su tier economico (WASM/Haiku) ≥70% (KPI v1, confermato in v2).
7. I namespace AgentDB `operations/` sono inizializzati; ogni workflow produce state
   ripartibile a freddo (test amnesia §6 piano V2).
8. Skill proprie dell'ecosistema forgiate (≥3: `empire-swarm`, `cost-ledger`,
   `budget-guard`) via 06b-FORGE con PRD+architettura (standard §8 piano V2).

**OUT OF SCOPE (ora, invariato dal v1):** spese API/crediti senza ok esplicito di Max
(OUT-OF-SCOPE #1 Piano Maestro); modifica dei flussi outreach attivi (`Outreach/*.py`,
`*.bat` — sono in produzione, 6 team Nemotron a €0/giorno: si WRAPPANO, non si toccano);
decisione su COSA produrre (spetta ai business, non a OPERATIONS).

---

## 1. Posizione nella holding — OPERATIONS è il motore che fa girare tutti

```
                    👑 LX — Mandato Empire (OUT-OF-SCOPE #1: zero spese senza ok Max)
                              |
L0  C-Suite ────── CFO/COO (supervisione costi e runtime) ──┤
                              |
L1  09-OPERATIONS ◄────── handoff contract ──────► TUTTI gli altri ecosistemi (i 5 business
        │                                           + i 3 core PLATFORM/FORGE/INTELLIGENCE)
        ├── DIPENDE DA: 06b-FORGE (registrazione nel cost model di ogni nuovo agente/team),
        │              06a-PLATFORM (scrive gli script di scheduling/dashboard che
        │              OPERATIONS usa — PLATFORM li scrive, OPERATIONS li usa)
        └── SERVE:    TUTTI — runtime swarm, scheduling, budget guard, storage, monitoraggio,
                      dashboard. È l'unico ecosistema con cui OGNI altro ha un handoff
                      obbligatorio bidirezionale (ogni run passa da qui e ogni run genera
                      un evento di ritorno)
```

### 1.1 Handoff espliciti — chi chiede cosa a OPERATIONS

| Committente | Cosa richiede | Formato tipico | Reparto / Workflow destinazione |
|---|---|---|---|
| **QUALSIASI ecosistema** | Esecuzione run (swarm, batch, singola) entro budget dichiarato | `{workflow, parametri, budget_max, schedule}` | RUNTIME — WF-SWARM-RUN / WF-QUEUE |
| **01 AGENCY** | Scheduling run outreach giornaliere (avvia-email/ig/parallel) | `cron` | SCHEDULING — WF-CRON |
| **02 INFO-BUSINESS** | Scheduling email lancio, costi lancio | `cron`, `budget_max` | SCHEDULING + COST GUARD |
| **03 CONTENT-FACTORY** | Mass-production swarm, render queue | `swarm --parallel N --budget N` | RUNTIME — WF-SWARM-RUN |
| **04 MARKETING** | Budget ads guard, cost attribution per campagna | `budget_max`, `commessa` | COST GUARD — WF-BUDGET / WF-ATTRIBUTION |
| **05 MULTI-BUSINESS** | Batch produzione libri/video, cron pubblicazione | `swarm`, `cron` | RUNTIME + SCHEDULING |
| **06a PLATFORM** | Evento costo/durata/esito per ogni build/deploy | `{commessa, costo, durata, esito}` | COST GUARD — WF-ATTRIBUTION |
| **06b FORGE** | Registrazione nel cost model di ogni nuovo agente (tier, costo stimato/run) | `{agente, tier, costo_stimato}` | COST GUARD — WF-TIER-ROUTING |
| **06c INTELLIGENCE** | Log/metriche delle run da distillare in pattern; scheduling di WF-WIKI-GARDEN/WF-TREND | `{run_log}`, `cron` | MONITORING (log) + SCHEDULING (cron) |
| **TUTTI** | Alert: budget all'80%, run fallita, drift di costo, processo zombie | evento push | MONITORING & DASHBOARD — WF-WATCH |
| **Board (L0)** | Report costi settimanale per ecosistema + dashboard | `report` | MONITORING & DASHBOARD — WF-BOARD-REPORT |

**Regola non negoziabile:** nessun workflow gira in produzione reale senza essere passato
prima da un dry-run con stima costi (pattern #3, G-DRYRUN) e senza un budget dichiarato
(G-BUDGET). Nessuna eccezione, nemmeno per run interne di OPERATIONS su se stesso.

### 1.2 Contratto di richiesta run (handoff contract standard)

```json
{
  "ecosistema_richiedente": "01-AGENCY | 02-INFO | 03-CF | 04-MKT | 05-MB | 06a-PLT | 06b-FRG | 06c-INT",
  "workflow": "nome del workflow da eseguire",
  "parametri": "payload specifico del workflow",
  "budget_max": "numero (valuta) — obbligatorio",
  "schedule": "immediate | cron_expr | one-shot YYYY-MM-DD HH:MM",
  "dry_run": "true (default) | false — richiede conferma esplicita per false"
}
```

Risposta di OPERATIONS: `{esito, costo_reale, durata, tier_usato, evento_ledger_id,
alert_generati}`. Campi opzionali: `priorita` (per arbitraggio codaco tra committenti),
`rollback_plan` (obbligatorio per workflow schedulati — G-RUNBOOK).

**Regole del contratto (non negoziabili):**
- Richiesta senza `budget_max` → COST GUARD rifiuta la run prima ancora che RUNTIME la spawni.
- Richiesta con `dry_run: false` senza conferma esplicita umana → bloccata (Art.4.3 Mandato,
  OUT-OF-SCOPE #1).
- Run schedulata senza `rollback_plan` → SCHEDULING rifiuta la schedulazione (G-RUNBOOK).

---

## 2. Reparti L2 v2 — 5 reparti (stessi del v1, portati a scala CF-grade)

```
09-OPERATIONS (L1) — coordinatore: OPS-Conductor
 ├── L2.1 RUNTIME                 ← esecuzione swarm: fan-out, worker pool, merge, retry, queue
 ├── L2.2 SCHEDULING              ← cron/loop: outreach, wiki-garden, trend-radar, token watch
 ├── L2.3 COST GUARD              ← il guardiano della holding intera: budget, attribution, tier
 ├── L2.4 STORAGE & ASSETS        ← naming, dedup, retention, backup/restore
 └── L2.5 MONITORING & DASHBOARD  ← health check, alert, dashboard, report Board
```

Nessun reparto nuovo rispetto al v1 (a differenza di 04-MARKETING che ne aveva aggiunti 2):
i 5 reparti del v1 coprono già l'intero perimetro runtime/costo/storage/osservabilità della
holding. L'espansione v2 è in **profondità** (team 6-10 con lead+QA su ogni reparto, dove il
v1 aveva 1-2 agenti condivisi senza gerarchia) e in **workflow CF-grade** (da 0 workflow
espliciti nel v1 a 1-5 per reparto).

---

### L2.1 — RUNTIME (esecuzione swarm — il motore di produzione di massa)

**Missione:** eseguire la produzione di massa via pattern CF `swarm.sh --parallel N --budget
N` (portato da Content Factory Exponium, non copiato: riscritto in versione DE) e la coda
di job/render con priorità, concorrenza e backpressure. RUNTIME non decide il budget (lo fa
COST GUARD) e non decide COSA produrre (lo decide il business committente): esegue.

**Dove il v1 era carente:** il v1 aveva solo `ops-swarm-marshal` come agente nominato, con le
funzioni L4 (`T-fanout`, `T-worker-pool`, `T-merge-results`, `T-retry-failed`) elencate ma
senza owner esplicito né QA di reparto. In v2 ogni funzione L4 ha un agente owner.

#### Team L2.1 (8 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `RUN-LEAD` | Runtime Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; riceve la richiesta di run dal contratto §1.2, sceglie la strategia di esecuzione (fan-out vs sequenziale), risponde dei tempi di completamento |
| `RUN1` | Swarm Marshal | worker | sonnet | (ex `ops-swarm-marshal`) Orchestrazione swarm: fan-out, `--parallel N`, merge risultati |
| `RUN2` | Worker Pool Manager | worker | haiku | **NUOVO v2:** gestisce il pool di worker/concorrenza disponibili, evita saturazione |
| `RUN3` | Fanout Sharder | worker | haiku | **NUOVO v2:** T-fanout — divide il lavoro in shard assegnabili in parallelo |
| `RUN4` | Merge Operator | worker | haiku | **NUOVO v2:** T-merge-results — consolida i risultati degli shard in output unico |
| `RUN5` | Retry Handler | worker | haiku | **NUOVO v2:** T-retry-failed — rilancia SOLO gli shard falliti, mai l'intero batch |
| `RUN6` | Queue Manager | worker | haiku | **NUOVO v2:** WF-QUEUE — priorità, concorrenza, backpressure sulla coda job/render |
| `RUN-QA` | Runtime QA Verifier | verifier | sonnet | **NUOVO v2:** verifica che ogni run rispetti il dry-run di default e il budget dichiarato PRIMA dell'esecuzione reale (gate G-DRYRUN) |

#### Workflow L3 di L2.1 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-SWARM-RUN** | Produzione di massa: pattern CF `swarm.sh --parallel N --budget N` — fan-out (RUN3), worker pool (RUN2), merge (RUN4), retry (RUN5) | RUN-QA verifica G-DRYRUN prima; COST GUARD approva budget; esito nel ledger |
| **WF-QUEUE** | Render/job queue (pattern render queue CF): priorità, concorrenza, backpressure | RUN6 verifica nessun job perso; backpressure attiva sotto soglia di saturazione |
| **WF-DRY-RUN-VALIDATE** | **NUOVO v2:** ogni workflow nuovo o modificato gira PRIMA in dry-run con stima costi, poi richiede conferma esplicita per la run reale | Stima costi prodotta; conferma umana loggata prima di `dry_run: false` |

---

### L2.2 — SCHEDULING (cron/loop — i flussi ricorrenti della holding)

**Missione:** far girare in automatico ciò che oggi gira a mano o rischia di essere
dimenticato: run outreach giornaliere, manutenzione wiki, radar trend, e qualsiasi altro
flusso ricorrente dichiarato da un ecosistema. **Wrappa senza modificare** gli script
outreach attivi verificati su disco in `Outreach/` (`run_parallel.py`, `run_ig_email.py`,
`run_all.bat`, `AVVIA-EMAIL-LIVE.bat`, `AVVIA-DASHBOARD.bat`, `TEST-EMAIL-10.bat`,
`rerun_partial.py`, `run_followup_b3.bat`, `run_linkedin_only.py`, `start-dashboard.bat`).

**Dove il v1 era carente:** un solo agente (`ops-scheduler`), nessun owner esplicito per lo
scheduling degli specifici flussi outreach, nessun agente dedicato al monitoraggio delle
scadenze token (citate nel v1 come rischio "token FB scaduto" ma senza owner chiaro fino a
`ops-watchdog`, che in v2 resta in MONITORING — qui SCHEDULING presidia la *pianificazione*
preventiva, MONITORING la *rilevazione* a runtime).

#### Team L2.2 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `SCHED-LEAD` | Scheduling Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; mantiene il calendario unico di tutti i cron/loop della holding, arbitra conflitti di orario |
| `SCH1` | Scheduler | worker | haiku | (ex `ops-scheduler`) Cron/loop generico: pianifica e lancia run ricorrenti |
| `SCH2` | Outreach Cron Keeper | worker | haiku | **NUOVO v2:** SPECIFICO per `avvia-email`/`avvia-ig`/`avvia-parallel` — schedula SENZA modificare i flussi attivi (ADR-003) |
| `SCH3` | Wiki-Garden Scheduler | worker | haiku | **NUOVO v2:** schedula `WF-WIKI-GARDEN` e `WF-TREND` in coordinamento con 06c-INTELLIGENCE |
| `SCH4` | Loop Coordinator | worker | haiku | **NUOVO v2:** gestisce le skill `loop`/`schedule` (cloud agents cron) per run self-paced |
| `SCH5` | Token Expiry Pre-Watcher | worker | haiku | **NUOVO v2:** verifica in anticipo le scadenze token (es. token FB) PRIMA che una run schedulata fallisca; propone ri-schedulazione preventiva |
| `SCH-QA` | Scheduling QA Verifier | verifier | sonnet | **NUOVO v2:** verifica che ogni run schedulata abbia `rollback_plan` e runbook (gate G-RUNBOOK) prima di attivarla |

#### Workflow L3 di L2.2 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-CRON** | Run ricorrenti: outreach giornaliero (avvia-email/ig/parallel), wiki-garden, trend-radar | SCH-QA verifica G-RUNBOOK; SCH2 non tocca i file outreach attivi |
| **WF-LOOP** | Loop self-paced su condizione (skill `loop`/`schedule`) | SCH4; condizione di stop esplicita, mai loop infinito senza budget |
| **WF-SCHEDULE-AUDIT** | **NUOVO v2:** verifica periodica che tutte le run schedulate abbiano ancora un runbook valido e token non in scadenza | SCH5 + SCH-QA; report settimanale a MONITORING |

---

### L2.3 — COST GUARD (il guardiano della holding intera)

**Missione:** essere il reparto che rende impossibile sforare un budget. Budget per
workflow/ecosistema, blocco pre-sforo (mai dopo), approvazione spese (OUT-OF-SCOPE #1: zero
spese API senza ok esplicito di Max), cost attribution per agente/run/commessa, enforcement
del routing 3-tier (WASM/Haiku/Sonnet-Opus: il modello giusto per il task giusto).

**Dove il v1 era carente:** 3 agenti (`ops-cost-sentinel`, `ops-cost-accountant`,
`ops-tier-router`) senza lead di reparto, senza un agente che gestisca esplicitamente il
"chiedi ok a Max" per le spese reali, e senza previsione di trend costo (solo misurazione a
posteriori). In v2 il reparto — il più critico della holding insieme a MONITORING — ha 8
agenti con gerarchia completa.

#### Team L2.3 (8 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `COST-LEAD` | Cost Guard Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; punto di escalation per ogni richiesta di spesa reale; risponde del ledger davanti alla Board/CFO |
| `CG1` | Cost Sentinel | verifier | sonnet | (ex `ops-cost-sentinel`) Sentinel always-on: budget guard, blocco pre-sforo, alert all'80% |
| `CG2` | Cost Accountant | worker | haiku | (ex `ops-cost-accountant`) Ledger: attribution per agente/run/commessa/ecosistema |
| `CG3` | Tier Router | worker | haiku | (ex `ops-tier-router`) Enforcement 3-tier routing + Thompson Sampling (via Ruflo) |
| `CG4` | Budget Approval Gatekeeper | worker | haiku | **NUOVO v2:** gestisce le richieste di "ok umano" per spese API reali (OUT-OF-SCOPE #1); instrada a Max, blocca fino a risposta |
| `CG5` | Cost Forecast Analyst | worker | haiku | **NUOVO v2:** proietta il costo settimanale/mensile per ecosistema sulla base del ledger, alimenta il report Board |
| `CG6` | Anomaly Detector | worker | haiku | **NUOVO v2:** rileva spike di costo anomali (drift) rispetto al trend storico, allerta CG1 |
| `CG-QA` | Cost Guard QA Verifier | verifier | sonnet | **NUOVO v2:** verifica copertura ledger ≥98%: nessuna run senza evento costo attribuito (gate G-ATTRIBUTION) |

#### Workflow L3 di L2.3 (5 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-BUDGET** | Budget per workflow/ecosistema; blocco pre-sforo; approvazione spese reali | CG1 blocca prima dello sforo; CG4 gestisce l'ok umano per spesa reale |
| **WF-ATTRIBUTION** | Cost attribution per agente/run/commessa → ledger | CG-QA verifica copertura ≥98% |
| **WF-TIER-ROUTING** | Enforcement 3-tier (WASM/Haiku/Sonnet-Opus): il modello giusto per il task giusto | CG3; KPI quota task su tier economico ≥70% |
| **WF-COST-FORECAST** | **NUOVO v2:** proiezione costo settimanale/mensile per ecosistema | CG5; alimenta `WF-BOARD-REPORT` di MONITORING |
| **WF-ANOMALY-DETECT** | **NUOVO v2:** rilevazione drift di costo anomalo rispetto al trend | CG6 allerta CG1; nessun blocco automatico senza conferma CG1 (anti falso positivo) |

---

### L2.4 — STORAGE & ASSETS (naming, dedup, retention, backup)

**Missione:** governare lo storage multi-tenant della holding — asset (immagini, video,
export) con naming coerente, deduplicazione, retention per tipo, e un ciclo di
backup/restore effettivamente testato (non solo dichiarato).

**Dove il v1 era carente:** 2 agenti (`ops-asset-keeper`, `ops-backup-op`), nessun lead di
reparto, nessuna policy di retention esplicita differenziata per tipo/ecosistema, nessun
collegamento diretto tra "spazio occupato" e COST GUARD.

#### Team L2.4 (6 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `STOR-LEAD` | Storage & Assets Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; definisce le convenzioni di naming/retention per l'intera holding |
| `ST1` | Asset Keeper | worker | haiku | (ex `ops-asset-keeper`) Storage, naming, dedup, retention asset |
| `ST2` | Backup Operator | worker | haiku | (ex `ops-backup-op`) Backup + restore test periodico |
| `ST3` | Retention Policy Enforcer | worker | haiku | **NUOVO v2:** applica la policy di retention per tipo asset/ecosistema, elimina ciò che è scaduto |
| `ST4` | Storage Cost Liaison | worker | haiku | **NUOVO v2:** collega lo spazio occupato a COST GUARD (lo storage È un costo, non un dato neutro) |
| `ST-QA` | Storage QA Verifier | verifier | haiku | **NUOVO v2:** verifica che il restore mensile sia stato effettivamente testato e verde (KPI v1) |

#### Workflow L3 di L2.4 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-ASSET-MGMT** | Asset (immagini, video, export) con naming, dedup, retention | ST1 + ST3; zero duplicati non tracciati |
| **WF-BACKUP** | Backup wiki/knowledge/registry + restore testato | ST2 esegue; ST-QA verifica il restore |
| **WF-RESTORE-TEST** | **NUOVO v2:** esecuzione mensile tracciata del test di restore (formalizza il KPI v1 "1/mese, verde") | ST-QA verde; risultato in `operations/storage/restore-log` |

---

### L2.5 — MONITORING & DASHBOARD (osservabilità e report Board)

**Missione:** sapere sempre, in tempo reale, cosa sta girando, cosa è fallito, quanto costa
e se qualcosa sta per scadere (token, licenze) — e restituire tutto questo alla Board in una
dashboard leggibile in 30 secondi. **Evolve** (non riscrive da zero) `outreach-dashboard-
premium`, verificato su disco in `Outreach/outreach-dashboard-premium/` (progetto Next.js
con `package.json`, `README.md`, `AGENTS.md`, `CLAUDE.md` propri).

**Dove il v1 era carente:** 2 agenti (`ops-watchdog`, `ops-dashboard-builder`), nessun lead
di reparto, nessun agente dedicato all'instradamento degli alert (chi riceve cosa) e nessun
processo esplicito di compilazione del report settimanale per la Board.

#### Team L2.5 (7 agenti)

| ID | Agente | Tipo | Tier | Ruolo operativo |
|---|---|---|---|---|
| `MON-LEAD` | Monitoring & Dashboard Lead | coordinator | sonnet | **NUOVO v2:** coordina il reparto; risponde della leggibilità "in 30 secondi" della dashboard davanti alla Board |
| `MON1` | Watchdog | worker | haiku | (ex `ops-watchdog`) Health check: run attive, daemon Ruflo, token in scadenza, processi zombie |
| `MON2` | Dashboard Builder | worker | sonnet | (ex `ops-dashboard-builder`) Mantiene la dashboard (con 06a-PLATFORM per il codice: PLATFORM scrive, OPERATIONS usa) |
| `MON3` | Alert Dispatcher | worker | haiku | **NUOVO v2:** instrada ogni alert (budget 80%, run fallita, drift di costo, processo zombie) al destinatario giusto senza rumore |
| `MON4` | Token Expiry Sentinel | worker | haiku | **NUOVO v2:** monitora a runtime le scadenze token OAuth/API (es. token FB) — complementa SCH5 (che pianifica in anticipo, questo rileva a runtime) |
| `MON5` | Weekly Report Compiler | worker | haiku | **NUOVO v2:** compila il report costi settimanale per Board (usa l'output di CG5 Cost Forecast Analyst) |
| `MON-QA` | Monitoring QA Verifier | verifier | sonnet | **NUOVO v2:** verifica che la dashboard sia effettivamente leggibile in 30s e priva di dati stale (KPI v1) |

#### Workflow L3 di L2.5 (3 workflow CF-grade)

| Workflow | Scopo | Gate di uscita |
|---|---|---|
| **WF-WATCH** | Health check processi (run attive, daemon Ruflo, token in scadenza) | MON1; tempo di rilevazione run fallita ≤15 min (KPI v1) |
| **WF-DASHBOARD** | Dashboard unica Board (estende `outreach-dashboard-premium`) | MON2 + MON-QA; leggibile in 30s |
| **WF-BOARD-REPORT** | **NUOVO v2:** report costi settimanale automatico per la Board (usa `WF-COST-FORECAST` di COST GUARD) | MON5 compila; MON-QA verifica dati non stale prima dell'invio |

---

## 3. Roster agenti completo (tutti i reparti)

### OPS-Conductor (L1)

| ID | Agente | Tipo | Tier | Ruolo |
|---|---|---|---|---|
| `OPS-0` | OPS-Conductor | coordinator | opus | (ex `ops-director`) Coordinatore ecosistema L1: riceve handoff dal BUS, valida il contratto §1.2, smista ai reparti, gestisce coda multi-committente, SLA run, priorità code, report Board, escalation a C-Suite (CFO/COO) |

### L2.1 Runtime (8 agenti)

`RUN-LEAD` [nuovo] · `RUN1` · `RUN2` [nuovo] · `RUN3` [nuovo] · `RUN4` [nuovo] · `RUN5` [nuovo] · `RUN6` [nuovo] · `RUN-QA` [nuovo]

### L2.2 Scheduling (7 agenti)

`SCHED-LEAD` [nuovo] · `SCH1` · `SCH2` [nuovo] · `SCH3` [nuovo] · `SCH4` [nuovo] · `SCH5` [nuovo] · `SCH-QA` [nuovo]

### L2.3 Cost Guard (8 agenti)

`COST-LEAD` [nuovo] · `CG1` · `CG2` · `CG3` · `CG4` [nuovo] · `CG5` [nuovo] · `CG6` [nuovo] · `CG-QA` [nuovo]

### L2.4 Storage & Assets (6 agenti)

`STOR-LEAD` [nuovo] · `ST1` · `ST2` · `ST3` [nuovo] · `ST4` [nuovo] · `ST-QA` [nuovo]

### L2.5 Monitoring & Dashboard (7 agenti)

`MON-LEAD` [nuovo] · `MON1` · `MON2` · `MON3` [nuovo] · `MON4` [nuovo] · `MON5` [nuovo] · `MON-QA` [nuovo]

### Conteggio roster v2

| Categoria | Agenti esistenti (dal v1) | Agenti nuovi v2 | Totale | di cui Haiku |
|---|---|---|---|---|
| OPS-Conductor (L1) | 1 (ex ops-director) | 0 | 1 | 0 |
| L2.1 Runtime | 1 (RUN1 ex ops-swarm-marshal) | 7 | 8 | 5 |
| L2.2 Scheduling | 1 (SCH1 ex ops-scheduler) | 6 | 7 | 5 |
| L2.3 Cost Guard | 3 (CG1-CG3 ex sentinel/accountant/tier-router) | 5 | 8 | 5 |
| L2.4 Storage & Assets | 2 (ST1-ST2 ex asset-keeper/backup-op) | 4 | 6 | 5 |
| L2.5 Monitoring & Dashboard | 2 (MON1-MON2 ex watchdog/dashboard-builder) | 5 | 7 | 4 |
| **TOTALE** | **10** | **27** | **37** | **24 (~65%)** |

*(Il v1 aveva 10 agenti registrati. In v2 se ne riusano tutti e 10 con ruolo promosso e se ne
aggiungono 27 per portare ogni reparto allo standard 6-10 con lead + QA + specialisti. Tier:
1 Opus (conductor), 12 Sonnet (5 lead di reparto + CG1 + MON2 + 5 QA "di giudizio"), 24 Haiku
— rispetta il principio "OPERATIONS più Haiku-heavy della holding" del v1.)*

---

## 4. Workflow chiave CF-grade

### (a) Routing richieste — flusso di ingresso principale

```
[Ecosistema richiedente]
   │  handoff contract {ecosistema_richiedente, workflow, parametri, budget_max, schedule, dry_run}
   ▼
OPS-Conductor ──► valida contratto (budget_max presente? workflow riconosciuto?)
   │
   ▼  ROUTING PER TIPO
   ├─ esecuzione immediata / batch     → L2.1 RUNTIME (WF-SWARM-RUN / WF-QUEUE)
   ├─ ricorrente (cron/loop)           → L2.2 SCHEDULING (WF-CRON / WF-LOOP)
   ├─ verifica budget PRIMA di tutto   → L2.3 COST GUARD (WF-BUDGET) — SEMPRE, non bypassabile
   ├─ asset/backup                     → L2.4 STORAGE & ASSETS
   └─ solo osservabilità/report        → L2.5 MONITORING & DASHBOARD
   ▼
COST GUARD (CG1) ──► budget_max verificato? dry_run rispettato?
   │  NO → blocco, richiesta respinta con motivo
   ▼  SI
Reparto destinazione esegue → emette evento {ecosistema, workflow, costo, durata, esito}
   ▼
CG2 Cost Accountant ──► scrive nel ledger unico (operations/cost/ledger)
   ▼
MON1/MON3 ──► se esito=fallito o costo anomalo → alert al committente + escalation
   ▼
Risposta handoff: {esito, costo_reale, durata, tier_usato, evento_ledger_id, alert_generati}
   └─► hooks post-task: log run → 06c-INTELLIGENCE per distillazione pattern
```

### (b) Esecuzione swarm end-to-end (RUNTIME × COST GUARD, il caso "produzione di massa")

```
Committente ── richiesta batch (es. 03-CONTENT-FACTORY: 50 varianti creative)
   ▼
RUN-LEAD ── sceglie strategia (fan-out vs sequenziale)
   ▼
RUN-QA ── G-DRYRUN: dry-run con stima costi PRIMA di tutto
   ▼
COST GUARD (CG1) ── approva budget_max o blocca
   ▼  (approvato)
RUN3 Fanout Sharder ── divide in shard ──┐
   ▼                                     │ PARALLELO (swarm fan-out, mesh)
RUN2 Worker Pool Manager ── assegna ─────┤
   ▼                                     │
RUN1 Swarm Marshal ── orchestrazione ────┘
   ▼
RUN5 Retry Handler ── rilancia SOLO gli shard falliti
   ▼
RUN4 Merge Operator ── consolida output
   ▼
CG2 Cost Accountant ── evento costo reale nel ledger
   ▼
Esito al committente + MON1/MON3 se anomalie
```

### (c) Budget guard — il blocco pre-sforo (COST GUARD, il gate più critico dell'ecosistema)

```
Qualsiasi workflow dichiara budget_max nel contratto §1.2
   ▼
CG1 Cost Sentinel ── monitora consumo in tempo reale durante l'esecuzione
   │
   ├─ consumo raggiunge 80% ──► CG1 alert (MON3 instrada al committente + OPS-Conductor)
   │
   ├─ consumo per raggiungere 100% ──► BLOCCO PRIMA dello sforo (pattern #9, non dopo)
   │                                    CG4 Budget Approval Gatekeeper: se il committente
   │                                    vuole proseguire, richiede ok ESPLICITO umano a Max
   │                                    (OUT-OF-SCOPE #1) — nessuna eccezione automatica
   │
   └─ run completata sotto budget ──► CG2 registra nel ledger; CG5 aggiorna il forecast
   ▼
CG6 Anomaly Detector ── confronta col trend storico ecosistema/workflow
   │  drift anomalo ──► allerta CG1 (non blocco automatico: richiede conferma umana CG1,
   │                     anti falso positivo)
   ▼
CG-QA ── verifica G-ATTRIBUTION: ogni run ha un evento costo, copertura ≥98%
```

### (d) Ciclo osservabilità → report Board (MONITORING, il cerchio settimanale)

```
1. RACCOLTA    MON1 Watchdog: run attive, daemon, token, processi zombie (continuo)
               CG2/CG5: eventi costo + forecast (continuo)
2. RILEVAZIONE MON1/MON4: run fallita o token in scadenza → MON3 Alert Dispatcher instrada
               (tempo di rilevazione ≤15 min — KPI v1)
3. COMPILAZIONE MON5 Weekly Report Compiler: costi per ecosistema + stato run + alert aperti
4. VERIFICA    MON-QA: dashboard leggibile in 30s, zero dati stale
5. CONSEGNA    Report + dashboard live alla Board (L0) — cadenza settimanale
6. DISTILLAZIONE Log run → 06c-INTELLIGENCE/LEARNING per pattern (fallimenti ricorrenti,
               drift di costo sistemici)
   └──────────────────────────────────────────► torna a 1 (loop continuo)
```

---

## 5. Asset esistenti wrappati (ADR-003: mappatura + wrapper, MAI riscrittura)

### 5.1 Flussi outreach attivi — rischio esplicito, NON toccare (Piano Maestro rischio #4)

| Path (verificato su disco) | Reparto L2 | Azione v2 |
|---|---|---|
| `Outreach/run_parallel.py`, `run_ig_email.py`, `run_all.bat`, `run_followup_b3.bat`, `run_linkedin_only.py`, `rerun_partial.py` | SCHEDULING | **WRAPPA** — SCH2 schedula e monitora SENZA modificare (workflow attivi: 6 team Nemotron €0/giorno, rischio #4 Piano Maestro) |
| `Outreach/AVVIA-EMAIL-LIVE.bat`, `TEST-EMAIL-10.bat`, `AVVIA-DASHBOARD.bat` | SCHEDULING | **WRAPPA** — trigger ufficiali, invocati da SCH1/SCH2, mai riscritti |
| skill `avvia-email`, `avvia-ig`, `avvia-linkedin`, `avvia-parallel`, `avvia-scraper` | SCHEDULING / WF-CRON | **USA** — trigger ufficiali delle run |
| `Outreach/SISTEMA_OUTREACH_COMPLETO.md` | MONITORING & DASHBOARD | **USA** come runbook di riferimento (base per G-RUNBOOK) |

### 5.2 Dashboard — evolve, non riscrive

| Path (verificato su disco) | Reparto L2 | Azione v2 |
|---|---|---|
| `Outreach/outreach-dashboard-premium/` (progetto Next.js: `package.json`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `next.config.ts`, `eslint.config.mjs` propri) | MONITORING & DASHBOARD | **EVOLVI** — MON2 con 06a-PLATFORM (PLATFORM scrive il codice, OPERATIONS lo usa e lo estende funzionalmente): da dashboard outreach a dashboard holding |
| `Outreach/start-dashboard.bat` | MONITORING & DASHBOARD | **USA** — trigger di avvio ufficiale |

### 5.3 Pattern portati da Content Factory Exponium (il pattern, non il file)

| Asset | Reparto L2 | Azione v2 |
|---|---|---|
| Pattern CF `swarm.sh --parallel N --budget N` | RUNTIME | **PORTA** — riscrittura versione DE (`empire-swarm`, §6); è l'unico "porta da fuori": si porta il pattern architetturale, non si copia il file |
| Pattern CF render queue + cost attribution | RUNTIME / COST GUARD | **PORTA** — idem, riscritto per lo schema costi DE |
| Ruflo: `task_orchestrate`, `swarm_init`, 3-tier routing, daemon | RUNTIME / COST GUARD | **USA** — con fallback bash auto-riparante (rischio #5 Piano Maestro: daemon Windows) |
| skill `loop`, `schedule` (cloud agents cron) | SCHEDULING | **USA** |
| skill `hooks-automation`, `workflow-automation`, `update-config` | SCHEDULING / MONITORING | **USA** |

---

## 6. Skill NUOVE da forgiare (via 06b-FORGE, standard §8 piano V2: PRD → architettura → build)

| Skill nuova | Reparto | Cosa fa | Priorità |
|---|---|---|---|
| `empire-swarm` | RUNTIME | `swarm.sh` versione DE: `--parallel N --budget N --dry-run`, fan-out + merge + retry — formalizza RUN1-RUN6 | **P0** |
| `cost-ledger` | COST GUARD | Ledger eventi costo + report settimanale per ecosistema — formalizza CG2 | **P0** |
| `budget-guard` | COST GUARD | Dichiarazione budget per workflow + blocco pre-sforo + richiesta ok umano per spese API — formalizza CG1/CG4 | **P0** |
| `empire-watchdog` | MONITORING & DASHBOARD | Health check schedulato: run, daemon Ruflo, token (es. FB scaduto), disco — formalizza MON1/MON4 | MEDIA |
| `asset-vault` | STORAGE & ASSETS | Convenzioni storage + dedup + retention per asset multi-ecosistema — formalizza ST1/ST3 | MEDIA |
| `run-dispatch-router` | RUNTIME | **NUOVO v2:** valida il contratto §1.2, verifica `budget_max` presente prima di spawnare qualsiasi run — formalizza il routing di OPS-Conductor | ALTA |
| `outreach-cron-wrapper` | SCHEDULING | **NUOVO v2:** wrapper di scheduling per gli script `Outreach/*.py`/`*.bat` — invoca senza mai modificare i file sorgente | ALTA |
| `cost-forecast` | COST GUARD | **NUOVO v2:** proiezione costo settimanale/mensile per ecosistema — formalizza CG5 | MEDIA |
| `board-report-compiler` | MONITORING & DASHBOARD | **NUOVO v2:** compila il report settimanale Board da ledger + watchdog — formalizza MON5 | MEDIA |

**Regola anti-contraddizione:** prima di creare ogni skill nuova → `skill-contradiction-analyzer`
contro le esistenti (`avvia-*`, `loop`, `schedule`, `hooks-automation`, `workflow-automation`).
Rischio concreto: `outreach-cron-wrapper` vs le skill `avvia-*` esistenti → il wrapper
INVOCA le skill `avvia-*`, non le sostituisce né le ridefinisce.

---

## 7. KPI + Quality Gates

### 7.1 Quality gates (bloccanti, in serie)

| Gate | Chi | Soglia | Esito fail |
|---|---|---|---|
| **G-DRYRUN** | RUN-QA | Ogni workflow nuovo gira prima in dry-run con stima costi | Run reale bloccata finché il dry-run non è stato eseguito |
| **G-BUDGET** | CG1 Cost Sentinel | Budget dichiarato e approvato PRIMA della run reale | Run rifiutata da OPS-Conductor senza `budget_max` |
| **G-ATTRIBUTION** | CG-QA | Run senza evento costo = run non valida | Run marcata invalida nel ledger, escalation a COST-LEAD |
| **G-RUNBOOK** | SCH-QA | Ogni workflow schedulato ha runbook e procedura di rollback | Schedulazione rifiutata finché `rollback_plan` non è presente |
| **G-RESTORE** | ST-QA | Restore backup testato e verde 1/mese | Escalation a STOR-LEAD se il test del mese manca |
| **G-DASHBOARD-FRESH** | MON-QA | Dashboard leggibile in 30s, zero dati stale | Blocco pubblicazione report, escalation a MON-LEAD |

### 7.2 KPI (riusa e amplia quelli del v1)

| KPI | Reparto | Target |
|---|---|---|
| Sforamenti budget | COST GUARD | 0 (blocco pre-sforo funziona) — v1 |
| Run schedulate completate senza intervento | SCHEDULING | ≥95% — v1 |
| Costo attribuito / costo totale (copertura ledger) | COST GUARD | ≥98% — v1 |
| Tempo rilevazione run fallita (watchdog) | MONITORING | ≤15 min — v1 |
| Quota task su tier economico (WASM/Haiku) | COST GUARD | ≥70% — v1 |
| Restore backup testato | STORAGE & ASSETS | 1/mese, verde — v1 |
| Giorni consecutivi outreach senza lancio manuale | SCHEDULING | **NUOVO v2** — target: 7gg consecutivi (DONE WHEN §0 punto 4) |
| Accuratezza forecast costi (previsto vs reale) | COST GUARD | **NUOVO v2** — nessuna baseline storica: si stabilisce al primo ciclo reale (niente numeri inventati) |
| Alert generati senza rumore (rapporto alert reali/falsi positivi) | MONITORING | **NUOVO v2** — nessun target imposto in assenza di dati storici; si misura da subito |
| Copertura dry-run pre-produzione | RUNTIME | **NUOVO v2** — target: 100% dei workflow nuovi passano G-DRYRUN prima della prima run reale |

---

## 8. Integrazione Ruflo (TopologyOrchestration)

**Topologia:** `hierarchical` (default holding) — OPS-Conductor coordinatore di ecosistema;
lead di reparto (RUN-LEAD, SCHED-LEAD, COST-LEAD, STOR-LEAD, MON-LEAD) coordinatori L2.
Fan-out `mesh` SOLO dentro batch paralleli di RUNTIME (shard di uno stesso swarm). Decisioni
cross-reparto (es. un batch RUNTIME che sfora il budget mentre STORAGE segnala spazio in
esaurimento) → escalation a OPS-Conductor, non risolte localmente.

| Funzione | Tool Ruflo | Uso in OPERATIONS |
|---|---|---|
| Fan-out swarm | `swarm_init` + `task_orchestrate` | RUN1/RUN3: produzione di massa, shard paralleli |
| Enforcement 3-tier | Thompson Sampling routing | CG3: instrada ogni task al tier giusto (WASM/Haiku/Sonnet-Opus) |
| Daemon runtime | Ruflo daemon + fallback bash auto-riparante | RUN1; mitigazione rischio #5 Piano Maestro (daemon Windows) |
| Pattern pre-scrittura | `memory_search` | CG6 confronta col trend storico prima di dichiarare anomalia |
| Salvataggio esiti | `memory_store` + hooks post-task | CG2 scrive ogni evento costo; MON1 scrive ogni esito health-check |
| Apprendimento | ReasoningBank (via 06c-INTELLIGENCE) | Log run → distillazione pattern (fallimenti ricorrenti, drift sistemici) |
| Sicurezza | `aidefence_scan` | Su parametri di run che includano dati esterni (es. liste outreach) |
| State per workflow | state.json per esecuzione | Ogni workflow CF-grade produce record ripartibile a freddo (test amnesia §6 piano V2) |

---

## 9. Namespace memoria — `operations/...` (AgentDB/HNSW)

| Namespace | Contenuto | Owner |
|---|---|---|
| `operations/runtime/shards/{run_id}` | Stato shard di un batch RUNTIME (per retry mirato) | RUN3/RUN5 scrivono |
| `operations/runtime/queue-state` | Stato coda WF-QUEUE (priorità, concorrenza) | RUN6 scrive |
| `operations/scheduling/cron-calendar` | Calendario unico di tutti i cron/loop della holding | SCHED-LEAD scrive |
| `operations/scheduling/rollback-plans/{workflow}` | Runbook e piano di rollback per ogni workflow schedulato | SCH-QA verifica presenza |
| `operations/cost/ledger` | Ledger eventi costo `{ecosistema, workflow, costo, durata, esito}` — cuore del reparto | CG2 scrive |
| `operations/cost/forecast/{ecosistema}` | Proiezioni costo settimanali/mensili | CG5 scrive |
| `operations/cost/anomalies` | Log delle anomalie di costo rilevate (confermate o falsi positivi) | CG6 scrive |
| `operations/storage/asset-registry` | Registro asset con naming/dedup/retention | ST1 scrive |
| `operations/storage/restore-log` | Storico test di restore mensili | ST2/ST-QA scrivono |
| `operations/monitoring/health-log` | Storico health check (run, daemon, token, zombie) | MON1 scrive |
| `operations/monitoring/alerts` | Registro alert generati e instradati | MON3 scrive |
| `operations/monitoring/board-reports` | Archivio report settimanali consegnati alla Board | MON5 scrive |
| `operations/handoffs/log` | Registro richieste/risposte cross-ecosistema | OPS-Conductor scrive |

**Wiki-first (pattern #12 Piano Maestro):** i pattern di fallimento ricorrente o di drift
sistemico rilevati da COST GUARD/MONITORING vengono segnalati a 06c-INTELLIGENCE/LEARNING
per la distillazione in pattern ReasoningBank e, se l'evidenza è forte, promossi a pagina
wiki. OPERATIONS non scrive direttamente sulla wiki: passa sempre da INTELLIGENCE (confine
di responsabilità esplicito, coerente con [[06c-ECOSISTEMA-INTELLIGENCE-V2]] §0).

---

## 10. Build plan v2

### Sequenza milestone (ordine non negoziabile: Cost Guard prima di moltiplicare gli agenti)

| Fase | Cosa si costruisce | Gate di uscita |
|---|---|---|
| **O1 — Cost ledger** | Team COST-* (8 agenti); `cost-ledger` (P0) forgiata; eventi costo dai flussi esistenti (outreach, build siti) | Primo report settimanale reale con dati veri |
| **O2 — Budget guard attivo** | `budget-guard` (P0) forgiata; G-BUDGET su tutti i workflow censiti; dry-run default | Un blocco pre-sforo testato dal vivo |
| **O3 — Runtime formalizzato** | Team RUN-* (8 agenti); `WF-SWARM-RUN` + `WF-DRY-RUN-VALIDATE`; `empire-swarm` (P0) forgiata | Prima produzione di massa reale entro budget |
| **O4 — Scheduling outreach** | Team SCHED-* (7 agenti); avvia-* sotto `WF-CRON` + `outreach-cron-wrapper`; `empire-watchdog` forgiata | 7 giorni di run outreach senza lancio manuale (DONE WHEN §0 punto 4) |
| **O5 — Storage a regime** | Team STOR-* (6 agenti); `asset-vault` forgiata; primo restore test tracciato | G-RESTORE verde |
| **O6 — Dashboard holding** | Team MON-* (7 agenti); evoluzione `outreach-dashboard-premium`; `board-report-compiler` forgiata; `WF-BOARD-REPORT` a regime | Dashboard live, leggibile in 30s; primo report Board automatico consegnato |

---

## 11. Pre-mortem — rischi v2

| Rischio | Probabilità | Mitigazione |
|---|---|---|
| **Modifica accidentale dei flussi outreach attivi** durante il wrapping di SCHEDULING | Alta se non presidiato | ADR-003 ferma: SCH2/`outreach-cron-wrapper` INVOCANO gli script esistenti, mai li editano; i file in `Outreach/*.py`/`*.bat` restano fonte di verità (rischio #4 Piano Maestro esplicito) |
| **Budget guard bypassato** da un workflow urgente ("solo questa volta") | Media | G-BUDGET non derogabile senza CG4 (ok umano esplicito, OUT-OF-SCOPE #1); nessuna eccezione automatica, nemmeno per OPS-Conductor |
| **Daemon Ruflo instabile su Windows** (rischio #5 Piano Maestro) | Alta | Fallback bash auto-riparante sempre attivo su RUN1; MON1/MON4 rilevano il daemon down entro 15 min |
| **Alert fatigue**: troppi alert, la Board smette di guardarli | Media | MON3 Alert Dispatcher instrada solo alert rilevanti; KPI "rapporto alert reali/falsi positivi" tracciato da subito, nessun target forzato finché non c'è baseline |
| **Cost forecast inaccurato nelle prime settimane** (nessuna baseline storica) | Alta nelle fasi iniziali | KPI esplicitamente "si stabilisce al primo ciclo reale, niente numeri inventati" (§7.2); CG5 dichiara sempre il livello di confidenza |
| **Reparti RUNTIME/COST GUARD in competizione** (RUNTIME vuole eseguire, COST GUARD vuole bloccare) | Media | Gerarchia esplicita: COST GUARD ha veto pre-esecuzione (G-BUDGET prima di G-DRYRUN nella sequenza); escalation a OPS-Conductor se il conflitto persiste |
| **Storage che cresce senza controllo di costo** (asset accumulati senza retention) | Media | ST4 Storage Cost Liaison collega esplicitamente spazio↔costo; ST3 applica retention automaticamente |
| **Dashboard che mostra dati stale** (la Board decide su numeri vecchi) | Media | MON-QA gate G-DASHBOARD-FRESH bloccante prima di ogni pubblicazione report |
| **Schede agenti v2 non millimetriche** (il rischio "è solo un file markdown" che Max denuncia) | Media | Standard §0 piano V2 obbligatorio per ogni agente nuovo; i 5 `-QA` di reparto verificano che ogni scheda abbia I/O, KPI, escalation |
| **Squilibrio tier**: agenti "nuovi v2" creati per default a Sonnet invece di Haiku, tradendo il principio "più Haiku-heavy" | Media | Roster §3 fissa il rapporto (~65% Haiku) come riferimento; CG3 Tier Router verifica anche l'allocazione interna di OPERATIONS, non solo quella degli altri ecosistemi |

---

## 12. Connessioni

- [[00-PIANO-MAESTRO]] — gerarchia LX→L5, backbone, pattern non negoziabili, i 10 ecosistemi
- [[11-PIANO-V2-DIRETTIVA-SCALA]] §0-2 — direttiva suprema che governa questo dossier (ADR-007)
- [[06-ECOSISTEMI-CORE]] — il v1 da cui si parte (sezione "09 · OPERATIONS", righe ~381-495); resta riferimento
- [[06a-ECOSISTEMA-PLATFORM-V2]] — scrive il codice di scheduling/dashboard che OPERATIONS usa; riceve eventi costo/durata/esito da ogni build/deploy
- [[06b-ECOSISTEMA-FORGE-V2]] — registra ogni nuovo agente/team nel cost model di OPERATIONS prima che sia operativo
- [[06c-ECOSISTEMA-INTELLIGENCE-V2]] — scritto in coppia con questo file; riceve log/metriche per distillazione pattern; schedula `WF-WIKI-GARDEN`/`WF-TREND` per conto suo
- [[04-ECOSISTEMA-MARKETING-V2]] — committente COST GUARD per budget ads guard e attribution campagne
- [[03-ECOSISTEMA-CONTENT-FACTORY]] — committente RUNTIME primario (mass-production swarm, render queue)
- [[01-ECOSISTEMA-AGENCY-V2]] — committente SCHEDULING primario (run outreach giornaliere, 6 team Nemotron attivi)
- `Outreach/` — asset reali wrappati (§5.1): run scripts, `outreach-dashboard-premium`, skill `avvia-*`
- [[07-BACKBONE-RUFLO-SKILLS]] — registro skill e integrazione Ruflo; tutte le skill §6 vanno registrate qui
- `company/Memory/STATO-EMPIRE.md` — regola memory-first: OPERATIONS logga qui come ogni altro ecosistema
- ADR-003 (wrap, non riscrittura) · ADR-007 (V2, CF-grade) · ADR-005 (minuzie → BACKLOG) · Mandato Empire OUT-OF-SCOPE #1 (zero spese senza ok Max)
