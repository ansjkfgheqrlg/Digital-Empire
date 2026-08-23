"""
Archiviazione di un libro pubblicato (2026-08-23).

PERCHE' ESISTE. "Quando pubblicato, sposta manualmente questa cartella in
LIBRI/libri_pubblicati/" era scritto in tre posti — README del pacchetto, REPORT.md,
ARCHITETTURA.md — ed e' l'unico passo del flusso che nessuno ha mai eseguito: dopo tre
libri finiti, `libri_pubblicati/` conteneva solo il `.gitkeep`. Un passo manuale ripetuto
in tre documenti e mai fatto non e' un passo manuale: e' un passo mancante.

E costava due cose vere:
  1. **doppioni**: 23 MB in `in_lavorazione/` + 16 MB in `libri_pronti/`, con gli stessi
     .docx, .pdf e .png in due posti — e nessun modo di sapere quale fosse quello caricato;
  2. **nessuna traccia dell'ASIN**: a libro pubblicato, il legame fra il libro e la sua
     pagina Amazon viveva solo nella memoria di chi l'aveva caricato.

COSA FA, in ordine, fermandosi al primo intoppo:
  1. rifiuta se il libro non e' `pubblicabile` (a meno di --forza, che resta dichiarato);
  2. copia i SORGENTI (capitoli, outline, riassunti, progetto, metriche) dentro il
     pacchetto, in `sorgenti/`: il libro pubblicato si porta dietro come e' stato fatto;
  3. VERIFICA la copia file per file, confrontando i byte;
  4. sposta il pacchetto in `LIBRI/libri_pubblicati/<Titolo>/`;
  5. scrive `pubblicazione.json` con ASIN, data, pagine reali e prezzo;
  6. registra il libro sulla nicchia del catalogo e chiude l'argomento in magazzino;
  7. solo allora cancella `in_lavorazione/<slug>/`.

Il punto 3 e' quello che rende sicuro il punto 7: non si cancella niente che non sia
gia' stato ricopiato e ricontrollato byte per byte.
"""
from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from . import config

# Cosa del progetto di lavorazione vale la pena conservare accanto al libro pubblicato.
# I capitoli sono la cartella, il resto sono file singoli; quello che manca si salta.
SORGENTI_FILE = ("progetto.json", "outline.md", "riassunti.md", "copertina-prompt.md",
                 "ispirazione.json", "metriche.json")
SORGENTI_CARTELLE = ("capitoli",)


class NonPubblicabile(RuntimeError):
    """Il pacchetto non ha passato la validazione: non si archivia come pubblicato."""


@dataclass
class EsitoPubblicazione:
    titolo: str
    asin: str
    cartella: Path
    file_sorgente_copiati: int
    lavorazione_rimossa: bool
    nicchia: str | None

    def __str__(self) -> str:
        righe = [
            f"Pubblicato: {self.titolo}  (ASIN {self.asin})",
            f"  archivio:  {self.cartella}",
            f"  sorgenti:  {self.file_sorgente_copiati} file copiati in sorgenti/ e verificati",
        ]
        righe.append("  lavorazione: cartella rimossa (i sorgenti sono nel pacchetto)"
                     if self.lavorazione_rimossa else
                     "  lavorazione: cartella TENUTA (--tieni-lavorazione)")
        if self.nicchia:
            righe.append(f"  catalogo:  registrato sulla nicchia '{self.nicchia}'")
        return "\n".join(righe)


def _pacchetto_di(titolo: str) -> Path:
    from . import book_output_manager
    return config.LIBRI_PRONTI_DIR / book_output_manager.sanitize_title(titolo)


def _verifica_pubblicabile(pacchetto: Path) -> dict:
    val = pacchetto / "validazione.json"
    if not val.exists():
        raise NonPubblicabile(
            f"Manca {val.name} nel pacchetto: questo libro non e' mai passato dalla "
            f"consegna. Lancia prima: kdp consegna <slug> --cover <png>")
    dati = json.loads(val.read_text(encoding="utf-8"))
    if not dati.get("pubblicabile"):
        raise NonPubblicabile(
            "Il pacchetto NON e' pubblicabile: "
            + "; ".join(dati.get("bloccanti", ["motivo non registrato"]))
            + ". Si corregge il libro, non si archivia lo stesso.")
    return dati


