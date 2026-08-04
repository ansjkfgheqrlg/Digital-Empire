# Tools — qa-regole-checker

| Tool | Uso |
|---|---|
| `qa_gate.gate_regole(ctx, dealer)` | verifica R-01…R-14 + scrive `regole-check.json` |
| `render_pdf._render_html(...)` | re-render HTML per ispezionare gli elementi delle regole |
| `qa_gate.gate_img(ctx, dealer)` | R-09 (delega) |
| `qa_gate.gate_b(ctx, dealer)` | R-11 (delega: italiano/no tedesco/no invenzioni) |
| `qa_gate.gate_c(ctx, dealer)` | R-12 (delega: prezzo indipendente) |
| `common.save_json` | scrive `runs/<id>/regole-check.json` |

## Report prodotto
`runs/<id>/regole-check.json`: `{ "R-01": {"pass": true, "note": "..."}, ... }`.
Serve come prova di conformità allegata al run (audit).

## Dati
- Legge: `runs/<id>/listing.json`, `listing_it.json`, config concessionaria (via `dealer`).
- Scrive: `runs/<id>/regole-check.json`.
