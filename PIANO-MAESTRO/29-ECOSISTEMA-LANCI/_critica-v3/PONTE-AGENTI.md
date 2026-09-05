# PONTE-AGENTI — uno script può invocare un agente?

## 1. RISPOSTA IN UNA RIGA

PARZIALE: il ponte ufficiale (`claude -p --agent <nome>`) esiste, è installato e funzionante sulla macchina ma **non è usato da nessuno script Python del repo**; l'unico meccanismo che uno script Python usa DAVVERO per "eseguire un file agente" (`conductor_auto.py` di YOUTUBE-AUTOMATION-FACTORY) chiama l'API Anthropic grezza con il testo del file come prompt — non invoca un agente `.claude/agents/*.md` nel senso di Claude Code (niente Task tool, niente strumenti nativi, niente permessi) e in più legge da una libreria di prompt propria, diversa da `.claude/agents/`.

## 2. LE PROVE

**Il comando `claude` esiste ed è funzionante:**
```
$ which claude
/c/Users/Utente/.local/bin/claude
$ claude --version
2.1.39 (Claude Code)
$ claude --help
...
--agent <agent>                Agent for the current session. Overrides the 'agent' setting.
--agents <json>                JSON object defining custom agents (e.g. '{"reviewer": {...}}')
-p, --print                    Print response and exit (useful for pipes)
--output-format <format>       "text" (default), "json" (single result), "stream-json"
```
Verificato eseguendo davvero il comando (non da documentazione). Il flag `--agent` seleziona un agente per la sessione, `-p` la rende non interattiva, `--output-format json` dà output strutturato: questo è il meccanismo ufficiale che, in teoria, permetterebbe a uno script di chiamare `subprocess.run(["claude", "-p", "--agent", "ytf-conductor", "prompt", "--output-format", "json"])` e leggere l'output.

**Nessuno script del repo usa questo meccanismo.**
Grep mirata `claude.{0,15}(-p|--print|--agent)` su `*.py, *.mjs, *.js, *.ps1, *.sh` in tutto il repo: 0 script applicativi lo fanno. L'unica occorrenza di "claude -p" è testo di documentazione vendorizzata (non codice eseguito):
- `.claude/skills/content-forge2.0/references/external/skill-creator.md:388,407` — prosa che spiega come Claude Code stesso userebbe `claude -p` per un'altra skill, non codice del repo di Digital Empire.

**Meccanismo realmente funzionante trovato — ma NON punta a `.claude/agents/`:**
`C:\Users\Utente\Desktop\qui tutto\Digital Empire\YOUTUBE-AUTOMATION-FACTORY\02-AUTOMAZIONI-E-SCRIPTS\conductor_auto.py`
- righe 77-83, funzione `read_agent_prompt(agent_filename)`: legge un file `.md` come testo grezzo da `AGENTS_DIR = BASE_DIR / "03-AGENTI-E-RUOLI" / "operatori"` (riga 15).
- righe 38-75, funzione `call_llm(prompt, context)`: se `ANTHROPIC_API_KEY` è settata (riga 55), fa:
```python
url = "https://api.anthropic.com/v1/messages"
headers = {"x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"}
data = {"model": "claude-3-5-sonnet-20240620", "max_tokens": 4000, "messages": [{"role": "user", "content": full_prompt}]}
response = requests.post(url, headers=headers, json=data)
```
- righe 108-114, `phases` list: mappa fasi a nomi di file come `"niche-scout.md"`, `"script-writer.md"` — questi file esistono davvero in `YOUTUBE-AUTOMATION-FACTORY/03-AGENTI-E-RUOLI/operatori/` (verificato via find), MA sono file DIVERSI dai corrispondenti `.claude/agents/ytf-niche-scout.md`, `.claude/agents/ytf-script-writer.md` che esistono in parallelo con contenuto e formato diverso (frontmatter YAML `name/description/model` per Claude Code, vedi sotto).
- Questo è quindi un vero mittente HTTP verso l'API Claude reale, ma legge il proprio archivio di prompt (`03-AGENTI-E-RUOLI/operatori/`), non `.claude/agents/`.

