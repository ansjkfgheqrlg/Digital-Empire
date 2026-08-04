# 🤝 HANDOFF → GAEL — PreventivoForge Half B

> **Gael: leggi questo PRIMA di costruire.** Max ha fatto Half A (acquisizione, dati, prezzo, regia).
> Tu fai **Half B = Contenuto · Output · Qualità**. Non toccare Half A se non per il wiring concordato (sotto).
> Metodo: 9 passi (ADR-006). Agenti **CF-grade** (7 file). Usa skill `content-forge`, `copywriting`,
> `cro-copy-architect`, `copy-editing` (S3) e `verification-quality`/`agent-tester` (QA).

## Contesto in 3 righe
Workflow che trasforma un **annuncio mobile.de (DE)** in un **PREVENTIVO italiano (PDF)** per una
concessionaria (multi-tenant; prima = `prof-autocad`). Half A produce `listing.json` (dati) e la
parte `price` di `listing_it.json`. **Tu produci la parte testuale + il PDF + i gate QA.**

## Cosa devi costruire (file)
| # | File | Tipo | Funzione attesa (firma) |
|---|---|---|---|
| 1 | `implementation/translate_copy.py` | S3 | `translate(ctx, dealer) -> dict` |
| 2 | `implementation/render_pdf.py` | S5 | `render(ctx, dealer) -> pathlib.Path` |
| 3 | `implementation/qa_gate.py` | Gate B/C/D | `gate_b(ctx)->(bool,list)`, `gate_c(ctx)->(bool,list)`, `gate_d(ctx)->(bool,list)` |
| 4 | `templates/preventivo.html` | template | Jinja2, stile pulito/professionale |
| 5 | `agents/operativi/op-translator-copy/` | agente CF-grade (7 file) | — |
| 6 | `agents/operativi/op-pdf-renderer/` | agente CF-grade (7 file) | — |
| 7 | `agents/verifica/qa-extraction-verifier/` | agente CF-grade (7 file) | Gate A completo (oggi c'è solo un check minimo in run.py) |
| 8 | `agents/verifica/qa-translation-verifier/` | agente CF-grade (7 file) | Gate B |
| 9 | `agents/verifica/qa-price-verifier/` | agente CF-grade (7 file) | Gate C (ricalcola prezzo INDIPENDENTE) |
| 10 | `agents/verifica/qa-output-reviewer/` | agente CF-grade (7 file) | Gate D |
| 11 | `rules/R3-translation-copy.md`, `R5-pdf-render.md`, `R6-qa-gate.md` | RULES (RBI) | — |

## Contratti dati (CONGELATI — non cambiare senza Max)
- **Input tuo:** `runs/<id>/listing.json` conforme a `schema/listing.schema.json`.
  Foto già scaricate in `runs/<id>/foto/` (path relativi in `listing.json.images[].local_path`).
- **Output S3:** scrivi `runs/<id>/listing_it.json` riempiendo **solo `content.*`** conforme a
  `schema/listing_it.schema.json`. **MERGE, non sovrascrivere `price`** (è di Max). Pattern: leggi il
  file se esiste, aggiorna `content`, riscrivi. (`pricer.price()` fa lo stesso lato `price`.)
- **Output S5:** `runs/<id>/preventivo_<marca-modello>.pdf`. Ritorna il `Path`.

### Integrazione con la regia (run.py, di Max)
`run.py` già chiama, se i moduli esistono:
- `translate_copy.translate(ctx, dealer)` dopo S2 (prima del pricing)
- `render_pdf.render(ctx, dealer)` dopo S4
`ctx` è `common.RunContext` (ha `ctx.listing_path`, `ctx.listing_it_path`, `ctx.foto_dir`, `ctx.dir`,
`ctx.logger`, `ctx.trace`). `dealer` è il dict di `dealers.load_dealer()` (ha `display_name`, `contacts`,
`logo_path`, `_dir`, `preventivo`, `pricing_resolved`).
**Wiring gate B/C/D:** quando i tuoi gate sono pronti, avvisa Max: aggiunge 3 chiamate in `run.py`
(dopo S3/S4/S5). Non modificare tu `run.py` senza dirlo (è Half A).

## S3 — Traduzione + Copy (regole d'oro)
- **Fedeltà + miglioramento**: traduci `description_de` in italiano scorrevole e vendibile; migliora il
  copy ma **NON inventare** optional/dati non presenti in `listing.json`. (Lo verifica Gate B.)
- `content.equipment_it` allineato **1:1** a `listing.equipment_de` (stesso numero di voci, tradotte).
- `content.specs_it`: scheda con label IT (Anno, Km, Alimentazione, Cambio, Potenza, Trazione, Colore,
  Porte, Posti, Classe emissioni…) prese da `listing.json`.
- `content.title_it`: titolo SENZA prezzo (il prezzo lo mette Max in `price.final_title`).
- `content.highlights_it`: 3–6 punti di forza.
- **Glossario seed DE→IT** (estendilo): `Allrad`=integrale · `Schaltgetriebe`=cambio manuale ·
  `Automatik`=automatico · `Standheizung`=riscaldamento autonomo · `Sitzheizung`=sedili riscaldati ·
  `Anhängerkupplung (AHK)`=gancio traino · `Navigationssystem`=navigatore · `Panoramadach`=tetto panoramico ·
  `Rückfahrkamera`=telecamera posteriore · `Tempomat`=cruise control · `Klimaautomatik`=clima automatico ·
  `Lederausstattung`=interni in pelle · `LED-Scheinwerfer`=fari LED · `Einparkhilfe`=sensori parcheggio.

## S5 — PDF Preventivo (stile pulito/professionale, scelto da Max)
Modello di riferimento = il PDF preventivo del cliente (es. "Preventivo BMW Z4"): chiedilo a Max,
mettilo in `concessionarie/prof-autocad/_riferimenti/`. Sezioni minime:
1. **Header** — logo concessionaria (`dealer.logo_path` in `dealer._dir`) + nome + contatti.
2. **Titolo** — `price.final_title` (marca/modello + prezzo finale).
3. **Foto copertina** (prima immagine).
4. **Scheda tecnica** — `content.specs_it`.
5. **Descrizione** — `content.description_it` + `content.highlights_it`.
6. **Dotazioni** — `content.equipment_it`.
7. **Gallery** — tutte le foto in `runs/<id>/foto/` (embed LOCALE, mai hotlink).
8. **Box prezzo** — `price.final_eur`. Mostra `breakdown` SOLO se `dealer.preventivo.show_price_breakdown_to_customer` è true.
9. **Footer** — validità (`dealer.preventivo.validity_days`) + `dealer.preventivo.footer_note`.
Tecnica: Jinja2 → HTML → WeasyPrint (già in requirements). Alternativa: Playwright `page.pdf()`.

## Gate (criteri)
- **Gate B (traduzione):** 0 parole tedesche residue in `content.*`; `len(equipment_it)==len(equipment_de)`;
  numeri/specifiche invariati vs `listing.json`; nessun optional non presente nel sorgente.
- **Gate C (prezzo):** ricalcola in modo INDIPENDENTE `round(listed×(1+pct/100)+f1+f2)` con i parametri
  di `dealer.pricing_resolved` e verifica `== price.final_eur`; verifica formato `final_title`.
- **Gate D (PDF):** PDF esiste e >20KB; tutte le sezioni presenti; n. foto in PDF == n. foto in `listing.json`;
  nessun placeholder/`{{ }}` non risolto; prezzo presente nel titolo.

## Definition of Done (Half B)
`python run.py "<url>"` (o `--manual`) produce un `preventivo_*.pdf` valido, gate B/C/D verdi,
su `prof-autocad`. Poi: checkpoint `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md` + STATO-EMPIRE + push.
