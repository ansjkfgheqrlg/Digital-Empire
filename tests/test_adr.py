# -*- coding: utf-8 -*-
"""Il coniatore di numeri ADR (scripts/adr.py).

PERCHE' ESISTE. Il numero di un ADR e' progressivo per forza, e "progressivo" e
"scelto a mano" insieme sono una collisione garantita. Il piano LANCI si e' visto
scippare il proprio numero tre volte di fila (022, 023, 024) da sessioni parallele
che leggevano la stessa cartella nello stesso momento, e la cartella delle decisioni
porta gia' due numeri usati due volte (ADR-012, ADR-016).
"""
import os
import sys

import pytest

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "scripts"))

import adr  # noqa: E402


@pytest.fixture
def cartella_finta(tmp_path, monkeypatch):
    """Una cartella decisions/ isolata, senza storia git."""
    d = tmp_path / "decisions"
    d.mkdir()
    monkeypatch.setattr(adr, "CARTELLA", str(d))
    monkeypatch.setattr(adr, "_numeri_nella_storia", lambda: set())
    return d


def _scrivi(d, nome):
    (d / nome).write_text("# stub\n", encoding="utf-8")


def test_il_prossimo_numero_segue_il_massimo_occupato(cartella_finta):
    for n in (1, 2, 24):
        _scrivi(cartella_finta, "ADR-%03d-cosa.md" % n)
    assert adr.prossimo_numero() == 25


def test_un_numero_vivo_solo_nella_storia_git_resta_occupato(cartella_finta, monkeypatch):
    """IL difetto vero: un numero usato da una sessione parallela e poi rinominato
    sparisce dalla cartella e resta preso. Guardare solo il disco lo riassegna, che
    e' il modo piu' silenzioso di perdere una decisione."""
    _scrivi(cartella_finta, "ADR-001-cosa.md")
    monkeypatch.setattr(adr, "_numeri_nella_storia", lambda: {1, 2, 3, 40})
    assert adr.prossimo_numero() == 41


def test_coniare_occupa_il_numero_creando_il_file(cartella_finta):
    codice = adr.conia("ecosistema-lanci", "Nasce LANCI")
    assert codice == "ADR-001"
    assert (cartella_finta / "ADR-001-ecosistema-lanci.md").exists()
    # il secondo conio non puo' ricevere lo stesso numero
    assert adr.conia("altra-cosa", "Altra") == "ADR-002"


def test_un_file_gia_presente_non_viene_sovrascritto(cartella_finta):
    """O_EXCL e' il punto di tutta la funzione: se il numero c'e' gia', si passa al
    successivo invece di scrivere sopra una decisione mai letta."""
    _scrivi(cartella_finta, "ADR-001-decisione-di-un-altro.md")
    codice = adr.conia("ecosistema-lanci", "Nasce LANCI")
    assert codice == "ADR-002"
    assert (cartella_finta / "ADR-001-decisione-di-un-altro.md").read_text(
        encoding="utf-8") == "# stub\n"


def test_lo_stato_predefinito_e_proposta_non_attiva(cartella_finta):
    """Un ADR coniato non e' un ADR approvato. ADR-009 dice che un ecosistema nuovo
    lo decide Max: il conio prenota il numero, non firma la decisione."""
    adr.conia("ecosistema-lanci", "Nasce LANCI")
    testo = (cartella_finta / "ADR-001-ecosistema-lanci.md").read_text(encoding="utf-8")
    assert "**Stato:** PROPOSTA" in testo


def test_verifica_segnala_i_duplicati_e_esce_1(cartella_finta, capsys):
    _scrivi(cartella_finta, "ADR-012-orchestration-layer.md")
    _scrivi(cartella_finta, "ADR-012-ponte-memory-wiki.md")
    assert adr.verifica() == 1
    assert "DUPLICATI" in capsys.readouterr().out


def test_verifica_esce_0_su_un_registro_sano(cartella_finta):
    _scrivi(cartella_finta, "ADR-001-una.md")
    _scrivi(cartella_finta, "ADR-002-due.md")
    assert adr.verifica() == 0


def test_uno_slug_sporco_viene_rifiutato(cartella_finta):
    for cattivo in ("Ecosistema Lanci", "ecosistema_lanci", "../fuori", ""):
        with pytest.raises(SystemExit):
            adr.conia(cattivo, "Titolo")
