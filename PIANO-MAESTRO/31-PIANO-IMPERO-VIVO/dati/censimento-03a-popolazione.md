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

---

## SEZIONE 2 — LA SPECIFICA ESATTA DI C1..C6

### 2.0 Come funziona la misura (il meccanismo, prima dei criteri)

`empire/forge.py:119-141 analizza()`:

```python
122      testo = percorso.read_text(encoding="utf-8", errors="replace")
...
127      for nome, (descr, patterns) in CRITERI.items():
128          prova = ""
129          for p in patterns:
130              m = re.search(p, testo, re.IGNORECASE | re.MULTILINE)
131              if m:
132                  prova = m.group(0).strip()[:60]
133                  break
134          criteri.append(Criterio(nome=nome, descrizione=descr, passa=bool(prova), prova=prova))
```

Cinque fatti che cambiano tutto:

1. **Si cerca su TUTTO il file**, testa a coda, comprese le zone dentro i blocchi di codice,
   le tabelle e i commenti. Non c'e' nozione di "sezione".
2. **`re.search`, non `re.match`**: i pattern **non sono ancorati a inizio riga** se non lo
   dichiarano con `^`. Quindi `##\s*Output` scatta anche dentro `### Output` e `#### Output`.
3. **`re.IGNORECASE`**: maiuscole e minuscole sono indifferenti (`## output` vale).
4. **`re.MULTILINE`**: `^` e `$` valgono a ogni riga, non solo a inizio file.
5. **Basta UN pattern** dei tanti elencati: il primo che scatta chiude il criterio (`break`).

**Punteggio e stato** (`empire/forge.py:94-116`): sei criteri, ognuno vale 1/6.
Verificato sui 439 agenti reali:

| criteri passati | punteggio | stato | quanti agenti |
|---|---|---|---|
| 0/6 | 0.0 | DOCUMENTALE | 4 |
| 1/6 | 1.7 | DOCUMENTALE | 4 |
| 2/6 | 3.3 | DOCUMENTALE | 16 |
| 3/6 | 5.0 | DOCUMENTALE | 30 |
| 4/6 | 6.7 | PARZIALE | 114 |
| 5/6 | 8.3 | PARZIALE | 210 |
| 6/6 | 10.0 | OPERATIVO | 61 |

**Conseguenza da tenere a mente per tutto il piano:** `OPERATIVO` richiede **tutti e sei** i
criteri, non "quasi tutti". Un solo criterio mancante degrada a PARZIALE. E i 210 agenti a
5/6 sono a **un criterio solo** dal traguardo — e nella stragrande maggioranza quel criterio
e' proprio C4.

---

### 2.1 C1-identita

- **Nome esatto nel codice:** `"C1-identita"` — `empire/forge.py:56`
- **Descrizione:** `"ha un id stabile con cui invocarlo"`
- **Pattern** (`empire/forge.py:56-57`):
  ```python
  r"^\s*[-*]?\s*\*\*ID\*\*\s*[:=]"      # scatta per primo in  26 agenti
  r"^\s*id\s*[:=]"                       # scatta per primo in   0 agenti
  r"`[a-z0-9][a-z0-9-]{3,}`"             # scatta per primo in 353 agenti
  ```
- **Mancante in 60 agenti su 439 (13,7%).**
- **Testo minimo che lo fa passare:** una qualunque delle tre forme —
  `**ID**: qualcosa` a inizio riga (anche preceduto da `-` o `*`), oppure `id: qualcosa`
  a inizio riga, oppure — ed e' quella che regge il 80% dei pass — **un qualsiasi pezzo di
  codice inline fra backtick lungo almeno 4 caratteri che inizia con lettera minuscola o
  cifra**: `` `ag-a1-icp` ``, ma anche `` `python` `` o `` `agency/a1/icp` ``.

> **Avvertenza:** C1 e' il criterio piu' debole dei sei. 353 agenti lo passano solo grazie
> al terzo pattern, che non verifica affatto l'esistenza di un id: verifica l'esistenza di
> un backtick. Non usare C1 come prova che un agente sia invocabile.

---

### 2.2 C2-ruolo

- **Nome esatto nel codice:** `"C2-ruolo"` — `empire/forge.py:58`
- **Descrizione:** `"una sola responsabilita' dichiarata"`
- **Pattern** (`empire/forge.py:58-59`):
  ```python
  r"##\s*Ruolo"        # scatta per primo in  40 agenti
  r"\*\*Ruolo\*\*"     # scatta per primo in   0 agenti
  r"^\s*Tipo\s*[:=]"   # scatta per primo in   0 agenti
  r"##\s*Identit[aà]"  # scatta per primo in 383 agenti
  ```
- **Mancante in 16 agenti su 439 (3,6%).** E' il criterio piu' soddisfatto.
- **Testo minimo:** un titolo `## Ruolo` **oppure** `## Identita` / `## Identità`
  (accento facoltativo grazie a `[aà]`). In pratica basta la sezione `## Identità`, che
  e' gia' nel modello standard degli agenti di `company/Ecosistemi`.

---

### 2.3 C3-ingresso

- **Nome esatto nel codice:** `"C3-ingresso"` — `empire/forge.py:60`
- **Descrizione:** `"dice cosa gli serve per lavorare"`
- **Pattern** (`empire/forge.py:60-61`):
  ```python
  r"##\s*Input"      # scatta per primo in 362 agenti
  r"\*\*Input\*\*"   # scatta per primo in   0 agenti
  r"##\s*Ingress"    # scatta per primo in   0 agenti
  r"\bINPUT\s*[:=]"  # scatta per primo in  35 agenti
  ```
- **Mancante in 42 agenti su 439 (9,6%).**
- **Testo minimo:** un titolo che comincia con `## Input` — **e qui sta la chiave del
  paradosso C4**: il titolo diffusissimo `## Input / Output` **soddisfa C3** (perche' dopo
  `##` viene subito `Input`) **e non soddisfa C4** (perche' dopo `##` non viene subito
  `Output`). Un solo titolo, due esiti opposti.

---

### 2.4 C5-successo

- **Nome esatto nel codice:** `"C5-successo"` — `empire/forge.py:65`
- **Descrizione:** `"ha un criterio di riuscita o un gate"`
- **Pattern** (`empire/forge.py:65-68`):
  ```python
  r"##\s*(Gate|Criteri|Successo|Definition of Done|DoD|Verifica|QA)"  #  51 agenti
  r"\bgate\b"                                                          # 216 agenti
  r"\bcriteri[oi] di (successo|riuscita)"                              #   0 agenti
  r"\bDoD\b"                                                           #   2 agenti
  r"\bsoglia\b"                                                        #  34 agenti
  r"\bthreshold\b"                                                     #   1 agente
  ```
- **Mancante in 135 agenti su 439 (30,8%).** E' il **secondo** collo di bottiglia dopo C4.
- **Testo minimo:** una sezione `## Gate` / `## Criteri` / `## Verifica` / `## QA`, **oppure**
  — ed e' cosi' che passano 216 agenti su 304 — **la sola parola `gate` scritta una volta
  in tutto il file**, anche in una frase di prosa ("passa il gate di AG-A1-QA"). Anche
  `soglia` da sola basta.

> **Avvertenza:** come C1, anche C5 e' quasi sempre soddisfatto per accidente lessicale, non
> perche' l'agente dichiari davvero un criterio di riuscita. Chi progettera' l'ondata C5 non
> deve fidarsi del 30,8%: il numero di agenti **senza un vero criterio di successo** e'
> molto piu' alto.

---

### 2.5 C6-comportamento

- **Nome esatto nel codice:** `"C6-comportamento"` — `empire/forge.py:69`
- **Descrizione:** `"ha istruzioni operative eseguibili, non solo descrittive"`
- **Pattern** (`empire/forge.py:69-72`):
  ```python
  r"##\s*(Prompt|Procedura|Algoritmo|Come lavora|Passi|Step|Esecuzione|Regole ferree)"  #   0
  r"```(bash|python|yaml|json|sh)"                                                       # 345
  r"^\s*\d+\.\s+\*\*[A-Z]"                                                               #  21
  r"\bSTEP \d"                                                                           #   4
  r"\bstate machine\b"                                                                   #   0
  ```
- **Mancante in 69 agenti su 439 (15,7%).**
- **Testo minimo:** in pratica **un blocco di codice recintato con linguaggio dichiarato**
  — ` ```json `, ` ```bash `, ` ```python `, ` ```yaml `, ` ```sh ` — che e' cio' che fa
  passare 345 agenti su 370. In alternativa una lista numerata i cui elementi iniziano con
  grassetto maiuscolo (`1. **Profilazione nicchia nuova** — ...`).

> **Avvertenza:** la docstring di `forge.py:39` dichiara *"C6 e' il piu' importante e il piu'
> assente"*. **Non e' piu' vero.** Alla misura di oggi C6 manca in 69 agenti e C4 in 314.
> Il documento di progetto e' rimasto indietro rispetto ai fatti: il collo di bottiglia si
> e' spostato su C4.

---

### 2.6 C4-USCITA — LA SPECIFICA SU CUI SI BASANO 314 RISCRITTURE

Questa e' la parte che non si puo' sbagliare. La riporto per esteso.

**Nome esatto nel codice:** `"C4-uscita"` — `empire/forge.py:62`
**Descrizione:** `"dice cosa produce e dove"`
**Codice sorgente integrale, `empire/forge.py:62-64`:**

