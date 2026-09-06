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

---

## SINTESI C — SORPRESE E CONTRADDIZIONI

> Ogni voce cita **entrambe** le fonti col percorso. Dove ho rimisurato io, riporto il comando.

### C1. Due gate sullo stesso repo, nello stesso minuto, verdetti opposti — **la sorpresa più grande**

- **Fonte A** — `powershell -File scripts/verify-empire.ps1`, eseguito ora:
  `PASS: 113 / 113 | FAIL: 0 | WARN: 0 — [OK] Tutti i gate VERDE - EMPIRE OS integro`.
- **Fonte B** — `python -m empire registry orphans`, eseguito ora sullo stesso disco:
  `block: 9911   warn: 12555   info/fixable: 0   totale: 22466`.
  Ripartizione per regola (`grep -oE "^\[(BLOCK|WARN )\] [A-Z0-9-]+" | sort | uniq -c`):
  **6.966 `[BLOCK] LINK-DEAD`** (riferimenti a file inesistenti), **2.945 `[BLOCK] ADR-008`**,
  7.367 `[WARN] ORPHAN-UNREF`, 4.967 `[WARN] ADR-008`, **221 `[WARN] UNREGISTERED`**
  («artefatto maggiore assente da REGISTRO-IMPRESA.md e da skills-map.yaml»).

Il gate che l'Impero cita ovunque come prova di salute controlla **l'esistenza di 113 percorsi**; il
gate che nessuno cita mai controlla **l'integrità di tutto il monorepo** e trova quasi diecimila
findings bloccanti. Non si contraddicono sui fatti: misurano due cose diverse e una sola delle due
viene mai guardata. Finché «113/113 VERDE» è l'unica frase che circola, l'Impero si autocertifica
integro con lo strumento più debole che possiede.

### C2. Il gate pre-commit ADR-008 esiste, è scritto, ed è cablato al nulla — e se lo lanci ti dice che va tutto bene

- **Fonte A** — `empire/registry/cli.py:145`: `sub_reg.add_parser("gate", help="gate bloccante di pre-commit (ADR-008)")`, e `empire/registry/gate.py:2`: «gate pre-commit/CI per prevenire nuovi orfani o link rotti (ADR-008)».
- **Fonte B** — `empire/registry/gate.py:44-46`: senza `--files` e senza `--staged`, `files = []`. Eseguito ora: `python -m empire registry gate` → `block: 0   warn: 0   info/fixable: 0   totale: 0`.
- **Fonte C** — `ls .git/hooks/ | grep -v ".sample" | wc -l` → **0**. Non esiste il pre-commit che dovrebbe passargli i file in staging.

È lo scenario peggiore dei tre possibili: non «manca il gate», non «il gate fallisce», ma **il gate
risponde "tutto a posto" perché non sta guardando niente**. Chiunque lo lanci per verificare
ottiene una conferma falsa.

### C3. L'organigramma chiama i sette C-level con sette nomi che non esistono

- **Fonte A** — `company/GRUPPO.md:27-33`, tabella L0: `empire-conductor`, `empire-coo`, `empire-cto`, `empire-cmo`, `empire-cro`, `empire-cfo`, `empire-chief-forge`.
- **Fonte B** — `ls .claude/agents/`: `ceo-empire-conductor.md`, `coo-empire.md`, `cto-empire.md`, `cmo-empire.md`, `cro-empire.md`, `cfo-empire.md`, `chief-forge.md`.

**Zero corrispondenze su sette.** Chi legge l'organigramma e prova a chiamare `empire-coo` non trova
nulla. Ed è l'unico documento che un umano leggerebbe per sapere come si convoca il Board.

### C4. Il Mandato ha 8 Articoli, il suo stesso README ne annuncia 7

- **Fonte A** — `grep -n "^## Articolo" company/Mandato/MANDATO-EMPIRE.md` → **8 risultati** (righe 16, 48, 80, 112, 140, 162, 179, **199**).
- **Fonte B** — `company/Mandato/README.md:11`: «`MANDATO-EMPIRE.md` | i **7** Articoli: identità/posizionamento, brand voice, offerta/pricing, qualità, memory/wiki-first, multi-tenant, sicurezza».

L'Articolo 8 — quello che vieta i workflow "solo testo", il più citato nei gate recenti — è stato
aggiunto il 2026-07-22 e **il puntatore non è mai stato aggiornato**. Chi si fida del README non sa
che esiste la legge che oggi blocca più cose di tutte.

### C5. Le sentinelle prescritte a Sonnet e Opus girano tutte a Haiku, e si sa quale riga le ha inchiodate

