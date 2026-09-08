# -*- coding: utf-8 -*-
"""Lo spaccatore di task grandi in micro-task (scripts/frantuma.py).

PERCHE' ESISTE. Max ha chiesto una funzione che spacchi una task grande (es.
TASK-LANCI-BUILD-W3) in micro-task eseguibili in chat separate, in parallelo.
Due rischi distinti: due sessioni coniano la stessa micro-task insieme (stesso
schema anti-collisione di adr.py/checkpoint.py), e due micro-task diverse
toccano lo stesso file (collisione di merge silenziosa) -- questo secondo
rischio e' quello nuovo rispetto ad ADR e checkpoint, e verifica_sovrapposizioni
esiste solo per quello.
"""
import os
import sys

import pytest

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "scripts"))

import frantuma  # noqa: E402


@pytest.fixture
def base_finta(tmp_path, monkeypatch):
    monkeypatch.setattr(frantuma, "CARTELLA_BASE", str(tmp_path))
    return tmp_path


def test_numerazione_e_per_padre_non_globale(base_finta):
    """Due task grandi diverse partono ognuna da MT-01: la numerazione non e'
    un contatore unico, altrimenti il numero smetterebbe di dire 'primo pezzo
    di QUESTA task' e diventerebbe un ID globale senza significato."""
    frantuma.conia("TASK-A", "primo", "Primo pezzo di A", onda=1)
    codice_b = frantuma.conia("TASK-B", "primo", "Primo pezzo di B", onda=1)
    assert codice_b == "MT-01"


def test_coniare_occupa_il_numero_creando_il_file(base_finta):
    codice = frantuma.conia("TASK-LANCI-BUILD-W3", "s0-incasso", "Giorno zero", onda=1)
    assert codice == "MT-01"
    assert (base_finta / "TASK-LANCI-BUILD-W3" / "MT-01-s0-incasso.md").exists()
    assert frantuma.conia("TASK-LANCI-BUILD-W3", "seconda", "Seconda", onda=1) == "MT-02"


def test_un_file_gia_presente_non_viene_sovrascritto(base_finta):
    frantuma.conia("TASK-A", "prima", "Prima", onda=1)
    prima = (base_finta / "TASK-A" / "MT-01-prima.md").read_text(encoding="utf-8")
    # forzo una collisione manuale: qualcuno ha gia' scritto MT-02
    (base_finta / "TASK-A" / "MT-02-altro.md").write_text("# stub\n", encoding="utf-8")
    codice = frantuma.conia("TASK-A", "terza", "Terza", onda=1)
    assert codice == "MT-03"
    assert (base_finta / "TASK-A" / "MT-01-prima.md").read_text(encoding="utf-8") == prima


def test_sovrapposizione_di_scope_viene_rilevata(base_finta):
    frantuma.conia("TASK-A", "uno", "Uno", onda=1,
                   scope="company/Ecosistemi/15-LANCI/agenti/lan-gate.md")
    frantuma.conia("TASK-A", "due", "Due", onda=1,
                   scope="company/Ecosistemi/15-LANCI/agenti/lan-gate.md,altro/file.py")
    sovr = frantuma.sovrapposizioni("TASK-A")
    assert len(sovr) == 1
    assert sovr[0][0] == "MT-01" and sovr[0][1] == "MT-02"


def test_scope_disgiunto_non_da_falsi_positivi(base_finta):
    frantuma.conia("TASK-A", "uno", "Uno", onda=1, scope="a/uno.py")
    frantuma.conia("TASK-A", "due", "Due", onda=1, scope="a/due.py")
    assert frantuma.sovrapposizioni("TASK-A") == []


def test_una_cartella_dentro_l_altra_conta_come_sovrapposizione(base_finta):
    """Non solo lo stesso file: se una micro-task tocca l'intera cartella e
    un'altra tocca un file dentro quella cartella, e' comunque una collisione."""
    frantuma.conia("TASK-A", "uno", "Uno", onda=1, scope="company/Ecosistemi/15-LANCI/agenti")
    frantuma.conia("TASK-A", "due", "Due", onda=1,
                   scope="company/Ecosistemi/15-LANCI/agenti/lan-gate.md")
    assert len(frantuma.sovrapposizioni("TASK-A")) == 1


def test_micro_task_in_sequenza_sullo_stesso_percorso_non_e_collisione(base_finta):
    """Il punto vero della funzione: due micro-task che si susseguono (una
    dipende dall'altra) costruiscono legittimamente sullo stesso pezzo. La
    collisione da segnalare e' solo quella fra micro-task che potrebbero
    girare in parallelo in due chat senza che nessuna aspetti l'altra."""
    frantuma.conia("TASK-A", "s0", "S0 incasso", onda=1,
                   scope="company/Ecosistemi/15-LANCI/")
    frantuma.conia("TASK-A", "s1", "S1 lancio a mano", onda=2, deps="MT-01",
                   scope="company/Ecosistemi/15-LANCI/")
    assert frantuma.sovrapposizioni("TASK-A") == []


def test_una_micro_task_senza_dipendenze_e_disponibile_subito(base_finta):
    frantuma.conia("TASK-A", "uno", "Uno", onda=1)
    tutte = frantuma.leggi_tutte("TASK-A")
    per_codice = {m["codice"]: m for m in tutte}
    assert frantuma._disponibile(tutte[0], per_codice) is True


def test_una_micro_task_con_dipendenza_aperta_non_e_disponibile(base_finta):
    frantuma.conia("TASK-A", "uno", "Uno", onda=1)
    frantuma.conia("TASK-A", "due", "Due", onda=2, deps="MT-01")
    tutte = frantuma.leggi_tutte("TASK-A")
    per_codice = {m["codice"]: m for m in tutte}
    seconda = per_codice["MT-02"]
    assert frantuma._disponibile(seconda, per_codice) is False


def test_chiudere_una_dipendenza_sblocca_la_successiva(base_finta):
    frantuma.conia("TASK-A", "uno", "Uno", onda=1)
    frantuma.conia("TASK-A", "due", "Due", onda=2, deps="MT-01")
    frantuma.chiudi("TASK-A", "MT-01")
    tutte = frantuma.leggi_tutte("TASK-A")
    per_codice = {m["codice"]: m for m in tutte}
    assert per_codice["MT-01"]["stato"] == "CHIUSA"
    assert frantuma._disponibile(per_codice["MT-02"], per_codice) is True


def test_report_conta_disponibili_e_chiuse_correttamente(base_finta):
    frantuma.conia("TASK-A", "uno", "Uno", onda=1)
    frantuma.conia("TASK-A", "due", "Due", onda=1)
    frantuma.conia("TASK-A", "tre", "Tre", onda=2, deps="MT-01,MT-02")
    testo = frantuma.report("TASK-A")
    assert "2 disponibili ORA" in testo
    assert "3 totali" in testo
    assert "MT-03" in testo and "aspetta MT-01" in testo


def test_report_su_task_senza_micro_task_lo_dice_chiaro(base_finta):
    testo = frantuma.report("TASK-INESISTENTE")
    assert "Nessuna micro-task" in testo


def test_uno_slug_sporco_viene_rifiutato(base_finta):
    for cattivo in ("Slug Con Spazi", "slug_underscore", "../fuori", ""):
        with pytest.raises(SystemExit):
            frantuma.conia("TASK-A", cattivo, "Titolo", onda=1)


def test_un_padre_sporco_viene_rifiutato(base_finta):
    with pytest.raises(SystemExit):
        frantuma.conia("../fuori", "slug", "Titolo", onda=1)
