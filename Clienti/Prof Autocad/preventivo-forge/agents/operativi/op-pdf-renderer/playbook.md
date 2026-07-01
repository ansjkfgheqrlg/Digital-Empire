# Playbook — op-pdf-renderer

## Flusso standard
1. Verifica che `listing_it.json` abbia sia `content` che `price` (S3 e S4 fatti).
2. Esegui `render(ctx, dealer)`.
3. Controlla il log: motore usato + dimensione KB.
4. Apri il PDF e verifica a occhio le 9 sezioni.
5. Consegna a Gate D.

## Personalizzazione per dealer
- **Logo:** metti `logo.png` in `concessionarie/<dealer>/`. Se assente, l'header lo omette.
- **Colore accento:** `preventivo.accent_color` nel config del dealer (default rosso sobrio).
- **Breakdown prezzo:** mostrato solo se `preventivo.show_price_breakdown_to_customer=true`.
- **Validità/nota:** `preventivo.validity_days` + `preventivo.footer_note`.

## Troubleshooting
| Problema | Causa | Azione |
|---|---|---|
| "Nessun motore PDF" | né Playwright né WeasyPrint | installa Playwright + chromium |
| PDF < 20 KB | render vuoto | controlla che `content`/foto esistano |
| Foto mancanti nella gallery | file non su disco | verifica `runs/<id>/foto/` (S1) |
| Placeholder `{{ }}` nel PDF | campo template non passato | Gate D lo intercetta; controlla il context |

## Riferimento verificato
Run BMW 320d → `preventivo_bmw-320d.pdf` 63 KB, motore Playwright, Gate D PASS.
