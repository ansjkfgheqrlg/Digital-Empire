"""
orchestrator.py — Book Factory: Orchestratore principale

Coordina i 3 agenti in sequenza per produrre il libro finale:
  1. Agente 1 — Generazione Immagini
  2. Agente 2 — Impaginazione Layout
  3. Agente 3 — Quality Assurance

Uso:
    python scripts/orchestrator.py                    # Flusso completo
    python scripts/orchestrator.py --placeholder      # Usa placeholder (no API immagini)
    python scripts/orchestrator.py --skip-images      # Salta generazione immagini
    python scripts/orchestrator.py --only-layout      # Solo layout (step 2)
    python scripts/orchestrator.py --only-qa          # Solo QA (step 3)
"""

import os
import sys
import subprocess
import argparse
import logging
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent

# ── Logging ───────────────────────────────────────────────────────────────────

os.makedirs(ROOT / "output", exist_ok=True)

# Reset del log ad ogni run
log_path = ROOT / "output" / "build_log.txt"
with open(log_path, "w", encoding="utf-8") as f:
    f.write(f"Book Factory — Build Log\n{'=' * 60}\n")
    f.write(f"Avvio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

import io as _io

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(
            _io.open(sys.stdout.fileno(), mode="w", encoding="utf-8",
                     errors="replace", closefd=False, buffering=1)
        ),
        logging.FileHandler(log_path, encoding="utf-8"),
    ]
)
log = logging.getLogger("orchestrator")


# ── Runner ────────────────────────────────────────────────────────────────────

def run_step(step_name: str, script_path: str, extra_args: list = None) -> bool:
    """
    Esegue uno script Python e restituisce True se successo.
    """
    log.info("=" * 60)
    log.info(f"INIZIO: {step_name}")
    log.info("=" * 60)

    cmd = [sys.executable, script_path]
    if extra_args:
        cmd.extend(extra_args)

    try:
        result = subprocess.run(
            cmd,
            cwd=str(ROOT),
            capture_output=False,  # Mostra output in tempo reale
            text=True,
        )

        if result.returncode == 0:
            log.info(f"✅ COMPLETATO: {step_name}")
            return True
        else:
            log.error(f"❌ FALLITO: {step_name} (exit code {result.returncode})")
            return False

    except FileNotFoundError:
        log.error(f"Script non trovato: {script_path}")
        return False
    except Exception as e:
        log.error(f"Errore durante {step_name}: {e}")
        return False


def validate_inputs() -> bool:
    """Verifica che tutti i file di input necessari esistano."""
    required = [
        ROOT / "input" / "manuscript.md",
        ROOT / "input" / "image_prompts.yaml",
        ROOT / "config" / "book_config.yaml",
    ]
    all_ok = True
    for path in required:
        if path.exists():
            log.info(f"  ✅ {path.relative_to(ROOT)}")
        else:
            log.error(f"  ❌ MANCANTE: {path.relative_to(ROOT)}")
            all_ok = False
    return all_ok


