# -*- coding: utf-8 -*-
"""
Test di youtube_studio_reader.py. Nessuna rete, nessun Playwright reale: le funzioni pure
(parsing numeri, estrazione da testo) sono testate direttamente; l'interazione con "la
pagina" e' testata con un doppio locale (PaginaFinta) che espone solo .url/.goto()/
.wait_for_timeout()/.inner_text()/.content() — mai import di playwright.sync_api.

I blocchi di testo usati come fixture per i test di estrazione sono copiati VERBATIM da
memory/_report_analytics_overview.txt (catturato dal vivo il 2026-09-03 sul canale reale
"Legami d'amore"), non inventati: se le etichette reali di Studio cambiano, e' proprio
questo il file che deve fallire per primo.
"""
from __future__ import annotations

import os

import youtube_studio_reader as ysr


# ============================================================================================
# PARSING NUMERI — le forme esplicitamente richieste: "1,2 mila", "4,5%", virgola decimale
# italiana, piu' le forme viste dal vivo nella cattura reale.
# ============================================================================================

def test_virgola_decimale_italiana_semplice():
    assert ysr.parse_numero("4,5") == 4.5
    assert ysr.parse_numero("13,2") == 13.2


def test_un_mila_due_con_suffisso_parola():
    assert ysr.parse_numero("1,2 mila") == 1200.0
    assert ysr.parse_numero("1,2mila") == 1200.0


def test_suffisso_k_abbreviato_visto_dal_vivo():
    # memory/_report_analytics_overview.txt riga 40: "13,2K" (Views, ultimi 28 giorni)
    assert ysr.parse_numero("13,2K") == 13200.0
    # riga 41: "6,3K less than usual" -> il segno "-" e' un dettaglio del chiamante,
    # qui si testa solo la lettura del valore assoluto piu' un segno esplicito.
    assert ysr.parse_numero("-6,3K") == -6300.0


def test_punto_delle_migliaia_visto_dal_vivo():
    # riga 76: "2.344" (views di un video nella tabella "Your top content")
    assert ysr.parse_numero("2.344") == 2344.0
    assert ysr.parse_numero("13.156") == 13156.0


def test_punto_decimale_valuta_visto_dal_vivo():
    # riga 52: "€31.72" (Estimated revenue) — punto con 2 cifre dopo = decimale, non migliaia
    assert ysr.parse_numero("€31.72") == 31.72
    assert ysr.parse_numero("31.72") == 31.72


def test_percentuale_con_punto_e_con_virgola():
    # riga 75: "(37.1%)" nella tabella top content
    assert ysr.parse_percentuale("37.1%") == 37.1
    assert ysr.parse_percentuale("4,5%") == 4.5


def test_percentuale_rifiuta_testo_senza_simbolo():
    # senza '%' non e' detto che sia una percentuale: meglio None che indovinare.
    assert ysr.parse_percentuale("37.1") is None


def test_numero_none_o_vuoto_ritorna_none():
    assert ysr.parse_numero(None) is None
    assert ysr.parse_numero("") is None
    assert ysr.parse_numero("   ") is None
    assert ysr.parse_numero("nessun dato") is None


def test_durata_mmss_e_hhmmss():
    # riga 160: "6:33" (Average view duration)
    assert ysr.parse_durata_hhmmss("6:33") == 393
    assert ysr.parse_durata_hhmmss("9:22") == 562
    assert ysr.parse_durata_hhmmss("1:02:03") == 3723
    assert ysr.parse_durata_hhmmss("non e' una durata") is None
    assert ysr.parse_durata_hhmmss(None) is None


def test_campo_valore_presente_non_ha_motivo():
    c = ysr.campo(42.0, grezzo="42")
    assert c == {"valore": 42.0, "motivo": None, "grezzo": "42"}


def test_campo_valore_assente_ha_sempre_un_motivo():
    c = ysr.campo(None, "spiegazione")
    assert c["valore"] is None
    assert c["motivo"] == "spiegazione"
    # anche senza motivo esplicito, non deve mai restare vuoto
    c2 = ysr.campo(None)
    assert c2["motivo"]


# ============================================================================================
# ESTRAZIONE DA TESTO — fixture copiate verbatim dal dump reale.
# ============================================================================================

