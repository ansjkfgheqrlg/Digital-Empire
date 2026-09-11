# -*- coding: utf-8 -*-
"""
Test di carica_pronti.py. Gira SENZA rete e SENZA lanciare un processo reale: subprocess.run
e' sostituito via monkeypatch con un doppio programmabile (nessun apex7_orchestrator.py vero
viene mai eseguito). Le cartelle sono tutte temporanee (tmp_path/tmp_dir), create a mano con
solo i file che servono al caso da verificare.

Verifica le cose che il committente ha dichiarato non negoziabili:
  1. Selezione: un video e' 'pronto' solo con video.mp4 + metadata.json + copertina + canale
     riconosciuto + nessun youtube_id gia' scritto. Ognuna di queste condizioni, mancante da
     sola, esclude la cartella (mai un errore che scoppia: uno stato riportato).
  2. Ordine: il piu' vecchio (mtime di video.mp4 piu' basso) parte per primo.
  3. --prova (default) non lancia MAI subprocess.run.
  4. --conferma lancia un video alla volta e si FERMA al primo fallimento (non processa i
     successivi).
  5. Dopo un caricamento riuscito, metadata.json riceve youtube_id/caricato_il -- e la
     cartella non e' piu' 'pronto' al giro successivo (protezione anti-doppio-caricamento).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time

import carica_pronti as cp


# ---------------------------------------------------------------------------------------
# Helper di costruzione cartelle finte -- niente pytest fixtures: il runner in fondo esegue
# solo funzioni senza parametri, quindi ogni test si costruisce/pulisce da solo.
# ---------------------------------------------------------------------------------------

class _CartellaTemporanea:
    """Context manager minimale attorno a tempfile.mkdtemp -- non serve tmp_path di pytest,
    cosi' i test girano anche con il runner autonomo in fondo al file."""

    def __enter__(self):
        self.path = tempfile.mkdtemp(prefix="carica_pronti_test_")
        return self.path

    def __exit__(self, *exc):
        shutil.rmtree(self.path, ignore_errors=True)
        return False


def _crea_video(base_dir, nome, *, video=True, metadata=None, immagine=True, copy_md=None,
                 mtime=None):
    """Crea una cartella video-NN dentro base_dir con i file richiesti. `metadata=None`
    significa NIENTE metadata.json; passare un dict (anche {}) per crearlo."""
    cartella = os.path.join(base_dir, nome)
    os.makedirs(cartella, exist_ok=True)

    if video:
        video_path = os.path.join(cartella, "video.mp4")
        with open(video_path, "wb") as f:
            f.write(b"finto-mp4")
        if mtime is not None:
            os.utime(video_path, (mtime, mtime))

    if metadata is not None:
        with open(os.path.join(cartella, "metadata.json"), "w", encoding="utf-8") as f:
            json.dump(metadata, f)

    if immagine:
        with open(os.path.join(cartella, "copertina.png"), "wb") as f:
            f.write(b"finta-immagine")

    if copy_md is not None:
        with open(os.path.join(cartella, "copy.md"), "w", encoding="utf-8") as f:
            f.write(copy_md)

    return cartella


class _RisultatoFinto:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


# ---------------------------------------------------------------------------------------
# 1. Selezione -- ogni condizione mancante esclude la cartella, con uno stato leggibile.
# ---------------------------------------------------------------------------------------

def test_cartella_completa_e_pronto():
    with _CartellaTemporanea() as base:
        cartella = _crea_video(base, "video-01", metadata={"title": "T"},
                                copy_md="canale legamidiamore")
        esito = cp.analizza_cartella("video-01", cartella)
        assert esito["stato"] == "pronto"
        assert esito["canale"] == "legamidiamore"


def test_manca_video_esclude():
    with _CartellaTemporanea() as base:
        cartella = _crea_video(base, "video-01", video=False, metadata={"title": "T"},
                                copy_md="legamidiamore")
        esito = cp.analizza_cartella("video-01", cartella)
        assert esito["stato"] == "manca_video"