```python
62      "C4-uscita": ("dice cosa produce e dove", [
63          r"##\s*Output", r"\*\*Output\*\*", r"##\s*Uscit", r"\bOUTPUT\s*[:=]",
64          r"##\s*Artefatt"]),
```

Valutati con `re.IGNORECASE | re.MULTILINE`, in quest'ordine, primo che scatta vince.

#### Le cinque porte, una per una

| # | pattern | cosa accetta davvero | quanti agenti entrano da qui |
|---|---|---|---|
| 0 | `##\s*Output` | la sequenza letterale `##` seguita da soli spazi/a-capo e poi da `Output`. Non ancorata: vale dentro `###`, `####`. Vale `## output`, `##Output`, `## OUTPUT`. | **40** |
| 1 | `\*\*Output\*\*` | esattamente `**Output**` in grassetto, **niente fra la parola e le due stelline di chiusura**. | **7** |
| 2 | `##\s*Uscit` | `## Uscita`, `## Uscite`, `## Uscita prodotta`. | **0** |
| 3 | `\bOUTPUT\s*[:=]` | la parola `output` a confine di parola, seguita da spazi facoltativi e poi da `:` **oppure** `=`. Vale ovunque, anche dentro un blocco JSON (`"output": {...}`). | **78** |
| 4 | `##\s*Artefatt` | `## Artefatti`, `## Artefatto`. | **0** |

Totale che passa: 40+7+0+78+0 = **125**. Mancante: **314**.

#### Cosa NON basta (le trappole verificate sui 314 falliti)

Ho aperto tutti e 314 i file che falliscono e misurato che cosa contengono davvero:

| forma presente nel file | quanti dei 314 | perche' fallisce comunque |
|---|---|---|
| titolo `## Input / Output` | **274** | dopo `##` viene `Input`, non `Output`. Il pattern 0 pretende `Output` **subito** dopo `##\s*`. |
| grassetto `**Output prodotto:**` | **228** | il pattern 1 pretende `**` **immediatamente** dopo `Output`; il pattern 3 pretende `:` o `=` **immediatamente** dopo `Output`. La parola `prodotto` in mezzo li rompe entrambi. |
| riga di tabella `\| Output \| ... \|` | 36 | dopo `Output` c'e' uno spazio e una pipe, non `:` ne' `=`. |
| verbo `produce` / `produrre` | 216 | nessun pattern cerca verbi. |
| verbo `scrive in ...` | 170 | idem. |
| parola `consegna` | 103 | idem. |
| `deliverable` | 26 | idem. |
| la parola `output` compare almeno una volta | **304 su 314** | ma mai nella forma richiesta. |
| la parola `output` **non compare affatto** | **10** | questi sono gli unici veri muti. |

**Il fatto centrale del censimento:** dei 314 agenti che "non dichiarano cosa producono",
**274 lo dichiarano eccome** — sotto il titolo combinato `## Input / Output`, con una sezione
`**Output prodotto:**` che contiene lo schema JSON di quello che esce e spesso anche il
`namespace` dove finisce. Prova, `company/Ecosistemi/01-AGENCY/Reparti/A1-Ricerca/Agenti/ag-a1-icp.md:45-69`:

```markdown
## Input / Output

**Input atteso:**
```json
{ "nicchia": "ristorazione-roma", ... }
```

**Output prodotto:**
```json
{
  "icp_id": "ICP-ristorazione-roma",
  ...
  "namespace": "agency/a1/icp/ristorazione-roma"
}
```
```

Questo agente **dice cosa produce e dove**, cioe' soddisfa la descrizione umana di C4 alla
lettera, e la macchina lo conta fra i 314 rotti. Non e' un agente da riscrivere: e' un
titolo da spezzare.

#### LA REGOLA C4, PRONTA DA APPLICARE

Perche' un file di agente risulti **presente su C4-uscita**, deve contenere, come riga
autonoma, un titolo markdown di livello 2 o superiore che comincia con la parola `Output`:

```markdown
## Output
```

Sono ugualmente validi, in ordine di preferenza:

1. `## Output` — **forma canonica: e' questa che va usata nelle 314 riscritture.**
2. `## Output prodotto` — valido (il pattern 0 guarda solo cio' che segue `##`, non cio' che
   segue `Output`).
3. `## Uscita` / `## Uscite` / `## Artefatti` — validi, sconsigliati (nessuno li usa oggi:
   0 agenti su 439, quindi non c'e' precedente da imitare).
4. `**Output**` in grassetto senza nient'altro fra le stelline — valido ma fragile:
   aggiungere una sola parola (`**Output prodotto**`) lo rompe.
5. `Output:` in mezzo a una riga qualsiasi — valido ma **da non usare**: e' la porta da cui
   passano oggi 78 agenti spesso per caso, perche' la stringa `"output":` dentro un esempio
   JSON basta a soddisfarla. Fa passare il criterio senza che l'agente dichiari niente.

**Sono INVALIDI, e sono esattamente gli errori gia' commessi 274 e 228 volte:**

- `## Input / Output` — invalido su C4 (valido su C3).
- `## Input e Output`, `## I/O`, `## Ingresso / Uscita` — invalidi.
- `**Output prodotto:**` — invalido.
- `**Output (JSON reale):**`, `**Output strutturato**`, `**Produce output**` — invalidi.
- una riga di tabella `| Output | ... |` — invalida.
- qualunque descrizione in prosa ("produce il profilo ICP e lo scrive in `agency/a1/icp`") —
  invalida, per quanto perfetta sia.

**Forma raccomandata per le riscritture** — soddisfa C3 e C4 insieme, senza perdere niente
di cio' che il file gia' diceva, e mantiene la sostanza richiesta dalla descrizione del
criterio ("cosa produce **e dove**"):

```markdown
## Input

**Input atteso:**
```json
{ ... }
```

## Output

**Artefatto prodotto:** <nome del file o della chiave>
**Dove finisce:** <percorso su disco o namespace AgentDB>
**Forma:**
```json
{ ... }
```
```

**Verifica di una singola riscrittura, comando esatto:**

```
python -m empire forge agente <id-agente>
```

(`empire/forge.py:267-281`) stampa i sei criteri con `OK` / `NO` e la stringa esatta che ha
fatto scattare ognuno (`prova:`). E' il collaudo per riscrittura, e costa un secondo.

---

## SEZIONE 3 — LA MAPPA DELLA POPOLAZIONE

### 3.1 Dove vivono gli agenti, contati uno per uno

Tutti i numeri di questa tabella vengono da `os.walk` o da `Path.glob` eseguiti adesso,
non da stime.

| # | posto | file `.md` | lo vede `forge scan`? |
|---|---|---|---|
| 1 | `company/Ecosistemi/**/Agenti/` | **339** | SI |
| 2 | `company/Board-CSuite/*/agenti/` | **70** | SI |
| 3 | `company/Ispettorato/agenti/` | **11** | SI |
| 4 | `DIGITAL-EMPIRE/04-AGENTS/**/` | **12** | SI |
| 5 | `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/` | **7** | SI |
| | *(sottototale perimetro forge, dedotti 4 file di corredo)* | **439** | |
| 6 | `company/Genesi-Core/FORGE/Agenti/` | **10** | **NO** |
| 7 | `company/Genesi-Core/ARCHITETTURA/Agenti/` | **8** | **NO** |
| 8 | `company/MAXIMILIAN/Agenti/` | **8** | **NO** |
| 9 | `.claude/agents/` (agenti eseguibili di progetto) | **129** | **NO** |
| 10 | `~/.claude/agents/` (agenti eseguibili globali) | **35** | **NO** |
| 11 | altre cartelle `agents/` e `Agenti/` alla radice del repo | **298** | **NO** |
| | **TOTALE FILE-AGENTE NEL REPOSITORY** | **927** | |

Dettaglio della riga 11 (cartelle il cui nome e' esattamente `agents` o `Agenti`, fuori da
`company/`, `.claude/` e `.agents/`; sovrapposizione col perimetro forge verificata = **0**):

```
  118  SKILL & Agenti/...
   63  WORKFLOW-ESTATE/...        (diverse da 03-AGENTI-E-RUOLI)
   61  DIGITAL-EMPIRE/...         (diverse da 04-AGENTS)
   38  second-brain-vault/...
    7  Agenti/
    4  Crea siti/
    3  Workflow-libri/
    2  master-build-architecture/
    1  Agency page/
    1  master-app-builder-skill/
```

**Altri due depositi che non sono agenti e vanno tolti dal ragionamento:**

- `.agents/` — contiene **solo** `AGENTS.md` e `.agents/skills/` con **1872 file `.md` di
  skill**. Zero agenti. Non e' un bacino di popolazione.
- **217 file `.md` annidati sotto una cartella `Agenti/`** in `company/` (cioe' in
  `Agenti/<nome-agente>/system-prompt.md`, `tools.md`, `playbook.md`, `evals.md`…): sono il
  **corredo CF-grade** degli agenti a 7 file. Forge non li vede (il suo pattern e'
  `**/Agenti/*.md`, figli diretti) e fa bene: non sono agenti.

### 3.2 Il perimetro eseguibile — verificato con lo strumento dell'azienda

