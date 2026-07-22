---
Owner: Max · Controllore: Claude · Origine: FORGE · Governo: MANDATO-EMPIRE.md
Esecutore: GEMINI (Antigravity) · Priorità: P0 BLOCCANTE · Created: 2026-07-22
Dipendenze: nessuna · Blocca: GEM-02, GEM-03, GEM-04, GEM-05, GEM-06
---

# GEM-01 — EMPIRE CORE RUNTIME
## Il substrato eseguibile che oggi non esiste

> **LEGGI PRIMA:** `company/Antigravity-Briefs/GEM-00-INDEX-E-PROTOCOLLO.md` (regole non
> negoziabili, protocollo verifica skill, formato consegna). Questo brief presuppone GEM-00 letto.

---

## 1. CONTESTO — cosa c'è e cosa manca

Digital Empire ha, su disco, un'azienda completa **descritta in Markdown**:

```
company/
├── Mandato/MANDATO-EMPIRE.md          ← la costituzione (8 articoli)
├── REGISTRO-IMPRESA.md                ← anagrafe artefatti (ADR-008)
├── skills-map.yaml                    ← mappa skill
├── Board-CSuite/  (163 file)          ← CEO/CFO/CTO/CMO/COO/CRO/Chief-Forge
│   └── <ruolo>/{agenti,kpi,principi,regole,scripts,skills,state,workflow}/
├── Ecosistemi/    (852 file)          ← 10 ecosistemi
│   └── NN-NOME/{Agenti,Funzioni,Reparti,Workflow}/ + ECOSISTEMA.md + BACKBONE.md
├── Genesi-Core/   (64 file)           ← ARCHITETTURA + FORGE
├── Ispettorato/   (27 file)           ← organo performance (telemetry/report/state VUOTE)
├── Guilds/ Sentinels/ MAXIMILIAN/ Backbone/ Gerarchia/
└── Memory/        (113 file)          ← INDEX, STATO-EMPIRE, ADR-001..008, checkpoint
```

**Numero di file Python in tutto `company/`: ZERO.**

Quindi: un agente descritto in `company/Ecosistemi/09-OPERATIONS/Agenti/ops-watchdog.md`
non è un processo. È un foglio. Nessuno lo carica, nessuno lo esegue, nessuno sa se ha girato,
nessuno misura cosa ha prodotto. Lo stesso vale per i 300+ agenti progettati.

**GEM-01 costruisce il pacchetto Python `empire/` che rende quei fogli interrogabili da codice.**
Non li esegue ancora (quello è GEM-06). Li rende **oggetti**: caricabili, validabili, indicizzabili,
risolvibili per path. È la fondazione di tutto il resto.

---

## 2. SKILL DA USARE (verifica prima — protocollo GEM-00 §2)

| Skill | Path | Come usarla qui | Fallback se assente |
|---|---|---|---|
| `sparc-methodology` | `.claude/skills/sparc-methodology/` | applica S→P→A→R→C: scrivi SPEC.md prima di una riga di codice | procedi comunque scrivendo `empire/SPEC.md` a mano con requisiti+acceptance+out-of-scope |
| `agent-specification` | `~/.claude/skills/agent-specification/` | formalizza requisiti e criteri di accettazione | sezione §7 di questo brief è già la spec |
| `agent-architecture` | `~/.claude/skills/agent-architecture/` | definisci file structure + data model + firme funzioni PRIMA di implementare | usa lo schema §5 di questo brief |
| `agent-coder` | `~/.claude/skills/agent-coder/` | implementazione incrementale, una funzione alla volta | — |
| `agent-tester` | `~/.claude/skills/agent-tester/` | pytest per ogni modulo, nessun modulo senza smoke test | scrivi test con `unittest` stdlib |
| `verification-quality` | `.claude/skills/verification-quality/` | gate comportamentale finale | checklist §8 |
| `master-build-architecture` | `DIGITAL-EMPIRE/05-SKILLS/master-build-architecture/` | metodo a fasi con gate tra una fase e l'altra | — |
| `swarm-orchestration` | `.claude/skills/swarm-orchestration/` | i 6 moduli di §5 sono disgiunti → parallelizzabili | esecuzione sequenziale |

