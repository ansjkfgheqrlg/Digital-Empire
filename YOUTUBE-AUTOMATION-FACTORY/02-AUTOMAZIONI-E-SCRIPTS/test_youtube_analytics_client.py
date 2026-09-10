# -*- coding: utf-8 -*-
"""
Test di youtube_analytics_client.py (A4-RC-15). Nessuna chiamata di rete: le risposte API
sono finte (fixture Python), e il caricamento credenziali con refresh_token e' testato
sostituendo la classe Credentials con un doppio locale che non tocca la rete.
"""
from __future__ import annotations

import os

import pytest

import youtube_analytics_client as yac


# --- funzioni pure ------------------------------------------------------------------------

def test_durata_iso8601_a_secondi_casi_noti():
    assert yac._durata_iso8601_a_secondi("PT4M13S") == 253.0
    assert yac._durata_iso8601_a_secondi("PT1H2M3S") == 3723.0
    assert yac._durata_iso8601_a_secondi("PT45S") == 45.0
    assert yac._durata_iso8601_a_secondi("PT2H") == 7200.0
    assert yac._durata_iso8601_a_secondi("") == 0.0
    assert yac._durata_iso8601_a_secondi("garbage") == 0.0


def test_estrai_punto_30s_sceglie_il_campione_piu_vicino():
    # durata video 100s: 30s equivale a ratio 0.30
    righe = [[0.0, 1.0], [0.10, 0.95], [0.29, 0.80], [0.31, 0.78], [0.50, 0.60], [1.0, 0.20]]
    punto = yac.estrai_punto_30s(righe, durata_secondi=100.0)
    assert punto is not None
    assert punto["elapsed_video_time_ratio"] == 0.29  # 0.29 e' piu' vicino a 0.30 di 0.31? verifica sotto
    assert punto["audience_watch_ratio"] == 0.80
    assert punto["secondo_stimato"] == pytest.approx(29.0, abs=0.01)


def test_estrai_punto_30s_video_piu_corto_di_30s_clampa_al_100_percento():
    righe = [[0.0, 1.0], [0.5, 0.5], [1.0, 0.1]]
    punto = yac.estrai_punto_30s(righe, durata_secondi=10.0, secondo_target=30.0)
    # 30s su un video di 10s: ratio_target clampato a 1.0 -> sceglie l'ultimo campione
    assert punto["elapsed_video_time_ratio"] == 1.0
    assert punto["audience_watch_ratio"] == 0.1


def test_estrai_punto_30s_senza_righe_o_durata_ritorna_none():
    assert yac.estrai_punto_30s([], durata_secondi=100.0) is None
    assert yac.estrai_punto_30s([[0.0, 1.0]], durata_secondi=0.0) is None
    assert yac.estrai_punto_30s([[0.0, 1.0]], durata_secondi=None) is None


# --- credenziali: mai rete, mai file dentro il repo ----------------------------------------

def _pulisci_env_credenziali(monkeypatch):
    for var in ("YT_ANALYTICS_CLIENT_ID", "YT_ANALYTICS_CLIENT_SECRET",
                "YT_ANALYTICS_REFRESH_TOKEN", "YT_ANALYTICS_TOKEN_FILE"):
        monkeypatch.delenv(var, raising=False)


def test_carica_credenziali_senza_nulla_si_ferma_con_messaggio_chiaro(monkeypatch):
    _pulisci_env_credenziali(monkeypatch)
    with pytest.raises(yac.CredenzialiMancanti) as exc:
        yac.carica_credenziali()
    messaggio = str(exc.value).lower()
    assert "yt_analytics_client_id" in messaggio or "yt_analytics_token_file" in messaggio


def test_carica_credenziali_rifiuta_token_file_dentro_il_repo(monkeypatch):
    _pulisci_env_credenziali(monkeypatch)
    percorso_dentro_repo = os.path.join(yac.SCRIPT_DIR, "token_finto.json")
    monkeypatch.setenv("YT_ANALYTICS_TOKEN_FILE", percorso_dentro_repo)
    with pytest.raises(yac.CredenzialiMancanti) as exc:
        yac.carica_credenziali()
    assert "repository" in str(exc.value).lower()


