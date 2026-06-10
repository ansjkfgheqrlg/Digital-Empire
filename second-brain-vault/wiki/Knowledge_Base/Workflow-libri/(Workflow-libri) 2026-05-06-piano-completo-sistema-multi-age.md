# 📚 Piano Completo Sistema Multi-Age
            
> Path: [[Map - Workflow-Libri|Workflow-libri]]

## Content

📚 Piano Completo: Sistema Multi-Agente per Impaginazione Libri
Ti preparo tutto il piano strutturato, pronto da dare a Claude Code.

1. STRUTTURA DEL PROGETTO
text

book-factory/
│
├── CLAUDE.md                          # Istruzioni master per Claude Code
│
├── config/
│   └── book_config.yaml               # Configurazione del libro corrente
│
├── input/
│   ├── manuscript.md                   # Testo completo del libro (Markdown)
│   └── image_prompts.yaml             # Prompt delle immagini per capitolo
│
├── agents/
│   ├── AGENT_IMAGE_GENERATOR.md       # Istruzioni Agente 1
│   ├── AGENT_LAYOUT.md                # Istruzioni Agente 2
│   └── AGENT_QA.md                    # Istruzioni Agente 3
│
├── templates/
│   ├── book_template.html             # Template HTML base del libro
│   ├── chapter_page.html              # Template pagina capitolo
│   ├── image_page.html                # Template pagina immagine
│   └── styles.css                     # CSS per impaginazione 6x9
│
├── assets/
│   └── images/                        # Immagini generate (output Agente 1)
│       ├── chapter_01.png
│       ├── chapter_02.png
│       └── ...
│
├── output/
│   ├── book_draft.pdf                 # PDF bozza
│   ├── book_final.pdf                 # PDF finale post-QA
│   └── qa_report.md                   # Report qualità
│
├── scripts/
│   ├── generate_images.py             # Script generazione immagini
│   ├── parse_manuscript.py            # Parser del manoscritto
│   ├── build_book.py                  # Costruttore PDF
│   ├── qa_checker.py                  # Quality assurance
│   └── orchestrator.py                # Orchestratore flusso completo
│
├── requirements.txt
└── README.md
2. CLAUDE.md (FILE MASTER)
Markdown

# CLAUDE.md — Book Factory: Sistema di Impaginazione Automatica Libri

## 🎯 OBIETTIVO DEL PROGETTO
Creare un sistema automatizzato che, dato un manoscritto in Markdown e una lista
di prompt per immagini, produca un PDF professionale impaginato in formato 6×9 pollici,
pronto per la stampa (KDP Amazon o simili).

## 🏗️ ARCHITETTURA: 3 AGENTI

### Agente 1 — IMAGE GENERATOR
- **File istruzioni**: `agents/AGENT_IMAGE_GENERATOR.md`
- **Input**: `input/image_prompts.yaml`
- **Output**: immagini in `assets/images/`
- **Compito**: Leggere i prompt dal file YAML, generare le immagini tramite API
  (DALL-E 3 / Midjourney / Flux), salvarle con naming convention `chapter_XX.png`
- **Specifiche immagini**: 
  - Risoluzione minima: 300 DPI
  - Dimensioni: 1800x2700px (per coprire pagina 6x9 a 300dpi)
  - Formato: PNG
  - Stile: coerente tra tutti i capitoli

### Agente 2 — LAYOUT ENGINE
- **File istruzioni**: `agents/AGENT_LAYOUT.md`
- **Input**: `input/manuscript.md` + `assets/images/` + `config/book_config.yaml`
- **Output**: `output/book_draft.pdf`
- **Compito**: Parsare il manoscritto, applicare formattazione, inserire immagini,
  generare PDF 6×9 pollici professionale
- **Stack tecnico**: Python + WeasyPrint (HTML/CSS → PDF)

### Agente 3 — QUALITY ASSURANCE
- **File istruzioni**: `agents/AGENT_QA.md`
- **Input**: `output/book_draft.pdf` + checklist
- **Output**: `output/qa_report.md` + `output/book_final.pdf` (se passa il check)
- **Compito**: Verificare ogni aspetto del libro contro la checklist di qualità

## 📐 SPECIFICHE TECNICHE DEL LIBRO

### Dimensioni pagina
- **Formato**: 6 × 9 pollici (15.24 × 22.86 cm)
- **Margini**: 
  - Interno (gutter): 0.75 pollici (per rilegatura)
  - Esterno: 0.5 pollici
  - Superiore: 0.75 pollici
  - Inferiore: 0.5 pollici
