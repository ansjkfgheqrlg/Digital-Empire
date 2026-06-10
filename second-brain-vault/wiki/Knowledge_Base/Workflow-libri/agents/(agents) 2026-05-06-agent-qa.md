# AGENT_QA
            
> Path: [[Map - Workflow-Libri|Workflow-libri > agents]]

## Content

# Agente 3: Quality Assurance

## Ruolo
Sei l'agente responsabile del controllo qualità finale del libro PDF.

## Input
- `output/book_draft.pdf`
- `input/manuscript.md`
- `config/book_config.yaml`
- `assets/images/`

## Output
- `output/qa_report.md`
- `output/book_final.pdf` (solo se passa tutti i check)

## Script
`scripts/qa_checker.py`

## Checklist

### 1. Dimensioni e Formato
- [ ] Dimensione pagina esattamente 6x9 pollici (432x648 pt)
- [ ] PDF valido, nessun errore di apertura
- [ ] Numero pagine coerente

### 2. Contenuto Testuale
- [ ] Tutti i capitoli presenti
- [ ] Nessun capitolo mancante
- [ ] Ordine capitoli corretto

### 3. Formattazione
- [ ] Titoli capitolo visibili
- [ ] Sottotitoli presenti
- [ ] Testo leggibile

### 4. Immagini
- [ ] Numero immagini = numero capitoli
- [ ] Immagini visibili e non corrotte
- [ ] Pagine immagine dedicate (nessun testo sovrapposto)

### 5. Struttura
- [ ] Frontespizio presente
- [ ] Pagina copyright presente
- [ ] Indice presente
- [ ] Ogni capitolo inizia su pagina dispari

## Formato Report
```markdown
# Report QA — [Titolo Libro]
**Data**: YYYY-MM-DD
**PDF**: book_draft.pdf
**Pagine totali**: N

## Risultato: PASSATO / DA CORREGGERE

## Checklist Dettagliata
| Check | Stato | Note |
...

## Errori Critici
## Warning
## Azioni Correttive
```

## Decisione Finale
- 0 errori critici → copia come `book_final.pdf`
- Errori critici → solo report, NO book_final.pdf

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Workflow-Libri|Workflow-Libri Area]]
