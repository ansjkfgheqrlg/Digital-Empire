---
Owner: Max
Controllore: Claude (gate 5-bis)
Origine: FORGE — seed costruito da Claude il 2026-07-22 (CP-20260722-006)
Governo: company/Mandato/MANDATO-EMPIRE.md + ADR-003 + ADR-008
---

# `empire/` — Core Runtime di Digital Empire

**Il livello che mancava.** L'azienda aveva 1.267 file `.md` e **0 file `.py`**: un
organigramma completo, nessun processo. Questo pacchetto rende gli artefatti descritti in
Markdown **interrogabili, validabili e misurabili da codice**.

Non esegue il lavoro. Lo rende osservabile.

## Uso

```bash
# dalla radice del monorepo, oppure da qualunque sottocartella
python -m empire status                    # stato del runtime, alias, moduli
python -m empire paths                     # 44 alias logici -> path reali, con esistenza
python -m empire paths memory_cp
python -m empire art8 WORKFLOW-ESTATE      # i 6 pilastri del Mandato Art.8
python -m empire links WORKFLOW-ESTATE     # riferimenti rotti / riparabili
python -m empire conform WORKFLOW-ESTATE   # art8 + links
python -m empire doctor                    # tutto; exit 1 se ci sono 'block'
```

Ogni comando di lettura accetta `--json`.
Exit code: `0` ok · `1` finding bloccanti · `2` errore interno.

## Cosa fa oggi (seed, 2026-07-22)

| Modulo | Cosa risolve |
|---|---|
| `paths.py` | trova la radice risalendo (**zero path assoluti**), 44 alias logici, e `resolve_legacy()` che **ripara i riferimenti rotti senza toccare i `.md`** (ADR-003) |
| `config.py` | `empire.toml` + `.env`. I segreti non vengono mai stampati né loggati |
| `schema.py` | `Agent · Department · Ecosystem · Workflow · Skill · Artifact · Finding · Provenance` (i 4 campi ADR-008) |
| `conform.py` | `check_art8()` — i 6 pilastri esistono e **non sono vuoti** · `check_links()` — ogni path citato esiste |
| `cli.py` | `python -m empire ...`, con `safe_stdout()` che evita il crash Unicode di Windows |

### Esito reale al 2026-07-22

```
python -m empire conform WORKFLOW-ESTATE
  block: 6   warn: 0   info(riparabili): 7   totale: 13
```
- **2 block Art.8**: `05-TEMPLATES-E-KIT/` e `06-DASHBOARD-E-METRICHE/` vuote → workflow abusivo
- **4 block LINK-DEAD**: `07-CONTROL/LISTA-7-LEAD.md`, `07-CONTROL/AUDIT-PAGINE-20260721.md`, `youtube/`, `andrei-pascu-system/`
- **7 info LINK-FIXABLE**: riferimenti a `00-MEMORY/`, `04-AGENTS/`, `03-WORKFLOWS/`, `02-ARCHITECTURE/` **già riparati a runtime** dal resolver

Le skill vendorizzate (`.agents/`, `04-SKILLS-E-REFERENCE/`) e gli artefatti di run
(`forge-run-*`) sono esclusi: hanno governo proprio. Con `include_vendored=True` i finding
passano da 13 a 746 — rumore, non segnale.

## Cosa NON fa (e chi lo costruisce)

| Modulo | Cosa | Chi | Brief |
|---|---|---|---|
| `loader.py`, `index.py` | carica i 300+ agenti/reparti/workflow dai `.md` → oggetti + indice + ricerca | **Gael** | GEM-01 lotto B |
| `flow/` | esegue `workflows.yaml`, applica i gate 🟢/🔴, coda swarm | **Gael** | GEM-06 |
| `memory/` | memoria unica a due livelli, lock anti-collisione ID, `mem recall` | **Claude** | GEM-02 |
| `inspect/` | Ispettorato: WF-PERF-LOOP T0→T5, scorecard 5D, telemetria | **Claude** | GEM-03 |
| `registry/` | anagrafe ADR-008, orfani, duplicati, gate bloccante | **Gemini/Antigravity** | GEM-04 |
| `dash/` | cruscotto HTML+MD, i 6 gate estate visibili | **Gemini/Antigravity** | GEM-05 |

Brief completi in [`company/Antigravity-Briefs/`](../company/Antigravity-Briefs/).

## Regole per chi ci lavora

1. **File congelati del seed**: `paths.py`, `config.py`, `schema.py`, `empire.toml`, `cli.py`,
   `conform.py`. Sono la fondazione condivisa Max/Gael/Gemini. Si possono **estendere**
   (nuove funzioni, nuovi campi, nuovi sottocomandi); **modificare o rinominare** ciò che
   esiste richiede una nota `⚠️ COORDINAMENTO` in `company/Memory/STATO-EMPIRE.md`.
2. **Zero path assoluti.** La radice si trova, non si dichiara. Il repo si sincronizza tra due
   macchine.
3. **Windows-first.** `safe_stdout()` come prima istruzione di ogni entry-point,
   `encoding="utf-8"` in ogni `open()`. Il crash `UnicodeEncodeError` di `memory_manager.py`
   non si ripete.
4. **Path con spazi.** La radice contiene `qui tutto` e `Digital Empire`: sempre `pathlib.Path`
   e liste di argomenti, mai interpolazione in stringa di shell.
5. **Standard library.** Nessuna dipendenza esterna nel seed. Aggiungerne una richiede una riga
   di motivazione in `requirements.txt`.
6. **Idempotenza.** Ogni comando si riesegue senza effetti collaterali.

## Test

```bash
python -m unittest discover -s empire/tests -p "test_*.py" -v
# oppure
python -m pytest empire/tests -q
```

## Perimetro

`empire/` **non** tocca: `EmpireDesk/platform/` (ownership Max), `Clienti/` (repo separati),
`.env`, `second-brain-vault/wiki/` (Memory Empire), le schede agente in
`company/Ecosistemi/**` (sono specifica approvata: si leggono, non si riscrivono).
</content>