**Meccanismo generico compatibile col formato `.claude/agents/*.md` — ma orfano:**
`C:\Users\Utente\Desktop\qui tutto\Digital Empire\empire\parser.py` righe 55-81 (`parse_hybrid_agent_file`): legge frontmatter YAML (`name`, `model`, `tools`, `description`) + corpo markdown come `system_prompt`. Confrontato riga per riga col vero file `.claude/agents/ytf-conductor.md` righe 1-5:
```
---
name: ytf-conductor
description: "Conductor di YouTube Automation Factory. ..."
model: sonnet
---
```
→ il formato COMBACIA esattamente: questo parser leggerebbe un file `.claude/agents/*.md` senza errori.

`C:\Users\Utente\Desktop\qui tutto\Digital Empire\empire\core\runner.py` righe 14, 58-59, 148-238 (`AgentRunner`): usa il vero SDK `from anthropic import APIError, AsyncAnthropic`, righe 175-181 chiama `self.client.messages.stream(model=self.model, system=self.system_prompt, messages=..., tools=...)`, con loop reale di tool-use (righe 199-234, dispatch di `tool_use` blocks su un `ToolRegistry` proprio). Questo È un vero harness agentic Claude, generico, non un mock.

Ma tre prove che è **scollegato/orfano**, non un ponte già in uso:
1. `empire/config.py` riga 88: `agents_dir: Path = field(default_factory=lambda: Path.cwd() / "agents")` — la directory di default NON è `.claude/agents`; nessun punto del codice la ripunta lì.
2. `empire/requirements.txt` (righe 1-11): elenca **solo** `pyyaml>=6.0` come dipendenza dichiarata; il pacchetto `anthropic` (necessario a `runner.py`) non è dichiarato — segno che questo modulo non fa parte del set testato/mantenuto del progetto "empire".
3. Nessun sottocomando in `empire/cli.py` (righe 115-183, lista completa dei comandi registrati: `status, paths, links, art8, adr001, conform, doctor` + plugin `loader_cli, index_cli, flow.cli, memory.cli, inspect.cli, registry.cli, dash.cli`) invoca `AgentRunner`. Nessun file in `empire/tests/` lo testa (verificato: `grep AgentRunner` in `empire/` trova solo `runner.py`, `kernel.py`, `__init__.py` — nessun test).
4. Bug di compatibilità se qualcuno collegasse davvero i due: `.claude/agents/ytf-conductor.md` ha `model: sonnet` (alias valido SOLO per la CLI `claude --model sonnet`); `empire/parser.py` riga 37 lo passerebbe letteralmente come `model="sonnet"` a `AsyncAnthropic().messages.stream()`, che si aspetta un nome di modello completo dell'API (es. `claude-sonnet-4-5-...`) — la chiamata fallirebbe.

**Il pacchetto `anthropic` è realmente installato sulla macchina:**
```
$ python -c "import anthropic; print(anthropic.__version__); print(anthropic.__file__)"
0.40.0
C:\Users\Utente\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\...\site-packages\anthropic\__init__.py
```
Anche dichiarato in `Agenti\Agency\requirements.txt:1` (`anthropic>=0.40.0`) e `Agenti\Agency\outreach\requirements.txt:18` (`anthropic==0.40.0`) — non ho verificato a fondo se questi due punti del repo lo usano davvero per chiamare Claude (vedi §6).

**`claude_agent_sdk` (Claude Agent SDK) — non trovato:**
Grep mirata `claude_agent_sdk|claude-agent-sdk|ClaudeSDKClient|from claude_code_sdk` su `empire/`, `company/`, `Outreach/`, `YOUTUBE-AUTOMATION-FACTORY/`: 0 risultati reali (unici hit in `Outreach/.../notebooklm/tests/cassettes/*.yaml`, fixture HTTP di un tool CLI di terze parti non correlato).

