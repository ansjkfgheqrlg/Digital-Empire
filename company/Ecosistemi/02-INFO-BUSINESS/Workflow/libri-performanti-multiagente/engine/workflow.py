"""
IL WORKFLOW — i 4 step, in quest'ordine, ogni volta uguale (2026-08-12).

Definito da Gael. Un solo avvio produce un libro completo nella nicchia del catalogo:

    STEP 0  Controllo salute della nicchia ATTIVA (non una scelta: una verifica)
    STEP 1  Trova il libro competitor di riferimento dentro quella nicchia
    STEP 2  Scrive il libro con Claude Code, modello HAIKU
    STEP 3  Genera la copertina con LM Arena (Playwright)
    STEP 4  Mette tutto in LIBRI/libri_pronti/<Titolo_Del_Libro>/

LE DUE REGOLE CHE PRIMA SBAGLIAVO, e che ora sono nel codice:

1. **La nicchia NON si sceglie ogni volta.** Si sceglie una volta e ci si costruisce sopra
   un catalogo. Prima di ogni libro si controlla solo se e' ancora sana; si cambia
   soltanto se ne esiste una nettamente migliore (vedi `nicchia_attiva.py`).

2. **L'obiettivo e' il volume di vendite.** Il flusso e' costruito per girare tante volte
   con poco attrito: modello economico, nessuna decisione da prendere a runtime, output
   sempre nello stesso posto e nella stessa forma.

UN LIMITE DA CONOSCERE, non un'obiezione: KDP rimuove i titoli che ricevono troppe
segnalazioni per qualita' insufficiente, e un account con rimozioni ripetute viene chiuso
— portandosi via l'intero catalogo. Per questo i controlli minimi (lunghezza reale,
capitoli non duplicati, copertina conforme) restano bloccanti anche in un flusso pensato
per il volume: servono a proteggere il catalogo, che e' l'asset.

USO:
    python -m engine.workflow nicchia-scegli --keywords "a" "b" "c"   # UNA VOLTA, la prima
    python -m engine.workflow libro                                    # ogni libro nuovo
    python -m engine.workflow riprendi <slug>                          # finisce un libro rotto
    python -m engine.workflow nicchia-stato
    python -m engine.workflow nicchia-confronta --keywords "x" --applica   # cambio col margine

DUE COSE CHE IL FLUSSO ORA FA DAVVERO (2026-08-14), e che prima erano solo dichiarate:

- **La nicchia si sceglie una volta sul serio.** `nicchia-scegli` si rifiuta di partire se
  ce n'e' gia' una: prima misurava e poi sovrascriveva in silenzio, quindi bastava
  rilanciarlo per ritrovarsi con una nicchia nuova e un catalogo orfano — esattamente
  l'impostazione sbagliata. Il cambio esiste, ma passa da `nicchia-confronta --applica` e
  pretende il margine; la nicchia lasciata viene archiviata coi suoi libri, non cancellata.
- **Un libro scritto non si butta.** Se la copertina fallisce, i capitoli restano e
  `riprendi <slug>` porta il libro fino a `libri_pronti/` senza riscriverne uno. Prima lo
  step piu' economico del flusso distruggeva il lavoro del piu' caro.
"""
from __future__ import annotations

import logging
import sys
from datetime import datetime
from pathlib import Path

from . import config

log = logging.getLogger("workflow")

OK, VALIDAZIONE_FALLITA, CONFIG_ERRATA, ERRORE_SISTEMA = 0, 1, 2, 3


# --------------------------------------------------------------------------- #
# STEP 0 — la nicchia e' ancora buona?
# --------------------------------------------------------------------------- #

def step0_controllo_nicchia() -> dict:
    from . import nicchia_attiva

    esito = nicchia_attiva.controlla_salute()
    print(f"\n[STEP 0] {esito['messaggio']}")
    return esito


# --------------------------------------------------------------------------- #
# STEP 1 — il libro competitor di riferimento
# --------------------------------------------------------------------------- #

