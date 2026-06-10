"""
build_book.py — Agente 2: Layout Engine

Costruisce il PDF 6x9 del libro a partire da:
- input/manuscript.md
- assets/images/chapter_XX.png
- config/book_config.yaml
- templates/

Output: output/book_draft.pdf

Uso:
    python scripts/build_book.py
"""

import os
import sys
import yaml
import logging
from pathlib import Path

# Aggiungi la directory root al path per import relativi
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from scripts.parse_manuscript import parse_manuscript, estimate_toc_pages, Chapter

# ── Logging ───────────────────────────────────────────────────────────────────

os.makedirs(ROOT / "output", exist_ok=True)

import io as _io

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(
            _io.open(sys.stdout.fileno(), mode="w", encoding="utf-8",
                     errors="replace", closefd=False, buffering=1)
        ),
        logging.FileHandler(ROOT / "output" / "layout_log.txt", encoding="utf-8"),
    ]
)
log = logging.getLogger("build_book")


# ── Utilities ─────────────────────────────────────────────────────────────────

def load_config(config_path: str) -> dict:
    """Carica la configurazione del libro"""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_css(templates_dir: Path) -> str:
    """Carica il file CSS"""
    css_path = templates_dir / "styles.css"
    if css_path.exists():
        return css_path.read_text(encoding="utf-8")
    log.warning("styles.css non trovato — uso CSS minimo")
    return _minimal_css()


def _minimal_css() -> str:
    """CSS minimo di fallback se styles.css non è disponibile"""
    return """
    @page { size: 6in 9in; margin: 0.75in 0.5in 0.5in 0.75in; }
    body { font-family: Georgia, serif; font-size: 11pt; line-height: 1.4; }
    h1 { font-size: 24pt; font-weight: bold; }
    h2 { font-size: 14pt; font-weight: bold; margin-top: 18pt; }
    p  { text-indent: 0.3in; margin: 0; text-align: justify; orphans: 2; widows: 2; }
    .image-page { page-break-before: always; page-break-after: always; }
    .image-page img { width: 100%; height: 100%; object-fit: cover; }
    """


def find_chapter_image(chapter_num: int, images_dir: Path) -> str | None:
    """
    Cerca l'immagine per un capitolo nelle possibili varianti di nome.
    Restituisce il percorso assoluto come stringa URI, o None.
    """
    patterns = [
        f"chapter_{chapter_num:02d}.png",
        f"chapter_{chapter_num}.png",
        f"chapter_{chapter_num:02d}.jpg",
        f"chapter_{chapter_num}.jpg",
        f"chapter_{chapter_num:02d}.jpeg",
    ]
    for pattern in patterns:
        img_path = images_dir / pattern
        if img_path.exists():
            # WeasyPrint richiede percorso assoluto come URI file://
            return img_path.as_uri()
    return None


# ── HTML Builder ──────────────────────────────────────────────────────────────

def build_title_page(config: dict) -> str:
    """Genera HTML del frontespizio"""
    book = config["book"]
    return f"""
<div class="title-page">
    <div class="book-title">{book['title']}</div>
    <div class="title-divider"></div>
    <div class="book-subtitle">{book.get('subtitle', '')}</div>
    <div class="title-divider"></div>
    <div class="book-author">{book['author']}</div>
</div>
"""


def build_copyright_page(config: dict) -> str:
    """Genera HTML della pagina copyright"""
    book = config["book"]
    return f"""
<div class="copyright-page">
    <p>Copyright &copy; {book['year']} {book['author']}</p>
    <p>Tutti i diritti riservati.</p>
    <p>Nessuna parte di questa pubblicazione pu&ograve; essere riprodotta,
    distribuita o trasmessa in qualsiasi forma o con qualsiasi mezzo,
    incluse fotocopie, registrazioni o altri metodi elettronici o meccanici,
    senza il previo consenso scritto dell&rsquo;autore.</p>
    <p>&nbsp;</p>
    <p>Prima edizione: {book['year']}</p>
    <p>&nbsp;</p>
    <p>Stampato e distribuito tramite Amazon KDP</p>
</div>
"""


def build_toc(chapters: list) -> str:
    """Genera HTML dell'indice"""
    entries = ""
    for ch in chapters:
        entries += f"""
    <div class="toc-entry">
        <div>
            <span class="toc-chapter-num">Capitolo {ch.number}</span>
            <span class="toc-title">{ch.title}</span>
        </div>
        <span class="toc-dots"></span>
        <span class="toc-page-num">{ch.toc_page}</span>
    </div>
"""
    return f"""
<div class="toc-page">
    <h2 class="no-indent center">Indice</h2>
    {entries}
</div>
"""


def build_image_page(chapter: Chapter) -> str:
    """Genera HTML della pagina immagine (full-page)"""
    if chapter.image_path:
        img_tag = (
            f'<img src="{chapter.image_path}" '
            f'alt="Capitolo {chapter.number}: {chapter.title}">'
        )
    else:
        img_tag = f"""
        <div class="image-placeholder">
            <p>IMMAGINE MANCANTE<br>Capitolo {chapter.number}<br>{chapter.title}</p>
        </div>"""

    return f"""
<div class="image-page">
    {img_tag}
</div>
"""