TESTO_OVERVIEW_CANALE_REALE = """Channel analytics
Action required: Accept updated YouTube Partner Program terms by Jan 31, 2027, to avoid gaps in earnings from features like ads, YouTube Premium, and fan funding
Review and accept
Dismiss
Skip navigation
Ask Studio
Create
Your channel
Legami d'amore
Dashboard
Content
Analytics
Community
Languages
Content detection
Earn
Customization
Audio library
Settings
Send feedback
Channel analytics
Advanced mode
How did viewers find my content?
How many new viewers did I reach?
Summarize my latest video performance
Overview
Content
Audience
Revenue
Trends
Aug 6 – Sep 2, 2026
Last 28 days
We updated how views are counted, so recent counts may be higher. Keep this in mind when analyzing your performance.
Learn more
Dismiss
Your channel got 13,156 views in the last 28 days
There are temporary data issues affecting your views, check back later
Views
Views
13,2K
6,3K less than usual
Channel views compared to your typical performance. Over time, this can help you spot high-performing videos, anticipate seasonal changes, and determine when to upload new videos. This includes public, private, unlisted, and deleted videos.
Watch time (hours)
1,2K
978,7 less than usual
Channel watch time compared to your typical performance. This includes public, private, unlisted, and deleted videos.
Subscribers
+17
17 less than usual
Change in subscribers compared to your typical performance. Over time, this can help you understand what causes viewers to subscribe or unsubscribe to your channel.
Estimated revenue
€31.72
Your final amount may change at the end of the month.
Aug 6, 2026
Aug 11, 2026
Aug 15, 2026
Aug 20, 2026
Aug 24, 2026
Aug 29, 2026
Sep 2, 2...
1.200
800
400
0
Views
See more
Your top content in this period
Content
Average view duration
Views
1
Segnali Che Una Donna Ti Vuole Indietro
Dec 3, 2025
9:22
(37.1%)
2.344
2
7 Frasi di Buongiorno Che Nessuna Donna Può Ignorare: Segreti di Psicologia Femminile!
Nov 24, 2024
3:06
(35.4%)
1.216
4
5 Segnali del Corpo che Rendono un UOMO Irresistibile
Aug 29, 2026
Recent upload
3:56
(49.7%)
812
See more
Realtime
Updating live
14.810
Subscribers
See live count
1.747
Views · Last 48 hours
Now
Latest activity, Views: Last 48 hours, 1.747.
Top content
Views
7 segnali non ti evita, ha paura di innamorarsi
438
Latest content
7 segnali non ti evita, ha paura di innamorarsi
First 2 days 8 hours
Views
586
Thumbnail click-through rate
6.7%
Average view duration
6:33
See video analytics
1 of 10"""


def test_estrai_tiles_overview_canale_dal_dump_reale():
    d = ysr.estrai_tiles_overview_canale(TESTO_OVERVIEW_CANALE_REALE)
    assert d["periodo_effettivo"] == "Last 28 days"
    assert d["views"]["valore"] == 13200.0
    assert d["views"]["motivo"] is None
    assert d["watch_time_ore"]["valore"] == 1200.0
    assert d["iscritti_variazione"]["valore"] == 17.0
    assert d["entrate_stimate"]["valore"] == 31.72
    assert d["entrate_valuta"] == "EUR"


def test_estrai_top_content_canale_dal_dump_reale():
    righe = ysr.estrai_top_content_canale(TESTO_OVERVIEW_CANALE_REALE)
    assert len(righe) == 3  # 3 righe complete nella fixture ridotta (rank 1, 2, 4)
    primo = righe[0]
    assert primo["rank"] == 1
    assert primo["titolo"] == "Segnali Che Una Donna Ti Vuole Indietro"
    assert primo["durata_video_secondi"]["valore"] == 562  # 9:22
    assert primo["retention_media_percento"]["valore"] == 37.1
    assert primo["views"]["valore"] == 2344.0

    # rank 4 ha la riga extra "Recent upload" fra la data e la durata: deve essere saltata
    # senza disallineare i campi successivi.
    terzo = righe[2]
    assert terzo["rank"] == 4
    assert terzo["data_pubblicazione"] == "Aug 29, 2026"
    assert terzo["durata_video_secondi"]["valore"] == 236  # 3:56
    assert terzo["retention_media_percento"]["valore"] == 49.7
    assert terzo["views"]["valore"] == 812.0


def test_estrai_ultimo_video_realtime_dal_dump_reale():
    d = ysr.estrai_ultimo_video_realtime(TESTO_OVERVIEW_CANALE_REALE)
    assert d["titolo"] == "7 segnali non ti evita, ha paura di innamorarsi"
    assert d["ctr_miniatura_percento"]["valore"] == 6.7
    assert d["durata_media_visualizzazione_secondi"]["valore"] == 393  # 6:33
    assert d["views"]["valore"] == 586.0


def test_estrai_top_content_su_testo_senza_la_sezione_ritorna_lista_vuota():
    assert ysr.estrai_top_content_canale("pagina qualunque senza la tabella") == []