```
$ python scripts/verify-agents.py
PROGETTO  .claude/agents/        129 agenti
GLOBALE   ~/.claude/agents/       35 agenti
AGENTI: 164  CHECK: 621  FALLITI: 6
  FAIL  [progetto ] conoscenza-empire        non censito in registro-agenti.yaml
  FAIL  [progetto ] tesoreria-conductor      non censito in registro-agenti.yaml
  FAIL  [progetto ] tesoreria-entrate        non censito in registro-agenti.yaml
  FAIL  [progetto ] tesoreria-previsione     non censito in registro-agenti.yaml
  FAIL  [progetto ] tesoreria-report         non censito in registro-agenti.yaml
  FAIL  [progetto ] tesoreria-spese          non censito in registro-agenti.yaml
GATE AGENTI: FAIL

$ python scripts/verify-skills.py
SKILL: 172  CHECK: 860  FALLITI: 2
  FAIL  tesoreria       non registrata in company/skills-map.yaml
  FAIL  ultimo-metro    non registrata in company/skills-map.yaml
GATE SKILL: FAIL
```

**Tutti i numeri dichiarati da EMPERATOR sono confermati** (129 · 35 · 164 · 6 · 172 · 2).
I 6 non censiti sono l'agente `conoscenza-empire` e i 5 del reparto Tesoreria: sono i piu'
recenti, mai iscritti in `company/Backbone/Identity-HR/registro-agenti.yaml`.

### 3.3 La frattura: due popolazioni che non si toccano

