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


def _apri_staging_google_doc(playwright, titolo: str, progetto):
    """Apre il Google Doc di sicurezza per i capitoli, oppure ritorna None.

    Non solleva MAI: lo staging e' un di piu'. Se non parte, i capitoli si scrivono
    comunque su disco — che e' il canale affidabile — e il libro non ne risente."""
    from . import config, google_doc_staging

    if not config.GOOGLE_DOC_STAGING_ENABLED:
        return None
    try:
        sessione = google_doc_staging.open_or_create_doc(
            playwright, titolo, doc_url_esistente=progetto._config().get("google_doc_url"))
        progetto._aggiorna_config(google_doc_url=sessione.doc_url)
        print(f"[STEP 2] staging Google Doc attivo: {sessione.doc_url}")
        return sessione
    except Exception as e:
        print(f"[STEP 2] staging Google Doc non disponibile ({e}) — si prosegue senza: "
              f"i capitoli restano comunque salvati su disco.")
        return None


def step2_scrivi(nicchia: str, titolo_lavoro: str, competitor: list[str],
                  capitoli: int, parole_per_capitolo: int,
                  tentativi_outline: int = 3, *,
                  force_new_chat: bool = True, profilo_reale: bool = False):
    """FASI 2 e 3 — piano di produzione e capitoli, tutto su LM Arena.

    Ritorna `(progetto, sessione_arena)`: la sessione resta APERTA di proposito, perche' la
    Fase 5 (copy KDP) deve girare nella STESSA chat degli ultimi capitoli — richiesta
    esplicita di Gael. Chiuderla qui renderebbe quella richiesta impossibile. Chi chiama e'
    responsabile di chiuderla (vedi `produci_libro`, che lo fa in un `finally`).

    `tentativi_outline` non serve piu' a inseguire una riga TITLE leggibile (il retry vive
    dentro `arena_book_writer.generate_plan`), ma a rigenerare un piano che il verificatore
    boccia: un sommario incompleto o una trama che non e' una storia si scoprono PRIMA di
    scrivere 24 capitoli, non dopo."""
    from playwright.sync_api import sync_playwright

    from . import arena_book_writer, book_project, google_doc_staging, lmarena_client

    playwright_cm = sync_playwright().start()
    sessione = lmarena_client.open_session(playwright_cm, headless=False,
                                            profilo_reale=profilo_reale)
    doc_session = None
    try:
        # --- FASE 2: piano di produzione (sommario capitoli + prompt copertina) --- #
        print(f"[STEP 2] piano di produzione su LM Arena ({capitoli} capitoli)...")
        piano, problemi = None, []
        for tentativo in range(1, tentativi_outline + 1):
            piano = arena_book_writer.generate_plan(
                sessione.page, {"titoli": competitor}, nicchia, titolo_lavoro,
                capitoli=capitoli)
            problemi = arena_book_writer.verifica_piano(piano, capitoli)
            if not problemi:
                break
            print(f"  [piano] tentativo {tentativo}: non passa la verifica — rigenero")
            for p in problemi:
                print(f"    - {p}")

        if problemi:
            raise RuntimeError(
                f"Il piano non passa la verifica dopo {tentativi_outline} tentativi: "
                f"{'; '.join(problemi)}. Il libro non viene creato — meglio zero libri che "
                f"24 capitoli scritti su un impianto sbagliato."
            )

        titolo = piano["title"]
        progetto = book_project.BookProject.crea(
            titolo, nicchia, capitoli=capitoli, parole_per_capitolo=parole_per_capitolo)
        progetto.salva_piano(piano)
        progetto.outline_path.write_text(
            f"# Piano di produzione — {titolo}\n\n"
            f"**Personaggi:** {piano['characters']}\n\n"
            f"**Atto 1:** {piano['act1']}\n\n**Atto 2:** {piano['act2']}\n\n"
            f"**Atto 3:** {piano['act3']}\n\n## Capitoli\n\n"
            + "\n".join(f"{i}. {c}" for i, c in enumerate(piano["chapters"], 1))
            + f"\n\n## Prompt copertina\n\n{piano['cover_prompt']}\n",
            encoding="utf-8")
        print(f"[STEP 2] titolo: {titolo}  ({progetto.slug})")

        # --- FASE 3: capitoli uno alla volta, con staging di sicurezza --- #
        doc_session = _apri_staging_google_doc(playwright_cm, titolo, progetto)
        arena_book_writer.write_chapters(
            sessione.page, progetto, piano, force_new_chat=force_new_chat,
            parole_per_capitolo=parole_per_capitolo, doc_session=doc_session)

        # L'URL della chat serve alla Fase 5 di sopravvivere a un'interruzione: un
        # `riprendi` in un processo nuovo puo' tentare di riaprirla invece di perdere la
        # continuita' con i capitoli appena scritti.
        try:
            progetto.salva_url_chat(sessione.page.url)
        except Exception:
            pass

        return progetto, sessione
    except Exception:
        # Se qualcosa esplode qui la sessione non serve piu' a nessuno: va chiusa, altrimenti
        # resta un browser orfano aperto. In caso di successo NON si chiude (serve alla Fase 5).
        try:
            sessione.close()
        finally:
            playwright_cm.stop()
        raise
    finally:
        if doc_session is not None:
            google_doc_staging.close(doc_session)


