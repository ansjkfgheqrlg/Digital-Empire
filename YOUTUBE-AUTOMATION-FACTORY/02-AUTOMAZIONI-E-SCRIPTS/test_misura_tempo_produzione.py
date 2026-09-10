# -*- coding: utf-8 -*-
"""
Test di misura_tempo_produzione.py (A4-RC-07). Nessuna dipendenza da produzione o rete:
solo stdlib (time/subprocess/json), quindi i test girano ovunque giri Python.
"""
from __future__ import annotations

import json
import sys

import misura_tempo_produzione as mtp


def test_misura_fase_scrive_una_riga_con_i_campi_attesi(tmp_path):
    log_path = str(tmp_path / "tempi.jsonl")
    with mtp.misura_fase("script", video_id="V-TEST-1", log_path=log_path):
        pass  # blocco cronometrato vuoto: verifica solo il meccanismo, non il carico

    voci = mtp.leggi_log(log_path)
    assert len(voci) == 1
    voce = voci[0]
    assert voce["fase"] == "script"
    assert voce["video_id"] == "V-TEST-1"
    assert voce["esito"] == "ok"
    assert voce["secondi"] >= 0.0
    assert "ts" in voce


def test_misura_fase_registra_errore_e_rilancia_eccezione(tmp_path):
    log_path = str(tmp_path / "tempi.jsonl")
    try:
        with mtp.misura_fase("fliki", video_id="V-TEST-2", log_path=log_path):
            raise ValueError("guasto simulato")
    except ValueError as e:
        assert "guasto simulato" in str(e)
    else:
        raise AssertionError("l'eccezione originale doveva propagarsi, non essere inghiottita")

    voci = mtp.leggi_log(log_path)
    assert len(voci) == 1
    assert voci[0]["esito"] == "errore"
    assert "ValueError" in voci[0]["errore"]


def test_cronometra_comando_wrappa_un_processo_esterno_senza_modificarlo(tmp_path):
    log_path = str(tmp_path / "tempi.jsonl")
    comando = [sys.executable, "-c", "import time; time.sleep(0.05)"]

    risultato = mtp.cronometra_comando("qa", comando, video_id="V-TEST-3", log_path=log_path)

    assert risultato["fase"] == "qa"
    assert risultato["esito"] == "ok"
    assert risultato["codice_uscita"] == 0
    assert risultato["secondi"] >= 0.04  # il sonno reale era 0.05s, tolleranza sotto per lo scheduler

    voci = mtp.leggi_log(log_path)
    assert len(voci) == 1
    assert voci[0]["comando"] == comando


def test_cronometra_comando_registra_codice_di_uscita_diverso_da_zero(tmp_path):
    log_path = str(tmp_path / "tempi.jsonl")
    comando = [sys.executable, "-c", "import sys; sys.exit(3)"]

    risultato = mtp.cronometra_comando("export", comando, log_path=log_path)

    assert risultato["esito"] == "errore"
    assert risultato["codice_uscita"] == 3


def test_genera_report_aggrega_per_fase_con_numeri_reali(tmp_path):
    log_path = str(tmp_path / "tempi.jsonl")
    # tre voci di 'fliki' e una di 'qa', valori noti a mano per verificare l'aggregazione
    righe = [
        {"ts": "x", "fase": "fliki", "secondi": 10.0, "video_id": "v1", "esito": "ok"},
        {"ts": "x", "fase": "fliki", "secondi": 20.0, "video_id": "v2", "esito": "ok"},
        {"ts": "x", "fase": "fliki", "secondi": 30.0, "video_id": "v3", "esito": "ok"},
        {"ts": "x", "fase": "qa", "secondi": 5.0, "video_id": "v1", "esito": "ok"},
    ]
    with open(log_path, "w", encoding="utf-8") as f:
        for r in righe:
            f.write(json.dumps(r) + "\n")

    aggregato = mtp.aggrega_per_fase(mtp.leggi_log(log_path))

    assert aggregato["fliki"]["conteggio"] == 3
    assert aggregato["fliki"]["secondi_totali"] == 60.0
    assert aggregato["fliki"]["secondi_medi"] == 20.0
    assert aggregato["fliki"]["secondi_min"] == 10.0
    assert aggregato["fliki"]["secondi_max"] == 30.0
    assert aggregato["qa"]["secondi_totali"] == 5.0

    # la fase piu' lenta (fliki, 60s totali) deve comparire per prima: e' la risposta a
    # "dove rallenta la catena"
    prima_fase = next(iter(aggregato))
    assert prima_fase == "fliki"

    report = mtp.genera_report(log_path)
    assert "fliki" in report
    assert "qa" in report


def test_genera_report_senza_log_non_esplode(tmp_path):
    log_path = str(tmp_path / "inesistente.jsonl")
    report = mtp.genera_report(log_path)
    assert "nessuna misurazione" in report.lower() or "vuoto" in report.lower()


def test_misura_fase_rifiuta_nome_fase_vuoto():
    try:
        mtp.misura_fase("")
    except ValueError:
        pass
    else:
        raise AssertionError("una fase senza nome deve sollevare ValueError subito, non a fine blocco")
