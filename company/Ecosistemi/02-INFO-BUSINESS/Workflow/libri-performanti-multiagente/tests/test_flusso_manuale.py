"""
Test del flusso "lo scrivo io" (2026-08-15) — l'attrezzatura che uso mentre scrivo un libro.

Raccoglie i test che sopravvivono all'archiviazione dell'automazione: nicchia persistente,
magazzino argomenti, estrazione del titolo, riassunto progressivo, metadati KDP, copertina
portata a norma. Tutti deterministici: **nessuno apre un browser o chiama un modello**, e
non e' una comodita' ma il senso stesso di questa suite — dopo la riorganizzazione, un test
che chiedesse la rete sarebbe il segno che qualcosa e' rientrato dalla finestra.

I casi non sono inventati: quasi ognuno riproduce un errore realmente avvenuto su questo
progetto ed e' li' per non farlo succedere di nuovo.

    python -m pytest tests/test_flusso_manuale.py -v
"""
from __future__ import annotations

import json
import sys
import types
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import book_project, copertina_kdp, kdp, magazzino, nicchia_attiva  # noqa: E402


# --------------------------------------------------------------------------- #
# Nicchia persistente — si sceglie UNA VOLTA
# --------------------------------------------------------------------------- #

@pytest.fixture
def stato_isolato(tmp_path, monkeypatch):
    """Ogni test lavora su un suo nicchia_attiva.json, mai su quello vero del catalogo."""
    monkeypatch.setattr(nicchia_attiva, "STATO_PATH", tmp_path / "nicchia_attiva.json")
    return tmp_path


def test_prima_scelta_permessa(stato_isolato):
    n = nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")
    assert n.keyword == "small town romance suspense"
    assert nicchia_attiva.carica().keyword == "small town romance suspense"


def test_seconda_scelta_rifiutata(stato_isolato):
    """Il bug: bastava rilanciare 'nicchia-scegli' per perdere il catalogo."""
    nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")
    nicchia_attiva.registra_libro("The Quiet Hours")

    with pytest.raises(nicchia_attiva.NicchiaGiaScelta, match="gia' una nicchia attiva"):
        nicchia_attiva.imposta("cozy mystery cats", 99.0, "molto meglio")

    n = nicchia_attiva.carica()
    assert n.keyword == "small town romance suspense"
    assert n.libri_pubblicati == ["The Quiet Hours"]


def test_cambio_rifiutato_senza_margine(stato_isolato):
    """Un vantaggio di pochi punti non ripaga il costo di abbandonare il catalogo."""
    nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")
    soglia = 77.7 + nicchia_attiva.MARGINE_PER_CAMBIARE

    with pytest.raises(nicchia_attiva.NicchiaGiaScelta, match="sotto la soglia"):
        nicchia_attiva.cambia("cozy mystery cats", soglia - 0.1, "di poco meglio")

    assert nicchia_attiva.carica().keyword == "small town romance suspense"


def test_cambio_accettato_col_margine_e_storia_conservata(stato_isolato):
    """Si cambia solo se e' NETTAMENTE migliore — e la nicchia lasciata non sparisce."""
    nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")
    nicchia_attiva.registra_libro("The Quiet Hours")
    nicchia_attiva.registra_libro("The Ninth Winter")

    nuova = nicchia_attiva.cambia("cozy mystery cats",
                                   77.7 + nicchia_attiva.MARGINE_PER_CAMBIARE,
                                   "nettamente meglio")

    assert nuova.keyword == "cozy mystery cats"
    assert nuova.libri_pubblicati == [], "il catalogo nuovo parte vuoto"
    assert len(nuova.storico) == 1
    lasciata = nuova.storico[0]
    assert lasciata["libri_pubblicati"] == ["The Quiet Hours", "The Ninth Winter"], (
        "i libri della nicchia precedente devono restare tracciati, altrimenti un cambio "
        "cancella la ragione per cui quel catalogo esisteva"
    )
    assert nicchia_attiva.carica().storico[0]["keyword"] == "small town romance suspense"


def test_cambia_senza_nicchia_equivale_a_scegliere(stato_isolato):
    n = nicchia_attiva.cambia("small town romance suspense", 70.0, "prima volta")
    assert n.keyword == "small town romance suspense"
    assert n.storico == []


