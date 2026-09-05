---
Type: PROJECT
Status: Active
Tags: #ccm #brand #lancio #design-system #guidelines
Created: 2026-09-03
Last updated: 2026-09-05
---

# BRAND GUIDELINES CCM — Claude Code Mastery

Il sistema visivo e verbale del lancio di **Claude Code Mastery**, in 18 pagine A4.

## Il file da mandare in giro

`CCM-Brand-Guidelines.pdf` — 18 pagine, 0,67 MB. Copertina, indice, **15 capitoli**, colophon.

## Come si rigenera

    python build_brand_guidelines.py
    python build_brand_guidelines.py --html-only   # solo HTML, per ispezione a schermo

Motore condiviso: `PIANO-MAESTRO/scripts/pdf_engine_empire.py` (standard-oro
`28-DOSSIER-HIGGSFIELD-ELEVENLABS.pdf`, direttiva Max 2026-09-05) — HTML + Chromium
`page.pdf()` via Playwright. Font Onest e IBM Plex Mono da Google.

## Come e' fatto

| File | Cosa contiene |
|---|---|
| `build_brand_guidelines.py` | CSS, impaginato, grana, stampa |
| `content.py` | testo e struttura delle 18 pagine |
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

## La grana ha un capitolo suo (cap. 11)

Non e' un dettaglio tecnico ma la firma materica del marchio, e il documento la tratta come tale:
tre campioni a confronto (assente / 13% da stampa / piena da schermo), i valori esatti dei due
strati, e il confronto misurato con gli altri — il concorrente diretto usa un reticolo appena
percettibile, il sito hub di Andrei Pascu una mezzatinta quasi invisibile. **Loro la nascondono,
noi la dichiariamo.**

## Regole di impaginazione rispettate

- Fondo chiaro e grana leggera, mai massimalista (riferimento AP Sales dato da Max).
- Un heading per pagina.
- Nessuna linea di separazione: lo stacco e' spazio.
- Unita' atomiche: un blocco o entra intero, o va alla pagina dopo.
- Grana come PNG ripetuto, mai filtro SVG (in stampa Chromium lo rasterizza e il file
  supera i 16 MB — lezione del piano editoriale YouTube).

## Verifica automatica

Ogni pagina e' misurata: il fondo dell'ultimo elemento contro il margine utile.
Alla consegna: **18 pagine su 18 in norma**, nessuna che trabocca, nessuna sotto la soglia
di riempimento.

## Copertina e colophon (rifatte 2026-09-05)

Max ha giudicato il contenuto perfetto ma la grafica no, e ha dato come standard-oro il PDF
`28-DOSSIER-HIGGSFIELD-ELEVENLABS.pdf`: copertina e colophon non hanno piu' il titolo a
gradiente centrato con glow radiale, ma il pattern condiviso del motore — titolo piatto
ancorato al terzo basso, una parola sola accentata in arancione, `.cover-lead` e
`.cover-meta` a riga. Le 15 pagine interne non sono state toccate: erano gia' allo standard.

## Connessioni

- [[Digital_Empire_Design_System]]
- [[Competitor_Andrei_Pascu]]
- [[Lancio_CCM]]