- **Area di stampa effettiva**: 4.75 × 7.75 pollici

### Tipografia
- **Font corpo testo**: Garamond, Georgia, o Crimson Text — dimensione 11pt
- **Interlinea**: 1.4 (line-height)
- **Font titolo capitolo**: stesso font, 24pt, bold, centrato
- **Font sottotitoli**: stesso font, 14pt, bold
- **Font numero capitolo**: 14pt, uppercase, centrato, sopra il titolo
- **Parole in grassetto**: usare **bold** dove indicato nel Markdown

### Struttura di ogni capitolo
1. **Pagina immagine** (pagina intera, solo immagine centrata, nessun testo, 
   nessun header/footer)
2. **Pagina titolo capitolo** (numero capitolo + titolo, centrati verticalmente)
3. **Pagine di testo** (corpo del capitolo con formattazione)

### Regole di impaginazione
- Ogni capitolo inizia su pagina dispari (recto)
- La pagina immagine precede la pagina del titolo del capitolo
- Nessuna pagina orfana (ultima riga di paragrafo da sola in cima a pagina)
- Nessuna vedova (prima riga di paragrafo da sola in fondo a pagina)
- Header su pagine di testo: titolo del libro (pari) / titolo capitolo (dispari)
- Footer: numero pagina centrato
- La prima pagina di ogni capitolo NON ha header
- Le pagine immagine NON hanno header né footer né numero pagina

## 📁 FORMATO DEI FILE DI INPUT

### manuscript.md
Il manoscritto usa questa convenzione Markdown:
Capitolo 1: Il Risveglio dell'Imperatore
La Nascita del Potere
Marco Aurelio nacque in una Roma turbolenta, dove il potere era
sia una benedizione che una maledizione...

Le Prime Lezioni
Fin dalla giovane età, Marco comprese che la disciplina era...

Capitolo 2: La Forgia dello Spirito
Il Cammino Interiore
...

text


Dove:
- `# Capitolo X: Titolo` = inizio nuovo capitolo
- `## Sottotitolo` = sottosezione
- `**parola**` = grassetto
- `---` = separatore tra capitoli (opzionale)

### image_prompts.yaml
```yaml
images:
  - chapter: 1
    prompt: "Ancient Roman emperor meditating in a marble palace at dawn, 
             stoic atmosphere, golden light, oil painting style, 
             dramatic lighting, 4k, detailed"
    style_notes: "Toni caldi, atmosfera contemplativa"
    
  - chapter: 2
    prompt: "Roman soldier training in an ancient gymnasium, 
             stoic discipline, marble columns, morning mist, 
             renaissance painting style, 4k"
    style_notes: "Enfasi sulla disciplina fisica"
book_config.yaml
YAML

book:
  title: "Mentalità da Imperatore"
  subtitle: "La Via Stoica al Potere Interiore"
  author: "Nome Autore"
  year: 2025
  language: "it"
  
page:
  width: "6in"
  height: "9in"
  margins:
    top: "0.75in"
    bottom: "0.5in"
    inner: "0.75in"
    outer: "0.5in"

typography:
  body_font: "Crimson Text"
  body_size: "11pt"
  line_height: 1.4
  chapter_title_size: "24pt"
  subtitle_size: "14pt"
  chapter_number_size: "14pt"

images:
  api: "openai"  # oppure "replicate", "midjourney"
  model: "dall-e-3"
  size: "1024x1792"  # verticale per pagina libro
  quality: "hd"
  
output:
  format: "pdf"
  filename: "mentality_imperatore"
🔄 FLUSSO DI LAVORO (ORCHESTRATOR)
text

STEP 1: Validazione Input
  → Verificare che manuscript.md esista e sia ben formattato
  → Verificare che image_prompts.yaml abbia un prompt per ogni capitolo
  → Verificare book_config.yaml

STEP 2: Agente 1 — Generazione Immagini
  → Per ogni capitolo, generare l'immagine dal prompt
  → Salvare in assets/images/chapter_XX.png
  → Verificare che tutte le immagini siano state generate
  → Log: quali immagini generate, eventuali errori

STEP 3: Agente 2 — Impaginazione
  → Parsare manuscript.md → estrarre capitoli, titoli, sottotitoli, testo
  → Per ogni capitolo:
    1. Creare pagina immagine (full-page, centrata)
    2. Creare pagina titolo capitolo
    3. Creare pagine di testo con formattazione
  → Applicare grassetti, dimensioni font, margini
  → Generare PDF 6×9
  → Salvare in output/book_draft.pdf

STEP 4: Agente 3 — Quality Assurance
  → Eseguire checklist completa
  → Generare report in output/qa_report.md
  → Se tutto OK → copiare come output/book_final.pdf
  → Se errori → segnalare cosa correggere
🛠️ STACK TECNICO
Python 3.11+
WeasyPrint: per conversione HTML/CSS → PDF con supporto pagine
Jinja2: per templating HTML
PyYAML: per leggere configurazioni
Pillow: per processare/verificare immagini
OpenAI API (o altra): per generare immagini
PyPDF2 o pikepdf: per analisi QA del PDF
⚠️ REGOLE IMPORTANTI PER CLAUDE CODE
NON inventare mai contenuto testuale — usare SOLO il testo dal manuscript.md
NON saltare capitoli — ogni capitolo DEVE avere la sua pagina immagine
Mantenere l'ORDINE esatto dei capitoli come nel manoscritto
Le immagini devono essere su pagina DEDICATA, SENZA testo
Il PDF finale deve essere ESATTAMENTE 6×9 pollici
Testare il PDF aprendolo e verificando le dimensioni
Se un'immagine non viene generata, mettere un placeholder grigio con testo
"IMMAGINE MANCANTE - Capitolo X"
Salvare log di ogni operazione in output/build_log.txt
text


---

## 3. ISTRUZIONI PER OGNI AGENTE

### AGENT_IMAGE_GENERATOR.md

```markdown
# Agente 1: Image Generator

