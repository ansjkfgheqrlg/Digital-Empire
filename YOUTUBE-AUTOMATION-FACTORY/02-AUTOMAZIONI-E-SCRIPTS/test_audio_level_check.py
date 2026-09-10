# -*- coding: utf-8 -*-
"""Test di audio_level_check.py (A4-RC-11). Fixture: un MP4 di 2 secondi generato al volo con
ffmpeg (lavfi: sinusoide + video sintetico), mai un video vero della fabbrica."""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile

import pytest

from audio_level_check import misura_livello, valuta_livello, TETTO_MUSICA_DB_DEFAULT

FFMPEG_DISPONIBILE = shutil.which("ffmpeg") is not None


@pytest.fixture(scope="module")
def mp4_due_secondi(tmp_path_factory):
    """MP4 di 2 secondi: sinusoide a 1000Hz (audio reale, non silenzio) + video sintetico."""
    if not FFMPEG_DISPONIBILE:
        pytest.skip("ffmpeg non disponibile in questo ambiente")
    cartella = tmp_path_factory.mktemp("fixture_audio")
    percorso = os.path.join(str(cartella), "due_secondi.mp4")
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "lavfi", "-i", "sine=frequency=1000:duration=2",
        "-f", "lavfi", "-i", "color=c=gray:s=64x64:d=2",
        "-shortest", "-pix_fmt", "yuv420p", percorso,
    ]
    subprocess.run(cmd, check=True, timeout=30)
    assert os.path.exists(percorso)
    return percorso


# --------------------------------------------------------------------------------------
def test_misura_livello_su_fixture_reale(mp4_due_secondi):
    misura = misura_livello(mp4_due_secondi)
    assert misura["disponibile"] is True
    assert isinstance(misura["mean_db"], float)
    assert isinstance(misura["max_db"], float)
    # una sinusoide piena scala non e' silenzio ne' clipping assurdo
    assert -60.0 < misura["mean_db"] <= 0.0
    assert -60.0 < misura["max_db"] <= 0.5


def test_file_inesistente_non_disponibile():
    misura = misura_livello("questo/file/non/esiste.mp4")
    assert misura["disponibile"] is False
    assert "inesistente" in misura["errore"]


def test_ffmpeg_assente_gestito_con_messaggio_chiaro(monkeypatch, tmp_path):
    finto_file = tmp_path / "video.mp4"
    finto_file.write_bytes(b"non importa, ffmpeg non c'e'")
    monkeypatch.setattr("audio_level_check.shutil.which", lambda nome: None)
    misura = misura_livello(str(finto_file))
    assert misura["disponibile"] is False
    assert "ffmpeg" in misura["errore"].lower()


# --------------------------------------------------------------------------------------
def test_valuta_fascia_voce_fuori_soglia_blocca():
    misura = {"disponibile": True, "mean_db": -5.0, "max_db": -1.0}
    risultato = valuta_livello(misura, fascia_voce=(-30.0, -20.0))
    assert risultato["esito"] == "BLOCCO"
    assert any("fascia dichiarata" in p for p in risultato["problemi"])


def test_valuta_fascia_voce_dentro_soglia_passa():
    misura = {"disponibile": True, "mean_db": -15.0, "max_db": -3.0}
    risultato = valuta_livello(misura, fascia_voce=(-20.0, -10.0))
    assert risultato["esito"] == "passa"


def test_valuta_senza_fascia_dichiarata_non_inventa_soglia():
    misura = {"disponibile": True, "mean_db": -50.0, "max_db": -1.0}
    risultato = valuta_livello(misura)
    assert risultato["esito"] == "passa"
    assert any("non dichiarata" in n for n in risultato["note"])


def test_valuta_tetto_musica_superato_blocca():
    misura = {"disponibile": True, "mean_db": -20.0, "max_db": -10.0}
    risultato = valuta_livello(misura, tetto_musica_db=TETTO_MUSICA_DB_DEFAULT)
    assert risultato["esito"] == "BLOCCO"
    assert any("tetto musica" in p for p in risultato["problemi"])


def test_valuta_tetto_musica_rispettato_passa():
    misura = {"disponibile": True, "mean_db": -40.0, "max_db": -36.0}
    risultato = valuta_livello(misura, tetto_musica_db=TETTO_MUSICA_DB_DEFAULT)
    assert risultato["esito"] == "passa"


def test_valuta_misura_non_disponibile_blocca_con_motivo():
    risultato = valuta_livello({"disponibile": False, "errore": "motivo di test"})
    assert risultato["esito"] == "BLOCCO"
    assert risultato["motivo"] == "motivo di test"