- **Fonte A** — `company/Sentinels/Drift-Sentinel/README.md`: «Sonnet (contradiction analysis) / **Opus** (analisi architetturale complessa)»; `Quality-Sentinel/README.md`: «Sonnet (audit APSOC) / Haiku (checklist semplici)»; `Security-Sentinel/README.md`: «Haiku (scan pattern-matching) / **Sonnet** (analisi supply-chain)».
- **Fonte B** — verificato ora, `grep -m1 "^model:" .claude/agents/sentinel-*.md` → **`model: haiku` su tutti e cinque** (`brandvoice` 319 righe, `cost` 360, `drift` 322, `quality` 376, `security` 350).
- **Fonte C — la causa** — `.claude/fix_agents_frontmatter.py:117`: `if any(x in name for x in ["sentinel", "guild-cost", "bb-"])` assegna il modello per **pattern nel nome**, ignorando quello che il README di ciascuna prescrive. Un'utility di manutenzione ha sovrascritto una decisione di governo.

### C6. «Enforcement automatico: blocca senza essere chiamato» — e non c'è un solo trigger

- **Fonte A** — `company/Sentinels/README.md`: «I Sentinel operano su tutti i livelli — **non su richiesta, ma in modo continuo e proattivo**… Guild: expertise su richiesta. **Sentinel: enforcement automatico (blocca senza essere chiamato)**». `Security-Sentinel/README.md` fissa perfino il KPI: «Tempo di blocco dalla rilevazione: **sotto 5 secondi (pre-commit hook sincrono)**».
- **Fonte B** — `rg "sentinel" .claude/settings.json` → **0 righe**; `ls .git/hooks/ | grep -v ".sample" | wc -l` → **0**.

E il KPI del Quality-Sentinel lo dice senza accorgersene: `Quality-Sentinel/README.md:96` — «Gate
bypassati | **0 (per definizione — Mandato Art.4.1)**». È vero, ma non per la ragione che intende:
**un gate che non gira non si può bypassare.** Il numero perfetto è la prova che la macchina è ferma.

### C7. L'Ispettorato: tre fonti, tre stati diversi dello stesso milestone

- **Fonte A** — `company/Ispettorato/README.md:26`: «⬜ **M3** — Reparto CF-grade (11 agenti, 5 workflow) via FORGE» (casella vuota), e riga 3: `Status: Active (M1 — fondamenta)`.
- **Fonte B** — `company/REGISTRO-IMPRESA.md:21`: «Ispettorato Generale (`Ispettorato/` — **M1+M3 ✅** 11 agenti/5 WF, M2/M4/M5 residui)».
- **Fonte C — il disco** — `ls company/Ispettorato/agenti/ | wc -l` → **11**; `ls company/Ispettorato/workflow/ | wc -l` → **5**. Gli artefatti di M3 ci sono tutti.

Il disco e l'anagrafe concordano, il README dell'organo è indietro di sette settimane. Peggio: il
README non registra nemmeno che **la macchina esiste**. `company/Ispettorato/scripts/` contiene solo
un README che descrive quattro script (`trace_collector.py`, `report_generator.py`,
`recidiva_check.py`, `revision_metrics.py`) **che in quella cartella non esistono**; il codice vero
sta in `empire/inspect/` — 10 moduli e 30 test verdi
(`python -m pytest empire/tests/test_inspect.py -q` → **30 passed**).

### C8. Il REGISTRO-ERRORI dice «queste 10 voci» e ne contiene 11

- **Fonte A** — intestazione di `company/Ispettorato/registro/REGISTRO-ERRORI.md`: «Queste 10 voci sono la migrazione iniziale (M1)».
- **Fonte B** — conteggio riga per riga della tabella (`awk 'NR>=22 && NR<=32 && /^\| \*\*/' | wc -l`) → **11**; celle di stato → **11**; occorrenze di `APERTO` → **2**.

L'undicesima voce (`ERR-20260905-001`) è stata aggiunta **ieri** senza toccare quella riga. In un
registro il cui primo comandamento è «append-only, ogni voce chiusa non si riscrive», il conteggio
dichiarato è già disallineato dopo una sola aggiunta.

### C9. Quanti agenti ha Digital Empire? Quattro fonti, quattro numeri

- **Fonte A** — `company/Backbone/Identity-HR/README.md:12,126`: «`registro-agenti.yaml` — ✅ PRESENTE (**19 agenti**: 7 Board + 2 Backbone + 5 Guild + 5 Sentinel)».
- **Fonte B** — il file che quel README descrive, `registro-agenti.yaml:229,244`: `totale_agenti: **123**`, `status_ufficiali: 123 # tutti registrati in .claude/agents/ il 2026-09-01`.
- **Fonte C** — `ls .claude/agents/*.md | wc -l` → **129**. Sei agenti girano fuori dal roster che si dichiara completo.
- **Fonte D** — la macchina che conta gli agenti *progettati*, `empire/loader.py:152-161` (KPI `agenti_progettati` in `empire/dash/kpi.py:67`): eseguita ora → **443 file agente**, di cui `company/Ecosistemi` 339, `company/Board-CSuite` **70**, `company/Ispettorato` **11**, fuori da `company/` 23.

**E nessuna delle quattro vede gli stessi agenti.** Il loader legge Board e Ispettorato ma **non ha
un pattern per `company/Guilds/`, `company/Sentinels/`, `company/MAXIMILIAN/Agenti/`,
`company/Genesi-Core/*/Agenti/` né `company/01-agency/`**: i 43 agenti di quei cinque organi
(5+5+8+18+7) sono invisibili al cruscotto. Il registro ne dichiara 123 e ne descrive 19. Il disco ne
ha 129 invocabili e 443 progettati. **Non esiste, oggi, una risposta unica alla domanda "quanti
agenti abbiamo".**

