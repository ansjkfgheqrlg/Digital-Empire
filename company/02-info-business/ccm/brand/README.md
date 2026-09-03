---
Type: PROJECT
Status: Active
Tags: #ccm #brand #lancio #design-system #guidelines
Created: 2026-09-03
Last updated: 2026-09-03
---

# BRAND GUIDELINES CCM — Claude Code Mastery

Il sistema visivo e verbale del lancio di **Claude Code Mastery**, in 17 pagine A4.

## Il file da mandare in giro

`CCM-Brand-Guidelines.pdf` — 17 pagine, 0,86 MB.

## Come si rigenera

    python build_brand_guidelines.py
    python build_brand_guidelines.py --html-only   # solo HTML, per ispezione a schermo

Motore: HTML + Chromium `page.pdf()` via Playwright. Font Onest e IBM Plex Mono da Google.

## Come e' fatto

| File | Cosa contiene |
|---|---|
| `build_brand_guidelines.py` | CSS, impaginato, grana, stampa |
| `content.py` | testo e struttura delle 17 pagine |
| `_preview/` | screenshot pagina per pagina (fuori da git) |

Si cambia il copy toccando solo `content.py`.

## Da dove vengono i valori

**Nessun valore e' inventato.**

- Colori, raggi, componenti, gradienti: letti da
  `Lancio corso skill beast/Leanding Page CCM/ccm-premium/src/app/globals.css`.
- Dati del concorrente: cattura forense del DOM in
  `competitor/Andrei Pascu/site-study/capture/07-claude-speedrun/design-tokens.json`.

Quando cambia una delle due fonti, il documento va rigenerato.

## La tesi del documento

`claude-speedrun.com`, il concorrente diretto di CCM, usa **il nostro identico `#fb4604`,
il nostro identico Onest e i nostri identici raggi** (12px e 9999px). Non e' una somiglianza:
e' lo stesso sistema visivo.

Quello che lui **non ha** e' la famiglia argento — tre gradienti costruiti, le pillole
flottanti, le card. Da qui la decisione che vincola tutto il resto del documento:

> **L'arancione smette di essere la nostra identita' e resta il colore dell'azione.
> L'argento su fondo inchiostro diventa la firma.**

## Regole di impaginazione rispettate

- Fondo chiaro e grana leggera, mai massimalista (riferimento AP Sales dato da Max).
- Un heading per pagina.
- Nessuna linea di separazione: lo stacco e' spazio.
- Unita' atomiche: un blocco o entra intero, o va alla pagina dopo.
- Grana come PNG ripetuto, mai filtro SVG (in stampa Chromium lo rasterizza e il file
  supera i 16 MB — lezione del piano editoriale YouTube).

## Verifica automatica

Ogni pagina e' misurata: il fondo dell'ultimo elemento contro il margine utile.
Alla consegna: **17 pagine su 17 in norma**, nessuna che trabocca, nessuna sotto l'80%
di riempimento.

## Connessioni

- [[Digital_Empire_Design_System]]
- [[Competitor_Andrei_Pascu]]
- [[Lancio_CCM]]
