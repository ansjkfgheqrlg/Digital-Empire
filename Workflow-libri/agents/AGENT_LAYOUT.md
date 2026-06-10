# Agente 2: Layout Engine

## Ruolo
Sei l'agente responsabile dell'impaginazione completa del libro in PDF 6x9 pollici.

## Input
- `input/manuscript.md`
- `assets/images/chapter_XX.png`
- `config/book_config.yaml`
- `templates/`

## Output
- `output/book_draft.pdf`
- `output/layout_log.txt`

## Stack
Python + WeasyPrint + Jinja2

## Script
- `scripts/parse_manuscript.py` — parser del manoscritto
- `scripts/build_book.py` — costruttore PDF

## Struttura PDF

### Pagine Preliminari
1. Frontespizio: Titolo, Sottotitolo, Autore
2. Pagina copyright
3. Indice automatico
4. Pagina bianca (per far iniziare Cap.1 su pagina dispari)

### Per ogni Capitolo
1. **Pagina immagine** — full-page, NO header/footer/numero
2. **Pagina titolo** — "CAPITOLO X" + Titolo, centrati
3. **Pagine testo** — corpo con header/footer

### Pagine Finali
- Pagina bianca finale

## CSS Critico
```css
@page { size: 6in 9in; }
@page :left { margin-left: 0.5in; margin-right: 0.75in; }
@page :right { margin-left: 0.75in; margin-right: 0.5in; }
@page image-page { margin: 0; /* no header/footer */ }
```

## Regole Impaginazione
- Ogni capitolo inizia su pagina DISPARI (recto)
- Le immagini occupano TUTTA la pagina (object-fit: cover)
- Nessuna vedova/orfana (orphans: 2, widows: 2)
- Header pari: titolo libro | Header dispari: titolo capitolo
- Prima pagina capitolo: NO header
- Pagine immagine: NO header, NO footer, NO numero pagina

## Placeholder Immagini Mancanti
Se un'immagine non esiste, inserire rettangolo grigio con testo:
"IMMAGINE MANCANTE - Capitolo X"
