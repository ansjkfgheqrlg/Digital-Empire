"""
Book Project (PIANO KDP V2) — il "ponte" fra i capitoli scritti a mano (da Claude, seguendo
la SOP) e il codice gia' costruito che formatta, impagina e impacchetta il libro.

PERCHE' ESISTE: fino al 2026-08-07 la scrittura passava da LM Arena via Playwright, che si
e' rivelato inadatto a una generazione lunga in serie (captcha dopo poche richieste, vedi
PIANO-KDP-67.md). Decisione di Gael: i capitoli li scrive Claude direttamente, uno o pochi
per volta, salvandoli come file di testo. Questo modulo li rilegge e produce il libro vero.

STRUTTURA DI UN PROGETTO LIBRO (una cartella per libro):

    LIBRI/in_lavorazione/<slug-del-libro>/
    ├── progetto.json          # titolo, autore, nicchia, target capitoli/parole
    ├── outline.md             # trama in 3 atti + scaletta capitoli (STEP 3 della SOP)
    ├── capitoli/
    │   ├── cap_01.md          # un file per capitolo (STEP 4)
    │   ├── cap_02.md
    │   └── ...
    └── riassunti.md           # riassunto progressivo, per la continuita' fra sessioni

Vantaggi di tenere i capitoli su file invece che in memoria: il lavoro non si perde se la
sessione si interrompe, si riprende dal primo capitolo mancante, ogni capitolo e'
rileggibile e correggibile a mano, e `stato()` dice sempre a che punto siamo.

USO:
    python -m engine.book_project nuovo "Titolo Del Libro" --nicchia "cozy mystery"
    python -m engine.book_project stato <slug>
    python -m engine.book_project assembla <slug>
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from . import book_output_manager, config, kdp_formatter

PROGETTI_DIR = config.LIBRI_DIR / "in_lavorazione"

# Default coerenti col target KDP di config.py (120 pagine ± 5 a 300 parole/pagina):
# 24 capitoli x 1500 parole = 36000 parole = 120 pagine.
DEFAULT_TOTAL_CHAPTERS = 24
DEFAULT_WORDS_PER_CHAPTER = 1500


def slugify(titolo: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", titolo.lower())
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    return slug[:60] or "libro"


@dataclass
class StatoProgetto:
    slug: str
    titolo: str
    capitoli_scritti: list[int]
    capitoli_totali: int
    parole_scritte: int
    parole_target: int
    prossimo_capitolo: int | None
    completo: bool

    def __str__(self) -> str:
        pagine = round(self.parole_scritte / config.WORDS_PER_PAGE_ESTIMATE, 1)
        pagine_target = round(self.parole_target / config.WORDS_PER_PAGE_ESTIMATE)
        righe = [
            f"Libro: {self.titolo}  [{self.slug}]",
            f"Capitoli: {len(self.capitoli_scritti)}/{self.capitoli_totali}",
            f"Parole: {self.parole_scritte} (~{pagine} pagine) — target {self.parole_target} (~{pagine_target} pagine)",
        ]
        if self.completo:
            righe.append("STATO: tutti i capitoli scritti — pronto per 'assembla'")
        else:
            mancanti = self.capitoli_totali - len(self.capitoli_scritti)
            righe.append(f"STATO: mancano {mancanti} capitoli — prossimo da scrivere: "
                         f"cap_{self.prossimo_capitolo:02d}.md")
        return "\n".join(righe)


class BookProject:
    def __init__(self, slug: str):
        self.slug = slug
        self.dir = PROGETTI_DIR / slug
        self.capitoli_dir = self.dir / "capitoli"
        self.progetto_path = self.dir / "progetto.json"
        self.outline_path = self.dir / "outline.md"
        self.riassunti_path = self.dir / "riassunti.md"

    # --- creazione / lettura ------------------------------------------------ #
    @classmethod
    def crea(cls, titolo: str, nicchia: str, autore: str = "Digital Empire",
             capitoli: int = DEFAULT_TOTAL_CHAPTERS,
             parole_per_capitolo: int = DEFAULT_WORDS_PER_CHAPTER) -> "BookProject":
        slug = slugify(titolo)
        p = cls(slug)
        if p.progetto_path.exists():
            raise FileExistsError(
                f"Progetto gia' esistente: {p.dir}. Usa 'stato {slug}' per vedere a che "
                f"punto e', oppure scegli un titolo diverso."
            )
        p.capitoli_dir.mkdir(parents=True, exist_ok=True)
        p.progetto_path.write_text(json.dumps({
            "titolo": titolo,
            "autore": autore,
            "nicchia": nicchia,
            "capitoli_totali": capitoli,
            "parole_per_capitolo": parole_per_capitolo,
            "creato": datetime.now().isoformat(),
        }, indent=2, ensure_ascii=False), encoding="utf-8")
        if not p.outline_path.exists():
            p.outline_path.write_text(
                f"# Outline — {titolo}\n\n"
                f"<!-- STEP 3 della SOP: sostituire questo file con titolo definitivo, "
                f"personaggi, trama in 3 atti e scaletta dei {capitoli} capitoli. -->\n",
                encoding="utf-8")
        if not p.riassunti_path.exists():
            p.riassunti_path.write_text(
                f"# Riassunti progressivi — {titolo}\n\n"
                "<!-- Un paragrafo per capitolo, aggiunto dopo averlo scritto. Serve a "
                "mantenere la continuita' quando si riprende in una sessione nuova. -->\n",
                encoding="utf-8")
        return p

    def _config(self) -> dict:
        if not self.progetto_path.exists():
            raise FileNotFoundError(
                f"Progetto non trovato: {self.dir}. Crealo con: "
                f"python -m engine.book_project nuovo \"<titolo>\" --nicchia \"<nicchia>\""
            )
        return json.loads(self.progetto_path.read_text(encoding="utf-8"))

    def path_capitolo(self, numero: int) -> Path:
        return self.capitoli_dir / f"cap_{numero:02d}.md"

    # --- stato --------------------------------------------------------------- #
    def capitoli_presenti(self) -> list[int]:
        if not self.capitoli_dir.exists():
            return []
        numeri = []
        for f in self.capitoli_dir.glob("cap_*.md"):
            m = re.match(r"cap_(\d+)\.md$", f.name)
            # Un file vuoto o quasi non conta come capitolo scritto: meglio saperlo subito
            # che scoprirlo in fase di assemblaggio.
            if m and len(f.read_text(encoding="utf-8").split()) >= 50:
                numeri.append(int(m.group(1)))
        return sorted(numeri)

    def stato(self) -> StatoProgetto:
        cfg = self._config()
        scritti = self.capitoli_presenti()
        totali = cfg["capitoli_totali"]
        parole = sum(len(self.path_capitolo(n).read_text(encoding="utf-8").split())
                     for n in scritti)
        mancanti = [n for n in range(1, totali + 1) if n not in scritti]
        return StatoProgetto(
            slug=self.slug,
            titolo=cfg["titolo"],
            capitoli_scritti=scritti,
            capitoli_totali=totali,
            parole_scritte=parole,
            parole_target=totali * cfg["parole_per_capitolo"],
            prossimo_capitolo=mancanti[0] if mancanti else None,
            completo=not mancanti,
        )

    # --- assemblaggio -------------------------------------------------------- #
    def _leggi_capitolo(self, numero: int) -> kdp_formatter.Chapter:
        """Legge un capitolo .md e lo converte nella forma attesa dal formatter.
        Prima riga '# Titolo' (opzionale) = titolo del capitolo; il resto sono paragrafi
        separati da riga vuota."""
        testo = self.path_capitolo(numero).read_text(encoding="utf-8").strip()
        righe = testo.split("\n")
        titolo = f"Chapter {numero}"
        if righe and righe[0].startswith("#"):
            titolo = righe[0].lstrip("#").strip() or titolo
            testo = "\n".join(righe[1:]).strip()
        paragrafi = [p.strip() for p in testo.split("\n\n") if p.strip()]
        if not paragrafi:
            raise ValueError(f"Capitolo {numero} vuoto dopo la lettura: {self.path_capitolo(numero)}")
        return kdp_formatter.Chapter(title=titolo, paragraphs=paragrafi)

    def assembla(self, cover_path: Path | None = None, forza: bool = False) -> dict:
        """Assembla il .docx reale dai capitoli su disco e, se c'e' la copertina, crea il
        pacchetto finale pronto per KDP.

        Non dichiara mai un successo falso: se le pagine reali sono sotto il target si
        FERMA (a meno di `forza`), dicendo quanti capitoli servono ancora — e' esattamente
        il bug che si e' ripetuto due volte nel workflow originale (120 pagine dichiarate,
        21 reali)."""
        cfg = self._config()
        stato = self.stato()
        if not stato.completo and not forza:
            raise RuntimeError(
                f"Mancano {stato.capitoli_totali - len(stato.capitoli_scritti)} capitoli "
                f"(prossimo: cap_{stato.prossimo_capitolo:02d}.md). Scrivili prima di "
                f"assemblare, oppure usa --forza per assemblare comunque una bozza parziale."
            )

        manoscritto = kdp_formatter.BookManuscript(
            title=cfg["titolo"],
            author=cfg.get("autore", "Digital Empire"),
            chapters=[self._leggi_capitolo(n) for n in stato.capitoli_scritti],
        )
        docx_path = self.dir / f"{book_output_manager.sanitize_title(cfg['titolo'])}.docx"
        risultato = kdp_formatter.build_manuscript_docx(manoscritto, docx_path)
        print(f"[assembla] {risultato}")

        out = {"docx": str(docx_path), "pagine": risultato.estimated_pages,
               "parole": risultato.word_count, "entro_target": risultato.within_target}

        if not risultato.within_target and not forza:
            parole_mancanti = risultato.target_min_words - risultato.word_count
            capitoli_mancanti = max(1, round(parole_mancanti / cfg["parole_per_capitolo"]))
            raise RuntimeError(
                f"Libro FUORI TARGET: {risultato.word_count} parole "
                f"(~{risultato.estimated_pages} pagine), servono almeno "
                f"{risultato.target_min_words}. Mancano circa {parole_mancanti} parole = "
                f"~{capitoli_mancanti} capitoli. Il .docx e' stato comunque salvato in "
                f"{docx_path} per controllo, ma NON e' pubblicabile cosi'."
            )

        if cover_path and Path(cover_path).exists():
            pacchetto = book_output_manager.create_book_package(
                book_title=cfg["titolo"],
                manuscript_path=docx_path,
                cover_path=Path(cover_path),
                kdp_metadata_text=self._metadata_kdp(cfg, risultato),
                word_count=risultato.word_count,
                page_count=risultato.estimated_pages,
            )
            out["pacchetto"] = str(pacchetto.folder_path)
            print(f"[assembla] pacchetto pronto: {pacchetto.folder_path}")
        else:
            print("[assembla] copertina non fornita — genera prima la copertina "
                  "(python -m engine.cover_generator) e ripassala con --cover")
        return out

    def _metadata_kdp(self, cfg: dict, risultato) -> str:
        return (
            f"Titolo: {cfg['titolo']}\n"
            f"Autore: {cfg.get('autore', 'Digital Empire')}\n"
            f"Nicchia/keyword: {cfg.get('nicchia', '')}\n"
            f"Parole: {risultato.word_count}\n"
            f"Pagine stimate: {risultato.estimated_pages}\n"
            f"Trim size: {config.TRIM_SIZE_INCHES[0]}x{config.TRIM_SIZE_INCHES[1]} in\n"
        )


def lista_progetti() -> list[str]:
    if not PROGETTI_DIR.exists():
        return []
    return sorted(d.name for d in PROGETTI_DIR.iterdir()
                  if d.is_dir() and (d / "progetto.json").exists())


if __name__ == "__main__":
    import argparse
    import sys

    cli = argparse.ArgumentParser(description="Gestione progetti libro (PIANO KDP V2)")
    sub = cli.add_subparsers(dest="cmd", required=True)

    c_nuovo = sub.add_parser("nuovo", help="crea un nuovo progetto libro")
    c_nuovo.add_argument("titolo")
    c_nuovo.add_argument("--nicchia", required=True)
    c_nuovo.add_argument("--autore", default="Digital Empire")
    c_nuovo.add_argument("--capitoli", type=int, default=DEFAULT_TOTAL_CHAPTERS)
    c_nuovo.add_argument("--parole-per-capitolo", type=int, default=DEFAULT_WORDS_PER_CHAPTER)

    c_stato = sub.add_parser("stato", help="a che punto e' un libro")
    c_stato.add_argument("slug", nargs="?")

    c_ass = sub.add_parser("assembla", help="genera il .docx (e il pacchetto se c'e' la copertina)")
    c_ass.add_argument("slug")
    c_ass.add_argument("--cover", default=None)
    c_ass.add_argument("--forza", action="store_true",
                       help="assembla anche se incompleto/fuori target (solo per bozze)")

    args = cli.parse_args()

    if args.cmd == "nuovo":
        p = BookProject.crea(args.titolo, args.nicchia, args.autore,
                             args.capitoli, args.parole_per_capitolo)
        print(f"Progetto creato: {p.dir}")
        print(f"  1. Scrivi l'outline in:  {p.outline_path}")
        print(f"  2. Poi i capitoli in:    {p.capitoli_dir}\\cap_01.md ... cap_{args.capitoli:02d}.md")
        print(f"  3. Controlla quando vuoi: python -m engine.book_project stato {p.slug}")
        sys.exit(0)

    if args.cmd == "stato":
        if not args.slug:
            progetti = lista_progetti()
            if not progetti:
                print("Nessun progetto libro. Creane uno con 'nuovo'.")
                sys.exit(0)
            print("Progetti:")
            for s in progetti:
                st = BookProject(s).stato()
                print(f"  - {s}: {len(st.capitoli_scritti)}/{st.capitoli_totali} capitoli, "
                      f"{st.parole_scritte} parole")
            sys.exit(0)
        print(BookProject(args.slug).stato())
        sys.exit(0)

    if args.cmd == "assembla":
        p = BookProject(args.slug)
        try:
            p.assembla(Path(args.cover) if args.cover else None, forza=args.forza)
        except RuntimeError as e:
            print(f"\nSTOP: {e}")
            sys.exit(1)
        sys.exit(0)
