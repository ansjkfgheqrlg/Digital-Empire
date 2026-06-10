#!/usr/bin/env python3
"""
Marketing Audit PDF Report Generator
Generates a professional PDF marketing report from a JSON data file.

DESIGN RULES (mandatory, enforced every generation):
  1. Text on dark background  -> always C_WHITE
  2. Text on light background -> always C_BODY / C_NAVY
  3. No nested Tables for badge cells -> use dynamic per-row TableStyle commands
  4. No emoji characters (Windows cp1252 encoding breaks)
  5. All colWidths arrays must sum to <= CONTENT_W (481.89pt for A4 + 2cm margins)
  6. Gauge height = size * 0.75 (prevents grade-text clipping)
  7. Bar chart row_h >= 34 (prevents label/bar overlap)
  8. Spacer(1, 0.4*cm) between all major sections
"""

import json
import sys
import math
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable,
)
from reportlab.platypus.flowables import Flowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ── Dimensions ────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4          # 595.27 x 841.89 pt
MARGIN = 2 * cm              # 56.69 pt each side
CONTENT_W = PAGE_W - 2 * MARGIN   # 481.89 pt  (~17 cm)
TOP_BAR_H = 1.2 * cm
BOT_BAR_H = 1.0 * cm
TOP_MARGIN = 1.7 * cm       # must clear the top bar
BOT_MARGIN = 1.5 * cm       # must clear the bottom bar

# ── Color Palette ─────────────────────────────────────────────────────────────
C_NAVY   = colors.HexColor("#1B2A4A")
C_BLUE   = colors.HexColor("#2563EB")
C_ORANGE = colors.HexColor("#EA580C")
C_GREEN  = colors.HexColor("#16A34A")
C_AMBER  = colors.HexColor("#D97706")
C_RED    = colors.HexColor("#DC2626")
C_LIGHT  = colors.HexColor("#F1F5F9")
C_LIGHT2 = colors.HexColor("#E2E8F0")
C_BODY   = colors.HexColor("#1E293B")
C_GRAY   = colors.HexColor("#64748B")
C_BORDER = colors.HexColor("#CBD5E1")
C_WHITE  = colors.white
C_BRAND  = colors.HexColor("#EBF5FF")   # light blue highlight for brand column


def score_color(score):
    """Return a color based on score range."""
    if score >= 80:  return C_GREEN
    if score >= 60:  return C_BLUE
    if score >= 40:  return C_AMBER
    return C_RED


def grade_label(score):
    if score >= 85: return "A"
    if score >= 70: return "B"
    if score >= 55: return "C"
    if score >= 40: return "D"
    return "F"


def severity_color(sev):
    return {
        "Critical": C_RED,
        "High":     C_ORANGE,
        "Medium":   C_AMBER,
        "Low":      C_BLUE,
    }.get(sev, C_GRAY)