def test_cli_nicchia_scegli_non_sovrascrive(stato_isolato, capsys, monkeypatch):
    """Il comando non deve nemmeno partire: niente ricerche, niente sovrascrittura."""
    nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")

    from engine import niche_finder

    def esplodi(*a, **k):
        raise AssertionError("non deve cercare nicchie: ce n'e' gia' una attiva")

    monkeypatch.setattr(niche_finder, "trova_nicchie", esplodi)

    rc = kdp.main(["nicchia-scegli", "--keywords", "cozy mystery cats"])

    assert rc == kdp.CONFIG_ERRATA
    assert "gia' una nicchia attiva" in capsys.readouterr().out
    assert nicchia_attiva.carica().keyword == "small town romance suspense"


# --------------------------------------------------------------------------- #
# Magazzino argomenti — il "flusso atemporale"
# --------------------------------------------------------------------------- #

@pytest.fixture
def magazzino_isolato(tmp_path, monkeypatch):
    monkeypatch.setattr(magazzino, "MAGAZZINO_PATH", tmp_path / "magazzino.json")
    return tmp_path


def _argomento_buono(titolo="The Lighthouse Letter") -> dict:
    return {
        "nicchia": "small town romance suspense",
        "titolo_lavoro": titolo,
        "premessa": "Una donna torna nella cittadina dove e' cresciuta e riapre un caso.",
        "dati_amazon": {"punteggio": 77.4, "recensioni_mediana": 324, "prezzo_medio": 10.77},
    }


def test_argomento_valido_entra(magazzino_isolato):
    inseriti, problemi = magazzino.aggiungi([_argomento_buono()])
    assert len(inseriti) == 1 and problemi == []
    assert magazzino.carica()[0].stato == magazzino.LIBERO


def test_argomento_senza_numeri_non_entra(magazzino_isolato):
    """Un argomento entra solo con dati veri: 'mi sembra una buona nicchia' non basta."""
    a = _argomento_buono()
    a["dati_amazon"] = {}
    inseriti, problemi = magazzino.aggiungi([a])
    assert inseriti == []
    assert any("numeri veri" in p for p in problemi)


def test_diario_non_entra_nel_magazzino(magazzino_isolato):
    """story_validator applicato all'ingresso: un planner non deve diventare un libro."""
    a = _argomento_buono("My Daily Gratitude Planner")
    a["nicchia"] = "gratitude journal planner"
    a["premessa"] = "Un diario guidato con tracker delle abitudini."
    inseriti, problemi = magazzino.aggiungi([a])
    assert inseriti == []
    assert any("non e' una storia" in p for p in problemi)


def test_duplicato_non_entra_due_volte(magazzino_isolato):
    magazzino.aggiungi([_argomento_buono()])
    inseriti, problemi = magazzino.aggiungi([_argomento_buono()])
    assert inseriti == []
    assert any("gia' presente" in p for p in problemi)


def test_prendi_marca_in_uso_e_non_ripete(magazzino_isolato):
    magazzino.aggiungi([_argomento_buono("Primo"), _argomento_buono("Secondo")])

    a1 = magazzino.prendi()
    a2 = magazzino.prendi()
    a3 = magazzino.prendi()

    assert a1.titolo_lavoro == "Primo" and a2.titolo_lavoro == "Secondo"
    assert a3 is None, "esaurito il magazzino deve dirlo, non riproporre un argomento"
    assert all(a.stato == magazzino.IN_USO for a in magazzino.carica())


def test_argomento_si_collega_al_libro_e_si_chiude(magazzino_isolato):
    magazzino.aggiungi([_argomento_buono()])
    magazzino.prendi()
    magazzino.collega_libro("The Lighthouse Letter", "the-lighthouse-letter")
    magazzino.segna_fatto("the-lighthouse-letter")

    a = magazzino.carica()[0]
    assert a.slug_libro == "the-lighthouse-letter"
    assert a.stato == magazzino.FATTO
    assert magazzino.conteggi()["fatto"] == 1


def test_magazzino_corrotto_non_esplode(magazzino_isolato):
    """Un file rovinato deve dare 'vuoto', non far cadere tutto il flusso."""
    magazzino.MAGAZZINO_PATH.write_text("{ non json", encoding="utf-8")
    assert magazzino.carica() == []


