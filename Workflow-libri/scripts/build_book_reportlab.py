"""
build_book_reportlab.py — Layout Engine (backend ReportLab)

Genera output/book_draft.pdf in formato 6x9 pollici.

═══════════════════════════════════════════════════════
REGOLE LAYOUT — APPLICATE OVUNQUE, SENZA ECCEZIONI
═══════════════════════════════════════════════════════

1. NESSUN OVERFLOW
   Ogni riga di testo verifica lo spazio disponibile PRIMA di essere
   disegnata. Se non c'è spazio → nuova pagina automatica.
   Nessun paragrafo, voce di lista o titolo può sforare il margine
   inferiore, nemmeno se è un singolo paragrafo lungo un'intera pagina.

2. NESSUN ORFANO
   Un heading (h2) richiede sempre almeno MIN_LINES_AFTER_HEADING righe
   di corpo testo dopo di sé. Se non c'è spazio sufficiente, l'heading
   si sposta alla pagina successiva. MAI un titolo da solo in fondo pagina.

3. NESSUN TRATTINO ARTIFICIALE
   • Le parole non vengono mai spezzate con un trattino (no hyphenation).
   • I ritorni a capo avvengono SOLO agli spazi tra le parole.
   • La giustificazione è CAP-pata: lo spazio extra per gap non supera
     MAX_EXTRA_SPACE_FACTOR × larghezza-spazio-normale. Righe con poche
     parole NON vengono iper-giustificate (sembrano trattini).
   • Le liste (ordinate e non) sono renderizzate come bullet/numeri,
     non come paragrafo unico con "2." e "3." in mezzo al testo.

4. NESSUN OVERLAP
   Il layout di ogni pagina è calcolato top-down con altezze pre-misurate.
   Nessun elemento può sovrapporsi a un altro.
   Le pagine titolo-capitolo calcolano prima l'altezza di ogni elemento,
   poi posizionano dall'alto verso il basso.

Uso:
    python scripts/build_book_reportlab.py
"""

import os
import sys
import re
import yaml
import logging
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from scripts.parse_manuscript import parse_manuscript, estimate_toc_pages

import io as _io

os.makedirs(ROOT / "output", exist_ok=True)

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
log = logging.getLogger("build_book_rl")


# ── Costanti pagina — conformi Amazon KDP 6×9 ────────────────────────────────
#
# Fonte: Amazon KDP Paperback Manuscript Formatting Guidelines
# https://kdp.amazon.com/en_US/help/topic/G201834180
#
# REQUISITI KDP MINIMI per 6×9" (pagine 24-150):
#   Gutter (interno):  0.375" (27 pt) — noi usiamo 0.75" (54 pt)  ✓
#   Margine esterno:   0.250" (18 pt) — noi usiamo 0.500" (36 pt)  ✓
#   Margine top:       0.250" (18 pt) — noi usiamo 0.750" (54 pt)  ✓
#   Margine bottom:    0.250" (18 pt) — noi usiamo 0.500" (36 pt)  ✓
#
# ZONA DI SICUREZZA KDP: nessun testo entro 0.25" (18 pt) da qualsiasi bordo.
# Tutti i margini sopra sono al di sopra di questo requisito.
#
# REGOLA PRIMARIA: il testo (incluso header/footer) non deve MAI superare
# i margini. Il lato DESTRO della riga più lunga deve essere ≤ RIGHT_EDGE_ODD
# (pagine dispari) o ≤ RIGHT_EDGE_EVEN (pagine pari).

PAGE_W = 6 * 72   # 432 pt
PAGE_H = 9 * 72   # 648 pt

MARGIN_TOP    = int(0.75 * 72)  # 54 pt  (0.75" — ampiamente sopra KDP min 0.25")
MARGIN_BOTTOM = int(0.50 * 72)  # 36 pt  (0.50" — sopra KDP min 0.25")
MARGIN_INNER  = int(0.75 * 72)  # 54 pt  (0.75" — sopra KDP min 0.375" per ≤150 pag.)
MARGIN_OUTER  = int(0.50 * 72)  # 36 pt  (0.50" — sopra KDP min 0.25")

# Area di testo (uguale per entrambe le pagine — simmetrica nella larghezza totale)
CONTENT_W = PAGE_W - MARGIN_INNER - MARGIN_OUTER  # 342 pt (4.75")
CONTENT_H = PAGE_H - MARGIN_TOP  - MARGIN_BOTTOM  # 558 pt (7.75")

# Bordi DESTRI assoluti della zona testo (punto massimo del testo su ogni riga)
# NESSUN testo può mai superare questi valori.
RIGHT_EDGE_ODD  = PAGE_W - MARGIN_OUTER  # 396 pt  (pagine dispari: gutter a SX)
RIGHT_EDGE_EVEN = PAGE_W - MARGIN_INNER  # 378 pt  (pagine pari:   gutter a DX)

# Bordi SINISTRI assoluti della zona testo
MARGIN_LEFT_ODD  = MARGIN_INNER  # 54 pt  (pagine dispari)
MARGIN_LEFT_EVEN = MARGIN_OUTER  # 36 pt  (pagine pari)

# Font sizes
BODY_FONT_SIZE   = 11     # 11pt corpo — leggibile e professionale
BODY_LEADING     = 16.5   # interlinea 1.5x (16.5pt a 11pt)