def test_estrai_ultimo_video_realtime_su_testo_senza_la_sezione_e_onesto():
    d = ysr.estrai_ultimo_video_realtime("pagina qualunque senza il riquadro")
    assert d["views"]["valore"] is None
    assert "non trovata" in d["views"]["motivo"]
    assert d["ctr_miniatura_percento"]["valore"] is None


def test_estrai_metriche_video_singolo_senza_ctr_ne_retention_scrive_null_con_motivo():
    # Una pagina che non contiene NESSUNA delle etichette ipotizzate: deve restare onesto,
    # mai stimare un numero plausibile.
    testo_vuoto = "Video analytics\nQualcosa che non contiene nessuna etichetta nota"
    d = ysr.estrai_metriche_video_singolo(testo_vuoto, "abc123XYZ00")
    assert d["video_id"] == "abc123XYZ00"
    assert d["ctr_miniatura_percento"]["valore"] is None
    assert d["ctr_miniatura_percento"]["motivo"]
    assert d["retention_media_percento"]["valore"] is None
    assert d["retention_30s_percento"]["valore"] is None
    # il motivo del punto ai 30s deve rimandare all'alternativa gia' pronta (API)
    assert "youtube_analytics_client" in d["retention_30s_percento"]["motivo"]


def test_estrai_metriche_video_singolo_trova_ctr_con_etichetta_alternativa():
    testo = "Impressions click-through rate\n5.4%\nViews\n1.234\nAverage view duration\n2:15"
    d = ysr.estrai_metriche_video_singolo(testo, "abc123XYZ00")
    assert d["ctr_miniatura_percento"]["valore"] == 5.4
    assert d["ctr_etichetta_trovata"] == "Impressions click-through rate"
    assert d["views"]["valore"] == 1234.0
    assert d["durata_media_visualizzazione_secondi"]["valore"] == 135


def test_valida_video_id_accetta_id_valido_e_rifiuta_il_resto():
    assert ysr.valida_video_id(" JOUWaLkyoN8 ") == "JOUWaLkyoN8"
    for cattivo in (None, "", "   ", "https://youtu.be/JOUWaLkyoN8", "ha spazi dentro"):
        try:
            ysr.valida_video_id(cattivo)
            assert False, "doveva sollevare ErroreValidazione per %r" % (cattivo,)
        except ysr.ErroreValidazione:
            pass


# ============================================================================================
# ENTRATA PRONTA PER TESORERIA — deve avere ESATTAMENTE i campi che
# scripts/tesoreria.py entrata si aspetta (--importo --da --per --stato --nota), e mai
# proporre un'entrata quando il valore e' None.
# ============================================================================================

def test_costruisci_entrata_tesoreria_con_valore_reale():
    campo_entrate = {"valore": 31.72, "motivo": None, "grezzo": "€31.72"}
    e = ysr.costruisci_entrata_tesoreria(campo_entrate, "EUR", "Last 28 days", "Legami d'amore")
    assert e["importo"] == 31.72
    assert e["valuta"] == "EUR"
    assert e["per"] == "youtube"
    assert e["stato"] == "previsto"
    assert "Legami d'amore" in e["da"]
    assert "Last 28 days" in e["nota"]


def test_costruisci_entrata_tesoreria_senza_valore_ritorna_none():
    campo_vuoto = {"valore": None, "motivo": "non trovato", "grezzo": None}
    assert ysr.costruisci_entrata_tesoreria(campo_vuoto, "EUR", "Last 28 days") is None
    assert ysr.costruisci_entrata_tesoreria(None, "EUR", "Last 28 days") is None


# ============================================================================================
# SALVATAGGIO SU DISCO — nome file con data/ora, mai sovrascritto.
# ============================================================================================

def test_salva_report_nome_file_con_data_e_ora(tmp_path):
    from datetime import datetime
    adesso = datetime(2026, 9, 10, 14, 30, 5)
    percorso = ysr.salva_report({"prova": True}, output_dir=str(tmp_path), adesso=adesso)
    assert os.path.basename(percorso) == "youtube_studio_report_20260910-143005.json"
    assert os.path.isfile(percorso)


def test_salva_report_due_esecuzioni_diverse_non_si_sovrascrivono(tmp_path):
    from datetime import datetime
    p1 = ysr.salva_report({"n": 1}, output_dir=str(tmp_path), adesso=datetime(2026, 9, 10, 10, 0, 0))
    p2 = ysr.salva_report({"n": 2}, output_dir=str(tmp_path), adesso=datetime(2026, 9, 10, 11, 0, 0))
    assert p1 != p2
    assert os.path.isfile(p1) and os.path.isfile(p2)
    import json as _json
    with open(p1, encoding="utf-8") as f:
        assert _json.load(f)["n"] == 1
    with open(p2, encoding="utf-8") as f:
        assert _json.load(f)["n"] == 2


