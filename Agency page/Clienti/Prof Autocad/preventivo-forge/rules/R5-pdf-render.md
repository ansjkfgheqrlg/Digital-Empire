# R5 — Render PDF Preventivo (S5, Half B / Gael)

> RBI operabile a freddo. Motore: `implementation/render_pdf.py` + `templates/preventivo.html`.
> Agente responsabile: `op-pdf-renderer`. Gate a valle: **Gate D** (`qa-output-reviewer`).

## OBIETTIVO
Comporre `listing_it.json` (content di Gael + price di Max) in un **PDF professionale** per il
cliente, con foto incorporate in locale (mai hotlink) e prezzo finale nel titolo.

## TRIGGER
- `run.py` step 5, dopo S4 (pricing). Chiamata: `render_pdf.render(ctx, dealer)`.

## INPUT
| Fonte | Campo | Uso |
|---|---|---|
| `runs/<id>/listing.json` | `images[].local_path` | copertina + gallery (embed base64) |
| `runs/<id>/listing_it.json` | `content.*` | titolo, specs, descrizione, dotazioni, highlights |
| | `price.final_eur`, `price.final_title`, `price.breakdown` | banda titolo + box prezzo |
| `dealer` | `display_name`, `contacts`, `logo_path`, `_dir` | header |
| | `preventivo.validity_days`, `footer_note`, `show_price_breakdown_to_customer`, `accent_color?` | footer/box/stile |

## OUTPUT
`runs/<id>/preventivo_<marca-modello>.pdf` (ritorna il `pathlib.Path`).

## STEP-BY-STEP
1. Carica `listing.json` + `listing_it.json`; estrai `content`, `price`, `preventivo`.
2. Prepara immagini: `_image_data_uri()` normalizza con Pillow (resize + JPEG q82) → base64.
   Copertina = prima foto; gallery = fino a 9 foto; logo se presente.
3. Costruisci il contesto Jinja2 e renderizza `templates/preventivo.html`.
4. `_html_to_pdf()` — **Playwright** (Chromium headless, `page.pdf`, A4, print_background) →
   fallback **WeasyPrint** → se nessuno, salva `.html` e alza errore azionabile.
5. Salva in `runs/<id>/preventivo_<slug>.pdf`; logga motore e dimensione.

## SEZIONI DEL PDF (minime — Gate D le verifica)
1. Header: logo + nome concessionaria + contatti.
2. Banda titolo: `title_it` + `headline_it` + prezzo (`final_eur`).
3. Foto copertina.
4. Scheda tecnica (`specs_it`).
5. Punti di forza (`highlights_it`) + Descrizione (`description_it`).
6. Dotazioni (`equipment_it`, 2 colonne).
7. Galleria (tutte le foto locali).
8. Box prezzo (`final_eur`; breakdown solo se `show_price_breakdown_to_customer`=true).
9. Footer: validità (`validity_days`) + `footer_note`.

## GESTIONE ERRORI / SELF-HEALING
- Motore PDF assente → prova l'altro; se entrambi mancano, HTML salvato + istruzioni install.
- Immagine illeggibile → Pillow fallisce → fallback byte grezzi; se manca il file → saltata.
- Logo assente → header senza logo (grazioso, non blocca).
- `final_eur` assente → "Prezzo su richiesta" (ma Gate D blocca se manca il prezzo nel titolo).

## CASI LIMITE
- 0 foto → niente copertina/gallery (Gate D segnala se `listing.json` aveva foto non su disco).
- PDF < 20 KB → sintomo di render vuoto → Gate D blocca.
- Immagini molto grandi → ridimensionate (cover ≤1400px, gallery ≤800px) per tenere il PDF leggero.

## SICUREZZA
Foto **sempre** incorporate in locale (base64). Mai `src` remoto (evita hotlink/leak/404 nel PDF).

## LOG
`ctx.logger`: nome file, motore usato (playwright/weasyprint), dimensione KB.