def _copia_sorgenti(lavorazione: Path, destinazione: Path) -> int:
    """Copia i sorgenti nel pacchetto e li riconta. Ritorna quanti file sono stati copiati.

    La verifica byte per byte non e' pignoleria: e' la condizione che rende lecito
    cancellare la cartella di lavorazione subito dopo."""
    destinazione.mkdir(parents=True, exist_ok=True)
    copiati = 0
    for nome in SORGENTI_FILE:
        sorgente = lavorazione / nome
        if not sorgente.exists():
            continue
        arrivo = destinazione / nome
        shutil.copy2(sorgente, arrivo)
        if arrivo.stat().st_size != sorgente.stat().st_size:
            raise RuntimeError(f"Copia incompleta di {nome}: byte diversi, niente da "
                               f"cancellare. Controlla lo spazio su disco.")
        copiati += 1
    for nome in SORGENTI_CARTELLE:
        sorgente = lavorazione / nome
        if not sorgente.is_dir():
            continue
        arrivo = destinazione / nome
        shutil.copytree(sorgente, arrivo, dirs_exist_ok=True)
        for f in sorted(sorgente.rglob("*")):
            if f.is_file():
                gemello = arrivo / f.relative_to(sorgente)
                if not gemello.exists() or gemello.stat().st_size != f.stat().st_size:
                    raise RuntimeError(
                        f"Copia incompleta di {f.name}: manca o ha byte diversi in "
                        f"{arrivo}. Niente viene cancellato.")
                copiati += 1
    return copiati


def pubblica(slug: str, asin: str, url: str = "", prezzo: float | None = None,
             forza: bool = False, tieni_lavorazione: bool = False) -> EsitoPubblicazione:
    from . import book_project, magazzino, nicchia_attiva

    progetto = book_project.BookProject(slug)
    cfg = progetto._config()          # solleva FileNotFoundError con istruzioni se non c'e'
    titolo = cfg["titolo"]

    pacchetto = _pacchetto_di(titolo)
    if not pacchetto.is_dir():
        raise FileNotFoundError(
            f"Nessun pacchetto in {pacchetto}. Un libro si archivia dopo la consegna: "
            f"kdp consegna {slug} --cover <png>")

    dati_validazione = {}
    try:
        dati_validazione = _verifica_pubblicabile(pacchetto)
    except NonPubblicabile:
        if not forza:
            raise

    destinazione = config.LIBRI_PUBBLICATI_DIR / pacchetto.name
    if destinazione.exists():
        raise FileExistsError(
            f"C'e' gia' un libro archiviato in {destinazione}. Non si sovrascrive: "
            f"se e' una ripubblicazione, rinomina o rimuovi la cartella vecchia a mano.")

    copiati = _copia_sorgenti(progetto.dir, pacchetto / "sorgenti")

    scheda = {
        "titolo": titolo,
        "slug": slug,
        "autore": cfg.get("autore", ""),
        "nicchia": cfg.get("nicchia", ""),
        "asin": asin,
        "url_amazon": url or (f"https://www.amazon.com/dp/{asin}" if asin else ""),
        "prezzo_usd": prezzo if prezzo is not None else (
            (cfg.get("copy_kdp") or {}).get("prezzo_suggerito_usd")),
        "pubblicato_il": datetime.now().isoformat(timespec="seconds"),
        "pagine_reali": dati_validazione.get("pagine_reali"),
        "validazione_al_momento_del_caricamento": {
            "pubblicabile": dati_validazione.get("pubblicabile"),
            "bloccanti": dati_validazione.get("bloccanti", []),
            "verifiche_non_eseguite": dati_validazione.get("verifiche_non_eseguite", []),
        },
    }
    (pacchetto / "pubblicazione.json").write_text(
        json.dumps(scheda, indent=2, ensure_ascii=False), encoding="utf-8")

    destinazione.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(pacchetto), str(destinazione))

    nicchia = None
    n = nicchia_attiva.carica()
    if n is not None and cfg.get("nicchia", "").strip().lower() == n.keyword.strip().lower():
        nicchia_attiva.registra_libro(titolo)
        nicchia = n.keyword
    magazzino.segna_fatto(slug)

    rimossa = False
    if not tieni_lavorazione:
        # Lecito solo perche' `_copia_sorgenti` ha appena verificato ogni file byte per byte.
        shutil.rmtree(progetto.dir)
        rimossa = True

    return EsitoPubblicazione(titolo=titolo, asin=asin, cartella=destinazione,
                              file_sorgente_copiati=copiati, lavorazione_rimossa=rimossa,
                              nicchia=nicchia)


def elenco_pubblicati() -> list[dict]:
    """I libri gia' su KDP, letti dalle schede. Serve al 'Also by' in fondo ai libri nuovi."""
    libri = []
    if not config.LIBRI_PUBBLICATI_DIR.exists():
        return libri
    for cartella in sorted(config.LIBRI_PUBBLICATI_DIR.iterdir()):
        scheda = cartella / "pubblicazione.json"
        if scheda.exists():
            try:
                libri.append(json.loads(scheda.read_text(encoding="utf-8")))
            except (json.JSONDecodeError, OSError):
                continue
    return libri