# --------------------------------------------------------------------------- #
# Titolo — mai un placeholder in copertina
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("testo, atteso", [
    ("TITLE: The Quiet Hours\nACT1: ...", "The Quiet Hours"),
    ("**TITLE:** The Quiet Hours", "The Quiet Hours"),
    ("# TITLE: The Quiet Hours", "The Quiet Hours"),
    ('TITLE: "The Quiet Hours"', "The Quiet Hours"),
    ("titolo del libro\ntitle: the quiet hours", "the quiet hours"),
])
def test_estrae_il_titolo_anche_se_decorato(testo, atteso):
    assert kdp.estrai_titolo(testo) == atteso


@pytest.mark.parametrize("testo", ["", "CHARACTERS: Anna\nACT1: x", "TITLE:", "TITLE senza due punti"])
def test_nessun_titolo_e_None_non_un_placeholder(testo):
    """Deve dire 'non l'ho trovato', non restituire qualcosa di plausibile."""
    assert kdp.estrai_titolo(testo) is None


# --------------------------------------------------------------------------- #
# Riassunto progressivo e metadati KDP
# --------------------------------------------------------------------------- #

def test_progetto_nuovo_non_ha_riassunto(tmp_path, monkeypatch):
    """Bug reale (2026-08-15): `crea()` scrive in riassunti.md un'intestazione e un commento
    di istruzioni. Leggere il file grezzo li restituiva come storia accaduta finora."""
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Riassunto Vuoto", "cozy mystery",
                                              capitoli=3, parole_per_capitolo=100)

    modello = progetto.riassunti_path.read_text(encoding="utf-8")
    assert "## Fili aperti" in modello and "### cap_01" in modello,         "il modello deve gia' avere la struttura che gate_blocco legge"
    assert progetto.riassunto_progressivo() == "",         "istruzioni e intestazioni non devono passare per storia accaduta"


def test_riassunto_progressivo_conserva_il_contenuto_vero(tmp_path, monkeypatch):
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Riassunto Pieno", "cozy mystery",
                                              capitoli=3, parole_per_capitolo=100)
    progetto.riassunti_path.write_text(
        "# Riassunti progressivi — Riassunto Pieno\n\n"
        "<!-- commento di istruzioni -->\n"
        "Anna trova un indizio. Sam apre l'indagine.\n",
        encoding="utf-8")
    assert progetto.riassunto_progressivo() == "Anna trova un indizio. Sam apre l'indagine."


def test_metadata_kdp_include_il_copy(tmp_path, monkeypatch):
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Con Copy", "cozy mystery",
                                              capitoli=1, parole_per_capitolo=100)
    progetto.salva_copy({
        "titolo_finale": "Murder at Maple Bakery",
        "sottotitolo": "A Small Town Cozy Mystery",
        "descrizione": "Anna torna a casa e trova un cadavere.",
        "keywords": ["cozy mystery", "amateur sleuth"],
        "categorie": ["Mystery"],
    })
    risultato = types.SimpleNamespace(word_count=35000, estimated_pages=116.7)

    testo = progetto._metadata_kdp(progetto._config(), risultato)
    assert "Murder at Maple Bakery" in testo
    assert "amateur sleuth" in testo
    assert "Anna torna a casa" in testo


def test_metadata_kdp_senza_copy_resta_il_minimo(tmp_path, monkeypatch):
    """Progetti vecchi (o libri senza copy) non devono rompersi."""
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Senza Copy", "cozy mystery",
                                              capitoli=1, parole_per_capitolo=100)
    risultato = types.SimpleNamespace(word_count=35000, estimated_pages=116.7)

    testo = progetto._metadata_kdp(progetto._config(), risultato)
    assert "Senza Copy" in testo
    assert "Keyword KDP" not in testo


# --------------------------------------------------------------------------- #
# Copertina arrivata da fuori
# --------------------------------------------------------------------------- #

def _png(path: Path, larghezza: int, altezza: int) -> Path:
    from PIL import Image
    Image.new("RGB", (larghezza, altezza), (40, 30, 60)).save(path)
    return path


def test_copertina_quadrata_viene_bocciata(tmp_path):
    """Caso reale: la prima copertina di The Quiet Hours era 1024x1024, inutilizzabile."""
    esito = copertina_kdp.verifica_copertina_kdp(_png(tmp_path / "q.png", 1024, 1024))
    assert not esito["ok"]
    assert any("proporzioni" in p for p in esito["problemi"])


