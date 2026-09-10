# -*- coding: utf-8 -*-
"""
Test di reframe_shorts.py (A4-RC-10). Le fixture video sono generate al volo con ffmpeg
(sorgente sintetica lavfi): nessuna dipendenza dalla produzione ne' dalla rete. Se ffmpeg o
opencv non sono installati sulla macchina che esegue i test, i test che li richiedono si
saltano da soli invece di fallire in modo fuorviante (coerente con la regola dello script:
dipendenza assente = lo dice e si ferma, non fallisce a meta').
"""
from __future__ import annotations

import shutil
import subprocess

import pytest

import reframe_shorts as rf


ha_ffmpeg = shutil.which("ffmpeg") is not None
ha_cv2 = rf._HAS_CV2


def _genera_video_sintetico(path, larghezza=640, altezza=360, durata_s=2, fps=10):
    """Crea un MP4 16:9 sintetico (testsrc + audio muto) con ffmpeg, senza toccare la rete."""
    comando = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"testsrc=size={larghezza}x{altezza}:rate={fps}",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
        "-t", str(durata_s), "-shortest",
        "-pix_fmt", "yuv420p",
        "-c:v", "libx264", "-c:a", "aac",
        str(path),
    ]
    risultato = subprocess.run(comando, capture_output=True, text=True)
    assert risultato.returncode == 0, risultato.stderr


# --- funzioni pure (nessuna dipendenza esterna) -----------------------------------------

def test_media_mobile_appiattisce_un_picco_isolato():
    valori = [100.0, 100.0, 500.0, 100.0, 100.0]
    lisci = rf._media_mobile(valori, finestra=5)
    assert lisci[2] < 500.0  # il picco centrale viene smussato dalla media mobile
    assert lisci[0] == pytest.approx(sum(valori[0:3]) / 3)


def test_media_mobile_finestra_1_non_modifica_i_valori():
    valori = [1.0, 2.0, 3.0]
    assert rf._media_mobile(valori, finestra=1) == valori


def test_comprimi_segmenti_unisce_campioni_vicini():
    campioni = [[0.0, 100, True], [0.5, 103, True], [1.0, 400, True], [1.5, 405, True]]
    segmenti = rf._comprimi_segmenti(campioni, soglia_px=8.0)
    # i primi due (100,103) e gli ultimi due (400,405) sono entro soglia: si accorpano in 2 segmenti
    assert segmenti == [[0.0, 100], [1.0, 400]]


def test_costruisci_espressione_ffmpeg_singolo_segmento_e_costante():
    assert rf._costruisci_espressione_ffmpeg([[0.0, 42]]) == "42"


def test_costruisci_espressione_ffmpeg_piu_segmenti_annida_gli_if():
    espressione = rf._costruisci_espressione_ffmpeg([[0.0, 10], [1.0, 20], [2.0, 30]])
    assert espressione == "if(lt(t,1.000),10,if(lt(t,2.000),20,30))"


# --- verifica dipendenze -----------------------------------------------------------------

def test_verifica_dipendenze_si_ferma_se_manca_ffmpeg(monkeypatch):
    monkeypatch.setattr(shutil, "which", lambda nome: None)
    with pytest.raises(SystemExit) as exc:
        rf.verifica_dipendenze()
    assert "ffmpeg" in str(exc.value)


def test_verifica_dipendenze_si_ferma_se_manca_opencv(monkeypatch):
    monkeypatch.setattr(shutil, "which", lambda nome: "/usr/bin/ffmpeg")
    monkeypatch.setattr(rf, "_HAS_CV2", False)
    with pytest.raises(SystemExit) as exc:
        rf.verifica_dipendenze()
    assert "opencv" in str(exc.value)


# --- integrazione reale con ffmpeg + opencv (saltata se assenti) -------------------------