def check_dependencies() -> bool:
    """Verifica che le dipendenze Python critiche siano installate."""
    all_ok = True
    missing = []

    # WeasyPrint: potrebbe essere installato ma richiedere GTK (ok con fallback ReportLab)
    try:
        __import__("weasyprint")
        log.info("  ✅ WeasyPrint (generazione PDF)")
    except (ImportError, OSError, Exception) as e:
        err = str(e)
        if "libgobject" in err or "GTK" in err or "cannot load library" in err:
            log.warning("  ⚠️  WeasyPrint installato ma GTK non disponibile")
            log.warning("      → Uso ReportLab come backend PDF (fallback automatico)")
            # Non è un errore critico: il fallback ReportLab gestirà la generazione
        else:
            log.warning(f"  ⚠️  WeasyPrint non disponibile: {e}")

    # ReportLab (fallback obbligatorio su Windows senza GTK)
    try:
        __import__("reportlab")
        log.info("  ✅ ReportLab (backend PDF fallback)")
    except ImportError:
        log.error("  ❌ MANCANTE: ReportLab — pip install reportlab")
        missing.append("reportlab")
        all_ok = False

    # Dipendenze critiche
    for module, name, install in [
        ("yaml", "PyYAML (configurazioni)", "PyYAML"),
        ("PIL", "Pillow (immagini)", "Pillow"),
    ]:
        try:
            __import__(module)
            log.info(f"  ✅ {name}")
        except ImportError:
            log.error(f"  ❌ MANCANTE: {name} — pip install {install}")
            missing.append(install)
            all_ok = False

    if missing:
        log.error(f"Dipendenze critiche mancanti: {missing}")
        log.error("Esegui: pip install -r requirements.txt")

    return all_ok


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Book Factory — Orchestratore"
    )
    parser.add_argument(
        "--placeholder",
        action="store_true",
        help="Genera placeholder invece di chiamare l'API immagini",
    )
    parser.add_argument(
        "--skip-images",
        action="store_true",
        help="Salta la generazione immagini (usa quelle già presenti)",
    )
    parser.add_argument(
        "--only-layout",
        action="store_true",
        help="Esegui solo l'Agente 2 (layout)",
    )
    parser.add_argument(
        "--only-qa",
        action="store_true",
        help="Esegui solo l'Agente 3 (QA)",
    )
    parser.add_argument(
        "--force-images",
        action="store_true",
        help="Forza la rigenerazione di tutte le immagini anche se esistono",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Numero massimo di tentativi del ciclo Layout→QA (default: 3)",
    )
    args = parser.parse_args()

    log.info("")
    log.info("🚀 BOOK FACTORY — AVVIO PIPELINE")
    log.info("=" * 60)

    # Step 0: Crea le directory necessarie
    for d in ["output", "assets/images"]:
        (ROOT / d).mkdir(parents=True, exist_ok=True)

    # Step 0a: Validazione input
    log.info("\nStep 0: Validazione file di input...")
    if not validate_inputs():
        log.error("⛔ Input mancanti — impossibile procedere")
        sys.exit(1)
    log.info("✅ Tutti i file di input presenti")

    # Step 0b: Verifica dipendenze
    log.info("\nStep 0: Verifica dipendenze Python...")
    if not check_dependencies():
        log.error("⛔ Dipendenze mancanti — impossibile procedere")
        sys.exit(1)

    # ── Modalità speciali ──────────────────────────────────────────────────────

    if args.only_qa:
        log.info("\nModalità: SOLO QA")
        success = run_step(
            "AGENTE 3 — Quality Assurance",
            str(ROOT / "scripts" / "qa_checker.py"),
        )
        sys.exit(0 if success else 1)

    if args.only_layout:
        log.info("\nModalità: SOLO LAYOUT")
        success = run_step(
            "AGENTE 2 — Layout Engine",
            str(ROOT / "scripts" / "build_book_reportlab.py"),
        )
        if success:
            run_step(
                "AGENTE 3 — Quality Assurance",
                str(ROOT / "scripts" / "qa_checker.py"),
            )
        sys.exit(0 if success else 1)

    # ── Pipeline completa ──────────────────────────────────────────────────────

    # STEP 1: Generazione immagini
    if not args.skip_images:
        log.info("\nStep 1: Agente 1 — Generazione Immagini")

        img_args = []
        if args.placeholder:
            img_args.append("--placeholder")
            log.info("  → Modalità PLACEHOLDER (no API)")
        if args.force_images:
            img_args.append("--force")

        if not run_step(
            "AGENTE 1 — Generazione Immagini",
            str(ROOT / "scripts" / "generate_images.py"),
            img_args,
        ):
            log.warning(
                "⚠️  Generazione immagini fallita o incompleta. "
                "Continuo con placeholder automatici..."
            )
            # Non blocco la pipeline — build_book gestisce le immagini mancanti
    else:
        log.info("\nStep 1: Generazione immagini SALTATA (--skip-images)")

    # ── CICLO SELF-HEALING: Layout → QA → Retry ────────────────────────────────
    #
    # Il ciclo esegue:
    #   1. Agente 2 (Layout) → genera book_draft.pdf
    #   2. Agente 3 (QA)     → verifica il PDF e produce qa_report.md
    #   3. Se QA OK → book_final.pdf creato → SUCCESSO
    #   4. Se QA FALLISCE → mostra gli errori → ritenta (fino a max_retries)
    #
    # Questo ciclo garantisce che il libro finale soddisfi TUTTI i criteri
    # di qualità prima di essere considerato pronto.

    draft_path = ROOT / "output" / "book_draft.pdf"
    final_path = ROOT / "output" / "book_final.pdf"
    qa_report_path = ROOT / "output" / "qa_report.md"
    layout_script = str(ROOT / "scripts" / "build_book_reportlab.py")
    qa_script = str(ROOT / "scripts" / "qa_checker.py")
    max_retries = args.max_retries
    qa_passed = False

    # Rimuove book_final.pdf precedente per non confonderlo con il risultato del ciclo attuale
    if final_path.exists():
        final_path.unlink()
        log.info("  (rimosso book_final.pdf precedente per ricominciare il ciclo QA pulito)")

    for attempt in range(1, max_retries + 1):
        log.info("")
        log.info(f"{'=' * 60}")
        log.info(f"CICLO QUALITY {attempt}/{max_retries}")
        log.info(f"{'=' * 60}")

        # STEP 2: Layout Engine
        log.info(f"\nStep 2 (tentativo {attempt}): Agente 2 — Layout Engine")
        if not run_step("AGENTE 2 — Layout Engine", layout_script):
            log.error("⛔ Pipeline interrotta — errore nel Layout Engine")
            sys.exit(1)

        if not draft_path.exists():
            log.error(f"⛔ PDF bozza non trovato dopo build: {draft_path}")
            sys.exit(1)

        # STEP 3: Quality Assurance
        log.info(f"\nStep 3 (tentativo {attempt}): Agente 3 — Quality Assurance")
        run_step("AGENTE 3 — Quality Assurance", qa_script)

        # Controlla se il PDF finale è stato creato (= QA superato)
        if final_path.exists():
            qa_passed = True
            log.info(f"\n✅ QA SUPERATO al tentativo {attempt}/{max_retries}")
            break

        # QA fallito: mostra gli errori dal report
        log.warning(f"\n❌ QA FALLITO (tentativo {attempt}/{max_retries})")
        if qa_report_path.exists():
            report_text = qa_report_path.read_text(encoding="utf-8")
            # Estrai solo le righe di errori critici dal report
            in_errors = False
            error_lines = []
            for line in report_text.splitlines():
                if "Errori Critici" in line:
                    in_errors = True
                    continue
                if in_errors:
                    if line.startswith("## ") and "Errori" not in line:
                        break
                    if line.strip().startswith("1.") or line.strip().startswith("❌"):
                        error_lines.append(f"  {line.strip()}")
            if error_lines:
                log.warning("Errori critici rilevati:")
                for el in error_lines[:10]:
                    log.warning(el)

        if attempt < max_retries:
            log.info(f"→ Rieseguo il layout (tentativo {attempt + 1}/{max_retries})...")
        else:
            log.error(f"⛔ QA non superato dopo {max_retries} tentativi.")
            log.error("Controllare output/qa_report.md per i dettagli.")

    # ── Risultato finale ───────────────────────────────────────────────────────
    log.info("")
    log.info("=" * 60)
    if qa_passed and final_path.exists():
        size_mb = final_path.stat().st_size / (1024 * 1024)
        log.info(f"🎉 LIBRO COMPLETATO CON SUCCESSO!")
        log.info(f"📖 File finale: output/book_final.pdf ({size_mb:.2f} MB)")
    else:
        log.warning(f"⚠️  Libro generato ma con errori QA residui.")
        log.warning(f"📋 Controllare: output/qa_report.md")
        log.warning(f"📄 Bozza disponibile: output/book_draft.pdf")

    # Mostra riepilogo file generati
    log.info("\nFile generati:")
    output_files = [
        "output/book_draft.pdf",
        "output/book_final.pdf",
        "output/qa_report.md",
        "output/build_log.txt",
        "output/layout_log.txt",
        "output/image_generation_log.txt",
        "output/book_debug.html",
    ]
    for rel_path in output_files:
        full_path = ROOT / rel_path
        if full_path.exists():
            size = full_path.stat().st_size
            if size > 1024 * 1024:
                size_str = f"{size / (1024*1024):.2f} MB"
            else:
                size_str = f"{size / 1024:.1f} KB"
            log.info(f"  ✅ {rel_path} ({size_str})")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
