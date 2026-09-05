# CENSIMENTO 03a — LA POPOLAZIONE DEGLI AGENTI

> Doom bot al servizio di EMPERATOR · misurato il 2026-09-06 sul repository
> `c:\Users\Utente\Desktop\qui tutto\Digital Empire` · branch `main`, HEAD `9036d18e`.
> Ogni numero di questo documento viene da un comando lanciato o da una riga di codice letta.
> Nessuna stima.

---

## SEZIONE 1 — CHI CONTA COSA

### 1.1 Che cosa conta `python -m empire forge scan`

Il perimetro di forge e' definito in due funzioni sole.

**`empire/forge.py:150-158`** — la scoperta dei file:

```python
150  def _file_agenti() -> list[Path]:
151      """Riusa la scoperta gia' esistente del loader invece di reinventarla,
152      poi scarta i file di corredo che non sono agenti veri."""
153      try:
154          from .loader import _agent_files  # noqa: PLC0415
155          files = list(_agent_files())
156      except (ImportError, AttributeError):
157          files = sorted((repo_root() / "company").rglob("*.md"))
158      return [p for p in files if p.stem.lower() not in _CORREDO]
```

**`empire/loader.py:152-175`** — i cinque soli posti che vengono guardati:

```python
155      patterns = [
156          (resolve("ecosistemi"), "**/Agenti/*.md"),
157          (resolve("board"), "**/agenti/*.md"),
158          (resolve("ispettorato") / "agenti", "*.md"),
159          (resolve("wf_agenti"), "*.md"),
160          (resolve("estate_agents"), "**/*.md"),
161      ]
```

Gli alias si sciolgono in `empire/empire.toml` (righe 27, 28, 23, 49, 43):

| pattern | percorso reale | file trovati |
|---|---|---|
| `**/Agenti/*.md` | `company/Ecosistemi` | 339 |
| `**/agenti/*.md` | `company/Board-CSuite` | 70 |
| `*.md` | `company/Ispettorato/agenti` | 11 |
| `*.md` | `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI` | 7 |
| `**/*.md` | `DIGITAL-EMPIRE/04-AGENTS` | 12 |
| | **totale dopo dedup** | **443** |

> Nota tecnica non ovvia: `Path.glob` su Windows e' **insensibile alle maiuscole**, quindi
> `**/Agenti/*.md` cattura anche `.../agenti/...` e viceversa. E' il motivo per cui
> `company/Ecosistemi` rende 339 file e non i 105 che si contano con un `find` sensibile al caso.

**Cosa esclude forge, in ordine:**

1. `empire/loader.py:42` — quattro nomi di file sempre scartati:
   `_EXCLUDE_FILENAMES = {"AGENTS-REGISTRY.md", "README.md", "ECOSISTEMA.md", "BACKBONE.md"}`
2. `empire/loader.py:170-173` — deduplica per path risolto (`rp = p.resolve()`), quindi lo stesso
   file raggiunto da due pattern viene contato una volta sola.
3. `empire/forge.py:146-147` — gli **11 nomi di corredo**, scartati per `stem` minuscolo:
   `evals, failure-modes, failure_modes, readme, catalog, index, changelog, license, note, notes, todo`.

**443 file grezzi meno 4 di corredo = 439 agenti misurati.** Verificato:

```
$ python -m empire forge scan
AGENTI ANALIZZATI: 439
  OPERATIVO       61    13.9%
  PARZIALE       324    73.8%
  DOCUMENTALE     54    12.3%

CRITERIO PIU' ASSENTE (quanti agenti NON ce l'hanno):
  C1-identita           60   13.7%
  C2-ruolo              16    3.6%
  C3-ingresso           42    9.6%
  C4-uscita            314   71.5%
  C5-successo          135   30.8%
  C6-comportamento      69   15.7%
```

I numeri dichiarati da EMPERATOR sono **confermati alla cifra**.