CHAPTER_TITLE_SIZE = 24
CHAPTER_NUM_SIZE   = 11
SUBTITLE_SIZE      = 13

HEADER_FONT_SIZE = 9
FOOTER_FONT_SIZE = 9

# Posizioni header/footer — DENTRO la zona di sicurezza KDP (≥ 0.25" dal bordo)
# Header: 16pt dentro il margine superiore (sopra la riga del testo)
HEADER_Y = PAGE_H - MARGIN_TOP + 18   # 612 pt = 0.50" dal top  ✓
# Footer: dentro il margine inferiore, a ≥ 0.29" dal bordo inferiore
FOOTER_Y = 21                          # 21 pt = 0.29" dal bottom ✓ (KDP min: 0.25")

# Rientro prima riga
INDENT = 0.25 * 72  # 18 pt

# ── Costanti universali di sicurezza layout ────────────────────────────────────
# Queste costanti implementano le 4 REGOLE LAYOUT e vengono usate ovunque.

# Regola 3 — anti-trattini: fattore max di espansione spazio nelle righe giustificate.
# Sopra questo valore la riga rimane allineata a sinistra (no iper-giustificazione).
MAX_EXTRA_SPACE_FACTOR = 2.0

# Regola 2 — anti-orfano: righe minime di corpo testo che devono seguire un heading.
MIN_LINES_AFTER_HEADING = 3

# Regola 1 — anti-overflow: tolleranza in pt per misure floating-point.
FLOAT_TOLERANCE = 0.5


# ── Font registration ─────────────────────────────────────────────────────────

def get_fonts():
    """Registra e restituisce i font da usare."""
    try:
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont

        font_map = {
            "Georgia":  ["C:/Windows/Fonts/georgia.ttf",  "C:/Windows/Fonts/Georgia.ttf"],
            "GeorgiaB": ["C:/Windows/Fonts/georgiab.ttf", "C:/Windows/Fonts/GeorgiaB.ttf"],
            "GeorgiaI": ["C:/Windows/Fonts/georgiai.ttf", "C:/Windows/Fonts/GeorgiaI.ttf"],
            "GeorgiaBI":["C:/Windows/Fonts/georgiaz.ttf", "C:/Windows/Fonts/GeorgiaBI.ttf"],
        }
        registered = {}
        for name, paths in font_map.items():
            for path in paths:
                if Path(path).exists():
                    pdfmetrics.registerFont(TTFont(name, path))
                    registered[name] = name
                    log.info(f"  Font: {name} → {path}")
                    break
    except Exception as e:
        log.warning(f"  Impossibile registrare font personalizzati: {e}")
        registered = {}

    if "Georgia" in registered:
        return {
            "body":   "Georgia",
            "bold":   registered.get("GeorgiaB",  "Times-Bold"),
            "italic": registered.get("GeorgiaI",  "Times-Italic"),
            "bolditalic": registered.get("GeorgiaBI", "Times-BoldItalic"),
            "header": registered.get("GeorgiaI",  "Times-Italic"),
        }
    # Fallback built-in
    return {
        "body":       "Times-Roman",
        "bold":       "Times-Bold",
        "italic":     "Times-Italic",
        "bolditalic": "Times-BoldItalic",
        "header":     "Times-Italic",
    }


# ── Inline text parsing ───────────────────────────────────────────────────────

def _parse_inline(text: str) -> list:
    """
    Converte testo Markdown inline in lista di (testo, stile).
    Stili: 'normal', 'bold', 'italic', 'bolditalic'
    NON aggiunge MAI trattini/hyphens.
    """
    result = []
    i = 0
    length = len(text)
    buf = []

    def flush_buf():
        if buf:
            result.append(("".join(buf), "normal"))
            buf.clear()

    while i < length:
        # ***bold+italic***
        if text[i:i+3] == "***":
            flush_buf()
            end = text.find("***", i + 3)
            if end != -1:
                result.append((text[i+3:end], "bolditalic"))
                i = end + 3
                continue
        # **bold**
        if text[i:i+2] == "**":
            flush_buf()
            end = text.find("**", i + 2)
            if end != -1:
                result.append((text[i+2:end], "bold"))
                i = end + 2
                continue
        # *italic*
        if text[i] == "*":
            flush_buf()
            end = text.find("*", i + 1)
            if end != -1:
                result.append((text[i+1:end], "italic"))
                i = end + 1
                continue
        buf.append(text[i])
        i += 1

    flush_buf()
    return [(t, s) for t, s in result if t]


# ── Font metrics helpers ──────────────────────────────────────────────────────

def _calc_lines(canvas, words_and_styles, max_w, fonts, font_size,
                first_line_max_w=None):
    """
    Pre-calcola le righe di testo SENZA disegnarle.
    Ritorna lista di righe, dove ogni riga è lista di (word, font, size).

    NON aggiunge mai hyphens — spezza SOLO agli spazi tra le parole.

    first_line_max_w (opzionale):
        Se specificato, la PRIMA riga usa questa larghezza massima invece di max_w.
        Usato per il rientro della prima riga: la prima riga parte da x+INDENT,
        quindi ha solo (max_w - INDENT) di spazio disponibile.
        Ignorarlo causerebbe testo che sfora il margine destro di INDENT punti.
    """
    tokens = []
    for text, style in words_and_styles:
        if style == "bold":
            f = fonts["bold"]
        elif style == "italic":
            f = fonts["italic"]
        elif style == "bolditalic":
            f = fonts["bolditalic"]
        else:
            f = fonts["body"]
        for word in text.split(" "):
            if word:
                tokens.append((word, f, font_size))

    lines = []
    current = []
    current_w = 0.0

    for word, font, size in tokens:
        w = canvas.stringWidth(word + " ", font, size)
        # Prima riga usa first_line_max_w se specificato, le altre usano max_w
        effective_max = (first_line_max_w
                         if first_line_max_w is not None and not lines
                         else max_w)
        if current_w + w > effective_max + FLOAT_TOLERANCE and current:
            lines.append(current)
            current = [(word, font, size)]
            current_w = w
        else:
            current.append((word, font, size))
            current_w += w

    if current:
        lines.append(current)

    return lines