**Riporta la tabella di verifica nella consegna. Se `sparc-methodology` esiste, la SPEC è obbligatoria.**

---

## 3. OBIETTIVO IN UNA FRASE

Creare `empire/` — un pacchetto Python installabile in locale che, data la radice del monorepo,
sa dire con precisione: **quali agenti esistono, quali reparti, quali workflow, quali skill, chi
possiede cosa, dove sta ogni cosa, e se la struttura è conforme al Mandato** — con schema
validato e senza mai indovinare un path.

---

## 4. IL PROBLEMA TECNICO CENTRALE DA RISOLVERE PER PRIMO

Il monorepo ha **tre sistemi paralleli che si ignorano**:

| Sistema | Radice | Contiene | Problema |
|---|---|---|---|
| Azienda | `company/` | 1267 md, organigramma completo | zero codice, zero runtime |
| Workflow estate (importato) | `DIGITAL-EMPIRE/` | `00-MEMORY/` … `07-CONTROL/`, 6702 file | auto-contenuto, path relativi interni, non collegato a `company/` |
| Workflow estate (riorganizzato) | `WORKFLOW-ESTATE/` | 6 pilastri Art.8, 2 vuoti | **26 path rotti** che puntano a `00-MEMORY/`, `04-AGENTS/`, `07-CONTROL/` — cartelle che esistono solo in `DIGITAL-EMPIRE/` |

Esempio concreto di rottura, da `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-PERF-LOOP.md`:
```
Esecuzione: Performance Cell (`04-AGENTS/PERFORMANCE-CELL.md`)     ← non esiste in WORKFLOW-ESTATE
perf-collector scrive PERF record in 00-MEMORY/performances/       ← non esiste in WORKFLOW-ESTATE
Comando: python3 00-MEMORY/memory_manager.py perf ...             ← il file sta in 02-AUTOMAZIONI-E-SCRIPTS/
```

**Il primo compito di `empire/` è chiudere questa frattura**, non con una riscrittura, ma con un
**resolver di path** che sa che `00-MEMORY/` (nome logico) → `DIGITAL-EMPIRE/00-MEMORY/` oppure
`WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/`, secondo una mappa dichiarata in un solo file.

---

## 5. ARCHITETTURA RICHIESTA

```
empire/                                  ← NUOVO, radice del monorepo
├── __init__.py                          ← esporta la API pubblica, versione
├── SPEC.md                              ← output di sparc-methodology fase 1
├── ARCHITECTURE.md                      ← output fase 3, con questo albero + data model
├── paths.py                             ← §5.1 risoluzione radice + alias logici
├── config.py                            ← §5.2 config unica, legge empire.toml + .env
├── schema.py                            ← §5.3 dataclass: Agent, Department, Ecosystem, Workflow, Skill, Artifact
├── loader.py                            ← §5.4 parsing dei .md/.yaml → oggetti schema
├── index.py                             ← §5.5 indice materializzato + ricerca
├── conform.py                           ← §5.6 conformità al Mandato (Art.8, ADR-008)
├── cli.py                               ← §5.7 `python -m empire <comando>`
├── empire.toml                          ← mappa alias logici → path reali (UNICO punto di verità)
├── requirements.txt
└── tests/
    ├── test_paths.py
    ├── test_loader.py
    ├── test_index.py
    ├── test_conform.py
    └── fixtures/                        ← mini-monorepo finto per i test, NON path reali
```

### 5.1 `paths.py` — risoluzione radice e alias

Requisiti:
- `repo_root() -> Path`: trova la radice risalendo dall'`__file__` finché non trova
  `company/Mandato/MANDATO-EMPIRE.md`. **Mai path assoluti hardcoded.** Se non la trova,
  solleva `EmpireRootNotFound` con messaggio che dice da dove ha iniziato a cercare.
