---
- **Type**: PROJECT
- **Purpose**: Automated book production system that transforms manuscripts and image prompts into professional, print-ready PDFs
- **Status**: Active
- **Tags**: `#publishing` `#automation` `#book-production` `#pdf-generation` `#multi-agent-system`
- **Created**: 2026-04-29
- **Last updated**: 2026-04-29
- **Tech Stack**: Python, WeasyPrint, DALL-E 3, Jinja2, YAML, PDF generation
---

# Project: Book Factory Automation System

## Executive Summary

The Book Factory Automation System is a sophisticated, multi-agent orchestration platform designed to completely automate professional book production. Given a manuscript and image generation prompts, the system produces print-ready PDFs in standard 6×9 inch format (Amazon KDP compatible) through three specialized agents:

1. **IMAGE GENERATOR** — Creates all chapter illustrations via DALL-E 3
2. **LAYOUT ENGINE** — Imposes manuscript into professional 6×9 PDF format
3. **QUALITY ASSURANCE** — Validates all technical specifications and content

## Project Architecture

### Three-Agent System

```
INPUT FILES (manuscript.md + image_prompts.yaml + book_config.yaml)
    ↓
[1] IMAGE GENERATOR AGENT (generate_images.py)
    ↓ Produces: assets/images/chapter_XX.png
    ↓
[2] LAYOUT ENGINE AGENT (parse_manuscript.py + build_book.py)
    ↓ Produces: output/book_draft.pdf
    ↓
[3] QUALITY ASSURANCE AGENT (qa_checker.py)
    ↓ Produces: output/qa_report.md + output/book_final.pdf
```

## Agent 1: Image Generator

### Responsibility
Generate all chapter illustrations using DALL-E 3 API.

### Input
- **Configuration**: `config/book_config.yaml`
- **Prompts**: `input/image_prompts.yaml` (YAML format with chapter prompts)

### Output
- **Images**: `assets/images/chapter_01.png`, `chapter_02.png`, etc.
- **Log**: `output/image_generation_log.txt`

### Processing Steps

**Step 1: Parse Prompt File**
```python
import yaml
with open('input/image_prompts.yaml', 'r') as f:
    data = yaml.safe_load(f)
prompts = data['images']
```

**Step 2: Generate Each Image**
- **API**: OpenAI DALL-E 3 (configurable in `book_config.yaml`)
- **Image Size**: 1024×1792 pixels (vertical, book-page format)
- **Quality**: HD (high definition)
- **Instruction Appended**: "No text, no letters, no words in the image."
- **Retry Logic**: 2 retries on failure, then create placeholder

**Step 3: Save & Validate**
- Naming convention: `chapter_01.png`, `chapter_02.png`, etc.
- Validation: Use Pillow (PIL) to verify each file is a valid image
- Dimensions verified: Exactly 1024×1792

**Step 4: Fallback - Placeholder Generation**
If image generation fails after 3 attempts:
- Create 1024×1792 gray image
- Add centered text: "PLACEHOLDER - Chapter X - Regenerate Manually"
- Save and log failure

### Error Handling
- Retry with exponential backoff: 5 seconds, then 10 seconds
- After 3 failures: auto-generate gray placeholder
- All operations logged with timestamps

### Validation Checklist
- [ ] Image count equals chapter count in manuscript
- [ ] All images are valid PNG files
- [ ] All images have correct aspect ratio (vertical: 1024×1792)
- [ ] No corrupted files
- [ ] All images accessible and readable

---

## Agent 2: Layout Engine

### Responsibility
Transform manuscript and images into a professional, impeccably formatted PDF.

### Input Files
- **Manuscript**: `input/manuscript.md` (Markdown format)
- **Images**: `assets/images/chapter_*.png` (from Image Generator)
- **Configuration**: `config/book_config.yaml`
- **Templates**: `templates/` directory (Jinja2 HTML templates)

### Output
- **Draft PDF**: `output/book_draft.pdf`
- **Log**: `output/layout_log.txt`

### Tech Stack
- **Language**: Python
- **PDF Generation**: WeasyPrint
- **Templating**: Jinja2
- **Markdown Parsing**: markdown library or pandoc

### Page Specifications

**Book Format**:
- Size: 6 × 9 inches (432 × 648 points)
- DPI: 300 (for print quality)

**Margins** (in inches):
- Inside margin (left): 0.75 in
- Outside margin (right): 0.5 in
- Top margin: 0.75 in
- Bottom margin: 0.5 in

**Typography**:
- Body font: Crimson Text, Georgia, or Garamond — 11 pt
- Line height: 1.4 (moderate leading)
- Chapter title: 24 pt, bold, centered
- Subheadings: 14 pt, bold
- Chapter number: 14 pt, uppercase, centered

### Document Structure

#### Preliminary Pages (Front Matter)

1. **Title Page**
   - Book title (centered, large)
   - Subtitle (centered, smaller)
   - Author name (centered)
   - Publisher info (if applicable)

