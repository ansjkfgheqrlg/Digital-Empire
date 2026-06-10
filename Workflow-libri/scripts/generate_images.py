"""
generate_images.py — Agente 1: Image Generator

Genera le immagini del libro usando l'API configurata (default: OpenAI DALL-E 3).
Per ogni capitolo in image_prompts.yaml, genera chapter_XX.png in assets/images/.

Uso:
    python scripts/generate_images.py

Variabili d'ambiente richieste:
    OPENAI_API_KEY — per OpenAI/DALL-E 3

Modalità offline (--placeholder):
    python scripts/generate_images.py --placeholder
    Genera solo placeholder grigi, utile per testare il layout senza API.
"""

import os
import sys
import time
import yaml
import logging
import argparse
from pathlib import Path
from io import BytesIO

# Aggiungi la directory root al path
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

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
        logging.FileHandler(
            ROOT / "output" / "image_generation_log.txt", encoding="utf-8"
        ),
    ]
)
log = logging.getLogger("generate_images")


# ── Placeholder Generator ─────────────────────────────────────────────────────

def create_placeholder_image(chapter_num: int, chapter_title: str = "", output_path: Path = None) -> Path:
    """
    Crea un'immagine placeholder grigia 1024x1792 con testo centrato.
    Usa Pillow.
    """
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        log.error("Pillow non installato. Esegui: pip install Pillow")
        sys.exit(1)

    width, height = 1024, 1792
    img = Image.new("RGB", (width, height), color=(180, 180, 180))
    draw = ImageDraw.Draw(img)

    # Testo placeholder
    lines = [
        "PLACEHOLDER",
        f"Capitolo {chapter_num:02d}",
    ]
    if chapter_title:
        # Spezza titolo lungo
        words = chapter_title.split()
        line = ""
        for word in words:
            if len(line + " " + word) <= 25:
                line = (line + " " + word).strip()
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)

    lines.append("")
    lines.append("Rigenerare manualmente")

    # Prova a caricare un font
    font_large = None
    font_small = None
    try:
        # Cerca font di sistema su Windows
        font_paths = [
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/calibri.ttf",
            "C:/Windows/Fonts/Georgia.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]
        for fp in font_paths:
            if Path(fp).exists():
                font_large = ImageFont.truetype(fp, 60)
                font_small = ImageFont.truetype(fp, 36)
                break
    except Exception:
        pass

    if font_large is None:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Calcola altezza totale testo
    line_heights = []
    for i, line in enumerate(lines):
        font = font_large if i < 2 else font_small
        try:
            bbox = draw.textbbox((0, 0), line, font=font)
            lh = bbox[3] - bbox[1]
        except Exception:
            lh = 60 if i < 2 else 40
        line_heights.append(lh)

    total_text_height = sum(line_heights) + (len(lines) - 1) * 20
    y_start = (height - total_text_height) // 2

    y = y_start
    for i, line in enumerate(lines):
        font = font_large if i < 2 else font_small
        try:
            bbox = draw.textbbox((0, 0), line, font=font)
            text_w = bbox[2] - bbox[0]
        except Exception:
            text_w = len(line) * 30

        x = (width - text_w) // 2
        draw.text((x, y), line, fill=(80, 80, 80), font=font)
        y += line_heights[i] + 20

    # Bordo
    draw.rectangle(
        [(30, 30), (width - 30, height - 30)],
        outline=(120, 120, 120),
        width=4
    )

    # Salva
    if output_path is None:
        output_path = ROOT / "assets" / "images" / f"chapter_{chapter_num:02d}.png"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(output_path), "PNG")
    log.info(f"  Placeholder creato: {output_path.name} ({width}x{height})")
    return output_path


# ── OpenAI DALL-E 3 ───────────────────────────────────────────────────────────