def step1_competitor(keyword: str, gia_scaricati: list[str] | None = None) -> dict:
    """I libri veri in prima pagina su Amazon per la nicchia del catalogo.

    Servono a capire cosa compra il lettore di questa nicchia: che tono, che promessa in
    copertina, che fascia di prezzo. Il testo del nostro libro resta originale — KDP
    verifica i manoscritti e chiude gli account per contenuti derivati.

    RIUSA i competitor che lo STEP 0 ha appena scaricato, se ci sono. Prima rifaceva da
    capo la STESSA ricerca sulla stessa keyword: lavoro doppio che raddoppiava le
    probabilita' di fallire, e infatti il 2026-08-14 lo STEP 0 e' passato e lo STEP 1 e'
    andato in timeout tre volte di fila mandando all'aria il run. Si riscarica solo se lo
    STEP 0 non ha potuto misurare (Amazon irraggiungibile in quel momento)."""
    if gia_scaricati:
        print(f"[STEP 1] {len(gia_scaricati)} concorrenti dallo STEP 0 (nessuna ricerca "
              f"ripetuta). Riferimento: {gia_scaricati[0][:60]}")
        return {"riferimento": {"titolo": gia_scaricati[0]}, "titoli": gia_scaricati}

    from playwright.sync_api import sync_playwright

    from . import amazon_research

    with sync_playwright() as p:
        listings = amazon_research.search_amazon(p, keyword, headless=True)
    if not listings:
        raise RuntimeError(f"Amazon non ha restituito risultati per '{keyword}'.")

    riferimento = listings[0]
    print(f"[STEP 1] {len(listings)} concorrenti trovati. Riferimento: {riferimento.title[:60]}")
    return {
        "riferimento": {"titolo": riferimento.title, "asin": riferimento.asin,
                         "prezzo": riferimento.price, "recensioni": riferimento.reviews_count},
        "titoli": [b.title for b in listings[:10]],
    }


# --------------------------------------------------------------------------- #
# STEP 2 — scrittura con Haiku
# --------------------------------------------------------------------------- #

def estrai_titolo(outline: str) -> str | None:
    """Pesca il titolo definitivo dall'impianto, o None se non c'e'.

    Tollera la decorazione markdown (2026-08-13): il modello scrive spesso `**TITLE:** X`
    o `# TITLE: X` invece della riga nuda chiesta dal prompt. La versione precedente
    accettava solo `TITLE:` in testa e in silenzio teneva il titolo di lavoro — il primo
    libro prodotto si chiamava "Untitled Small Town Romance Suspense 202608131759", che e'
    esattamente il genere di titolo che fa segnalare un libro su KDP."""
    for riga in outline.splitlines():
        pulita = riga.strip().lstrip("#*_ \t").strip()
        if not pulita.upper().startswith("TITLE"):
            continue
        _, sep, valore = pulita.partition(":")
        if not sep:
            continue
        valore = valore.strip().strip("*_\"'").strip()
        if valore:
            return valore
    return None


def step2_scrivi(nicchia: str, titolo_lavoro: str, competitor: list[str],
                  capitoli: int, parole_per_capitolo: int,
                  tentativi_outline: int = 3) -> "BookProject":
    from . import book_project, scrittore_haiku

    print(f"[STEP 2] impianto del libro (modello {scrittore_haiku.MODELLO})...")
    titolo, outline_grezzo = None, ""
    for tentativo in range(1, tentativi_outline + 1):
        outline_grezzo = scrittore_haiku.genera(
            scrittore_haiku.prompt_outline(nicchia, titolo_lavoro, competitor))
        titolo = estrai_titolo(outline_grezzo)
        if titolo:
            break
        print(f"  [outline] tentativo {tentativo}: nessuna riga TITLE: leggibile — rigenero")

    # Meglio fermare un libro che pubblicarne uno intitolato "Untitled ...": il titolo e' la
    # prima cosa che vede il lettore e un placeholder brucia credibilita' all'intero catalogo.
    if not titolo:
        raise RuntimeError(
            f"L'impianto non contiene un titolo leggibile dopo {tentativi_outline} tentativi. "
            f"Il libro non viene creato: un titolo placeholder su KDP e' un rischio per "
            f"l'account. Prime righe ricevute: {outline_grezzo[:200]!r}"
        )

    progetto = book_project.BookProject.crea(titolo, nicchia, capitoli=capitoli,
                                              parole_per_capitolo=parole_per_capitolo)
    progetto.outline_path.write_text(f"# Outline — {titolo}\n\n{outline_grezzo}\n", encoding="utf-8")
    print(f"[STEP 2] titolo: {titolo}  ({progetto.slug})")

    riassunto, corpi = "", []
    for n in range(1, capitoli + 1):
        corpo, nuovo = scrittore_haiku.scrivi_capitolo(
            titolo, nicchia, outline_grezzo, n, capitoli, riassunto,
            parole_per_capitolo, corpi)
        progetto.path_capitolo(n).write_text(corpo, encoding="utf-8")
        corpi.append(corpo)
        riassunto = f"{riassunto} {nuovo}".strip()
        progetto.riassunti_path.write_text(riassunto, encoding="utf-8")
        print(f"[STEP 2] capitolo {n}/{capitoli} scritto ({len(corpo.split())} parole)")

    return progetto


