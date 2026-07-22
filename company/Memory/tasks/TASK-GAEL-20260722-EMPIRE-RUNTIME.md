---
Owner: Max (committente) · Esecutore: GAEL · Controllore: Claude (gate 5-bis)
Origine: FORGE · Governo: MANDATO Art.8 + ADR-003 + ADR-006 + ADR-008
Emesso: 2026-07-22 · Priorità: P0 — supera V2-2 Lotto 4 e ogni altro lavoro in coda
Riferimenti: CP-20260722-005 (audit) · CP-20260722-006 (seed) · company/Antigravity-Briefs/
---

# 🚨 ORDINE MAX — GAEL: costruisci il livello eseguibile dell'azienda

## 0. Perché (leggi, sono 10 righe, ti risparmiano un giorno)

Audit del 2026-07-22 misurato su disco: **`company/` contiene 1.267 file `.md` e 0 file `.py`**.
L'azienda è descritta ma non gira. `company/Ispettorato/{telemetry,report,state}/` sono **vuote**:
l'organo che deve misurare le performance non ha mai emesso un report. `WORKFLOW-ESTATE/` aveva
**26 riferimenti a path inesistenti** e 2 pilastri Art.8 vuoti. `memory_manager.py` **crashava**
su Windows.

Claude ha già costruito e testato il **seed** del core runtime: `empire/` (23 test verdi).
**Tu costruisci sopra.** Non ricominci da zero, non riprogetti: estendi ciò che gira già.