def generate_with_openai(
    prompt: str,
    chapter_num: int,
    config: dict,
    output_path: Path,
    max_retries: int = 3,
) -> bool:
    """
    Genera un'immagine con OpenAI DALL-E 3.
    Ritorna True se successo, False se tutti i retry falliscono.
    """
    try:
        import openai
        import requests
    except ImportError:
        log.error("openai o requests non installato. Esegui: pip install openai requests")
        return False

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        log.error(
            "OPENAI_API_KEY non trovato nell'ambiente. "
            "Impostare la variabile d'ambiente o usare --placeholder."
        )
        return False

    client = openai.OpenAI(api_key=api_key)

    img_config = config.get("images", {})
    model = img_config.get("model", "dall-e-3")
    size = img_config.get("size", "1024x1792")
    quality = img_config.get("quality", "hd")
    style = img_config.get("style", "natural")

    # Aggiungi suffisso per coerenza stile e no-testo
    full_prompt = (
        f"{prompt} "
        f"No text, no letters, no words, no writing in the image. "
        f"Professional book illustration, high quality."
    )

    for attempt in range(1, max_retries + 1):
        try:
            log.info(
                f"  Capitolo {chapter_num:02d}: tentativo {attempt}/{max_retries} "
                f"— DALL-E {model}"
            )

            response = client.images.generate(
                model=model,
                prompt=full_prompt,
                size=size,
                quality=quality,
                style=style,
                n=1,
            )

            image_url = response.data[0].url
            log.info(f"  Capitolo {chapter_num:02d}: immagine generata, download...")

            # Scarica l'immagine
            img_response = requests.get(image_url, timeout=60)
            img_response.raise_for_status()

            # Verifica e salva con Pillow
            try:
                from PIL import Image
                img = Image.open(BytesIO(img_response.content))
                w, h = img.size
                log.info(
                    f"  Capitolo {chapter_num:02d}: dimensioni {w}x{h}px"
                )
            except Exception as e:
                log.warning(f"  Impossibile verificare con Pillow: {e}")

            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(img_response.content)
            log.info(
                f"  Capitolo {chapter_num:02d}: ✅ salvata → {output_path.name} "
                f"({output_path.stat().st_size / 1024:.0f} KB)"
            )
            return True

        except openai.RateLimitError as e:
            wait_time = 30 * attempt
            log.warning(
                f"  Rate limit raggiunto. Attendo {wait_time}s prima del retry..."
            )
            time.sleep(wait_time)

        except openai.BadRequestError as e:
            log.error(f"  Prompt rifiutato dall'API (content policy): {e}")
            return False  # Non ritentare — il prompt è il problema

        except Exception as e:
            wait_time = 5 * attempt
            log.warning(
                f"  Errore tentativo {attempt}: {e}. "
                f"Attendo {wait_time}s..."
            )
            if attempt < max_retries:
                time.sleep(wait_time)

    log.error(f"  Capitolo {chapter_num:02d}: ❌ tutti i retry falliti")
    return False


# ── Replicate API ─────────────────────────────────────────────────────────────

def generate_with_replicate(
    prompt: str,
    chapter_num: int,
    config: dict,  # noqa: ARG001 — reserved for future model config
    output_path: Path,
    max_retries: int = 3,
) -> bool:
    """
    Genera un'immagine con Replicate (es. Flux, SDXL).
    Ritorna True se successo, False se fallisce.
    """
    try:
        import replicate
        import requests
    except ImportError:
        log.error("replicate non installato. Esegui: pip install replicate")
        return False

    api_token = os.environ.get("REPLICATE_API_TOKEN")
    if not api_token:
        log.error("REPLICATE_API_TOKEN non trovato.")
        return False

    # Modello Flux Pro (alta qualità)
    model = "black-forest-labs/flux-pro"

    full_prompt = (
        f"{prompt} "
        f"No text, no letters, no words. "
        f"Professional book illustration, ultra detailed, 8k."
    )

    for attempt in range(1, max_retries + 1):
        try:
            log.info(
                f"  Capitolo {chapter_num:02d}: tentativo {attempt}/{max_retries} "
                f"— Replicate/Flux"
            )

            output = replicate.run(
                model,
                input={
                    "prompt": full_prompt,
                    "width": 1024,
                    "height": 1792,
                    "num_inference_steps": 28,
                    "guidance_scale": 3.5,
                }
            )

            # output è una lista di URL o FileOutput
            image_url = output[0] if isinstance(output, list) else str(output)

            img_response = requests.get(str(image_url), timeout=120)
            img_response.raise_for_status()

            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(img_response.content)
            log.info(f"  Capitolo {chapter_num:02d}: ✅ salvata → {output_path.name}")
            return True

        except Exception as e:
            wait_time = 10 * attempt
            log.warning(f"  Errore tentativo {attempt}: {e}. Attendo {wait_time}s...")
            if attempt < max_retries:
                time.sleep(wait_time)

    log.error(f"  Capitolo {chapter_num:02d}: ❌ tutti i retry Replicate falliti")
    return False


# ── Main Generator ────────────────────────────────────────────────────────────

