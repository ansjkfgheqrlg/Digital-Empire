# Censimento 01c — SINTESI DEGLI ORGANI DI GOVERNO

> Materia prima: `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/dati/censimento-01b-organi.md` (1.096 righe,
> 14 organi schedati, non modificato da me).
> Questo file contiene le **tre sintesi finali** che mancavano al censimento 01b, più le **tre
> verifiche supplementari** (Mandato · Sentinelle · Ispettorato) rifatte da me sul disco.
> Ogni numero qui viene o da una scheda del 01b, o da un comando che ho lanciato e che riporto.
> Data rilevazione: 2026-09-06.

---

## SINTESI A — LA TABELLA

**Legenda "chi lo chiama oggi":** «nessuno» significa nessun hook, nessuno script, nessun comando
dichiarato, nessun workflow. Un check di **esistenza** dentro `scripts/verify-empire.ps1` o
`scripts/gen-empire.py` **non è una chiamata**: verifica che l'organo ci sia, non lo convoca — e
`verify-empire.ps1` a sua volta non è agganciato ad alcun hook (verificato: `grep -nE
'"(SessionStart|Stop|PreToolUse|UserPromptSubmit)"' .claude/settings.json` → i 5 hook configurati
sono `empire-sync.ps1 pull`, `emperator_boot.py`, `gate_battito_hook.py`, `empire-sync.ps1 push`,
`graphify.exe hook-guard` ×2, `emperator_hook.py`. Nessuno nomina un organo).

