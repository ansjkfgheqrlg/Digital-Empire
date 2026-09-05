# Censimento 01b — GLI ORGANI DI GOVERNO

> Perimetro: `company/` **escluse** `Memory/` e `Ecosistemi/` (censite da altri).
> Metodo: ogni riga viene da un file aperto o da un comando lanciato. Conteggi con `find`, esclusi `__pycache__/`, `node_modules/`, `.git/`.
> Data rilevazione: 2026-09-06.

**Quadro dei conteggi (comando `find <organo> -type f`):**

| Organo | File |
|---|---|
| `company/Board-CSuite/` | 163 (163 .md) |
| `company/Guilds/` | 6 (6 .md) |
| `company/Sentinels/` | 6 (6 .md) |
| `company/Gerarchia/` | 1 (1 .md) |
| `company/MAXIMILIAN/` | 15 (15 .md) |
| `company/Mandato/` | 2 (2 .md) |
| `company/Ispettorato/` | 204 (115 .md, 88 .json, 1 .gitkeep) |
| `company/Genesi-Core/` | 64 (64 .md) |
| `company/Backbone/` | 10 (7 .md, 1 .yaml, 1 .json, 1 .gitkeep) |
| `company/org/` | 1 (1 .yaml) |
| `company/01-agency/` | 114 (91 .png, 15 .md, 6 .json, 1 .txt, 1 .gitignore) |
| `company/02-info-business/` | 24 (18 .png, 2 .py, 1 .pdf, 1 .md, 1 .html, 1 .gitignore) |
| `company/Antigravity-Briefs/` | 16 (16 .md) |
| File radice | `GRUPPO.md`, `REGISTRO-IMPRESA.md` (98.577 byte), `skills-map.yaml` (149.298 byte) |

**Nota di metodo — l'unico automatismo esistente.** In `.claude/settings.json` sono
configurati **5 hook** e nessuno di essi nomina un organo:
`SessionStart` → `scripts/empire-sync.ps1 -Mode pull` + `py -3 scripts/emperator_boot.py`;
`Stop` → `py -3 scripts/gate_battito_hook.py` + `empire-sync.ps1 -Mode push`;
`PreToolUse` → `graphify.exe hook-guard`; `UserPromptSubmit` → `py -3 scripts/emperator_hook.py`.
Dove sotto scrivo "nessun hook lo chiama", viene da qui.

---

## 1. `company/Board-CSuite/` — il Board

**Cosa è** (da `company/Board-CSuite/README.md`): «Livello L0 — 7 agenti che governano la holding.
Decisioni: via hive-mind consensus (raft) per task cross-ecosistema. Voto decisivo in stallo: CEO /
Empire-Conductor.» Si convoca quando «Task tocca 2+ ecosistemi / Budget > soglia autorizzata /
Conflitto tra ecosistemi / Proposta di nuovo ADR / Decisione che modifica il Mandato (LX)».

**Contenuto reale — 163 file, tutti .md.** Struttura verificata con `ls` e `find`:
- 7 schede-figura alla radice: `CEO-Empire-Conductor.md`, `COO.md`, `CTO.md`, `CMO.md`, `CRO.md`, `CFO.md`, `Chief-Forge.md` + `README.md`
- 7 cartelle-figura da **21 file ciascuna** (identiche di forma): `README.md`, `ARCHITETTURA.md`, `agenti/` (10 schede), `workflow/` (3), `principi/PRINCIPI.md`, `regole/REGOLE.md`, `skills/SKILLS.md`, `scripts/README.md`, `kpi/KPI.md`, `state/README.md`
- `_BLUEPRINT/` con 8 file: `BP-CEO.md`, `BP-CFO.md`, `BP-CMO.md`, `BP-COO.md`, `BP-CRO.md`, `BP-CTO.md`, `BP-Chief-Forge.md`, `BP-INDEX.md`

Attenzione a `scripts/README.md`: aperto, è **la descrizione** degli script di dispatch/report, non
gli script. In tutto il Board **non esiste un solo file .py o .sh**: 163 file su 163 sono markdown.

