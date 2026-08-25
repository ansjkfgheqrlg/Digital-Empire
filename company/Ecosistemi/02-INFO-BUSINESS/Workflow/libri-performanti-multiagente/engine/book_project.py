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

from . import (book_output_manager, book_report, config, epub, ispirazione, kdp_formatter,
                paratesto, report_validazione, validators)

PROGETTI_DIR = config.LIBRI_DIR / "in_lavorazione"

# Si mira al CENTRO della finestra, non al bordo (2026-08-19). config.py accetta 115-125
# pagine: il centro e' 120 pagine = 38.400 parole a 320 p/pag, cioe' 1600 parole per 24
# capitoli. Mirare al minimo e' quello che e' costato caro: The Ninth Winter e' atterrato a
# 115,2 pagine, sul bordo inferiore, e ogni ritocco lo faceva cadere sotto — sono servite
# quattro riprese (111 -> 113 -> 114 -> 115 -> 116), ognuna con un PDF da rigenerare.
# Al centro il margine e' +-1.600 parole per parte e la prima misura passa.
DEFAULT_TOTAL_CHAPTERS = 24
DEFAULT_WORDS_PER_CHAPTER = round(
    (config.TARGET_PAGE_COUNT * config.WORDS_PER_PAGE_ESTIMATE) / 24 / 50) * 50  # 1600


# Formato dei riassunti, fisso (2026-08-19). Non e' pignoleria: `gate_blocco` lo legge.
#
# Prima era prosa libera, e su The Ninth Winter e' cresciuto fino a 4.441 parole per fare lo
# stesso lavoro che su The Quiet Hours ne prendeva 666. Lo rileggo prima di ogni blocco,
# quindi quel peso si paga 3-5 volte per libro.
#
# La sezione "Fili aperti" e' la parte che conta: e' l'unica cosa che avrebbe intercettato
# Efrain (lasciato in sospeso al cap. 15, chiuso con una scena-toppa al 24) ed Emma (mai
# chiusa, aggiunta all'ultimo). Il gate la legge e blocca se un filo invecchia troppo.
MODELLO_RIASSUNTI = """# Riassunti — {titolo}

## Fili aperti

<!-- Una riga per filo, formato:  - [cap NN] cosa e' rimasto in sospeso
     `kdp blocco` BLOCCA se un filo resta aperto per piu' di 6 capitoli: e' cosi' che
     nascono le scene-toppa in coda. Quando il filo si chiude, si cancella la riga. -->

## Capitoli

<!-- Tre righe per capitolo, scritte NELLO STESSO passaggio in cui scrivo il capitolo, mai
     in un giro separato. `kdp blocco` BLOCCA se manca la sezione di un capitolo scritto.

### cap_01
- Succede: cosa accade, una riga
- Cambia: cosa e' diverso da prima (chi sa cosa, chi ha cosa, chi si fida di chi)
- Resta aperto: cosa il lettore si aspetta e non ha ancora avuto
-->
"""


