#!/usr/bin/env python3
"""
quality_check.py — QA Automatico HTML
Digital Empire | Website Creator System

Verifica che un file index.html rispetti le 5 Leggi d'Oro (K01) e la Legge Cosmica (K00).

Uso:
    python quality_check.py index.html
    python quality_check.py trading-ebook.html --verbose
    python quality_check.py mysite.html --fix-report
"""

import sys
import re
import argparse
import colorsys
from pathlib import Path


# =============================================================================
# COSTANTI
# =============================================================================

# Colori vietati (K00) — saturazione 100%, primari puri
FORBIDDEN_COLORS = {
    '#FF0000', '#FF0000', '#00FF00', '#0000FF',
    '#FFFF00', '#FF00FF', '#00FFFF',
    '#FF3300', '#FF6600', '#FF9900',  # arancioni puri
    '#33FF00', '#66FF00', '#99FF00',  # verdi puri
    '#0033FF', '#0066FF', '#0099FF',  # blu puri
}

# Soglia saturazione per warning K00
SAT_WARNING_THRESHOLD = 70  # %

# URL grain (Layer 1 — K02)
GRAIN_URL_PATTERN = 'grainy-gradients.vercel.app/noise.svg'

# Pattern feTurbulence (Layer 2 — K02)
GRAIN_NOISE_PATTERN = 'feTurbulence'

# Pattern per SVG divisori (K01 Legge 4)
SVG_DIVIDER_PATTERNS = [
    r'linearGradient.*94A3B8',  # gradient metallic silver
    r'stroke.*94A3B8',          # stroke silver
    r'stroke.*E3C878',          # stroke gold
    r'luxArcGrad|luxVGrad|curveLineGrad|triGrad',  # ID gradient divisori
]

# Pattern per clip-path curvo (K01 Legge 5)
CURVE_PATTERNS = [
    r'clip-path.*Q\s',          # quadratic bezier inline
    r'clip-path.*ellipse',      # ellipse
    r'clip-path.*url\(#',       # SVG clipPath
    r'clipPathUnits.*objectBoundingBox',  # SVG clipPath con Q
    r'<path.*Q\s.*clip',        # path con Q in clipPath
]


# =============================================================================
# PARSER HTML (semplice, senza BeautifulSoup)
# =============================================================================