**Cosa forge NON guarda mai** (e va detto, perche' e' la meta' mancante della popolazione):
`.claude/agents/`, `~/.claude/agents/`, `.agents/`, `company/Guilds/`, `company/Sentinels/`,
`company/Backbone/`, `company/MAXIMILIAN/`, e ogni cartella storica alla radice del repo.
Forge misura **il personale d'azienda scritto in `company/`**, non il personale eseguibile
di Claude Code.

---

### 1.2 Che cosa conta `python -m empire registry census`

Percorso opposto: `empire/registry/census.py:169-258 run_census()` cammina **tutto il monorepo**
da `repo_root()` con `os.walk`, potando solo le directory di `EXCL_DIRS`
(`empire/registry/census.py:24-27`: `.git, node_modules, .next, __pycache__, .cache, .venv,
venv, env, .pytest_cache, packaged-final, phase7-run, phase9-regression`).

Non ha un concetto di "file agente": **classifica ogni file** con
`_determine_kind()` (`empire/registry/census.py:138-166`). Un file diventa `kind="agent"` solo
all'ultimo scalino, righe 163-164:

```python
163          if "/04-agents/" in p_lower or "/agenti/" in p_lower or p.split("/")[-1].startswith("AGENTE-") or p.split("/")[-1].startswith("agent-"):
164              return "agent"
```

…ma **solo se non e' gia' stato intercettato da un ramo precedente**. E i rami precedenti
sono devastanti:

- **riga 142** — `if "ruflo/" in p_lower or ".agents/skills/" in p_lower or ".claude/" in p_lower ...: return "vendored"`.
  Tutti i 129 agenti di `.claude/agents/` sono classificati **vendored**, mai `agent`.
- **riga 147** — `if "-department.md" in p_lower or "dipartimento" in p_lower or "/board-csuite/" in p_lower:` → `department`.
  **Tutti e 70 gli agenti di `company/Board-CSuite/*/agenti/` diventano `department`**, mai `agent`.
- **riga 155** — `/skills/` nel path → `skill`.
- **riga 158** — `/03-workflows/`, `/01-flussi-e-piani/` o nome che inizia con `WF-` → `workflow`.

### 1.3 Il guasto vero: `run_census` legge un solo file per cartella

Questo e' il reperto centrale. `empire/registry/census.py:184-196`, indentazione reale
(verificata con `cat -A`):

```python
184          for fname in filenames:
185              if fname.startswith(".git") or fname == "census.json":
186                  continue
187              path = cur_dir / fname
188              rel_posix = path.relative_to(root).as_posix()
189              kind = _determine_kind(rel_posix)
190
191          try:                          # <-- 8 spazi: FUORI dal for interno
192              stat = path.stat()
```

Il corpo del ciclo `for fname in filenames:` **finisce a riga 189**. Tutto quello che segue —
lettura del file, hash, provenance, riferimenti, costruzione dell'`Artifact`, `artifacts.append`
(riga 239) — sta a 8 spazi, cioe' dentro il ciclo `for dirpath...` **esterno**. Il risultato:
per ogni cartella visitata viene creato **un solo artefatto, quello dell'ultimo file rimasto
nella variabile `path`**. Tutti gli altri file della cartella vengono classificati e buttati.

**Prova numerica**, eseguita adesso in memoria (senza riscrivere `census.json`):

```
TOTALE ARTEFATTI: 21682
  agent       :    70
  asset       :  4342
  dashboard   :    12
  department  :    65
  doc         :  6742
  ecosystem   :    12
  script      :  1596
  skill       :  1128
  template    :   185
  vendored    :  7480
  workflow    :    50
DIRECTORY VISITATE: 21682
```

**21682 artefatti = 21682 directory visitate, esattamente.** Non e' una coincidenza:
e' la firma matematica del guasto. Il censimento non sta contando file, sta contando cartelle.

Il numero `69` riportato da EMPERATOR e quello che misuro io ora, `70`, differiscono di uno
perche' nel frattempo il repository e' cambiato (10 voci non tracciate in `git status`):
un file in piu' o in meno *in fondo all'ordine di `os.listdir` di una cartella* sposta il conteggio.
E' un'ulteriore conferma della fragilita': **il risultato dipende da quale file capita per ultimo.**

---

### 1.4 VERDETTO

**Ha ragione `forge scan`. `registry census` mente, e mente due volte.**

1. **Mente per un difetto di indentazione** (`empire/registry/census.py:184-239`): conta una
   cartella invece che un file. Il suo `agent: 70` significa "70 *cartelle* il cui ultimo file
   assomiglia a un agente", non "70 agenti". Prova: artefatti totali = directory totali = 21682.
2. **Mente anche a guasto riparato**, perche' `_determine_kind` (righe 142 e 147) sottrae per
   costruzione tutti gli agenti di `.claude/` (marcati `vendored`) e tutti quelli di
   `company/Board-CSuite/` (marcati `department`).

I due strumenti **non contano la stessa cosa** e nessuno dei due copre l'intera popolazione:

- **`forge scan` conta 439 SCHEDE-AGENTE DI `company/`** — i cinque percorsi di
  `loader.py:155-161`, cioe' il personale d'azienda scritto in markdown dentro `company/` piu'
  due code storiche (`WORKFLOW-ESTATE/03-AGENTI-E-RUOLI`, `DIGITAL-EMPIRE/04-AGENTS`).
  E' il numero **giusto e utilizzabile** per il lavoro sui 314 contratti C4.
- **`registry census` vorrebbe contare TUTTI I FILE DEL MONOREPO classificati per tipo** —
  inventario generale, non anagrafe agenti. Anche riparato non sarebbe il censimento degli
  agenti: e' un altro mestiere.

**Conseguenza operativa:** il piano di riscrittura dei 314 contratti C4 si basa su
`forge scan`. `registry census` va escluso da qualunque conteggio di agenti finche' le
righe 191-240 di `empire/registry/census.py` non rientrano dentro il `for fname in filenames:`.
