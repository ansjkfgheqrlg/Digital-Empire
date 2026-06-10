"""
parse_manuscript.py — Parser del manoscritto Markdown

Estrae la struttura del libro da un file manuscript.md:
- Lista capitoli (numero, titolo)
- Per ogni capitolo: sottotitoli e paragrafi
- Converte Markdown in HTML per WeasyPrint

Uso:
    from scripts.parse_manuscript import parse_manuscript
    chapters = parse_manuscript('input/manuscript.md')
"""

import re
import html
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Section:
    """Sottosezione di un capitolo (heading ##)"""
    title: str
    paragraphs: List[str] = field(default_factory=list)


@dataclass
class Chapter:
    """Un capitolo del libro"""
    number: int
    title: str
    sections: List[Section] = field(default_factory=list)
    image_path: Optional[str] = None
    toc_page: int = 0  # numero pagina per l'indice (stimato)
    html_content: str = ""  # HTML già renderizzato


def _clean_dashes(text: str) -> str:
    """Rimuove em-dash e en-dash dal testo (REGOLA: nessun trattino)."""
    text = text.replace(' \u2014 ', ', ').replace(' \u2013 ', ', ')
    text = text.replace('\u2014', ' ').replace('\u2013', ' ')
    return text


def _inline_markdown_to_html(text: str) -> str:
    """
    Converte elementi Markdown inline in HTML:
    - **testo** → <strong>testo</strong>
    - *testo* o _testo_ → <em>testo</em>
    - ***testo*** → <strong><em>testo</em></strong>
    """
    # Bold+italic: ***text*** o ___text___
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'___(.+?)___', r'<strong><em>\1</em></strong>', text)

    # Bold: **text** o __text__
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)

    # Italic: *text* o _text_
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)

    return text


def _paragraph_to_html(text: str) -> str:
    """
    Converte un paragrafo di testo in HTML <p>.
    Gestisce anche liste non ordinate e ordinate.
    """
    text = text.strip()
    if not text:
        return ""

    # Controlla se è un separatore --- (ignorato, già gestito nel parser)
    if re.match(r'^-{3,}$', text):
        return ""

    # Testo normale → paragrafo
    converted = _inline_markdown_to_html(text)
    return f"<p>{converted}</p>"


def _section_to_html(section: Section) -> str:
    """Converte una Section in HTML (h2 + paragrafi)"""
    parts = []

    if section.title:
        title_html = _inline_markdown_to_html(html.escape(section.title))
        parts.append(f"<h2>{title_html}</h2>")

    for para_text in section.paragraphs:
        # Controlla se è una lista
        lines = para_text.strip().split('\n')
        is_unordered_list = all(
            re.match(r'^[\-\*\+]\s+', line.strip()) or not line.strip()
            for line in lines if line.strip()
        )
        is_ordered_list = all(
            re.match(r'^\d+\.\s+', line.strip()) or not line.strip()
            for line in lines if line.strip()
        )

        if is_unordered_list and any(
            re.match(r'^[\-\*\+]\s+', line.strip()) for line in lines
        ):
            items_html = ""
            for line in lines:
                line = line.strip()
                if re.match(r'^[\-\*\+]\s+', line):
                    item_text = re.sub(r'^[\-\*\+]\s+', '', line)
                    item_html = _inline_markdown_to_html(item_text)
                    items_html += f"<li>{item_html}</li>\n"
            if items_html:
                parts.append(f"<ul>\n{items_html}</ul>")

        elif is_ordered_list and any(
            re.match(r'^\d+\.\s+', line.strip()) for line in lines
        ):
            items_html = ""
            for line in lines:
                line = line.strip()
                if re.match(r'^\d+\.\s+', line):
                    item_text = re.sub(r'^\d+\.\s+', '', line)
                    item_html = _inline_markdown_to_html(item_text)
                    items_html += f"<li>{item_html}</li>\n"
            if items_html:
                parts.append(f"<ol>\n{items_html}</ol>")

        else:
            # Paragrafo normale
            para_html = _paragraph_to_html(para_text)
            if para_html:
                parts.append(para_html)

    return "\n".join(parts)


def _chapter_to_html(chapter: Chapter) -> str:
    """Converte l'intero contenuto testuale di un capitolo in HTML"""
    parts = []
    for section in chapter.sections:
        section_html = _section_to_html(section)
        if section_html:
            parts.append(section_html)
    return "\n\n".join(parts)