# ── Paragraph Styles ──────────────────────────────────────────────────────────
def get_styles():
    s = {}
    s["title"] = ParagraphStyle(
        "title", fontSize=28, textColor=C_NAVY,
        fontName="Helvetica-Bold", spaceAfter=6, alignment=TA_CENTER,
    )
    s["brand"] = ParagraphStyle(
        "brand", fontSize=15, textColor=C_ORANGE,
        fontName="Helvetica-Bold", spaceAfter=4, alignment=TA_CENTER,
    )
    s["subtitle"] = ParagraphStyle(
        "subtitle", fontSize=10, textColor=C_GRAY,
        fontName="Helvetica", spaceAfter=2, alignment=TA_CENTER,
    )
    s["url"] = ParagraphStyle(
        "url", fontSize=9, textColor=C_BLUE,
        fontName="Helvetica", alignment=TA_CENTER, spaceAfter=6,
    )
    s["h1"] = ParagraphStyle(
        "h1", fontSize=15, textColor=C_NAVY,
        fontName="Helvetica-Bold", spaceBefore=10, spaceAfter=6,
    )
    s["body"] = ParagraphStyle(
        "body", fontSize=9, textColor=C_BODY,
        fontName="Helvetica", leading=14, spaceAfter=4, alignment=TA_JUSTIFY,
    )
    s["body_center"] = ParagraphStyle(
        "body_center", fontSize=9, textColor=C_BODY,
        fontName="Helvetica", leading=14, alignment=TA_CENTER,
    )
    s["body_small"] = ParagraphStyle(
        "body_small", fontSize=8, textColor=C_BODY,
        fontName="Helvetica", leading=12, spaceAfter=2,
    )
    s["body_gray"] = ParagraphStyle(
        "body_gray", fontSize=8, textColor=C_GRAY,
        fontName="Helvetica", leading=12,
    )
    # White text styles (for use on dark/colored backgrounds)
    s["th_white"] = ParagraphStyle(
        "th_white", fontSize=9, textColor=C_WHITE,
        fontName="Helvetica-Bold", leading=13, alignment=TA_CENTER,
    )
    s["th_white_left"] = ParagraphStyle(
        "th_white_left", fontSize=9, textColor=C_WHITE,
        fontName="Helvetica-Bold", leading=13,
    )
    s["cell_white"] = ParagraphStyle(
        "cell_white", fontSize=9, textColor=C_WHITE,
        fontName="Helvetica-Bold", leading=13, alignment=TA_CENTER,
    )
    s["action_header"] = ParagraphStyle(
        "action_header", fontSize=11, textColor=C_WHITE,
        fontName="Helvetica-Bold", leading=15,
    )
    s["action_num"] = ParagraphStyle(
        "action_num", fontSize=10, textColor=C_WHITE,
        fontName="Helvetica-Bold", alignment=TA_CENTER, leading=14,
    )
    s["action_body"] = ParagraphStyle(
        "action_body", fontSize=9, textColor=C_BODY,
        fontName="Helvetica", leading=13, spaceAfter=2,
    )
    s["methodology"] = ParagraphStyle(
        "methodology", fontSize=9, textColor=C_BODY,
        fontName="Helvetica", leading=15, spaceAfter=4, alignment=TA_JUSTIFY,
    )
    s["footer_note"] = ParagraphStyle(
        "footer_note", fontSize=8, textColor=C_GRAY,
        fontName="Helvetica-Oblique", alignment=TA_CENTER,
    )
    return s


# ── Gauge Flowable ─────────────────────────────────────────────────────────────
class ScoreGauge(Flowable):
    """Semi-circular score gauge. Height = size * 0.75 to avoid clipping."""

    def __init__(self, score, size=200):
        super().__init__()
        self.score = score
        self.size = size
        self.width  = size
        self.height = size * 0.75   # taller than before — prevents text clipping

    def draw(self):
        s    = self.size
        cx   = s / 2
        cy   = s * 0.48
        r_ou = s * 0.42
        r_in = s * 0.29
        r_tr = (r_ou + r_in) / 2
        lw   = (r_ou - r_in) * 0.92
        steps = 72

        # Track (gray background arc)
        for i in range(steps):
            a0 = math.radians(180 - i * 180 / steps)
            a1 = math.radians(180 - (i + 1) * 180 / steps)
            x0, y0 = cx + r_tr * math.cos(a0), cy + r_tr * math.sin(a0)
            x1, y1 = cx + r_tr * math.cos(a1), cy + r_tr * math.sin(a1)
            self.canv.saveState()
            self.canv.setStrokeColor(C_LIGHT2)
            self.canv.setLineWidth(lw)
            self.canv.setLineCap(1)
            self.canv.line(x0, y0, x1, y1)
            self.canv.restoreState()

        # Filled arc (score)
        fill_steps = max(1, int(steps * self.score / 100))
        col = score_color(self.score)
        r, g, b = col.red, col.green, col.blue
        for i in range(fill_steps):
            a0 = math.radians(180 - i * 180 / steps)
            a1 = math.radians(180 - (i + 1) * 180 / steps)
            x0, y0 = cx + r_tr * math.cos(a0), cy + r_tr * math.sin(a0)
            x1, y1 = cx + r_tr * math.cos(a1), cy + r_tr * math.sin(a1)
            self.canv.saveState()
            self.canv.setStrokeColorRGB(r, g, b)
            self.canv.setLineWidth(lw)
            self.canv.setLineCap(1)
            self.canv.line(x0, y0, x1, y1)
            self.canv.restoreState()

        # Center white fill (to create donut effect)
        self.canv.setFillColor(C_WHITE)
        self.canv.setStrokeColor(C_WHITE)
        self.canv.circle(cx, cy, r_in - 2, fill=1, stroke=0)

        # Score number (large, on white center)
        self.canv.setFont("Helvetica-Bold", s * 0.22)
        self.canv.setFillColor(C_NAVY)
        self.canv.drawCentredString(cx, cy - s * 0.05, str(self.score))

        # /100 label
        self.canv.setFont("Helvetica", s * 0.075)
        self.canv.setFillColor(C_GRAY)
        self.canv.drawCentredString(cx, cy - s * 0.16, "/100")

        # Grade (below center, on white background)
        grade = grade_label(self.score)
        self.canv.setFont("Helvetica-Bold", s * 0.10)
        self.canv.setFillColor(score_color(self.score))
        self.canv.drawCentredString(cx, cy - s * 0.30, "Grade: " + grade)


