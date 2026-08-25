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
import tempfile
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
    cover_dest: Path | None
    metadata_dest: Path
    pdf_dest: Path | None = None
    prompt_copertina_dest: Path | None = None


def converti_in_pdf(docx_path: Path, pdf_path: Path | None = None) -> Path | None:
    """Converte il manoscritto .docx in PDF mantenendo la formattazione KDP reale
    (richiesta di Gael, 2026-08-08: nella cartella del libro finito ci devono essere il
    PDF e la copertina).

    Usa `docx2pdf`, che pilota Word installato sul PC: e' l'unico modo di ottenere un PDF
    con gli STESSI margini specchio, interruzioni di sezione e numeri di pagina del .docx —
    una libreria che ridisegna il documento da zero produrrebbe un impaginato diverso da
    quello verificato, e il conteggio pagine non corrisponderebbe piu'.

    Ritorna None (senza far fallire il pacchetto) se la conversione non e' possibile:
    meglio un pacchetto con .docx e copertina che nessun pacchetto."""
    docx_path = Path(docx_path)
    pdf_path = Path(pdf_path) if pdf_path else docx_path.with_suffix(".pdf")
    try:
        from docx2pdf import convert
        convert(str(docx_path), str(pdf_path))
    except Exception as exc:
        print(f"[output] PDF non generato ({type(exc).__name__}: {exc}). "
              f"Serve Microsoft Word installato. Il pacchetto resta valido col .docx.")
        return None
    if not pdf_path.exists():
        print("[output] PDF non generato: la conversione non ha prodotto il file.")
        return None
    print(f"[output] PDF creato: {pdf_path.name} ({pdf_path.stat().st_size / 1024:.0f} KB)")
    return pdf_path


def conta_pagine_pdf(pdf_path: Path) -> int | None:
    """Conta le pagine REALI del PDF impaginato.

    Perche' conta (2026-08-08): fino a oggi il numero di pagine era una STIMA
    (parole / 300). Sul primo libro vero la stima diceva 115.5 e il PDF impaginato da Word
    ne ha 106 — perche' Garamond 11pt su 6x9 con quei margini sta a ~327 parole/pagina, non
    300. Una stima ottimista del 9% e' esattamente il tipo di numero dichiarato-e-mai-
    verificato che questo progetto esiste per eliminare: KDP impagina il PDF, non la stima.

    Conta le occorrenze di /Type /Page nel PDF, senza dipendenze esterne."""
    import re
    data = Path(pdf_path).read_bytes()
    if not data.startswith(b"%PDF-"):
        return None
    pagine = len(re.findall(rb"/Type\s*/Page[^s]", data))
    return pagine or None