2. **Copyright Page**
   - Copyright notice
   - ISBN (if applicable)
   - Publication date
   - License/rights information

3. **Table of Contents**
   - Auto-generated from chapter headings
   - Page numbers right-aligned

4. **Blank Page** (to ensure Chapter 1 starts on recto/right page)

#### Chapter Pages (Body)

For each chapter:

1. **Chapter Image Page**
   - Full-page image (edge-to-edge, no margins)
   - No header, footer, or page number
   - Image scaling: `object-fit: cover`

2. **Chapter Title Page**
   - "CHAPTER X" (uppercase, centered, 14 pt)
   - Chapter title (centered, 24 pt, bold)
   - No header or footer
   - Establishes right-hand (recto) page

3. **Chapter Body Pages**
   - Flowing manuscript text
   - Header: Book title (left/even pages), Chapter title (right/odd pages)
   - Footer: Page number (centered or per convention)
   - Orphans/widows: Minimum 2 lines (CSS: `orphans: 2; widows: 2`)

#### Back Matter

- Final blank page (even pagination)

### CSS for Print

```css
@page {
  size: 6in 9in;
  margin: 0;
}

@page :left {
  margin-left: 0.5in;
  margin-right: 0.75in;
}

@page :right {
  margin-left: 0.75in;
  margin-right: 0.5in;
}

@page :first {
  margin: 0;
  /* Title page, no header/footer */
}

@page image-page {
  margin: 0;
  /* Image pages, no header/footer */
}

body {
  font-family: 'Crimson Text', Georgia, serif;
  font-size: 11pt;
  line-height: 1.4;
  orphans: 2;
  widows: 2;
}
```

### Impagination Rules

- **Odd/Even Pages**: Each chapter starts on an odd (right/recto) page
- **Image Coverage**: Full-page images occupy 100% of page area
- **Text Flow**: Automatic, with no manual breaks (except chapter breaks)
- **Headers**: Different for left (even) vs. right (odd) pages
- **Page Numbers**: Bottom center, but NOT on image pages or title pages

### Missing Image Handling

If an image file doesn't exist:
1. Generate a placeholder gray rectangle (1024×1792)
2. Add centered text: "IMAGE MISSING - Chapter X"
3. Insert into PDF
4. Log warning in `output/layout_log.txt`

### Manuscript Format Requirements

**Markdown structure** (expected format):

```markdown
# Book Title

## Chapter 1: First Chapter

Chapter text here...

## Chapter 2: Second Chapter

More chapter text...
```

The parser extracts:
- H1: Book title
- H2: Chapter headings and content
- Body paragraphs: Flow into main text

---

## Agent 3: Quality Assurance (QA)

### Responsibility
Validate all technical specifications and content integrity of the generated PDF.

### Input
- **Draft PDF**: `output/book_draft.pdf`
- **Manuscript**: `input/manuscript.md` (for content verification)
- **Configuration**: `config/book_config.yaml`
- **Assets**: `assets/images/` (for image verification)

### Output
- **QA Report**: `output/qa_report.md` (detailed findings)
- **Final PDF**: `output/book_final.pdf` (if all checks pass)

### QA Checklist

#### 1. Dimensions and Format
- [ ] Page size: Exactly 6×9 inches (432×648 points)
- [ ] PDF is valid and opens without errors
- [ ] All pages render correctly
- [ ] DPI/resolution: 300+ (for print)

#### 2. Content Integrity
- [ ] All chapters present (no missing chapters)
- [ ] Chapter order correct (1, 2, 3, ... N)
- [ ] No duplicate chapters
- [ ] Text visible and legible

#### 3. Formatting Validation
- [ ] Chapter titles visible and properly sized
- [ ] Subheadings present and formatted
- [ ] Body text readable (font size, line height appropriate)
- [ ] Margins respected (no text cutoff)

#### 4. Image Validation
- [ ] Number of images = number of chapters
- [ ] All images visible and not corrupted
- [ ] Image pages dedicated (no text overlay)
- [ ] Images scale correctly (no distortion)

#### 5. Structural Integrity
- [ ] Front matter present (title, copyright, TOC)
- [ ] Chapters follow front matter
- [ ] Page numbering consistent
- [ ] Each chapter starts on odd (right) page

#### 6. Typography & Accessibility
- [ ] Text contrast sufficient for readability
- [ ] Font sizes consistent with spec
- [ ] No text reflow errors
- [ ] Special characters/unicode renders correctly

### QA Report Format