### C10. «Creare senza registrare = artefatto abusivo»: la maggioranza delle skill è abusiva

- **Fonte A** — `company/skills-map.yaml`, riga di testa: «ADR-008: questa mappa + `company/REGISTRO-IMPRESA.md` = anagrafe unica. **Creare senza registrare = artefatto abusivo.** Aggiornare = ultimo passo di ogni ciclo FORGE.»
- **Fonte B** — misurato ora: `grep -c "^  - id:" company/skills-map.yaml` → **80 registrate**; `ls -d .claude/skills/*/ | wc -l` → **172** (progetto); `ls -d /c/Users/Utente/.claude/skills/*/ | wc -l` → **125** (globali).

Anche scontando ogni sovrapposizione, la stragrande maggioranza delle skill che l'Impero usa ogni
giorno non è nell'anagrafe. Per la sua stessa legge, sono artefatti abusivi. **Il controllo che li
smaschererebbe esiste** (`empire/registry/orphans.py:111-119`, regola `UNREGISTERED`, oggi 221
findings) e non lo lancia nessuno.

### C11. «Vivo» ha due definizioni incompatibili, e il registro usa quella debole

- **Fonte A** — `company/REGISTRO-IMPRESA.md`, sezione 2: `01-AGENCY (10/10 ✅) | **vivo**`, `02-INFO-BUSINESS (5/5 ✅) | vivo`, `03-CONTENT-FACTORY (9/9 ✅) | vivo`, `04-MARKETING (6/6 ✅) | vivo`.
- **Fonte B** — la definizione usata da questo piano (comando + contratto + posto stabilito + test) e verificata sul disco: gli agenti-direttore di quei quattro ecosistemi (`AG-*`, `IB-*`, `CF-R*`, `L2-*`) **non esistono in `.claude/agents/`** (`ls .claude/agents/ | grep -c "^AG-"` → 0).

Nel registro «vivo» significa **documentato al completo**. Nel piano significa **che qualcuno lo può
chiamare e qualcosa esce**. Sono due parole diverse scritte uguale, ed è il malinteso che tiene in
piedi la sensazione che l'azienda sia più operativa di quanto sia.

### C12. Il Board dichiara di essere un'organizzazione di 70; nella pratica è sette agenti singoli

- **Fonte A** — `company/Board-CSuite/CEO-Empire-Conductor/README.md`: «una figura C-level non è un agente singolo: è un'organizzazione di governo con un team di 10 agenti specializzati».
- **Fonte B** — `.claude/agents/`: le 7 figure ci sono, i loro 70 sotto-agenti **zero**. Ogni figura è, letteralmente, un agente singolo.
- **Aggravante** — l'unico nome che combacia è una **collisione**: `.claude/agents/cf-conductor.md:3` è «Conductor di Content Forge 2.0. Orchestratore principale della pipeline di trasformazione contenuti», mentre `company/Board-CSuite/Chief-Forge/agenti/cf-conductor.md` è «Conductor della Crescita Organizzativa… riporta al CEO». Stesso nome, due entità diverse: chi invoca `cf-conductor` aspettandosi il Board ottiene la pipeline contenuti.

### C13. Tre destinazioni ufficiali che non esistono su disco

- **`company/runtime/`** — dichiarata come posto dei deliverable da tutte e 5 le Guild (`Cost-Guild/README.md` → `company/runtime/cost/routing-policy.yaml`, `envelopes.yaml`, `sentinel-thresholds.yaml`; `Design-Guild` → `company/runtime/design/`; `Prompt-Guild` → `company/runtime/brain/patterns/prompt/`) e da tutte e 5 le Sentinelle (`company/runtime/metrics/runs.jsonl`). Verificato: `ls -d company/runtime` → `No such file or directory`.
- **`patterns/incidents/{cost,quality,drift,security,brand}/`** — seconda destinazione delle Sentinelle e prescritta anche dal Mandato Art.7.1 («un segreto committato = incidente… deposito in `patterns/incidents/`»): non esiste.
- **`Genesi-Core/07-CONTROL/DASHBOARD-E-RETRO.md`** — stampato come `Origine:` in testa a **ogni dashboard generata** da `empire/dash/render_md.py:26`. `company/Genesi-Core/` contiene solo `ARCHITETTURA/` e `FORGE/`. Ogni cruscotto dell'Impero cita come propria origine un file che non c'è.

### C14. I verbali in Memory sono fermi a una versione precedente del gate che citano

- **Fonte A** — `company/Memory/STATO-EMPIRE.md:5988,6045`: «`verify-empire.ps1` **PASS 59/59**», «F2 COMPLETATO — gate PASS 59/59».
- **Fonte B** — esecuzione di oggi: **`PASS: 113 / 113`**.

