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

## Stato build (2026-07-01)
- **Half A (Max): COSTRUITA** — scraper, parser, pricer, conductor/regia, run.py, schema, skill.
- **Half B (Gael): ✅ COMPLETA e verificata (CP-20260701-001)** — `translate_copy.py`+`glossary_de_it.py` (S3),
  `render_pdf.py`+`templates/preventivo.html` (S5), `qa_gate.py` (Gate A/B/C/D), `rules/R3-R5-R6`,
  6 agenti CF-grade in `agents/`. Test end-to-end `run.py --manual` (BMW 320d) → PDF, 4 gate verdi.
- **Pending Max (non bloccante):** wiring gate B/C/D in `run.py` (3 chiamate dopo S3/S4/S5, vedi HANDOFF §Integrazione).
- **Setup ambiente:** `pip install -r requirements.txt && playwright install chromium` (motore PDF = Playwright).

## Convenzioni
- Python: pathlib, type hints, docstring, try/except su I/O esterno.
- Agenti CF-grade: 7 file (`agent.md`, `system_prompt.md`, `tools.md`, `playbook.md`,
  `failure_modes.md`, `evals.md`, `memory.md`).
