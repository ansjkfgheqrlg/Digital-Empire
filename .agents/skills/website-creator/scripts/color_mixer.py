#!/usr/bin/env python3
"""
color_mixer.py — Silver Mixing Utility
Digital Empire | Website Creator System

Converte qualsiasi colore hex in una palette argentizzata a 5 varianti.
Implementa l'algoritmo K00 Legge Cosmica.

Uso:
    python color_mixer.py #8B00FF
    python color_mixer.py 8B00FF
    python color_mixer.py --palette violet
"""

import sys
import colorsys
import argparse


# =============================================================================
# ALGORITMO SILVER MIXING (K00)
# =============================================================================

SILVER_BASE = (0x94, 0xA3, 0xB8)  # #94A3B8 — cool silver base
SILVER_BLEND_RATIO = 0.35          # 35% blend con silver


def hex_to_rgb(hex_str: str) -> tuple:
    """Converte hex string in tupla RGB (0-255)."""
    hex_str = hex_str.lstrip('#')
    if len(hex_str) != 6:
        raise ValueError(f"Hex non valido: #{hex_str}. Usa formato #RRGGBB.")
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return (r, g, b)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Converte RGB in hex string."""
    return '#{:02X}{:02X}{:02X}'.format(
        max(0, min(255, int(r))),
        max(0, min(255, int(g))),
        max(0, min(255, int(b)))
    )


def rgb_to_hsl(r: int, g: int, b: int) -> tuple:
    """Converte RGB (0-255) in HSL (0-360, 0-100, 0-100)."""
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    return (h * 360, s * 100, l * 100)


def hsl_to_rgb(h: float, s: float, l: float) -> tuple:
    """Converte HSL (0-360, 0-100, 0-100) in RGB (0-255)."""
    r, g, b = colorsys.hls_to_rgb(h/360, l/100, s/100)
    return (int(r * 255), int(g * 255), int(b * 255))


def blend_with_silver(rgb: tuple, ratio: float = SILVER_BLEND_RATIO) -> tuple:
    """Blenda un colore RGB con silver base (#94A3B8) nella percentuale indicata."""
    r = rgb[0] * (1 - ratio) + SILVER_BASE[0] * ratio
    g = rgb[1] * (1 - ratio) + SILVER_BASE[1] * ratio
    b = rgb[2] * (1 - ratio) + SILVER_BASE[2] * ratio
    return (r, g, b)


def argentize(hex_input: str) -> dict:
    """
    Applica l'algoritmo K00 Silver Mixing a un colore hex.

    Algoritmo:
    1. Converti in HSL
    2. Abbassa saturazione del 40%
    3. Sposta hue verso 215° del 25%
    4. Blenda 35% con #94A3B8

    Returns: dizionario con 5 varianti argentizzate
    """
    rgb = hex_to_rgb(hex_input)
    h, s, l = rgb_to_hsl(*rgb)

    # Step 1: abbassa saturazione del 40%
    s_new = max(0, s * 0.60)

    # Step 2: sposta hue verso 215° del 25%
    target_hue = 215
    h_new = h + (target_hue - h) * 0.25

    # Step 3: converti di nuovo in RGB
    rgb_desaturated = hsl_to_rgb(h_new, s_new, l)

    # Step 4: blend 35% con silver
    rgb_silver = blend_with_silver(rgb_desaturated, SILVER_BLEND_RATIO)

    # Variante principale
    main = rgb_to_hex(*rgb_silver)

    # Variante più scura (per background)
    h2, s2, l2 = rgb_to_hsl(*rgb_silver)
    bg_rgb = hsl_to_rgb(h2, s2 * 0.5, max(5, l2 * 0.25))
    bg_dark = rgb_to_hex(*bg_rgb)

    # Variante chiara (per sezioni light)
    bg_light_rgb = hsl_to_rgb(h2, s2 * 0.2, 88)
    bg_light = rgb_to_hex(*bg_light_rgb)

    # Variante border (più trasparente — usare con rgba)
    border_rgb = hsl_to_rgb(h2, s2 * 0.8, min(90, l2 * 1.3))
    border = rgb_to_hex(*border_rgb)

    # Variante text (per strong su sfondo scuro)
    text_rgb = hsl_to_rgb(h2, s2 * 0.6, min(90, l2 * 1.5))
    text = rgb_to_hex(*text_rgb)

    return {
        'input':      hex_input.upper() if hex_input.startswith('#') else '#' + hex_input.upper(),
        'primary':    main,
        'bg_dark':    bg_dark,
        'bg_light':   bg_light,
        'border':     border,
        'text':       text,
        'hsl_input':  (round(h, 1), round(s, 1), round(l, 1)),
        'hsl_output': (round(h_new, 1), round(s_new, 1), round(l, 1)),
    }


# =============================================================================
# PALETTE PREDEFINITE (K04)
# =============================================================================

NAMED_PALETTES = {
    'gold':     '#FFD700',
    'green':    '#00AA55',
    'violet':   '#8B00FF',
    'red':      '#FF2200',
    'blue':     '#0055FF',
    'cyan':     '#00CCDD',
    'pink':     '#FF4488',
    'orange':   '#FF6600',
    'teal':     '#009688',
    'navy':     '#003388',
    'emerald':  '#00AA44',
    'burgundy': '#880033',
}


# =============================================================================
# OUTPUT
# =============================================================================

def print_css_variables(result: dict, palette_name: str = 'custom') -> None:
    """Stampa le variabili CSS pronte per l'uso."""

    print()
    print("=" * 60)
    print(f"  SILVER MIXER — {result['input']} → argentizzato")
    print("=" * 60)
    print()

    # Info conversione
    print(f"  HSL input:  H:{result['hsl_input'][0]}° S:{result['hsl_input'][1]:.0f}% L:{result['hsl_input'][2]:.0f}%")
    print(f"  HSL output: H:{result['hsl_output'][0]:.0f}° S:{result['hsl_output'][1]:.0f}% (sat -40%, hue →215°, blend 35% silver)")
    print()

    # Controllo saturazione
    if result['hsl_input'][1] > 70:
        print(f"  ⚠  ATTENZIONE: saturazione originale {result['hsl_input'][1]:.0f}% > 70%")
        print(f"     Il colore originale VIOLEREBBE K00 — usa la versione argentizzata.")
        print()

    print("  CSS Variables pronte:")
    print()
    print("  :root {")
    print(f"    --color-primary:   {result['primary']};")
    print(f"    --color-bg-dark:   {result['bg_dark']};")
    print(f"    --color-bg-light:  {result['bg_light']};")
    print(f"    --color-border:    {result['border']};")
    print(f"    --color-text:      {result['text']};")
    print(f"    /* Silver base (invariante) */")
    print(f"    --silver-cool:     #94A3B8;")
    print(f"    --silver-light:    #E2E8F0;")
    print(f"    --silver-dark:     #64748B;")
    print(f"  }}")
    print()

    print("  Gradient accent (per divisori e decorazioni):")
    print(f"  linear-gradient(90deg, #94A3B8 0%, #E2E8F0 20%, {result['primary']} 45%, #FFFFFF 50%, {result['primary']} 55%, #E2E8F0 80%, #94A3B8 100%)")
    print()

    print("  Colore bordo trasparente (rgba per border su card):")
    r, g, b = hex_to_rgb(result['border'])
    print(f"  rgba({r},{g},{b},0.3)  ← hover state")
    print(f"  rgba({r},{g},{b},0.08) ← background subtile")
    print()

    # Gradient hero suggerito
    print("  Gradient hero suggerito:")
    r1, g1, b1 = hex_to_rgb(result['bg_dark'])
    print(f"  background: linear-gradient(135deg, {result['bg_dark']} 0%, {result['bg_dark']} 50%, {result['bg_dark']} 100%);")
    print()

    print("=" * 60)
    print()


def check_violations(hex_input: str) -> None:
    """Controlla se un colore viola K00."""
    rgb = hex_to_rgb(hex_input)
    h, s, l = rgb_to_hsl(*rgb)

    FORBIDDEN = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']
    hex_upper = hex_input.upper()
    if not hex_upper.startswith('#'):
        hex_upper = '#' + hex_upper

    if hex_upper in FORBIDDEN:
        print(f"\n  ❌ VIOLAZIONE K00: {hex_upper} è un colore primario VIETATO!")
    elif s > 70:
        print(f"\n  ⚠  ATTENZIONE K00: saturazione {s:.0f}% > 70% — argentizza obbligatoriamente.")
    else:
        print(f"\n  ✓  Saturazione {s:.0f}% — potenzialmente accettabile, ma verifica sempre.")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Silver Mixer — converte colori hex in versioni argentizzate (K00 Legge Cosmica)',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'color',
        nargs='?',
        help='Colore hex (es: #8B00FF o 8B00FF) o nome palette (gold, violet, red, blue, ...)'
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='Mostra tutte le palette named disponibili'
    )
    parser.add_argument(
        '--check', '-c',
        action='store_true',
        help='Controlla solo se il colore viola K00 (senza argentizzare)'
    )

    args = parser.parse_args()

    if args.list:
        print("\n  Palette named disponibili:")
        for name, hex_val in NAMED_PALETTES.items():
            result = argentize(hex_val)
            print(f"  {name:12s} → {hex_val} → {result['primary']}")
        print()
        return

    if not args.color:
        parser.print_help()
        print("\n  Esempi:")
        print("    python color_mixer.py #8B00FF")
        print("    python color_mixer.py violet")
        print("    python color_mixer.py --list")
        return

    # Risolvi nome palette
    color_input = args.color.strip()
    if color_input.lower() in NAMED_PALETTES:
        hex_input = NAMED_PALETTES[color_input.lower()]
        print(f"\n  Palette '{color_input}' → {hex_input}")
    else:
        hex_input = color_input

    # Normalizza
    if not hex_input.startswith('#'):
        hex_input = '#' + hex_input

    try:
        hex_to_rgb(hex_input)  # Valida
    except ValueError as e:
        print(f"\n  Errore: {e}")
        sys.exit(1)

    if args.check:
        check_violations(hex_input)
        return

    result = argentize(hex_input)
    print_css_variables(result)


if __name__ == '__main__':
    main()