def _count_lines_for_text(canvas, text, font_name, font_size, max_w):
    """
    Conta le righe che un testo occuperà (stima rapida, testo semplice).
    Usato per pre-calcolare altezze senza parsing inline.
    """
    clean = re.sub(r'\*+', '', text)  # strip markdown markers
    words = clean.split()
    if not words:
        return 0
    lines = 1
    current_w = 0.0
    for word in words:
        w = canvas.stringWidth(word + " ", font_name, font_size)
        if current_w + w > max_w + 0.5:
            lines += 1
            current_w = w
        else:
            current_w += w
    return lines


def _text_height(n_lines, leading):
    return n_lines * leading


# ── Drawing helpers ───────────────────────────────────────────────────────────

def _draw_one_line(canvas, line, x, y, content_w, fonts, font_size, is_last):
    """
    Disegna UNA SINGOLA riga pre-calcolata.

    REGOLA 3 (anti-trattini):
    - Ultima riga o riga con ≤1 parola → allineata a sinistra (NO giustificazione)
    - Righe intermedie → giustificate con CAP su MAX_EXTRA_SPACE_FACTOR
    NON aggiunge mai hyphens. NON spezza mai parole.

    REGOLA KDP (anti-overflow margine destro):
    Il bordo destro della riga non supera mai x + content_w.
    content_w deve già tener conto dell'eventuale rientro:
      riga normale:     content_w = CONTENT_W
      prima riga (indent): content_w = CONTENT_W - INDENT
    """
    space_w    = canvas.stringWidth(" ", fonts["body"], font_size)
    max_extra  = space_w * MAX_EXTRA_SPACE_FACTOR
    curr_x     = x
    right_limit = x + content_w  # bordo destro assoluto — NESSUN testo lo supera mai

    if is_last or len(line) <= 1:
        # Allineata a sinistra — nessuna espansione degli spazi
        for word, font, size in line:
            canvas.setFont(font, size)
            if curr_x < right_limit:
                canvas.drawString(curr_x, y, word)
            curr_x += canvas.stringWidth(word + " ", font, size)
    else:
        # Giustificata — formula corretta:
        #   gap_width = (content_w - sum(word_widths)) / n_gaps
        #   L'avanzamento per ogni parola è: word_w + gap_width (non word_w + space_w + extra)
        #   Questo garantisce che l'ultima parola finisca ESATTAMENTE a right_limit.
        line_w   = sum(canvas.stringWidth(w, f, s) for w, f, s in line)
        gaps     = len(line) - 1
        slack    = content_w - line_w
        # gap_width = spazio TOTALE tra due parole (sostituisce space_w)
        # CAP: non superare space_w + max_extra per evitare fiumi bianchi
        if gaps > 0:
            gap_width = min(max(slack / gaps, 0), space_w + max_extra)
        else:
            gap_width = space_w
        for i, (word, font, size) in enumerate(line):
            canvas.setFont(font, size)
            if curr_x < right_limit:
                canvas.drawString(curr_x, y, word)
            # Avanza di: larghezza parola + gap (solo se NON è l'ultima parola)
            curr_x += canvas.stringWidth(word, font, size)
            if i < gaps:
                curr_x += gap_width


def _wrap_text_to_lines(canvas, text, font, size, max_w):
    """Spezza testo in righe basandosi su metriche reali. Ritorna lista di stringhe."""
    words = text.split()
    if not words:
        return [""]
    lines = []
    current = []
    current_w = 0.0
    for word in words:
        w = canvas.stringWidth(word + " ", font, size)
        if current_w + w > max_w + 0.5 and current:
            lines.append(" ".join(current))
            current = [word]
            current_w = w
        else:
            current.append(word)
            current_w += w
    if current:
        lines.append(" ".join(current))
    return lines


# ── Header / Footer ───────────────────────────────────────────────────────────

