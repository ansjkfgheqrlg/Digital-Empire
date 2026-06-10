# CLAUDE.md — Book Factory: Sistema di Impaginazione Automatica Libri

## OBIETTIVO DEL PROGETTO
Creare un sistema automatizzato che, dato un manoscritto in Markdown e una lista
di prompt per immagini, produca un PDF professionale impaginato in formato 6x9 pollici,
pronto per la stampa (KDP Amazon o simili).

## ARCHITETTURA: 3 AGENTI

### Agente 1 — IMAGE GENERATOR
- **File istruzioni**: `agents/AGENT_IMAGE_GENERATOR.md`
- **Script**: `scripts/generate_images.py`
- **Input**: `input/image_prompts.yaml`
- **Output**: immagini in `assets/images/`

### Agente 2 — LAYOUT ENGINE
- **File istruzioni**: `agents/AGENT_LAYOUT.md`
- **Script**: `scripts/build_book.py` + `scripts/parse_manuscript.py`
- **Input**: `input/manuscript.md` + `assets/images/` + `config/book_config.yaml`
- **Output**: `output/book_draft.pdf`

### Agente 3 — QUALITY ASSURANCE
- **File istruzioni**: `agents/AGENT_QA.md`
- **Script**: `scripts/qa_checker.py`
- **Input**: `output/book_draft.pdf`
- **Output**: `output/qa_report.md` + `output/book_final.pdf`

## SPECIFICHE TECNICHE

### Dimensioni pagina
- Formato: 6 x 9 pollici (432 x 648 pt)
- Margini interni: 0.75in, esterni: 0.5in, top: 0.75in, bottom: 0.5in

### Tipografia
- Font corpo: Crimson Text / Georgia / Garamond — 11pt
- Interlinea: 1.4
- Titolo capitolo: 24pt, bold, centrato
- Sottotitoli: 14pt, bold
- Numero capitolo: 14pt, uppercase

### Struttura capitolo
1. Pagina immagine (full-page, no header/footer)
2. Pagina titolo capitolo (centrata, no header)
3. Pagine di testo (header + footer)

## REGOLE IMPORTANTI
- NON inventare contenuto testuale — usare SOLO il testo da manuscript.md
- NON saltare capitoli — ogni capitolo DEVE avere la sua pagina immagine
- Il PDF finale deve essere ESATTAMENTE 6x9 pollici
- Se un'immagine manca, inserire placeholder grigio
- Salvare log in output/build_log.txt

## AVVIO
```bash
pip install -r requirements.txt
python scripts/orchestrator.py
```
