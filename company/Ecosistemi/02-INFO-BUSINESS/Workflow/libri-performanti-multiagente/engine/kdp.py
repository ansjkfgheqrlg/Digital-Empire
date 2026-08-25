"""
Comando unico del workflow KDP — l'attrezzatura che uso mentre scrivo (2026-08-15).

QUESTO E' L'UNICO PUNTO D'INGRESSO. Dal 2026-08-15 il libro lo scrivo io in sessione:
nessun modulo qui chiama un modello, ne' via API, ne' via CLI, ne' pilotando un browser
su un sito di chat. Il codice fa solo cio' che una macchina fa meglio di me — misurare
nicchie su Amazon, impaginare secondo le regole KDP, contare le pagine VERE dal PDF,
validare e impacchettare.

    python -m engine.kdp magazzino                      # gli argomenti pronti
    python -m engine.kdp magazzino --aggiungi f.json    # ci metto la ricerca fatta
    python -m engine.kdp magazzino --prendi             # il prossimo da scrivere
    python -m engine.kdp nicchie --keywords "cozy mystery" "small town romance"
    python -m engine.kdp nicchia-stato | nicchia-scegli | nicchia-confronta
    python -m engine.kdp nuovo "Titolo Del Libro" --nicchia "cozy mystery"
    python -m engine.kdp stato [slug]
    python -m engine.kdp consegna <slug> --cover copertina.png

La procedura completa e' in `SOP-SCRIVERE-UN-LIBRO.md` e nella skill `/libro`.

EXIT CODE (contratto stabile, usabile da uno script o da una tile Aureus):
    0  tutto a posto
    1  validazione fallita: il libro NON e' pubblicabile cosi'
    2  parametri o configurazione sbagliati
    3  errore di sistema (file mancanti, dipendenze, imprevisti)
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path

from . import config, metriche

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


def estrai_titolo(testo: str) -> str | None:
    """Pesca il titolo definitivo da un outline, o None se non c'e'.

    Tollera la decorazione markdown: il modello scrive spesso `**TITLE:** X` o `# TITLE: X`
    invece della riga nuda. La versione rigida accettava solo `TITLE:` in testa e in
    silenzio teneva il titolo di lavoro — il primo libro prodotto si chiamava "Untitled
    Small Town Romance Suspense 202608131759", che e' esattamente il genere di titolo che
    fa segnalare un libro su KDP.

    Vive qui (spostata da `workflow.py` il 2026-08-15, quando quel modulo e' stato
    archiviato) perche' e' una funzione pura su stringhe e serve ancora: la uso per
    ricontrollare un outline che ho appena scritto."""
    for riga in testo.splitlines():
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


def _cmd_magazzino(args) -> int:
    """Il magazzino degli argomenti: il "flusso atemporale" di Gael."""
    from . import magazzino

    if args.aggiungi:
        percorso = Path(args.aggiungi)
        if not percorso.exists():
            log.error("File non trovato: %s", percorso)
            return CONFIG_ERRATA
        try:
            dati = json.loads(percorso.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            log.error("JSON non valido in %s: %s", percorso, e)
            return CONFIG_ERRATA
        if isinstance(dati, dict):
            dati = [dati]

        inseriti, problemi = magazzino.aggiungi(dati)
        for p in problemi:
            log.warning("SCARTATO — %s", p)
        print(f"\nInseriti {len(inseriti)} argomenti su {len(dati)} proposti.")
        for a in inseriti:
            print(f"  + {a.titolo_lavoro}  ({a.nicchia})")
        # Se non e' entrato NIENTE ed erano stati proposti argomenti, e' un fallimento:
        # meglio un exit code che dice "non e' successo quello che credevi".
        return OK if inseriti or not dati else CONFIG_ERRATA

    if args.prendi:
        a = magazzino.prendi()
        if a is None:
            print("Magazzino esaurito: nessun argomento libero.")
            print("Serve una ricerca nuova prima di scrivere il prossimo libro.")
            return CONFIG_ERRATA
        print(f"\nProssimo argomento (ora marcato in uso):\n")
        print(f"  Titolo di lavoro : {a.titolo_lavoro}")
        print(f"  Nicchia          : {a.nicchia}")
        print(f"  Premessa         : {a.premessa}")
        print(f"  Dati Amazon      : {a.dati_amazon}")
        print(f"\nCrea il progetto con:")
        print(f"  python -m engine.kdp nuovo \"{a.titolo_lavoro}\" --nicchia \"{a.nicchia}\"\n")
        return OK

    argomenti = magazzino.carica()
    if not argomenti:
        print("Magazzino vuoto. Va riempito con una ricerca "
              "(python -m engine.kdp magazzino --aggiungi <file.json>).")
        return OK
    c = magazzino.conteggi()
    print(f"\nMagazzino argomenti — {c['totale']} totali: "
          f"{c['libero']} liberi, {c['in_uso']} in uso, {c['fatto']} fatti\n")
    for a in argomenti:
        print("  " + a.riga())
    print()
    return OK


def _cmd_nicchia(args) -> int:
    """Gestione della nicchia persistente del catalogo.

    Salvata da `workflow.py` prima della sua archiviazione (2026-08-15): e' logica
    deterministica sui dati Amazon, non ha mai avuto niente a che fare con un modello.
    La regola resta quella di Gael: la nicchia si sceglie UNA VOLTA e ci si costruisce
    sopra un catalogo; si cambia solo se ne esiste una nettamente migliore."""
    from . import nicchia_attiva

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

    if args.comando == "nicchia-scegli":
        from . import niche_finder

        attuale = nicchia_attiva.carica()
        if attuale is not None:
            print(f"C'e' gia' una nicchia attiva: '{attuale.keyword}' "
                  f"({attuale.punteggio_corrente}/100, {len(attuale.libri_pubblicati)} libri).")
            print("La nicchia si sceglie UNA VOLTA e ci si costruisce sopra il catalogo.")
            print("Per valutare un cambio (serve un vantaggio netto):")
            print("  python -m engine.kdp nicchia-confronta --keywords \"...\" --applica")
            return CONFIG_ERRATA

        esiti = niche_finder.trova_nicchie(args.keywords)
        if not esiti:
            return ERRORE_SISTEMA
        niche_finder.stampa_classifica(esiti)
        migliore = esiti[0]
        n = nicchia_attiva.imposta(migliore.keyword, migliore.punteggio, migliore.motivazione)
        print(f"\nNICCHIA DEL CATALOGO FISSATA: '{n.keyword}' ({n.punteggio_iniziale}/100)")
        return OK

    # nicchia-confronta
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


def _controlla_nicchia_catalogo(nicchia: str, motivo: str | None) -> str | None:
    """La disciplina di catalogo, applicata quando serve: alla creazione del libro.

    PERCHE' (2026-08-23). `nicchia_attiva.py` esiste da 12 giorni, sono 251 righe con
    storico, soglia di salute e margine per cambiare, e i primi tre libri del catalogo sono
    usciti in TRE nicchie diverse — nessuna delle quali e' quella attiva:

        nicchia attiva            small town romance suspense
        The Quiet Hours           psychological thriller unreliable narrator
        The Ninth Winter          amish romance suspense
        The Second-Hand Spellbook cozy fantasy bookshop

    Il controllo c'era e nessun percorso di codice lo interrogava: si sceglieva la nicchia
    con un comando e poi se ne scriveva un'altra con un comando diverso. Su KDP quello che
    vende il primo libro e' il secondo libro dello stesso autore nella stessa nicchia:
    saltare a ogni titolo butta via l'associazione fra i libri, la pagina autore e le
    recensioni che si spingono a vicenda.

    Non blocca in modo cieco: `--motivo` lascia passare uno scarto dichiarato (una prova,
    un libro di prestito a un'altra nicchia). Quello che non e' piu' possibile e' cambiare
    nicchia **senza accorgersene**. Ritorna il messaggio da stampare, o None."""
    from . import nicchia_attiva

    attiva = nicchia_attiva.carica()
    if attiva is None:
        return ("Nessuna nicchia di catalogo fissata. Si puo' scrivere lo stesso, ma finche' "
                "non c'e' i libri non si sommano: 'kdp nicchia-scegli --keywords \"...\"'.")
    if nicchia.strip().lower() == attiva.keyword.strip().lower():
        return None
    if motivo:
        return (f"Scarto DICHIARATO dalla nicchia di catalogo '{attiva.keyword}': {motivo}. "
                f"Registrato in progetto.json.")
    raise ValueError(
        f"La nicchia del catalogo e' '{attiva.keyword}' ({attiva.punteggio_corrente}/100, "
        f"{len(attiva.libri_pubblicati)} libri), questo libro sarebbe '{nicchia}'.\n"
        f"  Su KDP il secondo libro nella stessa nicchia e' cio' che vende il primo: "
        f"associazione fra titoli, pagina autore, recensioni che si spingono.\n"
        f"  Se e' voluto:  --motivo \"<perche'>\"   (resta scritto nel progetto)\n"
        f"  Se la nicchia e' da cambiare per davvero: "
        f"kdp nicchia-confronta --keywords \"{nicchia}\" --applica"
    )


def _cmd_nuovo(args) -> int:
    from .book_project import BookProject

    try:
        nota_nicchia = _controlla_nicchia_catalogo(args.nicchia, args.motivo)
    except ValueError as e:
        log.error("%s", e)
        return CONFIG_ERRATA

    try:
        p = BookProject.crea(args.titolo, args.nicchia, args.autore,
                             args.capitoli, args.parole_per_capitolo)
    except FileExistsError as e:
        log.error("%s", e)
        return CONFIG_ERRATA

    if args.motivo:
        p._aggiorna_config(scarto_nicchia={"nicchia_catalogo": args.nicchia,
                                           "motivo": args.motivo})
    metriche.registra(p.slug, "progetto_creato", nicchia=args.nicchia, autore=args.autore)
    log.info("Progetto creato: %s", p.dir)
    if nota_nicchia:
        print(f"\n  NICCHIA: {nota_nicchia}")
    cfg = p._config()
    bersaglio = cfg["capitoli_totali"] * cfg["parole_per_capitolo"]
    pagine = round(bersaglio / config.WORDS_PER_PAGE_ESTIMATE)
    print()
    print(f"  Bersaglio: {cfg['parole_per_capitolo']} parole x {cfg['capitoli_totali']} "
          f"capitoli = {bersaglio} parole (~{pagine} pagine)")
    print(f"  Finestra accettata: {config.TARGET_WORD_COUNT_MIN}-"
          f"{config.TARGET_WORD_COUNT_MAX} parole. Il bersaglio sta in MEZZO, non al minimo:")
    print( "  e' voluto. Mirare al bordo costa quattro riprese a fine libro.")
    print()
    print(f"  1. Outline:          {p.outline_path}")
    print(f"  2. Prompt copertina: {p.dir / 'copertina-prompt.md'}")
    print( "     >> DALLO A GAEL SUBITO, prima di scrivere i capitoli. Genera l'immagine")
    print( "     mentre scrivi: aspettarla a libro finito e' costato un giorno intero")
    print( "     su The Ninth Winter (libro finito il 17, copertina il 18).")
    print(f"  3. Capitoli in:      {p.capitoli_dir}")
    print(f"  4. Dopo OGNI blocco: python -m engine.kdp blocco {p.slug}")
    print( "     Meno di un secondo, e ferma i difetti al capitolo 8 invece che al 24.")
    print(f"  5. Alla fine:        python -m engine.kdp consegna {p.slug} --cover <png>")
    print()
    return OK


def _cmd_blocco(args) -> int:
    """Il gate da lanciare dopo ogni gruppo di capitoli. Gira in meno di un secondo:
    niente PDF, niente OCR — quelli restano alla consegna, che si fa una volta sola."""
    from .book_project import BookProject
    from . import gate_blocco

    try:
        esito = gate_blocco.controlla(BookProject(args.slug))
    except FileNotFoundError as e:
        log.error("%s", e)
        return CONFIG_ERRATA
    print(esito)
    # Ogni passaggio dal gate lascia una riga: e' da qui che si vede, a libro finito, che
    # i 18 minuti in piu' erano tre bocciature per capitoli corti e non "il flusso lento".
    metriche.registra(args.slug, "blocco",
                      esito="ok" if esito.si_prosegue else "bocciato",
                      capitoli=esito.capitoli_scritti, parole=esito.parole,
                      media_per_capitolo=esito.media_per_capitolo,
                      motivi=esito.blocchi or None)
    return OK if esito.si_prosegue else VALIDAZIONE_FALLITA


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
    print()
    print(metriche.riepilogo(args.slug))
    return OK


def _cmd_copy(args) -> int:
    """Salva il copy KDP del libro (Fase 5) e lo valida PRIMA di scriverlo.

    PERCHE' ESISTE (2026-08-25, TASK-KDP-W1). `BookProject.salva_copy()` c'era dal
    2026-08-15, ma nel flusso vivo non lo chiamava nessuno: nessun comando lo esponeva.
    Risultato misurato sui tre libri consegnati: il copy e' stato scritto **a mano dentro
    `progetto.json`**, cioe' modificando a mano un file di configurazione, e i difetti si
    scoprivano solo alla consegna. Le lineette lunghe nella descrizione di The Ninth
    Winter (3) e di The Quiet Hours (2) sono uscite proprio cosi', e quei due pacchetti
    erano gia' stati consegnati.

    Qui il copy entra da un file JSON, passa da `valida_copy_kdp` e, se ha problemi, NON
    viene salvato: exit 1. Il posto giusto per fermare un difetto e' dove nasce."""
    from . import validators
    from .book_project import BookProject

    progetto = BookProject(args.slug)
    if not progetto.progetto_path.exists():
        log.error("Nessun progetto '%s'. Vedi: python -m engine.kdp stato", args.slug)
        return CONFIG_ERRATA

    percorso = Path(args.file)
    if not percorso.exists():
        log.error("File del copy non trovato: %s", percorso)
        return CONFIG_ERRATA
    try:
        copy = json.loads(percorso.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        log.error("Il file del copy non e' JSON valido (%s): %s", percorso.name, e)
        return CONFIG_ERRATA
    if not isinstance(copy, dict) or not copy:
        log.error("Il copy deve essere un oggetto JSON con i campi KDP, non %s vuoto/errato.",
                  type(copy).__name__)
        return CONFIG_ERRATA

    # I campi che la form di KDP chiede davvero al caricamento. Senza uno di questi il
    # pacchetto esce col "minimo storico" e quel campo va inventato davanti alla form:
    # e' esattamente il pezzo che si perdeva fra una sessione e l'altra.
    obbligatori = ("titolo_finale", "descrizione", "keywords", "categorie")
    mancanti = [c for c in obbligatori if not copy.get(c)]
    if mancanti:
        log.error("Copy incompleto, mancano: %s", ", ".join(mancanti))
        return VALIDAZIONE_FALLITA

    problemi = validators.valida_copy_kdp(copy)
    if problemi:
        log.error("Copy NON salvato: %d problemi da correggere.", len(problemi))
        for p in problemi:
            log.error("  - %s", p)
        return VALIDAZIONE_FALLITA

    progetto.salva_copy(copy)
    print(f"[copy] salvato in {progetto.progetto_path}")
    print(f"[copy] titolo: {copy['titolo_finale']}")
    print(f"[copy] descrizione: {len(copy['descrizione'])} caratteri | "
          f"keyword: {len(copy.get('keywords') or [])} | "
          f"categorie: {len(copy.get('categorie') or [])}")
    if copy.get("prezzo_suggerito_usd"):
        print(f"[copy] prezzo suggerito: ${copy['prezzo_suggerito_usd']}")
    return OK


def _cmd_pacchetto(args) -> int:
    """Verifica che la cartella finale contenga DAVVERO i tre artefatti del flusso.

    E' la forma controllabile a macchina del gate TASK-KDP-W1: manoscritto, prompt della
    copertina e copy KDP dentro UNA cartella. Distingue due stati diversi che prima si
    confondevano:

      - COMPLETO: ci sono i tre artefatti che il flusso produce da solo (exit 0)
      - CARICABILE SU KDP: c'e' anche l'immagine di copertina, che la genera una persona

    Un pacchetto completo ma senza immagine non e' un difetto del flusso: e' il punto
    esatto in cui il lavoro passa a Gael."""
    from . import book_output_manager
    from .book_project import BookProject

    progetto = BookProject(args.slug)
    if not progetto.progetto_path.exists():
        log.error("Nessun progetto '%s'. Vedi: python -m engine.kdp stato", args.slug)
        return CONFIG_ERRATA
    cfg = progetto._config()
    cartella = config.LIBRI_PRONTI_DIR / book_output_manager.sanitize_title(cfg["titolo"])
    if not cartella.is_dir():
        log.error("Nessuna cartella finale per '%s' (attesa: %s). Serve prima la consegna: "
                  "python -m engine.kdp consegna %s", cfg["titolo"], cartella, args.slug)
        return VALIDAZIONE_FALLITA

    titolo_file = book_output_manager.sanitize_title(cfg["titolo"])
    attesi = {
        "manoscritto (.docx)": cartella / f"{titolo_file}.docx",
        "PDF (pagine reali)": cartella / f"{titolo_file}.pdf",
        "EPUB (ebook)": cartella / f"{titolo_file}.epub",
        "prompt copertina": cartella / "COPERTINA-PROMPT.md",
        "metadati KDP": cartella / "KDP_METADATA.txt",
        "report di consegna": cartella / "REPORT.md",
        "verdetto": cartella / "validazione.json",
    }
    mancanti = [nome for nome, p in attesi.items() if not p.exists()]

    # Il copy dev'essere quello vero, non il "minimo storico": un KDP_METADATA.txt senza
    # descrizione e' un file presente che non serve a niente al caricamento.
    copy = cfg.get("copy_kdp") or {}
    if not copy.get("descrizione"):
        mancanti.append("copy KDP reale (descrizione/keyword: c'e' solo il minimo storico)")

    print(f"Pacchetto: {cartella}")
    for nome, p in attesi.items():
        segno = "OK  " if p.exists() else "MANCA"
        print(f"  [{segno}] {nome}: {p.name}")
    print(f"  [{'OK  ' if copy.get('descrizione') else 'MANCA'}] copy KDP nel progetto: "
          f"{len(copy.get('descrizione') or '')} caratteri di descrizione")

    copertina = next((p for p in cartella.glob("Cover_*") if p.is_file()), None)
    if mancanti:
        log.error("Pacchetto INCOMPLETO, mancano: %s", "; ".join(mancanti))
        return VALIDAZIONE_FALLITA

    print("\nCOMPLETO: manoscritto + prompt copertina + copy KDP sono nella stessa cartella.")
    if copertina:
        print(f"CARICABILE SU KDP: copertina presente ({copertina.name}).")
    else:
        print("NON ancora caricabile: manca l'immagine di copertina. Generala dal prompt "
              f"in COPERTINA-PROMPT.md, poi: python -m engine.kdp consegna {args.slug} "
              "--cover <file.png>")
    return OK


def _cmd_consegna(args) -> int:
    """Assembla il pacchetto finale e dice se il libro e' pubblicabile."""
    from . import copertina_kdp
    from .book_project import BookProject

    progetto = BookProject(args.slug)
    cover = Path(args.cover) if args.cover else None
    if cover and not cover.exists():
        log.error("Copertina non trovata: %s", cover)
        return CONFIG_ERRATA

    # La copertina arriva da fuori (generata da Gael col prompt che ho scritto io): prima
    # di impacchettarla va portata a norma KDP — 2:3, 1800x2700. Se il titolo e' gia'
    # disegnato dentro l'immagine (il modo normale dal 2026-08-15) NON si riscrive sopra,
    # altrimenti comparirebbe due volte.
    if cover:
        try:
            cfg = progetto._config()
            esito_cover = copertina_kdp.prepara_copertina(
                cover, titolo=cfg["titolo"], autore=cfg.get("autore", "Digital Empire"),
                titolo_gia_in_copertina=not args.scrivi_titolo)
            cover = esito_cover["path"]
        except FileNotFoundError as e:
            log.error("%s", e)
            return CONFIG_ERRATA
        except Exception as e:
            log.exception("Impossibile preparare la copertina: %s", e)
            return ERRORE_SISTEMA

    try:
        esito = progetto.assembla(cover, forza=args.forza)
    except FileNotFoundError as e:
        log.error("%s", e)
        return CONFIG_ERRATA
    except RuntimeError as e:
        # Il libro esiste ma non e' pubblicabile: pagine sotto target, capitoli mancanti.
        log.error("%s", e)
        metriche.registra(args.slug, "consegna", esito="non_pubblicabile",
                          con_copertina=bool(cover), motivi=[str(e)[:200]])
        return VALIDAZIONE_FALLITA
    except Exception as e:  # imprevisto vero
        log.exception("Errore di sistema durante la consegna: %s", e)
        return ERRORE_SISTEMA

    metriche.registra(args.slug, "consegna", esito="ok", con_copertina=bool(cover),
                      pagine_reali=esito.get("pagine_reali"),
                      parole=esito.get("parole"))

    if not esito.get("pacchetto"):
        log.warning("Pacchetto non creato: manca la copertina. Passa --cover <file.png>.")
        return VALIDAZIONE_FALLITA

    print(f"\nPacchetto pronto: {esito['pacchetto']}")
    if esito.get("report"):
        print(f"Report di consegna: {Path(esito['report']).name}")
    print(f"Quando e' su KDP:  python -m engine.kdp pubblicato {args.slug} --asin <ASIN>")
    return OK


def _cmd_pubblicato(args) -> int:
    """Chiude il ciclo: il libro e' su KDP, l'archivio lo registra e i doppioni spariscono."""
    from . import pubblicazione

    try:
        esito = pubblicazione.pubblica(
            args.slug, asin=args.asin, url=args.url or "", prezzo=args.prezzo,
            forza=args.forza, tieni_lavorazione=args.tieni_lavorazione)
    except pubblicazione.NonPubblicabile as e:
        log.error("%s", e)
        return VALIDAZIONE_FALLITA
    except (FileNotFoundError, FileExistsError) as e:
        log.error("%s", e)
        return CONFIG_ERRATA
    except Exception as e:
        log.exception("Errore durante l'archiviazione: %s", e)
        return ERRORE_SISTEMA

    print()
    print(esito)
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

    m = sub.add_parser("magazzino", help="gli argomenti pronti da scrivere (flusso atemporale)")
    m.add_argument("--aggiungi", metavar="FILE.JSON",
                   help="inserisce gli argomenti di una ricerca (validati prima di entrare)")
    m.add_argument("--prendi", action="store_true",
                   help="restituisce il prossimo argomento libero e lo marca in uso")

    n = sub.add_parser("nicchie", help="analizza nicchie su Amazon e le classifica")
    n.add_argument("--keywords", nargs="+")
    n.add_argument("--file", help="file con una keyword per riga")
    n.add_argument("--top", type=int, default=10)
    n.add_argument("--visibile", action="store_true", help="mostra il browser")

    sub.add_parser("nicchia-stato", help="la nicchia attiva del catalogo e come sta")

    ns = sub.add_parser("nicchia-scegli", help="[una tantum] fissa la nicchia del catalogo")
    ns.add_argument("--keywords", nargs="+", required=True)

    nc = sub.add_parser("nicchia-confronta", help="verifica se conviene cambiare nicchia")
    nc.add_argument("--keywords", nargs="+", required=True)
    nc.add_argument("--applica", action="store_true",
                    help="se una candidata supera il margine, cambia davvero la nicchia")

    c = sub.add_parser("nuovo", help="crea un nuovo progetto libro")
    c.add_argument("titolo")
    c.add_argument("--nicchia", required=True)
    c.add_argument("--motivo", default=None,
                   help="perche' questo libro esce dalla nicchia del catalogo. Senza, un "
                        "libro in una nicchia diversa da quella attiva viene rifiutato: e' "
                        "cosi' che i primi tre sono usciti in tre nicchie scollegate")
    c.add_argument("--autore", default="Digital Empire")
    c.add_argument("--capitoli", type=int, default=24)
    from .book_project import DEFAULT_WORDS_PER_CHAPTER
    c.add_argument("--parole-per-capitolo", type=int,
                   default=DEFAULT_WORDS_PER_CHAPTER,
                   help="default calcolato dal centro della finestra pagine di config")

    b = sub.add_parser("blocco",
                       help="gate rapido dopo un gruppo di capitoli (<1s, niente PDF)")
    b.add_argument("slug")

    s = sub.add_parser("stato", help="a che punto sono i libri")
    s.add_argument("slug", nargs="?")

    cp = sub.add_parser("copy",
                        help="salva il copy KDP del libro (titolo, descrizione, keyword, "
                             "categorie) validandolo prima di scriverlo")
    cp.add_argument("slug")
    cp.add_argument("--file", required=True,
                    help="JSON col copy: titolo_finale, sottotitolo, descrizione, keywords, "
                         "categorie, codici_bisac, bio_autore, descrizione_html, "
                         "prezzo_suggerito_usd")

    pk = sub.add_parser("pacchetto",
                        help="verifica che la cartella finale contenga i tre artefatti "
                             "(manoscritto, prompt copertina, copy KDP)")
    pk.add_argument("slug")

    d = sub.add_parser("consegna", help="assembla il pacchetto finale (docx, pdf, copertina, report)")
    d.add_argument("slug")
    d.add_argument("--cover", help="percorso della copertina .png generata da te")
    d.add_argument("--scrivi-titolo", action="store_true",
                   help="scrive titolo e autore SOPRA la copertina con Pillow. Serve solo "
                        "se l'immagine e' arrivata senza testo o col testo sbagliato: "
                        "normalmente il titolo e' gia' dentro l'immagine (lo chiede il prompt)")
    d.add_argument("--forza", action="store_true", help="assembla anche se fuori target")

    pb = sub.add_parser("pubblicato",
                        help="il libro e' su KDP: archivia il pacchetto, registra l'ASIN, "
                             "toglie i doppioni")
    pb.add_argument("slug")
    pb.add_argument("--asin", required=True, help="l'ASIN che KDP assegna al libro")
    pb.add_argument("--url", default=None, help="link alla pagina Amazon (se diverso da /dp/ASIN)")
    pb.add_argument("--prezzo", type=float, default=None, help="prezzo di listino effettivo")
    pb.add_argument("--tieni-lavorazione", action="store_true",
                    help="non cancellare LIBRI/in_lavorazione/<slug>/ dopo l'archiviazione")
    pb.add_argument("--forza", action="store_true",
                    help="archivia anche un pacchetto non pubblicabile (resta scritto in "
                         "pubblicazione.json)")

    return cli


def main(argv: list[str] | None = None) -> int:
    args = costruisci_parser().parse_args(argv)
    _configura_log(config.LIBRI_DIR / "_log", args.verbose)
    log.debug("Comando: %s", args.comando)

    azioni = {"magazzino": _cmd_magazzino, "nicchie": _cmd_nicchie,
              "nicchia-stato": _cmd_nicchia, "nicchia-scegli": _cmd_nicchia,
              "nicchia-confronta": _cmd_nicchia, "nuovo": _cmd_nuovo,
              "stato": _cmd_stato, "blocco": _cmd_blocco,
              "copy": _cmd_copy, "pacchetto": _cmd_pacchetto,
              "consegna": _cmd_consegna, "pubblicato": _cmd_pubblicato}
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
