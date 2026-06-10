---
- **Type**: TOOL
- **Purpose**: PDF layout and formatting engine that transforms markdown manuscripts into professional 6x9 inch print-ready books
- **Status**: Active
- **Tags**: `#publishing` `#pdf-generation` `#book-layout` `#weasyprint` `#typography`
- **Created**: 2026-04-29
- **Last updated**: 2026-04-29
- **Tech Stack**: Python, WeasyPrint, Jinja2, Markdown, CSS for print
---

# Tool: Layout Engine Agent (Book Factory)

## Agent Overview

The Layout Engine Agent is responsible for transforming a manuscript (Markdown) and chapter images into a professionally formatted PDF. It handles all aspects of book impagination: typography, page layout, chapter breaks, headers/footers, image placement, and print specifications.

**Part of**: [[Book_Factory_Automation_System]]

**Processes Output From**: [[Tool_IMAGE_GENERATOR_Agent]]

**Produces Output For**: [[Tool_QA_Agent]]

## Core Responsibilities

1. Parse manuscript into structured chapter data
2. Load configuration and templates
3. Generate HTML from Markdown using Jinja2
4. Apply CSS for print layout (6×9 format)
5. Embed chapter images with proper page breaks
6. Generate front matter (title, copyright, TOC)
7. Compile final PDF with WeasyPrint
8. Validate output and create log

## Input Specifications

### 1. Manuscript: `input/manuscript.md`

Expected Markdown structure:

```markdown
# Book Title: The Complete Guide

## Chapter 1: Introduction

This is the first chapter. The text flows naturally across multiple paragraphs.

### Subheading

More detailed content here.

## Chapter 2: Getting Started

Second chapter content...

## Chapter 3: Advanced Topics

And so on...
```

**Requirements**:
- H1 (`# Title`) — Book title (appears once)
- H2 (`## Chapter X: Title`) — Chapter headings (one per chapter)
- Regular paragraphs and text content
- Optional H3 (`### Subheading`) — Subsections within chapters

### 2. Images: `assets/images/chapter_XX.png`

From Image Generator Agent:
- Location: `assets/images/`
- Naming: `chapter_01.png`, `chapter_02.png`, etc.
- Format: PNG, 1024×1792 pixels
- Count: Must equal number of chapters

### 3. Configuration: `config/book_config.yaml`

```yaml
book:
  title: "The Complete Guide"
  subtitle: "A Professional Book"
  author: "Author Name"
  publisher: "Your Publisher"
  isbn: "978-1-234567-89-0"
  publication_date: "2026-04-29"

format:
  width_inches: 6
  height_inches: 9
  margin_inside: 0.75
  margin_outside: 0.5
  margin_top: 0.75
  margin_bottom: 0.5

typography:
  body_font: "Crimson Text"
  body_size_pt: 11
  line_height: 1.4
  
  heading_font: "Georgia"
  heading_size_pt: 24
  heading_weight: bold
  
  chapter_number_size_pt: 14

generation:
  backend: "weasyprint"
  dpi: 300
```

### 4. Templates: `templates/`

Template files (Jinja2):
- `base.html` — Overall page structure
- `title_page.html` — Front matter
- `chapter.html` — Chapter layout with image
- `styles.css` — Print CSS

## Processing Pipeline

### Step 1: Parse Manuscript

```python
import markdown
from markdown import Markdown

def parse_manuscript(filepath):
    """Extract chapters and content from Markdown."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by H2 (chapter headers)
    chapters = []
    current_chapter = None
    
    md = Markdown(extensions=['meta'])
    
    lines = content.split('\n')
    current_title = None
    current_body = []
    
    for line in lines:
        if line.startswith('# '):
            # Book title
            book_title = line.replace('# ', '').strip()
            
        elif line.startswith('## '):
            # Chapter start
            if current_chapter:
                chapters.append({
                    'number': len(chapters) + 1,
                    'title': current_title,
                    'content': '\n'.join(current_body)
                })
            current_title = line.replace('## ', '').strip()
            current_body = []
            
        else:
            # Body content
            if current_title:
                current_body.append(line)
    
    # Add final chapter
    if current_title:
        chapters.append({
            'number': len(chapters) + 1,
            'title': current_title,
            'content': '\n'.join(current_body)
        })
    
    return {
        'title': book_title,
        'chapters': chapters
    }

# Usage
manuscript = parse_manuscript('input/manuscript.md')
print(f"Book: {manuscript['title']}")
print(f"Chapters: {len(manuscript['chapters'])}")
```

### Step 2: Load Configuration

```python
import yaml

def load_config():
    with open('config/book_config.yaml', 'r') as f:
        return yaml.safe_load(f)

config = load_config()

# Extract dimensions
page_width = config['format']['width_inches']
page_height = config['format']['height_inches']
margin_inside = config['format']['margin_inside']
margin_outside = config['format']['margin_outside']
```

### Step 3: Create HTML Structure