```markdown
# QA Report — [Book Title]

**Generated**: YYYY-MM-DD HH:MM:SS
**PDF File**: book_draft.pdf
**Total Pages**: N

## Overall Result: PASSED / REQUIRES CORRECTIONS

## Detailed Checklist

| Category | Check | Status | Notes |
|----------|-------|--------|-------|
| Format | Page size 6×9 in | ✓ PASS | |
| Format | DPI 300+ | ✓ PASS | |
| Content | All chapters present | ✓ PASS | 12 chapters verified |
| Content | Correct order | ✓ PASS | |
| Images | Count matches chapters | ✓ PASS | 12 images |
| Images | All visible | ✓ PASS | |
| Structure | Front matter complete | ✓ PASS | Title, Copyright, TOC |
| Structure | Chapter starts on recto | ✓ PASS | All verified |

## Critical Errors
None detected.

## Warnings
- None

## Recommendations
- Consider wider margins for easier reading
- Font size appropriate for intended audience

## Action Items
- PDF ready for print-on-demand (KDP, IngramSpark, etc.)
- Recommended next steps: Submit to Amazon KDP

---

**Validated By**: QA Agent v1.0
**Validation Date**: YYYY-MM-DD
```

### Decision Logic

- **0 critical errors** → Copy `book_draft.pdf` to `book_final.pdf`, ready for publication
- **1+ critical errors** → Halt, generate report only, no final PDF produced
- **Warnings (non-critical)** → Generate final PDF but include remediation suggestions

### Possible Critical Errors

1. Page size not 6×9 inches
2. Missing chapters
3. Duplicate chapters
4. Images missing or corrupted
5. Text unreadable (contrast/font issues)
6. PDF corrupted or unopenable

---

## Configuration System

### book_config.yaml

```yaml
book:
  title: "My Book Title"
  subtitle: "Optional Subtitle"
  author: "Author Name"
  publisher: "Publisher Name"
  isbn: "978-XXXXXXXXX"
  publication_date: "2026-04-29"
  format:
    width_inches: 6
    height_inches: 9
    dpi: 300
  margins:
    inside: 0.75
    outside: 0.5
    top: 0.75
    bottom: 0.5
  typography:
    body_font: "Crimson Text"
    body_size: 11
    line_height: 1.4
    heading_size: 24
    heading_weight: bold
  images:
    api: "openai_dalle3"
    size: "1024x1792"
    quality: "hd"
    fallback: "placeholder_gray"
```

---

## Workflow Orchestration

### Main Orchestrator (orchestrator.py)

```python
import subprocess
import sys

def main():
    print("Starting Book Factory Automation...")
    
    # Step 1: Image Generation
    print("\n[1/3] Generating images...")
    result = subprocess.run([sys.executable, "scripts/generate_images.py"], check=False)
    if result.returncode != 0:
        print("ERROR: Image generation failed")
        sys.exit(1)
    
    # Step 2: Layout & PDF Generation
    print("\n[2/3] Building PDF layout...")
    result = subprocess.run([sys.executable, "scripts/build_book.py"], check=False)
    if result.returncode != 0:
        print("ERROR: PDF generation failed")
        sys.exit(1)
    
    # Step 3: Quality Assurance
    print("\n[3/3] Running QA checks...")
    result = subprocess.run([sys.executable, "scripts/qa_checker.py"], check=False)
    if result.returncode != 0:
        print("ERROR: QA validation failed")
        sys.exit(1)
    
    print("\n✓ Book production complete!")
    print("→ Output: output/book_final.pdf")

if __name__ == "__main__":
    main()
```

### Startup Command

```bash
pip install -r requirements.txt
python scripts/orchestrator.py
```

---

## Integration Points

This system integrates with:
- [[SaaS_Copywriter_Agent]] — for book marketing copy
- [[Tool_UI_Engineer_Agent]] — for book cover design
- [[Skill_Neon_Dark_Premium]] — for premium book aesthetics
- 
- [[Project_App_Landing_Pages]] — marketing pages for published books

## Supported Output Formats

- **Amazon KDP** (Kindle Direct Publishing) — 6×9 PDF format, ready to upload
- **IngramSpark** — same format, broader distribution
- **Print-on-Demand services** — universal compatibility

## Project Files & Locations

```
Workflow-libri/
├── CLAUDE.md                      # Project overview
├── agents/
│   ├── AGENT_IMAGE_GENERATOR.md
│   ├── AGENT_LAYOUT.md
│   └── AGENT_QA.md
├── scripts/
│   ├── orchestrator.py
│   ├── generate_images.py
│   ├── parse_manuscript.py
│   ├── build_book.py
│   └── qa_checker.py
├── config/
│   └── book_config.yaml
├── templates/
│   ├── title_page.html
│   ├── chapter.html
│   └── styles.css
├── input/
│   ├── manuscript.md
│   └── image_prompts.yaml
├── assets/
│   └── images/
├── output/
│   ├── book_draft.pdf
│   ├── book_final.pdf
│   ├── qa_report.md
│   └── logs/
└── requirements.txt
```

---

## Status & Next Steps

- **Current Status**: Fully operational, agents tested
- **Production Ready**: Yes, for single-book publishing
- **Scaling Capability**: Can process multiple books in parallel with workflow management
- **Next Enhancements**: Batch processing, multi-format output (ePub, MOBI), cover design automation

## Related References

-  (DALL-E 3 integration)
- 
- 
- 

---

**Last Review**: 2026-04-29
**System Status**: Production Ready
**Version**: 1.0
**Maintenance**: Ongoing improvements to image quality and PDF optimization