def step2b_copy(sessione, progetto, piano: dict) -> dict:
    """FASE 5 — copy KDP (titolo finale, sottotitolo, descrizione, keyword, categorie).

    Gira nella STESSA chat degli ultimi capitoli (`force_new_chat=False`), subito dopo
    l'ultimo capitolo e prima di chiudere la sessione: e' la richiesta esplicita di Gael, e
    il motivo per cui `step2_scrivi` restituisce la sessione ancora aperta.

    Non blocca il libro se fallisce: senza copy il pacchetto esce comunque, con il
    `KDP_METADATA.txt` minimo. Meglio un libro consegnato con i metadati da scrivere a mano
    che un libro perso per una descrizione."""
    from . import arena_book_writer

    print("[STEP 2b] copy KDP nella stessa chat dei capitoli...")
    try:
        copy = arena_book_writer.generate_copy(sessione.page, piano, progetto,
                                                force_new_chat=False)
    except Exception as e:
        print(f"[STEP 2b] copy non generato ({e}) — il libro prosegue senza. "
              f"KDP_METADATA.txt restera' quello minimo.")
        return {}

    problemi = arena_book_writer.verifica_copy(copy)
    for p in problemi:
        print(f"[STEP 2b] copy: {p}")
    progetto.salva_copy(copy)
    print(f"[STEP 2b] copy salvato — titolo finale: {copy.get('titolo_finale', '?')}")
    return copy


# --------------------------------------------------------------------------- #
# STEP 3 — copertina
# --------------------------------------------------------------------------- #

def step3_copertina(progetto, nicchia: str, piano: dict | None = None,
                     *, profilo_reale: bool = False) -> Path:
    """FASE 4 — copertina, dal prompt gia' deciso nel PIANO (Fase 2).

    Il prompt creativo non si costruisce piu' a runtime: arriva dal piano, come chiesto da
    Gael ("nel piano non solo c'e' il sommario, ma anche il prompt per la copertina"). I
    vincoli tecnici KDP (formato 2:3, spelling esatto del titolo) restano fissi nel codice —
    sono stati conquistati con bug reali e non si delegano a un modello.

    Sessione Arena PROPRIA, aperta e chiusa qui: la copertina e' l'unica fase in modalita'
    immagine, e tenerla separata permette di rigenerarla da sola con `riprendi` senza
    toccare i capitoli."""
    from playwright.sync_api import sync_playwright

    from . import cover_generator, lmarena_client

    cfg = progetto._config()
    piano = piano or progetto.piano()
    if not piano:
        raise RuntimeError(
            "Nessun piano salvato per questo libro: la copertina si genera dal prompt del "
            "piano (Fase 2). Progetto creato con un flusso precedente?"
        )
    grezza = progetto.dir / "copertina_generata.png"

    print("[STEP 3] copertina su LM Arena (prompt dal piano)...")
    with sync_playwright() as p:
        sessione = lmarena_client.open_session(p, profilo_reale=profilo_reale)
        try:
            cover_generator.generate_cover_from_plan(
                sessione.page, piano, title=cfg["titolo"],
                author=cfg.get("autore", "Digital Empire"), out_path=grezza,
                genre=nicchia, verifica=False)
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