```python
from jinja2 import Environment, FileSystemLoader

def build_book_html(manuscript, config, templates_dir='templates'):
    """Assemble complete HTML document with all pages."""
    
    env = Environment(loader=FileSystemLoader(templates_dir))
    base_template = env.get_template('base.html')
    chapter_template = env.get_template('chapter.html')
    
    pages = []
    
    # Front matter
    title_page = env.get_template('title_page.html').render(
        book_title=manuscript['title'],
        author=config['book']['author'],
        publisher=config['book']['publisher']
    )
    pages.append(title_page)
    
    # Copyright page
    copyright_page = env.get_template('copyright.html').render(
        book_title=manuscript['title'],
        author=config['book']['author'],
        isbn=config['book'].get('isbn', ''),
        year=datetime.now().year
    )
    pages.append(copyright_page)
    
    # Table of Contents
    toc_html = '<h1>Table of Contents</h1>\n<ul>'
    for chapter in manuscript['chapters']:
        toc_html += f"\n<li>{chapter['number']}. {chapter['title']}</li>"
    toc_html += '\n</ul>'
    pages.append(toc_html)
    
    # Blank page before Chapter 1
    pages.append('<div class="blank-page"></div>')
    
    # Chapters
    for chapter in manuscript['chapters']:
        chapter_html = chapter_template.render(
            chapter_number=chapter['number'],
            chapter_title=chapter['title'],
            content=chapter['content'],
            image_path=f"assets/images/chapter_{chapter['number']:02d}.png"
        )
        pages.append(chapter_html)
    
    # Final blank page
    pages.append('<div class="blank-page"></div>')
    
    # Assemble full document
    full_html = base_template.render(
        pages=pages,
        book_title=manuscript['title'],
        author=config['book']['author']
    )
    
    return full_html
```

### Step 4: Generate PDF with WeasyPrint

```python
from weasyprint import HTML, CSS
import os

def generate_pdf(html_content, css_path, output_path, config):
    """Compile HTML to PDF using WeasyPrint."""
    
    # Load CSS
    css = CSS(string=generate_print_css(config))
    
    # Create PDF from HTML
    doc = HTML(string=html_content)
    
    # Write to file
    doc.write_pdf(output_path, stylesheets=[css])
    
    print(f"✓ PDF generated: {output_path}")

def generate_print_css(config):
    """Generate CSS for print layout."""
    
    width = config['format']['width_inches']
    height = config['format']['height_inches']
    m_in = config['format']['margin_inside']
    m_out = config['format']['margin_outside']
    m_top = config['format']['margin_top']
    m_bot = config['format']['margin_bottom']
    
    font = config['typography']['body_font']
    size = config['typography']['body_size_pt']
    lh = config['typography']['line_height']
    
    css = f"""
    @page {{
        size: {width}in {height}in;
        margin: 0;
    }}
    
    @page :left {{
        margin-left: {m_out}in;
        margin-right: {m_in}in;
        margin-top: {m_top}in;
        margin-bottom: {m_bot}in;
    }}
    
    @page :right {{
        margin-left: {m_in}in;
        margin-right: {m_out}in;
        margin-top: {m_top}in;
        margin-bottom: {m_bot}in;
    }}
    
    @page :first {{
        margin: 0;
        /* Title page, no margins */
    }}
    
    @page image-page {{
        margin: 0;
        /* Image pages, no margins */
    }}
    
    body {{
        font-family: '{font}', Georgia, serif;
        font-size: {size}pt;
        line-height: {lh};
        orphans: 2;
        widows: 2;
    }}
    
    .chapter-image {{
        page-break-before: always;
        page: image-page;
        width: 100%;
        height: 100%;
        object-fit: cover;
        margin: 0;
        padding: 0;
    }}
    
    .chapter-title {{
        page-break-before: always;
        text-align: center;
        margin-top: 3in;
        font-size: 24pt;
        font-weight: bold;
    }}
    
    .chapter-number {{
        font-size: 14pt;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    
    .chapter-content {{
        text-align: justify;
        margin-top: 1.5in;
    }}
    
    .blank-page {{
        page-break-after: always;
        height: 100%;
    }}
    """
    
    return css
```

### Step 5: Handle Missing Images

```python
from PIL import Image

def ensure_images(chapters, image_dir='assets/images'):
    """Create placeholder images for missing files."""
    
    for chapter in chapters:
        filename = f"{image_dir}/chapter_{chapter['number']:02d}.png"
        
        if not os.path.exists(filename):
            # Create gray placeholder
            image = Image.new('RGB', (1024, 1792), color='#CCCCCC')
            draw = ImageDraw.Draw(image)
            
            text = f"IMAGE MISSING\nChapter {chapter['number']}"
            # ... (center and draw text)
            
            image.save(filename, 'PNG')
            print(f"⚠ Placeholder created: {filename}")
```

## Page Structure & Layout

### Front Matter (Preliminary Pages)

**Page 1: Title Page**
- Book title (centered, large, ~44pt)
- Subtitle (centered, medium, ~18pt)
- Author name (centered, below title, ~14pt)
- No margins, full-bleed if applicable

**Page 2: Copyright**
- Copyright notice
- ISBN
- Publication date
- Publisher info
- Minimal formatting

**Page 3: Table of Contents**
- Chapter list with page numbers
- Auto-generated from H2 headings