def test_manca_metadata_esclude():
    with _CartellaTemporanea() as base:
        cartella = _crea_video(base, "video-01", metadata=None, copy_md="legamidiamore")
        esito = cp.analizza_cartella("video-01", cartella)
        assert esito["stato"] == "manca_metadata"


def test_manca_copertina_esclude():
    with _CartellaTemporanea() as base:
        cartella = _crea_video(base, "video-01", metadata={"title": "T"}, immagine=False,
                                copy_md="legamidiamore")
        esito = cp.analizza_cartella("video-01", cartella)
        assert esito["stato"] == "manca_copertina"


def test_canale_sconosciuto_non_si_indovina():
    with _CartellaTemporanea() as base:
        # nessun copy.md, metadata senza campo canale: nessun marcatore trovabile da nessuna parte
        cartella = _crea_video(base, "video-01", metadata={"title": "T"}, copy_md=None)
        esito = cp.analizza_cartella("video-01", cartella)
        assert esito["stato"] == "canale_sconosciuto"


def test_canale_letto_da_metadata_json():
    with _CartellaTemporanea() as base:
        cartella = _crea_video(base, "video-01", metadata={"title": "T", "canale": "dosementale"},
                                copy_md=None)
        esito = cp.analizza_cartella("video-01", cartella)
        assert esito["stato"] == "pronto"
        assert esito["canale"] == "dosementale"


def test_gia_caricato_esclude_dai_pronti():
    with _CartellaTemporanea() as base:
        cartella = _crea_video(base, "video-01",
                                metadata={"title": "T", "youtube_id": "abc123XYZ"},
                                copy_md="legamidiamore")
        esito = cp.analizza_cartella("video-01", cartella)
        assert esito["stato"] == "gia_caricato"


# ---------------------------------------------------------------------------------------
# 2. Ordine -- il piu' vecchio (mtime video.mp4 piu' basso) prima.
# ---------------------------------------------------------------------------------------

def test_ordine_per_anzianita_il_piu_vecchio_prima():
    with _CartellaTemporanea() as base:
        adesso = time.time()
        _crea_video(base, "video-03", metadata={"title": "recente"}, copy_md="legamidiamore",
                    mtime=adesso - 1 * 86400)
        _crea_video(base, "video-01", metadata={"title": "vecchio"}, copy_md="legamidiamore",
                    mtime=adesso - 18 * 86400)
        _crea_video(base, "video-02", metadata={"title": "medio"}, copy_md="legamidiamore",
                    mtime=adesso - 5 * 86400)

        report = cp.costruisci_report(base)
        candidati = cp.ordina_per_anzianita(report)

        assert [r["nome"] for r in candidati] == ["video-01", "video-02", "video-03"]


# ---------------------------------------------------------------------------------------
# 3. --prova non lancia mai subprocess.run.
# ---------------------------------------------------------------------------------------

def test_prova_non_lancia_subprocess(monkeypatch):
    chiamate = []
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: chiamate.append((a, k)) or _RisultatoFinto())

    with _CartellaTemporanea() as base:
        _crea_video(base, "video-01", metadata={"title": "T"}, copy_md="legamidiamore")
        log_path = os.path.join(base, "log.txt")

        codice = cp.esegui(video_pronti_dir=base, log_path=log_path, conferma=False,
                            stampa=lambda *a, **k: None)

        assert codice == 0
        assert chiamate == []
        # anche la prova lascia traccia nel log (regola generale del repo, vedi pubblica_video.py)
        assert os.path.exists(log_path)
        with open(log_path, encoding="utf-8") as f:
            assert "PROVA" in f.read()


# ---------------------------------------------------------------------------------------
# 4. --conferma: un video alla volta, si ferma al primo fallimento.
# ---------------------------------------------------------------------------------------

