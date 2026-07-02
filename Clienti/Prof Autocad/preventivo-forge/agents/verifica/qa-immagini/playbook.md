# Playbook — qa-immagini

## Quando gira
Dopo S5 (render), insieme a Gate R. Chiamata: `gate_img(ctx, dealer)`.
Wiring in `run.py` = Max (dopo S5), come da HANDOFF-GAEL-2 TASK 4.

## Interpretare i risultati
| Issue | Significato | Azione |
|---|---|---|
| `foto nel PDF (N) != foto annuncio (M)` | foto perse nel render | correggi `photo_pages` in `render_pdf` |
| `foto X mancante su disco` | download S1 fallito | rilancia scraping / verifica foto/ |
| `foto X bassa risoluzione` | immagine troppo piccola | usa la variante grande (scraper `rule=mo-1600`) |
| `uso di 'cover'` | template ritaglia | metti `object-fit: contain` nel `.photo-box img` |

## Riferimento verificato
Fixture BMW (4 foto) → `photo-box` = 4 == immagini, `contain` presente, Gate IMG PASS.