**Agenti definiti: 70** (10 per figura, in `*/agenti/`).
Elenco per figura — CEO: `ceo-conductor`, `ceo-analista-strategico`, `ceo-advisor-rischi`,
`ceo-advisor-opportunita`, `ceo-priorita-arbiter`, `ceo-budget-allocator`, `ceo-okr-tracker`,
`ceo-comunicatore`, `ceo-verificatore`, `ceo-memoria`. CFO: `cfo-conductor`, `cfo-budget-guard`,
`cfo-cost-accountant`, `cfo-cost-sentinel`, `cfo-forecast-finance`, `cfo-memoria`,
`cfo-roi-analyst`, `cfo-runway-tracker`, `cfo-spend-approver`, `cfo-tier-router`. CMO:
`cmo-conductor`, `cmo-audience-intel`, `cmo-brand-voice-warden`, `cmo-campaign-strategist`,
`cmo-content-liaison`, `cmo-funnel-architect`, `cmo-launch-coordinator`, `cmo-marketing-liaison`,
`cmo-memoria`, `cmo-performance-analyst`. COO: `coo-conductor`, `coo-backbone-health`,
`coo-cadence-keeper`, `coo-handoff-auditor`, `coo-incident-handler`, `coo-memoria`,
`coo-process-optimizer`, `coo-runtime-marshal`, `coo-sla-tracker`, `coo-sync-keeper`. CRO:
`cro-conductor`, `cro-agency-pipeline`, `cro-cross-sell-mapper`, `cro-deal-desk`,
`cro-forecast-analyst`, `cro-infobusiness-launches`, `cro-memoria`, `cro-pipeline-health`,
`cro-pricing-arbiter`, `cro-retention-revenue`. CTO: `cto-conductor`, `cto-architecture-warden`,
`cto-forge-liaison`, `cto-integration-architect`, `cto-memoria`, `cto-platform-liaison`,
`cto-quality-gate`, `cto-security-sentinel`, `cto-stack-radar`, `cto-tech-debt-tracker`.
Chief-Forge: `cf-conductor`, `cf-agent-registry`, `cf-architettura-liaison`,
`cf-contradiction-warden`, `cf-ecosystem-builder`, `cf-eval-warden`, `cf-forge-liaison`,
`cf-intake-router`, `cf-memoria`, `cf-skill-portfolio`.

**Di questi 70, invocabili in `.claude/agents/`: ZERO.** Verificato con confronto nome-per-nome dei
70 basename contro `.claude/agents/`. L'unico match apparente, `cf-conductor.md`, è un **omonimo di
un altro sistema**: `.claude/agents/cf-conductor.md` riga 3 dichiara «Conductor di Content Forge
2.0. Orchestratore principale della pipeline di trasformazione contenuti», mentre
`company/Board-CSuite/Chief-Forge/agenti/cf-conductor.md` è «Conductor della Crescita
Organizzativa … riporta al CEO». Stesso nome, due entità diverse: chi invocasse `cf-conductor`
aspettandosi il Board otterrebbe la pipeline contenuti.

**Esistono invece 7 agenti C-level distinti**, in `.claude/agents/`: `ceo-empire-conductor.md`,
`cfo-empire.md`, `cmo-empire.md`, `coo-empire.md`, `cro-empire.md`, `cto-empire.md`,
`chief-forge.md`. Sono le 7 figure, ma **non i loro 70 sotto-agenti**: la figura è invocabile, il
suo organico interno no. Il Board dichiara «una figura C-level non è un agente singolo: è
un'organizzazione di governo con un team di 10 agenti specializzati»
(`CEO-Empire-Conductor/README.md`) — nella pratica è esattamente un agente singolo.

**Come si attiva oggi.** Nessun hook. Nessuno script. L'unico riferimento in codice è
`scripts/gen-empire.py` righe 28-35, che elenca 8 file del Board fra i `REQUIRED_FILES` — ma **li
verifica soltanto** («NON tocca i file esistenti: crea solo i mancanti», docstring riga 15):
controlla che esistano, non li convoca. Gli altri hit sono `.claude/fix_descriptions.py:68-70` e
`.claude/fix_agents_frontmatter.py:119`, due utility che scrivono il frontmatter degli agenti, e
`empire/.cache/index.json`, che è **un indice generato**, non un chiamante. **Il Board si convoca
solo a mano, scrivendo il nome dell'agente C-level.**

**Che cosa produce e dove finisce.** Dal `README.md`: «Decisione → ADR in `Memory/decisions/` +
checkpoint STATO-EMPIRE». Da `CEO-Empire-Conductor/README.md`: proposta → voto raft → gate Mandato
→ «ADR + dispatch direttive» verso i 10 ecosistemi «via handoff contract», con «Regola universale:
nessuna decisione è presa finché non è documentata. *Documenta o non esiste*». La destinazione è
quindi scritta (`company/Memory/decisions/`), il canale di dispatch no: l'handoff contract è
nominato ma il Board non ha un solo file eseguibile che lo emetta.

**Cosa manca perché sia vivo:**
- (a) **comando** — manca del tutto per i 70 sotto-agenti; per le 7 figure il comando è "scrivere il nome in chat", che è invocazione ma non comando dichiarato. Manca uno `/board` o uno script di convocazione.
- (b) **contratto** — parziale: il formato ADR è definito in Memory, l'handoff contract è citato ma non ha schema dentro `Board-CSuite/`.
- (c) **posto stabilito** — c'è: `company/Memory/decisions/` + `STATO-EMPIRE.md`.
- (d) **test** — assente. Nessun test nomina il Board (163/163 file sono .md).

