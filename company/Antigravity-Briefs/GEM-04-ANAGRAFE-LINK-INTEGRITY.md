---
Owner: Max · Controllore: Claude · Origine: FORGE · Governo: MANDATO-EMPIRE.md + ADR-008
Esecutore: GEMINI (Antigravity) · Priorità: P1 · Created: 2026-07-22
Dipendenze: GEM-01 chiuso · Parallelizzabile con GEM-02 · Blocca: nessuno (alimenta GEM-05/06)
---

# GEM-04 — ANAGRAFE D'IMPRESA E INTEGRITÀ DEI COLLEGAMENTI
## Il reparto FORGE che deve impedire gli artefatti orfani, e oggi non lo impedisce

> **LEGGI PRIMA:** `GEM-00`, consegna `GEM-01`. Usa `empire.conform` come motore.

---

## 1. IL PROBLEMA MISURATO

ADR-008 (2026-07-19) stabilisce: **nessun artefatto orfano**. Ogni cosa nel monorepo ha
proprietario + controllore + origine (FORGE) + governo (Mandato), censita in
`company/REGISTRO-IMPRESA.md` e `company/skills-map.yaml`. FORGE è l'ufficio anagrafe.

Realtà sul disco al 2026-07-22:

| Misura | Valore |
|---|---|
| File `.md` in `company/` | 1.267 |
| Righe nel `REGISTRO-IMPRESA.md` | una frazione minima di quel numero |
| Path citati e inesistenti in `WORKFLOW-ESTATE/` | **26** |
| Cartelle-pilastro vuote in `WORKFLOW-ESTATE/` (viola Art.8) | **2** su 6 |
| Riferimenti da `company/` verso `WORKFLOW-ESTATE/` | **1**, ed è un **divieto** nel Mandato |
| Duplicazione `DIGITAL-EMPIRE/` ↔ `WORKFLOW-ESTATE/` | stesso sistema, due copie, nessuna dichiarata canonica |