**439 agenti misurati da forge (schede in markdown) e 164 agenti eseguibili da Claude Code
sono due insiemi quasi disgiunti.** Misurato: i 439 file portano **416 nomi distinti**, i
`.claude/agents` di progetto ne portano 129, i globali 35. L'intersezione fra il perimetro
forge e il perimetro eseguibile e' di **due nomi soli**: `cf-conductor` e `chief-forge`.
(Il terzo doppione, `cc-master`, e' fra progetto e globale, dentro lo stesso perimetro eseguibile.)

Detto altrimenti: **l'azienda descritta in `company/` e l'azienda che gira non sono la
stessa azienda.** Il lavoro sui 314 contratti C4 migliora la prima. Perche' l'orchestratore
possa concatenare qualcosa, il contratto va portato anche sulla seconda — o le due vanno
ricongiunte. Questo e' un problema di piano, non di questo censimento, ma va scritto qui
perche' nessuno lo scopra a meta' strada.

---

### 3.4 I DUPLICATI DIVERGENTI — le bombe

Metodo: per ognuno dei 629 file-agente dei bacini 1-10 (perimetro forge + `company/` fuori
perimetro + `.claude/agents/` + `~/.claude/agents/`) ho preso il nome del file senza
estensione, minuscolo, e lo `sha256` del contenuto. **593 nomi distinti; 36 nomi compaiono
in piu' di un file; di questi 36, quelli con contenuto identico sono ZERO.**

**Tutti e 36 i doppioni sono divergenti.** Quattro pero' sono falsi allarmi
(`memory`, `playbook`, `system-prompt`, `tools`: nomi generici del corredo CF-grade dentro
`DIGITAL-EMPIRE/04-AGENTS/chief-forge/` e `.../memory-architect/`, non agenti).

# **32 duplicati divergenti veri.**

#### Bomba 1 — 04-MARKETING, 19 agenti in doppia copia (entrambe contate nei 439)

Ogni agente di marketing esiste due volte: una versione **corta** nella radice
dell'ecosistema e una versione **lunga** dentro il reparto. Entrambe stanno nel perimetro
forge, quindi **i 439 contengono 19 doppi conteggi**.

| agente | copia radice ecosistema | copia reparto |
|---|---|---|
| a1-briefing-analyst | `04-MARKETING/Agenti/A1-briefing-analyst.md` (5018 B) | `04-MARKETING/Reparti/L2-1-Copywriting/Agenti/a1-briefing-analyst.md` (5893 B) |
| a2-target-analyst | `…/A2-target-analyst.md` (5089 B) | `…/L2-1-Copywriting/Agenti/a2-target-analyst.md` (6557 B) |
| a3-attention-writer | `…/A3-attention-writer.md` (4883 B) | `…/L2-1-Copywriting/Agenti/a3-attention-writer.md` (6363 B) |
| a4-problem-writer | `…/A4-problem-writer.md` (4841 B) | `…/L2-1-Copywriting/Agenti/a4-problem-writer.md` (6242 B) |
| a5-solution-writer | `…/A5-solution-writer.md` (5039 B) | `…/L2-1-Copywriting/Agenti/a5-solution-writer.md` (6540 B) |
| a6-objections-handler | `…/A6-objections-handler.md` (2713 B) | `…/L2-1-Copywriting/Agenti/a6-objections-handler.md` (6324 B) |
| a7-cta-writer | `…/A7-cta-writer.md` (2597 B) | `…/L2-1-Copywriting/Agenti/a7-cta-writer.md` (6170 B) |
| a8-copy-reviewer | `…/A8-copy-reviewer.md` (2890 B) | `…/L2-1-Copywriting/Agenti/a8-copy-reviewer.md` (6400 B) |
| ad1-audience-analyst | `…/AD1-audience-analyst.md` (2707 B) | `…/L2-2-Advertising/Agenti/ad1-audience-analyst.md` (7364 B) |
| ad2-creative-iterator | `…/AD2-creative-iterator.md` (2693 B) | `…/L2-2-Advertising/Agenti/ad2-creative-iterator.md` (7305 B) |
| ad3-media-buyer | `…/AD3-media-buyer.md` (2935 B) | `…/L2-2-Advertising/Agenti/ad3-media-buyer.md` (7579 B) |
| ad4-compliance-checker | `…/AD4-compliance-checker.md` (2900 B) | `…/L2-2-Advertising/Agenti/ad4-compliance-checker.md` (8016 B) |
| e1-lifecycle-architect | `…/E1-lifecycle-architect.md` (2882 B) | `…/L2-3-Email-Lifecycle/Agenti/e1-lifecycle-architect.md` (7310 B) |
| e2-deliverability-guard | `…/E2-deliverability-guard.md` (2793 B) | `…/L2-3-Email-Lifecycle/Agenti/e2-deliverability-guard.md` (8323 B) |
| e3-segmentation-analyst | `…/E3-segmentation-analyst.md` (2938 B) | `…/L2-3-Email-Lifecycle/Agenti/e3-segmentation-analyst.md` (7579 B) |
| an1-tracking-engineer | `…/AN1-tracking-engineer.md` (2909 B) | `…/L2-4-Analytics/Agenti/an1-tracking-engineer.md` (7826 B) |
| an2-attribution-analyst | `…/AN2-attribution-analyst.md` (2988 B) | `…/L2-4-Analytics/Agenti/an2-attribution-analyst.md` (7623 B) |
| an3-experiment-designer | `…/AN3-experiment-designer.md` (3093 B) | `…/L2-4-Analytics/Agenti/an3-experiment-designer.md` (7514 B) |
| an4-insight-distiller | `…/AN4-insight-distiller.md` (3088 B) | `…/L2-4-Analytics/Agenti/an4-insight-distiller.md` (8021 B) |

**In che cosa divergono** (verificato su `a1-briefing-analyst`): sono due schede scritte con
due modelli diversi. La copia radice apre con `# A1 — Briefing Analyst` e ha una sezione
`## Handoff Contract (I/O concreto)`; la copia reparto ha frontmatter YAML
(`Type: ENTITY / Status: Active / Created: 2026-06-18`), un blockquote `> **ID:** A1 · **Tier:** Sonnet`
e una sezione `## Identità`. **Non e' una copia piu' vecchia: e' un'altra scheda dello stesso
agente.** E danno esiti opposti alla misura:

```
OPERATIVO    10.0  manca: -                            04-MARKETING/Agenti/A1-briefing-analyst.md
PARZIALE      6.7  manca: C4-uscita, C5-successo       …/L2-1-Copywriting/Agenti/a1-briefing-analyst.md

DOCUMENTALE   5.0  manca: C1, C4, C6                   04-MARKETING/Agenti/AD1-audience-analyst.md
PARZIALE      6.7  manca: C4-uscita, C5-successo       …/L2-2-Advertising/Agenti/ad1-audience-analyst.md
```

Nel primo caso e' migliore la copia radice, nel secondo la copia reparto. **Non c'e' una
regola: vanno guardate a coppie.** Riscriverne una e lasciare l'altra significa lasciare in
casa due contratti diversi per lo stesso agente — che e' peggio di zero contratti, perche'
un orchestratore ne leggerebbe uno a caso.

#### Bomba 2 — FORGE, 10 agenti fra `Genesi-Core` e `Ecosistemi/07-FORGE` (una copia INVISIBILE)

| agente | copia CONTATA (`Ecosistemi/07-FORGE/Agenti/`) | copia INVISIBILE (`Genesi-Core/FORGE/Agenti/`) |
|---|---|---|
| frg-chief | 3078 B | 4970 B |
| frg-contradiction-gate | 3113 B | 4397 B |
| frg-eval-runner | 2860 B | 4345 B |
| frg-hr-registrar | 3076 B | 4394 B |
| frg-mkd-forger | 2975 B | 4475 B |
| frg-org-designer | 2722 B | 4698 B |
| frg-prd-architect | 2762 B | 4344 B |
| frg-skill-smith | 2575 B | 4436 B |
| frg-sparc-warden | 3177 B | 4295 B |
| frg-spec-writer | 2582 B | 4521 B |

Questa e' la peggiore delle due bombe, e il motivo e' questo:

```
PARZIALE      6.7  manca: C3-ingresso, C4-uscita   company/Ecosistemi/07-FORGE/Agenti/frg-chief.md
OPERATIVO    10.0  manca: -                        company/Genesi-Core/FORGE/Agenti/frg-chief.md
```

**La copia buona (10/10, tutti e sei i criteri) e' quella che forge NON vede.** Il piano di
riscrittura, se si basa solo sull'elenco di forge, andra' a riscrivere da zero un contratto
che in casa esiste gia', perfetto, in un'altra cartella. Vale per tutti e 10 gli `frg-*` e,
molto probabilmente, per gli 8 `arch-*` e gli 8 `MX-*` che stanno nello stesso limbo.

#### Bomba 3 — i 3 nomi a cavallo fra scheda e agente eseguibile

| agente | copia A | copia B |
|---|---|---|
| `cc-master` | `~/.claude/agents/cc-master.md` (14018 B) | `.claude/agents/cc-master.md` (14013 B) |
| `cf-conductor` | `.claude/agents/cf-conductor.md` (14523 B) | `company/Board-CSuite/Chief-Forge/agenti/cf-conductor.md` (4468 B) |
| `chief-forge` | `.claude/agents/chief-forge.md` (3755 B) | `DIGITAL-EMPIRE/04-AGENTS/chief-forge/chief-forge.md` (749 B) |

`cc-master` e' il caso piu' insidioso: **5 byte di differenza** fra la copia globale e quella
di progetto. Una divergenza da 5 byte non la vede nessuno a occhio, e Claude Code carica
quella di progetto: la globale e' un fantasma che qualcuno prima o poi modifichera' credendo
di modificare l'agente vivo.

### 3.5 Conseguenza sui conteggi del piano

- **439 non e' il numero degli agenti**: e' il numero dei *file* nel perimetro.
  I nomi distinti sono **416** (439 meno 19 doppioni di 04-MARKETING meno 4 nomi generici).
- **Nove di quei 439 file non sono agenti affatto.** Otto sono corredo CF-grade che la lista
  `_CORREDO` di `empire/forge.py:146-147` non copre — `memory.md`, `playbook.md`,
  `system-prompt.md`, `tools.md` dentro `DIGITAL-EMPIRE/04-AGENTS/chief-forge/` e
  `.../memory-architect/` — e sono tutti misurati DOCUMENTALE fra 0.0 e 3.3.
  Il nono e' `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/STATO-AGENTI.md`, misurato 1.7 DOCUMENTALE:
  **e' il report che forge stesso scrive** (`empire/forge.py:220-223`, `salva_report_visibile`).
  Forge conta il proprio referto fra il personale.
  **Agenti veri nel perimetro: 439 − 9 = 430 file, 407 nomi distinti.**
- **314 non e' il numero dei contratti da scrivere**: contiene doppioni e file di corredo.
  Il numero va ricalcolato dopo aver deciso quale copia sopravvive (§5).
- **26 agenti di `company/` non sono mai stati misurati** (Genesi-Core 18 + MAXIMILIAN 8),
  e almeno 10 di essi sono in stato migliore delle copie che invece vengono misurate.

---

## SEZIONE 4 — I MODELLI BUONI

**Esistono, e sono 61.** Non serve ripiegare sui "5 migliori": ci sono 61 agenti che superano
tutti e sei i criteri. Di questi, **31 lo fanno con un vero titolo `## Output`** (porta 0),
4 con `**Output**` (porta 1) e **26 per accidente lessicale** (porta 3, `\bOUTPUT\s*[:=]`, che
scatta anche su `"output":` dentro un blocco JSON).

**Ai modelli si prendono solo i 31 della porta 0.** Gli altri 30 sono OPERATIVO sulla carta ma
non insegnano niente.

Ne riporto cinque, scelti per coprire cinque famiglie diverse. Ognuno e' verificato con
`python -m empire forge agente <id>`, e per ognuno riporto per esteso i pezzi che soddisfano
C3, C4 e C5.

---

### MODELLO 1 — `AGENTE-CLOSER-A8` · **il migliore per C4, da usare come capostipite**

`WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/AGENTE-CLOSER-A8.md` — 134 righe — **10.0/10 OPERATIVO**

```
OK C1 prova: - **ID**:      OK C2 prova: ## Ruolo        OK C3 prova: ## Input
OK C4 prova: ## Output      OK C5 prova: ## Criteri      OK C6 prova: STEP 0
```

**C3-ingresso** — non uno schema astratto: i percorsi veri dei file che gli servono, con la
colonna "obbligatorio", e una guardia scritta sul campo.

```markdown
## Input

| Fonte | Contenuto | Obbligatorio |
|---|---|---|
| `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/lead.csv` | nome, stato relazione, canale, ultimo contatto | sì |
| `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/01_SCRIPT_CHIAMATA_FREDDA_APSOC.md` | struttura della chiamata | sì |
| `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/03_ARGOMENTARIO_OBIEZIONI_ESTESO.md` | risposte alle 4 obiezioni | sì |
| `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/05_FOLLOW_UP_G2_G5.md` | cosa fare se non chiude subito | no |
| `Crea siti/Siti CCM/checkout.config.json` | rail di pagamento attivi e tier | sì |

⚠️ **Guardia sull'input (imparata sul campo, 24/07):** prima di chiamare, verificare che il lead sia
tracciabile a una sorgente reale. Oggi `lead.csv` ha **0/7 riscontri** in `Outreach/**/*.csv`:
`python -m empire flow gate Gate-CONTATTI` lo dichiara. **Chiamare un lead inventato brucia tempo
e credibilità.** Se la guardia segnala, l'agente si ferma e lo dice.
```

**C4-uscita** — **questa e' la forma da copiare in tutte le 314 riscritture.** Tre colonne:
cosa esce, **dove finisce**, e quando esce. Soddisfa alla lettera la descrizione del criterio
("dice cosa produce **e dove**") e non lascia niente all'interpretazione di un orchestratore.

```markdown
## Output

| Artefatto | Destinazione | Sempre? |
|---|---|---|
| Esito chiamata (chiuso / da richiamare / perso + motivo) | `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/lead.csv` | sì |
| Traccia della decisione presa in chiamata | `empire trace scrivi decisione` | se si è concesso o negato qualcosa fuori standard |
| Traccia dell'obiezione non prevista | `empire trace scrivi errore` | se emerge un'obiezione fuori dalle 4 |
| Prestazione (durata, esito, incasso) | `empire trace scrivi prestazione` | sì, a chiamata chiusa |
| Link di pagamento consegnato | il rail attivo da `checkout.config.json` | se chiude |
```

**C5-successo** — gate numerati, con la condizione di verde, la conseguenza del rosso, e una
DoD esplicita a due livelli.

```markdown
## Criteri di successo (gate di uscita)

| # | Criterio | Verde se | Rosso → azione |
|---|---|---|---|
| G1 | Ogni chiamata ha un esito registrato | `lead.csv` aggiornato entro fine giornata | la chiamata non conta come fatta |
| G2 | Nessuna promessa fuori dai termini standard | nessuno sconto oltre "Partenza Anticipata" senza decisione registrata | serve una decisione scritta di Max |
| G3 | Le obiezioni nuove sono registrate | ogni quinta obiezione ha una traccia `errore` | l'argomentario non migliora mai |
| G4 | Il tier di pagamento è stato verificato prima | comando `--check` eseguito | rischio di promettere un pagamento impossibile |

**Definition of Done della singola chiamata:** esito in `lead.csv` + traccia di prestazione scritta.
**DoD dello stream S1:** ≥1 anticipo incassato (Gate-REV).
```

---

### MODELLO 2 — `ag-a8-script` · **il migliore per la forma JSON**

`company/Ecosistemi/01-AGENCY/Reparti/A8-Closing/Agenti/ag-a8-script.md` — 171 righe — **10.0/10**

```
OK C1 prova: `ag-a5-script`   OK C2 prova: ## Ruolo    OK C3 prova: ## Input
OK C4 prova: ## Output        OK C5 prova: ## Gate     OK C6 prova: ```json
```

**C3-ingresso** (righe 41-55) — schema JSON con la provenienza di ogni campo dichiarata
dentro il valore (`"output ag-a5-script (A5)"`, `"da ag-a1-brief (A1)"`): un orchestratore
sa da quale agente prendere ogni pezzo.

```markdown
## Input

```json
{
  "call_id": "CALL-001",
  "call_type": "discovery | closing",
  "lead_id": "LEAD-001",
  "icp": "PMI servizi | agenzia | e-commerce | ...",
  "awareness_level": "unaware | problem-aware | solution-aware | product-aware",
  "prodotto": "Outreach Factory | Content Factory | Second Brain | Engine Room",
  "script_standard": "output ag-a5-script (A5)",
  "problema_quantificato": "da ag-a1-brief (A1)",
  "prove_disponibili": ["riferimenti verificabili dal preventivo A3"]
}
```
```

**C4-uscita** (righe 59-77) — titolo dedicato `## Output` + schema completo di cio' che esce.

```markdown
## Output

```json
{
  "call_id": "CALL-001",
  "script": {
    "apertura": "30-60s, calibrata sull'awareness level, parte dal problema del prospect",
    "riallineamento": "conferma del problema quantificato (A1) — domanda, non affermazione",
    "domande_discovery": ["3-5 domande aperte, mirate al problema"],
    "presentazione_soluzione": "scope del preventivo A3, verbatim, 1 prova per promessa",
    "gestione_obiezioni": "rimando alle risposte a-prova di AG-A8-OBJ",
    "chiusura": "domanda di decisione chiara, senza pressione, con next step e data",
    "uscita_no": "come chiudere bene un NO (porta aperta, follow-up A3)"
  },
  "script_status": "personalizzato",
  "brand_voice_check": "conforme",
  "delta_vs_standard": "elenco delle personalizzazioni applicate allo script A5"
}
```
```

> **Il "dove" qui non e' nel blocco `## Output`**: sta nella tabella `## Chiavi AgentDB` (righe
> 140-149), che dichiara `agency/a8/scripts/{icp}-{prodotto}/` con accesso **RW (owner)**.
> E' una forma valida ma piu' fragile della tabella del Modello 1: il "cosa" e il "dove"
> stanno in due sezioni diverse.