def test_copertina_portata_a_norma_kdp(tmp_path):
    esito = copertina_kdp.prepara_copertina(_png(tmp_path / "q.png", 1024, 1024),
                                             titolo="Silence In Cedar Hollow")
    assert esito["verifica"]["ok"]
    assert (esito["verifica"]["larghezza"], esito["verifica"]["altezza"]) == (1800, 2700)


def test_titolo_gia_in_copertina_non_viene_riscritto(tmp_path):
    """Dal 2026-08-15 il titolo lo disegna il modello di immagini: riscriverlo sopra
    lo farebbe comparire due volte."""
    con = copertina_kdp.prepara_copertina(_png(tmp_path / "a.png", 1024, 1024),
                                           titolo="Titolo", titolo_gia_in_copertina=True)
    senza = copertina_kdp.prepara_copertina(_png(tmp_path / "b.png", 1024, 1024),
                                             titolo="Titolo", titolo_gia_in_copertina=False)

    assert "_finale" not in con["path"].name, "non deve scrivere il titolo sopra"
    assert "_finale" in senza["path"].name, "la rete di sicurezza deve poter intervenire"
    assert con["path"].stat().st_size != senza["path"].stat().st_size


def test_copertina_inesistente_errore_chiaro(tmp_path):
    with pytest.raises(FileNotFoundError, match="Copertina non trovata"):
        copertina_kdp.prepara_copertina(tmp_path / "non_esiste.png", titolo="X")


# --------------------------------------------------------------------------- #
# Pacchetto finale: una cartella per libro, e mai distruggere le sorgenti
# --------------------------------------------------------------------------- #

@pytest.fixture
def pronti_isolati(tmp_path, monkeypatch):
    from engine import book_output_manager, config
    dir_pronti = tmp_path / "libri_pronti"
    dir_pronti.mkdir()
    monkeypatch.setattr(config, "LIBRI_PRONTI_DIR", dir_pronti)
    # Il PDF richiede Word installato: qui non serve, si sta verificando il montaggio.
    monkeypatch.setattr(book_output_manager, "converti_in_pdf", lambda *a, **k: None)
    return dir_pronti


def _pacchetto(manoscritto, copertina, sostituisci):
    from engine import book_output_manager
    return book_output_manager.create_book_package(
        book_title="Libro Prova", manuscript_path=manoscritto, cover_path=copertina,
        kdp_metadata_text="metadati", word_count=1000, page_count=3.3,
        sostituisci=sostituisci)


def test_riconsegna_stesso_libro_non_crea_una_seconda_cartella(pronti_isolati, tmp_path):
    """Il 2026-08-17 The Ninth Winter aveva due cartelle — quella del giro bloccato e
    quella buona — e non si capiva piu' quale caricare su KDP."""
    ms = tmp_path / "Libro.docx"; ms.write_text("testo")
    cov = _png(tmp_path / "cover.png", 1800, 2700)

    primo = _pacchetto(ms, cov, sostituisci=True)
    secondo = _pacchetto(ms, cov, sostituisci=True)

    assert primo.folder_path == secondo.folder_path
    assert [p.name for p in pronti_isolati.iterdir()] == ["Libro_Prova"]


def test_libro_diverso_stesso_titolo_non_sovrascrive(pronti_isolati, tmp_path):
    """Senza `sostituisci` la cartella esistente e' intoccabile: potrebbe essere
    il libro di un altro."""
    ms = tmp_path / "Libro.docx"; ms.write_text("testo")
    cov = _png(tmp_path / "cover.png", 1800, 2700)

    primo = _pacchetto(ms, cov, sostituisci=False)
    secondo = _pacchetto(ms, cov, sostituisci=False)

    assert primo.folder_path != secondo.folder_path
    assert primo.manuscript_dest.exists(), "il primo pacchetto non va distrutto"


