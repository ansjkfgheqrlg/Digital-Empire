# -*- coding: utf-8 -*-
"""Test di verifica_pronuncia.py (A4-RC-13). Nessuna dipendenza da un video vero della
fabbrica: un MP4 di 2 secondi generato con ffmpeg per il test end-to-end, e testi sintetici per
la logica di confronto (che e' il cuore dello script e non richiede ne' ASR ne' ffmpeg)."""
from __future__ import annotations

import os
import shutil
import subprocess

import pytest

from verifica_pronuncia import (
    confronta_pronuncia, carica_modello, trascrivi_mp4, scrivi_proposte_lessico, MODELLI_DIR,
)

FFMPEG_DISPONIBILE = shutil.which("ffmpeg") is not None
MODELLO_BASE_LOCALE = os.path.exists(os.path.join(MODELLI_DIR, "faster-whisper-base", "model.bin"))


# --------------------------------------------------------------------------------------
# Logica di confronto — funzione pura, sempre testabile
# --------------------------------------------------------------------------------------
def test_nessuno_scarto_su_testo_identico():
    risultato = confronta_pronuncia("questa è la voce narrante", "questa è la voce narrante")
    assert risultato["esito"] == "passa"
    assert risultato["scarti"] == []


def test_parola_sostituita_rilevata():
    risultato = confronta_pronuncia(
        "grande affetto dei suoi figli",
        "grande effetto dei suoi figli",
    )
    assert risultato["esito"] == "BLOCCO"
    tipi = {s["tipo"] for s in risultato["scarti"]}
    assert "sostituita" in tipi
    sostituzione = next(s for s in risultato["scarti"] if s["tipo"] == "sostituita")
    assert sostituzione["atteso"] == "affetto"
    assert sostituzione["sentito"] == "effetto"


def test_parola_mancante_rilevata():
    risultato = confronta_pronuncia("il nome esatto è importante qui", "il nome è importante qui")
    tipi_mancanti = [s for s in risultato["scarti"] if s["tipo"] == "mancante"]
    assert tipi_mancanti and tipi_mancanti[0]["atteso"] == "esatto"


def test_proposte_lessico_generate_da_scarti():
    risultato = confronta_pronuncia("Gorbaciov ha parlato", "Gorbaciof ha parlato")
    assert risultato["proposte_lessico"], "una sostituzione deve generare una proposta"
    proposta = risultato["proposte_lessico"][0]
    assert proposta["si_scrive"] == "gorbaciov"
    assert proposta["si_legge_male_cosi"] == "gorbaciof"
    assert proposta["si_scrive_per_farla_leggere_bene"] == ""  # colonna da compilare a mano


def test_scrivi_proposte_lessico_su_file_nuovo(tmp_path):
    proposte = [{"si_scrive": "gorbaciov", "si_legge_male_cosi": "gorbaciof",
                 "si_scrive_per_farla_leggere_bene": ""}]
    percorso = os.path.join(str(tmp_path), "proposte.md")
    n = scrivi_proposte_lessico(proposte, percorso, trovata_in="video-test.mp4")
    assert n == 1
    contenuto = open(percorso, encoding="utf-8").read()
    assert "gorbaciov" in contenuto and "video-test.mp4" in contenuto
    assert "si scrive" in contenuto  # intestazione tabella presente


# --------------------------------------------------------------------------------------
# Caricamento modello: dipendenza esterna dichiarata, mai un fallimento silenzioso
# --------------------------------------------------------------------------------------
def test_modello_sconosciuto_da_errore_chiaro():
    modello, errore = carica_modello("un-modello-che-non-esiste")
    assert modello is None
    assert errore is not None
    assert "model.bin" in errore or "assente" in errore


@pytest.mark.skipif(not MODELLO_BASE_LOCALE, reason="modelli/faster-whisper-base non presente su questa macchina")
def test_modello_base_locale_si_carica():
    modello, errore = carica_modello("base")
    assert errore is None
    assert modello is not None


# --------------------------------------------------------------------------------------
# End-to-end: MP4 di 2 secondi generato con ffmpeg (fixture piccola, non un video vero)
# --------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def mp4_due_secondi(tmp_path_factory):
    if not FFMPEG_DISPONIBILE:
        pytest.skip("ffmpeg non disponibile in questo ambiente")
    cartella = tmp_path_factory.mktemp("fixture_pronuncia")
    percorso = os.path.join(str(cartella), "due_secondi.mp4")
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "lavfi", "-i", "sine=frequency=440:duration=2",
        "-f", "lavfi", "-i", "color=c=blue:s=64x64:d=2",
        "-shortest", "-pix_fmt", "yuv420p", percorso,
    ]
    subprocess.run(cmd, check=True, timeout=30)
    return percorso


@pytest.mark.skipif(not (FFMPEG_DISPONIBILE and MODELLO_BASE_LOCALE),
                     reason="serve ffmpeg + modelli/faster-whisper-base locale")
def test_trascrivi_mp4_pipeline_completa_senza_crash(mp4_due_secondi):
    """Un tono puro non contiene parlato: non ci aspettiamo un testo sensato, solo che l'intera
    pipeline (estrazione audio + caricamento modello + trascrizione) giri fino in fondo senza
    eccezioni e ritorni una stringa (anche vuota)."""
    testo, errore = trascrivi_mp4(mp4_due_secondi, nome_modello="base")
    assert errore is None
    assert isinstance(testo, str)


def test_mp4_inesistente_da_errore_senza_crash():
    testo, errore = trascrivi_mp4("percorso/inesistente.mp4", nome_modello="base")
    assert testo is None
    assert errore is not None


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
