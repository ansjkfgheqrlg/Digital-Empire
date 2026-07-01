# Agente: op-pdf-renderer

- **ID:** op-pdf-renderer
- **Team:** Operativo (Half B / Gael)
- **Stage:** S5 — Render PDF
- **Motore:** `implementation/render_pdf.py` + `templates/preventivo.html`
- **Regola:** `rules/R5-pdf-render.md`
- **Gate a valle:** Gate D (`qa-output-reviewer`)
- **Modello consigliato:** deterministico (nessun LLM; è impaginazione)

## Missione
Comporre `listing_it.json` (content di Gael + price di Max) in un **PDF professionale** pronto
per il cliente, con foto locali incorporate e prezzo finale nel titolo.

## Responsabilità
- Costruire il contesto Jinja2 dal listing IT + dealer.
- Normalizzare e incorporare le foto in base64 (copertina + gallery + logo).
- Renderizzare HTML → PDF (Playwright preferito, WeasyPrint fallback).
- Salvare `runs/<id>/preventivo_<marca-modello>.pdf` e ritornarne il path.

## Confini (NON fa)
- NON traduce (è S3) né calcola il prezzo (è S4).
- NON scarica foto da remoto (le usa già in locale da `runs/<id>/foto/`).
- NON modifica il contenuto testuale: impagina soltanto.

## Input / Output
- **IN:** `listing.json` (foto), `listing_it.json` (content+price), `dealer`.
- **OUT:** `runs/<id>/preventivo_<slug>.pdf` (Path).

## Definition of Done
PDF > 20 KB, tutte le sezioni presenti, prezzo nel titolo, 0 placeholder → Gate D verde.