Casi reali già avvenuti che questo pacchetto deve prevenire:
- **Agent pack orfano eliminato a mano** (CP-20260721-004: `youtube-department/` "non referenziato
  dal core, isolato" — scoperto per caso, non da un controllo).
- **Collisione di ownership**: `EmpireDesk/ui/index.html` modificato in parallelo da Max e Gael,
  8 blocchi in conflitto (CP-20260719-008).
- **Commit mal-etichettato**: "Fase 1 completata" con diff = solo log (CP-20260721-003).

Tutti e tre sono **falle di anagrafe**, non errori di codice. Nessuno sapeva chi possedeva cosa.

**GEM-04 costruisce il censimento automatico + il gate che blocca gli orfani prima che nascano.**

---

## 2. SKILL DA USARE (verifica prima — GEM-00 §2)

| Skill | Path | Uso | Fallback |
|---|---|---|---|
| `github-automation` | `~/.claude/skills/github-automation/` | il gate deve girare su pre-commit / CI, non solo a mano | script `.bat` documentato |
| `verification-quality` | `.claude/skills/verification-quality/` | il gate verifica comportamento (l'orfano viene bloccato?), non forma | §6 |
| `skill-builder` | `.claude/skills/skill-builder/` | per validare la conformità delle skill censite | lettura di `SKILL.md` |
| `agent-reviewer` | `~/.claude/skills/agent-reviewer/` | modello del report di findings | §4.4 |
| `content-forge2.0` | `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0/` | definisce lo standard **CF-grade a 7 file** per un agente: serve a marcare quali agenti sono completi e quali sono solo una scheda | template in `assets/templates/agent/` |
| `sparc-methodology` | `.claude/skills/sparc-methodology/` | SPEC prima del codice | §4 |

**Da leggere prima:** `company/Memory/decisions/ADR-008-catena-intestazione-controllo.md`,
`company/REGISTRO-IMPRESA.md`, `company/skills-map.yaml`,
`company/Mandato/MANDATO-EMPIRE.md` Art.8, `company/Genesi-Core/FORGE/`.

---

## 3. OBIETTIVO

Tre cose, in quest'ordine di importanza:
1. **Censire** — un inventario completo, automatico, rigenerabile di *tutto* ciò che l'azienda possiede.
2. **Diagnosticare** — cosa è orfano, cosa è rotto, cosa è duplicato, cosa viola il Mandato.
3. **Prevenire** — un gate che rifiuta un artefatto nuovo senza intestazione ADR-008.

---

## 4. ARCHITETTURA RICHIESTA

```
empire/registry/
├── __init__.py
├── SPEC.md
├── census.py       # §4.1 scansione totale → inventario
├── orphans.py      # §4.2 rilevamento orfani
├── links.py        # §4.3 integrità dei riferimenti
├── dupes.py        # §4.4 duplicazione tra alberi
├── render.py       # §4.5 rigenera REGISTRO-IMPRESA.md + skills-map.yaml
├── gate.py         # §4.6 il gate bloccante
├── cli.py
└── tests/
```

### 4.1 `census.py`
Scandisce l'intero monorepo (esclusioni: `.git/`, `node_modules/`, `.next/`, `__pycache__/`,
`packaged-final*/`, `phase7-run/`, `phase9-regression/`, `.cache/`) e produce un `Artifact` per
ogni file rilevante, con:
`path` · `kind` (agent|department|ecosystem|workflow|skill|script|doc|template|asset|dashboard) ·
`prov` (i 4 campi ADR-008, `None` se assenti) · `git_last_author` · `git_last_date` ·
`referenced_by: list[Path]` · `references: list[str]` · `size` · `hash` · `cf_grade` (per gli agenti).

`git_last_author`/`git_last_date`: da `git log -1 --format=%an|%aI -- <path>`. **Usa liste di
argomenti**, mai stringhe shell — i path contengono spazi (`qui tutto`, `Digital Empire`).

Output: `empire/.data/census.json`. **Deve completare in < 60 s** su ~9000 file.

### 4.2 `orphans.py` — 4 tipi di orfano, severità diverse
| Tipo | Definizione | Severità |
|---|---|---|
| `no-provenance` | mancano ≥1 dei 4 campi ADR-008 | `warn` se creato prima del 2026-07-19, **`block`** se dopo |
| `unreferenced` | nessun altro file lo cita e non è un entry-point noto | `warn` |
| `unregistered` | non compare in `REGISTRO-IMPRESA.md` né in `skills-map.yaml` | `warn` |
| `dead-end` | cita path che non esistono | **`block`** |

Falsi positivi da escludere esplicitamente (documentali): README, INDEX, template, fixture di
test, asset vendorizzati sotto `05-SKILLS/`/`.agents/skills/` (sono repo di terzi, hanno il loro
governo — censiscili come `vendored`, non come orfani).

### 4.3 `links.py` — riparare i 26
Per ogni riferimento estratto dai `.md`:
1. esiste come path relativo al file che lo cita? → OK
2. esiste come path relativo alla radice del monorepo? → OK, ma segnala `ambiguous`
3. risolve via `empire.paths.resolve_legacy()`? → **`fixable`** + suggerisci il path corretto
4. non risolve → **`dead-end`** (block)

Output atteso su `WORKFLOW-ESTATE/`: almeno 20 finding, la maggior parte `fixable` verso
`DIGITAL-EMPIRE/`. Esempi noti che devono comparire:
```
WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-PERF-LOOP.md  →  00-MEMORY/performances/      [fixable → DIGITAL-EMPIRE/00-MEMORY/performances/]
WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-PERF-LOOP.md  →  04-AGENTS/PERFORMANCE-CELL.md [fixable → DIGITAL-EMPIRE/04-AGENTS/PERFORMANCE-CELL.md]
WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-MASTER.md     →  07-CONTROL/DASHBOARD-E-RETRO.md
```

**`--fix` opzionale e mai automatico**: riscrive i riferimenti `fixable` dentro i `.md`, ma solo
se invocato esplicitamente, e produce prima un diff completo da approvare. Default = solo report.

### 4.4 `dupes.py` — la domanda che nessuno ha ancora posto
`DIGITAL-EMPIRE/` (6702 file) e `WORKFLOW-ESTATE/` (~1180 file reali) contengono lo stesso
sistema. `content-forge2.0` esiste in **almeno 4 copie** (`.agents/skills/`,
`DIGITAL-EMPIRE/05-SKILLS/`, `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/`, radice `content-forge2.0/`).

Confronta per `hash` e produci `empire/.data/duplicates.json` + un report leggibile:
per ogni gruppo di duplicati → path, dimensione totale sprecata, quale copia è più recente,
quale è referenziata da più file (= candidata canonica).

**Non cancellare niente.** Questo è materiale per una decisione di Max (ADR), non un'azione.

### 4.5 `render.py`
Rigenera `company/REGISTRO-IMPRESA.md` **preservando le sezioni scritte a mano**: delimita la
parte generata con marcatori
```
<!-- EMPIRE-CENSUS:BEGIN (rigenerato, non modificare a mano) -->
...
<!-- EMPIRE-CENSUS:END -->
```
e non toccare una riga fuori da quei marcatori. Idem per `skills-map.yaml`.
**Test obbligatorio**: contenuto manuale prima/dopo → identico.

### 4.6 `gate.py` — la prevenzione
```
python -m empire registry gate --staged      # solo i file in git staging
python -m empire registry gate --since HEAD~1
python -m empire registry gate --path <dir>
```
Exit 1 se trova `block`. Messaggio azionabile, con il frontmatter già pronto da incollare:
```
BLOCCATO — company/Ecosistemi/04-MARKETING/Agenti/mk-nuovo.md
  regola: ADR-008 (intestazione mancante: Controllore, Origine)
  aggiungi in testa al file:
    ---
    Owner: <chi>
    Controllore: <chi verifica>
    Origine: FORGE
    Governo: company/Mandato/MANDATO-EMPIRE.md
    ---
```
Usa `github-automation` per documentare l'aggancio a pre-commit. **Non installare l'hook git
senza approvazione di Max** — un pre-commit che blocca è una modifica al flusso di lavoro di
due persone. Documenta, non imporre.

---

## 5. SEQUENZA

**TASK 1 — Ricognizione.** Verifica skill. Leggi ADR-008, REGISTRO-IMPRESA, skills-map, Art.8,
Genesi-Core/FORGE. Campiona 15 file di tipo diverso e censisci a mano quali hanno intestazione.
Output `empire/registry/SPEC.md` con la **tassonomia dei `kind`** e le regole di esclusione
falsi-positivi. **Gate 1**: la SPEC dichiara esplicitamente cosa NON è un orfano e perché.

**TASK 2 — `census.py`.** **Gate 2**: censimento completo < 60 s, conteggio per `kind` coerente
con `find` manuale (incolla i due output affiancati).

**TASK 3 — `orphans.py` + `links.py`.** **Gate 3**: ≥20 link rotti trovati in `WORKFLOW-ESTATE/`,
di cui la maggioranza marcata `fixable` con il path corretto suggerito. Incolla la tabella.

**TASK 4 — `dupes.py`.** **Gate 4**: identifica il gruppo `content-forge2.0` (≥4 copie) e
quantifica lo spazio duplicato in MB. Incolla il report.

**TASK 5 — `render.py`.** **Gate 5**: rigenera `REGISTRO-IMPRESA.md`; `git diff` mostra
**solo** aggiunte dentro i marcatori, zero righe manuali toccate. Incolla il diff.

**TASK 6 — `gate.py`.** **Gate 6**: crea un file di prova senza intestazione, esegui il gate →
exit 1 con messaggio azionabile; aggiungi l'intestazione → exit 0; **cancella il file di prova**.
Incolla entrambi i run.

**TASK 7 — Riparazione Art.8 (i 2 pilastri vuoti).**
`WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/` e `06-DASHBOARD-E-METRICHE/` sono vuote → workflow abusivo.
**Non inventare contenuti.** Popolale con materiale **reale già presente altrove nel repo**,
spostato o linkato:
- `05-TEMPLATES-E-KIT/` ← template di preventivo, email outreach, script di chiamata, kit
  carosello già esistenti (cerca in `Outreach/`, `company/Ecosistemi/01-AGENCY/`, `caroselli/`,
  `DIGITAL-EMPIRE/`). Ogni file portato deve avere intestazione ADR-008 con `Origine:` che dice
  da dove viene.
- `06-DASHBOARD-E-METRICHE/` ← qui va il segnaposto strutturato che **GEM-05 riempirà**:
  `DASHBOARD.md` con lo schema dei KPI e `LISTA-LEAD.md` (esiste già come
  `DIGITAL-EMPIRE/07-CONTROL/LISTA-7-LEAD.md` — portala/collegala).
**Gate 7**: `python -m empire conform --workflow WORKFLOW-ESTATE` → **zero `block` su Art.8**.
Questo è il gate che rende `WORKFLOW-ESTATE/` non più abusivo.

**TASK 8 — Chiusura.** README, checkpoint via GEM-02, consegna GEM-00 §4.

---

## 6. DEFINITION OF DONE

- [ ] DoD-1 — censimento completo di ~9000 file in < 60 s
- [ ] DoD-2 — `REGISTRO-IMPRESA.md` rigenerato con ≥ 500 artefatti censiti, sezioni manuali intatte
- [ ] DoD-3 — ≥ 20 link rotti trovati con path corretto suggerito
- [ ] DoD-4 — duplicati quantificati in MB, gruppo `content-forge2.0` identificato
- [ ] DoD-5 — gate blocca un file senza intestazione (exit 1) e passa con intestazione (exit 0)
- [ ] DoD-6 — messaggio di blocco contiene il frontmatter pronto da incollare
- [ ] DoD-7 — `05-TEMPLATES-E-KIT/` e `06-DASHBOARD-E-METRICHE/` **non più vuote**, con materiale reale
- [ ] DoD-8 — `empire conform --workflow WORKFLOW-ESTATE` → zero `block` su Art.8
- [ ] DoD-9 — zero file cancellati (i duplicati sono **segnalati**, non rimossi) — `git status` incollato
- [ ] DoD-10 — `--fix` dei link produce un diff da approvare, non applica in automatico
- [ ] DoD-11 — pytest ≥ 20 test verdi
- [ ] DoD-12 — hook git **documentato, non installato**

---

## 7. ANTI-PATTERN

| Anti-pattern | Perché rifiutato |
|---|---|
| Cancellare i duplicati | Decide Max con un ADR. `DIGITAL-EMPIRE/` potrebbe essere la fonte canonica. |
| Riscrivere `REGISTRO-IMPRESA.md` da zero | Contiene decisioni scritte a mano. Marcatori, sempre. |
| Marcare orfani i vendored (`05-SKILLS/`, `.agents/skills/`) | Sono repo di terzi con governo proprio. |
| Inventare contenuti per riempire i 2 pilastri vuoti | Materiale finto = pilastro finto. Si sposta roba **reale**. |
| Installare un pre-commit hook senza chiedere | Blocca il lavoro di due persone. Si documenta. |
| `--fix` automatico sui `.md` | ADR-003. Prima il diff, poi l'approvazione. |
| `subprocess` con path interpolati in stringa | Il repo ha spazi ovunque. Liste di argomenti. |

---

## 8. HANDOFF

Alimenta **GEM-05** (Dashboard: la salute anagrafica è un KPI) e **GEM-06** (il workflow engine
rifiuta di eseguire un workflow con link rotti).

A Max, come **decisione da prendere** (non da eseguire da Gemini):
> `DIGITAL-EMPIRE/` e `WORKFLOW-ESTATE/` sono due copie dello stesso sistema estate. Il report
> `dupes` quantifica l'overlap. **Quale è canonica? L'altra si archivia, si cancella o si
> collega?** Serve un ADR. Finché non c'è, ogni modifica va fatta due volte o va persa.
</content>
