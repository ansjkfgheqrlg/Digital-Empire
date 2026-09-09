# -*- coding: utf-8 -*-
"""Lo spaccatore di task grandi in micro-task (scripts/frantuma.py).

PERCHE' ESISTE. Max ha chiesto una funzione che spacchi una task grande in
micro-task ufficiali, ognuna col suo ID -- esattamente come ADR e checkpoint.
Prima versione ci aveva messo dentro onde/parallelismo/verifica di scope non
richiesti: corretta il 2026-09-08, resta solo split + conio atomico + lo
schema fisso viola-con-frecce.
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
    """Due task grandi diverse partono ognuna da MT-01: il numero deve dire
    'il pezzo N-esimo DI QUESTA task', non essere un ID globale."""
    frantuma.conia("TASK-A", "primo", "Primo pezzo di A")
    codice_b = frantuma.conia("TASK-B", "primo", "Primo pezzo di B")
    assert codice_b == "MT-01"


def test_coniare_occupa_il_numero_creando_il_file(base_finta):
    codice = frantuma.conia("TASK-LANCI-BUILD-W3", "s0-incasso", "Giorno zero")
    assert codice == "MT-01"
    assert (base_finta / "TASK-LANCI-BUILD-W3" / "MT-01-s0-incasso.md").exists()
    assert frantuma.conia("TASK-LANCI-BUILD-W3", "seconda", "Seconda") == "MT-02"


def test_un_file_gia_presente_non_viene_sovrascritto(base_finta):
    frantuma.conia("TASK-A", "prima", "Prima")
    prima = (base_finta / "TASK-A" / "MT-01-prima.md").read_text(encoding="utf-8")
    (base_finta / "TASK-A" / "MT-02-altro.md").write_text("# stub\n", encoding="utf-8")
    codice = frantuma.conia("TASK-A", "terza", "Terza")
    assert codice == "MT-03"
    assert (base_finta / "TASK-A" / "MT-01-prima.md").read_text(encoding="utf-8") == prima


def test_uno_slug_sporco_viene_rifiutato(base_finta):
    for cattivo in ("Slug Con Spazi", "slug_underscore", "../fuori", ""):
        with pytest.raises(SystemExit):
            frantuma.conia("TASK-A", cattivo, "Titolo")


def test_un_padre_sporco_viene_rifiutato(base_finta):
    with pytest.raises(SystemExit):
        frantuma.conia("../fuori", "slug", "Titolo")


def test_report_legge_i_titoli_veri_dai_file(base_finta):
    frantuma.conia("TASK-A", "uno", "Sostituire la chiave Brevo esposta")
    frantuma.conia("TASK-A", "due", "Catena dell'incasso")
    testo = frantuma.report("TASK-A")
    assert "MT-01" in testo and "Sostituire la chiave Brevo esposta" in testo
    assert "MT-02" in testo and "Catena dell'incasso" in testo


def test_report_ha_lo_schema_fisso_viola_con_frecce(base_finta):
    """La forma esatta approvata da Max 08/09: titolo, sottotitolo col conteggio,
    un ramo per micro-task (└── sull'ultima), tutte col marcatore 🟣."""
    frantuma.conia("TASK-A", "uno", "Prima")
    frantuma.conia("TASK-A", "due", "Seconda")
    righe = frantuma.report("TASK-A").split("\n")
    assert righe[0] == "🟣 **TASK-A**"
    assert righe[1] == "🟣 divisa in 2 micro-task ufficiali"
    assert righe[3].startswith("   ├──🟣→ **MT-01**")
    assert righe[4].startswith("   └──🟣→ **MT-02**")


def test_report_su_task_senza_micro_task_lo_dice_chiaro(base_finta):
    testo = frantuma.report("TASK-INESISTENTE")
    assert "Nessuna micro-task" in testo