def generate_images(
    prompts_path: str,
    config_path: str,
    images_dir: Path,
    force_placeholder: bool = False,
    skip_existing: bool = True,
) -> dict:
    """
    Genera tutte le immagini del libro.

    Args:
        prompts_path: percorso image_prompts.yaml
        config_path: percorso book_config.yaml
        images_dir: directory output immagini
        force_placeholder: se True, genera solo placeholder (no API)
        skip_existing: se True, salta immagini già esistenti

    Returns:
        dict con statistiche: generated, placeholders, skipped, errors
    """
    # Carica config
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Carica prompt
    with open(prompts_path, "r", encoding="utf-8") as f:
        prompts_data = yaml.safe_load(f)

    prompts = prompts_data.get("images", [])
    if not prompts:
        log.error("Nessun prompt trovato in image_prompts.yaml")
        sys.exit(1)

    log.info(f"Trovati {len(prompts)} prompt da elaborare")

    images_dir.mkdir(parents=True, exist_ok=True)

    api = config.get("images", {}).get("api", "openai").lower()
    log.info(f"API configurata: {api}")

    if force_placeholder:
        log.info("Modalità PLACEHOLDER — nessuna chiamata API")

    stats = {
        "generated": 0,
        "placeholders": 0,
        "skipped": 0,
        "errors": [],
    }

    for item in prompts:
        chapter_num = item.get("chapter", 0)
        prompt = item.get("prompt", "")
        style_notes = item.get("style_notes", "")

        if not chapter_num or not prompt:
            log.warning(f"  Item incompleto (chapter={chapter_num}), salto")
            continue

        output_path = images_dir / f"chapter_{chapter_num:02d}.png"

        # Salta se già esiste
        if skip_existing and output_path.exists():
            log.info(f"  Capitolo {chapter_num:02d}: già esistente, salto")
            stats["skipped"] += 1
            continue

        log.info(f"\nCapitolo {chapter_num:02d}: '{prompt[:60]}...'")
        if style_notes:
            log.info(f"  Note stile: {style_notes}")

        # Modalità placeholder
        if force_placeholder:
            create_placeholder_image(chapter_num, "", output_path)
            stats["placeholders"] += 1
            continue

        # Genera con API
        success = False

        if api == "openai":
            success = generate_with_openai(
                prompt, chapter_num, config, output_path
            )
        elif api == "replicate":
            success = generate_with_replicate(
                prompt, chapter_num, config, output_path
            )
        else:
            log.error(f"API non supportata: {api}. Supportate: openai, replicate")
            log.warning(f"  Creo placeholder per capitolo {chapter_num}")
            create_placeholder_image(chapter_num, "", output_path)
            stats["placeholders"] += 1
            continue

        if success:
            stats["generated"] += 1
        else:
            log.warning(
                f"  Generazione fallita — creo placeholder per capitolo {chapter_num}"
            )
            create_placeholder_image(chapter_num, "", output_path)
            stats["placeholders"] += 1
            stats["errors"].append(f"Capitolo {chapter_num}: generazione fallita")

    return stats


# ── Validation ────────────────────────────────────────────────────────────────

def validate_images(images_dir: Path, expected_count: int) -> list:
    """
    Valida le immagini generate.
    Restituisce lista di errori (vuota se tutto OK).
    """
    errors = []

    try:
        from PIL import Image
    except ImportError:
        log.warning("Pillow non disponibile — validazione immagini saltata")
        return errors

    png_files = sorted(images_dir.glob("chapter_*.png"))

    if len(png_files) < expected_count:
        errors.append(
            f"Immagini trovate: {len(png_files)}, attese: {expected_count}"
        )

    for img_path in png_files:
        try:
            img = Image.open(img_path)
            w, h = img.size
            # Verifica aspect ratio verticale
            if w >= h:
                errors.append(
                    f"{img_path.name}: aspect ratio non verticale ({w}x{h})"
                )
            # Verifica dimensioni minime
            if w < 512 or h < 512:
                errors.append(
                    f"{img_path.name}: dimensioni troppo piccole ({w}x{h})"
                )
            img.close()
        except Exception as e:
            errors.append(f"{img_path.name}: immagine corrotta — {e}")

    return errors


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Agente 1 — Generazione immagini libro"
    )
    parser.add_argument(
        "--placeholder",
        action="store_true",
        help="Genera solo placeholder grigi (no API)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rigenera anche le immagini già esistenti",
    )
    args = parser.parse_args()

    log.info("=" * 60)
    log.info("AGENTE 1 — IMAGE GENERATOR — Avvio")
    log.info("=" * 60)

    # Percorsi
    prompts_path = ROOT / "input" / "image_prompts.yaml"
    config_path = ROOT / "config" / "book_config.yaml"
    images_dir = ROOT / "assets" / "images"

    # Verifica file di input
    for path in [prompts_path, config_path]:
        if not path.exists():
            log.error(f"File non trovato: {path}")
            sys.exit(1)

    # Conta capitoli attesi
    with open(prompts_path, "r", encoding="utf-8") as f:
        prompts_data = yaml.safe_load(f)
    expected = len(prompts_data.get("images", []))
    log.info(f"Capitoli da generare: {expected}")

    # Genera immagini
    stats = generate_images(
        str(prompts_path),
        str(config_path),
        images_dir,
        force_placeholder=args.placeholder,
        skip_existing=not args.force,
    )

    # Validazione
    log.info("\nValidazione immagini generate...")
    errors = validate_images(images_dir, expected)

    if errors:
        log.warning(f"Validazione: {len(errors)} problemi trovati:")
        for err in errors:
            log.warning(f"  ⚠️  {err}")
    else:
        log.info("Validazione: ✅ tutte le immagini OK")

    # Report finale
    log.info("\n" + "=" * 60)
    log.info("REPORT FINALE")
    log.info(f"  Generate con API:  {stats['generated']}")
    log.info(f"  Placeholder:       {stats['placeholders']}")
    log.info(f"  Saltate (già OK):  {stats['skipped']}")
    if stats["errors"]:
        log.warning(f"  Errori:            {len(stats['errors'])}")
        for err in stats["errors"]:
            log.warning(f"    - {err}")
    log.info("=" * 60)
    log.info("AGENTE 1 — COMPLETATO")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