def test_carica_credenziali_token_file_fuori_repo_ma_inesistente(monkeypatch, tmp_path):
    _pulisci_env_credenziali(monkeypatch)
    percorso_fuori_repo = str(tmp_path / "token.json")  # tmp_path e' sempre fuori dal repo
    monkeypatch.setenv("YT_ANALYTICS_TOKEN_FILE", percorso_fuori_repo)
    with pytest.raises(yac.CredenzialiMancanti) as exc:
        yac.carica_credenziali()
    assert "inesistente" in str(exc.value).lower()


def test_carica_credenziali_con_variabili_dirette_non_tocca_la_rete(monkeypatch):
    """
    Verifica il percorso 'felice' (client_id + client_secret + refresh_token in ambiente)
    senza mai chiamare Google: sostituisce Credentials con un doppio che non fa richieste.
    """
    _pulisci_env_credenziali(monkeypatch)
    monkeypatch.setenv("YT_ANALYTICS_CLIENT_ID", "id-finto")
    monkeypatch.setenv("YT_ANALYTICS_CLIENT_SECRET", "secret-finto")
    monkeypatch.setenv("YT_ANALYTICS_REFRESH_TOKEN", "refresh-finto")

    chiamate_refresh = []

    class CredenzialiFinte:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def refresh(self, request):
            chiamate_refresh.append(request)  # nessuna rete: solo registra la chiamata

    import google.oauth2.credentials as modulo_credenziali
    monkeypatch.setattr(modulo_credenziali, "Credentials", CredenzialiFinte)

    creds = yac.carica_credenziali()

    assert isinstance(creds, CredenzialiFinte)
    assert creds.kwargs["client_id"] == "id-finto"
    assert creds.kwargs["refresh_token"] == "refresh-finto"
    assert len(chiamate_refresh) == 1  # refresh chiamato una volta, mai un secondo login


# --- costruzione curva di retention: API finta, nessuna rete --------------------------------

def test_costruisci_curva_retention_con_api_finta(monkeypatch):
    class FakeVideosList:
        def execute(self):
            return {"items": [{"contentDetails": {"duration": "PT1M40S"}}]}  # 100 secondi

    class FakeVideos:
        def list(self, part, id):
            assert part == "contentDetails"
            assert id == "VID123"
            return FakeVideosList()

    class FakeReportsQuery:
        def execute(self):
            return {"rows": [[0.0, 1.0], [0.30, 0.75], [0.60, 0.40], [1.0, 0.10]]}

    class FakeReports:
        def query(self, **kwargs):
            assert kwargs["filters"] == "video==VID123"
            return FakeReportsQuery()

    class FakeYoutubeClient:
        def videos(self):
            return FakeVideos()

    class FakeAnalyticsClient:
        def reports(self):
            return FakeReports()

    def fake_build(nome_servizio, versione, credentials):
        if nome_servizio == "youtube":
            return FakeYoutubeClient()
        if nome_servizio == "youtubeAnalytics":
            return FakeAnalyticsClient()
        raise AssertionError(f"servizio inatteso: {nome_servizio}")

    import googleapiclient.discovery as modulo_discovery
    monkeypatch.setattr(modulo_discovery, "build", fake_build)

    risultato = yac.costruisci_curva_retention("VID123", credenziali=object())

    assert risultato["video_id"] == "VID123"
    assert risultato["durata_secondi"] == 100.0
    assert risultato["n_punti"] == 4
    assert risultato["punto_30s"]["elapsed_video_time_ratio"] == 0.30
    assert risultato["punto_30s"]["audience_watch_ratio"] == 0.75
    assert risultato["punto_30s"]["secondo_stimato"] == pytest.approx(30.0, abs=0.01)


def test_costruisci_curva_retention_video_non_trovato_solleva_errore(monkeypatch):
    class FakeVideosList:
        def execute(self):
            return {"items": []}

    class FakeVideos:
        def list(self, part, id):
            return FakeVideosList()

    class FakeYoutubeClient:
        def videos(self):
            return FakeVideos()

    def fake_build(nome_servizio, versione, credentials):
        return FakeYoutubeClient()

    import googleapiclient.discovery as modulo_discovery
    monkeypatch.setattr(modulo_discovery, "build", fake_build)

    with pytest.raises(ValueError):
        yac.costruisci_curva_retention("VID-INESISTENTE", credenziali=object())


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