- `resolve(alias: str) -> Path`: traduce un alias logico in path reale usando `empire.toml`.
  Alias minimi da supportare:
  ```
  company, memory, mandato, registro, skills_map, ispettorato,
  ecosistemi, board, guilds, sentinels, genesi, backbone,
  estate_src        → DIGITAL-EMPIRE/
  estate_wf         → WORKFLOW-ESTATE/
  estate_memory     → DIGITAL-EMPIRE/00-MEMORY/
  estate_agents     → DIGITAL-EMPIRE/04-AGENTS/
  estate_control    → DIGITAL-EMPIRE/07-CONTROL/
  estate_scripts    → WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/
  ```
- `resolve_legacy(ref: str) -> Path | None`: dato un riferimento come `"00-MEMORY/performances/"`
  scritto dentro un `.md` di `WORKFLOW-ESTATE/`, restituisce il path reale, o `None` se davvero
  non esiste da nessuna parte. **Questa è la funzione che ripara i 26 link rotti senza toccare
  i .md** (ADR-003: wrap, non riscrittura).
- Gestione spazi nei path: la radice contiene `qui tutto` e `Digital Empire` — spazi ovunque.
  Ogni uso in subprocess deve passare per `pathlib.Path` e liste di argomenti, **mai
  interpolazione in stringa di shell**.

### 5.2 `config.py`
- Legge `empire/empire.toml` con `tomllib` (stdlib da 3.11).
- Legge `.env` dalla radice (parser minimale, non aggiungere `python-dotenv` se non serve).
- `get_secret(name)` → valore o `MissingSecret` con messaggio azionabile
  (`"Manca FLIKI_API_KEY in .env alla radice del monorepo"`), mai stacktrace nudo.
- **Non stampare mai il valore di un segreto.** Neanche parziale, neanche in debug.

### 5.3 `schema.py` — il data model
Dataclass con `slots=True`, tutte con campi ADR-008:

```python
@dataclass(slots=True)
class Provenance:
    owner: str | None          # es. "Max", "Gael", "Claude"
    controller: str | None
    origin: str | None         # FORGE / import / ...
    governance: str | None     # path al Mandato/ADR
    source_file: Path
    line: int | None           # dove è stato letto il frontmatter

@dataclass(slots=True)
class Agent:
    id: str                    # es. "ops-watchdog", "INT-A02-int-memory-router"
    name: str
    ecosystem: str | None      # "09-OPERATIONS"
    department: str | None
    role: str | None           # director | conductor | operativo | qa | ...
    tier: str | None           # opus | sonnet | haiku — se dichiarato
    skills: list[str]          # skill citate nella scheda
    workflows: list[str]
    prov: Provenance
    cf_grade: bool             # True se rispetta lo standard content-forge 7-file

@dataclass(slots=True)
class Department: ...          # id, ecosystem, agents: list[str], workflows, readme
@dataclass(slots=True)
class Ecosystem: ...           # id, name, departments, agents_count, has_backbone, has_ecosistema_md
@dataclass(slots=True)
class Workflow: ...            # id, file, owner, steps, gates, triggers, referenced_paths
@dataclass(slots=True)
class Skill: ...               # name, path, scope(global|project|vendored), has_skill_md
@dataclass(slots=True)
class Artifact: ...            # qualunque file censito, con prov + hash + mtime
```

Ogni dataclass ha `to_dict()` e `from_dict()` — servono a `index.py` per serializzare in JSON.

### 5.4 `loader.py` — il parser
- `load_frontmatter(path) -> dict`: YAML frontmatter tra `---`. **Tollerante**: se il file non
  ce l'ha (la maggioranza non ce l'ha), non fallisce — restituisce `{}` e marca `prov` con
  campi `None`. Un file senza intestazione è un **finding ADR-008**, non un crash.