**C5-successo** (righe 128-136) — il gate scritto come elenco di condizioni di blocco, con la
piu' grave marcata.

```markdown
## Gate

AG-A8-QA blocca il dossier se, nel blocco script:

- Lo script **non è conforme Brand Voice** (`brand_voice_check != conforme`).
- Contiene una promessa **senza prova** agganciata e senza `[DM]`.
- Contiene **scarsità artificiale / urgenza fabbricata / pressione** (R4 — bloccante assoluta).
- Cita un prezzo o uno sconto **fuori catalogo** (R5).
- Manca il blocco "uscita NO": una call senza uscita pulita produce loss non registrati.
```

---

### MODELLO 3 — `isp-conductor` · **il piu' compatto (93 righe) e il migliore per C1**

`company/Ispettorato/agenti/isp-conductor.md` — 93 righe — **10.0/10**

```
OK C1 prova: - **ID**:   OK C2 prova: ## Ruolo   OK C3 prova: ## Input
OK C4 prova: ## Output   OK C5 prova: ## Gate    OK C6 prova: 1. **N
```

E' l'unico dei cinque che dichiara l'id in modo esplicito e non per accidente di backtick
(righe 11-13):

```markdown
- **ID**: `isp-conductor`
- **Tier**: `opus`
- **Tipo**: coordinator / orchestratore
```

**C3-ingresso** (righe 36-44) — tabella fonte/contenuto, e ogni riga dice **quale workflow apre**:

```markdown
## Input

| Fonte | Contenuto |
|---|---|
| Trigger "fine run" (ogni reparto/ecosistema) | `run_id`, workflow, esito grezzo → apre `WF-RUN-AUDIT` |
| Trigger "fine giorno" | segnale schedulato → apre `WF-DAILY-AUTOCRITICA` |
| Trigger "errore trovato" (da qualsiasi agente isp-*) | descrizione errore → apre `WF-RECIDIVA-GATE` |
| Trigger "fine ciclo di correzione" | catena di N revisioni di un task → apre `WF-REVISION-STUDY` |
| `ispettorato/telemetry` | stato collezioni run raccolte, per decidere se un audit è pronto |
```

**C4-uscita** (righe 48-55) — due colonne, artefatto e destinazione. **La forma minima
corretta**: quattro righe e il contratto e' chiuso.

```markdown
## Output

| Artefatto | Destinazione |
|---|---|
| Ordine di orchestrazione (chi fa cosa, in che ordine) | agenti `isp-*` assegnati |
| Report firmato (run/daily/escalation) | `isp-liaison-altiranghi` per l'instradamento |
| Verdetto di apertura/chiusura workflow | `ispettorato/state` |
| Escalation RECIDIVA (quando gate ROSSO) | `isp-liaison-altiranghi` → Board/MAXIMILIAN/Max |
```

**C5-successo** (righe 72-84) — quattro gate numerati, ognuno con la regola e la conseguenza:

```markdown
## Gate / comportamento bloccante

Il Conductor è custode dei gate d'organo (ARCHITETTURA §5):

1. **Nessuna run senza run-report.** Non firma la chiusura di un audit finché `isp-report-forger`
   non ha prodotto il report completo nel formato §8. Report parziale = non firmato = run non chiusa.
2. **Recidiva = gate ROSSO bloccante.** Se `isp-recidiva-sentinel` segnala un match col
   REGISTRO-ERRORI, il Conductor NON firma un "verde": blocca il commit della fase e apre
   escalation immediata via `isp-liaison-altiranghi`. Non è un warning.
3. **Zero numeri inventati (Mandato Art.2).** Non firma un report che espone un KPI senza dato:
   deve dire "nessun dato", mai uno zero finto.
4. **Firma = evidenza citata.** Come `AG-A10-COORD`, nessun verdetto senza evidenza. "Sembra a
   posto" non è una firma valida.
```

---

### MODELLO 4 — `ag-a7-qa` · **il migliore per un agente-gate**

`company/Ecosistemi/01-AGENCY/Reparti/A7-Account-Management/Agenti/ag-a7-qa.md` — 169 righe — **10.0/10**

```
OK C1 prova: `revops`    OK C2 prova: ## Ruolo   OK C3 prova: ## Input
OK C4 prova: ## Output   OK C5 prova: ## Gate    OK C6 prova: ```json
```

**C3-ingresso** — l'input **e' un elenco di chiavi di stato**, non di dati inline: e' cosi'
che si scrive l'ingresso di un agente che deve leggere lo stato altrui.

```markdown
## Input

```json
{
  "gate": "milestone | alert_churn | closure_90gg | draft_comunicazione",
  "client_id": "identificativo univoco cliente",
  "state_cliente": "agency/a7/clients/{client_id}",
  "state_health": "agency/a7/health/{client_id}",
  "state_alerts": ["agency/a7/alerts/{alert_id}"],
  "state_touchpoints": "agency/a7/touchpoints/{client_id}",
  "sla_ticket": "agency/a4/sla/{client_id} (sola lettura)"
}
```
```

**C4-uscita** — ogni check dell'esito porta con se' l'**evidenza**, cioe' il puntatore al dato
che giustifica il PASS o il FAIL. Un output che si autocertifica.

```markdown
## Output

```json
{
  "gate": "...",
  "client_id": "...",
  "esito": "PASS | FAIL",
  "check": [
    {"nome": "kam_popolato", "esito": "PASS | FAIL", "evidenza": "agency/a7/clients/{client_id}.kam"},
    {"nome": "milestone_loggate", "esito": "PASS | FAIL", "evidenza": "..."},
    {"nome": "nps_raccolto", "esito": "PASS | FAIL", "evidenza": "..."},
    {"nome": "alert_azione_entro_24h", "esito": "PASS | FAIL", "evidenza": "timestamp"},
    {"nome": "sla_ticket_rispettato", "esito": "PASS | FAIL", "evidenza": "agency/a4/sla/..."},
    {"nome": "no_claim_scoperti", "esito": "PASS | FAIL", "evidenza": "..."}
  ],
  "motivo_fail": "dato mancante o incoerente, con puntatore preciso",
  "azione_richiesta": "chi deve ripristinare cosa",
  "escalation": "nessuna | AG-DIR"
}
```
```

**C5-successo** — quattro gate in tabella, ognuno coi check bloccanti e la conseguenza del FAIL:

```markdown
## Gate / comportamento bloccante

| Gate | Check bloccanti | Su FAIL |
|---|---|---|
| **Milestone** | Milestone loggata e comunicata al cliente; `kam` popolato | Milestone non chiudibile; AG-A7-COORD ripristina |
| **Alert churn** | Alert alzato entro 24h dal segnale; azione correttiva **registrata** in `agency/a7/alerts`; segnale rientrato | Alert resta **aperto**; escalation AG-DIR |
| **Closure 90gg** | `nps` raccolto (mai `[DM]`); milestone tutte completate; `kam` continuo per tutto il ciclo; consenso case study se referral | Closure **bloccata**; ciclo non chiuso |
| **Draft comunicazione** | Nessun claim scoperto; ogni fatto ha fonte nello state; nessun ritardo mascherato | Draft **non inviabile**; rework |

**Regola cardine:** un dato mancante è un FAIL, non un warning. `[DM]` significa "da misurare",
mai "assumiamo che vada bene". Il gate non si bypassa: si risolve.
```

---

### MODELLO 5 — `cfo-spend-approver` · **10/10 che NON va copiato: l'esempio di come si passa per sbaglio**

`company/Board-CSuite/CFO/agenti/cfo-spend-approver.md` — 140 righe — **10.0/10 OPERATIVO**

```
OK C1 prova: `cfo-spend-approver`   OK C2 prova: ## Identità   OK C3 prova: ## Input
OK C4 prova: **Output**             OK C5 prova: Soglia        OK C6 prova: ```json
```

Lo includo perche' insegna piu' degli altri quattro messi insieme. **Il contenuto e'
ottimo**: sotto `## Input / Output` c'e' uno schema di ingresso e uno di uscita completi.

```markdown
## Input / Output

**Input atteso:**
```json
{ "tipo": "approval_request | soglia_check", "run_id": "RUN-YYYYMMDD-NNN",
  "ecosistema": "01-AGENCY | ...", "tier_pianificato": "haiku | sonnet | opus | wasm",
  "costo_stimato": "number", "metodo_stima": "token_count | analogia_run_precedente | stima_manuale",
  "budget_guard_check": "pass | pending", "tier_router_check": "ok | anomalia_segnalata" }