def test_conferma_si_ferma_al_primo_fallimento(monkeypatch):
    adesso = time.time()

    def subprocess_run_finto(cmd, **kwargs):
        # Il piu' vecchio (video-01) fallisce: returncode != 0. video-02 non deve MAI essere
        # tentato dopo -- se lo fosse, la lista `chiamate` avrebbe 2 elementi.
        chiamate.append(cmd)
        return _RisultatoFinto(returncode=1, stdout="[!] ERRORE: qualcosa non ha funzionato")

    chiamate = []
    monkeypatch.setattr(subprocess, "run", subprocess_run_finto)

    with _CartellaTemporanea() as base:
        _crea_video(base, "video-01", metadata={"title": "vecchio"}, copy_md="legamidiamore",
                    mtime=adesso - 10 * 86400)
        _crea_video(base, "video-02", metadata={"title": "nuovo"}, copy_md="legamidiamore",
                    mtime=adesso - 1 * 86400)
        log_path = os.path.join(base, "log.txt")

        codice = cp.esegui(video_pronti_dir=base, log_path=log_path, conferma=True,
                            stampa=lambda *a, **k: None)

        assert codice == 1
        assert len(chiamate) == 1, "non deve tentare video-02 dopo il fallimento di video-01"
        # ha tentato la cartella piu' vecchia, non una a caso
        assert any("video-01" in str(arg) for arg in chiamate[0])


# ---------------------------------------------------------------------------------------
# 5. Upload riuscito -- scrive youtube_id/caricato_il, e la cartella non e' piu' 'pronto'.
# ---------------------------------------------------------------------------------------

def test_upload_riuscito_scrive_id_e_impedisce_doppio_caricamento(monkeypatch):
    output_finto = ("[+] Upload reale completato — https://www.youtube.com/watch?v=ID12345678 "
                     "(PRIVATO). Registrato in memory/published_videos.json.")

    def subprocess_run_finto(cmd, **kwargs):
        return _RisultatoFinto(returncode=0, stdout=output_finto)

    monkeypatch.setattr(subprocess, "run", subprocess_run_finto)

    with _CartellaTemporanea() as base:
        cartella = _crea_video(base, "video-01", metadata={"title": "T"}, copy_md="legamidiamore")
        log_path = os.path.join(base, "log.txt")

        codice = cp.esegui(video_pronti_dir=base, log_path=log_path, conferma=True,
                            stampa=lambda *a, **k: None)

        assert codice == 0
        with open(os.path.join(cartella, "metadata.json"), encoding="utf-8") as f:
            metadata_dopo = json.load(f)
        assert metadata_dopo["youtube_id"] == "ID12345678"
        assert "caricato_il" in metadata_dopo

        # riscansionando la stessa cartella ora e' 'gia_caricato', non piu' 'pronto'
        esito = cp.analizza_cartella("video-01", cartella)
        assert esito["stato"] == "gia_caricato"


def test_upload_ok_ma_senza_id_estratto_e_trattato_come_fallito(monkeypatch):
    # returncode 0 ma nessun URL watch?v= nell'output: non deve scrivere nulla in
    # metadata.json (rischierebbe un id vuoto/sbagliato) e deve segnalare fallimento.
    def subprocess_run_finto(cmd, **kwargs):
        return _RisultatoFinto(returncode=0, stdout="tutto ok ma nessun url qui dentro")

    monkeypatch.setattr(subprocess, "run", subprocess_run_finto)

    with _CartellaTemporanea() as base:
        cartella = _crea_video(base, "video-01", metadata={"title": "T"}, copy_md="legamidiamore")
        log_path = os.path.join(base, "log.txt")

        codice = cp.esegui(video_pronti_dir=base, log_path=log_path, conferma=True,
                            stampa=lambda *a, **k: None)

        assert codice == 1
        with open(os.path.join(cartella, "metadata.json"), encoding="utf-8") as f:
            metadata_dopo = json.load(f)
        assert "youtube_id" not in metadata_dopo


def test_stato_bozza_rilevato_e_riportato_nel_log(monkeypatch):
    output_finto = ("[+] Upload reale completato — https://www.youtube.com/watch?v=ID99999999 "
                     "(PRIVATO). This video is in a draft state, verificare su Studio.")

    def subprocess_run_finto(cmd, **kwargs):
        return _RisultatoFinto(returncode=0, stdout=output_finto)

    monkeypatch.setattr(subprocess, "run", subprocess_run_finto)

    with _CartellaTemporanea() as base:
        _crea_video(base, "video-01", metadata={"title": "T"}, copy_md="legamidiamore")
        log_path = os.path.join(base, "log.txt")

        cp.esegui(video_pronti_dir=base, log_path=log_path, conferma=True,
                  stampa=lambda *a, **k: None)

        with open(log_path, encoding="utf-8") as f:
            contenuto = f.read()
        assert "BOZZA" in contenuto