def draw_header(canvas, page_num, book_title, chapter_title, fonts):
    """
    Header: titolo libro (pag pari, allineato a sinistra)
             o titolo capitolo (pag dispari, allineato a destra).

    KDP COMPLIANCE: il testo dell'header non supera mai ml/mr.
    Se il testo è troppo lungo viene troncato con "…" prima di essere disegnato.
    """
    from reportlab.lib.colors import Color

    canvas.saveState()
    canvas.setFont(fonts["header"], HEADER_FONT_SIZE)
    canvas.setFillColor(Color(0.4, 0.4, 0.4))

    is_odd = page_num % 2 == 1
    ml = MARGIN_LEFT_ODD  if is_odd else MARGIN_LEFT_EVEN
    mr = RIGHT_EDGE_ODD   if is_odd else RIGHT_EDGE_EVEN
    max_header_w = mr - ml - 4  # 4pt di padding di sicurezza

    def _fit_text(text, max_w):
        """Tronca il testo con '…' se supera max_w."""
        if canvas.stringWidth(text, fonts["header"], HEADER_FONT_SIZE) <= max_w:
            return text
        # Rimuovi caratteri dalla fine finché entra
        while len(text) > 1:
            text = text[:-2] + "\u2026"
            if canvas.stringWidth(text, fonts["header"], HEADER_FONT_SIZE) <= max_w:
                return text
        return text

    if is_odd:
        fitted = _fit_text(chapter_title, max_header_w)
        canvas.drawRightString(mr, HEADER_Y, fitted)
    else:
        fitted = _fit_text(book_title, max_header_w)
        canvas.drawString(ml, HEADER_Y, fitted)

    canvas.setStrokeColor(Color(0.7, 0.7, 0.7))
    canvas.setLineWidth(0.4)
    canvas.line(ml, HEADER_Y - 6, mr, HEADER_Y - 6)
    canvas.restoreState()


def draw_footer(canvas, page_num):
    """Numero pagina centrato in basso."""
    from reportlab.lib.colors import Color

    canvas.saveState()
    canvas.setFont("Times-Roman", FOOTER_FONT_SIZE)
    canvas.setFillColor(Color(0.35, 0.35, 0.35))
    canvas.drawCentredString(PAGE_W / 2, FOOTER_Y, str(page_num))
    canvas.restoreState()


# ── Page builders ─────────────────────────────────────────────────────────────

def add_blank_page(canvas):
    canvas.showPage()


def add_title_page(canvas, config, fonts):
    """Frontespizio."""
    from reportlab.lib.colors import Color
    canvas.setPageSize((PAGE_W, PAGE_H))
    book = config["book"]
    cx = PAGE_W / 2

    title_lines = _wrap_text_to_lines(canvas, book["title"], fonts["bold"], 28, CONTENT_W)
    title_h = len(title_lines) * 28 * 1.3
    subtitle = book.get("subtitle", "")
    subtitle_lines = _wrap_text_to_lines(canvas, subtitle, fonts["italic"], 15, CONTENT_W) if subtitle else []
    subtitle_h = len(subtitle_lines) * 15 * 1.3

    author_h = 14 * 1.5
    block_h = title_h + 20 + subtitle_h + 30 + author_h

    y = PAGE_H / 2 + block_h / 2

    # Titolo
    canvas.setFillColor(Color(0.08, 0.08, 0.08))
    for line in title_lines:
        canvas.setFont(fonts["bold"], 28)
        canvas.drawCentredString(cx, y, line)
        y -= 28 * 1.3
    y -= 10

    # Linea
    canvas.setStrokeColor(Color(0.6, 0.6, 0.6))
    canvas.setLineWidth(0.7)
    canvas.line(cx - 70, y, cx + 70, y)
    y -= 15

    # Sottotitolo
    canvas.setFillColor(Color(0.3, 0.3, 0.3))
    for line in subtitle_lines:
        canvas.setFont(fonts["italic"], 15)
        canvas.drawCentredString(cx, y, line)
        y -= 15 * 1.3
    y -= 15

    # Linea
    canvas.setStrokeColor(Color(0.6, 0.6, 0.6))
    canvas.line(cx - 70, y, cx + 70, y)
    y -= 25

    # Autore
    canvas.setFont(fonts["body"], 13)
    canvas.setFillColor(Color(0.15, 0.15, 0.15))
    canvas.drawCentredString(cx, y, book["author"].upper())

    canvas.showPage()


def add_copyright_page(canvas, config, fonts):
    """Pagina copyright."""
    from reportlab.lib.colors import Color
    book = config["book"]
    x = MARGIN_LEFT_EVEN
    y = MARGIN_BOTTOM + 50

    text_lines = [
        f"Copyright \u00a9 {book['year']} {book['author']}",
        "Tutti i diritti riservati.",
        "",
        "Nessuna parte di questa pubblicazione pu\u00f2 essere riprodotta,",
        "distribuita o trasmessa in qualsiasi forma o con qualsiasi mezzo",
        "senza il previo consenso scritto dell'autore.",
        "",
        f"Prima edizione: {book['year']}",
        "Stampato tramite Amazon KDP",
    ]

    canvas.setFont(fonts["body"], 8.5)
    canvas.setFillColor(Color(0.35, 0.35, 0.35))
    lh = 13
    for line in reversed(text_lines):
        canvas.drawString(x, y, line)
        y += lh

    canvas.showPage()