def create_book_package(
    book_title: str,
    manuscript_path: Path,
    cover_path: Path | None,
    kdp_metadata_text: str,
    word_count: int,
    page_count: float,
    sostituisci: bool = False,
    prompt_copertina_path: Path | None = None,
) -> BookPackageResult:
    """Crea LIBRI/libri_pronti/<Nome-Libro>/ con dentro libro e copertina APPENA
    generati per questo libro specifico. Solleva FileNotFoundError esplicito se
    manuscript_path o cover_path non esistono — mai un pacchetto con file finti o
    riciclati da un altro libro.

    `cover_path=None` e' lecito (2026-08-25, TASK-KDP-W1): l'immagine la genera una
    persona dal prompt, e prima di quel passaggio i tre artefatti che il flusso produce
    da solo — manoscritto, prompt copertina, copy KDP — devono comunque stare **in una
    cartella sola**. Prima non era cosi': senza .png il pacchetto non nasceva affatto e
    i tre pezzi restavano sparsi fra `in_lavorazione/` e la chat. Il pacchetto senza
    immagine NON e' pubblicabile, e chi lo dice e' `validazione.json`, non questa
    funzione. Un `cover_path` valorizzato ma inesistente resta un errore duro: quello
    era ed e' il guard-rail contro i file riciclati da un altro libro."""
    manuscript_path = Path(manuscript_path)
    cover_path = Path(cover_path) if cover_path else None
    if not manuscript_path.exists():
        raise FileNotFoundError(f"Manoscritto non trovato: {manuscript_path}")
    if cover_path is not None and not cover_path.exists():
        raise FileNotFoundError(f"Copertina non trovata: {cover_path}")

    safe_title = sanitize_title(book_title)
    folder_path = config.LIBRI_PRONTI_DIR / safe_title
    rifugio: Path | None = None
    if folder_path.exists():
        if sostituisci:
            # Stesso libro riconsegnato: la cartella e' UNA, e contiene l'ultima versione.
            # Prima si accumulavano copie col timestamp a ogni riconsegna (2026-08-17: due
            # cartelle per The Ninth Winter, una del giro bloccato e una di quello buono) e
            # dalla cartella non si capiva piu' quale fosse il libro da caricare su KDP.
            #
            # ATTENZIONE: sorgente e destinazione possono coincidere. Rilanciare la consegna
            # passando la copertina che sta GIA' nel pacchetto e' la cosa piu' naturale del
            # mondo — e senza questa protezione la cancellazione distrugge la copertina
            # prima di copiarla. Successo davvero il 2026-08-18 su The Quiet Hours: cartella
            # svuotata, copertina persa (recuperata solo perche' era su git).
            def _al_sicuro(p: Path) -> Path:
                nonlocal rifugio
                if folder_path.resolve() not in p.resolve().parents:
                    return p
                if rifugio is None:
                    rifugio = Path(tempfile.mkdtemp(prefix="kdp_sorgenti_"))
                copia = rifugio / p.name
                shutil.copy2(p, copia)
                return copia

            manuscript_path = _al_sicuro(manuscript_path)
            if cover_path is not None:
                cover_path = _al_sicuro(cover_path)
            if prompt_copertina_path is not None and Path(prompt_copertina_path).exists():
                prompt_copertina_path = _al_sicuro(Path(prompt_copertina_path))
            shutil.rmtree(folder_path)
        else:
            # Libro DIVERSO con lo stesso titolo: non si sovrascrive mai il lavoro altrui.
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            folder_path = config.LIBRI_PRONTI_DIR / f"{safe_title}_{timestamp}"
    folder_path.mkdir(parents=True, exist_ok=False)

    manuscript_dest = folder_path / f"{safe_title}{manuscript_path.suffix}"
    shutil.copy2(manuscript_path, manuscript_dest)
    cover_dest: Path | None = None
    if cover_path is not None:
        cover_dest = folder_path / f"Cover_{safe_title}{cover_path.suffix}"
        shutil.copy2(cover_path, cover_dest)

    # Il prompt della copertina viaggia CON il libro. Fino al 2026-08-25 restava in
    # `LIBRI/in_lavorazione/<slug>/copertina-prompt.md` e non entrava mai nel pacchetto:
    # chi apriva la cartella finale aveva il manoscritto ma non il testo con cui generare
    # l'immagine, e se lo faceva ridettare in chat. Nessuno dei tre pacchetti consegnati
    # (Ninth Winter, Quiet Hours, Second-Hand Spellbook) ce l'ha dentro.
    prompt_dest: Path | None = None
    if prompt_copertina_path is not None and Path(prompt_copertina_path).exists():
        prompt_dest = folder_path / "COPERTINA-PROMPT.md"
        shutil.copy2(Path(prompt_copertina_path), prompt_dest)

    # PDF accanto al .docx: e' il formato in cui il libro si legge e si controlla prima di
    # pubblicarlo (richiesta esplicita di Gael, 2026-08-08).
    pdf_dest = converti_in_pdf(manuscript_dest, folder_path / f"{safe_title}.pdf")

    # Pagine REALI dal PDF impaginato, non la stima parole/300: e' il numero che vedra' KDP.
    pagine_reali = conta_pagine_pdf(pdf_dest) if pdf_dest else None
    if pagine_reali:
        minimo = config.TARGET_PAGE_COUNT - config.TARGET_PAGE_COUNT_TOLERANCE
        stato = "OK" if pagine_reali >= minimo else f"SOTTO IL TARGET (minimo {minimo})"
        print(f"[output] pagine REALI nel PDF: {pagine_reali} — {stato}")
        if pagine_reali < minimo:
            print(f"[output] la stima diceva {page_count} pagine: e' ottimista perche' "
                  f"calcolata a {config.WORDS_PER_PAGE_ESTIMATE} parole/pagina, "
                  f"l'impaginato reale ne sta di piu'. Servono ancora circa "
                  f"{(minimo - pagine_reali) * 330} parole.")

    metadata_dest = folder_path / "KDP_METADATA.txt"
    metadata_dest.write_text(kdp_metadata_text, encoding="utf-8")

    readme_dest = folder_path / "README.txt"
    readme_dest.write_text(
        f"LIBRO: {book_title}\n"
        f"Generato: {datetime.now().isoformat()}\n"
        f"Word count: {word_count} — Pagine stimate: {page_count} @{config.WORDS_PER_PAGE_ESTIMATE}wpp\n"
        f"Manoscritto: {manuscript_dest.name}\n"
        f"PDF: {pdf_dest.name if pdf_dest else 'NON generato (serve Word installato)'}\n"
        f"Copertina: {cover_dest.name if cover_dest else 'DA GENERARE — usa ' + (prompt_dest.name if prompt_dest else 'copertina-prompt.md') + ', poi: python -m engine.kdp consegna <slug> --cover <file.png>'}\n"
        f"Prompt copertina: {prompt_dest.name if prompt_dest else 'assente'}\n"
        f"Quando pubblicato: sposta manualmente questa cartella in LIBRI/libri_pubblicati/\n",
        encoding="utf-8",
    )

    if rifugio is not None:
        shutil.rmtree(rifugio, ignore_errors=True)

    return BookPackageResult(
        folder_path=folder_path,
        manuscript_dest=manuscript_dest,
        cover_dest=cover_dest,
        metadata_dest=metadata_dest,
        pdf_dest=pdf_dest,
        prompt_copertina_dest=prompt_dest,
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