```

**Output prodotto:**
```json
{ "approval_id": "APPR-YYYYMMDD-NNN | null", "approvato": "boolean",
  "motivo_rifiuto": "stima non documentata | budget insufficiente | tier anomalia | sopra soglia | null",
  "costo_approvato": "number", "tier_approvato": "haiku | sonnet | opus | wasm",
  "escalation_conductor": "boolean", "timestamp_approvazione": "ISO8601 | null",
  "validita": "sessione corrente | YYYY-MM-DD (se scade)" }
```
```

**Ma la macchina non vede niente di tutto questo.** Il titolo e' `## Input / Output` (invisibile
a C4, §2.6) e il grassetto e' `**Output prodotto:**` (invisibile a C4). La prova che il forge
ha registrato viene da **riga 94**, dentro l'elenco "come ragiona":

```markdown
6. **Output** — JSON con approval_id (o null se rifiutato), motivo, tier e costo approvati.
```

E la prova di C5 non e' una sezione di gate, ma la parola `Soglia` a **riga 42**, dentro una
frase di prosa:

```markdown
4. **Soglia di approvazione autonoma** — per spese sotto soglia [DM] e su ecosistemi con …
```

**Morale, da portare nel piano:** `10.0/10 OPERATIVO` non significa "contratto scritto".
Su questi due criteri la misura e' generosa. Quando le 314 riscritture saranno fatte e il
punteggio salira', **il collaudo vero non e' il punteggio: e' che il titolo `## Output` esista
e che sotto ci sia scritto dove finisce la roba.**

---

### 4.6 Cosa hanno in comune tutti e cinque (lo scheletro dello standard)

| sezione | presente in | forma che funziona |
|---|---|---|
| `## Ruolo` o `## Identità` | 5/5 | una responsabilita' + un blocco **"Cosa NON fa"** |
| `## Input` | 5/5 | tabella `Fonte / Contenuto / Obbligatorio` **oppure** schema JSON |
| `## Output` | 4/5 (il quinto e' il controesempio) | tabella `Artefatto / Destinazione / Sempre?` **oppure** schema JSON + tabella delle chiavi |
| `## Gate` o `## Criteri di successo` | 5/5 | condizioni numerate con la conseguenza del rosso |
| passi operativi numerati | 5/5 | `## Come ragiona (passo-passo)` con verbi all'indicativo |
| `## Handoff` | 5/5 | chi manda, chi riceve, cosa transita |
| `## Connessioni` | 4/5 | wikilink agli agenti vicini |

---

## SEZIONE 5 — LE TRE CLASSI DI LAVORO

### 5.0 La distribuzione vera del lavoro (misurata, non stimata)

Non conta "quanti sono PARZIALI": conta **quale combinazione di criteri manca**. Ecco la
distribuzione esatta sui 439:

| cosa manca | agenti | che lavoro e' |
|---|---|---|
| **niente** (OPERATIVO) | **61** | zero |
| **solo C4** | **174** | **spezzare un titolo. Una riga.** |
| solo C4 + C5 | 66 | titolo + sezione gate |
| solo C5 | 17 | sezione gate |
| solo C3 + C4 | 14 | due titoli |
| solo C6 | 11 | passi operativi |
| solo C1 + C5 | 11 | id + gate |
| C1+C4+C5+C6 | 10 | riscrittura vera |
| solo C4 + C6 | 9 | titolo + passi |
| C1+C4+C6 | 9 | id + titolo + passi |
| C4+C5+C6 | 7 | riscrittura vera |
| C3+C4+C5 | 5 | tre titoli |
| *(altre 20 combinazioni)* | 45 | miste |

**Il numero che decide tutto il piano: 174 agenti — il 39,6% dell'intera popolazione —
sono a UN SOLO criterio dal 10/10, e quel criterio e' C4.** E di quei 174 la quasi totalita'
ha gia' il contenuto scritto sotto `## Input / Output` (§2.6: 274 dei 314 ce l'hanno).

Non e' un lavoro di scrittura. **E' un lavoro di rinomina.**

---

### 5.1 CLASSE A — i 54 DOCUMENTALI (punteggio ≤ 5.0)

Nove di questi **non sono agenti** e vanno esclusi dal conteggio prima di pianificare:
gli 8 file di corredo di `DIGITAL-EMPIRE/04-AGENTS/` (`memory`, `playbook`, `system-prompt`,
`tools` in due cartelle) e `STATO-AGENTI.md`, che e' il referto scritto da forge stesso
(§3.5). **DOCUMENTALI veri: 45.**

**Famiglia 04-MARKETING — 17 file (la piu' malata dell'impero)**
`company/Ecosistemi/04-MARKETING/Agenti/`

| punteggio | agente | manca |
|---|---|---|
| 3.3 | A6-objections-handler | C1, C4, C5, C6 |
| 3.3 | AD3-media-buyer | C1, C4, C5, C6 |
| 3.3 | AN1-tracking-engineer | C1, C4, C5, C6 |
| 3.3 | AN2-attribution-analyst | C1, C4, C5, C6 |
| 3.3 | AN4-insight-distiller | C1, C4, C5, C6 |
| 3.3 | E1-lifecycle-architect | C1, C4, C5, C6 |
| 3.3 | E3-segmentation-analyst | C1, C4, C5, C6 |
| 3.3 | S1-funnel-strategist | C1, C4, C5, C6 |
| 3.3 | S3-campaign-strategist | C1, C4, C5, C6 |
| 5.0 | A7-cta-writer | C1, C4, C6 |
| 5.0 | A8-copy-reviewer | C1, C4, C6 |
| 5.0 | AD1-audience-analyst | C1, C4, C6 |
| 5.0 | AD4-compliance-checker | C1, C4, C6 |
| 5.0 | AN3-experiment-designer | C1, C4, C6 |
| 5.0 | E2-deliverability-guard | C1, C4, C6 |
| 5.0 | MKT-0-conductor | C1, C4, C6 |
| 5.0 | S2-positioning-strategist | C1, C4, C6 |

**Attenzione: 14 di questi 17 hanno un gemello divergente nel reparto** (§3.4, Bomba 1),
e il gemello sta gia' a 6.7 PARZIALE. **Qui non si riscrive: si sceglie una copia e si
cancella l'altra.** Fare altrimenti significa produrre 17 riscritture che lasciano in casa
17 contratti concorrenti.

**Famiglia 06-PLATFORM — 5 file** · `company/Ecosistemi/06-PLATFORM/Agenti/`
`plt-custodian` (C4,C5,C6) · `plt-deploy-op` (C1,C4,C6) · `plt-seo-tech` (C4,C5,C6) ·
`plt-site-builder` (C3,C4,C5) · `plt-site-copy-merger` (C3,C4,C5) — tutti a 5.0.

**Famiglia 05-MULTI-BUSINESS — 4 file** · tutti a 5.0
`MB-A00-conductor` (C1,C3,C4) · `MB-YT-A01-strategy-coord` (C1,C4,C5) ·
`MB-YT-A07-brief-compiler` (C1,C4,C5) · `MB-YT-A09-opt-coord` (C1,C3,C4).

**Famiglia 02-INFO-BUSINESS — 3 file** · tutti a 5.0, tutti con la stessa mancanza C4,C5,C6
`IB-COMMUNITY-manager` · `IB-EMAIL-sequencer` · `IB-WEBINAR-host`.

**Famiglia 03-CONTENT-FACTORY — 3 file** · tutti a 5.0
`CF-A00-conductor` (C3,C4,C5) · `CF-R2-A02-soul-curator` (C1,C5,C6) ·
`CF-R2-A05-avatar-operator` (C1,C5,C6).