## Ruolo
Sei l'agente responsabile della generazione di tutte le immagini del libro.

## Input
- File: `input/image_prompts.yaml`
- Config: `config/book_config.yaml` (per sapere quale API usare)

## Output
- Immagini in: `assets/images/chapter_XX.png` (XX = numero capitolo, zero-padded)
- Log: `output/image_generation_log.txt`

## Procedura

### Step 1: Leggere i prompt
```python
import yaml

with open('input/image_prompts.yaml', 'r') as f:
    data = yaml.safe_load(f)
    
prompts = data['images']
Step 2: Per ogni prompt, generare l'immagine
Usare l'API configurata in book_config.yaml
Se OpenAI/DALL-E 3:
Modello: dall-e-3
Size: 1024x1792 (verticale)
Quality: hd
Style: natural (o vivid, secondo il libro)
Aggiungere al prompt base un suffisso di stile per coerenza:
"Consistent art style: [stile del libro]. No text in the image."
Step 3: Salvare le immagini
Naming: chapter_01.png, chapter_02.png, ...
Verificare che ogni file sia valido (apribile con Pillow)
Se errore nella generazione, ritentare 2 volte, poi creare placeholder
Step 4: Generare log
text

[2025-01-15 10:30:00] Capitolo 1: ✅ Generata (1024x1792, 2.3MB)
[2025-01-15 10:30:45] Capitolo 2: ✅ Generata (1024x1792, 1.8MB)
[2025-01-15 10:31:20] Capitolo 3: ❌ Errore API - Retry 1/2
[2025-01-15 10:31:50] Capitolo 3: ✅ Generata (1024x1792, 2.1MB)
Gestione Errori
Se l'API restituisce errore: retry fino a 2 volte con backoff
Se fallisce dopo 3 tentativi: creare immagine placeholder
Il placeholder deve essere un'immagine 1024x1792 grigia con testo:
"PLACEHOLDER - Capitolo X - Rigenerare manualmente"
Validazione Finale
Prima di terminare, verificare:

 Numero immagini generate = numero capitoli nel manoscritto
 Tutte le immagini sono PNG validi
 Tutte le immagini hanno aspect ratio verticale
 Nessuna immagine contiene testo sovrapposto indesiderato
text


### AGENT_LAYOUT.md

```markdown
# Agente 2: Layout Engine

## Ruolo
Sei l'agente responsabile dell'impaginazione completa del libro in PDF 6×9 pollici.

## Input
- Manoscritto: `input/manuscript.md`
- Immagini: `assets/images/chapter_XX.png`
- Config: `config/book_config.yaml`
- Templates: `templates/`

## Output
- PDF: `output/book_draft.pdf`
- Log: `output/layout_log.txt`

## Stack
- Python + WeasyPrint + Jinja2