def produci_libro(capitoli: int = 24, parole_per_capitolo: int = 1550, *,
                   force_new_chat: bool = True, profilo_reale: bool = False) -> int:
    """Il flusso completo. Un avvio = un libro pronto in LIBRI/libri_pronti/<Titolo>/.

    `force_new_chat` e `profilo_reale` sono le due variabili che la FASE 0
    (`python -m engine.lmarena_captcha_probe`) misura: quale pattern di chat e quale
    profilo browser reggano meglio il captcha. Restano parametri, coi default di oggi,
    finche' quella misura non c'e' — non si cabla in produzione un'ipotesi non verificata."""
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

    # STEP 2 + 3 (piano e capitoli) e subito dopo il copy, nella STESSA sessione Arena
    try:
        titolo_lavoro = f"Untitled {nicchia.title()} {datetime.now():%Y%m%d%H%M}"
        progetto, sessione = step2_scrivi(nicchia, titolo_lavoro, mercato["titoli"],
                                           capitoli, parole_per_capitolo,
                                           force_new_chat=force_new_chat,
                                           profilo_reale=profilo_reale)
    except Exception as e:
        log.error("STEP 2 fallito: %s", e)
        return ERRORE_SISTEMA

    # FASE 5 prima della copertina: il copy deve girare nella stessa chat dei capitoli,
    # quindi PRIMA di chiudere questa sessione. La copertina (Fase 4) apre una sessione
    # propria in modalita' immagine, quindi puo' venire dopo senza perdere niente —
    # l'ordine nel codice differisce dalla numerazione delle fasi per necessita' tecnica.
    try:
        step2b_copy(sessione, progetto, progetto.piano() or {})
    finally:
        try:
            sessione.close()
        except Exception:
            pass

    return _step3_e_step4(progetto, nicchia, inizio, profilo_reale=profilo_reale)


def _step3_e_step4(progetto, nicchia: str, inizio: datetime, *,
                    profilo_reale: bool = False) -> int:
    """La coda del flusso: copertina e pacchetto. Separata perche' si deve poter RIPRENDERE.

    Prima era in linea dentro `produci_libro`, e una copertina fallita buttava via il libro:
    24 capitoli gia' scritti e pagati restavano in `in_lavorazione`, il flusso usciva con
    errore senza mai arrivare allo STEP 4, e il rilancio ripartiva da zero (col titolo
    identico `BookProject.crea` sollevava pure FileExistsError). Lo step piu' economico
    distruggeva il lavoro del piu' caro."""
    from . import nicchia_attiva

    # STEP 3
    try:
        copertina = step3_copertina(progetto, nicchia, progetto.piano(),
                                     profilo_reale=profilo_reale)
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