# ---------------------------------------------------------------------------------------
# Funzioni pure di supporto -- coperte a parte perche' sono i mattoni di tutto il resto.
# ---------------------------------------------------------------------------------------

def test_costruisci_comando_riusa_esattamente_il_comando_documentato():
    cmd = cp.costruisci_comando("/qualsiasi/VIDEO-PRONTI/video-05", "legamidiamore",
                                 script_dir="/qualsiasi/02-AUTOMAZIONI-E-SCRIPTS")
    assert cmd[1:8] == ["apex7_orchestrator.py", "run", "--canale", "legamidiamore",
                         "--phase", "5", "--upload"]
    assert cmd[-2] == "--skip-thumbnail" or cmd[-1] == "--skip-thumbnail"
    assert "--video-folder" in cmd


def test_estrai_video_id_e_url_prende_ultima_occorrenza():
    testo = ("riga inutile\n"
             "[+] Upload reale completato — https://www.youtube.com/watch?v=ULTIMOID12 (PRIVATO).")
    video_id, url = cp.estrai_video_id_e_url(testo)
    assert video_id == "ULTIMOID12"
    assert url.endswith("ULTIMOID12")


def test_estrai_video_id_assente_ritorna_none():
    video_id, url = cp.estrai_video_id_e_url("nessun url qui")
    assert video_id is None and url is None


def test_rileva_canale_conflitto_ritorna_none():
    # due canali diversi citati nello stesso testo: non si indovina, si ferma.
    canale = cp.rileva_canale({}, "prima menzione legamidiamore, poi dosementale")
    assert canale is None


# ---------------------------------------------------------------------------------------
# Runner autonomo (stesso pattern di test_verifica_fatti.py): senza questo, `python
# test_carica_pronti.py` uscirebbe 0 senza eseguire niente. I casi con `monkeypatch` come
# parametro vengono eseguiti con un doppio minimale locale (niente pytest richiesto).
# ---------------------------------------------------------------------------------------

class _MonkeypatchMinimale:
    """Doppio minimale di pytest.monkeypatch.setattr/undo, per far girare i test che lo
    richiedono anche fuori da pytest (stesso spirito di FakePagina in test_pubblica_video.py:
    un doppio locale invece di dipendere dal framework per il runner autonomo)."""

    def __init__(self):
        self._originali = []

    def setattr(self, obj, nome, valore):
        self._originali.append((obj, nome, getattr(obj, nome)))
        setattr(obj, nome, valore)

    def undo(self):
        for obj, nome, valore in reversed(self._originali):
            setattr(obj, nome, valore)
        self._originali.clear()


if __name__ == "__main__":
    import sys as _sys, traceback as _tb, inspect as _ins

    _falliti = 0
    _saltati = 0
    _casi = [(_n, _f) for _n, _f in sorted(globals().items())
             if _n.startswith("test_") and callable(_f)]

    for _n, _f in _casi:
        _parametri = list(_ins.signature(_f).parameters)
        if _parametri and _parametri != ["monkeypatch"]:
            _saltati += 1
            print("SALTATO %s  (richiede pytest: %s)" % (_n, ", ".join(_parametri)))
            continue
        _mp = _MonkeypatchMinimale() if _parametri == ["monkeypatch"] else None
        try:
            _f(_mp) if _mp is not None else _f()
            print("OK      %s" % _n)
        except Exception:
            _falliti += 1
            print("FALLITO %s" % _n)
            _tb.print_exc()
        finally:
            if _mp is not None:
                _mp.undo()

    _eseguiti = len(_casi) - _saltati
    print("")
    print("%d/%d test passati (%d saltati, girano con: python -m pytest %s)"
          % (_eseguiti - _falliti, _eseguiti, _saltati, __file__.rsplit("\\", 1)[-1]))
    _sys.exit(1 if _falliti else 0)