| # | Organo | File | Agenti definiti | Invocabili in `.claude/agents/` | Chi lo chiama oggi | Difficoltà |
|---|---|---|---|---|---|---|
| 1 | `company/Board-CSuite/` | 163 (163 .md) | **70** (10 per figura) | **0 su 70** — esistono però le 7 figure con altro nome (`ceo-empire-conductor`, `cfo-empire`, `cmo-empire`, `coo-empire`, `cro-empire`, `cto-empire`, `chief-forge`) | **nessuno.** `gen-empire.py:28-35` ne verifica 8 file; `empire/loader.py:157` ne **legge** i 70 file per il cruscotto (letto ≠ chiamato) | MEDIA |
| 2 | `company/Guilds/` | 6 (6 .md, tutti README) | **5** Guild Master, solo nominati nei README | **5 su 5**, con nomi diversi: `guild-prompt`, `guild-copy-apsoc`, `guild-quality`, `guild-cost`, `guild-design` | **nessuno.** `gen-empire.py:43-48` verifica 6 path. Il "BUS" su cui i README dicono di mandare la `guild_request` non esiste come codice | BASSA |
| 3 | `company/Sentinels/` | 6 (6 .md, tutti README) | **5** | **5 su 5**: `sentinel-brandvoice/cost/drift/quality/security` (319-376 righe l'una) | **nessuno.** Nessun hook, nessun daemon, **0 git hook attivi** (`ls .git/hooks \| grep -v .sample \| wc -l` → 0) | MEDIA (Quality/BrandVoice/Cost) · BASSA (Security/Drift) |
| 4 | `company/Mandato/` | 2 (2 .md) | **0 — per statuto** («nessun agente, nessun codice: solo le leggi») | n/a | **verify-empire.ps1:81-89** (4 check di contenuto) + `empire/empire.toml:8` `root_marker` + `empire/tests/test_seed.py:23,66`. Tutto **solo a mano**: nessun hook lancia lo script | BASSA |
| 5 | `company/Ispettorato/` | 204 (115 .md, 88 .json, 1 .gitkeep) | **11** (`isp-*.md` in `agenti/`) | **0 su 11** (`ls .claude/agents/ \| grep -c "^isp-"` → 0) | **`python -m empire inspect capture\|analyze\|dispatch\|confirm\|report\|status\|backfill`** — comando reale, 30 test verdi, ma **a mano**: nessun hook post-run. `empire/loader.py:158` ne legge gli 11 file | BASSA |
| 6 | `company/MAXIMILIAN/` | 15 (15 .md) | **8** (`MX-PRIME`, `MX-VISION`, `MX-CRITIC`, `MX-CHALLENGE`, `MX-ANTICIPATE`, `MX-STYLE`, `MX-FAST`, `MX-MEMORY`) | **0 su 8** (`ls .claude/agents/ \| grep -ci "^MX-\|^maximilian"` → 0). Le sue 2 skill non sono installate in `.claude/skills/` | **nessuno.** Unico aggancio: `empire/empire.toml:33`, alias di percorso | MEDIA |
| 7 | `company/Gerarchia/` | 1 (1 .md, 79 righe) | 0 — è una mappa | n/a | `verify-empire.ps1:59` (esistenza, PASS) + `gen-empire.py:50` | BASSA |
| 8 | `company/Backbone/` | 10 (7 .md, 1 .yaml, 1 .json, 1 .gitkeep) | **2** | **2 su 2**: `bb-handoff-router`, `bb-memory-writer` | `verify-empire.ps1:117-121` (4 check di esistenza, PASS) + `gen-empire.py:36-42`. **`Bus/handoffs/` è vuota**: non ci è mai passato un messaggio | MEDIA |
| 9 | `company/Genesi-Core/` | 64 (64 .md) | **18** (8 `arch-*` + 10 `frg-*`) | **0 su 18** (`ls .claude/agents/ \| grep -c "^arch-\|^frg-"` → 0) | **nessuno.** Solo `empire/empire.toml:31`. **Unico organo che nemmeno il gate strutturale controlla**: assente da `gen-empire.py` e da `verify-empire.ps1` | ALTA (BASSA con la scorciatoia: 17 `mba-*` + 25 `cf-*` fanno già il mestiere) |
| 10 | `company/org/` | 1 (1 .yaml, 346 righe, 33 asset) | 0 — è un inventario | n/a | `verify-empire.ps1:139-145`: **check di contenuto** (`orfani <= 3`, oggi 2, PASS) | BASSA |
| 11 | `company/Antigravity-Briefs/` | 16 (16 .md, 2.314 righe) | 0 — sono brief | n/a | **nessuno**, ed è per natura umano (si incolla un brief a Gemini). Assente da `gen-empire.py` e `verify-empire.ps1` | BASSA |
| 12 | `company/01-agency/` | 114 (91 .png, 15 .md, 6 .json, 1 .txt, 1 .gitignore) | **7** (`AG-DIR` + `AG-A1..A6-COORD`, senza file-scheda) | **0 su 7** (`ls .claude/agents/ \| grep -c "^AG-"` → 0) | **`verify-empire.ps1:147-196`, ~30 check, tutti PASS** — l'organo più controllato. Comando di scrittura: `scripts/agency-trace.ps1`, che **nessuno chiama** | BASSA (rendimento più alto) |
| 13 | `company/02-info-business/` | 24 (18 .png, 2 .py, 1 .pdf, 1 .md, 1 .html, 1 .gitignore) | 0 | n/a | **nessuno.** `python build_brand_guidelines.py` a mano; non è in `skills-map.yaml`, non è in `verify-empire.ps1` | BASSA |
| 14a | `company/GRUPPO.md` | 1 (136 righe) | 0 — ma **cita 7 nomi-agente C-level** (`empire-conductor`, `empire-coo`, `empire-cto`, `empire-cmo`, `empire-cro`, `empire-cfo`, `empire-chief-forge`) | **0 su 7**: nessuno di quei sette nomi esiste in `.claude/agents/` | `verify-empire.ps1:42` + `gen-empire.py:26` (esistenza) | BASSA |
| 14b | `company/REGISTRO-IMPRESA.md` | 1 (699 righe, 98.577 byte) | 0 — è l'anagrafe | n/a | **nessuno.** Non è in `gen-empire.py` né in `verify-empire.ps1`. Solo `empire/registry/orphans.py:23` lo protegge dalla lista orfani | BASSA |
| 14c | `company/skills-map.yaml` | 1 (3.261 righe, 149.298 byte, 80 skill registrate) | 0 — è il registro | n/a | `verify-empire.ps1:127`: **solo esistenza**, nessun confronto con `.claude/skills/` (172 di progetto + 125 globali) | BASSA |

**Totali di colonna.** Agenti **definiti** dentro il perimetro di governo: **121**
(70 Board + 11 Ispettorato + 18 Genesi-Core + 8 MAXIMILIAN + 7 01-agency + 5 Guild + 5 Sentinel +
2 Backbone). **Invocabili in `.claude/agents/`: 19** — 5 Guild + 5 Sentinel + 2 Backbone + 7 figure
C-level (queste ultime con nomi che non compaiono in nessun documento di governo). **Copertura:
15,7%.** Fuori dal perimetro, `.claude/agents/` contiene in tutto **129 file**
(`ls .claude/agents/*.md | wc -l` → 129).

**Campi che il 01b lasciava scoperti e che ho misurato io.**
1. *Chi legge davvero le schede-agente del governo.* Ho eseguito
   `python -c "from empire.loader import _agent_files; ..."`, che risolve i pattern reali di
   `empire/loader.py:152-161`. Risultato: **443 file agente visti** — `company/Ecosistemi` 339,
   `company/Board-CSuite` **70**, `company/Ispettorato` **11**, fuori da `company/` 23.
   **Guilds, Sentinels, MAXIMILIAN, Genesi-Core e 01-agency non sono in nessuno dei 5 pattern**:
   i loro 43 agenti (5+5+8+18+7) sono invisibili anche alla macchina che conta gli agenti
   dell'azienda. Il cruscotto (`empire/dash/collect.py:26`, KPI `agenti_progettati`) li ignora.
2. *Il conteggio degli agenti invocabili per famiglia*, rifatto file per file:
   `^isp-` 0 · `^arch-` 0 · `^frg-` 0 · `^MX-` 0 · `^maximilian` 0 · `^AG-` 0 · `^guild-` **5** ·
   `^sentinel-` **5** · `^bb-` **2** · `^cf-` 25 · `^mba-` 17.

---

## SINTESI B — IL GOVERNO MUTO

> **È la lista più importante di questo documento.** Un governo che nessuno interroga non governa.
>
> **Metodo di verifica.** Per ogni organo ho lanciato, dalla radice del monorepo:
> `rg -n "<nome>" .claude/settings.json scripts/ empire/ .claude/skills/ -g '!__pycache__' -g '!*.pyc'`
> e ho classificato ogni riga trovata in tre categorie: **esistenza** (un path in una lista di
> `REQUIRED_FILES` o un `Check "... esiste"`), **alias** (una riga di `empire/empire.toml`, che
> risolve un percorso), **chiamata** (qualcosa che esegue l'organo). Sotto riporto il comando, il
> conteggio e la classificazione. **Righe di categoria "chiamata" trovate in tutto il perimetro:
> zero.**

### Gruppo I — muti assoluti: non esiste nemmeno il modo di chiamarli

**1. `company/MAXIMILIAN/` — il gate 5-bis. Il più muto di tutti.**
- Comando: `rg -n "MAXIMILIAN" .claude/settings.json scripts/ empire/ .claude/skills/`
- Risultato: **1 riga sola**, `empire/empire.toml:33` → `maximilian = "company/MAXIMILIAN"`. È un alias di percorso. Zero in `.claude/settings.json`, zero in `scripts/`, zero in `.claude/skills/`.
- **Cosa dovrebbe produrre:** un verdetto binario `{verdetto:"RIFAI", motivi:[…]}` oppure `{verdetto:"APPROVA"}` che rimanda un'intera fase al passo 3 (BUILD) o la fa procedere al passo 7 (COMMIT), più il brief di anticipazione verso SPEC/BACKLOG.
- **Cosa manca perché qualcuno lo chiami:** i suoi 8 agenti `MX-*` non sono in `.claude/agents/` (0 su 8) e le sue 2 skill non sono in `.claude/skills/`. Non c'è **nessun** modo di invocarlo, né a mano né automaticamente. Serve almeno `MX-PRIME` portato in `.claude/agents/` — è il conductor, orchestra gli altri sette — e `maximilian-standard-gate` installata come skill vera. In più il verdetto non avrebbe dove depositarsi: i 4 namespace `maximilian/*` non esistono su disco.

**2. `company/Sentinels/` — le 5 guardie che per definizione «bloccano senza essere chiamate».**
- Comando: `rg -n "company/Sentinels" .claude/settings.json scripts/ empire/ .claude/skills/`
- Risultato: **7 righe** — `scripts/gen-empire.py:49-54` (6 path in `REQUIRED_FILES`: esistenza) + `empire/empire.toml:30` (alias). Nessuna chiamata.
- Verifica incrociata del meccanismo che servirebbe: `ls .git/hooks/ | grep -v ".sample" | wc -l` → **0** (nessun git hook attivo); `rg "sentinel" .claude/settings.json` → **nessun risultato**.
- **Cosa dovrebbero produrre:** cinque giudizi JSON con potere di blocco (`brand_gate_pass`, `score_g2`, `item_falliti`, `azione`, `incident_id` nel formato `INC-<TIPO>-YYYYMMDD-NNN`) e un incident depositato.
- **Cosa manca perché qualcuno le chiami:** i 5 agenti `sentinel-*` **sono già invocabili** — manca il trigger, che per un Sentinel *è* la definizione del ruolo. Per Security e Drift il meccanismo è a portata di mano e già in uso: `.claude/settings.json` ha già due `PreToolUse` funzionanti (graphify hook-guard) e un `pre-commit` in `.git/hooks/` è un file di dieci righe. Manca anche il posto dove scrivere: `company/runtime/metrics/` non esiste (`ls -d company/runtime` → `No such file or directory`) e `patterns/incidents/` nemmeno.

**3. `company/Guilds/` — i 5 collegi trasversali.**
- Comando: `rg -n "company/Guilds" .claude/settings.json scripts/ empire/ .claude/skills/`
- Risultato: **7 righe** — `scripts/gen-empire.py:43-48` (esistenza) + `empire/empire.toml:29` (alias). Nessuna chiamata. Un'ottava riga, `empire/conform.py:247`, nomina `Guilds/` dentro il **testo di un suggerimento** («altrimenti spostarla (es. sotto Genesi-Core/, Guilds/ …)»): è una stringa di consiglio, non un'invocazione.
- **Cosa dovrebbero produrre:** le policy operative dell'Impero — `routing-policy.yaml`, `envelopes.yaml`, `sentinel-thresholds.yaml` (Cost-Guild), `DE-design-system.md` e `brand-kits/` (Design-Guild), `patterns/prompt/` (Prompt-Guild).
- **Cosa manca perché qualcuno le chiami:** i 5 agenti `guild-*` **sono già invocabili** (copertura 5/5, la migliore del governo) e i contratti di richiesta sono già scritti in ogni README. Manca (i) il **BUS** su cui i README dicono di mandare la `guild_request`, che non esiste come codice, e (ii) la cartella di destinazione: **tutti i loro deliverable puntano a `company/runtime/`, che non esiste**.

**4. `company/Genesi-Core/` — la fabbrica che dovrebbe creare gli altri organi.**
- Comando: `rg -n "Genesi-Core" .claude/settings.json scripts/ empire/ .claude/skills/`
- Risultato: **3 righe** — `empire/empire.toml:31` (alias), `empire/conform.py:247` (stringa di suggerimento), `empire/dash/render_md.py:26` (**un puntatore rotto**: stampa `Origine: Genesi-Core/07-CONTROL/DASHBOARD-E-RETRO.md` in testa a ogni dashboard, e quel percorso non esiste). Nessuna chiamata. **Ed è l'unico organo che nemmeno il gate strutturale controlla**: non compare in `gen-empire.py` né in `verify-empire.ps1`.
- **Cosa dovrebbe produrre:** blueprint (ARCHITETTURA) e artefatti forgiati (FORGE: skill, agenti, team, workflow, ecosistemi), con registrazione finale in `registro-agenti.yaml` via `frg-hr-registrar`.
- **Cosa manca perché qualcuno lo chiami:** 0 agenti su 18 invocabili, 0 skill installate. La scorciatoia esiste ed è economica: i 17 `mba-*` e i 25 `cf-*` già in `.claude/agents/` fanno gli stessi mestieri — va dichiarata la mappa `arch-*`/`frg-*` → `mba-*`/`cf-*` nel registro, invece di forgiare 18 file nuovi.

**5. `company/Board-CSuite/` — i 70 sotto-agenti (non le 7 figure).**
- Comando: `rg -n "Board-CSuite" .claude/settings.json scripts/ empire/ .claude/skills/`
- Risultato: **21 righe**, tutte classificabili: `verify-empire.ps1:44-51` (8 check di esistenza), `gen-empire.py:28-35` (8 path in `REQUIRED_FILES`), `empire/empire.toml:28` (alias), `empire/loader.py:8,11` + `empire/registry/SPEC.md:21,76` (**lettura**: il loader apre i 70 .md per contarli nel cruscotto). Nessuna chiamata.
- **Cosa dovrebbe produrre:** decisioni deliberate via consensus raft → ADR in `company/Memory/decisions/` + dispatch di direttive ai 10 ecosistemi via handoff contract.
- **Cosa manca perché qualcuno lo chiami:** le **7 figure sono già invocabili** (con nomi diversi da quelli scritti in `GRUPPO.md`); i 70 sotto-agenti no. Manca un comando di convocazione (`/board` o uno script) e manca il canale di dispatch: l'handoff contract è citato ovunque ma il Board non ha un solo file eseguibile che lo emetta. **In tutto il Board, 163 file su 163 sono markdown: non esiste un solo .py o .sh.**

**6. `company/REGISTRO-IMPRESA.md` — l'anagrafe («creare senza registrare = artefatto abusivo»).**
- Comando: `rg -n "REGISTRO-IMPRESA" .claude/settings.json scripts/ empire/ .claude/skills/`
- Risultato: **12 righe**, e qui il 01b va corretto (vedi Sintesi C §5): oltre all'alias `empire/empire.toml:14` e alla protezione `empire/registry/orphans.py:23`, esistono **un rigeneratore** (`empire/registry/render.py:42-46`, «rigenera la tabella di censimento automatico dentro REGISTRO-IMPRESA.md») e **un controllore vero** (`empire/registry/orphans.py:111-119`, regola `UNREGISTERED`: «artefatto maggiore assente da REGISTRO-IMPRESA.md e da skills-map.yaml»). Il codice per tenere onesta l'anagrafe **esiste ed è scritto.** Nessun hook lo esegue.
- **Cosa dovrebbe produrre:** l'elenco autoritativo di chi risponde di cosa (proprietario · controllore · origine · governo) per ogni artefatto dell'azienda.
- **Cosa manca perché qualcuno lo chiami:** l'aggancio di `python -m empire registry orphans` (o `gate`) a un hook. Vedi Sintesi C §5 per il numero che quel comando restituisce oggi.

**7. `company/02-info-business/` — zero assoluto.**
- Comandi: `rg -n "02-info-business" …` → **0 righe**. `rg -n "build_brand_guidelines" …` → **0 righe**.
- **Cosa dovrebbe produrre:** `CCM-Brand-Guidelines.pdf`, l'unico prodotto del perimetro consegnabile a una persona.
- **Cosa manca perché qualcuno lo chiami:** tutto. Il comando `python build_brand_guidelines.py` funziona ma **non è dichiarato da nessuna parte**: non è in `skills-map.yaml`, non ha un `/comando`, non è controllato da `verify-empire.ps1`. È l'unica cartella di `company/` con codice Python funzionante e nessun documento che sappia che esiste.

### Gruppo II — hanno la voce, ma nessuno la usa mai

Questi quattro **hanno un comando reale e documentato**. Il difetto non è l'assenza del comando: è
che l'unico dito che lo preme è quello di una persona, e da settimane non lo preme nessuno.

| Organo | Comando che esiste | Chi lo lancia | Prova che non gira |
|---|---|---|---|
| `company/Mandato/` | `powershell -File scripts/verify-empire.ps1` (113 check) | **nessun hook** — `rg "verify-empire" .claude/settings.json` → 0 righe | `verify-empire.ps1:230` contiene `Check "verify-empire.ps1 esiste"`: **il gate verifica la propria esistenza e nessuno lo lancia**. L'esito non viene scritto in nessun file: esce a console e muore con la finestra |
| `company/Ispettorato/` | `python -m empire inspect capture\|analyze\|dispatch\|confirm\|report\|status\|backfill` | **nessun hook** (il suo README lo mette fra i lavori futuri: «M5 — hook post-run») | 87 report e 87 telemetrie **tutti generati da un solo `backfill`**, ultimo giorno coperto **2026-07-24**: 44 giorni senza un report, contro una regola che ne pretende uno «dopo ogni run». `python -m empire inspect status` (eseguito ora) → `Loop aperti: 0 / TIP non confermati: 0 / Pattern in DRAFT: 0` |
| `company/01-agency/` | `powershell -File scripts/agency-trace.ps1` | **nessuno**: `rg "agency-trace" …` → 3 righe, di cui 2 nello script stesso e 1 in `verify-empire.ps1:199` che ne verifica l'esistenza | `company/Memory/state/agency/trace.jsonl`: **22 righe, tutte datate 2026-06-11**. Il Gate F4 cerca nel trace le 4 sigle HC e le trova — perché ce le ha messe il seed, non un ciclo di lavoro. **87 giorni senza un evento** |
| `company/org/` | il check `orfani <= 3` in `verify-empire.ps1:139-145` | vedi Mandato: nessun hook | `inventario-asset.yaml` è fermo a `updated: "2026-06-11"` (87 giorni). Il check resta verde perché **conta solo gli orfani già dichiarati**: un asset mai censito non è un orfano, è un invisibile |

### Gruppo III — muti per natura, e va bene così

- **`company/Gerarchia/`** (`rg "company/Gerarchia" …` → **1 riga**, `gen-empire.py:55`), **`company/GRUPPO.md`** (**4 righe**, tutte esistenza o rigenerazione da template) e **`company/skills-map.yaml`** (`verify-empire.ps1:127`, sola esistenza) sono documenti di consultazione: non devono essere "chiamati". Quello che manca loro non è un comando, è **un controllo che quello che dichiarano sia ancora vero** — e per `GRUPPO.md` quel controllo oggi fallirebbe 7 volte su 7 (vedi Sintesi C §1).
- **`company/Antigravity-Briefs/`** (`rg "Antigravity-Briefs" …` → **4 righe**: alias, un test, il README di `empire/`, e `empire/conform.py:64` che la classifica come cartella di planning) è muto per progetto: si attiva incollando un brief a un altro modello. Gli manca solo un indice di stato aperto/consegnato/verificato per gli 8 brief (oggi 3 consegne su 8, ricavabili solo contando i file in `consegne/`).

### Il conto

**Organi che nessuno chiama in alcun modo: 7** (MAXIMILIAN · Sentinels · Guilds · Genesi-Core ·
Board-CSuite · REGISTRO-IMPRESA.md · 02-info-business).
**Organi con un comando che nessuno esegue mai: 4** (Mandato/verify-empire · Ispettorato ·
01-agency/agency-trace · org).
**Organi muti per natura, correttamente: 4** (Gerarchia · GRUPPO.md · skills-map.yaml ·
Antigravity-Briefs).

**Il numero che riassume tutto: in `.claude/settings.json` ci sono 5 hook configurati, e nessuno dei
cinque nomina un organo di governo.** L'unica regola dell'Impero che sia mai passata dalla prosa a
un controllo eseguito automaticamente è quella del battito di Emperator
(`scripts/gate_battito_hook.py`, hook `Stop`, registrata ieri come contromisura di
`ERR-20260905-001`). È il precedente esatto che manca a tutti gli altri.
