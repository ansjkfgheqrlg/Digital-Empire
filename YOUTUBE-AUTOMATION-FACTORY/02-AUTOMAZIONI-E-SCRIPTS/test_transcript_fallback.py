# -*- coding: utf-8 -*-
"""Test di transcript_fallback.py (A4-RC-06). Nessuna chiamata di rete: `_esegui_ytdlp` viene
sostituita (monkeypatch) con risposte sintetiche che riproducono i guasti reali osservati
(timeout, HTTP error, assenza dello strumento, video davvero senza sottotitoli)."""
from __future__ import annotations

import json
import os

import transcript_fallback as tf


# --------------------------------------------------------------------------------------
# classifica_guasto — funzione pura, il cuore della misura A4-RC-06
# --------------------------------------------------------------------------------------
def test_strumento_assente_riconosciuto():
    g = tf.classifica_guasto(None, "", "", non_trovato=True)
    assert g["guasto"] == "strumento_assente"


def test_timeout_e_strumento_muto():
    g = tf.classifica_guasto(None, "", "", scaduto=True)
    assert g["guasto"] == "strumento_muto"


def test_errore_rete_e_strumento_muto_non_video_senza_sottotitoli():
    stderr = "ERROR: [youtube] abc123: Unable to download webpage: HTTP Error 429: Too Many Requests"
    g = tf.classifica_guasto(1, "", stderr)
    assert g["guasto"] == "strumento_muto"
    assert g["certezza"] == "alta"


def test_video_dichiarato_senza_sottotitoli_dal_tool():
    stderr = "WARNING: [youtube] abc123: There are no subtitles for the requested languages"
    g = tf.classifica_guasto(0, "", stderr)
    assert g["guasto"] == "video_senza_sottotitoli"


def test_uscita_pulita_senza_errori_e_video_senza_sottotitoli_media_certezza():
    g = tf.classifica_guasto(0, "", "")
    assert g["guasto"] == "video_senza_sottotitoli"
    assert g["certezza"] == "media"


def test_errore_sconosciuto_trattato_come_strumento_muto_per_prudenza():
    g = tf.classifica_guasto(2, "", "qualcosa di mai visto prima")
    assert g["guasto"] == "strumento_muto"
    assert g["certezza"] == "bassa"


def test_i_due_guasti_restano_distinguibili():
    """La misura esplicita della regola: i due esiti non devono MAI collassare nello stesso
    valore, o il log non serve a niente."""
    guasto_strumento = tf.classifica_guasto(1, "", "Connection reset by peer")
    guasto_video = tf.classifica_guasto(0, "", "")
    assert guasto_strumento["guasto"] != guasto_video["guasto"]


# --------------------------------------------------------------------------------------
# recupera_transcript_fallback — con _esegui_ytdlp sostituita, zero rete
# --------------------------------------------------------------------------------------
def test_fallback_trova_sottotitoli_manuali(tmp_path, monkeypatch):
    out_dir = str(tmp_path)
    video_id, prefisso = "VIDEOID1", "dosementale"
    percorso_vtt = os.path.join(out_dir, f"{prefisso}-{video_id}-fallback.it.vtt")

    def _finto_ytdlp(argomenti, timeout=180):
        # simula yt-dlp che scrive davvero il file, come farebbe con sottotitoli manuali trovati
        with open(percorso_vtt, "w", encoding="utf-8") as f:
            f.write("WEBVTT\n\n00:00:00.000 --> 00:00:02.000\nCiao a tutti benvenuti\n")
        return 0, "", "", False, False

    monkeypatch.setattr(tf, "_esegui_ytdlp", _finto_ytdlp)
    risultato = tf.recupera_transcript_fallback(video_id, "https://example.com/watch", out_dir,
                                                prefisso=prefisso)
    assert risultato["esito"] == "trovato"
    assert risultato["via"] == "sottotitoli_manuali"
    assert "Ciao a tutti benvenuti" in risultato["transcript"]
    assert risultato["guasto"] is None


def test_fallback_nessun_file_e_guasto_strumento_muto_riportato(tmp_path, monkeypatch):
    def _finto_ytdlp(argomenti, timeout=180):
        return 1, "", "ERROR: Unable to download webpage: HTTP Error 403: Forbidden", False, False

    monkeypatch.setattr(tf, "_esegui_ytdlp", _finto_ytdlp)
    risultato = tf.recupera_transcript_fallback("VIDEOID2", "https://example.com/watch", str(tmp_path))
    assert risultato["esito"] == "non_trovato"
    assert risultato["guasto"]["guasto"] == "strumento_muto"


def test_fallback_nessun_file_e_guasto_video_senza_sottotitoli_riportato(tmp_path, monkeypatch):
    def _finto_ytdlp(argomenti, timeout=180):
        return 0, "", "", False, False  # gira pulito, ma non scrive nessun .vtt

    monkeypatch.setattr(tf, "_esegui_ytdlp", _finto_ytdlp)
    risultato = tf.recupera_transcript_fallback("VIDEOID3", "https://example.com/watch", str(tmp_path))
    assert risultato["esito"] == "non_trovato"
    assert risultato["guasto"]["guasto"] == "video_senza_sottotitoli"


# --------------------------------------------------------------------------------------
# Log JSONL — append-only, serve a misurare quanti candidati si perdono per ciascun guasto
# --------------------------------------------------------------------------------------
def test_registra_esito_scrive_una_riga_jsonl_leggibile(tmp_path):
    percorso_log = os.path.join(str(tmp_path), "sottocartella", "log.jsonl")
    risultato = {"video_id": "X1", "esito": "non_trovato",
                "guasto": {"guasto": "strumento_muto", "certezza": "alta", "dettaglio": "test"}}
    tf.registra_esito(risultato, percorso_log)
    tf.registra_esito(risultato, percorso_log)  # append, non sovrascrive

    righe = open(percorso_log, encoding="utf-8").read().strip().splitlines()
    assert len(righe) == 2
    voce = json.loads(righe[0])
    assert voce["video_id"] == "X1"
    assert voce["guasto"]["guasto"] == "strumento_muto"
    assert "quando" in voce


# --------------------------------------------------------------------------------------
def test_pulisci_vtt_rimuove_timestamp_e_duplicati(tmp_path):
    percorso = os.path.join(str(tmp_path), "prova.vtt")
    with open(percorso, "w", encoding="utf-8") as f:
        f.write(
            "WEBVTT\nKind: captions\nLanguage: it\n\n"
            "00:00:00.000 --> 00:00:02.000\nCiao a tutti\n\n"
            "00:00:02.000 --> 00:00:04.000\nCiao a tutti\nbenvenuti nel video\n"
        )
    testo = tf._pulisci_vtt(percorso)
    assert "-->" not in testo
    assert testo.count("Ciao a tutti") == 1  # la riga duplicata (karaoke) va tolta
    assert "benvenuti nel video" in testo


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
