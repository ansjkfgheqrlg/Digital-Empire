# Tools — op-pdf-renderer

| Tool | Uso | Note |
|---|---|---|
| `render_pdf.render(ctx, dealer)` | entrypoint S5 | ritorna il Path del PDF |
| `render_pdf._render_html(...)` | HTML da template | usato anche da Gate D per il re-render |
| `render_pdf._image_data_uri(path, max_w)` | foto→base64 | Pillow resize + JPEG q82 |
| `render_pdf._html_to_pdf(html, out, ctx)` | HTML→PDF | Playwright → WeasyPrint → errore azionabile |
| `templates/preventivo.html` | template Jinja2 | stile inline, sezioni condizionali |

## Dipendenze runtime
- `jinja2` (template), `pillow` (immagini) — obbligatorie.
- Motore PDF: **Playwright + Chromium** (consigliato su Windows) *oppure* **WeasyPrint** (+GTK).
- Setup una tantum: `pip install playwright && playwright install chromium`.

## Dati
- Legge: `runs/<id>/listing.json`, `runs/<id>/listing_it.json`, foto in `runs/<id>/foto/`,
  logo in `dealer._dir/logo_path`.
- Scrive: `runs/<id>/preventivo_<slug>.pdf` (o `.html` di emergenza se nessun motore).