def test_copertina_dentro_il_pacchetto_sopravvive_alla_riconsegna(pronti_isolati, tmp_path):
    """Regressione 2026-08-18: rilanciare la consegna passando la copertina che sta gia'
    nel pacchetto la cancellava prima di copiarla. Cartella svuotata, copertina persa —
    recuperata solo perche' era su git. E' l'uso piu' naturale che ci sia."""
    ms = tmp_path / "Libro.docx"; ms.write_text("testo")
    primo = _pacchetto(ms, _png(tmp_path / "cover.png", 1800, 2700), sostituisci=True)

    # Adesso si riconsegna indicando le copie DENTRO il pacchetto appena creato.
    secondo = _pacchetto(primo.manuscript_dest, primo.cover_dest, sostituisci=True)

    assert secondo.cover_dest.exists(), "la copertina e' stata distrutta dalla sostituzione"
    assert secondo.cover_dest.stat().st_size > 0
    assert secondo.manuscript_dest.read_text() == "testo"


# --------------------------------------------------------------------------- #
# Lineette lunghe: regola di Gael 2026-08-18, blocca la consegna
# --------------------------------------------------------------------------- #

def test_lineetta_lunga_viene_trovata():
    from engine import validators
    for segno in ("\u2014", "\u2013", " -- "):
        esito = validators.valida_lineette(f"Rebecca si volto{segno}non c'era nessuno.")
        assert esito, f"la lineetta {segno!r} deve essere trovata"


def test_trattino_di_parola_composta_non_e_una_lineetta():
    """In inglese 'twenty-nine' e 'hand-lettered' sono ortografia: toglierli produrrebbe
    testo sgrammaticato. Se ne occupa valida_trattini, che segnala e non blocca."""
    from engine import validators
    testo = "She had counted twenty-nine days and read the hand-lettered sign."
    assert validators.valida_lineette(testo) == []


def test_riga_di_separazione_non_e_una_lineetta():
    from engine import validators
    assert validators.valida_lineette("---") == []


def test_lineette_contate_per_riga():
    from engine import validators
    esito = validators.valida_lineette("uno \u2014 due \u2014 tre\nquattro, cinque")
    assert len(esito) == 1, "una sola riga contiene lineette"
    assert "2 lineetta" in esito[0]


def test_lineetta_dentro_le_virgolette_e_permessa():
    """Nel parlato la lineetta segna la parola tagliata: chi interrompe e chi si corregge
    da solo. Non e' scrittura automatica, e' come si trascrive una voce (Gael, 2026-08-18)."""
    from engine import validators
    assert validators.valida_lineette('"There\'s Efrain\'s boy\'s wife. She\'d be \u2014 "') == []
    assert validators.valida_lineette('"No. Stay. I\'ll \u2014 it\'ll be nothing."') == []


def test_lineetta_nella_narrazione_blocca_anche_accanto_a_un_dialogo():
    """Il caso insidioso: riga mista. La lineetta sta FUORI dalle virgolette."""
    from engine import validators
    riga = 'And Sarah had said \u2014 and she was certain of it \u2014 "Do you think he knows?"'
    esito = validators.valida_lineette(riga)
    assert esito and "2 lineetta" in esito[0]


# --------------------------------------------------------------------------- #
# Capitolo interrotto a meta'
# --------------------------------------------------------------------------- #

def test_capitolo_finito_non_viene_segnalato():
    from engine import validators
    assert validators.valida_troncamento("Rebecca stood in the yard.") == []
    assert validators.valida_troncamento('"Then ask it badly."') == []
    assert validators.valida_troncamento("*twenty-seven in the spring.*") == []


def test_capitolo_interrotto_viene_preso():
    from engine import validators
    assert validators.valida_troncamento("She closed the clipboard, put it on")
    assert validators.valida_troncamento("It was cold, and")
    assert validators.valida_troncamento("He said,")


def test_parole_che_finiscono_come_una_congiunzione_non_ingannano():
    """Il \b nel pattern e' obbligatorio: senza, il ramo '(the)$' aggancia la fine di
    'breathe' e '(an)$' quella di 'woman'. Stesso genere di falso positivo dei trattini
    di 'twenty-nine' e dell'OCR della copertina."""
    from engine import validators
    assert validators.valida_troncamento("She let out a long breathe.") == []
    assert validators.valida_troncamento("It was an ordinary woman.") == []