def test_salva_report_contenuto_json_fedele(tmp_path):
    import json as _json
    dati = {"canale": {"views": 100}, "video": [{"video_id": "abc"}]}
    percorso = ysr.salva_report(dati, output_dir=str(tmp_path))
    with open(percorso, encoding="utf-8") as f:
        assert _json.load(f) == dati


# ============================================================================================
# INTERAZIONE CON "LA PAGINA" — doppio locale, mai import di playwright.
# ============================================================================================

class PaginaFinta:
    """Doppio minimale di una Page Playwright: solo cio' che youtube_studio_reader.py usa."""

    def __init__(self, testo="", url="https://studio.youtube.com/channel/UCFINTO123456/videos"):
        self._testo = testo
        self.url = url
        self.navigazioni = []

    def goto(self, url, **kwargs):
        self.url = url
        self.navigazioni.append(url)

    def wait_for_timeout(self, ms):
        pass

    def inner_text(self, selector):
        return self._testo

    def content(self):
        return self._testo

    def locator(self, selettore):
        class _LocatoreFinto:
            def is_visible(self_inner):
                return False
        return _LocatoreFinto()


def test_verifica_login_pagina_su_url_di_login_e_falso():
    pagina = PaginaFinta(url="https://accounts.google.com/login")
    assert ysr.verifica_login(pagina) is False


def test_verifica_login_pagina_normale_e_vero():
    pagina = PaginaFinta(url="https://studio.youtube.com/channel/UCFINTO123456/videos")
    assert ysr.verifica_login(pagina) is True


def test_ricava_channel_id_da_url_gia_presente():
    pagina = PaginaFinta(url="https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos")
    assert ysr.ricava_channel_id(pagina) == "UC0J2KtEiGnDZnzHlc2Vajpg"


def test_ricava_channel_id_naviga_se_url_iniziale_non_ce_lha():
    pagina = PaginaFinta(url="https://studio.youtube.com/")

    def goto_poi_channel(url, **kwargs):
        pagina.navigazioni.append(url)
        pagina.url = "https://studio.youtube.com/channel/UCABCDEF123456/videos"

    pagina.goto = goto_poi_channel
    assert ysr.ricava_channel_id(pagina) == "UCABCDEF123456"


def test_leggi_tutto_senza_login_e_onesto_e_non_apre_nessun_video():
    pagina = PaginaFinta(url="https://accounts.google.com/login")
    report = ysr.leggi_tutto(pagina, video_ids=["JOUWaLkyoN8"])
    assert "errore" in report
    assert report["video"] == []
    assert report["entrate_pronte_per_tesoreria"] == []


def test_leggi_tutto_con_login_e_canale_costruisce_entrata_tesoreria():
    pagina = PaginaFinta(
        testo=TESTO_OVERVIEW_CANALE_REALE,
        url="https://studio.youtube.com/channel/UC0J2KtEiGnDZnzHlc2Vajpg/videos",
    )
    report = ysr.leggi_tutto(pagina, video_ids=[], canale_nome="Legami d'amore")
    assert report["channel_id"] == "UC0J2KtEiGnDZnzHlc2Vajpg"
    assert report["canale"]["entrate_stimate"]["valore"] == 31.72
    assert len(report["entrate_pronte_per_tesoreria"]) == 1
    entrata = report["entrate_pronte_per_tesoreria"][0]
    assert entrata["importo"] == 31.72
    assert entrata["per"] == "youtube"
    assert entrata["stato"] == "previsto"


# ---------------------------------------------------------------------------
# Runner autonomo (stesso pattern di test_verifica_fatti.py, riga 90+): senza questo,
# `python test_<nome>.py` esce 0 SENZA ESEGUIRE NIENTE — un test silente e' peggio di
# nessun test, perche' rassicura. Gira in entrambi i modi: pytest e `python test_<nome>.py`.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys as _sys
    import traceback as _tb
    import inspect as _ins
    import tempfile as _tempfile

    _falliti = 0
    _casi = [(_n, _f) for _n, _f in sorted(globals().items())
             if _n.startswith("test_") and callable(_f)]
    _saltati = 0
    for _n, _f in _casi:
        _parametri = _ins.signature(_f).parameters
        _kwargs = {}
        _non_soddisfatti = []
        for _p in _parametri:
            if _p == "tmp_path":
                _kwargs["tmp_path"] = __import__("pathlib").Path(_tempfile.mkdtemp())
            else:
                _non_soddisfatti.append(_p)
        if _non_soddisfatti:
            _saltati += 1
            print("SALTATO %s  (richiede pytest: %s)" % (_n, ", ".join(_non_soddisfatti)))
            continue
        try:
            _f(**_kwargs)
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
