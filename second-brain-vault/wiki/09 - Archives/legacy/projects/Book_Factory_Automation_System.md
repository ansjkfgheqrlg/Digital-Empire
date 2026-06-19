# Project: Book Factory — Automated Book Production System

- **Type**: 📚 Book Production / 🤖 Automation System
- **Purpose**: Fully automated pipeline: manuscript → images → impagination → PDF (Amazon KDP ready)
- **Status**: 🟢 Operational (architecture defined, orchestrator built)
- **Tech Stack**: Python + WeasyPrint, DALL-E/Midjourney API, YAML configuration
- **Output Format**: 6×9" PDF (print-ready for Amazon KDP, IngramSpark, etc.)
- **Tags**: `#book-production` `#automation` `#pdf-generation` `#publishing` `#multi-agent`

---

## 📖 System Overview

**Book Factory** is a three-agent orchestrated system that transforms a Markdown manuscript into a professionally formatted, print-ready PDF with minimal human intervention.

**Problem Solved**: Self-publishing authors spend 40-60% of time on layout/formatting rather than writing. Book Factory automates this, freeing focus to content.

**Input**: 
1. Manuscript in Markdown
2. Image prompts per chapter (YAML)
3. Book configuration (metadata, fonts, margins)

**Output**:
1. Generated chapter images (DPI 300, print-quality)
2. Final PDF (6×9", print-ready)
3. QA report with compliance checklist

---

## 🏗️ Three-Agent Architecture

### Agent 1: IMAGE GENERATOR
**Purpose**: Create professional chapter illustrations

**Specifications**:
- **Input**: `image_prompts.yaml` (one prompt per chapter)
- **Output**: Chapter images in `assets/images/chapter_XX.png`
- **Resolution**: 300 DPI minimum (print quality)
- **Dimensions**: 1800×2700px (covers full 6×9" page at 300 DPI)
- **Format**: PNG
- **Consistency**: Unified visual style across all chapters

**API Integration**:
- DALL-E 3 (OpenAI)
- Midjourney (via API)
- Flux (via Replicate)

**Naming Convention**: `chapter_01.png`, `chapter_02.png`, ...

**Example Prompt Structure**:
```yaml
images:
  - chapter: 1
    prompt: "A Renaissance portrait of Dante Alighieri in exile, gazing toward Florence in the distance, dark dramatic lighting, classical painting style"
    style: "classical_painting"
    
  - chapter: 2
    prompt: "Napoleon standing alone on Sant'Elena island at sunset, staring toward the horizon, contemplative, oil painting, golden hour"
    style: "historical_portrait"
```

---

### Agent 2: LAYOUT ENGINE
**Purpose**: Parse manuscript, apply formatting, insert images, generate PDF

**Specifications**:
- **Input**: `manuscript.md` + generated images + `config/book_config.yaml`
- **Output**: `book_draft.pdf` (6×9", fully formatted)
- **Technology**: Python + WeasyPrint (HTML/CSS → PDF converter)

**Page Format: 6×9 inches**:
- **Total dimensions**: 6" × 9" (15.24 × 22.86 cm)
- **Interior margin (gutter)**: 0.75" (for binding)
- **Exterior margin**: 0.5"
- **Top margin**: 0.75"
- **Bottom margin**: 0.5"
- **Print area**: 4.75" × 7.75"

**Typography Standards**:
- **Body text font**: Garamond, Georgia, or Crimson Text
- **Font size**: 11pt
- **Line height**: 1.4 (for readability in print)
- **Chapter title**: 24pt, bold, centered
- **Subheadings**: 14pt, bold
- **Chapter number**: 14pt, uppercase, centered above title

**Chapter Structure**:
1. **Image page**: Full-page image, centered, no text/header/footer
2. **Chapter title page**: Chapter number + title, centered vertically
3. **Text pages**: Body text with headers/footers

**Pagination Rules**:
- Each chapter starts on recto (odd-numbered page)
- Image page precedes chapter title page
- No orphans (last line of paragraph alone at top of page)
- No widows (first line of paragraph alone at bottom)
- Header (text pages): book title (even pages) / chapter title (odd pages)
- Footer: centered page number
- First page of chapter: no header
- Image pages: no header, footer, or page number

**Manuscript Format** (Markdown):
```markdown
# Capitolo 1 — GLI ESILIATI
## Sottotitolo capitolo

Corpo del testo qui. Puoi usare **grassetto** e *corsivo*.

## Nuova sottosezione

Altro testo...

---

# Capitolo 2 — La Forgia dello Spirito
...
```

**Key Rules**:
- `# Capitolo X: Titolo` = new chapter marker
- `## Sottotitolo` = subsection
- `**parola**` = bold
- `---` = chapter separator (optional)
- NO invention of text (use ONLY manuscript content)
- NO chapter skipping
- Placeholder gray box if image missing
- Build logs to `output/build_log.txt`

---

### Agent 3: QUALITY ASSURANCE
**Purpose**: Verify every aspect of PDF against quality checklist

**Specifications**:
- **Input**: `book_draft.pdf` + QA checklist
- **Output**: `qa_report.md` + `book_final.pdf` (if passes)

**QA Checklist**:
- [ ] All 6×9" page dimensions correct
- [ ] All chapters present and in correct order
- [ ] Image placement correct (full-page, centered)
- [ ] Typography consistent across all pages
- [ ] Margins correct on all pages
- [ ] Headers/footers present (except chapter starts and image pages)
- [ ] Page numbers correct and consecutive
- [ ] No blank pages (unless intentional)
- [ ] No text overflow
- [ ] No orphans or widows
- [ ] Color mode: CMYK (for print) or RGB (for digital)
- [ ] All fonts embedded in PDF
- [ ] Metadata complete (title, author, copyright date)
- [ ] PDF readable and not corrupted
- [ ] Complies with KDP requirements
- [ ] Complies with IngramSpark requirements

**Pass/Fail Logic**:
- If all checks pass → approve `book_final.pdf`
- If checks fail → return `qa_report.md` with specific issues for human review

---

## 📊 Configuration System

### book_config.yaml Structure
```yaml
# Book metadata
book:
  title: "48 Persone che Hanno Vinto"
  author: "Digital Empire"
  copyright_year: 2026
  isbn: "978-3-16-148410-0"  # Optional

# Page setup
page:
  width: 6       # inches
  height: 9      # inches
  margin_interior: 0.75
  margin_exterior: 0.5
  margin_top: 0.75
  margin_bottom: 0.5

# Typography
fonts:
  body:
    family: "Crimson Text"
    size: 11
    line_height: 1.4
  chapter_title:
    family: "Crimson Text"
    size: 24
    weight: bold
  chapter_number:
    family: "Crimson Text"
    size: 14
    weight: uppercase

# Output
output:
  format: "pdf"
  color_mode: "CMYK"  # or "RGB"
  quality: "high"
```

---

## 🔄 End-to-End Workflow

```
1. AUTHOR PROVIDES
   ├── manuscript.md (Markdown file with all chapters)
   ├── image_prompts.yaml (one prompt per chapter)
   └── book_config.yaml (formatting specifications)

2. AGENT 1: IMAGE GENERATION
   ├── Reads image_prompts.yaml
   ├── Calls image API (DALL-E / Midjourney / Flux)
   ├── Saves images to assets/images/chapter_XX.png
   └── Logs status for each image

3. AGENT 2: LAYOUT ENGINE
   ├── Parses manuscript.md
   ├── Applies typography from config
   ├── Inserts chapter images in correct positions
   ├── Generates HTML intermediate format
   ├── Converts to PDF via WeasyPrint
   └── Saves book_draft.pdf

4. AGENT 3: QUALITY ASSURANCE
   ├── Reads book_draft.pdf
   ├── Runs QA checklist (16 checks)
   ├── Generates qa_report.md
   ├── If PASS: approves book_final.pdf
   └── If FAIL: flags issues for manual review

5. OUTPUT
   ├── book_final.pdf (print-ready)
   ├── qa_report.md (compliance documentation)
   └── build_log.txt (execution timeline)
```

---

## 📂 Project Structure

```
book-factory/
│
├── CLAUDE.md                    (master config for agents)
├── requirements.txt             (Python dependencies)
├── README.md
│
├── config/
│   └── book_config.yaml        (current book settings)
│
├── input/
│   ├── manuscript.md            (full Markdown manuscript)
│   └── image_prompts.yaml       (chapter image specs)
│
├── agents/
│   ├── AGENT_IMAGE_GENERATOR.md
│   ├── AGENT_LAYOUT.md
│   └── AGENT_QA.md
│
├── implementation/
│   ├── generate_images.py       (Agent 1 script)
│   ├── parse_manuscript.py      (manuscript parser)
│   ├── build_book.py            (PDF builder)
│   ├── qa_checker.py            (Agent 3 QA script)
│   ├── orchestrator.py          (orchestrator/runner)
│   └── utils/
│       ├── website_checker.py
│       ├── contact_extractor.py
│       ├── sheets_client.py
│       └── logger.py
│
├── templates/
│   ├── book_template.html
│   ├── chapter_page.html
│   ├── image_page.html
│   └── styles.css               (6x9 formatting CSS)
│
├── assets/
│   └── images/                  (generated chapter images)
│       ├── chapter_01.png
│       ├── chapter_02.png
│       └── ...
│
└── output/
    ├── book_draft.pdf           (after Agent 2)
    ├── book_final.pdf           (after Agent 3 approval)
    ├── qa_report.md             (compliance checklist)
    └── build_log.txt            (execution log)
```

---

## 💡 Key Features & Benefits

**Fully Automated**:
- No manual layout work
- No InDesign/Canva needed
- No expensive typesetter

**Professional Output**:
- Meets Amazon KDP specs
- Print-quality images (300 DPI)
- Proper typography (orphans/widows eliminated)
- CMYK color mode for offset printing

**Scalable**:
- One manuscript → multiple formats (hardcover, paperback, ebook)
- Batch processing multiple books
- Version control (manuscript iterations)

**Cost-Effective**:
- Upfront: image generation costs (DALL-E ~$0.04/img × 48 chapters = ~$2)
- Scaling: production cost nearly zero (just computational)
- vs. Traditional: saves $1,500-5,000 in design/layout fees per book

---

## 🔗 Related Pages

-  — The actual book created with this system
-  — Publishing platform optimization
-  — Traditional vs. automated comparison
-  — Larger publishing ecosystem

---

## 📝 Metadata

- **Created**: 2026-03-19
- **Status**: Architecture complete, orchestrator functional
- **First Book**: "48 Persone Che Hanno Vinto" (48 chapters)
- **Agents Operational**: 3/3
- **Production Time per Book**: ~2-3 hours (image generation + layout + QA)
- **Cost per Book**: ~$2-5 (API costs only)
- **Print-Ready**: Yes (KDP-compatible, CMYK)
