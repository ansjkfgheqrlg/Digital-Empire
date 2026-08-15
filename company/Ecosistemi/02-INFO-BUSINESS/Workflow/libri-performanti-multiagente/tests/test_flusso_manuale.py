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

    assert "Riassunti progressivi" in progetto.riassunti_path.read_text(encoding="utf-8")
    assert progetto.riassunto_progressivo() == ""


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