## 3. I MECCANISMI TROVATI NEL REPO

| Meccanismo | Come funziona | Dove | Stato |
|---|---|---|---|
| `claude` CLI (`-p`, `--agent`, `--agents`, `--output-format json`) | Binario ufficiale Claude Code, invocabile da `subprocess` | Installato sulla macchina (`~/.local/bin/claude`, v2.1.39) | **Esiste e funziona**, ma **nessuno script del repo lo chiama** |
| HTTP diretto a `api.anthropic.com/v1/messages` con testo di file `.md` come prompt | `requests.post`, single-shot, nessun tool-use | `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/conductor_auto.py` righe 38-83 | **Reale e funzionante** (se c'è `ANTHROPIC_API_KEY`), ma legge una libreria di prompt propria (`03-AGENTI-E-RUOLI/operatori/`), non `.claude/agents/` |
| `AgentRunner` + `parse_hybrid_agent_file` (SDK `anthropic`, tool-use loop) | Parser YAML-frontmatter generico compatibile col formato `.claude/agents/*.md` + client `AsyncAnthropic` con loop di tool reale | `empire/core/runner.py`, `empire/parser.py`, `empire/core/loader.py` | **Codice reale**, non mock — ma **orfano**: non punta a `.claude/agents`, non nei requirements dichiarati, non wired a nessun comando CLI, non testato, e romperebbe su `model: sonnet` |
| `empire/loader.py` (top-level) — `load_agents()` | Scansiona l'intero monorepo, estrae SOLO metadati (id, nome, path, ecosistema) da >200 file agente in 4 formati campionati | `empire/loader.py`, testato da `empire/tests/test_loader.py` (righe 166-196: verifica >200 agenti, nessun path duplicato) | **Reale e testato**, ma è un CATALOGO statico — non chiama nessuna AI, non esegue nulla |
| APEX-7 nativo (`Planner/Writer/Analyst/Critic/Refiner/MetaAgent`) con `LocalMockBackend` / `LLMBackend` | Classi Python proprie (non leggono `.claude/agents/*.md`); backend default = mock deterministico offline; backend "reale" opzionale = client OpenAI-compatible (`pip install openai`) | `empire/intelligence/apex7/*.py`, `company/Ecosistemi/11-APEX-7-CORE/agents/*.py` | **Default = SIMULATO** (`LocalMockBackend`, righe 43-75 di `backends.py`, testo deterministico dipendente solo da keyword). L'opzione reale (`LLMBackend`) chiama **OpenAI-compatible**, non Anthropic |
| `RufloOrchestrator` (adapter Rust) | Interfaccia + adapter che solleva esplicitamente `NotImplementedError` se non collegato a un binding pyo3 mai scritto | `empire/intelligence/apex7/ruflo_adapter.py` righe 25-38 | **Onestamente dichiarato come NON collegato** — non è codice che finge, dice apertamente "serve il binding Rust" |
| "RuFLO Core" Python-puro (event bus, priority queue, router) | Dichiarato nel proprio docstring: *"Simula l'architettura ruvnet/ruflo con performance Python"* (riga 3) | `company/Ecosistemi/11-APEX-7-CORE/orchestrator/ruflo_core.py` | **Simulazione dichiarata**, nessuna chiamata AI — esegue `agent.execute()` su agenti Python deterministici (es. `planner.py`: intent detection per keyword-matching, righe 69-80) |
| Orchestration-layer (FastAPI, Postgres, task graph) | Agenti come `SummarizerAgent`, `code_review.py` sono euristiche Python pure (regex, conteggio parole, ricerca stringa "TODO/FIXME") | `company/Ecosistemi/11-APEX-7-CORE/orchestration-layer/src/orchestrator/agents/*.py` | **Zero chiamate AI** in tutta la cartella (grep "anthropic" → 0 risultati) |
| Outreach 6-team | Sistema multi-agente reale e in produzione, ma su NVIDIA Nemotron via OpenRouter | `Outreach/Outreach Workflow/agents/orchestrator.py` riga 54 (`config["OPENROUTER_API_KEY"]`) | **Reale, funzionante, ma non è Claude** |

Nessuno di questi meccanismi (tranne la CLI `claude`, mai usata) invoca un agente `.claude/agents/*.md` nel senso pieno di Claude Code: nessuno passa dal Task tool, nessuno eredita gli strumenti nativi (Read/Edit/Bash/Grep/ecc.) né la gerarchia di permessi che un vero subagente Claude Code ha quando lanciato da dentro una sessione Claude Code.

## 4. IL COSTO DI OGNI MECCANISMO

- **`claude -p`**: nessun documento nel repo (nelle cartelle ispezionate) quantifica un costo per chiamata specifico a questo meccanismo. Consumerebbe crediti/quota dell'abbonamento o della API key associata all'installazione Claude Code su questa macchina — non trovato un numero interno.
- **HTTP diretto `api.anthropic.com` (`conductor_auto.py`)**: usa `model: claude-3-5-sonnet-20240620`, `max_tokens: 4000` per chiamata (riga 64) — nessuna tabella di prezzo €/$ per token trovata nel repo per questo script specifico.
- **`empire/core/runner.py`**: nessun costo documentato (per giunta mai eseguito, essendo orfano).
- **Outreach 6-team**: unico costo esplicitamente documentato nel codice stesso — riga 12 e 327 di `orchestrator.py`: *"Costo: $0/giorno — tutto NVIDIA Nemotron via OpenRouter (gratuito)"*. Questo però è un LLM diverso da Claude.
- Non ho trovato, nelle cartelle ispezionate, un documento interno con €/token o $/milione-token specifico per Claude Sonnet/Opus dentro Digital Empire. Esistono agenti dichiarati nella lista di sistema (`cfo-empire`, `sentinel-cost`) il cui ruolo parla di "budget-guard" e "3-tier routing Haiku/Sonnet/Opus", ma non ne ho letto il contenuto per restare dentro il perimetro della missione — se esiste un numero, è lì o nei dossier PIANO-MAESTRO non ancora aperti (vedi §6).

## 5. COSA SI PUO' FARE OGGI, REALMENTE

Dal più solido al più fragile:

1. **`subprocess.run(["claude", "-p", "--agent", "<nome-agente-in-.claude/agents>", "<prompt>", "--output-format", "json"])`** — il meccanismo ufficiale. Esiste, è installato, è documentato da `claude --help` eseguito davvero su questa macchina. Non è mai stato usato nel repo per questo scopo, quindi andrebbe scritto e testato da zero, ma non c'è nessuna barriera tecnica nota che lo impedisca. Costo: quota/crediti dell'installazione Claude Code esistente.
2. **Chiamata HTTP/SDK diretta all'API Anthropic con il testo del file come prompt** (pattern già collaudato in `conductor_auto.py`, SDK `anthropic` 0.40.0 già installato su questa macchina) — funziona oggi, ma è "leggi il file come istruzioni e falle processare in un singolo turno di chat": si perdono gli strumenti nativi (Read/Edit/Bash/ecc.), i permessi, e tutto ciò che rende un file `.claude/agents/*.md` un "agente Claude Code" e non un semplice prompt.
3. **Completare `empire/core/runner.py` + `empire/parser.py`** puntandoli esplicitamente a `.claude/agents/`: servirebbe (a) aggiungere `anthropic` a `empire/requirements.txt`, (b) tradurre l'alias modello (`sonnet` → id modello reale dell'API), (c) scrivere un sottocomando CLI che li invochi, (d) testarli con una vera chiamata. Oggi è "quasi pronto" ma non collegato — più lavoro del punto 1 o 2, stesso risultato finale (nessun vantaggio evidente rispetto a `claude -p`, che fa la stessa cosa ed è già pronto).
4. **Backend Mock/OpenAI di APEX-7** — funziona, ma di default è simulato e nella modalità "reale" non è nemmeno Claude.
5. **RuFLO (adapter Rust o "core" Python)** — non funziona: l'adapter dichiara esplicitamente `NotImplementedError`, il "core" è una simulazione dichiarata nel proprio docstring.