# ── Category Bar Chart Flowable ────────────────────────────────────────────────
class CategoryBars(Flowable):
    """Horizontal bar chart. row_h >= 34 to prevent overlap."""

    def __init__(self, categories, width=None, row_h=38):
        super().__init__()
        self.categories = categories   # list of (name, score, weight_str)
        self.bar_width  = width or CONTENT_W
        self.row_h      = row_h
        self.label_w    = 150
        self.score_w    = 52
        self.gap        = 10
        self.width      = self.bar_width
        self.height     = row_h * len(categories) + 12

    def draw(self):
        bar_area = self.bar_width - self.label_w - self.score_w - self.gap
        for i, (name, score, weight) in enumerate(self.categories):
            # y baseline for this row (top-down)
            y_top  = self.height - (i + 1) * self.row_h
            y_bar  = y_top + 14          # bar sits in lower 14pt of row
            y_name = y_top + self.row_h - 10  # category name above bar

            # Category name — dark text on white page
            self.canv.setFont("Helvetica-Bold", 8.5)
            self.canv.setFillColor(C_BODY)
            self.canv.drawString(0, y_name, name)

            # Weight — gray text below name
            self.canv.setFont("Helvetica", 7)
            self.canv.setFillColor(C_GRAY)
            self.canv.drawString(0, y_bar + 2, weight)

            # Track (gray background)
            self.canv.setFillColor(C_LIGHT)
            self.canv.roundRect(self.label_w, y_bar, bar_area, 13, 3, fill=1, stroke=0)

            # Colored fill
            fill = max(6.0, bar_area * score / 100)
            self.canv.setFillColor(score_color(score))
            self.canv.roundRect(self.label_w, y_bar, fill, 13, 3, fill=1, stroke=0)

            # Score label — dark text, positioned AFTER the bar area (no overlap)
            self.canv.setFont("Helvetica-Bold", 9)
            self.canv.setFillColor(C_NAVY)
            self.canv.drawString(
                self.label_w + bar_area + self.gap,
                y_bar + 3,
                str(score) + "/100"
            )


# ── Header / Footer ────────────────────────────────────────────────────────────
def make_header_footer(canvas, doc):
    """Draws the top navy bar and bottom light bar on every page."""
    canvas.saveState()
    w, h = A4

    # Top bar — navy background, white text
    canvas.setFillColor(C_NAVY)
    canvas.rect(0, h - TOP_BAR_H, w, TOP_BAR_H, fill=1, stroke=0)
    canvas.setFillColor(C_WHITE)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.drawString(MARGIN, h - 0.82 * cm, "MARKETING AUDIT REPORT")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(w - MARGIN, h - 0.82 * cm, doc.report_url)

    # Bottom bar — light background, gray text
    canvas.setFillColor(C_LIGHT)
    canvas.rect(0, 0, w, BOT_BAR_H, fill=1, stroke=0)
    canvas.setFillColor(C_GRAY)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(MARGIN, 0.35 * cm, "Generated by AI Marketing Suite for Claude Code")
    canvas.drawRightString(w - MARGIN, 0.35 * cm, "Page " + str(canvas.getPageNumber()))

    canvas.restoreState()