- `load_agents(ecosystem: str | None = None) -> list[Agent]`: scandisce
  `company/Ecosistemi/*/Agenti/*.md`, `company/Board-CSuite/*/agenti/*.md`,
  `company/Ispettorato/agenti/*.md`, `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/*.md`,
  `DIGITAL-EMPIRE/04-AGENTS/**/*.md`.
  - Estrai `id` dal nome file, ripulendo prefissi tipo `INT-A02-`, `AGENTE-`.
  - Estrai skill citate cercando pattern: backtick con nome che matcha una skill nota, oppure
    sezioni `## Skill` / `## Skills` / `## Tools`.
  - `cf_grade = True` se accanto alla scheda esistono i 7 file dello standard content-forge
    (`agent.md`, `system_prompt.md`, `tools.md`, `playbook.md`, `failure_modes.md`,
    `eval_cases.json`, `README.md`) — vedi `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/templates/agent/`.
- `load_ecosystems()`, `load_departments()`, `load_workflows()`, `load_skills()`: analoghi.
- `load_workflows()` deve inoltre estrarre **tutti i path citati** dentro il `.md`
  (regex su backtick + pattern `NN-NOME/...`) e metterli in `Workflow.referenced_paths` —
  input diretto per GEM-04.
- **Performance**: il monorepo ha ~9000 file. Il load completo deve stare **sotto 10 secondi**
  a freddo. Usa `os.scandir`, escludi sempre `.git/`, `node_modules/`, `.next/`, `__pycache__/`,
  `packaged-final*/`, `phase7-run/`, `phase9-regression/`.

### 5.5 `index.py` — indice materializzato
- `build_index() -> dict`: esegue tutti i loader, produce un dizionario serializzabile.
- Scrive `empire/.cache/index.json` + `index.meta.json` (timestamp, conteggi, hash della
  configurazione). **`.cache/` va in `.gitignore`.**
- `load_index(max_age_s=3600)`: se la cache è fresca la usa, altrimenti ricostruisce.
- `search(query, kind=None) -> list`: ricerca substring case-insensitive su id/nome/path/skill.
- `stats() -> dict`: conteggi per ecosistema, per tipo, quanti agenti CF-grade, quanti file
  senza intestazione ADR-008, quanti path rotti.

### 5.6 `conform.py` — conformità al Mandato
Tre validatori, ognuno restituisce `list[Finding]` dove
`Finding = (severity: "block"|"warn"|"info", rule: str, path: Path, line: int|None, message: str, fix: str)`:

1. **`check_art8(workflow_root: Path)`** — Mandato Art.8: i 6 pilastri esistono E **non sono vuoti**.
   Deve segnalare oggi, su `WORKFLOW-ESTATE/`: `05-TEMPLATES-E-KIT/` vuota (block),
   `06-DASHBOARD-E-METRICHE/` vuota (block).
2. **`check_adr008()`** — ogni artefatto ha Owner+Controllore+Origine+Governo e compare in
   `company/REGISTRO-IMPRESA.md`. Severity `warn` per i file legacy, `block` per file creati
   dopo il 2026-07-19 (data ADR-008).
3. **`check_links()`** — ogni path citato dentro i `.md` di workflow esiste, direttamente o via
   `paths.resolve_legacy()`. Deve trovare i 26 riferimenti di `WORKFLOW-ESTATE/` e dire, per
   ciascuno, se è **riparabile via alias** (info) o **davvero orfano** (block).

### 5.7 `cli.py` — interfaccia
`python -m empire <comando>`. Comandi minimi:

```
python -m empire status                 # conteggi globali, salute, freschezza indice
python -m empire index --rebuild        # ricostruisce la cache
python -m empire agents [--eco 09-OPERATIONS] [--json]
python -m empire ecosystems
python -m empire workflows
python -m empire skills [--missing]     # skill citate ma non presenti su disco
python -m empire find "watchdog"
python -m empire show agent ops-watchdog
python -m empire conform [--workflow WORKFLOW-ESTATE] [--fail-on block]
python -m empire doctor                 # tutti i check + exit code 1 se ci sono "block"
```