def test_troncamento_non_usa_le_virgolette_bilanciate():
    """L'euristica ovvia (virgolette dispari = troncato) e' sbagliata sulla narrativa: una
    battuta che prosegue per due paragrafi le apre nel primo e le chiude nel secondo."""
    from engine import validators
    battuta_su_due_paragrafi = '"I told her on Thursday.\n\n"And she wrote it down."'
    assert validators.valida_troncamento(battuta_su_due_paragrafi) == []


# --------------------------------------------------------------------------- #
# Scheda di ispirazione: numeri veri o niente
# --------------------------------------------------------------------------- #

def test_scheda_senza_numeri_amazon_non_e_valida():
    """Una scheda con numeri inventati e' peggio di nessuna scheda: sembra ricerca e non
    lo e'. Stessa regola di magazzino.valida_argomento()."""
    from engine.ispirazione import Ispirazione
    solo_testo = Ispirazione(
        nicchia="amish suspense", genere="suspense", lettore_tipo="donne 35-65",
        temi_chiave=["lutto"], stile="terza persona", tono="trattenuto",
        come_ci_distinguiamo="finale che non assolve",
    )
    ok, mancanti = solo_testo.valida()
    assert not ok
    assert any("recensioni_mediana" in m for m in mancanti)
    assert any("prezzo_medio" in m for m in mancanti)


def test_scheda_completa_e_valida():
    from engine.ispirazione import Ispirazione
    piena = Ispirazione(
        nicchia="amish suspense", genere="suspense", lettore_tipo="donne 35-65",
        temi_chiave=["lutto"], stile="terza persona", tono="trattenuto",
        come_ci_distinguiamo="finale che non assolve",
        recensioni_mediana=180.0, prezzo_medio=5.95, rilevato_il="2026-08-13",
    )
    assert piena.valida() == (True, [])


def test_numeri_presi_per_copia_dalla_ricerca():
    """I numeri veri entrano per copia, non ribattuti a mano: e' il modo piu' comune in cui
    un numero vero diventa un numero sbagliato."""
    from engine.ispirazione import da_ricerca_nicchia
    voce = {"keyword": "amish romance suspense", "n_risultati": 16,
            "recensioni_mediana": 180.0, "recensioni_min": 14, "prezzo_medio": 5.95,
            "rating_medio": 4.5, "concorrenti_deboli": 6, "punteggio": 73.1}
    campi = da_ricerca_nicchia(voce)
    assert campi["nicchia"] == "amish romance suspense"
    assert campi["recensioni_mediana"] == 180.0
    assert campi["concorrenti_deboli"] == 6


def test_scheda_va_e_torna_dal_file(tmp_path):
    from engine import ispirazione
    originale = ispirazione.Ispirazione(
        nicchia="cozy mystery", recensioni_mediana=386, prezzo_medio=8.99,
        temi_chiave=["gatti", "paese piccolo"], rilevato_il="2026-08-07")
    percorso = ispirazione.salva(originale, tmp_path / "ispirazione.json")
    riletta = ispirazione.carica(percorso)
    assert riletta == originale, "il campo _nota non deve rientrare nella dataclass"


# --------------------------------------------------------------------------- #
# Gate di blocco (2026-08-19): fermare i difetti al capitolo 8, non al 24
# --------------------------------------------------------------------------- #

@pytest.fixture
def libro_finto(tmp_path, monkeypatch):
    """Crea un progetto e ci mette dentro capitoli di lunghezza scelta."""
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)

    def costruisci(parole_per_capitolo, quanti=8, riassunti=None, lineette=False,
                   tronca=False):
        p = book_project.BookProject.crea("Libro Gate", "cozy mystery")
        for n in range(1, quanti + 1):
            corpo = " ".join(["parola"] * (parole_per_capitolo - 3))
            if lineette and n == 1:
                corpo = "Lei si volto\u2014non c'era nessuno. " + corpo
            fine = "" if tronca and n == quanti else "."
            p.path_capitolo(n).write_text(f"# Cap {n}\n\n{corpo}{fine}\n", encoding="utf-8")
        if riassunti is not None:
            p.riassunti_path.write_text(riassunti, encoding="utf-8")
        else:
            sezioni = "\n".join(f"### cap_{n:02d}\n- Succede: cose\n" for n in range(1, quanti + 1))
            p.riassunti_path.write_text(
                f"# Riassunti\n\n## Fili aperti\n\n## Capitoli\n\n{sezioni}", encoding="utf-8")
        return p
    return costruisci