Il numero di check è quasi raddoppiato e i verbali non se ne sono accorti. Lo stesso file, alle
righe 5975 e 6940, riporta correttamente 113/113: **dentro lo stesso documento convivono due verità
sullo stesso gate**, a seconda di quale checkpoint si legge.

### C15. La diagnosi del 2026-07-22 descrive un'azienda peggiore di quella che è

- **Fonte A** — `company/Antigravity-Briefs/GEM-00-INDEX-E-PROTOCOLLO.md`, tabella «Diagnosi misurata il 2026-07-22»: `Ispettorato/telemetry/` **vuota**, `Ispettorato/report/` **vuota**, `.py` in `company/` = **0**; conclusione in grassetto: «Digital Empire oggi è un'azienda *descritta*, non un'azienda *che gira*».
- **Fonte B** — oggi: `telemetry/` **88 file**, `report/` **88 file**, `empire/inspect/` con 30 test verdi (consegna GEM-03), e `company/02-info-business/ccm/brand/` contiene 2 file `.py` funzionanti.

È l'unica contraddizione di questo elenco in cui la realtà è **migliore** del documento. Ma il
documento non è stato aggiornato, quindi il progresso non è visibile a nessuno che lo legga: tre
caselle chiuse su nove continuano a risultare aperte. **Un'azienda che non registra i propri
miglioramenti li spende due volte.**

---

# LE TRE VERIFICHE SUPPLEMENTARI

---

## VERIFICA 1 — IL MANDATO: gli Articoli, numero e titolo per esteso

**Fonte:** `company/Mandato/MANDATO-EMPIRE.md` — 242 righe, 14.420 byte, versione 2.0 F1-bis.
**Comando:** `grep -n "^## Articolo" company/Mandato/MANDATO-EMPIRE.md` → **8 risultati**.
**Comando:** `grep -nE "^\*\*[0-9]+\.[0-9]+" …` → **28 commi**.
Ogni gate del piano dovrà poterli citare: qui sono tutti, con il numero di riga esatto.

