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

---

## 3. `company/Sentinels/` — le guardie (APPROFONDIMENTO)

**Cosa è** (da `company/Sentinels/README.md`): «I Sentinel operano su **tutti i livelli** della
holding — non su richiesta, ma in modo continuo e proattivo. Possono bloccare qualsiasi delivery
che viola il Mandato Empire, indipendentemente dalla gerarchia. Sono l'autorità di enforcement di
LX.» La differenza dichiarata con le Guild: «Guild: expertise su richiesta. **Sentinel: enforcement
automatico (blocca senza essere chiamato).**» E: «Solo i fondatori (LX) possono derogare a un
Sentinel — e devono documentarlo con ADR.»

**Contenuto reale — 6 file, tutti .md, tutti README.** `README.md` (23 righe),
`Cost-Sentinel/README.md` (116), `Quality-Sentinel/README.md` (123), `Drift-Sentinel/README.md`
(116), `Security-Sentinel/README.md` (117), `BrandVoice-Sentinel/README.md` (130). Zero script,
zero test, zero daemon.

### Le 5 sentinelle — cosa sorvegliano, con quale soglia, e se si attivano da sole

**1. Cost Sentinel** (`Cost-Sentinel/README.md`) — ID registro `SENT-COST-001`, supervisore CFO.
*Sorveglia:* crediti API per agente/team/ecosistema/brand_kit, tier modello usato vs routing policy
3-tier, agenti in loop, Opus su task Tier 0-1, dry-run eseguito o no.
*Soglie (7, tutte numeriche):* **60%** envelope → log + notifica CFO; **80%** → warning CFO+COO+CEO
`priority: HIGH`; **95%** → blocco task non urgenti + escalation CFO; **100% + accelerazione** →
stop immediato + escalation CEO; **Opus su Tier ≤1** → segnalazione + raccomandazione downgrade;
**oltre 20 chiamate/min per oltre 2 min** → sospensione agente; **dry-run saltato** → blocco
esecuzione.
*Si attiva da sola?* **NO.** Lo dice il file stesso: KPI «Latenza alert dalla soglia: < 30 secondi
**(quando daemon attivo)**» — il daemon non esiste. E lo `Stato` chiude: «Implementazione automatica
da costruire in F2-F5. Nelle prime fasi (F1-F3): eseguito manualmente come checklist dal fondatore o
da Claude.» In più, il posto dove dovrebbe scrivere è `company/runtime/metrics/runs.jsonl` —
`company/runtime/` **non esiste**.

**2. Quality Sentinel** (`Quality-Sentinel/README.md`) — ID `SENT-QUAL-001`, supervisore CMO.
*Sorveglia:* score APSOC di ogni output di conversione, completezza dei blocchi APSOC, pass-rate per
team sugli ultimi 10 run, reject consecutivi, trend qualità.
*Soglie (6):* **APSOC sotto 80/100** su copy standard → blocco consegna; **sotto 85/100** su sales
page o preventivo → blocco + escalation; **P dopo S** → **meno 15 punti automatici e blocco
obbligatorio indipendentemente dal totale**; **pass-rate sotto 90% su 10 run** → segnalazione
Quality-Guild + CMO; **2 reject consecutivi stesso team** → escalation automatica; **trend in calo
per 3 cicli** → convocazione Quality-Guild + CTO.
*Si attiva da sola?* **NO.** Stesso blocco `Stato`: «eseguito manualmente come checklist».
Nota: il KPI «Gate bypassati: 0 (per definizione — Mandato Art.4.1)» è vero solo perché il gate non
gira: un gate che non si esegue non si può bypassare.

**3. Drift Sentinel** (`Drift-Sentinel/README.md`) — ID `SENT-DRIFT-001`, supervisore CTO.
*Sorveglia:* coerenza tra output e ADR attivi in `company/Memory/decisions/`; lag di sync tra
`second-brain-vault/wiki/` e AgentDB; agenti fuori dal proprio scope in `registro-agenti.yaml`;
documenti normativi (MANDATO-EMPIRE.md, ADR, README Backbone) modificati senza entry in
`wiki/log.md`; decisioni architetturali senza ADR.
*Soglie (5):* **contraddizione bloccante** rilevata da `contradiction-analyzer` → blocco
merge/deploy; **lag wiki/AgentDB oltre 24h** → forzatura sync; **handoff fuori scope** → blocco
handoff; **documento normativo modificato senza log** → **blocco commit**; **decisione
architetturale senza ADR** → richiesta ADR retroattivo. Escalation al Board se non risolto in **24h**.
*Si attiva da sola?* **NO** — ed è la più grave delle cinque, perché è quella che dovrebbe bloccare
i commit. Non esiste alcun hook git: `.git/hooks/` contiene **solo i 14 file `.sample`** di default,
nessuno attivo. Nessun `PreToolUse` in `.claude/settings.json` la richiama.

**4. Security Sentinel** (`Security-Sentinel/README.md`) — ID `SENT-SEC-001`, supervisore CTO.
*Sorveglia:* segreti in file tracciati (pattern `sk-`, `ANTHROPIC_API_KEY=`, `password=`, `token:`,
`instagram_session.json`, `linkedin_session.json`); PII in output esterni; prompt/SQL injection e
XSS; supply-chain (npm/python/vendor nuovi); permessi anomali; repo cliente mescolati col monorepo.
*Soglie (5):* **secret in commit** → blocco push + quarantena + istruzione rotazione; **PII in
output esterno** → blocco invio; **skill/vendor senza scan** → blocco adozione; **permessi fuori
scope** → quarantena agente; **compromissione sospetta** → stop agente + consenso byzantine
CTO→CEO. KPI: «Tempo di blocco dalla rilevazione: **sotto 5 secondi (pre-commit hook sincrono)**».
*Si attiva da sola?* **NO.** Il file stesso dichiara la dipendenza mancante: «`git-secrets` pattern
— pre-commit hook (**da configurare in `.claude/settings.json` F2**)». Verificato in
`.claude/settings.json`: i `PreToolUse` presenti sono due, entrambi `graphify.exe hook-guard`
(matcher `Bash|Grep` e `Read|Glob`). Nessuno riguarda la sicurezza. E `.git/hooks/` è privo di hook
attivi. **La guardia che dovrebbe bloccare i segreti in meno di 5 secondi non è collegata a niente.**