def add_toc_page(canvas, chapters, fonts, page_num_start=3):
    """
    Indice con REGOLA 1 (anti-overflow):
    Ogni voce verifica lo spazio prima di essere disegnata.
    """
    from reportlab.lib.colors import Color

    x_left  = MARGIN_LEFT_ODD
    x_right = PAGE_W - MARGIN_OUTER

    # Altezza di una voce di indice (label "Capitolo N" + riga titolo)
    ITEM_H = 32

    def avail_toc(y):
        return y - MARGIN_BOTTOM

    y = PAGE_H - MARGIN_TOP

    # Titolo INDICE — pre-verifica spazio (sempre presente)
    canvas.setFont(fonts["bold"], 16)
    canvas.setFillColor(Color(0.08, 0.08, 0.08))
    canvas.drawCentredString(PAGE_W / 2, y - 10, "INDICE")
    y -= 50

    for ch in chapters:
        # REGOLA 1: verifica che una voce (ITEM_H) entri nel margine
        if ITEM_H > avail_toc(y) - FLOAT_TOLERANCE:
            draw_footer(canvas, page_num_start)
            canvas.showPage()
            page_num_start += 1
            y = PAGE_H - MARGIN_TOP

        # "Capitolo N" piccolo — sopra la riga principale
        canvas.setFont(fonts["italic"], 8)
        canvas.setFillColor(Color(0.55, 0.55, 0.55))
        canvas.drawString(x_left, y + 13, f"Capitolo {ch.number}")

        # Titolo capitolo
        canvas.setFont(fonts["body"], 11)
        canvas.setFillColor(Color(0.1, 0.1, 0.1))

        # Se il titolo è troppo lungo, lo tronca con "…" per stare su una riga
        title = ch.title
        max_title_w = CONTENT_W - 40
        while canvas.stringWidth(title, fonts["body"], 11) > max_title_w and len(title) > 4:
            title = title[:-2] + "\u2026"
        canvas.drawString(x_left, y, title)

        # Numero pagina
        pg_str = str(ch.toc_page)
        canvas.drawRightString(x_right, y, pg_str)

        # Puntini di collegamento (solo se c'è spazio tra titolo e numero)
        title_w = canvas.stringWidth(title, fonts["body"], 11)
        pg_w    = canvas.stringWidth(pg_str, fonts["body"], 11)
        dot_x0  = x_left + title_w + 8
        dot_x1  = x_right - pg_w - 8
        if dot_x1 > dot_x0 + 10:
            canvas.setFont(fonts["body"], 10)
            canvas.setFillColor(Color(0.65, 0.65, 0.65))
            dot_x = dot_x0
            while dot_x < dot_x1 - 4:
                canvas.drawString(dot_x, y, ".")
                dot_x += 6

        y -= ITEM_H

    draw_footer(canvas, page_num_start)
    canvas.showPage()


def add_image_page(canvas, chapter, images_dir=None):
    """Pagina immagine full-bleed."""
    from reportlab.lib.colors import Color

    canvas.setPageSize((PAGE_W, PAGE_H))
    base = images_dir if images_dir else (ROOT / "assets" / "images")
    img_path = base / f"chapter_{chapter.number:02d}.png"

    if img_path.exists():
        try:
            canvas.drawImage(
                str(img_path), 0, 0,
                width=PAGE_W, height=PAGE_H,
                preserveAspectRatio=False,
            )
        except Exception as e:
            log.warning(f"  Errore immagine cap.{chapter.number}: {e}")
            _draw_placeholder(canvas, chapter)
    else:
        _draw_placeholder(canvas, chapter)

    canvas.showPage()


def _draw_placeholder(canvas, chapter):
    """Placeholder grigio per immagine mancante."""
    from reportlab.lib.colors import Color
    canvas.setFillColor(Color(0.72, 0.72, 0.72))
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setStrokeColor(Color(0.5, 0.5, 0.5))
    canvas.setLineWidth(1.2)
    canvas.rect(12, 12, PAGE_W - 24, PAGE_H - 24, fill=0, stroke=1)
    canvas.setFillColor(Color(0.3, 0.3, 0.3))
    canvas.setFont("Helvetica-Bold", 16)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 18, "IMMAGINE MANCANTE")
    canvas.setFont("Helvetica", 13)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 8,  f"Capitolo {chapter.number}")
    canvas.setFont("Helvetica", 11)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 30, chapter.title)


def add_chapter_title_page(canvas, chapter, page_num, fonts):
    """
    Pagina titolo capitolo.
    Layout top-down: calcola prima le altezze, poi posiziona senza overlap.
    """
    from reportlab.lib.colors import Color

    canvas.setPageSize((PAGE_W, PAGE_H))
    cx = PAGE_W / 2

    # Pre-calcola altezze
    cap_text  = f"CAPITOLO {chapter.number}"
    cap_h     = CHAPTER_NUM_SIZE * 1.5

    title_lines = _wrap_text_to_lines(
        canvas, chapter.title, fonts["bold"], CHAPTER_TITLE_SIZE, CONTENT_W
    )
    title_h = len(title_lines) * CHAPTER_TITLE_SIZE * 1.3

    gap_above_line = 12
    gap_below_line = 22
    line_h = 0.5
    total_block = cap_h + gap_above_line + line_h + gap_below_line + title_h

    # Centra il blocco leggermente sopra il centro geometrico
    block_top = PAGE_H / 2 + total_block / 2 + 20

    y = block_top

    # "CAPITOLO N"
    canvas.setFont(fonts["body"], CHAPTER_NUM_SIZE)
    canvas.setFillColor(Color(0.5, 0.5, 0.5))
    canvas.drawCentredString(cx, y, cap_text)
    y -= cap_h + gap_above_line

    # Linea decorativa
    canvas.setStrokeColor(Color(0.65, 0.65, 0.65))
    canvas.setLineWidth(0.6)
    canvas.line(cx - 45, y, cx + 45, y)
    y -= gap_below_line

    # Titolo capitolo (una riga alla volta, top → bottom)
    canvas.setFont(fonts["bold"], CHAPTER_TITLE_SIZE)
    canvas.setFillColor(Color(0.08, 0.08, 0.08))
    for line in title_lines:
        canvas.drawCentredString(cx, y, line)
        y -= CHAPTER_TITLE_SIZE * 1.3

    # Numero pagina
    draw_footer(canvas, page_num)
    canvas.showPage()


