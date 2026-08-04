# Tools — qa-output-reviewer

| Tool | Uso |
|---|---|
| `qa_gate.gate_d(ctx, dealer=None)` | verifica PDF + contenuto + (opz.) re-render |
| `render_pdf._render_html(...)` | re-render HTML per ispezione placeholder/immagini |
| filesystem `ctx.dir.glob("preventivo_*.pdf")` | trova il PDF più recente |
| `common.load_json` | lettura listing.json + listing_it.json |

## Verifica profonda (se `dealer` passato)
Re-renderizza l'HTML dal template e controlla:
- assenza di `{{` / `}}` (placeholder Jinja non risolti);
- `data:image/` presenti (immagini incorporate, non hotlink).

## Dati
- Legge: `runs/<id>/preventivo_*.pdf`, `listing.json`, `listing_it.json`, foto in `runs/<id>/foto/`.
- Non scrive nulla.
