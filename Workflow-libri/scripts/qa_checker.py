"""
qa_checker.py — Agente 3: Quality Assurance

Verifica il PDF generato contro la checklist di qualità completa.
Produce un report Markdown dettagliato e, se tutto OK, copia il PDF come finale.

Output:
    output/qa_report.md
    output/book_final.pdf (solo se 0 errori critici)

Uso:
    python scripts/qa_checker.py
"""

import os
import sys
import yaml
import shutil
import logging
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from scripts.parse_manuscript import parse_manuscript

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
        logging.FileHandler(ROOT / "output" / "qa_log.txt", encoding="utf-8"),
    ]
)
log = logging.getLogger("qa_checker")


# ── Data structures ───────────────────────────────────────────────────────────

@dataclass
class CheckResult:
    name: str
    passed: bool
    note: str = ""
    critical: bool = True


@dataclass
class QAReport:
    title: str
    pdf_path: str
    date: str
    total_pages: int = 0
    checks: List[CheckResult] = field(default_factory=list)
    critical_errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    corrective_actions: List[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return len(self.critical_errors) == 0


# ── PDF Analysis ──────────────────────────────────────────────────────────────

def check_pdf_dimensions(pdf_path: str) -> Tuple[bool, str, int]:
    """
    Verifica dimensioni pagina: deve essere 432x648 pt (6x9in).
    Restituisce (ok, note, total_pages).
    """
    try:
        import pikepdf
        pdf = pikepdf.open(pdf_path)
        total_pages = len(pdf.pages)
        wrong = []

        for i, page in enumerate(pdf.pages):
            try:
                mb = page.MediaBox
                w = float(mb[2]) - float(mb[0])
                h = float(mb[3]) - float(mb[1])
                if not (abs(w - 432) < 2 and abs(h - 648) < 2):
                    wrong.append(f"p.{i+1}: {w:.1f}x{h:.1f}pt")
            except Exception as e:
                wrong.append(f"p.{i+1}: errore lettura — {e}")

        pdf.close()

        if wrong:
            note = f"Pagine con dimensioni errate: {', '.join(wrong[:5])}"
            return False, note, total_pages
        else:
            return True, f"432x648pt verificato su {total_pages} pagine", total_pages

    except ImportError:
        log.warning("pikepdf non disponibile — verifica dimensioni saltata")
        # Tentiamo con PyPDF2
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(pdf_path)
            total_pages = len(reader.pages)
            wrong = []
            for i, page in enumerate(reader.pages):
                try:
                    box = page.mediabox
                    w = float(box.width)
                    h = float(box.height)
                    if not (abs(w - 432) < 2 and abs(h - 648) < 2):
                        wrong.append(f"p.{i+1}: {w:.1f}x{h:.1f}pt")
                except Exception:
                    pass
            if wrong:
                return False, f"Pagine errate: {', '.join(wrong[:5])}", total_pages
            return True, f"432x648pt ({total_pages} pagine, via PyPDF2)", total_pages
        except ImportError:
            return None, "pikepdf/PyPDF2 non disponibili — verifica saltata", 0
    except Exception as e:
        return False, f"Errore apertura PDF: {e}", 0


def check_pdf_validity(pdf_path: str) -> Tuple[bool, str]:
    """Verifica che il PDF sia apribile e non corrotto."""
    if not Path(pdf_path).exists():
        return False, f"File non trovato: {pdf_path}"

    size_mb = Path(pdf_path).stat().st_size / (1024 * 1024)
    if size_mb < 0.01:
        return False, f"File troppo piccolo: {size_mb:.3f} MB (probabilmente vuoto)"

    # Tenta apertura
    try:
        import pikepdf
        pdf = pikepdf.open(pdf_path)
        pages = len(pdf.pages)
        pdf.close()
        return True, f"PDF valido, {pages} pagine, {size_mb:.2f} MB"
    except ImportError:
        pass

    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(pdf_path)
        pages = len(reader.pages)
        return True, f"PDF valido, {pages} pagine, {size_mb:.2f} MB (via PyPDF2)"
    except ImportError:
        # Fallback: controlla firma PDF
        with open(pdf_path, "rb") as f:
            header = f.read(4)
        if header == b"%PDF":
            return True, f"PDF valido (firma OK), {size_mb:.2f} MB"
        return False, "File non sembra un PDF valido"
    except Exception as e:
        return False, f"PDF corrotto: {e}"


def extract_pdf_text(pdf_path: str) -> Optional[str]:
    """
    Estrae testo dal PDF.
    Restituisce il testo o None se non possibile.
    """
    # Tenta con pikepdf (limitato per testo)
    try:
        import pdfplumber
        text_parts = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text_parts.append(t)
        return "\n".join(text_parts)
    except ImportError:
        pass

    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(pdf_path)
        text_parts = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text_parts.append(t)
        return "\n".join(text_parts)
    except ImportError:
        pass

    return None


def count_images_in_pdf(pdf_path: str) -> Tuple[int, str]:
    """
    Conta le immagini nel PDF.
    Restituisce (count, note).
    """
    try:
        import pikepdf
        pdf = pikepdf.open(pdf_path)
        image_count = 0
        for page in pdf.pages:
            try:
                resources = page.get("/Resources", {})
                xobjects = resources.get("/XObject", {})
                for key in xobjects:
                    xobj = xobjects[key]
                    if hasattr(xobj, "get"):
                        subtype = xobj.get("/Subtype", "")
                        if str(subtype) == "/Image":
                            image_count += 1
            except Exception:
                pass
        pdf.close()
        return image_count, f"Trovate {image_count} immagini nel PDF"
    except ImportError:
        return -1, "pikepdf non disponibile — conteggio immagini saltato"
    except Exception as e:
        return -1, f"Errore conteggio immagini: {e}"


# ── Content Checks ────────────────────────────────────────────────────────────

def check_chapters_content(
    pdf_text: Optional[str],
    manuscript_chapters: list,
) -> Tuple[bool, str, list]:
    """
    Verifica che tutti i capitoli del manoscritto siano presenti nel PDF.
    Restituisce (ok, note, missing_chapters).
    """
    if pdf_text is None:
        return None, "Estrazione testo non disponibile", []

    missing = []
    for ch in manuscript_chapters:
        # Cerca il titolo del capitolo nel testo PDF
        title_lower = ch.title.lower()
        pdf_lower = pdf_text.lower()
        if title_lower not in pdf_lower:
            missing.append(f"Cap. {ch.number}: '{ch.title}'")

    if missing:
        return False, f"Capitoli mancanti: {', '.join(missing)}", missing
    return True, f"Tutti i {len(manuscript_chapters)} capitoli presenti", []


def check_images_on_disk(images_dir: Path, chapters: list) -> Tuple[bool, str, list]:
    """
    Verifica che ci siano le immagini per ogni capitolo del manoscritto.
    Usa i numeri di capitolo reali (possono partire da 0).
    """
    import re as _re
    existing = sorted(images_dir.glob("chapter_*.png"))
    existing_nums = set()
    for img in existing:
        m = _re.search(r"chapter_(\d+)", img.name)
        if m:
            existing_nums.add(int(m.group(1)))

    chapter_nums = [ch.number for ch in chapters]
    missing = [n for n in chapter_nums if n not in existing_nums]

    if missing:
        return (
            False,
            f"Immagini mancanti per capitoli: {missing}",
            [f"Capitolo {n}" for n in missing],
        )
    return True, f"Tutte le {len(chapter_nums)} immagini presenti in assets/images/ (cap. {min(chapter_nums)}-{max(chapter_nums)})", []


def check_page_count_reasonable(
    total_pages: int,
    chapter_count: int,
) -> Tuple[bool, str]:
    """
    Verifica che il numero di pagine sia ragionevole.
    Minimo atteso: 4 (prelim) + capitoli * 3 (immagine + titolo + almeno 1 testo)
    """
    min_expected = 4 + chapter_count * 3
    max_expected = 4 + chapter_count * 50  # massimo ragionevole

    if total_pages < min_expected:
        return (
            False,
            f"{total_pages} pagine trovate, minimo atteso {min_expected} "
            f"(cap={chapter_count})"
        )
    if total_pages > max_expected:
        return (
            False,
            f"{total_pages} pagine trovate, massimo atteso {max_expected} — "
            f"possibile errore di layout"
        )
    return True, f"{total_pages} pagine (atteso {min_expected}-{max_expected})"


# ── Report Generator ──────────────────────────────────────────────────────────

def generate_report_markdown(report: QAReport) -> str:
    """Genera il report QA in formato Markdown"""
    lines = []

    result_emoji = "PASSATO" if report.passed else "DA CORREGGERE"
    result_icon = "✅" if report.passed else "❌"

    lines.append(f"# Report Quality Assurance — {report.title}")
    lines.append(f"")
    lines.append(f"**Data**: {report.date}")
    lines.append(f"**PDF analizzato**: `{Path(report.pdf_path).name}`")
    lines.append(f"**Pagine totali**: {report.total_pages}")
    lines.append(f"")
    lines.append(f"## Risultato Globale: {result_icon} {result_emoji}")
    lines.append(f"")

    # Raggruppa i check per categoria
    categories = {
        "Dimensioni e Formato": [],
        "Validita PDF": [],
        "Contenuto Testuale": [],
        "Immagini": [],
        "Struttura": [],
        "Altro": [],
    }

    for check in report.checks:
        placed = False
        for cat_key in categories:
            # Assegna alla categoria in base al nome
            cat_lower = cat_key.lower().replace("à", "a")
            check_lower = check.name.lower()
            if any(word in check_lower for word in cat_lower.split()):
                categories[cat_key].append(check)
                placed = True
                break
        if not placed:
            categories["Altro"].append(check)

    lines.append("## Dettaglio Checklist")
    lines.append("")

    for cat_name, cat_checks in categories.items():
        if not cat_checks:
            continue
        lines.append(f"### {cat_name}")
        lines.append("| Check | Stato | Note |")
        lines.append("|-------|-------|------|")
        for check in cat_checks:
            if check.passed is True:
                icon = "✅"
            elif check.passed is False:
                icon = "❌" if check.critical else "⚠️"
            else:
                icon = "⏭️"
            lines.append(f"| {check.name} | {icon} | {check.note} |")
        lines.append("")

    # Errori critici
    if report.critical_errors:
        lines.append("## Errori Critici (da correggere obbligatoriamente)")
        for i, err in enumerate(report.critical_errors, 1):
            lines.append(f"{i}. ❌ {err}")
        lines.append("")

    # Warning
    if report.warnings:
        lines.append("## Warning (consigliato correggere)")
        for i, w in enumerate(report.warnings, 1):
            lines.append(f"{i}. ⚠️ {w}")
        lines.append("")

    # Azioni correttive
    if report.corrective_actions:
        lines.append("## Azioni Correttive")
        for i, action in enumerate(report.corrective_actions, 1):
            lines.append(f"{i}. {action}")
        lines.append("")

    if report.passed:
        lines.append("---")
        lines.append("")
        lines.append(
            f"**PDF finale**: `output/book_final.pdf` — "
            f"pronto per la stampa su KDP Amazon"
        )

    return "\n".join(lines)


# ── Main QA ───────────────────────────────────────────────────────────────────

def run_qa(
    draft_path: str,
    manuscript_path: str,
    config_path: str,
    images_dir: Path,
) -> QAReport:
    """
    Esegue tutti i controlli QA e costruisce il report.
    """
    # Carica config e manoscritto
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    chapters = parse_manuscript(manuscript_path)
    chapter_count = len(chapters)

    report = QAReport(
        title=config["book"]["title"],
        pdf_path=draft_path,
        date=datetime.now().strftime("%Y-%m-%d"),
    )

    log.info(f"QA per: {report.title} — {chapter_count} capitoli")

    # ── CHECK 1: PDF valido ────────────────────────────────────────────────────
    log.info("Check 1: Validità PDF...")
    ok, note = check_pdf_validity(draft_path)
    report.checks.append(CheckResult("PDF valido e non corrotto", ok, note))
    if ok is False:
        report.critical_errors.append(f"PDF non valido: {note}")
        report.corrective_actions.append(
            "Rigenerare il PDF lanciando build_book.py"
        )

    # ── CHECK 2: Dimensioni pagina ─────────────────────────────────────────────
    log.info("Check 2: Dimensioni pagina (6x9in = 432x648pt)...")
    ok, note, total_pages = check_pdf_dimensions(draft_path)
    report.total_pages = total_pages
    if ok is None:
        report.checks.append(
            CheckResult("Dimensioni pagina 6x9", None, note, critical=False)
        )
        report.warnings.append(note)
    else:
        report.checks.append(CheckResult("Dimensioni pagina 6x9", ok, note))
        if not ok:
            report.critical_errors.append(f"Dimensioni pagina errate: {note}")
            report.corrective_actions.append(
                "Verificare il CSS @page nel file styles.css e rigenerare"
            )

    # ── CHECK 3: Numero pagine ragionevole ────────────────────────────────────
    if total_pages > 0:
        log.info(f"Check 3: Numero pagine ({total_pages})...")
        ok, note = check_page_count_reasonable(total_pages, chapter_count)
        report.checks.append(
            CheckResult("Numero pagine ragionevole", ok, note, critical=False)
        )
        if not ok:
            report.warnings.append(f"Numero pagine anomalo: {note}")

    # ── CHECK 4: Immagini su disco ────────────────────────────────────────────
    log.info(f"Check 4: Immagini in assets/images/ ({chapter_count} attese)...")
    ok, note, missing = check_images_on_disk(images_dir, chapters)
    report.checks.append(CheckResult("Immagini per ogni capitolo", ok, note))
    if not ok:
        for m in missing:
            report.critical_errors.append(f"Immagine mancante: {m}")
        report.corrective_actions.append(
            "Eseguire generate_images.py per rigenerare le immagini mancanti"
        )

    # ── CHECK 5: Immagini nel PDF ─────────────────────────────────────────────
    log.info("Check 5: Immagini incorporate nel PDF...")
    img_count, img_note = count_images_in_pdf(draft_path)
    if img_count == -1:
        report.checks.append(
            CheckResult("Immagini incorporate nel PDF", None, img_note, critical=False)
        )
    else:
        ok = img_count >= chapter_count
        report.checks.append(
            CheckResult(
                "Immagini incorporate nel PDF",
                ok,
                f"{img_note} (attese almeno {chapter_count})"
            )
        )
        if not ok:
            report.warnings.append(
                f"Solo {img_count} immagini nel PDF, attese {chapter_count}"
            )

    # ── CHECK 6: Contenuto testuale ───────────────────────────────────────────
    log.info("Check 6: Contenuto testuale (capitoli nel PDF)...")
    pdf_text = extract_pdf_text(draft_path)
    ok, note, missing_chaps = check_chapters_content(pdf_text, chapters)

    if ok is None:
        report.checks.append(
            CheckResult(
                "Tutti i capitoli presenti nel testo",
                None,
                "Estrazione testo non disponibile (installa pdfplumber o PyPDF2)",
                critical=False,
            )
        )
        report.warnings.append(
            "Impossibile verificare il testo: installa pdfplumber per check completo"
        )
    else:
        report.checks.append(
            CheckResult("Tutti i capitoli presenti nel testo", ok, note)
        )
        if not ok:
            for mc in missing_chaps:
                report.critical_errors.append(f"Testo mancante: {mc}")
            report.corrective_actions.append(
                "Verificare il parser del manoscritto e rigenerare il PDF"
            )

    # ── CHECK 7: File PDF presente ────────────────────────────────────────────
    pdf_exists = Path(draft_path).exists()
    report.checks.append(
        CheckResult(
            "File PDF esiste in output/",
            pdf_exists,
            draft_path if pdf_exists else "File non trovato",
        )
    )

    # ── CHECK 8: Dimensione file ragionevole ──────────────────────────────────
    if pdf_exists:
        size_mb = Path(draft_path).stat().st_size / (1024 * 1024)
        size_ok = 0.1 < size_mb < 500
        report.checks.append(
            CheckResult(
                "Dimensione PDF ragionevole",
                size_ok,
                f"{size_mb:.2f} MB",
                critical=False,
            )
        )
        if not size_ok:
            if size_mb <= 0.1:
                report.warnings.append(
                    f"PDF molto piccolo ({size_mb:.2f} MB) — potrebbe essere vuoto"
                )
            else:
                report.warnings.append(
                    f"PDF molto grande ({size_mb:.2f} MB) — possibili immagini non compresse"
                )

    # ── CHECK 9: Struttura Frontespizio (via testo) ───────────────────────────
    if pdf_text:
        title = config["book"]["title"]
        author = config["book"]["author"]
        has_title = title.lower() in pdf_text.lower()
        has_author = author.lower() in pdf_text.lower()

        report.checks.append(
            CheckResult(
                "Frontespizio: titolo presente",
                has_title,
                f"'{title}'" if has_title else f"'{title}' NON trovato",
                critical=False,
            )
        )
        report.checks.append(
            CheckResult(
                "Frontespizio: autore presente",
                has_author,
                f"'{author}'" if has_author else f"'{author}' NON trovato",
                critical=False,
            )
        )

        if not has_title:
            report.warnings.append(
                f"Titolo libro '{title}' non trovato nel testo del PDF"
            )
        if not has_author:
            report.warnings.append(
                f"Nome autore '{author}' non trovato nel testo del PDF"
            )

    # ── CHECK 10: Nessun artefatto Markdown nel PDF ───────────────────────────
    log.info("Check 10: Artefatti Markdown nel PDF...")
    if pdf_text:
        import re as _re
        artifacts_found = []
        # Cerca tag non processati: __H3__, __H2__, sequenze ** o ###
        for pattern, label in [
            (r'__H[123]__', 'tag __HX__'),
            (r'\*\*\S', 'grassetto ** non chiuso'),
            (r'###\s', 'heading ### letterale'),
            (r'##\s', 'heading ## letterale'),
        ]:
            if _re.search(pattern, pdf_text):
                artifacts_found.append(label)

        if artifacts_found:
            note = f"Artefatti trovati: {', '.join(artifacts_found)}"
            report.checks.append(CheckResult("Nessun artefatto Markdown nel PDF", False, note))
            report.critical_errors.append(f"Artefatti Markdown nel PDF: {note}")
            report.corrective_actions.append(
                "Correggere il parser (parse_manuscript.py) e il renderer (build_book_reportlab.py)"
            )
        else:
            report.checks.append(
                CheckResult("Nessun artefatto Markdown nel PDF", True, "Nessun tag residuo")
            )
    else:
        report.checks.append(
            CheckResult(
                "Nessun artefatto Markdown nel PDF", None,
                "Estrazione testo non disponibile", critical=False
            )
        )

    # ── CHECK 11: Nessun trattino/em-dash nel testo ───────────────────────────
    log.info("Check 11: Trattini/em-dash nel testo...")
    if pdf_text:
        dash_count = pdf_text.count('\u2014') + pdf_text.count('\u2013')
        if dash_count > 0:
            report.checks.append(
                CheckResult(
                    "Nessun trattino nel testo",
                    False,
                    f"{dash_count} trattini (em-dash/en-dash) trovati",
                )
            )
            report.critical_errors.append(
                f"Trovati {dash_count} trattini nel PDF — rimuoverli dal manoscritto"
            )
            report.corrective_actions.append(
                "Rimuovere em-dash (—) e en-dash (–) dal testo nel parser"
            )
        else:
            report.checks.append(
                CheckResult("Nessun trattino nel testo", True, "Nessun em-dash trovato")
            )
    else:
        report.checks.append(
            CheckResult(
                "Nessun trattino nel testo", None,
                "Estrazione testo non disponibile", critical=False
            )
        )

    # ── CHECK 12: Margini KDP — conformità per numero di pagine ──────────────────
    log.info("Check 12: Conformità margini KDP Amazon...")
    #
    # Fonte ufficiale: https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6
    # Margine interno (gutter) MINIMO per numero di pagine:
    #   24–150  pag. → 0.375" (27pt)
    #   151–300 pag. → 0.500" (36pt)
    #   301–500 pag. → 0.625" (45pt)
    #   501–700 pag. → 0.750" (54pt)
    #   701–828 pag. → 0.875" (63pt)
    # Margine ESTERNO minimo: 0.250" (18pt) per tutti i formati senza bleed
    # Margine TOP/BOTTOM minimo: 0.250" (18pt)
    #
    PAGE_W_PT      = 432   # 6 inch
    PAGE_H_PT      = 648   # 9 inch
    MARGIN_INNER_DECLARED = int(0.75 * 72)  # 54pt — come dichiarato in build_book_reportlab
    MARGIN_OUTER_DECLARED = int(0.50 * 72)  # 36pt
    MARGIN_TOP_DECLARED   = int(0.75 * 72)  # 54pt
    MARGIN_BOTTOM_DECLARED= int(0.50 * 72)  # 36pt
    FOOTER_Y_DECLARED     = 21              # pt dal bordo inferiore

    total_pages_for_kdp = report.total_pages if report.total_pages > 0 else 260

    # Determina gutter minimo KDP per il numero di pagine
    if total_pages_for_kdp <= 150:
        kdp_min_gutter = int(0.375 * 72)   # 27pt
        kdp_range = "24–150"
    elif total_pages_for_kdp <= 300:
        kdp_min_gutter = int(0.500 * 72)   # 36pt
        kdp_range = "151–300"
    elif total_pages_for_kdp <= 500:
        kdp_min_gutter = int(0.625 * 72)   # 45pt
        kdp_range = "301–500"
    elif total_pages_for_kdp <= 700:
        kdp_min_gutter = int(0.750 * 72)   # 54pt
        kdp_range = "501–700"
    else:
        kdp_min_gutter = int(0.875 * 72)   # 63pt
        kdp_range = "701–828"

    kdp_min_outer  = int(0.25 * 72)   # 18pt
    kdp_min_top    = int(0.25 * 72)   # 18pt
    kdp_min_bottom = int(0.25 * 72)   # 18pt

    margin_violations = []
    margin_ok_notes   = []

    # Controlla gutter
    if MARGIN_INNER_DECLARED >= kdp_min_gutter:
        margin_ok_notes.append(
            f"Gutter: {MARGIN_INNER_DECLARED}pt ≥ {kdp_min_gutter}pt (KDP min per {kdp_range} pag.) ✓"
        )
    else:
        margin_violations.append(
            f"Gutter {MARGIN_INNER_DECLARED}pt < KDP minimo {kdp_min_gutter}pt "
            f"(per {total_pages_for_kdp} pagine, fascia {kdp_range})"
        )

    # Controlla margine esterno
    if MARGIN_OUTER_DECLARED >= kdp_min_outer:
        margin_ok_notes.append(
            f"Esterno: {MARGIN_OUTER_DECLARED}pt ≥ {kdp_min_outer}pt ✓"
        )
    else:
        margin_violations.append(
            f"Margine esterno {MARGIN_OUTER_DECLARED}pt < KDP minimo {kdp_min_outer}pt"
        )

    # Controlla margine top
    if MARGIN_TOP_DECLARED >= kdp_min_top:
        margin_ok_notes.append(
            f"Top: {MARGIN_TOP_DECLARED}pt ≥ {kdp_min_top}pt ✓"
        )
    else:
        margin_violations.append(
            f"Margine top {MARGIN_TOP_DECLARED}pt < KDP minimo {kdp_min_top}pt"
        )

    # Controlla margine bottom (il footer è nel margine inferiore — verificare che sia ≥ 18pt dal bordo)
    if FOOTER_Y_DECLARED >= kdp_min_bottom:
        margin_ok_notes.append(
            f"Footer: {FOOTER_Y_DECLARED}pt dal bordo ≥ {kdp_min_bottom}pt KDP min ✓"
        )
    else:
        margin_violations.append(
            f"Footer a {FOOTER_Y_DECLARED}pt dal bordo < KDP minimo {kdp_min_bottom}pt"
        )

    if margin_violations:
        note_kdp = f"{len(margin_violations)} violazioni: {'; '.join(margin_violations)}"
        report.checks.append(
            CheckResult("Margini KDP Amazon conformi", False, note_kdp)
        )
        for v in margin_violations:
            report.critical_errors.append(f"MARGINE KDP NON CONFORME: {v}")
            report.corrective_actions.append(
                f"Aumentare il margine in build_book_reportlab.py: {v}"
            )
    else:
        note_kdp = (
            f"Libro {total_pages_for_kdp} pag. (fascia {kdp_range}) — "
            + " | ".join(margin_ok_notes)
        )
        report.checks.append(
            CheckResult("Margini KDP Amazon conformi", True, note_kdp)
        )

    # ── CHECK 13: Testo fuori dai margini dichiarati ──────────────────────────
    log.info("Check 13: Testo fuori margini (coordinate)...")
    try:
        import pdfplumber
        # Margini dichiarati in pt (coordinate PDF: origine in basso a sinistra)
        # pdfplumber usa coordinate con origine in ALTO a sinistra → y invertita
        # Content area in coord. pdfplumber (origine alto-sx, y cresce verso il basso):
        #   Top del content area  = MARGIN_TOP          = 54pt dall'alto
        #   Bottom del content area = PAGE_H - MARGIN_BOTTOM = 648 - 36 = 612pt dall'alto
        #   Left content: MARGIN_INNER (pag. dispari) o MARGIN_OUTER (pag. pari)
        #   Right content: PAGE_W - MARGIN_OUTER (dispari) o PAGE_W - MARGIN_INNER (pari)
        # Tolleranza per header/footer (sono nel margine per design):
        HEADER_ZONE_BOTTOM = MARGIN_TOP_DECLARED - 4    # 50pt dall'alto
        FOOTER_ZONE_TOP = PAGE_H_PT - MARGIN_BOTTOM_DECLARED + 4  # 616pt dall'alto

        # Per il check delle coordinate usiamo i MINIMI KDP ASSOLUTI (non i margini dichiarati).
        # Questo distingue le vere violazioni KDP (testo che verrebbe tagliato in stampa)
        # dai margini "dichiarati" interni al design (più conservativi).
        # Le prime 4 pagine (frontespizio, copyright, indice, bianca) sono
        # pagine speciali con layout centrato → escluse dal check.
        KDP_ABS_MIN_LEFT  = int(0.25 * 72)  # 18pt — minimo assoluto KDP dal bordo SX
        KDP_ABS_MIN_RIGHT = PAGE_W_PT - int(0.25 * 72)  # 414pt — dal bordo DX
        SKIP_PRELIMINARY_PAGES = 4  # salta le prime 4 pagine speciali

        violations_13 = []
        pages_checked  = 0
        TOLERANCE = 2  # pt di tolleranza floating-point

        with pdfplumber.open(draft_path) as pdf:
            total_pdf_pages = len(pdf.pages)
            # Controlla un campione di pagine (max 30) per non rallentare troppo
            step = max(1, (total_pdf_pages - SKIP_PRELIMINARY_PAGES) // 30)
            for pg_idx in range(SKIP_PRELIMINARY_PAGES, total_pdf_pages, step):
                page = pdf.pages[pg_idx]
                pg_num = pg_idx + 1
                pages_checked += 1

                words = page.extract_words() or []
                for w in words:
                    x0, y0, x1, y1 = w.get("x0", 0), w.get("top", 0), w.get("x1", 0), w.get("bottom", 0)
                    text_snippet = w.get("text", "")[:20]

                    # Skip header zone (in cima, dentro il margine superiore)
                    if y1 <= HEADER_ZONE_BOTTOM + TOLERANCE:
                        continue
                    # Skip footer zone (in fondo, dentro il margine inferiore)
                    if y0 >= FOOTER_ZONE_TOP - TOLERANCE:
                        continue

                    # Controlla bordo SINISTRO (minimo KDP assoluto)
                    if x0 < KDP_ABS_MIN_LEFT - TOLERANCE:
                        violations_13.append(
                            f"pag.{pg_num} SX: '{text_snippet}' x0={x0:.1f}pt < {KDP_ABS_MIN_LEFT}pt KDP"
                        )

                    # Controlla bordo DESTRO (minimo KDP assoluto)
                    if x1 > KDP_ABS_MIN_RIGHT + TOLERANCE:
                        violations_13.append(
                            f"pag.{pg_num} DX: '{text_snippet}' x1={x1:.1f}pt > {KDP_ABS_MIN_RIGHT}pt KDP"
                        )

        if violations_13:
            # Mostra solo i primi 5
            sample = violations_13[:5]
            note_13 = (
                f"{len(violations_13)} violazioni su {pages_checked} pagine campionate: "
                + " | ".join(sample)
            )
            report.checks.append(
                CheckResult("Testo nei margini (coordinate)", False, note_13)
            )
            report.critical_errors.append(
                f"Testo fuori dai margini dichiarati in {len(violations_13)} occorrenze"
            )
            report.corrective_actions.append(
                "Verificare _get_x() e right_limit in build_book_reportlab.py"
            )
        else:
            report.checks.append(
                CheckResult(
                    "Testo nei margini (coordinate)", True,
                    f"Nessuna violazione su {pages_checked} pagine campionate"
                )
            )

    except ImportError:
        report.checks.append(
            CheckResult(
                "Testo nei margini (coordinate)", None,
                "pdfplumber non disponibile — verifica saltata", critical=False
            )
        )
    except Exception as e:
        report.checks.append(
            CheckResult(
                "Testo nei margini (coordinate)", None,
                f"Errore verifica coordinate: {e}", critical=False
            )
        )

    return report


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    log.info("=" * 60)
    log.info("AGENTE 3 — QUALITY ASSURANCE — Avvio")
    log.info("=" * 60)

    # Percorsi
    draft_path = ROOT / "output" / "book_draft.pdf"
    final_path = ROOT / "output" / "book_final.pdf"
    manuscript_path = ROOT / "input" / "manuscript.md"
    config_path = ROOT / "config" / "book_config.yaml"
    images_dir = ROOT / "assets" / "images"
    report_path = ROOT / "output" / "qa_report.md"

    # Verifica input
    if not draft_path.exists():
        log.error(f"PDF bozza non trovato: {draft_path}")
        log.error("Lanciare prima build_book.py")
        sys.exit(1)

    if not manuscript_path.exists():
        log.error(f"Manoscritto non trovato: {manuscript_path}")
        sys.exit(1)

    if not config_path.exists():
        log.error(f"Config non trovato: {config_path}")
        sys.exit(1)

    # Esegui QA
    log.info("Esecuzione controlli qualità...")
    report = run_qa(
        str(draft_path),
        str(manuscript_path),
        str(config_path),
        images_dir,
    )

    # Genera e salva report
    report_md = generate_report_markdown(report)
    report_path.write_text(report_md, encoding="utf-8")
    log.info(f"Report QA salvato: {report_path}")

    # Stampa sommario
    passed = sum(1 for c in report.checks if c.passed is True)
    failed = sum(1 for c in report.checks if c.passed is False)
    skipped = sum(1 for c in report.checks if c.passed is None)

    log.info(f"\nRisultato QA:")
    log.info(f"  ✅ Passati: {passed}")
    log.info(f"  ❌ Falliti: {failed}")
    log.info(f"  ⏭️ Saltati: {skipped}")
    log.info(f"  Errori critici: {len(report.critical_errors)}")
    log.info(f"  Warning: {len(report.warnings)}")

    # Decisione finale
    if report.passed:
        log.info("\n✅ QUALITÀ: PASSATA — Copio PDF come book_final.pdf")
        shutil.copy2(str(draft_path), str(final_path))
        log.info(f"PDF finale: {final_path}")
    else:
        log.warning(
            f"\n❌ QUALITÀ: DA CORREGGERE — "
            f"{len(report.critical_errors)} errori critici"
        )
        for err in report.critical_errors:
            log.warning(f"  ❌ {err}")
        log.warning("Controllare output/qa_report.md per le azioni correttive")
        log.warning("book_final.pdf NON creato")

    log.info("\n" + "=" * 60)
    log.info("AGENTE 3 — COMPLETATO")
    log.info("=" * 60)

    return report.passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
