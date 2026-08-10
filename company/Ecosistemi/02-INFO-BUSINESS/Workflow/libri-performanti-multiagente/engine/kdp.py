"""
Comando unico del workflow KDP (Snippet 8 del piano del 2026-08-10, RF-05).

Prima servivano tre comandi separati e bisognava ricordarsi l'ordine. Qui c'e' un solo
punto d'ingresso con sottocomandi, exit code espliciti e un log su file per ogni
esecuzione.

    python -m engine.kdp nicchie --keywords "cozy mystery" "small town romance"
    python -m engine.kdp nuovo "Titolo Del Libro" --nicchia "cozy mystery"
    python -m engine.kdp stato [slug]
    python -m engine.kdp consegna <slug> --cover copertina.png

EXIT CODE (contratto stabile, usabile da uno script o da una tile Aureus):
    0  tutto a posto
    1  validazione fallita: il libro NON e' pubblicabile cosi'
    2  parametri o configurazione sbagliati
    3  errore di sistema (file mancanti, dipendenze, imprevisti)
"""
from __future__ import annotations

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

from . import config

OK, VALIDAZIONE_FALLITA, CONFIG_ERRATA, ERRORE_SISTEMA = 0, 1, 2, 3

log = logging.getLogger("kdp")


def _configura_log(cartella: Path, verbose: bool) -> Path:
    """Log a schermo + su file, uno per esecuzione con timestamp nel nome (RNF-03/04):
    quando un run fallisce dopo mezz'ora, il file e' l'unico modo di sapere cos'e'
    successo senza rilanciare tutto."""
    cartella.mkdir(parents=True, exist_ok=True)
    file_log = cartella / f"kdp_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    livello = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=livello,
        format="%(asctime)s  %(levelname)-7s %(name)s: %(message)s",
        handlers=[logging.FileHandler(file_log, encoding="utf-8"), logging.StreamHandler()],
        force=True,
    )
    log.debug("Log di questa esecuzione: %s", file_log)
    return file_log


# --------------------------------------------------------------------------- #
# Sottocomandi
# --------------------------------------------------------------------------- #

def _cmd_nicchie(args) -> int:
    from . import niche_finder

    keywords = list(args.keywords or [])
    if args.file:
        percorso = Path(args.file)
        if not percorso.exists():
            log.error("File keyword non trovato: %s", percorso)
            return CONFIG_ERRATA
        keywords += [r.strip() for r in percorso.read_text(encoding="utf-8").splitlines()
                     if r.strip() and not r.startswith("#")]
    if not keywords:
        log.error("Serve almeno una keyword (--keywords oppure --file).")
        return CONFIG_ERRATA

    esiti = niche_finder.trova_nicchie(keywords, headless=not args.visibile)
    if not esiti:
        log.error("Nessuna nicchia analizzata: Amazon non ha risposto per nessuna keyword.")
        return ERRORE_SISTEMA
    niche_finder.stampa_classifica(esiti, top=args.top)
    return OK


def _cmd_nuovo(args) -> int:
    from .book_project import BookProject

    try:
        p = BookProject.crea(args.titolo, args.nicchia, args.autore,
                             args.capitoli, args.parole_per_capitolo)
    except FileExistsError as e:
        log.error("%s", e)
        return CONFIG_ERRATA

    log.info("Progetto creato: %s", p.dir)
    print(f"\n  1. Scrivi l'outline:   {p.outline_path}")
    print(f"  2. Poi i capitoli in:  {p.capitoli_dir}")
    print(f"  3. Controlla lo stato: python -m engine.kdp stato {p.slug}\n")
    return OK


def _cmd_stato(args) -> int:
    from .book_project import BookProject, lista_progetti

    if not args.slug:
        progetti = lista_progetti()
        if not progetti:
            print("Nessun libro in lavorazione.")
            return OK
        print("Libri in lavorazione:\n")
        for s in progetti:
            st = BookProject(s).stato()
            print(f"  {s}: {len(st.capitoli_scritti)}/{st.capitoli_totali} capitoli, "
                  f"{st.parole_scritte} parole")
        return OK
    try:
        print(BookProject(args.slug).stato())
    except FileNotFoundError as e:
        log.error("%s", e)
        return CONFIG_ERRATA
    return OK