@pytest.mark.skipif(not ha_ffmpeg or not ha_cv2, reason="richiede ffmpeg e opencv installati")
def test_reframe_verticale_produce_un_file_9_16_dalla_sorgente_sintetica(tmp_path):
    sorgente = tmp_path / "orizzontale.mp4"
    uscita = tmp_path / "verticale.mp4"
    _genera_video_sintetico(sorgente)

    risultato = rf.reframe_verticale(
        str(sorgente), str(uscita),
        campioni_al_secondo=2.0, larghezza_uscita=270, altezza_uscita=480, smoothing=3,
    )

    assert uscita.exists() and uscita.stat().st_size > 0
    assert risultato["output"] == str(uscita)
    assert risultato["risoluzione_uscita"] == "270x480"
    assert risultato["campioni_totali"] > 0
    assert 0.0 <= risultato["percentuale_rilevazione"] <= 100.0
    assert risultato["rilevatore"] in ("mediapipe", "opencv-haar")

    # verifica la risoluzione reale del file prodotto (non solo il valore dichiarato)
    import cv2
    cap = cv2.VideoCapture(str(uscita))
    larghezza_reale = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    altezza_reale = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    assert larghezza_reale == 270
    assert altezza_reale == 480
    assert abs((larghezza_reale / altezza_reale) - (9 / 16)) < 0.01


@pytest.mark.skipif(not ha_ffmpeg or not ha_cv2, reason="richiede ffmpeg e opencv installati")
def test_reframe_verticale_su_sorgente_senza_volti_ripiega_su_centro_fisso(tmp_path):
    # testsrc non contiene volti: verifica il ramo di ripiego (nessun soggetto rilevato ->
    # ritaglio statico centrato, non un crash)
    sorgente = tmp_path / "senza_volti.mp4"
    uscita = tmp_path / "verticale.mp4"
    _genera_video_sintetico(sorgente, durata_s=1)

    risultato = rf.reframe_verticale(str(sorgente), str(uscita), campioni_al_secondo=2.0,
                                      larghezza_uscita=180, altezza_uscita=320)

    assert risultato["campioni_con_soggetto"] == 0
    assert risultato["percentuale_rilevazione"] == 0.0
    assert uscita.exists()


@pytest.mark.skipif(not ha_ffmpeg or not ha_cv2, reason="richiede ffmpeg e opencv installati")
def test_reframe_verticale_su_file_inesistente_solleva_errore_chiaro(tmp_path):
    with pytest.raises(FileNotFoundError):
        rf.reframe_verticale(str(tmp_path / "non-esiste.mp4"), str(tmp_path / "out.mp4"))


# ---------------------------------------------------------------------------
# Runner autonomo (aggiunto 2026-09-10). Senza questo, `python test_<nome>.py`
# usciva 0 SENZA ESEGUIRE NIENTE: i test in stile pytest sono sole funzioni, e un
# file che esce 0 in silenzio sembra un test verde mentre non ha provato nulla.
# Un test silente e' peggio di nessun test, perche' rassicura. Ora gira in
# entrambi i modi: `pytest` e `python test_<nome>.py`.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys as _sys, traceback as _tb
    _falliti = 0
    _casi = [(_n, _f) for _n, _f in sorted(globals().items())
             if _n.startswith("test_") and callable(_f)]
    import inspect as _ins
    _saltati = 0
    for _n, _f in _casi:
        # I casi che chiedono una fixture di pytest (tmp_path, monkeypatch...) non possono
        # girare qui: si dichiarano SALTATI, non falliti. Chiamarli "falliti" farebbe
        # scattare un allarme falso ogni volta, e un allarme che grida sempre viene spento.
        if _ins.signature(_f).parameters:
            _saltati += 1
            print("SALTATO %s  (richiede pytest: %s)"
                  % (_n, ", ".join(_ins.signature(_f).parameters)))
            continue
        try:
            _f()
            print("OK      %s" % _n)
        except Exception:
            _falliti += 1
            print("FALLITO %s" % _n)
            _tb.print_exc()
    _eseguiti = len(_casi) - _saltati
    print("")
    print("%d/%d test passati (%d saltati, girano con: python -m pytest %s)"
          % (_eseguiti - _falliti, _eseguiti, _saltati, __file__.rsplit("\\", 1)[-1]))
    _sys.exit(1 if _falliti else 0)