Regole CLI:
- `--json` su ogni comando di lettura, output JSON puro su stdout (parsabile da GEM-05).
- Exit code: `0` ok, `1` findings di severità `block`, `2` errore interno.
- **Prima riga di `cli.py`**, prima di qualunque print:
  ```python
  import sys
  if hasattr(sys.stdout, "reconfigure"):
      sys.stdout.reconfigure(encoding="utf-8", errors="replace")
      sys.stderr.reconfigure(encoding="utf-8", errors="replace")
  ```
  Questa riga esiste perché `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py`
  **crasha oggi** con `UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f9e0'`.
  Non ripetere quell'errore.

---

## 6. SEQUENZA DI ESECUZIONE — task dopo task

### TASK 1 — Ricognizione (nessun codice)
1. Esegui la verifica skill del protocollo GEM-00 §2. Produci la tabella.
2. Leggi in quest'ordine: `company/Mandato/MANDATO-EMPIRE.md` (tutto, in particolare Art.8),
   `company/Memory/INDEX.md`, `company/Memory/STATO-EMPIRE.md` (primi 120 righe),
   `company/REGISTRO-IMPRESA.md`, `company/skills-map.yaml`,
   `company/Memory/decisions/ADR-003-*.md` e `ADR-008-*.md`.
3. Campiona **10 schede agente da ecosistemi diversi** e annota la varianza di formato
   (hanno frontmatter? come si chiamano le sezioni? come citano le skill?).
   Questa varianza determina quanto deve essere tollerante `loader.py`.
4. **Output TASK 1**: `empire/SPEC.md` — requisiti, criteri di accettazione, esplicito
   *out-of-scope* (NON esegue agenti, NON scrive nei .md esistenti, NON tocca `EmpireDesk/platform/`).
   **Gate 1**: la SPEC elenca almeno 12 criteri di accettazione verificabili con un comando.

### TASK 2 — Fondazione (`paths.py`, `config.py`, `empire.toml`)
- Implementa §5.1 e §5.2.
- `empire.toml` deve contenere TUTTI gli alias di §5.1 con il path reale verificato su disco.
- Test: `tests/test_paths.py` — `repo_root()` trovata da 3 CWD diversi; ogni alias risolve a un
  path esistente; `resolve_legacy("00-MEMORY/performances/")` non solleva.
- **Gate 2**: `python -m pytest empire/tests/test_paths.py -q` verde. Incolla l'output.

### TASK 3 — Schema + Loader
- Implementa §5.3 e §5.4.
- Test su fixtures sintetiche (`tests/fixtures/`), poi **un run reale** sul monorepo.
- **Gate 3**: `python -m empire agents --json | python -c "import json,sys; d=json.load(sys.stdin); print(len(d))"`
  restituisce un numero **> 200** (nel monorepo ci sono 300+ agenti progettati) e il load
  completo sta sotto 10 s. Incolla tempo reale misurato.

### TASK 4 — Indice + CLI
- Implementa §5.5 e §5.7.
- **Gate 4**: `python -m empire status` gira su Windows **senza UnicodeEncodeError** e stampa
  conteggi coerenti con `find` manuale. Incolla entrambi gli output affiancati.

### TASK 5 — Conformità
- Implementa §5.6.
- **Gate 5 (il più importante)**: `python -m empire conform --workflow WORKFLOW-ESTATE`
  deve produrre, senza che tu glielo suggerisca a mano:
  - `block` su `05-TEMPLATES-E-KIT/` vuota
  - `block` su `06-DASHBOARD-E-METRICHE/` vuota
  - almeno **20 finding** sui path rotti (ne abbiamo contati 26)
  Se non li trova, il validatore è sbagliato — non il monorepo. Correggi il validatore.

### TASK 6 — Riparazione minima (wrap, ADR-003)
- Correggi **un solo file esistente**: `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py`
  - aggiungi il blocco `reconfigure` di §5.7 in cima
  - forza `encoding="utf-8"` in ogni `open()`
  - fai sì che risolva le sue directory via `empire.paths` invece che relative al CWD
  - **non cambiare la sua interfaccia CLI** né i formati dei record: altri file la citano.
- **Gate 6**: da tre CWD diversi, `python <path>/memory_manager.py status` esce 0 e stampa.
  Incolla i tre output.