def _cmd_consegna(args) -> int:
    """Assembla il pacchetto finale e dice se il libro e' pubblicabile."""
    from .book_project import BookProject

    progetto = BookProject(args.slug)
    cover = Path(args.cover) if args.cover else None
    if cover and not cover.exists():
        log.error("Copertina non trovata: %s", cover)
        return CONFIG_ERRATA

    try:
        esito = progetto.assembla(cover, forza=args.forza)
    except FileNotFoundError as e:
        log.error("%s", e)
        return CONFIG_ERRATA
    except RuntimeError as e:
        # Il libro esiste ma non e' pubblicabile: pagine sotto target, capitoli mancanti.
        log.error("%s", e)
        return VALIDAZIONE_FALLITA
    except Exception as e:  # imprevisto vero
        log.exception("Errore di sistema durante la consegna: %s", e)
        return ERRORE_SISTEMA

    if not esito.get("pacchetto"):
        log.warning("Pacchetto non creato: manca la copertina. Passa --cover <file.png>.")
        return VALIDAZIONE_FALLITA

    print(f"\nPacchetto pronto: {esito['pacchetto']}")
    if esito.get("report"):
        print(f"Report di consegna: {Path(esito['report']).name}")
    return OK


# --------------------------------------------------------------------------- #
# Entrypoint
# --------------------------------------------------------------------------- #

def costruisci_parser() -> argparse.ArgumentParser:
    cli = argparse.ArgumentParser(
        prog="python -m engine.kdp",
        description="Workflow libri KDP: scelta nicchia, progetto, consegna.",
        epilog="Exit code: 0 ok | 1 non pubblicabile | 2 parametri errati | 3 errore di sistema",
    )
    cli.add_argument("--verbose", action="store_true", help="log dettagliato")
    sub = cli.add_subparsers(dest="comando", required=True)

    n = sub.add_parser("nicchie", help="analizza nicchie su Amazon e le classifica")
    n.add_argument("--keywords", nargs="+")
    n.add_argument("--file", help="file con una keyword per riga")
    n.add_argument("--top", type=int, default=10)
    n.add_argument("--visibile", action="store_true", help="mostra il browser")

    c = sub.add_parser("nuovo", help="crea un nuovo progetto libro")
    c.add_argument("titolo")
    c.add_argument("--nicchia", required=True)
    c.add_argument("--autore", default="Digital Empire")
    c.add_argument("--capitoli", type=int, default=24)
    c.add_argument("--parole-per-capitolo", type=int, default=1500)

    s = sub.add_parser("stato", help="a che punto sono i libri")
    s.add_argument("slug", nargs="?")

    d = sub.add_parser("consegna", help="assembla il pacchetto finale (docx, pdf, copertina, report)")
    d.add_argument("slug")
    d.add_argument("--cover", help="percorso della copertina .png")
    d.add_argument("--forza", action="store_true", help="assembla anche se fuori target")

    return cli


def main(argv: list[str] | None = None) -> int:
    args = costruisci_parser().parse_args(argv)
    _configura_log(config.LIBRI_DIR / "_log", args.verbose)
    log.debug("Comando: %s", args.comando)

    azioni = {"nicchie": _cmd_nicchie, "nuovo": _cmd_nuovo,
              "stato": _cmd_stato, "consegna": _cmd_consegna}
    try:
        return azioni[args.comando](args)
    except KeyboardInterrupt:
        log.warning("Interrotto da tastiera.")
        return ERRORE_SISTEMA
    except Exception as e:
        log.exception("Errore non gestito: %s", e)
        return ERRORE_SISTEMA


if __name__ == "__main__":
    sys.exit(main())