**5. BrandVoice Sentinel** (`BrandVoice-Sentinel/README.md`) — ID `SENT-BV-001`, supervisore CMO.
È l'unica dichiarata **LX-Sentinel**: «può bloccare anche output approvati dal Board».
*Sorveglia:* ogni output con parole verso l'esterno — email, DM, landing, sales page, preventivi,
post, caroselli, script, comunicazioni cliente. Aspetti: tono diretto-provocatorio-trasparente
(Art.2.1), ogni claim con proof in struttura CPB (Art.2.2), P prima di S (Art.2.4), nessun canone
mensile (Art.3.2), nessun dependency-language (Art.1.2).
*Soglie:* tabella di **8 anti-pattern bloccanti** (AI-slop, icebreaker vuoto, hype senza dato, tono
agenzia tradizionale, dependency-language, canone implicito, APSOC incompleto, qualificatore molle),
ognuno mappato sull'Articolo violato. Gate G2 = **checklist binaria a 8 item: un solo fail = output
bloccato**. Escalation CMO a **3 o più blocchi dello stesso anti-pattern in 7 giorni**.
*Si attiva da sola?* **NO.** Stesso `Stato` di chiusura delle altre quattro. Il fallback dichiarato
è «checklist §Checklist Brand Gate in `Mandato/MANDATO-EMPIRE.md`».

### Confronto con `.claude/agents/sentinel-*.md`

**5 su 5 esistono e sono invocabili**, e sono file sostanziosi, non stub:
`sentinel-brandvoice.md` (319 righe), `sentinel-cost.md` (360), `sentinel-drift.md` (322),
`sentinel-quality.md` (376), `sentinel-security.md` (350).
**Ma tutti e cinque dichiarano `model: haiku`**, e questo contraddice i README:
`Drift-Sentinel/README.md` prescrive «Sonnet (contradiction analysis) / Opus (analisi
architetturale complessa)», `Quality-Sentinel/README.md` «Sonnet (audit APSOC) / Haiku (checklist
semplici)», `Security-Sentinel/README.md` «Haiku (scan pattern-matching) / **Sonnet** (analisi
supply-chain)». Sulla carta le sentinelle salgono di modello quando il lavoro è difficile; nei file
invocabili sono tutte inchiodate a Haiku. Il caso Drift è il più pesante: l'analisi architetturale
prescritta a Opus gira a Haiku.

Le descrizioni degli agenti dicono tutte «Attiva su ogni output / ogni commit / ogni modifica» — ma
"attiva su" in un file agente è **testo per il router semantico**, non un trigger: nessun hook le
invoca. La parola "always-on" nei README e "ogni commit" nelle descrizioni non ha, oggi, nessun
meccanismo che la renda vera.

**Come si attivano oggi.** Nessun hook, nessun daemon, nessun git hook. Gli unici riferimenti in
codice sono `.claude/fix_descriptions.py:142-147` (scrive le descrizioni) e
`.claude/fix_agents_frontmatter.py:117` (assegna il modello: `if any(x in name for x in
["sentinel", "guild-cost", "bb-"])` — **è questa riga che le ha messe tutte su Haiku**). Sono
registrate in `company/Backbone/Identity-HR/registro-agenti.yaml` righe 177-233 (`sentinels: 5`) con
il path del README di ciascuna: il registro le conosce, nessuno le chiama. **Si attivano solo se
qualcuno scrive il loro nome in chat.**

**Che cosa producono e dove finisce.** Ognuna produce un **giudizio JSON con blocco**: schema
completo in ogni README (per BrandVoice: `{"brand_gate_pass": false, "score_g2": "5/8",
"item_falliti": [...], "azione": "rewrite_required", "incident_id": "INC-BV-20260611-005"}`;
analoghi per le altre quattro). Le destinazioni dichiarate sono due, **e nessuna delle due esiste su
disco**: `patterns/incidents/{cost,quality,drift,security,brand}/` (namespace AgentDB) e
`company/runtime/metrics/runs.jsonl`. Gli `incident_id` hanno un formato preciso
(`INC-<TIPO>-YYYYMMDD-NNN`) e nessun posto dove essere scritti.

**Cosa manca perché siano vive:**
- (a) **comando** — c'è a metà: 5 agenti invocabili a nome. Manca il trigger automatico, che per un Sentinel *è* la definizione: «blocca senza essere chiamato».
- (b) **contratto** — c'è, ed è il migliore di tutto il governo: input JSON, output JSON, soglie numeriche, escalation table. Riusabile così com'è.
- (c) **posto stabilito** — **rotto due volte**: `company/runtime/metrics/` non esiste e `patterns/incidents/` non esiste.
- (d) **test** — assente.

**Difficoltà: MEDIA per le tre "di testo" (Quality, BrandVoice, Cost-checklist), BASSA per Security
e Drift.** Security e Drift sono basse perché il meccanismo è già noto e già in uso nel repo:
`.claude/settings.json` ha già due `PreToolUse` funzionanti (graphify) — se ne aggiunge uno che
chiama uno script di scan; e un `pre-commit` in `.git/hooks/` è un file di dieci righe.
Quality/BrandVoice/Cost richiedono invece che qualcuno chiami il gate al momento della consegna, e
oggi il momento della consegna non è un evento intercettabile. Prima di tutto: creare
`company/runtime/metrics/` e `patterns/incidents/`, altrimenti anche una sentinella che scatta non
ha dove scrivere.

---

## 4. `company/Mandato/` — la legge (APPROFONDIMENTO)

**Cosa è** (da `company/Mandato/README.md`): «Questa cartella contiene **la costituzione della
holding**: `MANDATO-EMPIRE.md`. **Nessun agente, nessun codice: solo le leggi.** Tutto ciò che esce
da Digital Empire — a qualsiasi livello, L0→L5 — deve rispettarle.» Gerarchia stabilita nel
documento: `Mandato (LX) > Board (L0) > Ecosistema (L1) > Reparto (L2) > Workflow (L3) > Funzione
(L4) > Agente (L5)`.

**Contenuto reale — 2 file .md.** `MANDATO-EMPIRE.md` (242 righe, 14.420 byte, versione 2.0 F1-bis,
aggiornato 2026-06-11 in calce ma con l'Art.8 datato 2026-07-22 nel corpo) e `README.md` (65 righe,
3.279 byte). È l'organo più piccolo del governo e il più citato dagli altri.

### GLI ARTICOLI — elenco per esteso (per i gate che dovranno citarli)

**Articolo 1 — Identità e Posizionamento** (righe 16-46)
- **1.1 Chi siamo** — multi-business company AI-native, Max founder + Gael socio operativo. «Costruiamo e vendiamo sistemi AI operativi — non consulenza, non slide, non promesse».
- **1.2 Il posizionamento fondativo (non negoziabile)** — *«L'agenzia progettata per essere licenziata.»* Ogni delivery punta all'autonomia del cliente. «Qualsiasi copy, contratto o architettura che crea lock-in del cliente viola questo Articolo.»
- **1.3 I 4 pilastri business** — Agency · Info Business · Multi-Business · Holding AI-native, con la mappa ai 10 ecosistemi.
- **1.4 Regola di pertinenza** — «Se un task non è riconducibile a un ecosistema, non si esegue: si porta al Board.»