**Famiglia 10-MEMORY — 3 file**
`ME-A00-memory-conductor` 3.3 (C1,C4,C5,C6) · `ME-A00-conductor` 5.0 (C1,C3,C4) ·
`ME-A09-wiki-syncer` 5.0 (C4,C5,C6).
*(Nota: `ME-A00-memory-conductor` e `ME-A00-conductor` sono due conductor nella stessa
cartella — verificare se e' un doppione mascherato da nome diverso.)*

**Famiglia Board / Chief-Forge — 2 file** · `cf-intake-router` e `cf-skill-portfolio`,
5.0, entrambi C3,C4,C5.

**Famiglia 09-OPERATIONS — 1 file** · `ops-director` 5.0 (C4,C5,C6).
E' il **direttore** dell'ecosistema operazioni: e' documentale mentre otto suoi sottoposti
sono PARZIALI. Priorita' alta per ragioni di gerarchia, non di punteggio.

**Le persone — 4 file** · `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/`
`AGENTE-MAX` 1.7 (C1,C2,C3,C4,C5) · `AGENTE-CLAUDE` 3.3 (C2,C3,C4,C5) ·
`AGENTE-GAEL` 3.3 (C2,C3,C4,C5) · piu' `STATO-AGENTI` 1.7 che e' il referto, non un agente.
Sono le schede dei soci e dell'assistente: valutarle con lo stesso metro degli agenti
worker e' probabilmente un errore di categoria. **Da decidere se escluderle dal perimetro
invece che riscriverle.**

**Il residuo storico — 12 file** · `DIGITAL-EMPIRE/04-AGENTS/`
`chief-forge` 5.0 · `memory-architect` 3.3 · `PERFORMANCE-CELL` 1.7 · `YT-AGENT-PACK` 5.0,
piu' gli **8 file di corredo a 0.0-3.3 che non sono agenti**. Questa cartella e' l'unica
del perimetro dove non c'e' un solo OPERATIVO e dove il 66% dei file non e' un agente:
**va tolta dal perimetro di forge, non riscritta.**

---

### 5.2 CLASSE B — i 324 PARZIALI, per famiglia

Le famiglie sono le cartelle `Agenti/` reali (reparti degli ecosistemi + uffici del Board).
Per ognuna: quanti PARZIALI, il criterio che manca piu' spesso, e **se in casa esiste gia' un
capostipite OPERATIVO da cui copiare la forma**.

| PARZ | OPER | DOC | famiglia | manca piu' spesso | capostipite in casa |
|---|---|---|---|---|---|
| 10 | 0 | 0 | `01-AGENCY/A2-Acquisizione` | C4:10, C5:2 | — **nessuno** |
| 10 | 0 | 0 | `04-MARKETING/L2-1-Copywriting` | C4:10, C5:2 | — **nessuno** |
| 10 | 0 | 0 | `Board/CEO-Empire-Conductor` | C4:9, C5:4 | — **nessuno** |
| 10 | 0 | 0 | `Board/COO` | C4:10, C5:6 | — **nessuno** |
| 10 | 0 | 0 | `Board/CTO` | C4:8, C5:4 | — **nessuno** |
| 9 | 0 | 3 | `02-INFO-BUSINESS` (radice) | C4:8, C6:5, C3:4 | — **nessuno** |
| 9 | 0 | 0 | `02-INFO-BUSINESS/IB-L2-LANC` | C4:9 | — **nessuno** |
| 9 | 1 | 0 | `02-INFO-BUSINESS/IB-L2-PROD` | C4:9 | `ib-prod-mkd` |
| 9 | 0 | 3 | `03-CONTENT-FACTORY` (radice) | C6:8, C1:4, C5:3 | — **nessuno** |
| 9 | 1 | 0 | `03-CONTENT-FACTORY/CF-R3-Video` | C4:8, C5:7 | `cf-r3-edit` |
| 9 | 1 | 0 | `03-CONTENT-FACTORY/CF-R5-Caroselli` | C4:9, C5:2 | `cf-r5-slidecopy` |
| 9 | 1 | 0 | `07-FORGE` | C5:6, C3:4, C4:1 | `frg-contradiction-gate` |
| 9 | 0 | 3 | `10-MEMORY` | C1:9, C5:6, C4:2 | — **nessuno** |
| 9 | 1 | 0 | `Board/CMO` | C4:9, C5:2 | `cmo-audience-intel` |
| 8 | 1 | 0 | `01-AGENCY/A1-Ricerca` | C4:8 | `ag-a1-qa` |
| 8 | 0 | 0 | `01-AGENCY/A3-Preventivi` | C4:8, C5:1 | — **nessuno** |
| 8 | 1 | 0 | `01-AGENCY/A4-Delivery` | C4:8, C5:5 | `ag-a4-qa` |
| 8 | 0 | 0 | `02-INFO-BUSINESS/IB-L2-COMM` | C4:8, C5:2 | — **nessuno** |
| 8 | 0 | 0 | `02-INFO-BUSINESS/IB-L2-VEND` | C4:8, C5:2 | — **nessuno** |
| 8 | 0 | 0 | `03-CONTENT-FACTORY/CF-R1-Brief` | C4:8, C5:3 | — **nessuno** |
| 8 | 0 | 0 | `03-CONTENT-FACTORY/CF-R6-QA-Gate` | C4:8 | — **nessuno** |
| 8 | 1 | 1 | `09-OPERATIONS` | C5:8, C4:6 | `ops-cost-sentinel` |
| 8 | 0 | 2 | `Board/Chief-Forge` | C3:8, C4:8 | — **nessuno** |
| 7 | 1 | 0 | `03-CONTENT-FACTORY/CF-R4-Testuale` | C4:7, C5:3 | `cf-r4-seo` |
| 7 | 1 | 0 | `03-CONTENT-FACTORY/CF-R7-Pubblicazione` | C4:7, C5:1 | `cf-r7-adapt` |
| 7 | 1 | 0 | `04-MARKETING/L2-2-Advertising` | C4:7, C5:2 | `ad-qa-ads-verifier` |
| 7 | 0 | 0 | `04-MARKETING/L2-3-Email-Lifecycle` | C4:7, C5:3 | — **nessuno** |
| 7 | 0 | 0 | `04-MARKETING/L2-4-Analytics` | C4:7, C5:1 | — **nessuno** |
| 7 | 3 | 0 | `Board/CFO` | C4:5, C5:2 | `cfo-forecast-finance` |
| 6 | 0 | 0 | `01-AGENCY/A5-Copywriting-Interno` | C4:6, C5:1 | — **nessuno** |
| 6 | 0 | 0 | `01-AGENCY/A6-Marketing-Interno` | C4:6, C5:1 | — **nessuno** |
| 6 | 1 | 0 | `03-CONTENT-FACTORY/CF-R0-Director` | C4:6, C5:2 | `cf-d-budget` |
| 6 | 1 | 17 | `04-MARKETING` (radice) | C4:6, C5:3 | `A1-briefing-analyst` |
| 6 | 0 | 4 | `05-MULTI-BUSINESS` | C1:6, C5:3 | — **nessuno** |
| 6 | 0 | 5 | `06-PLATFORM` | C4:5, C3:3, C6:3 | — **nessuno** |
| 6 | 4 | 0 | `Board/CRO` | C5:6, C4:1 | `cro-deal-desk` |
| 5 | 1 | 0 | `01-AGENCY/A10-QA-Cliente` | C6:5 | `ag-a10-uat` |
| 5 | 2 | 0 | `02-INFO-BUSINESS/IB-L2-STRA` | C4:5 | `ib-coord-strategia` |
| 5 | 1 | 0 | `03-CONTENT-FACTORY/CF-R8-Apprendimento` | C4:5 | `cf-r8-hook` |
| 5 | 1 | 0 | `04-MARKETING/L2-5-Brand-Creative` | C4:5, C5:3 | `brand-lead` |
| 5 | 1 | 0 | `04-MARKETING/L2-6-Conversion-Arch.` | C4:5, C5:1 | `ca3-micro-conversion-analyst` |
| 4 | 2 | 0 | `01-AGENCY/A9-Partnership-Referral` | C6:4 | `ag-a9-mgmt` |
| 4 | 2 | 0 | `03-CONTENT-FACTORY/CF-R2-Brand-Kit` | C4:4 | `cf-r2-drift` |
| 4 | 0 | 0 | `08-INTELLIGENCE` | C1:4, C5:2 | — **nessuno** |
| | | | **TOTALE** | **324** | |

**Lettura della tabella:**

- **C4 e' il criterio piu' assente in 33 famiglie su 44.** Non e' un problema di reparto: e'
  un problema di modello di scheda, uguale ovunque.
- **19 famiglie su 44 non hanno un capostipite in casa** (nessun OPERATIVO). Per quelle il
  modello va importato da fuori, dalle famiglie d'oro (§5.3).
- Tre famiglie hanno un problema **diverso** da C4 e vanno trattate a parte:
  `10-MEMORY` (manca C1 in 9 su 9), `05-MULTI-BUSINESS` (C1 in 6 su 6),
  `08-INTELLIGENCE` (C1 in 4 su 4) — qui il buco e' **l'identita'**, non l'uscita;
  e `01-AGENCY/A10-QA-Cliente` + `A9-Partnership` dove manca **C6**, e
  `03-CONTENT-FACTORY` radice dove manca C6 in 8 su 9.
- Le famiglie del **Board** (CEO, COO, CTO: 30 agenti, zero OPERATIVO) sono il blocco
  organizzativo piu' alto e piu' scoperto dell'impero.

---

### 5.3 CLASSE C — le famiglie d'oro, da cui si copia

Quattro famiglie sono **al 100% OPERATIVO**, senza un solo PARZIALE ne' DOCUMENTALE.
**28 agenti che sono gia' lo standard.**

| agenti | famiglia | perche' e' il modello |
|---|---|---|
| **11/11** | `company/Ispettorato/agenti/` | `## Input` e `## Output` in tabella, `## Gate / comportamento bloccante` numerato, `- **ID**:` esplicito. La forma piu' compatta (93 righe). |
| **7/7** | `company/Ecosistemi/01-AGENCY/Reparti/A8-Closing/Agenti/` | schema JSON in ingresso e uscita + `## Gate` come lista di condizioni bloccanti |
| **7/7** | `company/Ecosistemi/01-AGENCY/Reparti/A7-Account-Management/Agenti/` | output con **evidenza per ogni check**, gate in tabella a 3 colonne |
| **3/3** | `company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/Agenti/` | `KDP-GATE`, `KDP-SCOUT`, `KDP-EDITOR` |

A queste si aggiungono i 3 OPERATIVO storici di `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/`
(`AGENTE-CLOSER-A8`, `AGENTE-CRO-COPY-ARCHITECT`, `AGENTE-ANDREI-PASCU-MINER`), fra cui il
**capostipite assoluto per C4** (§4, Modello 1).

**Regola di assegnazione del modello, per famiglia:**
- famiglia con capostipite in casa → si copia la forma del capostipite (25 famiglie);
- famiglia senza capostipite → si copia dall'Ispettorato se e' un organo di controllo,
  da A8-Closing se e' un reparto operativo, da A7-Account se e' un gate (19 famiglie).

---
---

# SINTESI FINALE

## A. VERDETTO SUI DUE CENSIMENTI — tre righe

1. **Ha ragione `forge scan`: 439 e' il numero giusto**, confermato riga per riga
   (`empire/forge.py:150-158` + `empire/loader.py:152-175`), e cosi' tutti gli altri numeri
   di EMPERATOR (61/324/54, C4 mancante in 314, 129 · 35 · 164 · 6 · 172 · 2).
2. **`registry census` mente per un difetto di indentazione**: in `empire/registry/census.py`
   il corpo del ciclo `for fname in filenames:` finisce a riga 189 e tutto il resto (191-240,
   `artifacts.append` compreso) sta nel ciclo esterno — cosi' viene salvato **un solo file per
   cartella**. Prova: artefatti totali = directory visitate = **21682, identici**.
3. **Non contano comunque la stessa cosa**: forge conta le **schede-agente dei cinque percorsi
   di `company/`**; registry census conta **tutti i file del monorepo classificati per tipo**, e
   per costruzione non chiamerebbe mai "agent" ne' gli agenti di `.claude/` (riga 142 → `vendored`)
   ne' quelli del Board (riga 147 → `department`). Fino alla riparazione, `registry census` va
   escluso da ogni conteggio di agenti.

---

## B. LA SPECIFICA C4-USCITA, PRONTA DA APPLICARE

> ### REGOLA C4 — CONTRATTO DI USCITA
>
> **Ogni file di agente deve contenere una riga autonoma che comincia con `## Output`.**
> Il titolo deve essere di livello 2, e la parola `Output` deve seguire immediatamente i
> cancelletti e gli spazi: `## Output`. Sotto quel titolo va dichiarato, per ogni artefatto
> prodotto, **che cosa e'** e **dove finisce** (percorso su disco, chiave AgentDB, o agente
> destinatario).
>
> **Forma obbligatoria — tabella a tre colonne:**
>
> ```markdown
> ## Output
>
> | Artefatto | Destinazione | Sempre? |
> |---|---|---|
> | <cosa esce, in una riga> | <percorso, namespace o agente> | sì / condizione |
> ```
>
> **Forma alternativa ammessa** — schema JSON, **a condizione che** la destinazione sia
> dichiarata dentro lo schema (campo `namespace` / `destinazione`) o in una tabella
> `## Chiavi AgentDB` nello stesso file.
>
> **VIETATO, perche' la misura non lo vede** (errori gia' commessi rispettivamente 274 e 228
> volte nel repository):
> - `## Input / Output` — un titolo unico per due contratti: soddisfa C3 e **fallisce C4**.
>   Va **spezzato** in `## Input` e `## Output`.
> - `**Output prodotto:**` — il grassetto con una parola in mezzo non e' riconosciuto.
>   Il testo puo' restare, ma **sopra ci deve stare il titolo `## Output`**.
> - una riga di tabella `| Output | … |`, il verbo `produce`, `consegna`, `scrive in`:
>   nessuna di queste forme e' riconosciuta.
>
> **Collaudo, uno per uno:** `python -m empire forge agente <id>` deve stampare
> `OK C4-uscita` con `prova: ## Output`. Una `prova:` diversa da `## Output` (per esempio
> `**Output**` o `Output:`) segnala un passaggio accidentale, non un contratto.

