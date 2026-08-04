# Evals — op-pdf-renderer

## Test funzionali
| Eval | Input | Atteso |
|---|---|---|
| E1 esistenza | run completo | `preventivo_*.pdf` esiste |
| E2 dimensione | PDF generato | > 20 KB |
| E3 sezioni | template render | header, titolo, specs, descrizione, dotazioni, gallery, box prezzo, footer |
| E4 prezzo | banda titolo | contiene `final_eur` formattato + € |
| E5 foto locali | HTML | solo `data:image/...`, 0 `http(s)://` |
| E6 no placeholder | HTML | 0 occorrenze di `{{` o `}}` |
| E7 motore | ambiente Playwright | log "motore=playwright" |
| E8 breakdown off | dealer default | box prezzo senza dettaglio |

## Metriche
- **Render success rate** = 100% sugli annunci con dati validi.
- **Tempo render** < 3s per preventivo (Playwright headless).
- **Peso PDF** tipico 50–200 KB (dipende dal n. foto).

## Comando di verifica
`render(ctx, dealer)` poi `qa_gate.gate_d(ctx, dealer)` → `(True, [])`.
Riferimento verificato: BMW 320d, 63 KB, Gate D PASS.
