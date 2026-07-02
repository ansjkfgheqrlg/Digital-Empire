# Tools — qa-immagini

| Tool | Uso |
|---|---|
| `qa_gate.gate_img(ctx, dealer)` | esegue tutti i controlli R-09 |
| `render_pdf._render_html(...)` | re-render HTML per contare le foto + verificare `contain` |
| `PIL.Image` | apre ogni foto per risoluzione |
| `common.load_json` | lettura listing.json |

## Cosa conta come "foto nel PDF"
Nel template ogni foto è in un `<div class="photo-box">` (2 per pagina). Il gate conta le
occorrenze di `photo-box` nell'HTML e le confronta con `len(listing.images)`.

## Dati
- Legge: `runs/<id>/listing.json`, foto in `runs/<id>/foto/`.
- Non scrive nulla (il report complessivo lo scrive `qa-regole-checker`).
