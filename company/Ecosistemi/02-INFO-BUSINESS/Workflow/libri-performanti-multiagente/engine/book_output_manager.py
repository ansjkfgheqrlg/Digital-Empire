"""
Book Output Manager (PIANO-KDP-67, CP8) — crea la cartella dedicata in
LIBRI/libri_pronti/<Nome-Libro>/ con dentro il manoscritto e la copertina APPENA
generati per QUEL libro.

Riscritto da zero: la versione consegnata nello zip analizzato (`genera_nuovo_libro.py`)
copiava sempre lo stesso file template rinominandolo (vedi CP-20260805-001 §Audit punto 5
— provato con dimensioni byte identiche su 5 "libri" diversi). Qui `manuscript_path` e
`cover_path` sono OBBLIGATORI e vengono verificati esistenti prima di procedere — non
c'è nessun fallback silenzioso a un file template.
"""
from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from . import config


def sanitize_title(title: str) -> str:
    safe = re.sub(r'[<>:"/\\|?*]', "", title)
    safe = safe.replace(" ", "_")
    return safe[:60]


@dataclass
class BookPackageResult:
    folder_path: Path
    manuscript_dest: Path
    cover_dest: Path
    metadata_dest: Path


def create_book_package(
    book_title: str,
    manuscript_path: Path,
    cover_path: Path,
    kdp_metadata_text: str,
    word_count: int,
    page_count: float,
) -> BookPackageResult:
    """Crea LIBRI/libri_pronti/<Nome-Libro>/ con dentro libro e copertina APPENA
    generati per questo libro specifico. Solleva FileNotFoundError esplicito se
    manuscript_path o cover_path non esistono — mai un pacchetto con file finti o
    riciclati da un altro libro."""
    manuscript_path = Path(manuscript_path)
    cover_path = Path(cover_path)
    if not manuscript_path.exists():
        raise FileNotFoundError(f"Manoscritto non trovato: {manuscript_path}")
    if not cover_path.exists():
        raise FileNotFoundError(f"Copertina non trovata: {cover_path}")

    safe_title = sanitize_title(book_title)
    folder_path = config.LIBRI_PRONTI_DIR / safe_title
    if folder_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        folder_path = config.LIBRI_PRONTI_DIR / f"{safe_title}_{timestamp}"
    folder_path.mkdir(parents=True, exist_ok=False)

    manuscript_dest = folder_path / f"{safe_title}{manuscript_path.suffix}"
    cover_dest = folder_path / f"Cover_{safe_title}{cover_path.suffix}"
    shutil.copy2(manuscript_path, manuscript_dest)
    shutil.copy2(cover_path, cover_dest)

    metadata_dest = folder_path / "KDP_METADATA.txt"
    metadata_dest.write_text(kdp_metadata_text, encoding="utf-8")

    readme_dest = folder_path / "README.txt"
    readme_dest.write_text(
        f"LIBRO: {book_title}\n"
        f"Generato: {datetime.now().isoformat()}\n"
        f"Word count: {word_count} — Pagine stimate: {page_count} @{config.WORDS_PER_PAGE_ESTIMATE}wpp\n"
        f"Manoscritto: {manuscript_dest.name}\n"
        f"Copertina: {cover_dest.name}\n"
        f"Quando pubblicato: sposta manualmente questa cartella in LIBRI/libri_pubblicati/\n",
        encoding="utf-8",
    )

    return BookPackageResult(
        folder_path=folder_path,
        manuscript_dest=manuscript_dest,
        cover_dest=cover_dest,
        metadata_dest=metadata_dest,
    )


if __name__ == "__main__":
    import sys
    import tempfile

    print("=== CP8 self-test: 2 libri DIVERSI, verifica che i file risultanti NON siano "
          "identici (replica del test forense usato nell'audit per smascherare il bug "
          "copia-template) ===\n")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # Due manoscritti e due copertine di contenuto/dimensione DIVERSA
        ms1 = tmp_path / "manoscritto1.docx"
        ms1.write_bytes(b"CONTENUTO LIBRO UNO " * 100)
        cover1 = tmp_path / "cover1.png"
        cover1.write_bytes(b"FINTA-IMMAGINE-UNO" * 50)

        ms2 = tmp_path / "manoscritto2.docx"
        ms2.write_bytes(b"CONTENUTO LIBRO DUE COMPLETAMENTE DIVERSO E PIU LUNGO " * 137)
        cover2 = tmp_path / "cover2.png"
        cover2.write_bytes(b"FINTA-IMMAGINE-DUE-DIVERSA" * 83)

        # Redirigo temporaneamente LIBRI_PRONTI_DIR verso una cartella di test
        original_dir = config.LIBRI_PRONTI_DIR
        config.LIBRI_PRONTI_DIR = tmp_path / "LIBRI_TEST" / "libri_pronti"
        try:
            result1 = create_book_package(
                "Il Primo Libro Di Test", ms1, cover1, "meta1", word_count=1000, page_count=10.0
            )
            result2 = create_book_package(
                "Il Secondo Libro Di Test", ms2, cover2, "meta2", word_count=2000, page_count=20.0
            )

            size_ms1 = result1.manuscript_dest.stat().st_size
            size_ms2 = result2.manuscript_dest.stat().st_size
            size_cov1 = result1.cover_dest.stat().st_size
            size_cov2 = result2.cover_dest.stat().st_size

            print(f"Libro 1: {result1.folder_path.name} — manoscritto {size_ms1} byte, copertina {size_cov1} byte")
            print(f"Libro 2: {result2.folder_path.name} — manoscritto {size_ms2} byte, copertina {size_cov2} byte")

            assert result1.folder_path != result2.folder_path, "ERRORE: stessa cartella per libri diversi"
            assert size_ms1 != size_ms2, "ERRORE CRITICO: manoscritti identici — stesso bug del copia-template originale"
            assert size_cov1 != size_cov2, "ERRORE CRITICO: copertine identiche — stesso bug del copia-template originale"
            print("\n-> corretto: cartelle distinte, file DIVERSI per libro — bug copia-template NON riprodotto")

            # Test errore esplicito su file mancante
            try:
                create_book_package("Libro Fantasma", tmp_path / "non_esiste.docx", cover1, "meta", 0, 0)
                raise AssertionError("ERRORE: doveva sollevare FileNotFoundError e non l'ha fatto")
            except FileNotFoundError:
                print("-> corretto: FileNotFoundError sollevato per manoscritto mancante, nessun fallback silenzioso")
        finally:
            config.LIBRI_PRONTI_DIR = original_dir

    print("\nCP8 self-test: TUTTO VERIFICATO OK")
    sys.exit(0)