def build_chapter_title_page(chapter: Chapter) -> str:
    """Genera HTML della pagina titolo del capitolo"""
    return f"""
<div class="chapter-title-page">
    <div class="chapter-number">Capitolo {chapter.number}</div>
    <div class="chapter-number-divider"></div>
    <h1 class="chapter-title">{chapter.title}</h1>
</div>
"""


def build_chapter_content(chapter: Chapter) -> str:
    """Genera HTML del contenuto testuale del capitolo"""
    if chapter.html_content:
        return f'<div class="chapter-content">\n{chapter.html_content}\n</div>'
    return '<div class="chapter-content"><p>(capitolo vuoto)</p></div>'


def build_complete_html(config: dict, chapters: list, css: str) -> str:
    """
    Assembla l'HTML completo del libro:
    frontespizio → copyright → indice → capitoli
    """
    book = config["book"]

    # Costruisci ogni sezione
    title_html = build_title_page(config)
    copyright_html = build_copyright_page(config)
    toc_html = build_toc(chapters)

    # Pagina bianca (per far iniziare Cap. 1 su pagina dispari)
    blank_page = '<div class="blank-page"></div>'

    # Capitoli
    chapters_html_parts = []
    for chapter in chapters:
        img_page = build_image_page(chapter)
        title_page = build_chapter_title_page(chapter)
        content = build_chapter_content(chapter)
        chapters_html_parts.append(img_page + title_page + content)

    chapters_html = "\n\n".join(chapters_html_parts)

    # Pagina finale bianca
    final_blank = '<div class="blank-page"></div>'

    return f"""<!DOCTYPE html>
<html lang="{book.get('language', 'it')}">
<head>
    <meta charset="UTF-8">
    <meta name="author" content="{book['author']}">
    <title>{book['title']}</title>
    <style>
{css}
    </style>
</head>
<body>

<!-- Stringa nascosta per header "titolo libro" -->
<span class="book-title-string">{book['title']}</span>

{title_html}

{copyright_html}

{toc_html}

{blank_page}

{chapters_html}

{final_blank}

</body>
</html>"""


# ── PDF Builder ───────────────────────────────────────────────────────────────

def build_pdf(html_content: str, output_path: str, base_url: str = None) -> bool:
    """
    Converte HTML in PDF usando WeasyPrint.
    Se WeasyPrint non è disponibile (mancano le GTK libs su Windows),
    usa automaticamente il backend ReportLab come fallback.
    Restituisce True se successo, False se errore.
    """
    # Tenta prima con WeasyPrint
    try:
        from weasyprint import HTML as WP_HTML
        from weasyprint.text.fonts import FontConfiguration

        font_config = FontConfiguration()

        if base_url is None:
            base_url = ROOT.as_uri() + "/"

        log.info("Avvio generazione PDF con WeasyPrint...")
        log.info(f"Base URL: {base_url}")

        wp = WP_HTML(
            string=html_content,
            base_url=base_url,
        )
        wp.write_pdf(
            output_path,
            font_config=font_config,
        )
        log.info("PDF generato con WeasyPrint")
        return True

    except ImportError:
        log.warning("WeasyPrint non installato — uso fallback ReportLab")
    except Exception as e:
        if "libgobject" in str(e) or "GTK" in str(e) or "cannot load library" in str(e):
            log.warning(
                f"WeasyPrint richiede GTK (non disponibile su questo sistema): {e}"
            )
            log.warning("Utilizzo backend ReportLab come fallback...")
        else:
            log.error(f"Errore WeasyPrint inatteso: {e}")
            log.warning("Provo con ReportLab come fallback...")

    # Fallback: ReportLab
    return _build_pdf_reportlab(output_path)


def _build_pdf_reportlab(output_path: str) -> bool:
    """
    Genera il PDF usando il backend ReportLab.
    Questo è il fallback quando WeasyPrint non è disponibile.
    """
    try:
        log.info("Avvio generazione PDF con ReportLab (fallback)...")

        # Importa e usa il modulo ReportLab dedicato
        from scripts.build_book_reportlab import main as rl_main

        # Chiama direttamente il builder
        import yaml
        config_path = ROOT / "config" / "book_config.yaml"
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        from scripts.parse_manuscript import parse_manuscript, estimate_toc_pages
        manuscript_path = ROOT / "input" / "manuscript.md"
        chapters = parse_manuscript(str(manuscript_path))
        chapters = estimate_toc_pages(chapters)

        images_dir = ROOT / "assets" / "images"

        from scripts.build_book_reportlab import build_book_with_reportlab
        build_book_with_reportlab(config, chapters, images_dir, output_path)

        log.info("PDF generato con ReportLab")
        return True

    except ImportError as e:
        log.error(f"ReportLab non disponibile: {e}. Esegui: pip install reportlab")
        return False
    except Exception as e:
        log.error(f"Errore ReportLab: {e}")
        import traceback
        log.error(traceback.format_exc())
        return False