Per il piano `lancio.py avanza` con 41 agenti in sequenza: l'opzione 1 è l'unica che userebbe DAVVERO i file in `.claude/agents/` con i loro strumenti nativi. Le opzioni 2 e 3 userebbero il *testo* di quei file (o di una copia) come prompt, perdendo il resto dell'infrastruttura Claude Code.

## 6. COSA NON HO POTUTO VERIFICARE

- Non ho letto per intero il codice in `Agenti\Agency\` e `Agenti\Agency\outreach\` (che dichiarano `anthropic>=0.40.0` / `==0.40.0` nei rispettivi `requirements.txt`) per confermare se quella dipendenza viene davvero usata per chiamare Claude o è dichiarata e poi non importata da nessuna parte — resta un'area aperta.
- `company/Ecosistemi/11-APEX-7-CORE/orchestration-layer/src/` contiene 161 file `.py` complessivi; ne ho letti/grep-ati una decina in modo mirato (agents/, non l'intero albero: adapters/, application/, chaos/, governance/, identity/, memory/, observability/, operations/ non tutti ispezionati riga per riga). Non escludo che esista un punto di chiamata AI con un nome di variabile/wrapper che le mie grep ("anthropic", "claude", "subprocess.*claude") non hanno intercettato.
- Non ho eseguito un vero `claude -p --agent <nome> "..."` per osservarne l'output end-to-end: avrebbe consumato crediti/chiamate reali senza un'autorizzazione esplicita di spesa nella missione. Ho verificato solo che il flag esiste ed è documentato da `claude --help` eseguito davvero.
- Non ho aperto il file `.env` alla radice del repo per verificare se `ANTHROPIC_API_KEY` sia presente e valida (policy: non esporre segreti) — quindi non so se, ammesso di avere un ponte funzionante, la chiave sarebbe già pronta o mancante.
- La grep esaustiva su TUTTO il repo per pattern come `subprocess.*claude` è andata in timeout (il repo contiene un clone vendorizzato completo di claude-flow/ruflo sotto `.claude/skills/ruflo/`, `WORKFLOW-ESTATE/.../ruflo-reference/`, `.agents/skills/ruflo/`, `DIGITAL-EMPIRE/05-SKILLS/ruflo/` — centinaia di file `package.json` di un progetto Node/Rust di terze parti, non codice originale di Digital Empire). Ho ristretto la ricerca alle cartelle indicate dalla missione (`company/Ecosistemi/11-APEX-7-CORE`, `empire/`, `Outreach/`, `YOUTUBE-AUTOMATION-FACTORY/`) più `requirements.txt`/`package.json` a livello di repo; non ho scandagliato riga per riga cartelle come `SKILL & Agenti/`, `DIGITAL-EMPIRE/`, `PIANO-MAESTRO/`, `competitor/` che potrebbero contenere altri script isolati.
- Non ho letto il contenuto degli agenti `cfo-empire` / `sentinel-cost` né i dossier PIANO-MAESTRO relativi ai costi API, quindi non so se altrove nel repo esista già una tabella €/token per Claude specificamente.

---

## Cose trovate ma FUORI dal perimetro della missione (non toccate, solo segnalate)

- `Agenti\Agency\requirements.txt` e `Agenti\Agency\outreach\requirements.txt` dichiarano `anthropic` come dipendenza reale — varrebbe la pena controllare se quel codice chiama Claude davvero (vedi §6).
- `empire/core/runner.py` ha un bug di compatibilità sul campo `model` se mai puntato a file con `model: sonnet` (alias CLI, non id API) — non l'ho corretto, solo documentato.
- `empire/requirements.txt` non dichiara `anthropic` pur avendo un modulo (`empire/core/runner.py`) che lo importa — incoerenza da segnalare a chi gestisce quel lotto (Gael/Max secondo le note nei file).
