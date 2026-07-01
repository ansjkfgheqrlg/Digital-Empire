# CLAUDE.md — PreventivoForge (BRAIN, framework RBI)

## Identità progetto
Workflow multi-agente per il cliente **Prof Autocad** (automotive). Input: URL annuncio
**mobile.de** (tedesco). Output: **PDF** annuncio in **italiano**, copy migliorato, con
**prezzo finale** calcolato nel titolo. Deve girare **automatico** (consegna al cliente).

## Workflow attivi (trigger → file)
| Workflow | Trigger | Regola | Script |
|---|---|---|---|
| Pipeline completa | `/preventivo-auto <url>` o `python run.py <url>` | tutte | `run.py` |
| S1 Scraping | run.py step 1 | `rules/R1-scraping.md` | `implementation/scraper.py` |
| S2 Parsing | run.py step 2 | `rules/R2-parsing.md` | `implementation/parser.py` |
| S3 Traduci+Copy (Half B) | run.py step 3 | `rules/R3-translation-copy.md` | `implementation/translate_copy.py` |
| S4 Pricing | run.py step 4 | `rules/R4-pricing.md` | `implementation/pricer.py` |
| S5 PDF (Half B) | run.py step 5 | `rules/R5-pdf-render.md` | `implementation/render_pdf.py` |
| QA gate A–D (Half B) | dopo ogni step | `rules/R6-qa-gate.md` | `implementation/qa_gate.py` |

## Regole operative
- **Credenziali/config:** SOLO da `.env` (mai hardcoded). Vedi `.env.example`.
- **Data contract:** `schema/listing.schema.json` (raw) e `schema/listing_it.schema.json`
  (arricchito) sono CONGELATI. Validare sempre prima di passare allo step successivo.
- **Self-healing:** ogni step ha retry/fallback definiti nella sua regola. S1 fallisce →
  fallback manuale (`--manual`). Un gate rosso ferma la pipeline con messaggio chiaro.
- **No invenzione fatti:** la traduzione/copy (S3) può migliorare la forma ma NON aggiungere
  optional o dati non presenti in `listing.json`. Lo verifica Gate B.
- **Logging:** ogni step logga in `logs/` e appende a `runs/<id>/trace.jsonl`; stato in `runs/<id>/state.json`.
- **Naming run:** `runs/<id>/` con `id = AF-YYYYMMDD-HHMMSS-<sourceid>`.

## Stato build (2026-06-30)
- **Half A (Max): IN COSTRUZIONE** — scraper, parser, pricer, conductor/regia, run.py, schema, skill.
- **Half B (Gael): DA FARE** — vedi `HANDOFF-GAEL.md`. Finché assente, `run.py` si ferma dopo S4
  producendo `listing.json` + `listing_it.json` (sola parte prezzo) e stampa nota handoff.

## Convenzioni
- Python: pathlib, type hints, docstring, try/except su I/O esterno.
- Agenti CF-grade: 7 file (`agent.md`, `system_prompt.md`, `tools.md`, `playbook.md`,
  `failure_modes.md`, `evals.md`, `memory.md`).