# Cosa BLOCCA la consegna e cosa no, per esteso (2026-08-23). Prima la decisione si
# prendeva con `etichetta.startswith(("Titolo sulla copertina", "Lineette lunghe", ...))`:
# funzionava, ma legava la gravita' di un controllo a come era scritta la sua etichetta —
# un esito nuovo chiamato "Copy KDP assente" sarebbe diventato bloccante per sbaglio.
# Qui la gravita' e' un dato, non una coincidenza di stringhe. Chi non e' in tabella e'
# un avviso.
GRAVITA_ESITI = {
    "Titolo sulla copertina": "bloccante",
    "Lineette lunghe (non devono esserci)": "bloccante",
    "Capitoli interrotti a meta'": "bloccante",
    "Capitoli che si ripetono": "bloccante",
    "Copy KDP (lo legge chi compra)": "bloccante",
    "EPUB (ebook)": "bloccante",
}


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
        # Il MINIMO che blocca la consegna vive in config, non in progetto.json: un libro
        # creato prima di un cambio di taratura porterebbe in giro un bersaglio vecchio e
        # si fermerebbe corto seguendo il proprio file (successo davvero: 'target 36000'
        # stampato quando il minimo era gia' 36.800).
        minimo = config.TARGET_WORD_COUNT_MIN
        righe = [
            f"Libro: {self.titolo}  [{self.slug}]",
            f"Capitoli: {len(self.capitoli_scritti)}/{self.capitoli_totali}",
            f"Parole: {self.parole_scritte} (~{pagine} pagine) — mira a {self.parole_target} "
            f"(~{pagine_target} pagine), minimo per la consegna {minimo}",
        ]
        if self.parole_scritte and self.parole_scritte < minimo:
            righe.append(f"         mancano {minimo - self.parole_scritte} parole al minimo")
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
        self.ispirazione_path = self.dir / "ispirazione.json"
        # Il prompt della copertina: lo scrive Claude in sessione (Fase 3 della skill),
        # ma fino al 2026-08-25 il codice non lo conosceva affatto — quindi non finiva nel
        # pacchetto e non era controllabile. E' uno dei tre artefatti del gate TASK-KDP-W1.
        self.copertina_prompt_path = self.dir / "copertina-prompt.md"

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
                MODELLO_RIASSUNTI.format(titolo=titolo), encoding="utf-8")
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

    # --- piano di produzione e copy KDP (flusso Arena v3, 2026-08-15) --------- #
    def _aggiorna_config(self, **campi) -> None:
        cfg = self._config()
        cfg.update(campi)
        self.progetto_path.write_text(
            json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    def salva_piano(self, piano: dict) -> None:
        """Salva il piano di produzione (Fase 2) come dato STRUTTURATO in progetto.json.

        `outline.md` resta il documento leggibile da una persona, ma il dato autoritativo
        vive qui: Fase 3 (traccia per capitolo), Fase 4 (prompt copertina) e il resume
        devono poter leggere un campo preciso senza ri-parsare testo libero ogni volta."""
        self._aggiorna_config(piano=piano)

    def piano(self) -> dict | None:
        return self._config().get("piano")

    def salva_copy(self, copy: dict) -> None:
        """Salva il copy KDP (Fase 5): titolo finale, sottotitolo, descrizione, keyword,
        categorie. Da qui `_metadata_kdp()` produce un KDP_METADATA.txt davvero
        compilabile, invece del minimo storico (solo titolo/parole/pagine)."""
        self._aggiorna_config(copy_kdp=copy)

    def copy_kdp(self) -> dict | None:
        return self._config().get("copy_kdp")

    def salva_ispirazione(self, scheda: "ispirazione.Ispirazione") -> Path:
        """Salva la scheda del concorrente da cui nasce questo libro.

        Sta in un file suo e non in progetto.json perche' e' ricerca, non configurazione:
        si rilegge scrivendo, si porta nel pacchetto finale, e fra due mesi dice perche'
        questo libro e' stato fatto cosi'."""
        return ispirazione.salva(scheda, self.ispirazione_path)

    def ispirazione(self) -> "ispirazione.Ispirazione | None":
        if not self.ispirazione_path.exists():
            return None
        return ispirazione.carica(self.ispirazione_path)

    def riassunto_progressivo(self) -> str:
        """Il riassunto REALE dei capitoli gia' scritti — stringa vuota se non ce n'e'.

        Serve perche' `crea()` scrive in `riassunti.md` un'intestazione e un commento di
        istruzioni segnaposto, e leggere il file grezzo li restituisce come se fossero
        contenuto (bug reale trovato il 2026-08-15 con una prova diretta): il prompt del
        capitolo 1 riceveva "What has happened so far: # Riassunti progressivi — <titolo>
        <!-- Un paragrafo per capitolo... -->" invece del ramo "questo e' il PRIMO
        capitolo". Ogni libro nasceva con il primo capitolo istruito male, in silenzio —
        i test non lo vedevano perche' usano un invio finto che ignora il prompt.

        Toglie righe di intestazione markdown e commenti HTML: se non resta niente, il
        riassunto non esiste ancora e la risposta corretta e' "" (non il segnaposto)."""
        if not self.riassunti_path.exists():
            return ""
        testo = self.riassunti_path.read_text(encoding="utf-8")
        testo = re.sub(r"<!--.*?-->", " ", testo, flags=re.DOTALL)
        righe = [r for r in testo.splitlines() if not r.lstrip().startswith("#")]
        return " ".join(" ".join(righe).split()).strip()

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

    def _costruisci_epub(self, cfg: dict, capitoli: list, contorno: dict,
                         destinazione: Path, cover: Path | None = None) -> tuple[Path, int]:
        """Scrive l'EPUB e riconta le parole DENTRO il file appena creato."""
        copy = cfg.get("copy_kdp") or {}
        libro = epub.LibroEpub(
            titolo=cfg["titolo"],
            autore=cfg.get("autore", "Digital Empire"),
            capitoli=[epub.CapitoloEpub(c.title, c.paragraphs) for c in capitoli],
            sottotitolo=copy.get("sottotitolo", ""),
            descrizione=copy.get("descrizione", ""),
            copertina=Path(cover) if cover and Path(cover).exists() else None,
            # Il copyright non va nell'indice di un ebook, la richiesta di recensione e il
            # "Also by" si': sono le pagine che un lettore puo' voler raggiungere.
            pagine_iniziali=[(t, p, False) for t, p in contorno["iniziali"]],
            pagine_finali=[(t, p, True) for t, p in contorno["finali"]],
        )
        percorso = epub.costruisci(libro, destinazione)
        return percorso, epub.conta_parole_epub(percorso)

    @staticmethod
    def _controlla_epub(parole_epub: int, parole_docx: int) -> list[str]:
        """L'EPUB deve contenere lo stesso libro del .docx.

        Non e' un controllo di forma: una conversione che perde un capitolo per strada
        produce un file che si apre benissimo e che e' meta' romanzo, ed e' il genere di
        difetto che si scopre da una recensione a una stella. Si tollera uno scarto del 3%,
        che e' la differenza fra come si contano le parole in XHTML e in Word."""
        if not parole_docx:
            return []
        scarto = abs(parole_epub - parole_docx) / parole_docx
        if scarto > 0.03:
            return [f"l'EPUB ha {parole_epub} parole contro le {parole_docx} del "
                    f"manoscritto ({scarto * 100:.0f}% di scarto): la conversione ha perso "
                    f"o duplicato del testo, non caricarlo cosi'."]
        return []

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

        # Le pagine di contorno (copyright davanti; recensione, "Also by" e bio in fondo)
        # entrano sia nel .docx sia nell'EPUB, e non contano nel conteggio parole.
        autore = cfg.get("autore", "Digital Empire")
        contorno = paratesto.costruisci(cfg["titolo"], autore, cfg.get("copy_kdp"),
                                        slug=self.slug)
        capitoli_letti = [self._leggi_capitolo(n) for n in stato.capitoli_scritti]
        manoscritto = kdp_formatter.BookManuscript(
            title=cfg["titolo"],
            author=autore,
            chapters=capitoli_letti,
            subtitle=(cfg.get("copy_kdp") or {}).get("sottotitolo", ""),
            pagine_iniziali=contorno["iniziali"],
            pagine_finali=contorno["finali"],
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

        # --- Controlli editoriali sul testo, PRIMA di impacchettare ----------- #
        testo_completo = "\n\n".join(
            self.path_capitolo(n).read_text(encoding="utf-8") for n in stato.capitoli_scritti
        )
        # Trattini nel sorgente: SEGNALATI, non bloccanti (2026-08-10). Bloccare qui era
        # sbagliato: in narrativa inglese i trattini sono grammatica ('twenty-nine',
        # 'night-time'), e il testo puo' contenerne di voluti ("M-A-R-S-H", un personaggio
        # che fa lo spelling). Il difetto vero — parole spezzate dall'impaginazione — si
        # cerca sul PDF, dove nasce (`valida_sillabazione_pdf`).
        trattini = validators.valida_trattini(testo_completo)
        # Le lineette lunghe invece BLOCCANO (regola di Gael, 2026-08-18): sono la firma
        # piu' riconoscibile della scrittura automatica, e si tolgono riscrivendo la frase.
        lineette = validators.valida_lineette(testo_completo)
        # Capitolo interrotto a meta': nessun altro controllo lo vede. Il conteggio parole
        # e' a posto, le pagine pure, e il libro andrebbe in stampa con un capitolo mozzo.
        testi_capitoli = {f"cap_{n:02d}": self.path_capitolo(n).read_text(encoding="utf-8")
                          for n in stato.capitoli_scritti}
        troncati = []
        for nome, testo_cap in testi_capitoli.items():
            troncati += validators.valida_troncamento(testo_cap, nome)
        # Regola non negoziabile n.2 ("mai un capitolo identico o quasi a un altro"): era
        # l'unica delle sei senza una funzione che la facesse rispettare.
        ripetizioni = validators.valida_ripetizioni(testi_capitoli)
        rip_bloccanti = validators.ripetizioni_bloccanti(ripetizioni)
        # Il copy passa dagli stessi controlli del libro: e' il testo che si legge PRIMA di
        # comprare, ed e' rimasto scoperto fino al 2026-08-23 (3 lineette nella descrizione
        # di The Ninth Winter e 2 in quella di The Quiet Hours, gia' consegnate).
        copy_kdp = cfg.get("copy_kdp")
        esiti = {
            "Capitoli interrotti a meta'": troncati,
            "Lineette lunghe (non devono esserci)": lineette,
            "Capitoli che si ripetono": rip_bloccanti,
            "Capitoli simili (da rileggere)": [r for r in ripetizioni if r not in rip_bloccanti],
            "Copy KDP (lo legge chi compra)": validators.valida_copy_kdp(copy_kdp),
            "Trattini nel testo (da rivedere a occhio)": trattini,
        }
        scheda_ispirazione = self.ispirazione()
        esiti["Prezzo rispetto alla nicchia"] = validators.valida_prezzo(
            (copy_kdp or {}).get("prezzo_suggerito_usd"),
            scheda_ispirazione.prezzo_medio if scheda_ispirazione else None)
        for avviso in esiti["Prezzo rispetto alla nicchia"]:
            print(f"[assembla] prezzo: {avviso}")
        if not copy_kdp:
            esiti["Copy per KDP assente"] = [
                "nessun copy salvato: KDP_METADATA.txt uscira' col minimo storico (titolo, "
                "parole, pagine) e descrizione, keyword, BISAC e bio andranno inventati "
                "davanti alla form di caricamento."]
        for avviso in esiti["Capitoli che si ripetono"] + esiti["Capitoli simili (da rileggere)"]:
            print(f"[assembla] ripetizione: {avviso}")
        for avviso in esiti["Copy KDP (lo legge chi compra)"]:
            print(f"[assembla] copy: {avviso}")
        for avviso in troncati:
            print(f"[assembla] {avviso}")
        if lineette:
            print(f"[assembla] {len(lineette)} righe contengono lineette lunghe (— – --). "
                  f"Vanno tolte riscrivendo la frase: virgola, punto, punto e virgola o "
                  f"parentesi. Elenco completo nel REPORT.")
        if trattini:
            print(f"[assembla] {len(trattini)} trattini segnalati nel testo — controlla il "
                  f"REPORT: in inglese molti sono corretti, non vanno cambiati alla cieca.")

        # LA CARTELLA SI FA SEMPRE (2026-08-25, TASK-KDP-W1). Prima tutto questo blocco
        # girava solo `if cover_path esiste`: senza il .png non nasceva nessun pacchetto,
        # e manoscritto, prompt copertina e copy restavano sparsi fra `in_lavorazione/` e
        # la chat finche' una persona non generava l'immagine. Ora la cartella nasce con i
        # tre artefatti che il flusso produce da solo; la copertina mancante la dichiara
        # `validazione.json` come bloccante, quindi il libro resta NON pubblicabile.
        cover_presente = bool(cover_path and Path(cover_path).exists())
        if cover_presente:
            esiti["Titolo sulla copertina"] = validators.valida_copertina_testo(
                Path(cover_path), cfg["titolo"])
            for avviso in esiti["Titolo sulla copertina"]:
                print(f"[assembla] copertina: {avviso}")
        pacchetto = book_output_manager.create_book_package(
            book_title=cfg["titolo"],
            manuscript_path=docx_path,
            cover_path=Path(cover_path) if cover_presente else None,
            kdp_metadata_text=self._metadata_kdp(cfg, risultato),
            word_count=risultato.word_count,
            page_count=risultato.estimated_pages,
            # Riconsegnare lo stesso libro deve aggiornare la sua cartella, non
            # aggiungerne una nuova col timestamp: qui il libro lo conosciamo per slug.
            sostituisci=True,
            prompt_copertina_path=self.copertina_prompt_path,
        )
        out["pacchetto"] = str(pacchetto.folder_path)
        if pacchetto.prompt_copertina_dest:
            out["copertina_prompt"] = str(pacchetto.prompt_copertina_dest)

        # EPUB accanto al cartaceo (2026-08-23): e' il formato dell'ebook, cioe' il
        # canale che nei generi che scriviamo fa il volume. Fino a oggi il pacchetto
        # era solo .docx + PDF, quindi solo carta.
        epub_dest = pacchetto.folder_path / f"{book_output_manager.sanitize_title(cfg['titolo'])}.epub"
        percorso_epub, parole_epub = self._costruisci_epub(
            cfg, capitoli_letti, contorno, epub_dest, cover=pacchetto.cover_dest)
        out["epub"] = str(percorso_epub)
        esiti["EPUB (ebook)"] = self._controlla_epub(parole_epub, risultato.word_count)
        for avviso in esiti["EPUB (ebook)"]:
            print(f"[assembla] epub: {avviso}")

        # Scheda del concorrente: va nel pacchetto in due formati, JSON per il codice
        # e testo per chi apre la cartella. Se manca si dice, non si finge.
        scheda = self.ispirazione()
        if scheda is None:
            esiti["Scheda libro di ispirazione"] = [
                "assente: nessun ispirazione.json nel progetto. Non blocca, ma il "
                "libro non porta con se' il perche' e' stato fatto cosi'."]
        else:
            ok, mancanti = scheda.valida()
            if not ok:
                esiti["Scheda libro di ispirazione"] = [
                    f"incompleta, mancano: {', '.join(mancanti)}"]
            ispirazione.salva(scheda, pacchetto.folder_path / "ISPIRAZIONE.json")
            (pacchetto.folder_path / "ISPIRAZIONE.txt").write_text(
                scheda.testo(), encoding="utf-8")
            out["ispirazione"] = str(pacchetto.folder_path / "ISPIRAZIONE.json")
        for avviso in esiti.get("Scheda libro di ispirazione", []):
            print(f"[assembla] ispirazione: {avviso}")

        pagine_reali = (book_output_manager.conta_pagine_pdf(pacchetto.pdf_dest)
                        if pacchetto.pdf_dest else None)
        if pacchetto.pdf_dest:
            esiti["Numerazione pagine"] = validators.valida_numerazione_pagine(pacchetto.pdf_dest)
            for avviso in esiti["Numerazione pagine"]:
                print(f"[assembla] numerazione: {avviso}")
            esiti["Parole spezzate a fine riga"] = validators.valida_sillabazione_pdf(
                pacchetto.pdf_dest, testo_sorgente=testo_completo)
            for avviso in esiti["Parole spezzate a fine riga"][:3]:
                print(f"[assembla] sillabazione: {avviso}")

        # --- REPORT di consegna (richiesta di Gael, 2026-08-10) ----------- #
        report_path = pacchetto.folder_path / "REPORT.md"
        report_path.write_text(
            book_report.genera_report(
                cfg, stato, risultato, pagine_reali,
                {
                    "PDF (da leggere)": pacchetto.pdf_dest,
                    "Copertina": pacchetto.cover_dest,
                    "Manoscritto Word": pacchetto.manuscript_dest,
                    "Metadati KDP": pacchetto.metadata_dest,
                },
                esiti,
            ),
            encoding="utf-8",
        )
        out["report"] = str(report_path)

        # --- Verdetto unico: pubblicabile o no ---------------------------- #
        verdetto = report_validazione.ReportValidazione(pagine_reali=pagine_reali)
        minimo = config.TARGET_PAGE_COUNT - config.TARGET_PAGE_COUNT_TOLERANCE
        if pagine_reali is None:
            # NON MISURATO NON E' A POSTO (2026-08-23). Prima la condizione era
            # `if pagine_reali and pagine_reali < minimo`: con `None` — cioe' quando il
            # PDF non si era potuto fare — il controllo spariva in silenzio e il libro
            # usciva `pubblicabile: true` senza che nessuno avesse contato una pagina.
            # E' il difetto originale del progetto (120 pagine dichiarate, 21 reali)
            # rientrato dalla finestra, in un ramo che nessuno guardava.
            verdetto.blocca(
                "Pagine reali NON CONTATE: il PDF non e' stato prodotto (serve Microsoft "
                "Word, lo pilota docx2pdf). Il conteggio pagine e' l'unico requisito KDP "
                "che questo pacchetto non puo' dimostrare, e la stima a "
                f"{config.WORDS_PER_PAGE_ESTIMATE} parole/pagina non lo sostituisce: sui "
                "tre libri veri ha sbagliato fino a 4,3 pagine, una volta dando per buono "
                "un libro da 113 pagine contro un minimo di 115."
            )
        elif pagine_reali < minimo:
            verdetto.blocca(f"Pagine reali {pagine_reali}, il minimo per il target e' {minimo}")
        if not cover_presente:
            # La cartella ora nasce anche senza immagine, quindi il "manca la copertina"
            # deve diventare una voce ESPLICITA del verdetto. Senza, un pacchetto senza
            # copertina uscirebbe `pubblicabile: true` — lo stesso errore di forma del
            # bug "pagine non contate" chiuso il 2026-08-23: un requisito che sparisce
            # perche' nessuno lo nomina.
            verdetto.blocca(
                "Copertina assente: il pacchetto ha manoscritto, prompt copertina e copy, "
                "ma non l'immagine. Genera il .png dal prompt in COPERTINA-PROMPT.md, poi: "
                f"python -m engine.kdp consegna {self.slug} --cover <file.png>"
            )
        for etichetta, voci in esiti.items():
            gravita = GRAVITA_ESITI.get(etichetta, "avviso")
            # "VERIFICA A MANO" = lo strumento non c'era, il controllo non e' girato.
            # Non e' un difetto del libro e non blocca, ma non e' nemmeno un avviso da
            # sfogliare: finisce in `verifiche_non_eseguite`, dove si vede che quel
            # controllo NON ha detto di si'.
            voci_vere = [v for v in voci if not v.startswith("VERIFICA A MANO")]
            voci_manuali = [v for v in voci if v.startswith("VERIFICA A MANO")]
            verdetto.aggiungi(etichetta, voci_vere, gravita)
            verdetto.aggiungi(etichetta, voci_manuali, "non_verificato")

        verdetto.salva(pacchetto.folder_path / "validazione.json")
        out["pubblicabile"] = verdetto.pubblicabile
        print(verdetto.riepilogo())
        print(f"[assembla] report di consegna: {report_path.name}")
        print(f"[assembla] pacchetto pronto: {pacchetto.folder_path}")
        if not verdetto.pubblicabile and not forza:
            raise RuntimeError(
                "Il pacchetto e' stato creato ma il libro NON e' pubblicabile cosi': "
                + "; ".join(verdetto.bloccanti)
            )
        return out

    def _metadata_kdp(self, cfg: dict, risultato) -> str:
        """Metadati pronti da incollare nella form di KDP.

        Se esiste il copy della Fase 5 (`copy_kdp`) include titolo finale, sottotitolo,
        descrizione, keyword e categorie — cioe' i campi che si compilano davvero al
        caricamento. Se non esiste (libro scritto senza passare dalla Fase 5, o progetto
        vecchio) resta il set minimo storico: mai un errore, mai campi finti."""
        copy = cfg.get("copy_kdp") or {}
        titolo_finale = copy.get("titolo_finale") or cfg["titolo"]

        righe = [
            f"Titolo: {titolo_finale}",
            f"Autore: {cfg.get('autore', 'Digital Empire')}",
        ]
        if copy.get("sottotitolo"):
            righe.append(f"Sottotitolo: {copy['sottotitolo']}")
        righe.append(f"Nicchia/keyword: {cfg.get('nicchia', '')}")

        if copy.get("descrizione"):
            righe.append("")
            righe.append("Descrizione (back cover):")
            righe.append(copy["descrizione"])

        if copy.get("keywords"):
            righe.append("")
            righe.append(f"Keyword KDP ({len(copy['keywords'])}):")
            righe.extend(f"  {k}" for k in copy["keywords"])

        if copy.get("categorie"):
            righe.append("")
            righe.append("Categorie:")
            righe.extend(f"  {c}" for c in copy["categorie"])

        # Campi presi dal piano del 2026-08-19: sono quelli che al caricamento su KDP si
        # compilano davvero e che finora mancavano, costringendo a inventarli sul momento.
        if copy.get("codici_bisac"):
            righe.append("")
            righe.append("Codici BISAC (KDP ne chiede fino a 3):")
            righe.extend(f"  {b}" for b in copy["codici_bisac"])

        if copy.get("bio_autore"):
            righe.append("")
            righe.append("Bio autore (campo 'Author Bio' su KDP):")
            righe.append(copy["bio_autore"])

        if copy.get("descrizione_html"):
            righe.append("")
            # Niente lineetta lunga nemmeno nelle etichette di questo file: e' il foglio da
            # cui si copia-incolla dentro KDP, e una lineetta di troppo si porta dietro
            # senza accorgersene.
            righe.append("Descrizione Amazon in HTML (da incollare cosi' com'e';")
            righe.append("KDP accetta <b> <i> <br> <p> <ul> <li> <h4>):")
            righe.append(copy["descrizione_html"])

        if copy.get("prezzo_suggerito_usd"):
            righe.append("")
            righe.append(f"Prezzo suggerito: ${copy['prezzo_suggerito_usd']} "
                         f"(royalty 60% sopra $9.99 per il cartaceo)")
            # Il numero scelto accanto al numero misurato: erano due dati che vivevano nello
            # stesso progetto senza mai incontrarsi.
            scheda = self.ispirazione()
            if scheda is not None and scheda.prezzo_medio:
                righe.append(f"  prezzo medio rilevato nella nicchia "
                             f"'{scheda.nicchia}': ${scheda.prezzo_medio:.2f} "
                             f"su {scheda.concorrenti_analizzati or '?'} concorrenti "
                             f"({scheda.rilevato_il or 'data non registrata'})")

        righe.extend([
            "",
            f"Parole: {risultato.word_count}",
            f"Pagine stimate: {risultato.estimated_pages}",
            f"Trim size: {config.TRIM_SIZE_INCHES[0]}x{config.TRIM_SIZE_INCHES[1]} in",
        ])
        return "\n".join(righe) + "\n"


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