Verifica subito che ci sia (se non c'è: `git pull`, il task non è ancora arrivato):
```bash
cd "<radice monorepo>"
python -m empire status          # deve stampare "EMPIRE CORE RUNTIME ... alias rotti 0"
python -m empire conform WORKFLOW-ESTATE
python -m unittest discover -s empire/tests -p "test_*.py"   # 23 test, OK
```

---

## 1. Cosa è già fatto e NON devi rifare

| File | Cosa fa | Stato |
|---|---|---|
| `empire/paths.py` | trova la radice risalendo (zero path assoluti), 44 alias, `resolve_legacy()` che ripara i link rotti **senza toccare i .md** | ✅ testato |
| `empire/config.py` | `empire.toml` + `.env`, segreti mai stampati | ✅ |
| `empire/schema.py` | `Agent · Department · Ecosystem · Workflow · Skill · Artifact · Finding · Provenance` | ✅ |
| `empire/conform.py` | `check_art8()` + `check_links()` | ✅ 6 block / 7 riparabili trovati |
| `empire/cli.py` | `python -m empire {status,paths,links,art8,conform,doctor}` + **loop di plugin** | ✅ |
| `empire/empire.toml` | mappa alias → path reali | ✅ |
| `empire.bat` · `pyproject.toml` | launcher da qualunque cartella | ✅ |

**FILE CONGELATI** (fondazione condivisa Max/Gael/Gemini): `paths.py`, `config.py`, `schema.py`,
`conform.py`, `cli.py`, `empire.toml`.
Puoi **estenderli** (nuove funzioni, nuovi campi dataclass, nuovi `check_*`).
**Non** puoi rinominare o cambiare firme esistenti senza scrivere prima una nota
`⚠️ COORDINAMENTO GAEL` in `company/Memory/STATO-EMPIRE.md` e pushare.

**Non devi toccare `cli.py` per aggiungere comandi.** C'è già il loop di plugin: crea il tuo
modulo con una funzione `register(sub)` e viene caricato da solo. Zero conflitti di merge.

```python
# esempio: empire/loader_cli.py
def register(sub):
    p = sub.add_parser("agents", help="elenca gli agenti dell'azienda")
    p.add_argument("--eco"); p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_agents)
```

---

## 2. I TUOI 3 LOTTI (in quest'ordine)

Brief completi con DoD e anti-pattern: `company/Antigravity-Briefs/GEM-01` e `GEM-06`.
Qui c'è l'essenziale. **Leggi i brief prima di partire.**

### 🟣 G-A — `empire/loader.py` + `empire/index.py` (P0, sblocca tutto)

Carica gli artefatti descritti nei `.md` e rendili oggetti interrogabili.

- `load_agents()` → scandisce `company/Ecosistemi/*/Agenti/*.md`,
  `company/Board-CSuite/*/agenti/*.md`, `company/Ispettorato/agenti/*.md`,
  `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/*.md`, `DIGITAL-EMPIRE/04-AGENTS/**/*.md` → `list[Agent]`
- idem `load_ecosystems()`, `load_departments()`, `load_workflows()`, `load_skills()`
- `load_frontmatter()` **tollerante**: la maggior parte dei file NON ha frontmatter → non
  fallire, restituire `{}` e lasciare `Provenance` con campi `None` (è un finding ADR-008 per
  GEM-04, non un crash tuo)
- `cf_grade = True` se accanto alla scheda ci sono i 7 file dello standard content-forge
  (template: `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/assets/templates/agent/`)
- `load_workflows()` deve riempire `Workflow.referenced_paths` (input per GEM-04)
- `index.py`: `build_index()` → `empire/.data/index.json` + `search()` + `stats()`
- CLI via `empire/loader_cli.py` e `empire/index_cli.py`:
  `agents [--eco] [--json]`, `ecosystems`, `workflows`, `skills [--missing]`,
  `index --rebuild`, `find <query>`, `show agent <id>`

**Gate G-A** (incolla gli output nel checkpoint):
1. `python -m empire agents --json` → **> 200** agenti reali con ecosistema corretto
2. load completo **< 10 s** a freddo (tempo misurato)
3. `python -m empire find "watchdog"` trova `ops-watchdog`
4. `index --rebuild` due volte di fila → stesso risultato, zero duplicati
5. i 23 test del seed restano verdi + ≥ 15 test tuoi

**Nota di realtà**: le schede agente hanno formati diversi tra ecosistemi. **Campiona 10 schede
da ecosistemi diversi PRIMA di scrivere il parser** e progetta per la varianza che trovi, non
per quella che ti aspetti.

### 🟣 G-B — fix `memory_manager.py` (piccolo, 30 minuti, ADR-003 wrap)

`WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py` oggi crasha:
```
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f9e0' in position 0
```
- aggiungi `from empire.paths import safe_stdout; safe_stdout()` come **prima istruzione**
- `encoding="utf-8"` in ogni `open()`
- risolvi le sue directory via `empire.paths.resolve()`, non relative al CWD
- **NON cambiare la sua interfaccia CLI né i formati dei record**: altri file la citano
  (ADR-003: si corregge il difetto, non si riscrive)

**Gate G-B**: `python <path>/memory_manager.py status` esce 0 da **3 CWD diversi**. Incolla i tre output.

### 🟣 G-C — `empire/flow/` — workflow engine (GEM-06)

Fa girare `WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/workflows.yaml` con i gate reali.
**Leggi `company/Antigravity-Briefs/GEM-06-WORKFLOW-ENGINE.md` per intero** — c'è tutto:
schema yaml, tipi di gate, coda swarm, DAG, DoD.

Punti che non puoi sbagliare:
- l'engine **non esegue** il lavoro, lo **governa**: stato, gate, assegnazione, registrazione
- un passo `executor: human` **non si chiude mai da solo**. Se Max non conferma, resta aperto e
  va in ritardo — quel ritardo è l'unico segnale utile che oggi manca
- **nessun gate "quasi verde"**: 🟢 o 🔴, regola letterale di `WF-MASTER.md` §3
- gate scaduto senza esito → 🔴 automatico + `on_red` applicato
- **niente `eval()`** su `green_if`: mini-valutatore che accetta solo `<nome> <op> <numero>` e `and`/`or`
- deadline sempre ISO-8601 con timezone, **mai date relative**
- coda: max 1 swarm pesante, ordine `S1 > S2 > S6 > S5`

**Gate G-C**: `flow validate` passa · `flow gates` valuta i 6 gate estate sui dati **reali** di
oggi (alcuni saranno 🔴: **va bene, è la verità**) · un passo con dipendenza aperta non parte ·
`flow done` due volte non duplica.

---

## 3. Perimetro — cosa NON tocchi (anti-collisione con Max/Claude e Gemini)

| Area | Di chi è |
|---|---|
| `empire/memory/**`, `empire/inspect/**` | **Claude** (GEM-02 memoria, GEM-03 Ispettorato) — in costruzione ORA, non entrarci |
| `empire/registry/**`, `empire/dash/**` | **Gemini/Antigravity** (GEM-04, GEM-05) |
| `company/Memory/**` (tranne il TUO checkpoint) | Claude |
| `company/Ispettorato/**` | Claude |
| `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/`, `06-DASHBOARD-E-METRICHE/` | Claude (risanamento Art.8) |
| `company/Ecosistemi/**` | **nessuno li riscrive**: sono specifica approvata. Si leggono. |
| `EmpireDesk/platform/` | Max (grafica) |
| `Clienti/`, `.env`, `second-brain-vault/wiki/` | fuori perimetro |

**Tuo, in esclusiva**: `empire/loader.py`, `empire/loader_cli.py`, `empire/index.py`,
`empire/index_cli.py`, `empire/flow/**`, `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py`.

---

## 4. Regole operative (Mandato + ADR)

1. **Windows-first.** `safe_stdout()` come prima istruzione di ogni entry-point,
   `encoding="utf-8"` in ogni `open()`. Uno script che crasha su Windows non è consegnato.
2. **Zero path assoluti.** Usa `empire.paths`. Il repo si sincronizza su due macchine.
3. **Path con spazi** (`qui tutto`, `Digital Empire`): `pathlib.Path` e liste di argomenti nei
   `subprocess`, mai interpolazione in stringa di shell.
4. **Standard library.** Nessuna dipendenza nuova senza una riga di motivazione.
5. **Idempotenza.** Ogni comando si riesegue senza duplicare nulla. Test esplicito.
6. **Prova, non dichiarazione.** Nel checkpoint incolli **comando + output reale**.
   "Dovrebbe funzionare" = task non chiuso. (Precedente: CP-20260721-003, commit "Fase 1
   completata" con diff = solo log.)
7. **ADR-006 ciclo a 9 passi** per ogni lotto: RECALL → SPEC → PRE-MORTEM → BUILD → GATE →
   REVIEW → TEST → COMMIT → RETRO.
8. **Prima di un build grosso**: blocco `⚠️ COORDINAMENTO GAEL` in `STATO-EMPIRE.md` + push.
9. **Budget-guard**: sotto il 20% di risorse di sessione → chiudi con COMMIT, non aprire lotti nuovi.
10. **Task chiuso → checkpoint** in `company/Memory/checkpoints/CP-20260722-NNN.md`.
    Prendi il primo numero libero: al momento dell'emissione di questo ordine sono usati 001-003.
11. **Item minori → `company/Memory/BACKLOG.md`** (ADR-005), non fermare la costruzione.

---

## 5. Skill da usare (verifica che esistano PRIMA di partire)

```bash
ls "C:/Users/Utente/.claude/skills/" ; ls .claude/skills/ ; ls DIGITAL-EMPIRE/05-SKILLS/
```

| Skill | Uso |
|---|---|
| `sparc-methodology` | SPEC prima del codice, per ogni lotto |
| `agent-architecture` / `agent-coder` / `agent-tester` / `agent-reviewer` | catena di build |
| `verification-quality` | gate comportamentale finale |
| `swarm-orchestration` / `swarm-advanced` | G-A ha 5 loader disgiunti → parallelizzabili |
| `master-build-architecture` | metodo a fasi con gate |
| `content-forge2.0` | standard CF-grade a 7 file (serve a `cf_grade`) e i template `workflow/` per G-C |
| `workflow-automation` | pattern di automazione per G-C |

Se una skill non c'è: **non inventarla**, usa il fallback indicato nel brief e segnalalo.

---

## 6. Definition of Done complessiva

- [ ] `python -m empire agents` elenca > 200 agenti reali, indice < 10 s
- [ ] `python -m empire find` e `show agent` funzionanti
- [ ] `memory_manager.py status` non crasha più, da 3 CWD diversi
- [ ] `flow validate` + `flow gates` girano sui dati reali
- [ ] passo `human` mai auto-chiuso · gate mai "quasi verde" · nessun `eval()`
- [ ] i 23 test del seed restano verdi + ≥ 30 test tuoi
- [ ] `cli.py` **non modificato** (hai usato il loop di plugin)
- [ ] zero file di `company/Ecosistemi/**` modificati (`git status` incollato)
- [ ] checkpoint con comandi e output reali incollati
- [ ] `empire/` registrato: la riga in `REGISTRO-IMPRESA.md` c'è già, aggiungi i tuoi moduli

---

## 7. Ordine di marcia

1. `git pull` → verifica che `empire/` ci sia e che i 23 test passino
2. leggi `GEM-00-INDEX-E-PROTOCOLLO.md` + `GEM-01` + `GEM-06`
3. scrivi il blocco `⚠️ COORDINAMENTO GAEL` in `STATO-EMPIRE.md` + push
4. **G-A** (loader+index) → gate → commit
5. **G-B** (memory_manager) → gate → commit
6. **G-C** (flow engine) → gate → commit
7. checkpoint + RETRO + push

**Se qualcosa non torna** (un formato imprevisto, un contratto ambiguo, una collisione):
**non indovinare**. Scrivi il problema con **comando esatto + errore esatto** in
`STATO-EMPIRE.md` e prosegui sul lotto successivo. Precedente da non ripetere: "Gael ha dei
problemi" senza dettagli → tempo perso a ricostruirli (STATO-EMPIRE, 2026-07-21).
</content>