# --------------------------------------------------------------------------- #
# STEP 3 — copertina
# --------------------------------------------------------------------------- #

def step3_copertina(progetto, nicchia: str, outline: str) -> Path:
    from playwright.sync_api import sync_playwright

    from . import cover_generator, lmarena_client

    cfg = progetto._config()
    contesto = {"writing": {"title": cfg["titolo"]},
                "planning": {"title": cfg["titolo"], "characters": "", "act1": outline[:400]},
                "research": {"keyword": nicchia}}
    grezza = progetto.dir / "copertina_generata.png"

    print("[STEP 3] copertina su LM Arena...")
    with sync_playwright() as p:
        sessione = lmarena_client.open_session(p)
        try:
            cover_generator.generate_cover(sessione.page, contesto, grezza, verifica=False)
        finally:
            sessione.close()

    kdp = cover_generator.adatta_a_kdp(grezza, progetto.dir / "copertina_kdp.png")
    finale = cover_generator.aggiungi_titolo(kdp, cfg["titolo"], cfg.get("autore", "Digital Empire"),
                                              progetto.dir / "copertina_finale.png")
    print(f"[STEP 3] copertina pronta: {finale.name}")
    return finale


# --------------------------------------------------------------------------- #
# Il flusso completo
# --------------------------------------------------------------------------- #

def produci_libro(capitoli: int = 24, parole_per_capitolo: int = 1550) -> int:
    """I 4 step in sequenza. Un avvio = un libro pronto in LIBRI/libri_pronti/<Titolo>/."""
    from . import nicchia_attiva

    inizio = datetime.now()

    # STEP 0
    salute = step0_controllo_nicchia()
    if salute["stato"] == "nessuna_nicchia":
        print("\nNessuna nicchia attiva. Scegline una UNA VOLTA con:\n"
              "  python -m engine.workflow nicchia-scegli --keywords \"...\" \"...\"")
        return CONFIG_ERRATA
    if salute["stato"] == "peggiorata":
        print("  La nicchia e' sotto soglia: si procede comunque con questo libro, ma "
              "valuta un cambio con 'nicchia-confronta'.")

    n = nicchia_attiva.carica()
    nicchia = n.keyword

    # STEP 1 — riusa i competitor gia' scaricati dallo STEP 0
    try:
        mercato = step1_competitor(nicchia, salute.get("competitor"))
    except Exception as e:
        log.error("STEP 1 fallito: %s", e)
        return ERRORE_SISTEMA

    # STEP 2
    try:
        titolo_lavoro = f"Untitled {nicchia.title()} {datetime.now():%Y%m%d%H%M}"
        progetto = step2_scrivi(nicchia, titolo_lavoro, mercato["titoli"],
                                 capitoli, parole_per_capitolo)
    except Exception as e:
        log.error("STEP 2 fallito: %s", e)
        return ERRORE_SISTEMA

    return _step3_e_step4(progetto, nicchia, inizio)