def add_chapter_content(canvas, chapter, page_num_start, book_title, fonts):
    """
    Disegna le pagine di testo del capitolo.
    Ritorna il numero di pagina successivo disponibile.

    Regole:
    - Heading h2: NON può stare da solo in fondo alla pagina;
      deve avere almeno 2 righe di testo dopo di sé.
    - Paragrafi: calcolati con metriche reali, mai overflow.
    - Liste: renderizzate come bullet/numero, NON come paragrafo normale.
    - Giustificazione: capped per evitare spazi enormi che sembrano trattini.
    """
    from reportlab.lib.colors import Color

    page_num = page_num_start
    is_first_page = True

    def _get_x():
        return MARGIN_LEFT_ODD if page_num % 2 == 1 else MARGIN_LEFT_EVEN

    def _get_content_w():
        return CONTENT_W

    def _get_right_edge():
        """Bordo destro assoluto KDP-compliant per la pagina corrente."""
        return RIGHT_EDGE_ODD if page_num % 2 == 1 else RIGHT_EDGE_EVEN

    y = PAGE_H - MARGIN_TOP

    def new_page():
        nonlocal page_num, y, is_first_page
        draw_footer(canvas, page_num)
        if not is_first_page:
            draw_header(canvas, page_num, book_title, chapter.title, fonts)
        canvas.showPage()
        page_num += 1
        is_first_page = False  # noqa: SIM909 — nonlocal update
        y = PAGE_H - MARGIN_TOP  # noqa: SIM909 — nonlocal update

    def available():
        return y - MARGIN_BOTTOM

    def draw_paragraph(text, first_in_section=False):
        """
        Disegna un paragrafo di testo normale RIGA PER RIGA.

        REGOLA 1 (anti-overflow): ogni riga verifica lo spazio disponibile
        prima di essere disegnata. Se non basta → nuova pagina.
        Funziona anche per paragrafi lunghi quanto una pagina intera.

        REGOLA 3 (anti-trattini): delegato a _draw_one_line.

        FIX MARGINE DESTRO:
        Il rientro della prima riga (INDENT) è sottratto dalla larghezza
        disponibile sia nel calcolo delle righe (_calc_lines) sia nel
        disegno (_draw_one_line). Questo garantisce che il testo non superi
        mai RIGHT_EDGE_ODD / RIGHT_EDGE_EVEN di un solo punto.
        """
        nonlocal y

        text = text.strip()
        if not text:
            return

        cw         = _get_content_w()
        use_indent = not first_in_section
        indent_val = INDENT if use_indent else 0
        first_w    = cw - indent_val  # larghezza disponibile per la prima riga

        wands = _parse_inline(text)
        # Passa first_line_max_w: la prima riga è più stretta di INDENT pt
        lines = _calc_lines(canvas, wands, cw, fonts, BODY_FONT_SIZE,
                            first_line_max_w=first_w)
        if not lines:
            return

        canvas.setFillColor(Color(0.05, 0.05, 0.05))
        # Traccia se il rientro va applicato sulla riga corrente
        # (solo sulla prima riga del paragrafo; si azzera dopo un page break
        #  nel caso raro in cui il primo page break cada sulla riga 0)
        apply_indent = use_indent

        for line_idx, line in enumerate(lines):
            is_last = line_idx == len(lines) - 1

            # REGOLA 1: controlla spazio PRIMA di disegnare ogni riga
            if BODY_LEADING > available() - FLOAT_TOLERANCE:
                new_page()
                if line_idx == 0:
                    apply_indent = False  # no indent se page break cade sulla prima riga

            x = _get_x()

            if line_idx == 0 and apply_indent:
                # Prima riga: parte da x+INDENT, larghezza = cw-INDENT
                draw_x  = x + indent_val
                line_cw = first_w
            else:
                # Righe successive: tutta la larghezza disponibile
                draw_x  = x
                line_cw = cw

            _draw_one_line(canvas, line, draw_x, y, line_cw, fonts, BODY_FONT_SIZE, is_last)
            y -= BODY_LEADING

        y -= 1  # micro-gap tra paragrafi

    def draw_h2(text):
        """
        Disegna un sottotitolo h2, con wrapping se il testo è lungo.

        REGOLA 2 (anti-orfano): richiede MIN_LINES_AFTER_HEADING righe di
        corpo testo DOPO di sé. Se lo spazio non basta → pagina nuova.
        L'h2 non resta MAI da solo in fondo pagina.

        REGOLA 1 (anti-overflow): se l'h2 stesso è più lungo di una pagina
        (caso rarissimo), viene disegnato riga per riga con page break.
        """
        nonlocal y

        text = text.strip()
        if not text:
            return

        h2_leading  = SUBTITLE_SIZE * 1.3
        space_above = 18
        space_below = 8
        min_after   = MIN_LINES_AFTER_HEADING * BODY_LEADING

        cw = _get_content_w()
        h2_lines = _wrap_text_to_lines(canvas, text, fonts["bold"], SUBTITLE_SIZE, cw)
        h2_total  = len(h2_lines) * h2_leading

        # REGOLA 2: spazio per h2 + righe minime di corpo
        needed = space_above + h2_total + space_below + min_after
        if needed > available() - FLOAT_TOLERANCE:
            new_page()

        y -= space_above
        canvas.setFont(fonts["bold"], SUBTITLE_SIZE)
        canvas.setFillColor(Color(0.06, 0.06, 0.06))

        for h2_line in h2_lines:
            # REGOLA 1: anche le righe del titolo non sfondano il margine
            if h2_leading > available() - FLOAT_TOLERANCE:
                new_page()
            canvas.drawString(_get_x(), y, h2_line)
            y -= h2_leading

        y -= space_below

    def draw_h3(text):
        """
        Disegna un sottotitolo h3 (sotto-sezione).
        Più piccolo di h2, in grassetto corsivo.
        REGOLA 2: richiede almeno MIN_LINES_AFTER_HEADING righe dopo di sé.
        """
        nonlocal y

        text = text.strip()
        if not text:
            return

        H3_SIZE     = BODY_FONT_SIZE + 1  # 12pt
        h3_leading  = H3_SIZE * 1.3
        space_above = 12
        space_below = 4
        min_after   = MIN_LINES_AFTER_HEADING * BODY_LEADING

        cw = _get_content_w()
        h3_lines = _wrap_text_to_lines(canvas, text, fonts["bolditalic"], H3_SIZE, cw)
        h3_total  = len(h3_lines) * h3_leading

        needed = space_above + h3_total + space_below + min_after
        if needed > available() - FLOAT_TOLERANCE:
            new_page()

        y -= space_above
        canvas.setFont(fonts["bolditalic"], H3_SIZE)
        canvas.setFillColor(Color(0.15, 0.15, 0.15))

        for h3_line in h3_lines:
            if h3_leading > available() - FLOAT_TOLERANCE:
                new_page()
            canvas.drawString(_get_x(), y, h3_line)
            y -= h3_leading

        y -= space_below

    def draw_list_item(item_text, num=None, bullet=None):
        """
        Disegna un elemento di lista RIGA PER RIGA.

        REGOLA 1 (anti-overflow): ogni riga verifica lo spazio.
        REGOLA 3 (anti-trattini): delegato a _draw_one_line.
        Il marcatore (numero o bullet) appare solo sulla prima riga.
        """
        nonlocal y

        item_text = item_text.strip()
        if not item_text:
            return

        cw       = _get_content_w()
        marker_w = 20
        text_w   = cw - marker_w

        wands = _parse_inline(item_text)
        lines = _calc_lines(canvas, wands, text_w, fonts, BODY_FONT_SIZE)
        if not lines:
            return

        canvas.setFillColor(Color(0.05, 0.05, 0.05))
        first_line_of_item = True

        for line_idx, line in enumerate(lines):
            is_last = line_idx == len(lines) - 1

            # REGOLA 1: controlla spazio PRIMA di ogni riga
            if BODY_LEADING > available() - FLOAT_TOLERANCE:
                new_page()
                first_line_of_item = False  # il marcatore è già stato scritto

            x      = _get_x()
            text_x = x + marker_w

            # Marcatore solo sulla prima riga dell'elemento
            if first_line_of_item:
                canvas.setFont(fonts["body"], BODY_FONT_SIZE)
                if num is not None:
                    canvas.drawString(x, y, f"{num}.")
                else:
                    canvas.drawString(x + 4, y, bullet or "\u2022")
                first_line_of_item = False

            _draw_one_line(canvas, line, text_x, y, text_w, fonts, BODY_FONT_SIZE, is_last)
            y -= BODY_LEADING

        y -= 2

    # ── Rendering sezioni del capitolo ─────────────────────────────────────────
    for sec_idx, section in enumerate(chapter.sections):

        if section.title:
            draw_h2(section.title)

        for para_idx, para in enumerate(section.paragraphs):
            first_in_sec = (para_idx == 0 and bool(section.title))

            # Intestazione H3 (marcata da parse_manuscript)
            if para.startswith("__H3__"):
                draw_h3(para[6:])  # rimuove il prefisso "__H3__"
                continue

            # Controlla se è una lista (items separati da \n)
            if "\n" in para:
                items = [l.strip() for l in para.split("\n") if l.strip()]
                # Orderd list
                if all(re.match(r'^\d+[\.\)]\s+', it) for it in items):
                    for n, item in enumerate(items, 1):
                        item_text = re.sub(r'^\d+[\.\)]\s+', '', item)
                        draw_list_item(item_text, num=n)
                # Unordered list
                elif all(re.match(r'^[\-\*\+]\s+', it) for it in items):
                    for item in items:
                        item_text = re.sub(r'^[\-\*\+]\s+', '', item)
                        draw_list_item(item_text, bullet="\u2022")
                else:
                    # Mix o altro: renderizza come paragrafi separati
                    for item in items:
                        draw_paragraph(item, first_in_section=False)
            else:
                draw_paragraph(para, first_in_section=first_in_sec)

    # Fine capitolo: finalizza l'ultima pagina
    draw_footer(canvas, page_num)
    if not is_first_page:
        draw_header(canvas, page_num, book_title, chapter.title, fonts)
    canvas.showPage()
    page_num += 1

    return page_num


