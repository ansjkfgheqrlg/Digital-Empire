# Failure Modes — op-pdf-renderer

| # | Modo di fallimento | Sintomo | Mitigazione |
|---|---|---|---|
| 1 | Nessun motore PDF disponibile | eccezione al render | fallback Playwright→WeasyPrint; se entrambi mancano salva `.html` + istruzioni |
| 2 | WeasyPrint senza librerie GTK (Windows) | ImportError | preferire Playwright; è già dipendenza Half A |
| 3 | Immagine corrotta/illeggibile | Pillow error | fallback byte grezzi; se manca, foto saltata (no crash) |
| 4 | Hotlink foto remoto | PDF con foto rotte/404 | vietato: solo base64 locale |
| 5 | Logo assente | header vuoto | omesso con grazia, non blocca |
| 6 | Prezzo assente | "Prezzo su richiesta" | Gate D blocca se manca nel titolo |
| 7 | PDF enorme | foto non ridimensionate | resize cover ≤1400px, gallery ≤800px |
| 8 | Placeholder non risolto | `{{ }}` nel PDF | Gate D re-render controlla; correggere il context |

## Nota Chromium
`page.pdf()` funziona solo in Chromium **headless**. Il render lancia sempre headless.
