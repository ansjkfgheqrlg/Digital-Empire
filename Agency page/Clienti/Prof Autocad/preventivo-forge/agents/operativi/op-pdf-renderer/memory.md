# Memory — op-pdf-renderer

## Conoscenza persistente
- Il template `templates/preventivo.html` è la memoria di layout: ogni miglioria di impaginazione
  vive lì (CSS inline, sezioni condizionali).
- Namespace memory (se Backbone attivo): `agency/preventivo/render` per preferenze per-dealer.

## Lezioni apprese
- 2026-07-01: su Windows WeasyPrint richiede GTK nativo (import fallisce) → **Playwright è il motore
  di default**; è già dipendenza dichiarata dell'Half A.
- 2026-07-01: incorporare le foto in **base64 data-URI** elimina i problemi di path/base-url tra i due
  motori ed evita hotlink (Gate D).
- `page.pdf()` richiede Chromium headless: mai tentarlo in modalità headful.

## Preferenze cliente Prof Autocad
- Stile pulito/professionale (scelto da Max).
- Breakdown prezzo NON mostrato al cliente (`show_price_breakdown_to_customer=false`).
- Validità preventivo 15 giorni; nota "Prezzo chiavi in mano da confermare".
- Logo: attendere `logo.png` dal cliente (oggi assente → header senza logo).