def riprendi_libro(slug: str, *, force_new_chat: bool = True,
                    profilo_reale: bool = False) -> int:
    """Porta a termine un libro gia' iniziato: capitoli mancanti, copy, copertina, pacchetto.

    Esiste perche' il flusso deve poter ricominciare dal punto in cui si e' rotto invece
    che dall'inizio — su un catalogo che punta al volume, rifare 24 capitoli per una
    copertina fallita e' il modo piu' rapido di bruciare il margine.

    Se mancano capitoli riapre una sessione Arena e scrive SOLO quelli; poi, se il copy non
    c'e' ancora, lo genera nella stessa sessione prima di chiuderla (Fase 5). Se i capitoli
    sono tutti a posto non apre nessuna sessione di scrittura: va dritto a copertina e
    pacchetto."""
    from playwright.sync_api import sync_playwright

    from . import arena_book_writer, book_project, google_doc_staging, lmarena_client

    inizio = datetime.now()
    progetto = book_project.BookProject(slug)
    try:
        cfg = progetto._config()
    except FileNotFoundError as e:
        print(f"Progetto '{slug}' non trovato: {e}")
        return CONFIG_ERRATA

    stato = progetto.stato()
    nicchia = cfg.get("nicchia", "")
    piano = progetto.piano()
    print(f"[riprendi] {cfg['titolo']} — {len(stato.capitoli_scritti)}/{stato.capitoli_totali} "
          f"capitoli gia' scritti")

    if not stato.completo or not progetto.copy_kdp():
        if not piano:
            print("[riprendi] nessun piano salvato: questo libro e' stato iniziato con un "
                  "flusso precedente e non si puo' riprendere da qui.")
            return CONFIG_ERRATA

        playwright_cm = sync_playwright().start()
        sessione = None
        doc_session = None
        try:
            sessione = lmarena_client.open_session(playwright_cm, headless=False,
                                                    profilo_reale=profilo_reale)
            # Continuita' con i capitoli gia' scritti: si tenta di riaprire la stessa chat.
            # Se non ci si riesce si prosegue su una chat nuova, dicendolo — mai una finta
            # continuita' silenziosa.
            url_chat = progetto.url_chat()
            if url_chat and not force_new_chat:
                try:
                    sessione.page.goto(url_chat, wait_until="domcontentloaded")
                    print(f"[riprendi] ripresa la chat precedente: {url_chat}")
                except Exception as e:
                    print(f"[riprendi] impossibile riaprire la chat precedente ({e}) — "
                          f"si prosegue in una chat nuova.")

            if not stato.completo:
                doc_session = _apri_staging_google_doc(playwright_cm, cfg["titolo"], progetto)
                arena_book_writer.write_chapters(
                    sessione.page, progetto, piano, force_new_chat=force_new_chat,
                    da_capitolo=stato.prossimo_capitolo or 1,
                    parole_per_capitolo=cfg["parole_per_capitolo"],
                    doc_session=doc_session)

            if not progetto.copy_kdp():
                step2b_copy(sessione, progetto, piano)
        except Exception as e:
            log.error("Ripresa fallita: %s", e)
            return ERRORE_SISTEMA
        finally:
            if doc_session is not None:
                google_doc_staging.close(doc_session)
            if sessione is not None:
                try:
                    sessione.close()
                except Exception:
                    pass
            playwright_cm.stop()

    return _step3_e_step4(progetto, nicchia, inizio, profilo_reale=profilo_reale)


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
    l.add_argument("--stessa-chat", action="store_true",
                   help="scrive tutti i capitoli nella stessa chat invece di una per capitolo "
                        "(da decidere con l'esito della Fase 0)")
    l.add_argument("--profilo-reale", action="store_true",
                   help="usa il profilo Brave reale invece di quello dedicato (Fase 0). "
                        "Richiede Brave COMPLETAMENTE chiuso.")

    r = sub.add_parser("riprendi", help="finisce un libro gia' iniziato (capitoli/copertina/pacchetto)")
    r.add_argument("slug")
    r.add_argument("--stessa-chat", action="store_true")
    r.add_argument("--profilo-reale", action="store_true")

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
        return produci_libro(args.capitoli, args.parole_per_capitolo,
                              force_new_chat=not args.stessa_chat,
                              profilo_reale=args.profilo_reale)

    if args.comando == "riprendi":
        return riprendi_libro(args.slug, force_new_chat=not args.stessa_chat,
                               profilo_reale=args.profilo_reale)

    return CONFIG_ERRATA


if __name__ == "__main__":
    sys.exit(main())