def _motivi(esito):
    return " | ".join(esito.blocchi)


def test_gate_ferma_i_capitoli_troppo_corti(libro_finto):
    """IL controllo che giustifica tutto il gate. Stato reale del 2026-08-13: 8 capitoli a
    1.041 parole, proiezione 25.000 su un minimo di 36.800. Il difetto e' stato scoperto al
    capitolo 24 ed e' costato quattro riprese piu' scene aggiunte in coda."""
    from engine import gate_blocco
    esito = gate_blocco.controlla(libro_finto(1041))
    assert not esito.si_prosegue
    assert "sotto il minimo" in _motivi(esito)
    assert esito.proiezione < 26000, "la proiezione deve dire dove ATTERRA il libro"


def test_gate_lascia_passare_la_lunghezza_giusta(libro_finto):
    from engine import gate_blocco
    esito = gate_blocco.controlla(libro_finto(1600))
    assert esito.si_prosegue, _motivi(esito)
    assert esito.proiezione == 1600 * 24


def test_gate_prende_le_lineette_al_capitolo_8(libro_finto):
    """A fine libro sono state 193 righe da riscrivere a mano. Qui sono una."""
    from engine import gate_blocco
    esito = gate_blocco.controlla(libro_finto(1600, lineette=True))
    assert not esito.si_prosegue
    assert "lineette" in _motivi(esito)


def test_gate_prende_il_capitolo_troncato(libro_finto):
    from engine import gate_blocco
    esito = gate_blocco.controlla(libro_finto(1600, tronca=True))
    assert not esito.si_prosegue
    assert "cap_08" in _motivi(esito)


def test_gate_pretende_i_riassunti_aggiornati(libro_finto):
    """Su The Ninth Winter riassunti.md non fu mai aggiornato, e il capitolo 9 sarebbe stato
    scritto alla cieca: nessun controllo automatico se ne accorgeva."""
    from engine import gate_blocco
    esito = gate_blocco.controlla(libro_finto(1600, riassunti="# Riassunti\n\n## Capitoli\n"))
    assert not esito.si_prosegue
    assert "riassunti.md non copre" in _motivi(esito)


def test_gate_ferma_un_filo_aperto_da_troppo(libro_finto):
    """Efrain: lasciato in sospeso al cap. 15, chiuso con una scena-toppa al 24."""
    from engine import gate_blocco
    sezioni = "\n".join(f"### cap_{n:02d}\n- Succede: cose\n" for n in range(1, 23))
    riassunti = ("# Riassunti\n\n## Fili aperti\n\n"
                 "- [cap 15] Efrain ha chiesto di non essere ricontattato prima di aprile\n\n"
                 f"## Capitoli\n\n{sezioni}")
    esito = gate_blocco.controlla(libro_finto(1600, quanti=22, riassunti=riassunti))
    assert not esito.si_prosegue
    assert "filo aperto dal capitolo 15" in _motivi(esito)


def test_filo_aperto_da_poco_non_blocca(libro_finto):
    from engine import gate_blocco
    sezioni = "\n".join(f"### cap_{n:02d}\n- Succede: cose\n" for n in range(1, 19))
    riassunti = ("# Riassunti\n\n## Fili aperti\n\n- [cap 15] Efrain aspetta aprile\n\n"
                 f"## Capitoli\n\n{sezioni}")
    esito = gate_blocco.controlla(libro_finto(1600, quanti=18, riassunti=riassunti))
    assert esito.si_prosegue, _motivi(esito)


def test_bersaglio_al_centro_della_finestra():
    """Mirare al minimo e' quello che e' costato quattro riprese su The Ninth Winter."""
    from engine import book_project as bp, config
    bersaglio = bp.DEFAULT_WORDS_PER_CHAPTER * bp.DEFAULT_TOTAL_CHAPTERS
    centro = (config.TARGET_WORD_COUNT_MIN + config.TARGET_WORD_COUNT_MAX) / 2
    assert abs(bersaglio - centro) <= 50, f"bersaglio {bersaglio}, centro {centro}"
    assert bersaglio - config.TARGET_WORD_COUNT_MIN >= 1500, "serve margine sotto"
    assert config.TARGET_WORD_COUNT_MAX - bersaglio >= 1500, "serve margine sopra"