| Art. | Titolo per esteso | Riga | Commi |
|---|---|---|---|
| **Articolo 1** | **Identità e Posizionamento** | 16 | **1.1** Chi siamo · **1.2** Il posizionamento fondativo (non negoziabile) · **1.3** I 4 pilastri business · **1.4** Regola di pertinenza |
| **Articolo 2** | **Brand Voice ("prove, non promesse")** | 48 | **2.1** La voce · **2.2** Invariante assoluta: MAI un claim senza evidenza · **2.3** Anti-pattern bloccati (lista di enforcement del Brand-Voice Sentinel) · **2.4** Framework di scrittura |
| **Articolo 3** | **Offerta e Pricing Policy** | 80 | **3.1** Listino corrente (pubblico e fisso) · **3.2** Invarianti pricing (mai contraddirle, in nessun copy e in nessun preventivo) · **3.3** Chi decide i prezzi (ADR-005, punto 4) · **3.4** Prodotti info e multi-business |
| **Articolo 4** | **Qualità (gate non bypassabili)** | 112 | **4.1** Principio · **4.2** Gate copy (APSOC) · **4.3** Gate codice e sistemi · **4.4** Gate contenuti |
| **Articolo 5** | **Memory-first e Wiki-first (ADR-002, pattern #12 e #13)** | 140 | **5.1** Memory-first (pattern #13, non negoziabile) · **5.2** Wiki-first (pattern #12) · **5.3** Decisioni |
| **Articolo 6** | **Multi-tenant by design (pattern #11)** | 162 | **6.1** Principio · **6.2** Conseguenze operative |
| **Articolo 7** | **Sicurezza (zero segreti, PII protetta)** | 179 | **7.1** Zero segreti nel repo (assoluto) · **7.2** PII protetta · **7.3** Supply-chain e perimetro · **7.4** Enforcement |
| **Articolo 8** | **Regola Assoluta del Workflow Reale e Autocontenuto (Struttura Tangibile 360°)** | 199 | **8.1** Divieto assoluto di Workflow "Solo Testo" o Dispersi · **8.2** I 6 Pilastri Obbligatori di ogni Cartella Workflow · **8.3** Enforcement (Gate-5-bis e Sentinels) |
| *(non è un Articolo)* | **Checklist Brand Gate (uso operativo — da copiare nei gate QA)** | 221 | 10 voci a spunta |

**Le clausole che un gate deve poter citare alla lettera:**
- **Art. 1.2** — «L'agenzia progettata per essere licenziata.» *«Qualsiasi copy, contratto o architettura che crea lock-in del cliente viola questo Articolo.»*
- **Art. 1.4** — «Se un task non è riconducibile a un ecosistema, non si esegue: si porta al Board.»
- **Art. 2.2** — struttura **CPB (Claim → Proof → Benefit)**: «Un claim senza proof è un difetto bloccante… vale anche per il Board.»
- **Art. 2.4** — **APSOC**, «P sempre prima di S (violazione = **meno 15** al gate)».
- **Art. 3.1** — listino fisso: Outreach Factory **€4.000** · Content Factory **€3.500** · Second Brain **€2.500** · Engine Room **€8.000**; setup 7 giorni lavorativi, 90 giorni di supporto inclusi.
- **Art. 3.2** — 3 invarianti: one-time **zero canoni** · codice **di proprietà del cliente** · sconti **solo via bundle**.
- **Art. 4.1** — «I gate non sono bypassabili: **nessun flag `--skip`, nessuna eccezione inline**.» Unica via alternativa: deroga del Board via raft depositata in `Memory/decisions/`.
- **Art. 4.2** — APSOC **≥ 80/100** standard, **≥ 85/100** sales page e proposte, P prima di S, **Brand gate G2 binario**.
- **Art. 4.3** — dry-run obbligatorio · `verify-empire` verde (5 categorie) prima di ogni chiusura di fase · zero bug bloccanti · **i sistemi attivi non si riscrivono: si wrappano (ADR-003)**.
- **Art. 5.1** — «Nessun task è "fatto" finché non è salvato in Memory.»
- **Art. 5.2** — «in caso di conflitto wiki ↔ AgentDB: **vince la wiki**»; lag KPI **< 24h**.
- **Art. 6.1** — «un handoff senza `brand_kit` dichiarato è **invalido**».
- **Art. 7.1** — zero segreti in Git: un segreto committato = incidente, blocco push + rotazione + deposito in `patterns/incidents/`.
- **Art. 8** — citazione diretta del founder, **2026-07-22**: *«Quando ti chiedo di creare un workflow… voglio che ci sia una cartella reale, tangibile e autocontenuta… Questo vale per sempre.»* I **6 pilastri**: `01-FLUSSI-E-PIANI/` · `02-AUTOMAZIONI-E-SCRIPTS/` · `03-AGENTI-E-RUOLI/` · `04-SKILLS-E-REFERENCE/` · `05-TEMPLATES-E-KIT/` · `06-DASHBOARD-E-METRICHE/`. Chi ne manca anche uno è **«Workflow Abusivo / Incompleto»**.

**Gerarchia stabilita dal documento:** `Mandato (LX) > Board (L0) > Ecosistema (L1) > Reparto (L2) >
Workflow (L3) > Funzione (L4) > Agente (L5)`.

**Esito della verifica: gli Articoli sono 8.** Il README della cartella ne annuncia 7 (vedi Sintesi C
§4) — **da correggere, costa una riga.**

---

## VERIFICA 2 — LE 5 SENTINELLE: cosa sorvegliano, con quale soglia, e se si attivano da sole

**Fonti confrontate:** `company/Sentinels/*/README.md` (6 file .md, nessuno script) **contro**
`.claude/agents/sentinel-*.md` (5 file, 319-376 righe l'uno).

| # | Sentinella | ID · Supervisore | Cosa sorveglia | Soglie numeriche | Si attiva da sola **oggi**? |
|---|---|---|---|---|---|
| 1 | **Cost** | `SENT-COST-001` · CFO | crediti API per agente/team/ecosistema/brand_kit · tier modello vs routing policy 3-tier · agenti in loop · Opus su task Tier 0-1 · dry-run eseguito o no | **7 soglie:** 60% envelope → log + notifica CFO · **80%** → warning CFO+COO+CEO `priority: HIGH` · **95%** → blocco task non urgenti · **100% + accelerazione** → stop immediato + escalation CEO · Opus su Tier ≤1 → downgrade · **>20 chiamate/min per >2 min** → sospensione agente · dry-run saltato → blocco | **NO.** Il file stesso: «Latenza alert dalla soglia: < 30 secondi **(quando daemon attivo)**» — il daemon non esiste |
| 2 | **Quality** | `SENT-QUAL-001` · CMO | score APSOC di ogni output di conversione · completezza dei blocchi APSOC · pass-rate per team sugli ultimi 10 run · reject consecutivi · trend qualità | **6 soglie:** APSOC **< 80/100** su copy standard → blocco · **< 85/100** su sales page/preventivo → blocco + escalation · **P dopo S → −15 punti e blocco obbligatorio a prescindere dal totale** · pass-rate < 90% su 10 run → segnalazione · 2 reject consecutivi stesso team → escalation · trend in calo per 3 cicli → convocazione Quality-Guild + CTO | **NO.** «eseguito manualmente come checklist» |
| 3 | **Drift** | `SENT-DRIFT-001` · CTO | coerenza output ↔ ADR attivi in `Memory/decisions/` · lag `second-brain-vault/wiki/` ↔ AgentDB · agenti fuori scope in `registro-agenti.yaml` · documenti normativi modificati senza entry in `wiki/log.md` · decisioni architetturali senza ADR | **5 soglie:** contraddizione bloccante → blocco merge/deploy · **lag > 24h** → forzatura sync · handoff fuori scope → blocco handoff · documento normativo modificato senza log → **blocco commit** · decisione senza ADR → ADR retroattivo. Escalation al Board se non risolto in **24h** | **NO — ed è la più grave**, perché è quella che dovrebbe bloccare i commit: `.git/hooks/` contiene **solo i 14 `.sample`**, zero hook attivi |
| 4 | **Security** | `SENT-SEC-001` · CTO | segreti in file tracciati (`sk-`, `ANTHROPIC_API_KEY=`, `password=`, `token:`, `instagram_session.json`, `linkedin_session.json`) · PII in output esterni · prompt/SQL injection e XSS · supply-chain (npm/python/vendor nuovi) · permessi anomali · repo cliente mescolati col monorepo | **5 soglie:** secret in commit → blocco push + quarantena + rotazione · PII in output esterno → blocco invio · skill/vendor senza scan → blocco adozione · permessi fuori scope → quarantena agente · compromissione sospetta → stop + consenso byzantine CTO→CEO. KPI: **blocco < 5 secondi (pre-commit hook sincrono)** | **NO.** Il file dichiara la dipendenza mancante: «`git-secrets` pattern — pre-commit hook (**da configurare in `.claude/settings.json` F2**)». Verificato: i due `PreToolUse` presenti sono entrambi `graphify.exe hook-guard` |
| 5 | **BrandVoice** | `SENT-BV-001` · CMO — **unica LX-Sentinel**: «può bloccare anche output approvati dal Board» | ogni output con parole verso l'esterno: email, DM, landing, sales page, preventivi, post, caroselli, script, comunicazioni cliente. Aspetti: tono (Art.2.1) · claim con proof in CPB (Art.2.2) · P prima di S (Art.2.4) · nessun canone mensile (Art.3.2) · nessun dependency-language (Art.1.2) | tabella di **8 anti-pattern bloccanti** (AI-slop · icebreaker vuoto · hype senza dato · tono agenzia tradizionale · dependency-language · canone implicito · APSOC incompleto · qualificatore molle), ognuno mappato sull'Articolo violato. **Gate G2 = checklist binaria a 8 item: un solo fail = output bloccato.** Escalation CMO a **≥3 blocchi dello stesso anti-pattern in 7 giorni** | **NO.** Stesso blocco `Stato` delle altre quattro; fallback dichiarato: la «Checklist Brand Gate» del Mandato |

**Risposta secca: 0 sentinelle su 5 si attivano da sole.** Tutte e cinque si attivano solo se
qualcuno scrive il loro nome in chat.

**Il confronto `company/Sentinels/` ↔ `.claude/agents/sentinel-*.md` — cosa c'è e cosa manca.**
- **Copertura: 5 su 5.** Tutte e cinque hanno un agente invocabile, e non sono stub: 319 · 360 · 322 · 376 · 350 righe.
- **Le soglie sono passate nei file invocabili.** Verificato contando le occorrenze numeriche in ciascuno (`grep -cE "60%|80%|95%|100%|80/100|85/100|24h|5 secondi|8 item|20 chiamate"`): `sentinel-cost` **25**, `sentinel-quality` **12**, `sentinel-drift` **7**, `sentinel-security` **2**, `sentinel-brandvoice` **3**. Esempi: `sentinel-cost.md:53` «soglie percentuali (60% / 80% / 95% / 100%)», `sentinel-drift.md:120` «Lag wiki/AgentDB > 24h», `sentinel-brandvoice.md:220` «Score G2: N/8 (8/8 = passa)», `sentinel-security.md:202` «< 5 secondi (pre-commit hook sincrono)». **La conoscenza è a bordo: manca solo il dito che preme.**
- **Il modello è sbagliato in tutti e cinque.** `model: haiku` ovunque, contro le prescrizioni dei README (Drift: Opus per l'analisi architetturale; Security: Sonnet per la supply-chain; Quality: Sonnet per l'audit APSOC). Causa in `.claude/fix_agents_frontmatter.py:117`. Vedi Sintesi C §5.
- **Le descrizioni promettono un trigger che non esiste.** Tutte dicono «Attiva su ogni output / ogni commit / ogni modifica»: in un file agente quella riga è **testo per il router semantico**, non un evento. `rg "sentinel" .claude/settings.json` → 0 righe.
- **Non hanno dove scrivere.** Le due destinazioni dichiarate — `company/runtime/metrics/runs.jsonl` e `patterns/incidents/{cost,quality,drift,security,brand}/` — **non esistono su disco**. Gli `incident_id` hanno un formato preciso (`INC-<TIPO>-YYYYMMDD-NNN`) e nessun posto dove essere depositati.

**La mossa più corta per accenderne una.** Security e Drift sono le più economiche perché il
meccanismo esiste già ed è già in uso nel repo: `.claude/settings.json` ha due `PreToolUse`
funzionanti (graphify hook-guard) e un `pre-commit` in `.git/hooks/` è un file di dieci righe. In
più il gate che servirebbe loro è **già scritto**: `python -m empire registry gate --staged`
(`empire/registry/gate.py`) è dichiarato «gate bloccante di pre-commit (ADR-008)» e oggi non è
collegato a niente (Sintesi C §2). Prima di qualunque accensione: creare
`company/runtime/metrics/` e `patterns/incidents/`, altrimenti anche una sentinella che scatta non
ha dove depositare l'incidente.

---

## VERIFICA 3 — L'ISPETTORATO: M1..M5, cosa è operativo, e il REGISTRO-ERRORI

### 3a. Che cos'è

Da `company/Ispettorato/README.md`: «L'organo trasversale che misura le performance dell'Impero.
**NON produce, NON corregge da solo: rileva, registra, assegna, verifica.** Indipendente da chi
costruisce». Da `ARCHITETTURA.md`: «organo trasversale con **diritto di audit su tutti gli altri**».
Nasce da una direttiva di Max del 2026-07-04, estesa il 2026-07-20: «report dopo ogni run, analisi
al millimetro, **mai lo stesso errore due volte**».
**204 file** (115 .md, 88 .json, 1 .gitkeep) — il secondo organo per dimensione dopo il Board, e
l'unico dove i file non sono quasi tutti descrizioni.

### 3b. M1..M5 — cosa sono e cosa è davvero operativo

| Milestone | Cosa è | Dichiarato in `README.md:23-28` | **Realtà sul disco (verificata ora)** |
|---|---|---|---|
| **M1 — Fondamenta dati** | struttura + REGISTRO-ERRORI migrato + REGISTRO-REVISIONI seed + REGISTRO-SUCCESSI seed + KPI empire-wide | ✅ fatto | ✅ **confermato.** `registro/` contiene 4 file: `REGISTRO-ERRORI.md`, `REGISTRO-REVISIONI.md`, `REGISTRO-SUCCESSI.md`, `REGISTRO-DECISIONI-ALTIRANGHI.md`; `kpi/KPI-EMPIRE-WIDE.md` presente |
| **M2 — Pilota PreventivoForge** | trace JSONL reale su un flusso vero | ⬜ da fare | ⬜ **confermato: non fatto.** Nessun trace di PreventivoForge |
| **M3 — Reparto CF-grade** | 11 agenti + 5 workflow via FORGE | ⬜ da fare | ✅ **FATTO, il README è indietro.** `ls agenti/ \| wc -l` → **11** (`isp-conductor`, `isp-telemetry-collector`, `isp-run-auditor`, `isp-error-registrar`, `isp-recidiva-sentinel`, `isp-kpi-analyst`, `isp-report-forger`, `isp-liaison-altiranghi`, `isp-improvement-dispatcher`, `isp-verifier`, `isp-revision-analyst`); `ls workflow/ \| wc -l` → **5** (`WF-RUN-AUDIT`, `WF-DAILY-AUTOCRITICA`, `WF-RECIDIVA-GATE`, `WF-REPORT-ALTIRANGHI`, `WF-REVISION-STUDY`). Lo conferma `company/REGISTRO-IMPRESA.md:21`: «M1+M3 ✅ 11 agenti/5 WF» |
| **M4 — Aggancio Impero** | RECALL/RETRO + handoff verso MAXIMILIAN / Board / Sentinelle | ⬜ da fare | ⬜ **confermato: non fatto** — e non può esserlo, perché MAXIMILIAN non è invocabile e il BUS non esiste |
| **M5 — Estensione** | telemetria outreach + report settimanale + **hook post-run** | ⬜ da fare | ⬜ **confermato: non fatto.** È il pezzo che manca perché l'organo si accenda da solo |

**Operativi oggi: M1 e M3.** In sospeso: M2, M4, M5.

**Ma il pezzo che conta non è in nessuna delle cinque caselle: la macchina esiste già.**
`company/Ispettorato/scripts/` contiene **solo un README** che descrive quattro script
(`trace_collector.py`, `report_generator.py`, `recidiva_check.py`, `revision_metrics.py`) **che in
quella cartella non esistono**. Il codice vero sta in **`empire/inspect/`**: 10 moduli Python
(`cli.py` 10.997 byte, `report.py` 10.292, `metrics.py` 7.366, `record.py`, `dispatch.py`,
`analyst.py`, `synth.py`, `collector.py`, `confirm.py`, `benchmarks.py`) più `SPEC.md` con le
formule della **Scorecard 5D** (asse ①: `Score = 5 − min(4, errori + retry×0.5 + escalation×2)`).
È la consegna del brief `company/Antigravity-Briefs/GEM-03-ISPETTORATO-TELEMETRIA.md`.

**Prove eseguite ora:**
- `python -m empire inspect status` → `STATO ISPETTORATO GENERALE / Loop aperti: 0 / TIP non confermati: 0 / Pattern in DRAFT: 0`
- `python -m pytest empire/tests/test_inspect.py -q` → **30 passed in 0.28s**
- 7 comandi disponibili (`empire/inspect/cli.py:257-311`): `capture` · `analyze` · `dispatch` · `confirm` · `report` · `status` · `backfill`

**E i dati sono fermi.** Gli 87 report in `report/run/` e le 87 telemetrie in `telemetry/runs/`
coprono 22 giornate dal **2026-06-10 al 2026-07-24** e vengono da **un'unica esecuzione di
`backfill`** — lo dichiara `company/Antigravity-Briefs/consegne/GEM-03-CONSEGNA.md:53`: «sono stati
caricati ed analizzati tutti i **79 checkpoint storici**». **Il `capture` per una run nuova non
l'ha mai chiamato nessuno: 44 giorni senza un report**, contro una regola che ne pretende uno «dopo
ogni run».

**Manca una cosa sola: qualcuno che chiami `capture` quando una run finisce.** Comando ✅ ·
contratto ✅ (`empire/inspect/SPEC.md`) · posto stabilito ✅ (popolato) · test ✅ (30 verdi).
È l'organo più vicino alla vita di tutto il perimetro, e il modello per gli altri. Da sistemare in
contorno: le caselle M3 nel README, `scripts/README.md` che descrive quattro script inesistenti,
e `report/escalation/` — dichiarata nel README e cablata in `empire/inspect/report.py:84`, **ma
assente dal disco**.

### 3c. Il REGISTRO-ERRORI — dov'è, quante voci, quante aperte

**Percorso:** `company/Ispettorato/registro/REGISTRO-ERRORI.md`
**Dimensione:** 8.670 byte · **ultima modifica: 2026-09-05** (ieri) — è il file più vivo dell'organo.
**Regola in testa:** «Append-only. Ogni voce chiusa non si riscrive. Un errore già qui che si
ripresenta = **RECIDIVA = gate ROSSO bloccante**.»

**Voci: 11.** Contate riga per riga della tabella
(`awk 'NR>=22 && NR<=32 && /^\| \*\*/' … | wc -l` → **11**; celle di stato → **11**).
*Nota: gli ID univoci nel formato `ERR-YYYYMMDD-NNN` sono 10, perché una voce ha ID irregolare —*
`ERR-20260618/22-001`. *E l'intestazione del file dice ancora «queste 10 voci»: vedi Sintesi C §8.*

**APERTE: 2** (`grep -cE "APERTO"` → 2). **Chiuse: 9.**

| ID | Data | Sintomo | Stato |
|---|---|---|---|
| `ERR-20260616-001` | 2026-06-16 | collisione git su naming misto MAIUSCOLO/Title-Case (Windows `core.ignorecase`) | CHIUSO — 0 recidive |
| `ERR-20260616-002` | 2026-06-16 | swarm di alto valore girato su Sonnet low-effort senza che nessuno se ne accorgesse | CHIUSO |
| `ERR-20260618/22-001` | 2026-06-18, ripetuto 2026-06-22 | swarm muore a metà: «You've hit your weekly/session limit» (due sessioni sullo stesso account) | CHIUSO |
| `ERR-20260622-001` | 2026-06-22 | 4 agenti muoiono dopo 14-21 tool_use: 1 file prodotto su 62 attesi (prompt read-heavy) → regola **WRITE-EARLY** | CHIUSO |
| `ERR-20260622-002` | 2026-06-22 | 87 occorrenze di namespace AgentDB divergente fra reparti | CHIUSO |
| `ERR-20260622-003` | 2026-06-22 | 6 README v1 elencavano un roster inesistente: l'idempotenza aveva protetto i file stantii | CHIUSO |
| **`ERR-20260703-001`** | **ricorrente, ultima 2026-07-19/20** | **`git push origin main` fallisce: `send-pack: unexpected disconnect`.** Causa: rete debole su pacchi grossi + due motori auto-sync (Max/Gael) che pushano nello stesso minuto sullo stesso branch. Contromisura: light-sync via worktree | **APERTO — «funziona ma è un workaround, non una soluzione»** |
| `ERR-20260719-001` | 2026-07-19 | Max e Gael costruiscono la stessa sera due switcher diversi per lo stesso file EmpireDesk, contratti API incompatibili | CHIUSO |
| `ERR-20260719-002` | 2026-07-19 | tile "Caroselli" sarebbe stato un bottone finto: il selftest verificava il path, non gli argomenti runtime | CHIUSO |
| `ERR-20260720-001` | 2026-07-20 | UI EmpireDesk costruita, consegnata e bocciata da Max: riferimento visivo mai verificato prima del build | CHIUSO (pivot same-day) |
| **`ERR-20260905-001`** | **2026-09-05** | **il battito/recap di Emperator è uscito fuori forma almeno 4 volte nello stesso giorno.** Causa radice: «La regola viveva solo in prosa (dottrina + reminder), **mai in un controllo eseguito prima dell'invio**: l'enforcement dipendeva dalla disciplina del turno in corso, non da un gate». Contromisura in vigore: `scripts/gate_battito_hook.py`, hook **Stop** in `.claude/settings.json`, blocca la consegna; provato 6/6 con `scripts/test_gate_battito.py` | **APERTO** — «il gate copre la FORMA; il contenuto resta non verificabile da macchina. Chiusura solo dopo N battiti reali passati dal gate» |

**`ERR-20260905-001` è il precedente che serve a tutto questo piano.** È l'unico caso documentato in
cui una regola dell'Impero è passata **dalla prosa a un hook che blocca** — ed è stato scritto ieri.
La sua causa radice descrive alla lettera la condizione di tutti e 14 gli organi censiti: regole
scritte benissimo, enforcement affidato alla disciplina di chi passa di lì. La cura, lì, è stata di
dieci righe di Python agganciate a un evento.