## Struttura del PDF (in ordine)

### Pagine Preliminari
1. **Pagina bianca** (opzionale, per stampa)
2. **Frontespizio**: Titolo, Sottotitolo, Autore — centrati verticalmente
3. **Pagina copyright**: Anno, "Tutti i diritti riservati", info
4. **Indice**: Lista capitoli con numeri pagina (generato automaticamente)
5. **Pagina bianca** (per far iniziare il Capitolo 1 su pagina dispari)

### Per ogni Capitolo
1. **Pagina immagine** (pagina intera):
   - L'immagine occupa tutta la pagina (bleed)
   - NESSUN testo, NESSUN header, NESSUN footer, NESSUN numero pagina
   - L'immagine è centrata e ridimensionata per coprire l'area di stampa
   
2. **Pagina titolo capitolo**:
   - Centrata verticalmente nel terzo superiore della pagina
   - "CAPITOLO X" in maiuscolo, 14pt, centrato
   - Spazio
   - "Titolo del Capitolo" in 24pt, bold, centrato
   - NESSUN header, numero pagina in basso centrato
   
3. **Pagine di testo**:
   - Corpo testo: 11pt, giustificato, interlinea 1.4
   - Sottotitoli (##): 14pt, bold, spazio sopra 18pt, spazio sotto 8pt
   - Parole in grassetto: **bold** come da Markdown
   - Paragrafi: rientro prima riga 0.3in OPPURE spazio tra paragrafi 6pt
   - Header: titolo libro (pagine pari) / titolo capitolo (pagine dispari)
   - Footer: numero pagina centrato
   - Prima pagina di testo del capitolo: NO header

### Pagine Finali
1. **Pagina "Fine"** o **"Nota dell'Autore"** (opzionale)
2. **Pagina bianca finale**

## CSS Critico per 6×9

```css
@page {
    size: 6in 9in;
    margin-top: 0.75in;
    margin-bottom: 0.5in;
    
    @bottom-center {
        content: counter(page);
        font-size: 10pt;
    }
}

@page :left {
    margin-left: 0.5in;    /* esterno */
    margin-right: 0.75in;  /* interno (gutter) */
    
    @top-left {
        content: "Titolo del Libro";
        font-size: 9pt;
        font-style: italic;
    }
}

@page :right {
    margin-left: 0.75in;   /* interno (gutter) */
    margin-right: 0.5in;   /* esterno */
    
    @top-right {
        content: string(chapter-title);
        font-size: 9pt;
        font-style: italic;
    }
}

@page image-page {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
}

@page chapter-start {
    @top-left { content: none; }
    @top-right { content: none; }
}

.image-page {
    page: image-page;
    page-break-before: always;
    page-break-after: always;
}

.image-page img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.chapter-title-page {
    page: chapter-start;
    page-break-before: right; /* Inizia sempre su pagina dispari */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    text-align: center;
}

h1 {
    font-size: 24pt;
    font-weight: bold;
    string-set: chapter-title content();
}

h2 {
    font-size: 14pt;
    font-weight: bold;
    margin-top: 18pt;
    margin-bottom: 8pt;
}

p {
    font-size: 11pt;
    line-height: 1.4;
    text-align: justify;
    text-indent: 0.3in;
    margin: 0;
    orphans: 2;
    widows: 2;
}

strong {
    font-weight: bold;
}
Procedura di Build
Step 1: Parsing del manoscritto
Python

# Estrarre la struttura:
# - Lista capitoli
# - Per ogni capitolo: numero, titolo, sottotitoli, paragrafi
# - Identificare parole in grassetto
# - Contare capitoli totali
Step 2: Preparazione HTML
Python

# Usare Jinja2 per popolare i template:
# - Per ogni capitolo, generare blocco HTML
# - Inserire riferimenti alle immagini
# - Applicare classi CSS corrette
Step 3: Generazione PDF
Python

from weasyprint import HTML

html_content = render_complete_book()  # HTML completo
HTML(string=html_content).write_pdf('output/book_draft.pdf')
Step 4: Verifica dimensioni
Python

# Aprire il PDF e verificare:
# - Dimensione pagina = 6x9 pollici (432x648 pt)
# - Numero pagine ragionevole
# - Tutte le immagini presenti
⚠️ Attenzione
NON ridimensionare le immagini in modo che si deformino (mantenere aspect ratio)
Le immagini devono COPRIRE tutta la pagina (object-fit: cover)
Se un'immagine manca, inserire placeholder con bordo e testo
I numeri di pagina delle pagine preliminari possono essere in numeri romani
Il conteggio pagine arabe inizia dal Capitolo 1
text


### AGENT_QA.md

```markdown
# Agente 3: Quality Assurance

## Ruolo
Sei l'agente responsabile del controllo qualità finale del libro PDF.

## Input
- PDF da controllare: `output/book_draft.pdf`
- Manoscritto originale: `input/manuscript.md`
- Config: `config/book_config.yaml`
- Immagini: `assets/images/`

## Output
- Report: `output/qa_report.md`
- Se tutto OK: copia il PDF come `output/book_final.pdf`
- Se errori critici: lista azioni correttive

## CHECKLIST DI QUALITÀ

### 1. Dimensioni e Formato
- [ ] Dimensione pagina esattamente 6×9 pollici (432×648 punti)
- [ ] Margini corretti (verificare con misurazione)
- [ ] PDF valido (nessun errore di apertura)
- [ ] Numero pagine coerente con lunghezza manoscritto

### 2. Contenuto Testuale
- [ ] TUTTO il testo del manoscritto è presente nel PDF
- [ ] Nessun testo tagliato o fuori margine
- [ ] Nessun capitolo mancante
- [ ] Ordine dei capitoli corretto
- [ ] Nessun testo duplicato
- [ ] Nessun carattere corrotto o mancante (encoding UTF-8)

### 3. Formattazione Testo
- [ ] Titoli capitolo: dimensione corretta (24pt), bold, centrati
- [ ] Numero capitolo: presente sopra ogni titolo, 14pt, maiuscolo
- [ ] Sottotitoli: dimensione corretta (14pt), bold
- [ ] Corpo testo: dimensione corretta (11pt)
- [ ] Interlinea corretta (1.4)
- [ ] Testo giustificato
- [ ] Parole in grassetto dove indicato nel Markdown
- [ ] Nessuna orfana (ultima riga sola in cima pagina)
- [ ] Nessuna vedova (prima riga sola in fondo pagina)

### 4. Immagini
- [ ] Ogni capitolo ha la sua pagina immagine
- [ ] Le immagini sono su pagine DEDICATE (nessun testo sulla stessa pagina)
- [ ] Le immagini sono visibili e non corrotte
- [ ] Le immagini sono correttamente ridimensionate (no deformazione)
- [ ] Le pagine immagine NON hanno header/footer/numeri pagina
- [ ] L'ordine delle immagini corrisponde ai capitoli

### 5. Struttura del Libro
- [ ] Frontespizio presente con titolo, sottotitolo, autore
- [ ] Pagina copyright presente
- [ ] Indice presente con numeri pagina corretti
- [ ] Ogni capitolo inizia su pagina dispari (recto)
- [ ] Sequenza corretta: immagine → titolo → testo per ogni capitolo

### 6. Headers e Footers
- [ ] Numeri pagina presenti e sequenziali
- [ ] Header pagine pari: titolo del libro
- [ ] Header pagine dispari: titolo del capitolo corrente
- [ ] Prima pagina di ogni capitolo: NO header
- [ ] Pagine immagine: NO header, NO footer, NO numero pagina
- [ ] Pagine preliminari: numerazione romana o nessuna

### 7. Qualità Generale
- [ ] Nessuna pagina completamente bianca indesiderata
- [ ] Spaziatura coerente in tutto il libro
- [ ] Font coerente in tutto il libro
- [ ] Nessun artefatto visivo

## Procedura di Verifica

### Step 1: Analisi automatica del PDF
```python
import pikepdf

pdf = pikepdf.open('output/book_draft.pdf')

# Verificare dimensioni pagina
for i, page in enumerate(pdf.pages):
    mediabox = page.MediaBox
    width = float(mediabox[2]) - float(mediabox[0])   # in punti
    height = float(mediabox[3]) - float(mediabox[1])
    
    assert abs(width - 432) < 1, f"Pagina {i+1}: larghezza errata ({width}pt)"
    assert abs(height - 648) < 1, f"Pagina {i+1}: altezza errata ({height}pt)"

# Contare pagine totali
total_pages = len(pdf.pages)
Step 2: Confronto testo
Python

# Estrarre testo dal PDF
# Confrontare con manuscript.md
# Verificare che ogni paragrafo del manoscritto sia presente
# Segnalare testo mancante o in eccesso
Step 3: Verifica immagini
Python

# Contare immagini nel PDF
# Verificare che il numero corrisponda ai capitoli
# Verificare posizione (pagine dedicate)
Step 4: Generazione Report
Il report deve avere questo formato:

Markdown

# 📋 Report Quality Assurance — [Titolo Libro]
**Data**: 2025-XX-XX
**PDF analizzato**: book_draft.pdf
**Pagine totali**: XXX

## Risultato Globale: ✅ PASSATO / ❌ DA CORREGGERE

## Dettaglio Checklist

### Dimensioni e Formato
| Check | Stato | Note |
|-------|-------|------|
| Dimensione pagina 6×9 | ✅ | 432×648pt verificato |
| PDF valido | ✅ | Nessun errore |
| Numero pagine | ✅ | 187 pagine |

### Contenuto Testuale
| Check | Stato | Note |
|-------|-------|------|
| Testo completo | ✅ | 12/12 capitoli presenti |
| Nessun testo tagliato | ✅ | Verificato |

... (continua per ogni sezione)

## Errori Critici (da correggere obbligatoriamente)
1. ❌ Capitolo 7: immagine mancante
2. ❌ Pagina 45: testo fuori margine destro

## Warning (consigliato correggere)
1. ⚠️ Pagina 23: possibile vedova (1 riga isolata)
2. ⚠️ Capitolo 10: spaziatura sottotitolo inconsistente

## Azioni Correttive
1. Rigenerare immagine Capitolo 7 e rilanciare Agente 2
2. Verificare margine destro nel CSS per pagina 45
Step 5: Decisione finale
Se 0 errori critici → copiare book_draft.pdf come book_final.pdf
Se errori critici presenti → NON creare book_final.pdf, solo il report
text


---

## 4. ORCHESTRATORE

```python
# scripts/orchestrator.py

"""
Book Factory Orchestrator
Coordina i 3 agenti in sequenza per produrre il libro finale.

Uso: python scripts/orchestrator.py
"""

import subprocess
import sys
import os
from datetime import datetime

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
    with open("output/build_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def run_step(step_name, script_path):
    log(f"{'='*60}")
    log(f"INIZIO: {step_name}")
    log(f"{'='*60}")
    
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        log(f"❌ ERRORE in {step_name}:")
        log(result.stderr)
        return False
    
    log(f"✅ COMPLETATO: {step_name}")
    return True

def main():
    # Pulizia log
    os.makedirs("output", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)
    
    with open("output/build_log.txt", "w") as f:
        f.write(f"Book Factory Build Log\n{'='*60}\n")
    
    log("🚀 AVVIO BOOK FACTORY")
    
    # Step 0: Validazione input
    log("Step 0: Validazione input...")
    if not os.path.exists("input/manuscript.md"):
        log("❌ File manuscript.md non trovato!")
        return
    if not os.path.exists("input/image_prompts.yaml"):
        log("❌ File image_prompts.yaml non trovato!")
        return
    if not os.path.exists("config/book_config.yaml"):
        log("❌ File book_config.yaml non trovato!")
        return
    log("✅ Tutti i file di input presenti")
    
    # Step 1: Generazione immagini
    if not run_step("AGENTE 1 — Generazione Immagini", "scripts/generate_images.py"):
        log("⛔ Pipeline interrotta per errore nella generazione immagini")
        return
    
    # Step 2: Impaginazione
    if not run_step("AGENTE 2 — Impaginazione Libro", "scripts/build_book.py"):
        log("⛔ Pipeline interrotta per errore nell'impaginazione")
        return
    
    # Step 3: Quality Assurance
    if not run_step("AGENTE 3 — Quality Assurance", "scripts/qa_checker.py"):
        log("⛔ Pipeline interrotta per errore nel QA")
        return
    
    # Risultato finale
    if os.path.exists("output/book_final.pdf"):
        log("🎉 LIBRO COMPLETATO CON SUCCESSO!")
        log(f"📖 File finale: output/book_final.pdf")
    else:
        log("⚠️ Libro generato ma con errori. Controllare output/qa_report.md")

if __name__ == "__main__":
    main()
5. REQUIREMENTS.TXT
text

weasyprint>=60.0
Jinja2>=3.1
PyYAML>=6.0
Pillow>=10.0
pikepdf>=8.0
openai>=1.0
requests>=2.31
markdown>=3.5

## Collegamenti Correlati
- [[Knowledge_Base/Stubs/headers|headers]]
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - General|General Area]]