**Articolo 2 — Brand Voice ("prove, non promesse")** (righe 48-78)
- **2.1 La voce** — diretta, provocatoria, trasparente, «tre aggettivi, in quest'ordine», ciascuno con definizione operativa.
- **2.2 Invariante assoluta: MAI un claim senza evidenza** — struttura **CPB (Claim → Proof → Benefit)**. «Un claim senza proof è un difetto bloccante… vale anche per il Board.»
- **2.3 Anti-pattern bloccati** — 5 voci: AI-slop, dependency-language, hype non fondato, tono agenzia tradizionale, canoni impliciti.
- **2.4 Framework di scrittura** — **APSOC** (Attenzione → Problema → Soluzione → Obiezioni → CTA). «P sempre prima di S (violazione = meno 15 al gate).»

**Articolo 3 — Offerta e Pricing Policy** (righe 80-110)
- **3.1 Listino corrente (pubblico e fisso)** — Outreach Factory €4.000 · Content Factory €3.500 · Second Brain €2.500 · Engine Room (bundle) €8.000. Setup 7 giorni lavorativi, 90 giorni di supporto inclusi.
- **3.2 Invarianti pricing** — 3 assolute: one-time zero canoni · codice di proprietà del cliente · sconti solo via bundle.
- **3.3 Chi decide i prezzi (ADR-005 punto 4)** — team prezzi propone, Max approva a lotti, ogni variazione → ADR.
- **3.4 Prodotti info e multi-business** — «Un prodotto senza prezzo approvato non si lancia — ma non blocca la costruzione dell'infrastruttura».

**Articolo 4 — Qualità (gate non bypassabili)** (righe 112-138)
- **4.1 Principio** — «I gate non sono bypassabili: nessun flag `--skip`, nessuna eccezione inline.» Unica via alternativa: deroga registrata dal Board via raft in `Memory/decisions/`.
- **4.2 Gate copy (APSOC)** — score ≥ 80/100 standard, ≥ 85/100 sales page e proposte, P prima di S, **Brand gate G2** binario.
- **4.3 Gate codice e sistemi** — dry-run obbligatorio; `verify-empire` verde (5 categorie: struttura · brand · APSOC · costi · sicurezza) prima di ogni chiusura di fase; zero bug bloccanti; **i sistemi attivi non si riscrivono: si wrappano (ADR-003)**.
- **4.4 Gate contenuti** — revisione umana obbligatoria in F1-F7.