**Fondamento nel codice** (`empire/forge.py:62-64`), da citare nel prompt delle riscritture:

```python
"C4-uscita": ("dice cosa produce e dove", [
    r"##\s*Output", r"\*\*Output\*\*", r"##\s*Uscit", r"\bOUTPUT\s*[:=]",
    r"##\s*Artefatt"]),
```

---

## C. LE ONDATE DI LAVORO PROPOSTE

Ogni ondata e' definita da **cosa manca**, non da chi e' l'agente: e' cosi' che il prompt
resta uguale per tutti i file dell'ondata e il lavoro si puo' parallelizzare.
Dopo ogni ondata si rilancia `python -m empire forge scan` e il progresso si vede.

### ONDATA 0 — BONIFICA DEL PERIMETRO · **non tocca nessun agente** · prima di tutto

Senza questa, le ondate 1-4 lavorano su un elenco sporco.

| intervento | quanti file | effetto |
|---|---|---|
| togliere dal perimetro gli 8 file di corredo di `DIGITAL-EMPIRE/04-AGENTS/` (`memory`, `playbook`, `system-prompt`, `tools`) — basta aggiungerli a `_CORREDO`, `empire/forge.py:146-147` | 8 | −8 falsi DOCUMENTALI |
| togliere `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/STATO-AGENTI.md`: **e' il referto che forge stesso scrive** (`empire/forge.py:220-223`) | 1 | −1 falso DOCUMENTALE |
| **decidere una copia** per i 19 doppioni divergenti di 04-MARKETING (§3.4 Bomba 1) | 19 | −19 doppi conteggi |
| **includere nel perimetro** i 26 agenti mai misurati di `company/Genesi-Core/` (18) e `company/MAXIMILIAN/` (8) — fra cui 10 `frg-*` che sono **migliori delle copie oggi contate** | +26 | perimetro vero |
| decidere se `AGENTE-MAX` / `AGENTE-GAEL` / `AGENTE-CLAUDE` sono agenti o schede di persone | 3 | evita 3 riscritture inutili |

**Perimetro dopo la bonifica: ~436 file, tutti agenti veri.**

### ONDATA 1 — **174 agenti** · manca SOLO C4 · *spezzare un titolo*

Il lavoro per agente e' una sostituzione:

```
-  ## Input / Output
+  ## Input
   …blocco input…
+  ## Output
```

Nessun contenuto nuovo da inventare: il contratto d'uscita **e' gia' scritto** sotto
`**Output prodotto:**`. Va solo messo sotto un titolo che la macchina veda, e completato con
la destinazione dove manca.

**Effetto misurato in anticipo: 61 + 174 = 235 OPERATIVO, dal 13,9% al 53,5%.**
E' l'ondata con il rapporto risultato/fatica piu' alto che esista in questo lavoro:
**da sola vale piu' delle altre quattro messe insieme.**

### ONDATA 2 — **66 agenti** · mancano C4 e C5 · *titolo + gate*

Stesso intervento dell'ondata 1, piu' una sezione `## Gate` (o `## Criteri di successo`)
copiata nella forma dal capostipite della famiglia (§5.2, colonna "capostipite") o, se la
famiglia non ne ha, da `isp-conductor` / `ag-a7-qa` (§4).

**Effetto: 235 + 66 = 301 OPERATIVO, 68,6%.**

### ONDATA 3 — **74 agenti** · manca C4 + qualcos'altro (C1, C3, C6 in varie combinazioni)

Le combinazioni piu' frequenti: C3+C4 (14), C1+C4+C5+C6 (10), C4+C6 (9), C1+C4+C6 (9),
C4+C5+C6 (7), C3+C4+C5 (5). Qui la scheda va davvero rimessa in forma sullo scheletro di §4.6.
Concentrati in `04-MARKETING` (radice), `06-PLATFORM`, `05-MULTI-BUSINESS`, `Board/Chief-Forge`.

**Effetto: 301 + 74 = 375 OPERATIVO, 85,4%.**

### ONDATA 4 — **64 agenti** · hanno C4, manca altro

17 solo C5 · 11 solo C6 · 11 C1+C5 · 25 altre combinazioni.
Tre famiglie intere hanno un buco di **identita'** e non di uscita, e vanno trattate insieme:
`10-MEMORY` (C1 in 9 su 9), `05-MULTI-BUSINESS` (C1 in 6 su 6), `08-INTELLIGENCE` (C1 in 4 su 4):
l'intervento e' aggiungere `- **ID**: \`<nome-file>\`` in testa, come fa l'Ispettorato.

**Effetto: 439 OPERATIVO, 100%.**

### Riepilogo delle ondate

| ondata | agenti | intervento | OPERATIVO dopo | % |
|---|---|---|---|---|
| 0 — bonifica perimetro | 0 (57 file toccati) | escludere, deduplicare, includere | 61 | 13,9% |
| **1 — solo C4** | **174** | **spezzare `## Input / Output`** | **235** | **53,5%** |
| 2 — C4 + C5 | 66 | titolo + sezione gate | 301 | 68,6% |
| 3 — C4 + altro | 74 | rimessa in forma sullo scheletro §4.6 | 375 | 85,4% |
| 4 — senza C4 | 64 | id, gate, passi operativi | 439 | 100% |

### Due avvertenze da portare nel piano

1. **Il punteggio non e' il contratto.** `cfo-spend-approver` e' 10/10 con la prova C4 presa
   da un bullet in mezzo alla prosa (§4, Modello 5), e 26 dei 61 OPERATIVO passano C4 dalla
   porta accidentale `\bOUTPUT\s*[:=]`. Il collaudo di ogni riscrittura deve verificare che la
   `prova:` stampata sia esattamente `## Output` — non basta guardare salire il numero.
2. **Le due popolazioni.** I 439 agenti-scheda di `company/` e i 164 agenti eseguibili di
   `.claude/agents/` si toccano in **due nomi soli** (§3.3). Portare i 439 al 100% non rende
   concatenabile un solo agente che gira davvero. Il contratto C4 va portato **anche** nei 164,
   o le due anagrafi vanno ricongiunte: e' una decisione di piano che va presa **prima**
   dell'ondata 1, non dopo.

---

*Fine del censimento 03a. Prodotto da un doom bot al servizio di EMPERATOR, 2026-09-06.
Nessun file del repository e' stato modificato all'infuori di questo.*
