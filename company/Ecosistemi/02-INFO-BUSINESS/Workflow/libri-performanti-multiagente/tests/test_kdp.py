"""
Suite di test del workflow KDP (RNF-07 del piano del 2026-08-10).

Girano senza dipendenze opzionali (niente Word, Tesseract, pdfplumber) e senza rete: sono
pensati per essere lanciati sempre, non solo quando l'ambiente e' completo.

I casi non sono inventati: quasi tutti riproducono un falso positivo o un bug REALE trovato
sul primo libro, cosi' se qualcuno "semplifica" un validatore il test lo riprende.

    python -m pytest tests/ -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import report_validazione, validators  # noqa: E402
from engine.book_project import slugify  # noqa: E402


# --------------------------------------------------------------------------- #
# Trattini
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("testo", [
    "She was twenty-nine years old.",       # numero composto inglese: obbligatorio
    "Item forty-one on the list.",
    "A check-up at the dentist.",           # phrasal noun
    "The second-cheapest bottle.",
    "A self-made man.",
    "An accidental break-in.",
    "- primo punto di un elenco",
    "# Titolo markdown",
    "---",
    "Data 2024-01-01 e 12-03-2024.",
    "Link https://esempio.com/a-b-c ok.",
    "Frase del tutto normale.",
])
def test_trattini_leciti_non_segnalati(testo):
    """Questi trattini sono corretti: segnalarli farebbe riscrivere testo giusto.
    Caso reale: la prima versione bloccava 'twenty-nine' e 'M-A-R-S-H'."""
    assert validators.valida_trattini(testo) == []


@pytest.mark.parametrize("testo,attesi", [
    ("La parola impagina-zione spezzata.", 1),
    ("Testo con qualcosa-strano dentro.", 1),
    ("Due casi: aaa-bbb e ccc-ddd.", 2),
])
def test_trattini_sospetti_segnalati(testo, attesi):
    assert len(validators.valida_trattini(testo)) == attesi


def test_trattini_riporta_riga_e_contesto():
    errori = validators.valida_trattini("prima riga\nqui c'e' aaa-bbb dentro")
    assert errori and "riga 2" in errori[0] and "aaa-bbb" in errori[0]


# --------------------------------------------------------------------------- #
# Report di validazione
# --------------------------------------------------------------------------- #

def test_report_nuovo_e_pubblicabile():
    assert report_validazione.ReportValidazione().pubblicabile is True


def test_solo_i_bloccanti_impediscono_la_pubblicazione():
    r = report_validazione.ReportValidazione()
    r.avvisa("un trattino da guardare")
    r.errore("un difetto minore")
    assert r.pubblicabile is True, "avvisi ed errori non devono bloccare la pubblicazione"
    r.blocca("copertina senza titolo")
    assert r.pubblicabile is False


def test_aggiungi_prefissa_l_etichetta():
    r = report_validazione.ReportValidazione()
    r.aggiungi("Trattini", ["riga 3: aaa-bbb"], gravita="avviso")
    assert r.avvisi == ["[Trattini] riga 3: aaa-bbb"]


def test_riepilogo_dice_lo_stato():
    r = report_validazione.ReportValidazione()
    assert "PUBBLICABILE" in r.riepilogo()
    r.blocca("pagine sotto il minimo")
    testo = r.riepilogo()
    assert "NON PUBBLICABILE" in testo and "pagine sotto il minimo" in testo


def test_salvataggio_su_file(tmp_path):
    r = report_validazione.ReportValidazione()
    r.blocca("problema")
    destinazione = r.salva(tmp_path / "sotto" / "validazione.json")
    assert destinazione.exists()
    assert '"pubblicabile": false' in destinazione.read_text(encoding="utf-8")


# --------------------------------------------------------------------------- #
# Validatori senza dipendenze installate
# --------------------------------------------------------------------------- #

def test_file_mancante_non_solleva_ma_segnala(tmp_path):
    """Un validatore non deve mai far crollare il workflow per un file assente:
    deve dirlo e lasciare decidere a chi chiama."""
    inesistente = tmp_path / "non_esiste.pdf"
    assert validators.valida_numerazione_pagine(inesistente)
    assert validators.valida_copertina_testo(tmp_path / "no.png")


# --------------------------------------------------------------------------- #
# Slug dei progetti
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("titolo,atteso", [
    ("The Quiet Hours", "the-quiet-hours"),
    ("Titolo: con  punteggiatura!", "titolo-con-punteggiatura"),
    ("", "libro"),
])
def test_slugify(titolo, atteso):
    assert slugify(titolo) == atteso


def test_slug_non_supera_i_60_caratteri():
    assert len(slugify("parola " * 40)) <= 60


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def test_cli_senza_keyword_esce_con_parametri_errati():
    from engine import kdp
    assert kdp.main(["nicchie"]) == kdp.CONFIG_ERRATA


def test_cli_stato_di_uno_slug_inesistente():
    from engine import kdp
    assert kdp.main(["stato", "slug-che-non-esiste-12345"]) == kdp.CONFIG_ERRATA


def test_cli_consegna_con_copertina_mancante():
    from engine import kdp
    assert kdp.main(["consegna", "qualsiasi", "--cover", "/percorso/inesistente.png"]) \
        == kdp.CONFIG_ERRATA


def test_i_quattro_exit_code_sono_distinti():
    from engine import kdp
    codici = {kdp.OK, kdp.VALIDAZIONE_FALLITA, kdp.CONFIG_ERRATA, kdp.ERRORE_SISTEMA}
    assert codici == {0, 1, 2, 3}