# ── Section Header Helper ─────────────────────────────────────────────────────
def section_header(title, styles):
    """Full-width navy strip with white title text."""
    # Use a Table so it spans CONTENT_W exactly
    t = Table(
        [[Paragraph(title.upper(), styles["th_white_left"])]],
        colWidths=[CONTENT_W],
    )
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), C_NAVY),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
    ]))
    return [Spacer(1, 0.2 * cm), t, Spacer(1, 0.35 * cm)]


# ── PDF Builder ────────────────────────────────────────────────────────────────
def build_pdf(data, output_path):
    styles = get_styles()
    story  = []

    url         = data.get("url", "")
    brand       = data.get("brand_name", "Brand")
    date_str    = data.get("date", datetime.now().strftime("%B %d, %Y"))
    score       = int(data.get("overall_score", 0))
    summary     = data.get("executive_summary", "")
    categories  = data.get("categories", {})
    findings    = data.get("findings", [])
    quick_wins  = data.get("quick_wins", [])
    medium_term = data.get("medium_term", [])
    strategic   = data.get("strategic", [])
    competitors = data.get("competitors", [])

    # =========================================================================
    # PAGE 1: COVER
    # =========================================================================
    story.append(Spacer(1, 1.8 * cm))
    story.append(Paragraph("MARKETING AUDIT", styles["title"]))
    story.append(Paragraph("REPORT", styles["title"]))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph(brand, styles["brand"]))
    story.append(Paragraph(url, styles["url"]))
    story.append(Paragraph(date_str, styles["subtitle"]))
    story.append(Spacer(1, 0.7 * cm))

    # Gauge — centered via single-cell Table
    gauge = ScoreGauge(score, size=200)
    gauge_wrap = Table([[gauge]], colWidths=[CONTENT_W])
    gauge_wrap.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER")]))
    story.append(gauge_wrap)
    story.append(Spacer(1, 0.6 * cm))

    # Executive summary box — light background, dark text
    summary_box = Table(
        [[Paragraph(summary, styles["body"])]],
        colWidths=[CONTENT_W - 1 * cm],
    )
    summary_box.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), C_LIGHT),
        ("TOPPADDING",    (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
    ]))
    # Center the box on the page
    outer = Table([[summary_box]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER")]))
    story.append(outer)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: SCORE BREAKDOWN
    # =========================================================================
    story += section_header("Score Breakdown", styles)

    cat_list = [
        (name, int(v["score"]), v.get("weight", ""))
        for name, v in categories.items()
    ]

    # Bar chart
    bars = CategoryBars(cat_list, width=CONTENT_W)
    story.append(bars)
    story.append(Spacer(1, 0.5 * cm))

    # Score summary table
    # Columns: Category | Score | Weight | Status
    # Widths (must sum <= CONTENT_W = 481.89):
    col_cat    = CONTENT_W * 0.44   # 212 pt
    col_score  = CONTENT_W * 0.16   # 77 pt
    col_weight = CONTENT_W * 0.14   # 67 pt
    col_status = CONTENT_W * 0.26   # 125 pt

    # Header row — navy bg, white text
    score_rows = [[
        Paragraph("Category",  styles["th_white_left"]),
        Paragraph("Score",     styles["th_white"]),
        Paragraph("Weight",    styles["th_white"]),
        Paragraph("Status",    styles["th_white"]),
    ]]

    # Build dynamic style commands
    score_style_cmds = [
        ("BACKGROUND",    (0, 0), (-1,  0), C_NAVY),
        ("FONTNAME",      (0, 0), (-1,  0), "Helvetica-Bold"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("GRID",          (0, 0), (-1, -1), 0.3, C_BORDER),
        ("ALIGN",         (1, 0), (3, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]

    for i, (name, sc, wt) in enumerate(cat_list):
        col   = score_color(sc)
        row_i = i + 1
        if sc >= 80: status_txt = "Strong"
        elif sc >= 60: status_txt = "Good"
        elif sc >= 40: status_txt = "Needs Work"
        else: status_txt = "Critical"

        row_bg = C_WHITE if i % 2 == 0 else C_LIGHT

        score_rows.append([
            Paragraph(name,   styles["body"]),
            Paragraph("<b>" + str(sc) + "/100</b>", ParagraphStyle(
                "sc_" + str(i), fontSize=9, textColor=col,
                fontName="Helvetica-Bold", alignment=TA_CENTER)),
            Paragraph(wt, styles["body_center"]),
            Paragraph(status_txt, ParagraphStyle(
                "st_" + str(i), fontSize=8.5, textColor=C_WHITE,
                fontName="Helvetica-Bold", alignment=TA_CENTER)),
        ])
        score_style_cmds += [
            ("BACKGROUND", (0, row_i), (-1, row_i), row_bg),
            ("BACKGROUND", (3, row_i), (3, row_i), col),   # status cell colored
        ]

    score_tbl = Table(
        score_rows,
        colWidths=[col_cat, col_score, col_weight, col_status],
    )
    score_tbl.setStyle(TableStyle(score_style_cmds))
    story.append(score_tbl)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: KEY FINDINGS
    # =========================================================================
    story += section_header("Key Findings", styles)

    # Columns: Severity | Finding
    col_sev     = CONTENT_W * 0.17   # 82 pt
    col_finding = CONTENT_W * 0.83   # 400 pt

    findings_rows = [[
        Paragraph("Severity", styles["th_white"]),
        Paragraph("Finding",  styles["th_white_left"]),
    ]]
    findings_style_cmds = [
        ("BACKGROUND",    (0, 0), (-1,  0), C_NAVY),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("GRID",          (0, 0), (-1, -1), 0.3, C_BORDER),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",         (0, 0), (0,  -1), "CENTER"),
    ]

    for i, f in enumerate(findings):
        sev   = f.get("severity", "Medium")
        col   = severity_color(sev)
        row_i = i + 1
        row_bg = C_WHITE if i % 2 == 0 else C_LIGHT

        findings_rows.append([
            Paragraph(sev, styles["cell_white"]),
            Paragraph(f.get("finding", ""), styles["body_small"]),
        ])
        findings_style_cmds += [
            ("BACKGROUND", (0, row_i), (-1, row_i), row_bg),
            ("BACKGROUND", (0, row_i), (0,  row_i), col),   # severity cell colored bg
        ]

    findings_tbl = Table(
        findings_rows,
        colWidths=[col_sev, col_finding],
    )
    findings_tbl.setStyle(TableStyle(findings_style_cmds))
    story.append(findings_tbl)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: ACTION PLAN
    # =========================================================================
    story += section_header("Prioritized Action Plan", styles)

    def action_section(title, color, items):
        """Renders a colored header strip + numbered rows for an action group."""
        block = []

        # Header strip — colored bg, white text
        hdr = Table(
            [[Paragraph(title, styles["action_header"])]],
            colWidths=[CONTENT_W],
        )
        hdr.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), color),
            ("TOPPADDING",    (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING",   (0, 0), (-1, -1), 12),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ]))
        block.append(hdr)

        if items:
            rows       = []
            style_cmds = [
                ("GRID",          (0, 0), (-1, -1), 0.3, C_BORDER),
                ("TOPPADDING",    (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("LEFTPADDING",   (0, 0), (-1, -1), 6),
                ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
                ("VALIGN",        (0, 0), (-1, -1), "TOP"),
                ("ALIGN",         (0, 0), (0,  -1), "CENTER"),
            ]
            num_col_w  = 0.7 * cm
            text_col_w = CONTENT_W - num_col_w

            for i, item in enumerate(items):
                row_bg = C_WHITE if i % 2 == 0 else C_LIGHT
                rows.append([
                    Paragraph("<b>" + str(i + 1) + "</b>", ParagraphStyle(
                        "num_" + str(i), fontSize=9.5, textColor=color,
                        fontName="Helvetica-Bold", alignment=TA_CENTER, leading=14,
                    )),
                    Paragraph(item, styles["action_body"]),
                ])
                style_cmds.append(("BACKGROUND", (0, i), (-1, i), row_bg))

            items_tbl = Table(rows, colWidths=[num_col_w, text_col_w])
            items_tbl.setStyle(TableStyle(style_cmds))
            block.append(items_tbl)

        block.append(Spacer(1, 0.45 * cm))
        return block

    story += action_section("QUICK WINS  --  This Week",      C_GREEN,  quick_wins)
    story += action_section("MEDIUM-TERM  --  1-3 Months",    C_BLUE,   medium_term)
    story += action_section("STRATEGIC  --  3-6 Months",      C_ORANGE, strategic)

    # =========================================================================
    # PAGE 5: COMPETITIVE LANDSCAPE (optional)
    # =========================================================================
    if competitors:
        story.append(PageBreak())
        story += section_header("Competitive Landscape", styles)

        comp_names  = [c.get("name", "Competitor " + str(i + 1)) for i, c in enumerate(competitors[:3])]
        row_labels  = [("Positioning", "positioning"), ("Pricing", "pricing"),
                       ("Social Proof", "social_proof"), ("Content", "content")]

        n_data_cols = 1 + len(comp_names)          # brand col + competitor cols
        n_total     = 1 + n_data_cols               # factor label + data cols
        label_w     = CONTENT_W * 0.18
        data_col_w  = (CONTENT_W - label_w) / n_data_cols

        # Header row — navy bg, white text
        comp_header_row = [Paragraph("Factor", styles["th_white"])]
        comp_header_row.append(Paragraph(brand, styles["th_white"]))
        for cn in comp_names:
            comp_header_row.append(Paragraph(cn, styles["th_white"]))

        comp_rows = [comp_header_row]
        comp_style_cmds = [
            ("BACKGROUND",    (0, 0), (-1,  0), C_NAVY),
            ("TOPPADDING",    (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING",   (0, 0), (-1, -1), 7),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 7),
            ("GRID",          (0, 0), (-1, -1), 0.3, C_BORDER),
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
            ("FONTNAME",      (0, 1), (0,  -1), "Helvetica-Bold"),
            ("FONTSIZE",      (0, 0), (-1, -1), 8),
        ]

        for i, (lbl, key) in enumerate(row_labels):
            row_bg = C_WHITE if i % 2 == 0 else C_LIGHT
            row_i  = i + 1
            row = [Paragraph(lbl, styles["body_small"])]
            row.append(Paragraph(data.get("brand_" + key, "—"), styles["body_small"]))
            for c in competitors[:3]:
                row.append(Paragraph(c.get(key, "—"), styles["body_small"]))
            comp_rows.append(row)
            comp_style_cmds += [
                ("BACKGROUND", (0,  row_i), (-1,  row_i), row_bg),
                ("BACKGROUND", (1,  row_i), (1,   row_i), C_BRAND),   # brand col highlight
                ("TEXTCOLOR",  (0,  row_i), (0,   row_i), C_NAVY),
            ]

        comp_tbl = Table(
            comp_rows,
            colWidths=[label_w] + [data_col_w] * n_data_cols,
        )
        comp_tbl.setStyle(TableStyle(comp_style_cmds))
        story.append(comp_tbl)

    # =========================================================================
    # FINAL PAGE: METHODOLOGY
    # =========================================================================
    story.append(PageBreak())
    story += section_header("Methodology", styles)

    methodology_text = (
        "This report was generated using the AI Marketing Suite audit framework. "
        "Each category is scored 0-100 based on the following weighted criteria:<br/><br/>"
        "<b>Content &amp; Messaging (25%)</b> — Headline clarity, value proposition strength, "
        "copy persuasion, social proof quality, brand voice consistency.<br/><br/>"
        "<b>Conversion Optimization (20%)</b> — CTA effectiveness, form friction, visual hierarchy, "
        "trust signals at conversion points, pricing psychology, upsell logic.<br/><br/>"
        "<b>SEO &amp; Discoverability (20%)</b> — Title tags, meta descriptions, URL structure, "
        "schema markup, Core Web Vitals, internal linking, content marketing strategy.<br/><br/>"
        "<b>Competitive Positioning (15%)</b> — Unique positioning clarity, market category "
        "definition, competitive awareness signals, third-party validation.<br/><br/>"
        "<b>Brand &amp; Trust (10%)</b> — Brand identity consistency, social proof depth, "
        "mission communication, trust infrastructure.<br/><br/>"
        "<b>Growth &amp; Strategy (10%)</b> — Business model clarity, growth loops, retention "
        "signals, revenue expansion opportunities, scalability.<br/><br/>"
        "<b>Score Interpretation:</b> "
        "85-100 (A): Excellent. "
        "70-84 (B): Good. "
        "55-69 (C): Average. "
        "40-54 (D): Below Average. "
        "0-39 (F): Critical."
    )
    story.append(Paragraph(methodology_text, styles["methodology"]))
    story.append(Spacer(1, 1.2 * cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_BORDER, spaceAfter=8))
    story.append(Paragraph(
        "Generated by AI Marketing Suite for Claude Code",
        styles["footer_note"],
    ))

    # ── Build document ────────────────────────────────────────────────────────
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOT_MARGIN,
    )
    doc.report_url = url
    doc.build(story, onFirstPage=make_header_footer, onLaterPages=make_header_footer)
    print("[OK] PDF report generated: " + output_path)


# ── Entry Point ────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) == 1:
        # Demo mode with sample data
        data = {
            "url": "https://example.com",
            "date": "March 9, 2026",
            "brand_name": "Example Co",
            "overall_score": 62,
            "executive_summary": (
                "Example Co scores 62/100, reflecting a solid foundation with clear "
                "opportunities for conversion and SEO improvement. The primary gaps are "
                "missing social proof and a weak organic search strategy. Implementing the "
                "recommended quick wins could generate an estimated EUR 5,000-12,000 per month "
                "in additional revenue within 30 days."
            ),
            "categories": {
                "Content & Messaging":    {"score": 68, "weight": "25%"},
                "Conversion Optimization":{"score": 52, "weight": "20%"},
                "SEO & Discoverability":  {"score": 74, "weight": "20%"},
                "Competitive Positioning":{"score": 48, "weight": "15%"},
                "Brand & Trust":          {"score": 70, "weight": "10%"},
                "Growth & Strategy":      {"score": 55, "weight": "10%"},
            },
            "findings": [
                {"severity": "Critical", "finding": "No customer testimonials on product or pricing pages."},
                {"severity": "High",     "finding": "Homepage headline is generic and fails the 5-second test."},
                {"severity": "Medium",   "finding": "Missing meta descriptions on 6 of 8 key pages."},
                {"severity": "Low",      "finding": "Social media links open in the same tab."},
            ],
            "quick_wins": [
                "Add 3-5 customer testimonials with photos and specific results to the homepage.",
                "Rewrite the primary CTA to include the price and outcome: 'Start Free Trial -- No Card Required'.",
                "Write custom meta descriptions (140-155 chars) for all landing pages.",
            ],
            "medium_term": [
                "Build a comparison page targeting '[Product] vs [Competitor]' search queries.",
                "Implement a post-purchase email upsell sequence for existing customers.",
                "Add Product and FAQ schema markup to all product pages.",
            ],
            "strategic": [
                "Launch a content hub with 12 articles targeting high-intent keywords.",
                "Develop a referral program for existing customers (20-30% commission).",
                "Redesign the pricing page with value anchoring and payment plan options.",
            ],
            "competitors": [
                {
                    "name": "Competitor A",
                    "positioning": "Enterprise-focused, compliance-first",
                    "pricing": "$99/mo base, annual discounts available",
                    "social_proof": "Case studies, G2 reviews, 4.8 stars",
                    "content": "Deep technical blog, webinars",
                },
                {
                    "name": "Competitor B",
                    "positioning": "SMB-focused, ease of use",
                    "pricing": "$29/mo, free tier available",
                    "social_proof": "Trustpilot 4.7 stars, 2000+ reviews",
                    "content": "YouTube tutorials, help docs",
                },
            ],
        }
        output = "MARKETING-REPORT-sample.pdf"
    else:
        json_path = sys.argv[1]
        output    = sys.argv[2] if len(sys.argv) > 2 else "MARKETING-REPORT.pdf"
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    build_pdf(data, output)


if __name__ == "__main__":
    main()