def verify_pdf(pdf_path: str) -> dict:
    """
    Verifica il PDF generato:
    - dimensioni pagina (deve essere 432x648 pt = 6x9in)
    - numero di pagine
    Restituisce dict con i risultati.
    """
    result = {
        "valid": False,
        "pages": 0,
        "correct_size": False,
        "size_details": [],
        "errors": [],
    }

    if not Path(pdf_path).exists():
        result["errors"].append(f"File non trovato: {pdf_path}")
        return result

    try:
        import pikepdf
        pdf = pikepdf.open(pdf_path)
        result["pages"] = len(pdf.pages)
        result["valid"] = True

        wrong_pages = []
        for i, page in enumerate(pdf.pages):
            try:
                mb = page.MediaBox
                w = float(mb[2]) - float(mb[0])
                h = float(mb[3]) - float(mb[1])
                result["size_details"].append((i + 1, w, h))

                # Tolleranza di 2 punti
                if not (abs(w - 432) < 2 and abs(h - 648) < 2):
                    wrong_pages.append(
                        f"Pag. {i+1}: {w:.1f}x{h:.1f}pt (atteso 432x648pt)"
                    )
            except Exception as e:
                result["errors"].append(f"Pag. {i+1}: errore lettura dimensioni — {e}")

        if not wrong_pages:
            result["correct_size"] = True
        else:
            result["errors"].extend(wrong_pages[:5])  # mostra max 5 errori

        pdf.close()

    except ImportError:
        log.warning("pikepdf non disponibile — verifica dimensioni saltata")
        result["valid"] = True
        result["correct_size"] = None  # non verificato
    except Exception as e:
        result["errors"].append(f"Errore apertura PDF: {e}")

    return result


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    log.info("=" * 60)
    log.info("AGENTE 2 — LAYOUT ENGINE — Avvio")
    log.info("=" * 60)

    # 1. Carica configurazione
    config_path = ROOT / "config" / "book_config.yaml"
    if not config_path.exists():
        log.error(f"Config non trovato: {config_path}")
        sys.exit(1)

    config = load_config(config_path)
    log.info(f"Libro: '{config['book']['title']}' di {config['book']['author']}")

    # 2. Parsa manoscritto
    manuscript_path = ROOT / "input" / "manuscript.md"
    if not manuscript_path.exists():
        log.error(f"Manoscritto non trovato: {manuscript_path}")
        sys.exit(1)

    log.info("Parsing manoscritto...")
    chapters = parse_manuscript(str(manuscript_path))
    chapters = estimate_toc_pages(chapters)
    log.info(f"Trovati {len(chapters)} capitoli")

    # 3. Associa immagini ai capitoli
    images_dir = ROOT / "assets" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    missing_images = []
    for chapter in chapters:
        img_uri = find_chapter_image(chapter.number, images_dir)
        if img_uri:
            chapter.image_path = img_uri
            log.info(f"  Cap. {chapter.number:02d}: immagine trovata → {img_uri}")
        else:
            chapter.image_path = None
            missing_images.append(chapter.number)
            log.warning(
                f"  Cap. {chapter.number:02d}: IMMAGINE MANCANTE — "
                f"verrà usato placeholder"
            )

    if missing_images:
        log.warning(
            f"Immagini mancanti per capitoli: {missing_images}. "
            f"Lanciare prima generate_images.py"
        )

    # 4. Carica CSS
    templates_dir = ROOT / "templates"
    css = load_css(templates_dir)

    # 5. Genera HTML
    log.info("Generazione HTML...")
    html_content = build_complete_html(config, chapters, css)

    # Salva HTML per debug
    html_debug_path = ROOT / "output" / "book_debug.html"
    html_debug_path.write_text(html_content, encoding="utf-8")
    log.info(f"HTML di debug salvato in: {html_debug_path}")

    # 6. Genera PDF
    output_path = ROOT / "output" / "book_draft.pdf"
    os.makedirs(ROOT / "output", exist_ok=True)

    log.info(f"Generazione PDF: {output_path}")
    success = build_pdf(html_content, str(output_path), base_url=ROOT.as_uri() + "/")

    if not success:
        log.error("Generazione PDF FALLITA")
        sys.exit(1)

    # 7. Verifica PDF
    log.info("Verifica PDF generato...")
    verification = verify_pdf(str(output_path))

    if verification["valid"]:
        log.info(f"PDF valido — Pagine totali: {verification['pages']}")
    else:
        log.error(f"PDF non valido: {verification['errors']}")

    if verification.get("correct_size") is True:
        log.info("Dimensioni pagina: OK (432x648pt = 6x9in)")
    elif verification.get("correct_size") is False:
        log.warning(f"Dimensioni pagina non corrette: {verification['errors']}")
    else:
        log.info("Dimensioni pagina: non verificate (pikepdf non disponibile)")

    # 8. Report finale
    file_size_mb = output_path.stat().st_size / (1024 * 1024)
    log.info(f"PDF generato: {output_path}")
    log.info(f"Dimensione file: {file_size_mb:.2f} MB")
    log.info(f"Pagine totali: {verification['pages']}")
    log.info("=" * 60)
    log.info("AGENTE 2 — COMPLETATO")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