def _step3_e_step4(progetto, nicchia: str, inizio: datetime) -> int:
    """La coda del flusso: copertina e pacchetto. Separata perche' si deve poter RIPRENDERE.

    Prima era in linea dentro `produci_libro`, e una copertina fallita buttava via il libro:
    24 capitoli gia' scritti e pagati restavano in `in_lavorazione`, il flusso usciva con
    errore senza mai arrivare allo STEP 4, e il rilancio ripartiva da zero (col titolo
    identico `BookProject.crea` sollevava pure FileExistsError). Lo step piu' economico
    distruggeva il lavoro del piu' caro."""
    from . import nicchia_attiva

    # STEP 3
    try:
        copertina = step3_copertina(progetto, nicchia,
                                     progetto.outline_path.read_text(encoding="utf-8"))
    except Exception as e:
        log.error("STEP 3 fallito (copertina): %s", e)
        print(f"\n  Il TESTO DEL LIBRO E' SALVO in {progetto.dir}")
        print(f"  Non e' andato perso niente: la copertina si rigenera da sola e il libro")
        print(f"  arriva in libri_pronti/ senza riscrivere un capitolo. Riprendi con:")
        print(f"    python -m engine.workflow riprendi {progetto.slug}")
        return ERRORE_SISTEMA

    # STEP 4
    try:
        esito = progetto.assembla(copertina)
    except RuntimeError as e:
        print(f"\n[STEP 4] il libro non e' pubblicabile cosi': {e}")
        print(f"  Il materiale resta in {progetto.dir}: si corregge e si riprende con")
        print(f"    python -m engine.workflow riprendi {progetto.slug}")
        return VALIDAZIONE_FALLITA

    nicchia_attiva.registra_libro(progetto._config()["titolo"])
    minuti = (datetime.now() - inizio).total_seconds() / 60
    print(f"\n[STEP 4] pacchetto pronto: {esito['pacchetto']}")
    print(f"LIBRO COMPLETATO in {minuti:.0f} minuti — nicchia '{nicchia}', "
          f"{len(nicchia_attiva.carica().libri_pubblicati)} libri nel catalogo.")
    return OK


