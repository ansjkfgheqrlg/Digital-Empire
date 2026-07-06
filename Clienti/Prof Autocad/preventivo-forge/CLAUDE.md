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

## Stato build (2026-07-05) — CONSEGNA NOVACAR PRONTA (ultimo su main `063cd27`)
- **Half A (Max): COMPLETA** — scraper (Chrome reale via `cdp.py`, off-screen, **aspetta `__INITIAL_STATE__`**, **profilo
  persistente anti-blocco IP**, retry), parser, pricer, regia `run.py` (Gate A/B/C/D/IMG/R + storico), schema, multi-tenant,
  **fabbrica `nuovo_concessionario.py`**, **kill-switch `licenza.py`+`gestione-licenze.py`** (Gist), **riserva AI `ai_translate.py`**
  (Groq €0), **archivio `archivio.py`**.
- **Half B (Gael): COMPLETA** — `translate_copy.py`+`glossary_de_it.py` (S3), `render_pdf.py`+`templates/preventivo.html`
  (S5, modello Novacar), `qa_gate.py`, app GUI premium pywebview (multi-link 10, avanzamento compatto, **Archivio**).
- **Novità 05/07**: traduzione AI su TUTTI i campi (6 auto → 0 residui) · gate solo su difetti veri · GUI avanzamento compatto
  + Archivio · **REGISTRO-ERRORI.md** + **CHECKLIST-CONSEGNA.md** (leggerli prima di modificare/consegnare).
- **⚠️ File Half B toccati da Max** (lista COMPLETA in STATO-EMPIRE): `app.py`, `ui/index.html` (riscritta), `translate_copy.py`
  (`_ai_fix_sources`+`_ai_final_sweep`), `qa_gate.py` (gate_img/gate_b/km), `glossary_de_it.py` (+TÜV). `render_pdf.py`/template/REGOLE mai toccati.
- **Consegna:** `Consegna-Novacar/PreventivoForge-Novacar.zip` (exe autonoma). Guida `COME-CONSEGNARE-A-NOVACAR.md`.
- **Setup dev:** `pip install -r requirements.txt`. Motore PDF/scraping = Chrome del PC via `cdp.py`.

## Convenzioni
- Python: pathlib, type hints, docstring, try/except su I/O esterno.
- Agenti CF-grade: 7 file (`agent.md`, `system_prompt.md`, `tools.md`, `playbook.md`,
  `failure_modes.md`, `evals.md`, `memory.md`).