### TASK 7 — Chiusura
- `empire/README.md`: come si installa, come si usa, cosa fa e cosa **non** fa.
- `empire/ARCHITECTURE.md`: albero + data model + decisioni prese e scartate.
- Aggiungi `empire/.cache/` al `.gitignore` della radice.
- Registra `empire/` in `company/REGISTRO-IMPRESA.md` (Owner: Max · Controllore: Claude ·
  Origine: FORGE via Gemini/Antigravity · Governo: MANDATO Art.8 + ADR-008).
- Checkpoint: `company/Memory/checkpoints/CP-20260722-GEM01.md`.
- Consegna: `company/Antigravity-Briefs/consegne/GEM-01-CONSEGNA.md` nel formato GEM-00 §4.

---

## 7. DEFINITION OF DONE (checklist verificabile)

- [ ] DoD-1 — `python -m empire status` gira da qualunque CWD dentro il monorepo, exit 0, zero eccezioni
- [ ] DoD-2 — nessun path assoluto hardcoded in tutto `empire/` (dimostralo con un grep incollato)
- [ ] DoD-3 — `python -m empire agents` elenca > 200 agenti reali con ecosistema corretto
- [ ] DoD-4 — indice completo costruito in < 10 s a freddo (tempo misurato incollato)
- [ ] DoD-5 — `python -m empire conform --workflow WORKFLOW-ESTATE` trova i 2 pilastri vuoti + ≥20 link rotti
- [ ] DoD-6 — `python -m empire doctor` esce 1 oggi (perché ci SONO problemi) e lo spiega leggibile
- [ ] DoD-7 — `memory_manager.py status` non crasha più su Windows, da 3 CWD diversi
- [ ] DoD-8 — pytest: ≥ 20 test, tutti verdi, output incollato
- [ ] DoD-9 — doppio run consecutivo di `index --rebuild` → stesso risultato, zero duplicati
- [ ] DoD-10 — zero segreti letti/stampati/scritti; grep di `sk-`, `api_key=`, `token=` in `empire/` vuoto
- [ ] DoD-11 — `empire/` registrato in `REGISTRO-IMPRESA.md` con i 4 campi ADR-008
- [ ] DoD-12 — nessun file di `company/Ecosistemi/**` modificato (dimostralo con `git status`)

---

## 8. ANTI-PATTERN — cose che rendono il lavoro RIFIUTATO

| Anti-pattern | Perché è rifiutato |
|---|---|
| Riscrivere `memory_manager.py` da zero | Viola ADR-003. Si correggono i difetti, si mantiene l'interfaccia. |
| Path assoluti tipo `C:\Users\Utente\...` nel codice | Il repo si sincronizza tra Max e Gael. Si rompe subito. |
| Modificare le schede agente in `company/Ecosistemi/` | Sono specifica approvata. Si leggono. |
| `print()` con emoji senza `reconfigure` | Crasha su Windows. È già successo. |
| Test che girano solo sul monorepo reale | Fragili. Servono fixtures sintetiche + un run reale come conferma. |
| Consegnare senza incollare output reali | "Dovrebbe funzionare" non è una prova. |
| Aggiungere pandas/numpy/pydantic per fare 4 conteggi | Standard library. Se serve davvero, motivalo in una riga. |
| Creare `empire/` dentro `WORKFLOW-ESTATE/` | Va alla **radice del monorepo**: serve a tutta l'azienda, non a un workflow. |

---

## 9. HANDOFF

Quando GEM-01 è chiuso, sblocca in parallelo:
- **GEM-02** (Memory Runtime) — userà `empire.paths` + `empire.schema`
- **GEM-04** (Anagrafe & Link Integrity) — userà `empire.conform` come motore

E consegna a Claude: l'elenco dei finding `block` trovati da `doctor`, perché alcuni
richiedono una **decisione** (ADR), non una correzione tecnica — in particolare:
*"`DIGITAL-EMPIRE/` e `WORKFLOW-ESTATE/` sono due copie dello stesso sistema: quale è la fonte
di verità e cosa si fa dell'altra?"* — questa la decide Max, non Gemini.
</content>