**Articolo 5 — Memory-first e Wiki-first (ADR-002, pattern #12 e #13)** (righe 140-160)
- **5.1 Memory-first** — leggere `INDEX.md` + `STATO-EMPIRE.md` prima; checkpoint `CP-YYYYMMDD-NNN.md` dopo. «Nessun task è "fatto" finché non è salvato in Memory.»
- **5.2 Wiki-first** — `second-brain-vault/wiki/` è la fonte di verità leggibile; «in caso di conflitto wiki ↔ AgentDB: vince la wiki». Lag vigilato dal Drift-Sentinel, KPI sotto 24h.
- **5.3 Decisioni** — ogni decisione architetturale o di policy → ADR con contesto, decisione, conseguenze, decisore, data, contradiction-check.

**Articolo 6 — Multi-tenant by design (pattern #11)** (righe 162-177)
- **6.1 Principio** — «ogni workflow accetta `brand_kit` + `icp` come input obbligatori: un handoff senza brand_kit dichiarato è invalido».
- **6.2 Conseguenze operative** — niente brand hard-coded; default `DE` (ink/paper/orange `#fb4604`); cost-attribution per cliente; «Il Mandato vincola COME lavoriamo per i clienti, non la LORO voce».

**Articolo 7 — Sicurezza (zero segreti, PII protetta)** (righe 179-197)
- **7.1 Zero segreti nel repo (assoluto)** — «mai in Git», `.gitignore` blindato (ADR-004); un segreto committato = incidente, blocco push + rotazione + deposito in `patterns/incidents/`.
- **7.2 PII protetta** — scan PII (`aidefence_has_pii`) su ogni output esterno.
- **7.3 Supply-chain e perimetro** — vendor verificati; quarantena per permessi anomali; repo cliente separati dal monorepo.
- **7.4 Enforcement** — Security-Sentinel con autorità di blocco immediato; escalation CTO → CEO.

**Articolo 8 — Regola Assoluta del Workflow Reale e Autocontenuto (Struttura Tangibile 360°)**
(righe 199-219) — è il più recente e l'unico con citazione diretta del founder datata **2026-07-22**:
*«Quando ti chiedo di creare un workflow… voglio che ci sia una cartella reale, tangibile e
autocontenuta… Questo vale per sempre.»*
- **8.1 Divieto assoluto di workflow "solo testo" o dispersi.**
- **8.2 I 6 pilastri obbligatori di ogni cartella workflow** — `01-FLUSSI-E-PIANI/` · `02-AUTOMAZIONI-E-SCRIPTS/` · `03-AGENTI-E-RUOLI/` · `04-SKILLS-E-REFERENCE/` · `05-TEMPLATES-E-KIT/` · `06-DASHBOARD-E-METRICHE/`.
- **8.3 Enforcement (Gate-5-bis e Sentinels)** — chi manca anche di una sola componente è **"Workflow Abusivo / Incompleto"**, bloccato dal Quality-Sentinel e dal Gate 5-bis di Max.

**+ Checklist Brand Gate** (righe 221-238, non è un Articolo ma è operativa e va copiata nei gate
QA): 10 voci a spunta — voce · CPB · APSOC con P prima di S · pricing one-time · zero AI-slop ·
autonomia cliente · brand_kit+icp dichiarati · Art.8 cartella autocontenuta · segreti fuori dal repo
· checkpoint in Memory.

**Totale: 8 Articoli.** Nota: il `README.md` della cartella dice «i **7** Articoli» (riga della
tabella «Cosa c'è qui»): il puntatore non è stato aggiornato quando Max ha aggiunto l'Art.8 il
2026-07-22.

**Agenti definiti: nessuno.** Lo dichiara esplicitamente il README: «Nessun agente, nessun codice:
solo le leggi». Coerente, e per questo l'unico organo dove "0 agenti invocabili" non è un difetto.

**Come si attiva oggi — ed è l'organo con la storia migliore.** Il Mandato è l'unico pezzo di
governo **realmente ancorato al codice**:
- `empire/empire.toml:8` lo usa come **`root_marker`** del monorepo: è il file che definisce dove comincia l'Impero. Riga 13: alias `mandato = "company/Mandato/MANDATO-EMPIRE.md"`.
- `empire/tests/test_seed.py:23` **è un test vero** che ne asserisce l'esistenza; riga 66 asserisce che l'alias `mandato` risolva esattamente a `company/Mandato/MANDATO-EMPIRE.md`.
- `scripts/verify-empire.ps1:81-89` **ne verifica il contenuto**, non solo l'esistenza: quattro check su parole chiave — contiene «APSOC», contiene «brand voice», contiene i prezzi (regex `4\.000|3\.500|2\.500|8\.000`), contiene «non-negoziabil».
- `empire/registry/census.py:104` lo marca come `governance`; `empire/registry/orphans.py:23` lo protegge dalla lista orfani; `empire/dash/render_md.py:27` stampa «Governo: company/Mandato/MANDATO-EMPIRE.md» nel cruscotto; `empire/__init__.py:5` lo cita come fonte di governo del pacchetto.
- `scripts/gen-empire.py:27` lo elenca fra i `REQUIRED_FILES`.

**Chi lo esegue automaticamente, però, è nessuno.** `verify-empire.ps1` non è chiamato da nessun
hook: `.claude/settings.json` non lo nomina, `.git/hooks/` non ha hook attivi. È registrato come
skill in `company/skills-map.yaml:492-494` (`id: verify-empire`, `percorso:
scripts/verify-empire.ps1`) ma va lanciato a mano. Il README del Mandato dichiara «Gli agenti
caricano il Mandato compresso via skill `empire-context` (**hook pre-task**)»: quell'hook pre-task
**non esiste** in `.claude/settings.json`.

**Ho eseguito `verify-empire.ps1` durante questo censimento**: `PASS: 113 / 113 | FAIL: 0 | WARN: 0
— [OK] Tutti i gate VERDE`. Il gate funziona ed è verde oggi. (Nota: `STATO-EMPIRE.md` lo registra
in 4 punti come «verify-empire.ps1 PASS 59/59» — il numero di check è quasi raddoppiato da allora,
i verbali in Memory sono fermi a una versione precedente dello script.)

**Che cosa produce e dove finisce.** Il Mandato non produce: **è consumato**. Il suo prodotto
indiretto è il verdetto di `verify-empire.ps1`, che esce sullo **standard output della console** e
termina con `exit $fail`. Non scrive un file di rapporto da nessuna parte: il verdetto vive finché
la finestra resta aperta, poi sparisce. Il posto stabilito, per questo organo, è quello che manca.

**Cosa manca perché sia vivo:**
- (a) **comando** — c'è: `powershell -File scripts/verify-empire.ps1`, documentato alla riga 2 dello script stesso. Manca l'automatismo (nessun hook lo lancia).
- (b) **contratto** — c'è, ed è il migliore dell'intero perimetro: 8 Articoli numerati con sotto-commi, più una checklist a 10 voci già in forma di gate.
- (c) **posto stabilito** — **manca**: l'esito di verify-empire non viene scritto in nessun file. Un gate il cui verdetto non si deposita non è opponibile a nessuno.
- (d) **test** — **c'è, ed è l'unico organo che ce l'ha**: `verify-empire.ps1` (113 check, verde) + `empire/tests/test_seed.py` (2 asserzioni sul Mandato).

**Difficoltà: BASSA.** È l'organo più vicino al traguardo di tutto il perimetro. Servono due cose:
far scrivere a `verify-empire.ps1` il proprio esito in un file datato (una riga di
`Out-File`), e agganciarlo a un hook `Stop` o `SessionStart` accanto a quelli già presenti. Da
correggere subito, a costo zero, il puntatore «i 7 Articoli» nel README quando gli Articoli sono 8.

---

## 5. `company/Ispettorato/` — Performance & Autocritica (APPROFONDIMENTO)

**Cosa è** (da `company/Ispettorato/README.md`): «L'organo trasversale che misura le performance
dell'Impero. **NON produce, NON corregge da solo: rileva, registra, assegna, verifica.** Indipendente
da chi costruisce». Nasce da una direttiva di Max del 2026-07-04, estesa il 2026-07-20: «report dopo
ogni run, analisi al millimetro, **mai lo stesso errore due volte**, e studio dei cicli di correzione
per fare meglio al primo colpo, e studio di cosa esce bene — non solo di cosa esce male».
Da `ARCHITETTURA.md`: «organo trasversale con **diritto di audit su tutti gli altri**».

**Contenuto reale — 204 file (115 .md, 88 .json, 1 .gitkeep).** È il secondo organo per dimensione
dopo il Board, e l'unico dove i file non sono quasi tutti descrizioni:
- radice: `README.md`, `ARCHITETTURA.md`
- `agenti/` — **11 file** `isp-*.md`
- `workflow/` — **5 file** `WF-*.md`
- `registro/` — **4 file**: `REGISTRO-ERRORI.md`, `REGISTRO-REVISIONI.md`, `REGISTRO-SUCCESSI.md`, `REGISTRO-DECISIONI-ALTIRANGHI.md`
- `report/run/` — **87 report .md reali** · `report/daily/` — 1 (`RPT-2026-07-22.md`)
- `telemetry/runs/` — **87 .json reali** · `telemetry/daily/` — 1 (`2026-07-22.json`)
- `kpi/KPI-EMPIRE-WIDE.md`, `principi/PRINCIPI.md`, `regole/REGOLE.md`, `skills/SKILLS.md` — 1 file ciascuno
- `scripts/` — **solo `README.md`**
- `state/` — **vuota** (contiene solo il `.gitkeep`)
- `report/escalation/` — **non esiste**, pur essendo dichiarata in `README.md` («report/ run/ · daily/ · escalation/») e pur essendo la destinazione scritta in `empire/inspect/report.py:84`

### M1..M5 — cosa è operativo

Da `README.md`, sezione «Stato build (M1→M5, dossier 15 §10)», riportata alla lettera:
- ✅ **M1 — Fondamenta dati**: struttura + REGISTRO-ERRORI migrato (10 voci reali) + REGISTRO-REVISIONI seed + REGISTRO-SUCCESSI seed + KPI empire-wide.
- ⬜ **M2 — Pilota PreventivoForge** (trace JSONL reale).
- ⬜ **M3 — Reparto CF-grade** (11 agenti, 5 workflow) via FORGE.
- ⬜ **M4 — Aggancio Impero** (RECALL/RETRO, handoff MAXIMILIAN/Board/Sentinelle).
- ⬜ **M5 — Estensione** (telemetria outreach, report settimanale, hook post-run).

**Ma il disco dice altro, e dice di più.** Il README è fermo al 2026-07-20 e non registra quello che
è successo cinque giorni dopo:
- **M3 ha i suoi artefatti già a terra**: `agenti/` contiene esattamente gli 11 agenti del roster (`isp-conductor`, `isp-telemetry-collector`, `isp-run-auditor`, `isp-error-registrar`, `isp-recidiva-sentinel`, `isp-kpi-analyst`, `isp-report-forger`, `isp-liaison-altiranghi`, `isp-improvement-dispatcher`, `isp-verifier`, `isp-revision-analyst`) e `workflow/` i 5 workflow (`WF-RUN-AUDIT`, `WF-DAILY-AUTOCRITICA`, `WF-RECIDIVA-GATE`, `WF-REPORT-ALTIRANGHI`, `WF-REVISION-STUDY`). La casella è vuota, i file ci sono.
- **La macchina esiste e funziona, ma non è dove il README la cerca.** `company/Ispettorato/scripts/` contiene **solo un README** che descrive quattro script — `trace_collector.py`, `report_generator.py`, `recidiva_check.py`, `revision_metrics.py` — **che in quella cartella non esistono**. Il codice vero sta in **`empire/inspect/`**: 10 moduli Python (`cli.py` 10.997 byte, `report.py` 10.292, `metrics.py` 7.366, `record.py`, `dispatch.py`, `analyst.py`, `synth.py`, `collector.py`, `confirm.py`, `benchmarks.py`) più `SPEC.md`, che formalizza la **Scorecard 5D** con le formule di calcolo (asse ① `Score = 5 − min(4, errori + retry×0.5 + escalation×2)`, e così per gli altri quattro assi). È il brief `company/Antigravity-Briefs/GEM-03-ISPETTORATO-TELEMETRIA.md` ad averlo consegnato.

**Prova che gira — eseguito durante questo censimento:**
- `python -m empire inspect status` → risponde: `STATO ISPETTORATO GENERALE / Loop aperti: 0 / TIP non confermati: 0 / Pattern in DRAFT: 0`
- `python -m pytest empire/tests/test_inspect.py -q` → **30 passed in 0.28s**

Il CLI espone 7 comandi (`empire/inspect/cli.py:257-311`): `capture` (T1 telemetria di una run),
`analyze` (T2 performance), `dispatch` (T4 feedback e proposte), `confirm` (T5 chiude i feedback:
`confirmed`/`recurred`), `report` (aggregati), `status`, `backfill`. Le destinazioni sono cablate nel
codice: `report.py:15` scrive `company/Ispettorato/report/run/RPT-RUN-<id>.md`, `:84`
`report/escalation/ESC-<id>.md`, `:127` `telemetry/daily/<date>.json`, `:159`
`report/daily/RPT-<date>.md`. Gli alias sono in `empire/empire.toml:23-26` (`ispettorato`,
`isp_telemetry`, `isp_report`, `isp_state`).

**Gli 87 report non sono un flusso: sono un colpo solo.** Coprono 22 giornate distinte dal
**2026-06-10 al 2026-07-24** e si fermano lì: **44 giorni senza un report**, a fronte di una regola
che ne pretende uno «dopo ogni run». Vengono da un'unica esecuzione di `backfill`, come dichiara
`company/Antigravity-Briefs/consegne/GEM-03-CONSEGNA.md:53`: «Eseguendo il comando `python -m empire
inspect backfill`, sono stati caricati ed analizzati tutti i **79 checkpoint storici** di performance
reali presenti nel repository». Il `capture` per una run nuova non l'ha mai chiamato nessuno.

### REGISTRO-ERRORI — dov'è, quante voci, quante aperte

**Percorso:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (8.670 byte, ultimo aggiornamento
**2026-09-05**, ieri: è il file più vivo dell'organo).
**Regola:** «Append-only. Ogni voce chiusa non si riscrive. Un errore già qui che si ripresenta =
**RECIDIVA = gate ROSSO bloccante**.»

**Voci: 11.** L'intestazione dice ancora «Queste 10 voci sono la migrazione iniziale (M1)» — ne è
stata aggiunta una undicesima ieri senza aggiornare quella riga.

**Aperte: 2.**
- **`ERR-20260703-001`** (ricorrente, ultima 2026-07-19/20) — «`git push origin main` fallisce ripetutamente: `send-pack: unexpected disconnect`». Causa: rete debole su pacchi grossi + due motori auto-sync (Max/Gael) che pushano nello stesso minuto sullo stesso branch. Contromisura in atto: light-sync via worktree. Stato dichiarato: «**APERTO — funziona ma è un workaround, non una soluzione**».
- **`ERR-20260905-001`** (2026-09-05) — il battito/recap di Emperator è uscito fuori forma «almeno quattro volte nello stesso giorno». Causa radice, scritta con precisione insolita: «La regola viveva solo in prosa (dottrina + reminder), **mai in un controllo eseguito prima dell'invio**: l'enforcement dipendeva dalla disciplina del turno in corso, non da un gate». Contromisura di 2° livello in vigore: `scripts/gate_battito_hook.py`, hook **Stop** registrato in `.claude/settings.json`, che blocca la consegna; provato 6/6 con `scripts/test_gate_battito.py`. Stato: «**APERTO** — il gate copre la FORMA; il contenuto resta non verificabile da macchina. Chiusura solo dopo N battiti reali passati dal gate».

Le altre **9 sono CHIUSE**. Vale la pena notare che `ERR-20260905-001` è, in tutto questo
censimento, l'unico caso documentato in cui una regola dell'Impero è passata **dalla prosa a un hook
che blocca**: è il precedente esatto che serve a tutti gli altri organi.

**Agenti definiti: 11** (i file `isp-*.md` in `agenti/`). **Invocabili in `.claude/agents/`: ZERO** —
nessun file `isp-*` esiste lì (verificato: `ls .claude/agents/ | grep -c "^isp-"` → 0). L'organo che
ha il codice non ha gli agenti; il Board che ha gli agenti non ha il codice.

**Come si attiva oggi.** A mano, con `python -m empire inspect <comando>`. Nessun hook lo chiama:
in `.claude/settings.json` non compare. Il README stesso lo mette fra i lavori futuri: «M5 —
Estensione (telemetria outreach, report settimanale, **hook post-run**)». `empire/trace.py:11`
registra il capolinea: «`empire inspect` restituisce 0 su tutte e sei le metriche, con nota "nessun
record PERF"» — e `company/Memory/checkpoints/CP-20260724-002.md:39` lo conferma come prova
incrociata di quel giorno.

**Che cosa produce e dove finisce.** Produce **rapporti e verdetti**, con formato fisso: report di
run (`report/run/RPT-RUN-<id>.md`, con sezioni ESITO / TIMELINE / GATE / NUMERI-Scorecard 5D),
report daily, report di escalation, snapshot di telemetria giornaliera, e il verdetto della
sentinella anti-recidiva (`recidiva_check` → `0` errore nuovo, `3` RECIDIVA = gate ROSSO, `2`
registro illeggibile). Le destinazioni **esistono davvero e sono popolate** — è l'unico organo del
governo di cui si può dire. Manca solo `report/escalation/`, che il codice sa scrivere e che sul
disco non c'è ancora.

**Cosa manca perché sia vivo:**
- (a) **comando** — **c'è, ed è dichiarato**: `python -m empire inspect capture|analyze|dispatch|confirm|report|status|backfill`.
- (b) **contratto** — **c'è**: `empire/inspect/SPEC.md` con le formule della Scorecard 5D; `scripts/README.md` con i return code (`0` ok, `1` errore d'uso, `2` dati mancanti, `3` recidiva); template di report in dossier 15 §8.
- (c) **posto stabilito** — **c'è e funziona**: `report/run/`, `report/daily/`, `telemetry/runs/`, `telemetry/daily/` (87+87 file dentro). Da creare `report/escalation/`.
- (d) **test** — **c'è**: `empire/tests/test_inspect.py`, 30 test verdi.

**Manca una sola cosa: qualcuno che chiami `capture` quando una run finisce.** Le quattro condizioni
sono già soddisfatte tutte e quattro — ma su dati fermi al 24 luglio.

**Difficoltà: BASSA.** È l'organo più vicino alla vita di tutto il perimetro, e il modello per gli
altri. Serve un hook post-run che invochi `empire inspect capture`, esattamente come `Stop` già
invoca `gate_battito_hook.py`. Da sistemare in contorno: aggiornare le caselle M3 in `README.md`
(gli 11 agenti e i 5 workflow sono a terra), correggere `scripts/README.md` che descrive quattro
script inesistenti in quella cartella mentre il codice vero sta in `empire/inspect/`, creare
`report/escalation/`, portare gli 11 `isp-*` in `.claude/agents/` se si vuole il reparto invocabile.

---

## 6. `company/MAXIMILIAN/` — l'organo che È Max (gate 5-bis)

**Cosa è** (da `ECOSISTEMA.md`): «Il team di agenti che **incarna Max**: ne ha carattere, carisma,
idee, personalità e — soprattutto — gli **standard**. Non esegue il lavoro degli ecosistemi:
**giudica, corregge la rotta, anticipa.**» Dato un deliverable di fase risponde a una domanda sola:
**«Max approverebbe questo?»** — «è abbastanza grande? abbastanza chirurgico? è "un file markdown"
travestito? cosa avrebbe chiesto IN PIÙ?». E dichiara cosa NON è: «Non è un chatbot "in stile Max":
è un **organo di governo con potere di BLOCCO** (RIFAI = la fase torna a BUILD)».

**Contenuto reale — 15 file, tutti .md, 1.169 righe totali:**
- radice: `ECOSISTEMA.md` (103 righe), `BACKBONE.md` (78), `Corpus-Link.md` (66)
- `Agenti/` — **8** file `MX-*.md`: `MX-PRIME` (71 righe, la Voce/conductor, opus), `MX-VISION` (61, scala e ambizione, opus), `MX-CRITIC` (61), `MX-CHALLENGE` (61), `MX-ANTICIPATE` (61), `MX-STYLE` (61), `MX-FAST` (61), `MX-MEMORY` (64)
- `Skill/` — **2**: `maximilian-standard-gate.md` (93), `maximilian-voice.md` (89)
- `Workflow/` — **2**: `WF-REVIEW-MAXIMILIAN.md` (123), `WF-ANTICIPAZIONE.md` (116)

Nessuno script. La distinzione con il Mandato è scritta con cura in `BACKBONE.md` e vale la pena
riportarla, perché è la regola che decide chi blocca cosa: «**Mandato = legge.** Cosa è *lecito*…
Risposta binaria: lecito/illecito. **MAXIMILIAN = standard e direzione.** Cosa è *all'altezza* di
Max. […] In conflitto: il Mandato prevale sul lecito/illecito; MAXIMILIAN prevale sullo
standard/scala.» I gate sono in serie: ARCHITETTURA → FORGE → MAXIMILIAN → Mandato → Identity-HR →
VIVO.

**Agenti definiti: 8** (`MX-PRIME`, `MX-VISION`, `MX-CRITIC`, `MX-CHALLENGE`, `MX-ANTICIPATE`,
`MX-STYLE`, `MX-FAST`, `MX-MEMORY`).
**Invocabili in `.claude/agents/`: ZERO** (verificato: nessun file `MX-*` né `maximilian*`).
**Le sue 2 skill non sono installate**: `maximilian-standard-gate` e `maximilian-voice` vivono solo
come .md dentro `company/MAXIMILIAN/Skill/`; in `.claude/skills/` non c'è nulla che le contenga.
Il gate 5-bis, che per statuto può rimandare indietro un'intera fase, **non ha oggi un solo modo di
essere invocato**.

**Come si attiva oggi.** Nessun hook, nessuno script, nessun agente. L'unico aggancio al codice è
`empire/empire.toml:33` (`maximilian = "company/MAXIMILIAN"`), che ne fa un alias di percorso — e
quindi `empire/tests/test_seed.py::test_every_alias_exists` verifica che la cartella esista. Verifica
la cartella, non l'organo. Nei log dell'Ispettorato compaiono due tracce di lavoro reale fatto *da*
Max con questo standard (`telemetry/runs/RUN-PERF-20260616-009.json`: «costruire l'organo
MAXIMILIAN dal dossier 12»; `RUN-PERF-20260723-005.json`: «M-A chiusura + gate 5-bis su
G-A/G-C/GEM-04/GEM-05») — il 5-bis è stato eseguito, ma da una persona, non dall'organo.

**Il corpus su cui dovrebbe essere addestrato è quasi vuoto.** `ECOSISTEMA.md` dichiara che
MAXIMILIAN è «addestrata sulle parole reali di Max (`company/Memory/maximilian-corpus/`)». Quella
cartella esiste e contiene **1 solo file**: `direttiva-20260611-scala-v2.md`. Un organo che deve
riprodurre il giudizio di una persona ha una riga sola di quella persona.

**Che cosa produce e dove finisce.** Produce un **verdetto binario con motivi**, in due forme
(`BACKBONE.md`, tabella handoff in uscita):
- `{verdetto:"RIFAI", motivi:[…]}` → la fase **torna indietro** al passo 3 (BUILD): è il potere di blocco;
- `{verdetto:"APPROVA"}` → la fase procede al passo 7 (COMMIT: checkpoint + STATO + push);
- più il brief di anticipazione verso SPEC/BACKLOG, e il record obbligatorio in `maximilian/verdetti` — «tracciamento obbligatorio: Max può ribaltare a posteriori».
Le destinazioni sono **namespace AgentDB** (`maximilian/verdetti`, `maximilian/corpus-index`,
`maximilian/anticipazioni`, `maximilian/calibrazione`), non cartelle: nessuna di esse esiste come
posto scrivibile su disco. Quindi il verdetto oggi non ha dove depositarsi, e la promessa scritta —
«un verdetto perso non si rigiudica a naso, si ricarica da `maximilian/verdetti`» — non è mantenibile.

**Cosa manca perché sia vivo:**
- (a) **comando** — manca del tutto: 0 agenti invocabili, 0 skill installate.
- (b) **contratto** — c'è ed è netto: verdetto binario RIFAI/APPROVA con motivi, più i 2 workflow (`WF-REVIEW-MAXIMILIAN`, `WF-ANTICIPAZIONE`) che ne descrivono il flusso passo per passo.
- (c) **posto stabilito** — manca: i 4 namespace `maximilian/*` non esistono su disco.
- (d) **test** — assente (l'unico test che lo tocca verifica che la cartella esista).

**Difficoltà: MEDIA.** Il materiale c'è ed è di qualità: 8 schede agente, 2 workflow, 2 skill già
scritte. Servono tre mosse concrete: portare almeno `MX-PRIME` in `.claude/agents/` (è il conductor
che sintetizza il verdetto: gli altri 7 può orchestrarli lui), installare
`maximilian-standard-gate` come skill vera in `.claude/skills/`, e dare al verdetto una cartella
(`company/MAXIMILIAN/verdetti/`) invece di un namespace che non esiste. Da fare in parallelo, e
costa poco: **riempire il corpus**. Con un file solo, l'organo non può somigliare a nessuno.

---

## 7. `company/Gerarchia/` — lo schema LX→L5

**Cosa è** (da `company/Gerarchia/README.md`): «Schema completo della gerarchia di EMPIRE OS».
Non è un organo che agisce: è **la mappa che dice a ogni altro organo dove sta**.

**Contenuto reale — 1 file .md, 79 righe.** `README.md`, nient'altro. È l'organo più piccolo del
perimetro.

Contiene l'albero completo con il percorso di ogni livello, ed è la fonte più compatta e più
utile del censimento perché lega ogni livello a una cartella reale:
`LX — DIPARTIMENTO EMPIRE` (Mandato Empire + Sentinels → `company/Mandato/` + `company/Sentinels/`)
→ `L0 — BOARD/C-SUITE`, 7 agenti, decisioni via raft (→ `company/Board-CSuite/`)
→ `L1 — 10 ECOSISTEMI` (→ `company/Ecosistemi/`)
→ `L2 — REPARTI` (→ `.../Reparti/`) → `L3 — WORKFLOW` (→ `.../Workflow/`)
→ `L4 — FUNZIONI` (→ `.../Funzioni/`) → `L5 — AGENTI REALI`, «Running via Ruflo agent_spawn /
Agent tool di Claude Code», con schema fisso «identità · responsabilità · I/O · acceptance criteria ·
failure handling · shared_state · KPI · escalation».

**Agenti definiti: nessuno** — coerente con la natura del file.

**Come si attiva oggi.** Non si attiva: è un documento di consultazione. L'unico riferimento in
codice è `scripts/gen-empire.py:50` fra i `REQUIRED_FILES` e `scripts/verify-empire.ps1:59`
(`company\Gerarchia\README.md` fra i check F1, oggi PASS). Nessun hook, nessuna skill lo legge.

**Che cosa produce e dove finisce.** Non produce nulla. È **il contratto di posizione** degli altri
organi: se un giorno il Board decidesse di spostare un ecosistema, questo è il file che va cambiato
per primo — ed è anche il file che nessuno controlla che sia rimasto vero.

**Cosa manca perché sia vivo:** per un documento-mappa le quattro condizioni non si applicano tutte.
Ha (c) un posto stabilito (è lui il posto) e (d) un test di esistenza in `verify-empire.ps1`.
Mancano (a) e (b) nel senso proprio, e manca la cosa che conta davvero per una mappa: **un controllo
che i percorsi che elenca esistano ancora**. Oggi il file cita `company/Ecosistemi/<NN-NOME>/Reparti/`,
`/Workflow/`, `/Funzioni/` — nessuno verifica che quelle cartelle ci siano per tutti e 10 gli
ecosistemi.

**Difficoltà: BASSA.** Il modo di renderlo vivo è trasformarlo da testo in verifica: un check che
legga i percorsi citati nel file e ne provi l'esistenza — venti righe dentro `verify-empire.ps1`,
che già fa esattamente questo per altri 113 percorsi.

---

## 8. `company/Backbone/` — il sistema nervoso condiviso

**Cosa è** (da `company/Backbone/README.md`): «Il sistema nervoso condiviso della holding. **Nessun
ecosistema lo possiede: tutti lo usano.**» Sei componenti con una catena di dipendenza dichiarata:
COORDINATION (Ruflo) → BUS → BRAIN → GOVERNANCE (gate prima di ogni consegna) → IDENTITY-HR (valida
che mittente e destinatario esistano nel roster) → OBSERVABILITY (logga ogni evento).

**Contenuto reale — 10 file (7 .md, 1 .yaml, 1 .json, 1 .gitkeep), 711 righe di markdown:**
`README.md` (45 righe), `Bus/README.md` (110), `Brain/README.md` (117), `Governance/README.md`
(126), `Identity-HR/README.md` (130), `Observability/README.md` (134), `Coordination/README.md`
(49), più i due soli file non-descrittivi dell'organo:
- **`Identity-HR/registro-agenti.yaml`** — 653 righe, `version: "1.1"`, `updated: "2026-09-01"`, `maintainer: "Identity-HR (Backbone)"`. È **il roster di tutta l'azienda**, con sezioni `board:`, `backbone:`, `guilds:`, `sentinels:` e un blocco `stats:` (righe 228-245): `totale_agenti: 123` — board 7 · backbone 2 · guilds 5 · sentinels 5 · context_engineering 21 · content_forge 25 · master_build_architecture 17 · youtube_factory 14 · youtube_launch 5 · youtube_compliance 4 · outreach 4 · website_creator 3 · standalone 3 (emperator, cc-master, credential-keeper); e `status_ufficiali: 123 # tutti registrati in .claude/agents/ il 2026-09-01`, `status_defined: 0`.
- **`Bus/contracts/HC-template.json`** — lo schema `empire-handoff-contract-v1`: `from` (ecosystem/agent/task_id), `to` (ecosystem/agent/**queue: "company/Backbone/Bus/handoffs/"**), `payload`, `acceptance_criteria` (array), `metadata` (created_at, due_at, priority P1-P3, status pending/in_progress/completed/rejected).
- **`Bus/handoffs/`** — **vuota**: contiene solo il `.gitkeep`. È la coda su cui, secondo i README di Board, Guild e Sentinel, dovrebbe passare ogni comunicazione fra organi. **Non ci è mai passato un solo messaggio.**

**Stato dichiarato dai componenti stessi** (ogni README chiude con una sezione «Stato»):
- **BUS** — «## Stato: **DA COSTRUIRE** (F2, task 2.3)»
- **BRAIN** — wiki ✅ ATTIVO · `company/Memory/` ✅ ATTIVO · AgentDB namespace ⏳ da inizializzare · ReasoningBank ⏳ da costruire (F8) · wiki-syncer ⏳ da forgiare
- **GOVERNANCE** — `scripts/verify-empire.ps1` v1 ✅ **ATTIVO** · `verify-empire.sh` cat.1-5 ⏳ · skill `empire-verify` ⏳ · skill `empire-brand-gate` ⏳
- **IDENTITY-HR** — `registro-agenti.yaml` ✅ PRESENTE · schema tipato ✅ · agenti L1-L5 ⏳ da censire · vista `registro-agenti.md` ⏳
- **OBSERVABILITY** — `company/metrics/` ⏳ da creare · `costs.sh` ⏳ · `dashboard.sh` ⏳ · `neural_train` + `autopilot` ⏳ (F8). **Tutto da fare, niente fatto.**
- **COORDINATION** — «ruflo installato globalmente; init EMPIRE OS da fare (F2, task 2.1)»

Su sei componenti, **uno solo è pienamente attivo** (Governance, e solo grazie a
`verify-empire.ps1`), due sono attivi a metà (Brain via wiki e Memory; Identity-HR via il registro),
tre sono da costruire.

**Agenti definiti: 2** (`backbone: 2` nel registro). **Invocabili in `.claude/agents/`: 2 su 2** —
`bb-handoff-router.md` («Instrada handoff tra ecosistemi, verifica schema HC-v1») e
`bb-memory-writer.md` («Scrive e legge AgentDB per tutti i 10 namespace ecosistema»). Copertura
piena — con l'ironia che `bb-handoff-router` è invocabile ma il BUS che dovrebbe instradare è
«DA COSTRUIRE», e `bb-memory-writer` è invocabile ma l'AgentDB su cui scrive è «⏳ da inizializzare».
Due postini assunti prima delle poste.

**Come si attiva oggi.** Nessun hook. `scripts/gen-empire.py:36-42` elenca i 6 README fra i
`REQUIRED_FILES`; `scripts/verify-empire.ps1:117-121` controlla i quattro pezzi operativi —
`Bus\handoffs` esiste, `Bus\contracts` esiste, `HC-template.json` esiste, `registro-agenti.yaml`
esiste — e sono tutti PASS. Ma sono check di **esistenza**: verificano che la coda ci sia, non che
qualcosa vi transiti. Il registro è citato dal Drift Sentinel come fonte per rilevare gli agenti
fuori scope: nessun codice lo legge per farlo.

**Che cosa produce e dove finisce.** Il Backbone non produce un deliverable proprio: **fornisce il
canale**. I suoi due prodotti concreti oggi sono (1) il roster in `registro-agenti.yaml`, che è il
solo censimento ufficiale degli agenti dell'azienda, e (2) lo schema di handoff in
`HC-template.json`, che è il contratto che tutti gli altri organi citano. La destinazione dei
messaggi — `company/Backbone/Bus/handoffs/` — esiste ed è vuota.

**Una discrepanza da segnalare.** Il registro dichiara `totale_agenti: 123` e `status_ufficiali:
123 # tutti registrati in .claude/agents/`. In `.claude/agents/` i file sono **129**. Sei agenti
girano fuori dal roster ufficiale — e `Identity-HR/README.md` afferma l'invariante contrario:
«nessun agente viene cancellato; solo `stato: retired`… → record creato in registro-agenti.yaml».
Lo stesso README, nella sezione Stato, è rimasto indietro di due mesi: dice ancora
«`registro-agenti.yaml` — ✅ PRESENTE (**19 agenti**: 7 Board + 2 Backbone + 5 Guild + 5 Sentinel)»,
quando il file che descrive ne conta 123.

**Cosa manca perché sia vivo:**
- (a) **comando** — 2 agenti invocabili su 2 definiti; ma i comandi che contano (mandare un handoff, scrivere in AgentDB) non hanno un'implementazione sotto.
- (b) **contratto** — c'è ed è ottimo: `HC-template.json` è uno schema JSON completo e riusabile, l'unico file-contratto eseguibile di tutto il governo.
- (c) **posto stabilito** — c'è per gli handoff (`Bus/handoffs/`, vuota) e per il roster (`registro-agenti.yaml`, popolato). Manca per Observability (`company/metrics/` non esiste).
- (d) **test** — c'è solo di esistenza: 4 check in `verify-empire.ps1`, tutti PASS.

**Difficoltà: MEDIA.** Il pezzo che sblocca tutto il resto è il **BUS**: Board, Guild e Sentinel
descrivono tutti il proprio ingaggio come «manda un handoff sul BUS», e finché la coda resta vuota
quei tre organi non possono parlarsi neanche volendo. Ma il costo reale è basso: il contratto è già
scritto, la cartella già esiste, e "mandare un handoff" può voler dire, al primo giro, scrivere un
JSON conforme a `HC-template.json` dentro `Bus/handoffs/` e un check in `verify-empire.ps1` che
validi i file presenti contro lo schema. Da correggere subito, a costo zero: il numero «19 agenti»
in `Identity-HR/README.md`, e la differenza 123 vs 129 fra registro e `.claude/agents/`.
