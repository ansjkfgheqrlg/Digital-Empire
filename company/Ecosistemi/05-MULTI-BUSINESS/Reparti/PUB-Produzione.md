> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.2 + 5.1 + 5.2

# Reparto L2 — PUB-Produzione (interfaccia CF + book-factory) (`MB-PUB`)

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-PUB-PROD · **Priorità:** MEDIA-ALTA
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Interfaccia tra Multi-Business e Content-Factory per il manoscritto, e motore dell'impaginazione
via book-factory (`Workflow-libri/`). Questo reparto NON scrive il manoscritto — lo ordina a CF
e poi lo impagina in PDF 6x9 tramite l'asset esistente wrappato (ADR-003: mai riscrivere).

## Workflow L3 di competenza

| Workflow | Fase pipeline | Output |
|---|---|---|
| `WF-PUB-BOOK-ORDER` | 2 — Ordine manoscritto | Contratto a CF: `{brand_kit, formato: manoscritto_md + image_prompts.yaml, spec: n_capitoli/parole/stile}` → consegna: manoscritto MD + image_prompts |
| `WF-PUB-LAYOUT` | 3 — Impaginazione | `book_final.pdf` 6x9 + `qa_report.md` verde; Gate Layout superato |

## Funzioni L4

| Team | Responsabilità |
|---|---|
| T-manuscript-brief | Compila il brief-ordine manoscritto per CF: spec, niche, brand_kit, stile, n. capitoli/parole |
| T-image-prompts | Genera i prompt immagine (image_prompts.yaml) per le illustrazioni del libro |
| T-layout-engine | Opera `orchestrator.py` di book-factory: generate_images → build_book → output PDF 6x9 |
| T-book-qa | QA PDF tramite `qa_checker.py` + estensioni; verifica Gate Layout (vedi sotto) |

## Agenti L5 assegnati

- `mb-pub-layout-operator` (worker, WASM/Haiku) — esegue book-factory orchestrator.py
- `mb-pub-book-qa` (worker, Sonnet) — QA PDF 6x9, estende qa_checker.py
- `mb-pub-coord` (coordinator, Sonnet) — supervisione pipeline 7 step

## Asset esistente — integrazione book-factory (ADR-003)

`Workflow-libri/` viene wrappato come motore di WF-PUB-LAYOUT, esattamente com'è:
- `agents/` — agenti AI per scrittura/editing (3 agenti interni)
- `scripts/orchestrator.py` — pipeline principale
- `scripts/generate_images.py` — generazione immagini
- `scripts/build_book.py` — assemblaggio PDF
- `scripts/qa_checker.py` — QA automatico (esteso da mb-pub-book-qa)
- `templates/` — template capitoli e copertine
- `input/` → `output/book_final.pdf`

**Regola ferrea:** non riscrivere mai book-factory. Qualsiasi evoluzione = wrapper o estensione.

## Gate Layout (bloccante)

Criteri di pass:
- PDF esattamente 6x9 pollici
- Ogni capitolo ha pagina immagine (zero placeholder grigi residui)
- `qa_report.md` verde (zero errori critici)
- Zero caratteri mal formattati o encoding errato
- Numero pagine reale calcolato correttamente (serve per cover trim + spine in step 4)

## KPI di reparto

- % PDF che passano Gate Layout al primo colpo: ≥ 85% (baseline post F-MB6)
- Lead time ordine CF → PDF validato: ≤ 5 giorni lavorativi
- Zero libri pubblicati senza qa_report.md verde