# ── Main build ────────────────────────────────────────────────────────────────

def build_book_with_reportlab(config, chapters, images_dir, output_path):
    """Costruisce il PDF completo con ReportLab."""
    from reportlab.pdfgen import canvas as rl_canvas

    log.info("Canvas ReportLab inizializzato")
    c = rl_canvas.Canvas(output_path, pagesize=(PAGE_W, PAGE_H))
    c.setTitle(config["book"]["title"])
    c.setAuthor(config["book"]["author"])
    c.setSubject(config["book"].get("subtitle", ""))

    # ── Audit KDP compliance ────────────────────────────────────────────
    log.info("Audit KDP margins (6×9\"):")
    log.info(f"  Pagina: {PAGE_W}×{PAGE_H}pt = {PAGE_W/72:.3f}\"×{PAGE_H/72:.3f}\"")
    log.info(f"  Gutter (inner): {MARGIN_INNER}pt = {MARGIN_INNER/72:.3f}\" "
             f"(KDP min 0.375\" per ≤150 pag.) ✓")
    log.info(f"  Margine outer:  {MARGIN_OUTER}pt = {MARGIN_OUTER/72:.3f}\" "
             f"(KDP min 0.250\") ✓")
    log.info(f"  Margine top:    {MARGIN_TOP}pt = {MARGIN_TOP/72:.3f}\" "
             f"(KDP min 0.250\") ✓")
    log.info(f"  Margine bottom: {MARGIN_BOTTOM}pt = {MARGIN_BOTTOM/72:.3f}\" "
             f"(KDP min 0.250\") ✓")
    log.info(f"  Area testo: {CONTENT_W}pt × {CONTENT_H}pt "
             f"= {CONTENT_W/72:.2f}\" × {CONTENT_H/72:.2f}\"")
    log.info(f"  Right edge dispari: {RIGHT_EDGE_ODD}pt  "
             f"Right edge pari: {RIGHT_EDGE_EVEN}pt")
    log.info(f"  Footer: {FOOTER_Y}pt = {FOOTER_Y/72:.3f}\" dal bordo ✓ (KDP min 0.25\")")
    # ────────────────────────────────────────────────────────────────────

    fonts = get_fonts()
    book_title = config["book"]["title"]
    page_num = 1

    # Pagine preliminari
    log.info("Frontespizio...")
    add_title_page(c, config, fonts)
    page_num += 1

    log.info("Copyright...")
    add_copyright_page(c, config, fonts)
    page_num += 1

    log.info("Indice...")
    add_toc_page(c, chapters, fonts, page_num)
    page_num += 1

    # Pagina bianca se necessario per far iniziare Cap.1 su pagina dispari
    if page_num % 2 == 0:
        add_blank_page(c)
        page_num += 1

    # Capitoli
    for chapter in chapters:
        log.info(f"Capitolo {chapter.number}: '{chapter.title}'...")

        # Forza inizio su pagina dispari
        if page_num % 2 == 0:
            add_blank_page(c)
            page_num += 1

        # Aggiorna stima pagina per l'indice
        chapter.toc_page = page_num + 2

        # 1. Pagina immagine
        add_image_page(c, chapter, images_dir)
        page_num += 1

        # 2. Pagina titolo capitolo
        add_chapter_title_page(c, chapter, page_num, fonts)
        page_num += 1

        # 3. Pagine testo
        page_num = add_chapter_content(c, chapter, page_num, book_title, fonts)
        log.info(f"  → pagina corrente dopo cap {chapter.number}: {page_num}")

    # Pagina finale
    add_blank_page(c)
    c.save()
    log.info(f"PDF salvato: {output_path}")