def parse_manuscript(manuscript_path: str) -> List[Chapter]:
    """
    Parsa il file manuscript.md e restituisce una lista di Chapter.

    Il formato atteso:
      # Capitolo N: Titolo    ← inizio capitolo
      ## Sottotitolo           ← inizio sezione
      testo...

    Args:
        manuscript_path: percorso al file manuscript.md

    Returns:
        Lista di Chapter ordinati per numero
    """
    path = Path(manuscript_path)
    if not path.exists():
        raise FileNotFoundError(f"Manoscritto non trovato: {manuscript_path}")

    content = path.read_text(encoding='utf-8')
    lines = content.splitlines()

    chapters: List[Chapter] = []
    current_chapter: Optional[Chapter] = None
    current_section: Optional[Section] = None
    current_paragraph_lines: List[str] = []

    def flush_paragraph():
        """Salva il paragrafo corrente nella sezione corrente"""
        nonlocal current_paragraph_lines
        if current_section is not None and current_paragraph_lines:
            non_empty = [l for l in current_paragraph_lines if l.strip()]
            if not non_empty:
                current_paragraph_lines = []
                return

            # Se tutte le righe sono elementi di lista, preserva i \n
            # così _section_to_html può renderle come lista corretta
            is_list = all(
                re.match(r'^[\-\*\+]\s+', l.strip())
                or re.match(r'^\d+[\.\)]\s+', l.strip())
                for l in non_empty
            )
            if is_list:
                para_text = "\n".join(non_empty)
            else:
                para_text = " ".join(non_empty).strip()

            # REGOLA: nessun trattino/dash nel testo finale (vale per tutti i tipi)
            para_text = _clean_dashes(para_text)

            if para_text:
                current_section.paragraphs.append(para_text)
        current_paragraph_lines = []

    def flush_section():
        """Salva la sezione corrente nel capitolo corrente"""
        nonlocal current_section
        flush_paragraph()
        if current_chapter is not None and current_section is not None:
            # Aggiungi solo se ha contenuto
            if current_section.title or current_section.paragraphs:
                current_chapter.sections.append(current_section)
        current_section = None

    for line in lines:
        stripped = line.strip()

        # Titolo capitolo: # Capitolo N: Titolo
        chapter_match = re.match(
            r'^#\s+Capitolo\s+(\d+)\s*[:\-]\s*(.+)$',
            stripped,
            re.IGNORECASE
        )
        if chapter_match:
            # Finalizza capitolo precedente
            flush_section()
            if current_chapter is not None:
                current_chapter.html_content = _chapter_to_html(current_chapter)
                chapters.append(current_chapter)

            chapter_num = int(chapter_match.group(1))
            chapter_title = _clean_dashes(chapter_match.group(2).strip())
            current_chapter = Chapter(number=chapter_num, title=chapter_title)
            current_section = Section(title="")  # sezione anonima iniziale
            continue

        # Titolo H1 generico (non capitolo)
        h1_match = re.match(r'^#\s+(.+)$', stripped)
        if h1_match and not chapter_match:
            flush_section()
            if current_chapter is None:
                # Potrebbe essere il titolo del libro — ignora
                continue
            current_section = Section(title=h1_match.group(1).strip())
            continue

        # Sottotitolo H2
        h2_match = re.match(r'^##\s+(.+)$', stripped)
        if h2_match:
            flush_section()
            if current_chapter is not None:
                current_section = Section(title=_clean_dashes(h2_match.group(1).strip()))
            continue

        # Sottotitolo H3
        h3_match = re.match(r'^###\s+(.+)$', stripped)
        if h3_match:
            flush_paragraph()
            if current_section is not None:
                h3_text = _clean_dashes(h3_match.group(1).strip())
                current_section.paragraphs.append(f"__H3__{h3_text}")
            continue

        # Separatore ---
        if re.match(r'^-{3,}$', stripped):
            flush_paragraph()
            continue

        # Riga vuota — fine paragrafo
        if not stripped:
            flush_paragraph()
            continue

        # Riga di testo — accumula nel paragrafo corrente
        if current_chapter is not None and current_section is not None:
            current_paragraph_lines.append(stripped)

    # Finalizza l'ultimo capitolo
    flush_section()
    if current_chapter is not None:
        current_chapter.html_content = _chapter_to_html(current_chapter)
        chapters.append(current_chapter)

    # Ordina per numero capitolo
    chapters.sort(key=lambda c: c.number)

    return chapters


def estimate_toc_pages(chapters: List[Chapter]) -> List[Chapter]:
    """
    Stima i numeri di pagina per l'indice.
    Ogni capitolo occupa: 2 (immagine+titolo) + testo stimato
    Le prime 4 pagine sono preliminari.

    Questa è una stima approssimativa — WeasyPrint assegnerà i numeri reali.
    """
    # Pagine preliminari: frontespizio, copyright, indice, bianca = 4
    current_page = 5  # Capitolo 1 inizia a pagina 5 (dispari)

    for chapter in chapters:
        # Assicura che cada su pagina dispari
        if current_page % 2 == 0:
            current_page += 1

        chapter.toc_page = current_page

        # Stima pagine: 2 (immagine + titolo) + testo
        # Stimiamo ~3000 caratteri per pagina
        total_chars = sum(
            sum(len(p) for p in s.paragraphs) + len(s.title)
            for s in chapter.sections
        )
        text_pages = max(2, total_chars // 2500)
        current_page += 2 + text_pages  # immagine + titolo + testo

    return chapters


if __name__ == "__main__":
    # Test rapido
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "input/manuscript.md"

    try:
        chapters = parse_manuscript(path)
        chapters = estimate_toc_pages(chapters)

        print(f"Trovati {len(chapters)} capitoli:\n")
        for ch in chapters:
            total_sections = len(ch.sections)
            total_paras = sum(len(s.paragraphs) for s in ch.sections)
            print(f"  Cap. {ch.number:02d}: '{ch.title}'")
            print(f"    Sezioni: {total_sections}, Paragrafi: {total_paras}")
            print(f"    Pagina stimata indice: {ch.toc_page}")
            print()
    except FileNotFoundError as e:
        print(f"Errore: {e}")
        sys.exit(1)