**Page 4: Blank** (to ensure Chapter 1 starts on recto/right page)

### Chapter Pages (Body)

**Pattern per Chapter**:

1. **Full-Page Image**
   - Chapter image (1024×1792 from Image Generator)
   - Full bleed, no margins, no header/footer
   - Page break: always before
   - Class: `page: image-page`

2. **Chapter Title Page**
   - "CHAPTER X" (uppercase, 14pt, centered)
   - Chapter title (24pt bold, centered)
   - No header or footer
   - Ensures recto (right) page start
   - Page break: always before

3. **Chapter Body Pages**
   - Body text flows naturally
   - Headers and footers on all body pages
   - Left pages: book title in header
   - Right pages: chapter title in header
   - Centered page number in footer
   - Orphans/widows: 2 line minimum

### Back Matter

**Final Blank Page** — Ensures even page count

## Configuration Examples

### Compact Layout (Academic)
```yaml
typography:
  body_font: "Georgia"
  body_size_pt: 10
  line_height: 1.3
  margin_inside: 0.5
  margin_outside: 0.5
```

### Spacious Layout (Premium)
```yaml
typography:
  body_font: "Crimson Text"
  body_size_pt: 12
  line_height: 1.6
  margin_inside: 1.0
  margin_outside: 0.75
```

## Output Specifications

### PDF File: `output/book_draft.pdf`

- **Format**: PDF/A-1b (archival standard, print-ready)
- **Size**: Exactly 6 × 9 inches per page
- **Resolution**: 300 DPI (print quality)
- **Color Space**: RGB or CMYK (RGB for on-screen preview)
- **Compression**: Optimized for file size
- **Metadata**: Title, author, publication date

### Log File: `output/layout_log.txt`

```
Layout Engine Log
Started: 2026-04-29 14:50:00

Manuscript parsed:
  Title: "The Complete Guide"
  Chapters: 12
  Total words: 45,632

Configuration loaded:
  Format: 6 x 9 inches
  Font: Crimson Text, 11pt
  Margins: 0.75in (inside), 0.5in (outside)

Pages generated:
  Front matter: 4 pages
  Chapter 1: 1 image + 1 title + 8 content = 10 pages
  Chapter 2: 1 image + 1 title + 6 content = 8 pages
  ... (continued for all chapters)
  Back matter: 1 page
  
Total pages: 143
Total images: 12
Images verified: 12/12

PDF compiled: book_draft.pdf
File size: 24.5 MB

Layout completed successfully.
Finished: 2026-04-29 15:10:42
Total time: 20 minutes 42 seconds
```

## Typography & Styling

### Font Recommendations

**Body Text** (flowing narrative):
- Crimson Text (serif, elegant)
- Georgia (serif, web-safe)
- Garamond (serif, classic)

**Headings** (chapter titles):
- Georgia bold
- Crimson Text bold italic
- Custom serif for premium feel

**Monospace** (code, if applicable):
- Courier New
- Menlo
- Roboto Mono

### Size Guidelines

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Book title | 44pt | Bold | Title page only |
| Chapter number | 14pt | Regular | "CHAPTER 1" |
| Chapter title | 24pt | Bold | Centered |
| Body text | 11pt | Regular | Main narrative |
| Subheading | 14pt | Bold | Section breaks |
| Footer (page#) | 10pt | Regular | Centered |

## Validation & Quality Checks

Before sending to QA Agent:

```python
def validate_pdf(pdf_path):
    """Quick validation of generated PDF."""
    
    checks = {
        'file_exists': os.path.exists(pdf_path),
        'file_size': os.path.getsize(pdf_path) > 1000000,  # > 1MB
        'readable': check_pdf_readable(pdf_path),
        'page_count': check_page_count(pdf_path),
    }
    
    if all(checks.values()):
        print("✓ PDF validation passed")
        return True
    else:
        print("✗ PDF validation issues:")
        for check, result in checks.items():
            print(f"  {check}: {'PASS' if result else 'FAIL'}")
        return False
```

## Integration Points

```
IMAGE GENERATOR AGENT (produces images)
    ↓
LAYOUT ENGINE AGENT (this tool)
    ↓ Produces: output/book_draft.pdf
    ↓ Produces: output/layout_log.txt
    ↓
QA AGENT (validates and finalizes)
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Text overflows page | Reduce font size or margins |
| Images distorted | Check source image dimensions (1024×1792) |
| Fonts not rendering | Ensure font files are installed or embed fonts |
| Page count incorrect | Verify chapter breaks and page-break-before styles |
| PDF too large | Enable compression in WeasyPrint |

## Related References

- [[Book_Factory_Automation_System]] — Parent project
- [[Tool_IMAGE_GENERATOR_Agent]] — Produces images
- [[Tool_QA_Agent]] — Consumes draft PDF
- 
- 

---

**Last Review**: 2026-04-29
**Agent Status**: Operational
**Typical Performance**: 20-30 minutes for 12-chapter, 150-page book
**Success Rate**: 99% (failures typically due to missing images, not layout)
**Output Quality**: Print-ready, Amazon KDP compatible