def riprendi_libro(slug: str) -> int:
    """Porta a termine un libro gia' scritto: capitoli mancanti, copertina, pacchetto.

    Esiste perche' il flusso deve poter ricominciare dal punto in cui si e' rotto invece
    che dall'inizio — su un catalogo che punta al volume, rifare 24 capitoli per una
    copertina fallita e' il modo piu' rapido di bruciare il margine."""
    from . import book_project, nicchia_attiva, scrittore_haiku

    inizio = datetime.now()
    progetto = book_project.BookProject(slug)
    try:
        cfg = progetto._config()
    except FileNotFoundError as e:
        print(f"Progetto '{slug}' non trovato: {e}")
        return CONFIG_ERRATA

    stato = progetto.stato()
    nicchia = cfg.get("nicchia", "")
    print(f"[riprendi] {cfg['titolo']} — {len(stato.capitoli_scritti)}/{stato.capitoli_totali} "
          f"capitoli gia' scritti")

    # STEP 2, solo il pezzo mancante: i capitoli gia' su disco non si riscrivono.
    if not stato.completo:
        outline = progetto.outline_path.read_text(encoding="utf-8")
        riassunto = (progetto.riassunti_path.read_text(encoding="utf-8")
                     if progetto.riassunti_path.exists() else "")
        corpi = [progetto.path_capitolo(n).read_text(encoding="utf-8")
                 for n in stato.capitoli_scritti]
        try:
            for n in range(1, stato.capitoli_totali + 1):
                if n in stato.capitoli_scritti:
                    continue
                corpo, nuovo = scrittore_haiku.scrivi_capitolo(
                    cfg["titolo"], nicchia, outline, n, stato.capitoli_totali,
                    riassunto, cfg["parole_per_capitolo"], corpi)
                progetto.path_capitolo(n).write_text(corpo, encoding="utf-8")
                corpi.append(corpo)
                riassunto = f"{riassunto} {nuovo}".strip()
                progetto.riassunti_path.write_text(riassunto, encoding="utf-8")
                print(f"[riprendi] capitolo {n}/{stato.capitoli_totali} scritto "
                      f"({len(corpo.split())} parole)")
        except Exception as e:
            log.error("Scrittura dei capitoli mancanti fallita: %s", e)
            return ERRORE_SISTEMA

    return _step3_e_step4(progetto, nicchia, inizio)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    import argparse

    cli = argparse.ArgumentParser(
        prog="python -m engine.workflow",
        description="Workflow libri KDP a 4 step. La nicchia si sceglie UNA VOLTA.",
        epilog="Exit: 0 ok | 1 non pubblicabile | 2 configurazione | 3 errore di sistema")
    sub = cli.add_subparsers(dest="comando", required=True)

    s = sub.add_parser("nicchia-scegli", help="[una tantum] fissa la nicchia del catalogo")
    s.add_argument("--keywords", nargs="+", required=True)

    sub.add_parser("nicchia-stato", help="la nicchia attiva e come sta")

    c = sub.add_parser("nicchia-confronta", help="verifica se conviene cambiare nicchia")
    c.add_argument("--keywords", nargs="+", required=True)
    c.add_argument("--applica", action="store_true",
                   help="se una candidata supera il margine, cambia davvero la nicchia")

    l = sub.add_parser("libro", help="produce il prossimo libro del catalogo (i 4 step)")
    l.add_argument("--capitoli", type=int, default=24)
    l.add_argument("--parole-per-capitolo", type=int, default=1550)

    r = sub.add_parser("riprendi", help="finisce un libro gia' iniziato (capitoli/copertina/pacchetto)")
    r.add_argument("slug")

    args = cli.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)-7s %(message)s")
    from . import nicchia_attiva

    if args.comando == "nicchia-scegli":
        from . import niche_finder

        # La nicchia si sceglie UNA VOLTA: se ce n'e' gia' una, questo comando non deve
        # nemmeno partire. Prima misurava e poi sovrascriveva in silenzio, riportando il
        # flusso all'impostazione sbagliata (nicchia nuova a ogni giro, catalogo orfano).
        attuale = nicchia_attiva.carica()
        if attuale is not None:
            print(f"C'e' gia' una nicchia attiva: '{attuale.keyword}' "
                  f"({attuale.punteggio_corrente}/100, {len(attuale.libri_pubblicati)} libri).")
            print("La nicchia si sceglie UNA VOLTA e ci si costruisce sopra il catalogo.")
            print("Per valutare un cambio (serve un vantaggio netto):")
            print(f"  python -m engine.workflow nicchia-confronta --keywords \"...\" --applica")
            return CONFIG_ERRATA

        esiti = niche_finder.trova_nicchie(args.keywords)
        if not esiti:
            return ERRORE_SISTEMA
        niche_finder.stampa_classifica(esiti)
        migliore = esiti[0]
        n = nicchia_attiva.imposta(migliore.keyword, migliore.punteggio, migliore.motivazione)
        print(f"\nNICCHIA DEL CATALOGO FISSATA: '{n.keyword}' ({n.punteggio_iniziale}/100)")
        print("Tutti i libri successivi nasceranno da questa. Per produrne uno:")
        print("  python -m engine.workflow libro")
        return OK

    if args.comando == "nicchia-stato":
        n = nicchia_attiva.carica()
        if n is None:
            print("Nessuna nicchia attiva.")
            return CONFIG_ERRATA
        print(f"Nicchia: {n.keyword}")
        print(f"Scelta il: {n.scelta_il[:10]} con punteggio {n.punteggio_iniziale}/100")
        print(f"Punteggio corrente: {n.punteggio_corrente}/100 "
              f"({'sana' if n.sana else 'SOTTO SOGLIA'})")
        print(f"Libri nel catalogo: {len(n.libri_pubblicati)}")
        for t in n.libri_pubblicati:
            print(f"  - {t}")
        return OK

    if args.comando == "nicchia-confronta":
        esito = nicchia_attiva.valuta_cambio(args.keywords)
        print(f"\n{esito.get('messaggio', esito)}")

        if not args.applica:
            if esito.get("stato") == "conviene_cambiare":
                print("\nPer cambiare davvero rilancia con --applica "
                      "(la nicchia lasciata resta archiviata nello storico).")
            return OK

        if esito.get("stato") != "conviene_cambiare":
            print("\nNiente da applicare: nessuna candidata supera il margine.")
            return OK

        migliore = esito["migliore_candidata"]
        try:
            n = nicchia_attiva.cambia(migliore["keyword"], migliore["punteggio"],
                                       migliore["motivazione"])
        except nicchia_attiva.NicchiaGiaScelta as e:
            print(f"\nCambio rifiutato: {e}")
            return CONFIG_ERRATA
        precedente = n.storico[-1]
        print(f"\nNICCHIA CAMBIATA: '{precedente['keyword']}' -> '{n.keyword}' "
              f"({n.punteggio_iniziale}/100)")
        print(f"  Archiviati nello storico i {len(precedente['libri_pubblicati'])} libri "
              f"costruiti sulla nicchia precedente.")
        return OK

    if args.comando == "libro":
        return produci_libro(args.capitoli, args.parole_per_capitolo)

    if args.comando == "riprendi":
        return riprendi_libro(args.slug)

    return CONFIG_ERRATA


if __name__ == "__main__":
    sys.exit(main())
