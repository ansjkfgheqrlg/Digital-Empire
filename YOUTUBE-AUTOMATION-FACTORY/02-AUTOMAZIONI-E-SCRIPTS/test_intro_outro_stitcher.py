# -*- coding: utf-8 -*-
"""
Test di intro_outro_stitcher.py (A4-RC-14). Le fixture video sono generate al volo con
ffmpeg (sorgente sintetica lavfi): nessuna dipendenza dalla produzione ne' dalla rete. Se
ffmpeg/ffprobe non sono installati, i test che li richiedono si saltano da soli.
"""
from __future__ import annotations

import shutil
import subprocess

import pytest

import intro_outro_stitcher as ios


ha_ffmpeg = shutil.which("ffmpeg") is not None and shutil.which("ffprobe") is not None


def _genera_clip(path, larghezza=320, altezza=240, durata_s=1, fps=10, codec_v="libx264"):
    comando = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"testsrc=size={larghezza}x{altezza}:rate={fps}",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
        "-t", str(durata_s), "-shortest",
        "-pix_fmt", "yuv420p",
        "-c:v", codec_v, "-c:a", "aac",
        str(path),
    ]
    risultato = subprocess.run(comando, capture_output=True, text=True)
    assert risultato.returncode == 0, risultato.stderr


def test_verifica_dipendenze_si_ferma_se_manca_ffmpeg_o_ffprobe(monkeypatch):
    monkeypatch.setattr(shutil, "which", lambda nome: None)
    with pytest.raises(SystemExit) as exc:
        ios.verifica_dipendenze()
    assert "ffmpeg" in str(exc.value) or "ffprobe" in str(exc.value)


@pytest.mark.skipif(not ha_ffmpeg, reason="richiede ffmpeg/ffprobe installati")
def test_concatena_file_compatibili_usa_copy_senza_ricodifica(tmp_path):
    intro = tmp_path / "intro.mp4"
    principale = tmp_path / "video.mp4"
    outro = tmp_path / "outro.mp4"
    uscita = tmp_path / "finale.mp4"
    for p, durata in ((intro, 1), (principale, 2), (outro, 1)):
        _genera_clip(p, durata_s=durata)

    risultato = ios.concatena(str(intro), str(principale), str(outro), str(uscita))

    assert risultato["metodo"] == "copy"
    assert uscita.exists() and uscita.stat().st_size > 0
    # durata attesa = somma delle tre clip (1+2+1=4s), tolleranza per il concat demuxer
    assert risultato["durata_secondi"] == pytest.approx(4.0, abs=0.3)


@pytest.mark.skipif(not ha_ffmpeg, reason="richiede ffmpeg/ffprobe installati")
def test_concatena_file_con_risoluzioni_diverse_ripiega_su_ricodifica(tmp_path):
    intro = tmp_path / "intro.mp4"
    principale = tmp_path / "video.mp4"
    outro = tmp_path / "outro.mp4"
    uscita = tmp_path / "finale.mp4"
    _genera_clip(intro, larghezza=320, altezza=240, durata_s=1)
    _genera_clip(principale, larghezza=640, altezza=360, durata_s=1)  # risoluzione diversa
    _genera_clip(outro, larghezza=320, altezza=240, durata_s=1)

    risultato = ios.concatena(str(intro), str(principale), str(outro), str(uscita))

    assert risultato["metodo"] == "ricodifica"
    assert uscita.exists() and uscita.stat().st_size > 0
    assert risultato["durata_secondi"] == pytest.approx(3.0, abs=0.3)


@pytest.mark.skipif(not ha_ffmpeg, reason="richiede ffmpeg/ffprobe installati")
def test_concatena_forza_ricodifica_anche_con_file_identici(tmp_path):
    intro = tmp_path / "intro.mp4"
    principale = tmp_path / "video.mp4"
    outro = tmp_path / "outro.mp4"
    uscita = tmp_path / "finale.mp4"
    for p in (intro, principale, outro):
        _genera_clip(p, durata_s=1)

    risultato = ios.concatena(str(intro), str(principale), str(outro), str(uscita), forza_ricodifica=True)

    assert risultato["metodo"] == "ricodifica"


@pytest.mark.skipif(not ha_ffmpeg, reason="richiede ffmpeg/ffprobe installati")
def test_concatena_file_mancante_solleva_errore_chiaro(tmp_path):
    principale = tmp_path / "video.mp4"
    _genera_clip(principale, durata_s=1)
    with pytest.raises(FileNotFoundError):
        ios.concatena(str(tmp_path / "non-esiste-intro.mp4"), str(principale),
                      str(tmp_path / "non-esiste-outro.mp4"), str(tmp_path / "out.mp4"))


@pytest.mark.skipif(not ha_ffmpeg, reason="richiede ffmpeg/ffprobe installati")
def test_sonda_legge_codec_e_risoluzione(tmp_path):
    clip = tmp_path / "clip.mp4"
    _genera_clip(clip, larghezza=320, altezza=240, durata_s=1)
    info = ios._sonda(str(clip))
    assert info["video"]["width"] == 320
    assert info["video"]["height"] == 240
    assert info["video"]["codec"] is not None
    assert info["audio"]["codec"] is not None