def main():
    log.info("=" * 60)
    log.info("AGENTE 2 — LAYOUT ENGINE (ReportLab) — Avvio")
    log.info("=" * 60)

    config_path = ROOT / "config" / "book_config.yaml"
    if not config_path.exists():
        log.error(f"Config non trovato: {config_path}")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    log.info(f"Libro: '{config['book']['title']}' di {config['book']['author']}")

    manuscript_path = ROOT / "input" / "manuscript.md"
    if not manuscript_path.exists():
        log.error(f"Manoscritto non trovato: {manuscript_path}")
        sys.exit(1)

    log.info("Parsing manoscritto...")
    chapters = parse_manuscript(str(manuscript_path))
    chapters = estimate_toc_pages(chapters)
    log.info(f"Trovati {len(chapters)} capitoli")

    images_dir = ROOT / "assets" / "images"
    output_path = ROOT / "output" / "book_draft.pdf"
    os.makedirs(ROOT / "output", exist_ok=True)

    log.info(f"Generazione PDF: {output_path}")
    build_book_with_reportlab(config, chapters, images_dir, str(output_path))

    if output_path.exists():
        size_mb = output_path.stat().st_size / (1024 * 1024)
        log.info(f"PDF: {output_path} ({size_mb:.2f} MB)")
        try:
            import pikepdf
            pdf = pikepdf.open(str(output_path))
            log.info(f"Pagine totali: {len(pdf.pages)}")
            # Verifica prima pagina
            mb = pdf.pages[0].MediaBox
            w = float(mb[2]) - float(mb[0])
            h = float(mb[3]) - float(mb[1])
            log.info(f"Dimensioni pag 1: {w:.0f}x{h:.0f}pt (atteso 432x648)")
            pdf.close()
        except Exception:
            pass
    else:
        log.error("PDF non generato!")
        sys.exit(1)

    log.info("=" * 60)
    log.info("AGENTE 2 — COMPLETATO (ReportLab)")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