**Difficoltà: MEDIA.** Le 7 figure sono già invocabili e la destinazione dell'output è già decisa:
manca il comando di convocazione e un test. I 70 sotto-agenti sarebbero ALTA se li si volesse tutti
invocabili (70 file da portare in `.claude/agents/`, più la collisione `cf-conductor` da
risolvere) — ma probabilmente non serve: bastano le 7 figure vive che li orchestrano dall'interno.

---

## 2. `company/Guilds/` — i collegi trasversali

**Cosa è** (da `company/Guilds/README.md`): «Le Guild sono gruppi di agenti con expertise specifica
che serve **tutti** gli ecosistemi. Non hanno gerarchia verticale — sono colleghi orizzontali
disponibili su richiesta via BUS. Ogni Guild ha un Guild Master che ne mantiene gli standard.» E la
riga che pesa di più: «Le Guild non hanno workflow propri: eseguono su richiesta degli ecosistemi.»

**Contenuto reale — 6 file, tutti .md, tutti README.** Nient'altro:
`README.md` (26 righe), `Prompt-Guild/README.md` (111), `Copy-APSOC-Guild/README.md` (103),
`Quality-Guild/README.md` (105), `Cost-Guild/README.md` (119), `Design-Guild/README.md` (122).
Nessuna cartella `agenti/`, nessun workflow, nessuno script, nessun template: 5 collegi = 5 file di
descrizione. I README sono però densi e contengono standard veri e riusabili — la routing table
3-tier (Cost-Guild §1), la struttura obbligatoria di un system prompt (Prompt-Guild §1), gli
acceptance criteria per 7 tipi di deliverable (Quality-Guild §1), la palette `--ink #1a1a1a` /
`--paper #f5f0e8` / `--orange #fb4604` (Design-Guild §1), il framework APSOC con i gate G1 ≥80 e
G2 (Copy-APSOC-Guild §1).

**Agenti definiti: 5 Guild Master**, ma solo *nominati* dentro i README, non come file-scheda:
`prompt-guild-master`, `copy-guild-master`, `quality-guild-master`, `cost-guild-master`,
`design-guild-master`. Non esiste un solo file agente in `company/Guilds/`.

**Invocabili in `.claude/agents/`: 5 su 5** — ma **con nomi diversi**: `guild-prompt.md`,
`guild-copy-apsoc.md`, `guild-quality.md`, `guild-cost.md`, `guild-design.md`. La differenza è di
nomenclatura, non di sostanza: le cinque Guild hanno tutte un agente invocabile. È l'organo con la
copertura migliore di tutto il governo.

**Come si attiva oggi.** Nessun hook. L'unico riferimento in codice è di nuovo
`scripts/gen-empire.py` righe 43-48 (6 path di Guild nei `REQUIRED_FILES`): verifica di esistenza,
non chiamata. `empire/.data/census.json` e `empire/.cache/index.json` le indicizzano — sono output,
non chiamanti. `empire/conform.py:247` le nomina in un messaggio di suggerimento («altrimenti
spostarla (es. sotto Genesi-Core/, Guilds/ o il suo workflow)»): è un consiglio di collocazione
file, non un'invocazione. **Il "BUS" su cui i README dicono di mandare la guild_request non esiste
come codice**: si attivano solo scrivendo il nome dell'agente in chat.

**Che cosa produce e dove finisce.** Ogni README elenca i propri deliverable con path preciso:
Cost-Guild → `company/runtime/cost/routing-policy.yaml`, `envelopes.yaml`,
`sentinel-thresholds.yaml`; Design-Guild → `company/runtime/design/DE-design-system.md` e
`company/runtime/design/brand-kits/`; Prompt-Guild → `company/runtime/brain/patterns/prompt/`.
**`company/runtime/` non esiste** (verificato: `ls: cannot access 'company/runtime': No such file or
directory`). Quindi il posto stabilito è stabilito su carta e non esiste su disco: **tutti i
deliverable delle Guild puntano a una cartella fantasma.** Ogni README chiude con lo stesso stato:
«Struttura creata (F1). Agenti L5 da assegnare in F3… Guild Master disponibile in consultazione
manuale (F1-F3)» — l'organo si autodichiara non ancora operativo.

**Cosa manca perché sia vivo:**
- (a) **comando** — i 5 agenti sono invocabili a nome; manca la guild_request come canale reale (lo schema JSON è scritto in ogni README ma nulla lo legge).
- (b) **contratto** — c'è ed è di buona qualità: schema JSON di richiesta + formato_atteso + KPI, in tutti e 5 i README.
- (c) **posto stabilito** — **rotto**: `company/runtime/**` non esiste. Va creata la cartella o vanno riscritti i path.
- (d) **test** — assente.

**Difficoltà: BASSA.** È l'organo più vicino alla vita: 5/5 agenti già invocabili, contratti già
scritti. Bastano `mkdir company/runtime/{cost,design,brain}` con i file di policy dentro, e un test
che verifichi che i tre YAML esistano e siano parsabili.
