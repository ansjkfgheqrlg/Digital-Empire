"""
PDF Generator — Sub-agent CRO-Funnel
Converte il report Markdown in PDF professionale via ReportLab.
Fallback: salva come file .md se ReportLab non disponibile.

Installazione: pip install reportlab markdown2
"""

import os
import re

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.platypus import (
        HRFlowable,
        Paragraph,
        SimpleDocTemplate,
        Spacer,
    )
    REPORTLAB_OK = True
except ImportError:
    REPORTLAB_OK = False

# Colori Digital Empire
COLORE_BLU = colors.HexColor("#0f3460")
COLORE_ROSSO = colors.HexColor("#e94560")
COLORE_CHIARO = colors.HexColor("#f4f4f8")


def _get_styles():
    base = getSampleStyleSheet()

    titolo = ParagraphStyle(
        "Titolo",
        parent=base["Heading1"],
        fontSize=22,
        textColor=COLORE_BLU,
        spaceAfter=6,
        spaceBefore=0,
        fontName="Helvetica-Bold",
    )
    sezione = ParagraphStyle(
        "Sezione",
        parent=base["Heading2"],
        fontSize=14,
        textColor=COLORE_BLU,
        spaceAfter=4,
        spaceBefore=16,
        fontName="Helvetica-Bold",
        borderPad=(0, 0, 0, 8),
    )
    sottosezione = ParagraphStyle(
        "Sottosezione",
        parent=base["Heading3"],
        fontSize=12,
        textColor=COLORE_BLU,
        spaceAfter=3,
        spaceBefore=10,
        fontName="Helvetica-Bold",
    )
    corpo = ParagraphStyle(
        "Corpo",
        parent=base["Normal"],
        fontSize=10,
        leading=15,
        spaceAfter=4,
        textColor=colors.HexColor("#1a1a2e"),
    )
    bullet_item = ParagraphStyle(
        "Bullet",
        parent=corpo,
        leftIndent=16,
        bulletIndent=6,
        spaceBefore=2,
        spaceAfter=2,
    )
    footer = ParagraphStyle(
        "Footer",
        parent=base["Normal"],
        fontSize=8,
        textColor=colors.grey,
        alignment=1,
    )
    return {
        "titolo": titolo,
        "sezione": sezione,
        "sottosezione": sottosezione,
        "corpo": corpo,
        "bullet": bullet_item,
        "footer": footer,
    }


def _markdown_to_story(markdown_text: str, styles: dict) -> list:
    """Converte Markdown in elementi ReportLab (story)."""
    story = []
    lines = markdown_text.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]

        # Titolo H1
        if line.startswith("# "):
            testo = line[2:].strip()
            story.append(Paragraph(testo, styles["titolo"]))
            story.append(HRFlowable(width="100%", thickness=2, color=COLORE_ROSSO, spaceAfter=8))

        # Titolo H2
        elif line.startswith("## "):
            testo = line[3:].strip()
            story.append(Spacer(1, 4))
            story.append(Paragraph(testo, styles["sezione"]))
            story.append(HRFlowable(width="100%", thickness=1, color=COLORE_ROSSO, spaceAfter=4))

        # Titolo H3
        elif line.startswith("### "):
            testo = line[4:].strip()
            story.append(Paragraph(testo, styles["sottosezione"]))

        # Separatore ---
        elif line.strip() in ("---", "***", "___"):
            story.append(Spacer(1, 6))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
            story.append(Spacer(1, 6))

        # Riga vuota
        elif not line.strip():
            story.append(Spacer(1, 3))

        # Lista puntata
        elif line.startswith("- ") or line.startswith("* "):
            testo = _inline_md(line[2:].strip())
            story.append(Paragraph(f"&bull; {testo}", styles["bullet"]))

        # Lista numerata
        elif re.match(r"^\d+\.\s", line):
            testo = _inline_md(re.sub(r"^\d+\.\s", "", line))
            story.append(Paragraph(f"&bull; {testo}", styles["bullet"]))

        # Riga normale
        else:
            testo = _inline_md(line.strip())
            if testo:
                story.append(Paragraph(testo, styles["corpo"]))

        i += 1

    return story


def _inline_md(text: str) -> str:
    """Converte formattazione inline Markdown in tag ReportLab."""
    # Grassetto **testo** o __testo__
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"__(.+?)__", r"<b>\1</b>", text)
    # Corsivo *testo* o _testo_
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"_(.+?)_", r"<i>\1</i>", text)
    # Codice `testo`
    text = re.sub(r"`(.+?)`", r"<font face='Courier'>\1</font>", text)
    # Escape caratteri speciali per ReportLab
    text = text.replace("&", "&amp;").replace("<b>", "<b>").replace("</b>", "</b>")
    # Re-fix: escapiamo solo & che non sono tag
    # Approccio semplice: già gestito sopra
    return text


def genera_pdf(markdown_content: str, output_path: str) -> bool:
    """
    Converte Markdown → PDF via ReportLab.
    Fallback: salva come .md se ReportLab non disponibile.
    Ritorna True se PDF generato, False altrimenti.
    """
    if not REPORTLAB_OK:
        md_path = output_path.replace(".pdf", ".md")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"[CRO-FUNNEL] ReportLab non installato. Report salvato come: {md_path}")
        return False

    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        styles = _get_styles()

        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=2 * cm,
            leftMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm,
        )

        story = _markdown_to_story(markdown_content, styles)

        # Footer
        story.append(Spacer(1, 20))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
        story.append(Spacer(1, 4))
        story.append(Paragraph("Report generato da Digital Empire Agency", styles["footer"]))

        doc.build(story)
        print(f"[CRO-FUNNEL] PDF generato: {output_path}")
        return True

    except Exception as e:
        # Fallback a Markdown
        md_path = output_path.replace(".pdf", ".md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"[CRO-FUNNEL] Errore PDF ({e}). Report salvato come: {md_path}")
        return False