def read_file(path: str) -> str:
    """Legge il file HTML."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"\n  ❌ File non trovato: {path}")
        sys.exit(1)
    except Exception as e:
        print(f"\n  ❌ Errore lettura file: {e}")
        sys.exit(1)


def find_sections(html: str) -> list:
    """Trova tutti i blocchi <section> con il loro contenuto."""
    pattern = re.compile(r'<section[^>]*>(.*?)</section>', re.DOTALL | re.IGNORECASE)
    return pattern.findall(html)


def find_all_hex_colors(html: str) -> list:
    """Estrae tutti i colori hex dal file."""
    # Trova hex nel formato #RRGGBB e #RGB
    pattern = re.compile(r'#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})\b')
    matches = pattern.findall(html)
    colors = []
    for m in matches:
        if len(m) == 3:
            m = m[0]*2 + m[1]*2 + m[2]*2
        colors.append('#' + m.upper())
    return list(set(colors))


def find_paragraphs_and_lists(html: str) -> dict:
    """Trova tutti i <p> e <li> e verifica presenza di <strong>."""
    p_pattern = re.compile(r'<p[^>]*>(.*?)</p>', re.DOTALL | re.IGNORECASE)
    li_pattern = re.compile(r'<li[^>]*>(.*?)</li>', re.DOTALL | re.IGNORECASE)

    p_elements = p_pattern.findall(html)
    li_elements = li_pattern.findall(html)

    p_without_strong = [p for p in p_elements if '<strong' not in p.lower() and len(p.strip()) > 30]
    li_without_strong = [li for li in li_elements if '<strong' not in li.lower() and len(li.strip()) > 20]

    return {
        'p_total': len(p_elements),
        'li_total': len(li_elements),
        'p_without_strong': len(p_without_strong),
        'li_without_strong': len(li_without_strong),
        'p_samples': p_without_strong[:3],  # primi 3 per debug
        'li_samples': li_without_strong[:3],
    }


def hex_to_hsl(hex_str: str) -> tuple:
    """Converte hex in HSL (H 0-360, S 0-100, L 0-100)."""
    hex_str = hex_str.lstrip('#')
    r = int(hex_str[0:2], 16) / 255
    g = int(hex_str[2:4], 16) / 255
    b = int(hex_str[4:6], 16) / 255
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (h * 360, s * 100, l * 100)


def check_color_violation(hex_color: str) -> tuple:
    """
    Controlla se un hex viola K00.
    Returns (is_violation, severity, message)
    """
    if hex_color in FORBIDDEN_COLORS:
        return (True, 'ERROR', f'colore primario puro VIETATO')

    try:
        h, s, l = hex_to_hsl(hex_color)
    except Exception:
        return (False, 'OK', '')

    # Ignora bianchi, neri, grigi (saturazione < 5%)
    if s < 5:
        return (False, 'OK', '')

    # Ignora colori molto scuri o molto chiari (probabilmente sfondo/testo)
    if l < 8 or l > 92:
        return (False, 'OK', '')

    if s > SAT_WARNING_THRESHOLD:
        return (True, 'WARNING', f'saturazione {s:.0f}% > {SAT_WARNING_THRESHOLD}% — argentizza')

    return (False, 'OK', '')


# =============================================================================
# CHECKS
# =============================================================================

def check_k00_colors(html: str, verbose: bool = False) -> dict:
    """CHECK K00: Nessun colore saturo puro."""
    colors = find_all_hex_colors(html)
    violations = []
    warnings = []

    for color in colors:
        is_viol, severity, msg = check_color_violation(color)
        if is_viol:
            if severity == 'ERROR':
                violations.append(f'{color} — {msg}')
            else:
                warnings.append(f'{color} — {msg}')

    passed = len(violations) == 0
    return {
        'name': 'K00 — Silver Mixing',
        'passed': passed,
        'errors': violations,
        'warnings': warnings,
        'total_colors': len(colors),
    }


def check_k01_grain(html: str) -> dict:
    """CHECK K01 Legge 1: Grain in ogni sezione."""
    sections = find_sections(html)
    sections_without_grain = []

    for i, section in enumerate(sections, 1):
        has_layer1 = GRAIN_URL_PATTERN in section
        has_layer2 = GRAIN_NOISE_PATTERN in section
        if not has_layer1 and not has_layer2:
            sections_without_grain.append(f'sezione #{i}')

    passed = len(sections_without_grain) == 0
    return {
        'name': 'K01 L1 — Grain in ogni sezione',
        'passed': passed,
        'errors': [f'{s} manca grain layer' for s in sections_without_grain],
        'warnings': [],
        'total_sections': len(sections),
    }


def check_k01_pattern_interrupt(html: str) -> dict:
    """CHECK K01 Legge 2: Pattern interrupt dark↔light."""
    # Cerca sezioni con sfondi chiari
    light_patterns = [
        r'background[^;]*#DCD8CF',
        r'background[^;]*#F8F6F2',
        r'background[^;]*#E8E',
        r'background[^;]*#F0E',
        r'section-light',
        r'bg-interrupt',
        r'bg-beige',
    ]

    has_light = any(re.search(p, html, re.IGNORECASE) for p in light_patterns)

    sections = find_sections(html)
    passed = has_light and len(sections) >= 3

    return {
        'name': 'K01 L2 — Pattern interrupt dark↔light',
        'passed': passed,
        'errors': [] if passed else ['nessuna sezione chiara trovata — aggiungi almeno 1 sezione light (es. FAQ, beige)'],
        'warnings': [],
        'sections_found': len(sections),
    }


def check_k01_lowercase(html: str) -> dict:
    """CHECK K01 Legge 3A: Headings in lowercase (spot check)."""
    # Cerca h1/h2 con testo tutto uppercase (segnale di violazione)
    heading_pattern = re.compile(r'<h[12][^>]*>(.*?)</h[12]>', re.DOTALL | re.IGNORECASE)
    headings = heading_pattern.findall(html)

    violations = []
    for h in headings:
        # Rimuovi tag HTML interni
        text = re.sub(r'<[^>]+>', '', h).strip()
        if text and text == text.upper() and len(text) > 3 and not text.isdigit():
            violations.append(text[:50])

    passed = len(violations) == 0
    return {
        'name': 'K01 L3A — Lowercase headings',
        'passed': passed,
        'errors': [f'heading in maiuscolo: "{v}"' for v in violations],
        'warnings': [],
    }


def check_k01_strong(html: str) -> dict:
    """CHECK K01 Legge 3B: <strong> in ogni <p> e <li>."""
    result = find_paragraphs_and_lists(html)

    errors = []
    if result['p_without_strong'] > 0:
        errors.append(f"{result['p_without_strong']}/{result['p_total']} paragrafi <p> senza <strong>")
    if result['li_without_strong'] > 0:
        errors.append(f"{result['li_without_strong']}/{result['li_total']} list items <li> senza <strong>")

    passed = len(errors) == 0
    return {
        'name': 'K01 L3B — <strong> in ogni <p> e <li>',
        'passed': passed,
        'errors': errors,
        'warnings': [],
        'p_total': result['p_total'],
        'li_total': result['li_total'],
    }


def check_k01_svg_divider(html: str) -> dict:
    """CHECK K01 Legge 4: Almeno 1 SVG divider notevole."""
    has_svg_divider = any(
        re.search(p, html, re.DOTALL | re.IGNORECASE)
        for p in SVG_DIVIDER_PATTERNS
    )

    # Check alternativo: cerca SVG con stroke e gradient
    has_svg_stroke = bool(re.search(r'<svg[^>]*>.*?stroke.*?</svg>', html, re.DOTALL | re.IGNORECASE))
    has_linear_grad = 'linearGradient' in html

    passed = has_svg_divider or (has_svg_stroke and has_linear_grad)

    return {
        'name': 'K01 L4 — SVG divider metallico',
        'passed': passed,
        'errors': [] if passed else ['nessun SVG divider con gradient metallic trovato — aggiungi un LuxArc, LuxV o InclinedStrip (vedi K03)'],
        'warnings': [],
    }


def check_k01_curve(html: str) -> dict:
    """CHECK K01 Legge 5: Almeno 1 sezione con bordo curvo."""
    has_curve = any(
        re.search(p, html, re.DOTALL | re.IGNORECASE)
        for p in CURVE_PATTERNS
    )

    return {
        'name': 'K01 L5 — Sezione con bordo curvo',
        'passed': has_curve,
        'errors': [] if has_curve else ['nessuna sezione curva trovata — aggiungi clip-path con Q (quadratic bezier) o ellipse (vedi K03 LuxCurve)'],
        'warnings': [],
    }


def check_mobile_responsive(html: str) -> dict:
    """CHECK extra: Media query per mobile."""
    has_media_query = '@media' in html and ('max-width' in html or 'min-width' in html)
    has_viewport = 'viewport' in html

    errors = []
    if not has_viewport:
        errors.append('manca <meta name="viewport"> nell\'<head>')
    if not has_media_query:
        errors.append('nessuna @media query trovata — aggiungi responsive CSS')

    passed = len(errors) == 0
    return {
        'name': 'EXTRA — Mobile responsive',
        'passed': passed,
        'errors': errors,
        'warnings': [],
    }


def check_fonts(html: str) -> dict:
    """CHECK extra: Font Google Fonts caricato."""
    has_cinzel = 'Cinzel' in html
    has_inter = 'Inter' in html
    has_fonts_link = 'fonts.googleapis.com' in html

    errors = []
    warnings = []
    if not has_fonts_link:
        errors.append('Google Fonts non caricato nell\'<head>')
    if not has_cinzel:
        warnings.append("font 'Cinzel' non trovato — necessario per headline premium")
    if not has_inter:
        warnings.append("font 'Inter' non trovato — raccomandato per body text")

    passed = len(errors) == 0
    return {
        'name': 'EXTRA — Google Fonts',
        'passed': passed,
        'errors': errors,
        'warnings': warnings,
    }


# =============================================================================
# REPORT
# =============================================================================

def print_report(checks: list, html_path: str, verbose: bool = False) -> int:
    """Stampa il report completo. Returns numero di errori totali."""

    passed_count = sum(1 for c in checks if c['passed'])
    failed_count = len(checks) - passed_count
    total_errors = sum(len(c['errors']) for c in checks)
    total_warnings = sum(len(c.get('warnings', [])) for c in checks)

    print()
    print("=" * 65)
    print(f"  QUALITY CHECK — {Path(html_path).name}")
    print("=" * 65)
    print()

    for check in checks:
        icon = "✅" if check['passed'] else "❌"
        print(f"  {icon} {check['name']}")

        if not check['passed'] or verbose:
            for err in check.get('errors', []):
                print(f"       ❌ {err}")

        if verbose or (not check['passed'] and check.get('warnings')):
            for warn in check.get('warnings', []):
                print(f"       ⚠  {warn}")

        # Info aggiuntive
        if verbose:
            if 'total_sections' in check:
                print(f"       ℹ  {check['total_sections']} sezioni trovate")
            if 'total_colors' in check:
                print(f"       ℹ  {check['total_colors']} colori hex analizzati")
            if 'p_total' in check:
                print(f"       ℹ  {check['p_total']} paragrafi, {check.get('li_total',0)} list items")

        print()

    # Sommario
    print("-" * 65)
    print(f"  Risultato: {passed_count}/{len(checks)} check passati")
    if total_errors > 0:
        print(f"  ❌ {total_errors} errori da correggere")
    if total_warnings > 0:
        print(f"  ⚠  {total_warnings} warning da valutare")
    if total_errors == 0:
        print("  ✅ Il file rispetta le 5 Leggi d'Oro e la Legge Cosmica!")
    print("=" * 65)
    print()

    # Istruzioni correzione
    if total_errors > 0:
        print("  COME CORREGGERE:")
        for check in checks:
            if not check['passed'] and check['errors']:
                print(f"\n  [{check['name']}]")
                for err in check['errors']:
                    print(f"    → {err}")
        print()

    return total_errors


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Quality Check HTML — verifica K00 + K01 (5 Leggi d\'Oro)',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('file', help='Path al file HTML da verificare')
    parser.add_argument('--verbose', '-v', action='store_true', help='Output dettagliato')
    parser.add_argument('--fix-report', '-f', action='store_true', help='Mostra solo gli errori da correggere')

    args = parser.parse_args()

    html = read_file(args.file)

    verbose = args.verbose and not args.fix_report

    checks = [
        check_k00_colors(html, verbose),
        check_k01_grain(html),
        check_k01_pattern_interrupt(html),
        check_k01_lowercase(html),
        check_k01_strong(html),
        check_k01_svg_divider(html),
        check_k01_curve(html),
        check_mobile_responsive(html),
        check_fonts(html),
    ]

    error_count = print_report(checks, args.file, verbose)

    sys.exit(0 if error_count == 0 else 1)


if __name__ == '__main__':
    main()
