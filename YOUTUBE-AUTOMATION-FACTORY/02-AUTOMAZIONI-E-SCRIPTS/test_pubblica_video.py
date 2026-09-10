# -*- coding: utf-8 -*-
"""
Test di pubblica_video.py. Gira SENZA rete e SENZA toccare YouTube: Playwright non viene
nemmeno importato (pubblica_video lo importa solo dentro avvia_playwright_e_pubblica(), mai a
livello di modulo), e la `page` usata nei test e' un doppio minimale (FakePagina/FakeLocator),
stesso pattern gia' in uso in test_youtube_analytics_client.py (classi Fake* iniettate al
posto dell'oggetto reale, invece di monkeypatchare un modulo esterno).

Verifica le tre regole non negoziabili:
  1. --video-id mancante o vuoto ferma tutto (ErroreValidazione), prima che un browser esista.
  2. Senza --conferma esplicito, esegui_pubblicazione() non clicca MAI (FakePagina.clic resta
     vuota), qualunque cosa sia stata chiesta con --pubblica/--programma.
  3. Ogni chiamata (anche di prova) scrive una riga nel log, con id, modalita', stato prima/dopo.
"""
from __future__ import annotations

import argparse
import os
import re
import tempfile

import pubblica_video as pv


# ---------------------------------------------------------------------------------------
# Doppio minimale di una Page di Playwright — nessuna rete, nessun browser vero.
# ---------------------------------------------------------------------------------------

class _FakeLocator:
    def __init__(self, page, descrizione, esiste=True, visibile=True):
        self._page = page
        self._descrizione = descrizione
        self._esiste = esiste
        self._visibile = visibile

    @property
    def first(self):
        return self

    def count(self):
        return 1 if self._esiste else 0

    def is_visible(self):
        return self._visibile

    def click(self, timeout=None):
        if not self._esiste:
            raise RuntimeError("elemento non trovato: %s" % self._descrizione)
        self._page.clic.append(self._descrizione)

    def fill(self, valore):
        if not self._esiste:
            raise RuntimeError("elemento non trovato: %s" % self._descrizione)
        self._page.campi_riempiti[self._descrizione] = valore


class FakePagina:
    """Simula lo stato di una schermata Video di YouTube Studio: quali testi/bottoni/radio
    sono presenti, e registra ogni clic che il codice sotto test avrebbe fatto davvero."""

    def __init__(self, testo_presente=None, radio_presenti=None, visibility_box=False):
        self.testo_presente = set(testo_presente or [])
        self.radio_presenti = set(radio_presenti or [])
        self.visibility_box = visibility_box
        self.clic = []
        self.campi_riempiti = {}
        self.url_visitati = []

    def goto(self, url, **kw):
        self.url_visitati.append(url)

    def wait_for_timeout(self, ms):
        pass

    def content(self):
        return "<html><!-- dom finto di test --></html>"

    def get_by_text(self, testo, exact=True):
        esiste = testo in self.testo_presente
        return _FakeLocator(self, "testo:%s" % testo, esiste, esiste)

    def locator(self, selettore):
        m = re.search(r"name='([A-Z]+)'", selettore)
        if m:
            chiave = m.group(1)
            esiste = chiave in self.radio_presenti
            return _FakeLocator(self, "radio:%s" % chiave, esiste, esiste)
        m2 = re.search(r"has-text\('([^']+)'\)", selettore)
        if m2:
            testo = m2.group(1)
            esiste = testo in self.testo_presente
            return _FakeLocator(self, "bottone:%s" % testo, esiste, esiste)
        if "visibility" in selettore:
            return _FakeLocator(self, "box-visibilita", self.visibility_box, self.visibility_box)
        if "aria-label" in selettore:
            # campi data/ora dello schedule: assenti di default nei test (non verificati dal vivo)
            return _FakeLocator(self, "campo:%s" % selettore, False, False)
        return _FakeLocator(self, "selettore:%s" % selettore, False, False)


def _log_temporaneo():
    fd, percorso = tempfile.mkstemp(prefix="pubblica_video_test_", suffix=".log")
    os.close(fd)
    os.remove(percorso)  # deve nascere da scrivi_log(), non esistere gia'
    return percorso


def _pulisci(percorso):
    try:
        os.remove(percorso)
    except OSError:
        pass


def _args(video_id="RUg6TgSd79s", pubblica=True, programma=None, conferma=False, prova=False):
    ns = argparse.Namespace()
    ns.video_id = video_id
    ns.pubblica = pubblica
    ns.programma = programma
    ns.conferma = conferma
    ns.prova = prova
    return ns


# ---------------------------------------------------------------------------------------
# Regola 1 — id mancante ferma tutto
# ---------------------------------------------------------------------------------------

def test_video_id_vuoto_solleva_errore_validazione():
    try:
        pv.valida_video_id("")
        assert False, "doveva sollevare ErroreValidazione"
    except pv.ErroreValidazione:
        pass


def test_video_id_none_solleva_errore_validazione():
    try:
        pv.valida_video_id(None)
        assert False, "doveva sollevare ErroreValidazione"
    except pv.ErroreValidazione:
        pass


def test_video_id_con_url_intero_rifiutato():
    # non deve accettare un link incollato per sbaglio al posto dell'id nudo
    try:
        pv.valida_video_id("https://www.youtube.com/watch?v=RUg6TgSd79s")
        assert False, "un URL intero non e' un id valido"
    except pv.ErroreValidazione:
        pass


def test_video_id_valido_passa_e_viene_pulito():
    assert pv.valida_video_id("  RUg6TgSd79s  ") == "RUg6TgSd79s"


def test_valida_argomenti_senza_id_ferma_tutto():
    ns = _args(video_id="")
    try:
        pv.valida_argomenti(ns)
        assert False, "doveva fermarsi senza id"
    except pv.ErroreValidazione:
        pass


# ---------------------------------------------------------------------------------------
# Regola 2 — senza conferma esplicita, non si clicca mai
# ---------------------------------------------------------------------------------------

def test_senza_conferma_il_piano_e_di_prova():
    ns = _args(conferma=False)
    piano = pv.valida_argomenti(ns)
    assert piano["esegue_davvero"] is False


def test_conferma_esplicita_attiva_il_piano_reale():
    ns = _args(conferma=True)
    piano = pv.valida_argomenti(ns)
    assert piano["esegue_davvero"] is True


def test_prova_e_conferma_insieme_e_contraddizione():
    ns = _args(conferma=True, prova=True)
    try:
        pv.valida_argomenti(ns)
        assert False, "--prova e --conferma insieme devono fermarsi"
    except pv.ErroreValidazione:
        pass


def test_dry_run_non_clicca_niente_anche_se_tutto_esiste():
    # Anche con radio PRIVATE/PUBLIC e bottoni tutti presenti, senza esegue_davvero=True
    # esegui_pubblicazione() non deve chiamare click() su NULLA.
    piano = {"video_id": "RUg6TgSd79s", "modalita": "pubblica", "quando": None,
             "esegue_davvero": False}
    pagina = FakePagina(testo_presente={"Private", "Done", "Save"},
                         radio_presenti={"PRIVATE", "PUBLIC"})
    log_path = _log_temporaneo()
    try:
        risultato = pv.esegui_pubblicazione(piano, pagina, log_path)
        assert risultato["eseguito"] is False
        assert risultato["prova"] is True
        assert pagina.clic == [], "in dry-run non deve esserci NESSUN clic: %r" % pagina.clic
        assert pagina.url_visitati == ["https://studio.youtube.com/video/RUg6TgSd79s/edit"]
    finally:
        _pulisci(log_path)


def test_dry_run_legge_lo_stato_corretto():
    piano = {"video_id": "abc123", "modalita": "pubblica", "quando": None,
             "esegue_davvero": False}
    pagina = FakePagina(testo_presente={"Public"}, radio_presenti={"PRIVATE", "PUBLIC"})
    log_path = _log_temporaneo()
    try:
        risultato = pv.esegui_pubblicazione(piano, pagina, log_path)
        assert risultato["stato_prima"] == "pubblico"
        assert pagina.clic == []
    finally:
        _pulisci(log_path)


# ---------------------------------------------------------------------------------------
# Esecuzione reale (con --conferma) — verifica che clicchi le cose giuste
# ---------------------------------------------------------------------------------------

def test_conferma_reale_pubblica_clicca_radio_public_e_salva():
    piano = {"video_id": "RUg6TgSd79s", "modalita": "pubblica", "quando": None,
             "esegue_davvero": True}
    pagina = FakePagina(testo_presente={"Private", "Done", "Save"},
                         radio_presenti={"PRIVATE", "PUBLIC"})
    log_path = _log_temporaneo()
    try:
        risultato = pv.esegui_pubblicazione(piano, pagina, log_path)
        assert risultato["eseguito"] is True
        assert "testo:Private" in pagina.clic  # apertura popup
        assert "radio:PUBLIC" in pagina.clic  # selezione Pubblico
        assert "testo:Done" in pagina.clic or "testo:Save" in pagina.clic  # conferma
    finally:
        _pulisci(log_path)


def test_conferma_reale_senza_popup_apribile_non_clicca_radio_e_segnala_errore():
    piano = {"video_id": "RUg6TgSd79s", "modalita": "pubblica", "quando": None,
             "esegue_davvero": True}
    pagina = FakePagina(testo_presente=set(), radio_presenti={"PRIVATE", "PUBLIC"})
    log_path = _log_temporaneo()
    try:
        risultato = pv.esegui_pubblicazione(piano, pagina, log_path)
        assert risultato["eseguito"] is False
        assert "errore" in risultato
        assert "radio:PUBLIC" not in pagina.clic  # non deve mai cliccare la radio a vuoto
    finally:
        _pulisci(log_path)


def test_conferma_reale_radio_public_assente_non_finge_successo():
    piano = {"video_id": "RUg6TgSd79s", "modalita": "pubblica", "quando": None,
             "esegue_davvero": True}
    pagina = FakePagina(testo_presente={"Private"}, radio_presenti={"PRIVATE"})  # niente PUBLIC
    log_path = _log_temporaneo()
    try:
        risultato = pv.esegui_pubblicazione(piano, pagina, log_path)
        assert risultato["eseguito"] is False
        assert risultato["stato_dopo"] == risultato["stato_prima"]  # stato dichiarato invariato
    finally:
        _pulisci(log_path)


# ---------------------------------------------------------------------------------------
# Regola 3 — log sempre scritto, anche in prova
# ---------------------------------------------------------------------------------------

def test_log_viene_scritto_in_dry_run():
    piano = {"video_id": "ID-DI-PROVA", "modalita": "pubblica", "quando": None,
             "esegue_davvero": False}
    pagina = FakePagina(testo_presente={"Private"}, radio_presenti={"PRIVATE", "PUBLIC"})
    log_path = _log_temporaneo()
    try:
        pv.esegui_pubblicazione(piano, pagina, log_path)
        assert os.path.exists(log_path)
        with open(log_path, "r", encoding="utf-8") as f:
            contenuto = f.read()
        assert "ID-DI-PROVA" in contenuto
        assert "modalita=prova" in contenuto
        assert "prima=privato" in contenuto
        assert "dopo=privato" in contenuto
    finally:
        _pulisci(log_path)


def test_log_viene_scritto_in_append_su_esecuzioni_successive():
    piano = {"video_id": "ID-RIPETUTO", "modalita": "pubblica", "quando": None,
             "esegue_davvero": False}
    pagina = FakePagina(testo_presente={"Private"}, radio_presenti={"PRIVATE", "PUBLIC"})
    log_path = _log_temporaneo()
    try:
        pv.esegui_pubblicazione(piano, pagina, log_path)
        pv.esegui_pubblicazione(piano, pagina, log_path)
        with open(log_path, "r", encoding="utf-8") as f:
            righe = [r for r in f.read().splitlines() if r.strip()]
        assert len(righe) == 2, "la seconda scrittura deve aggiungersi, non sovrascrivere"
    finally:
        _pulisci(log_path)


def test_scrivi_log_diretto_contiene_tutti_i_campi_richiesti():
    log_path = _log_temporaneo()
    try:
        riga = pv.scrivi_log("XYZ999", "privato", "pubblico", "pubblica", "nota di test", log_path)
        assert "id=XYZ999" in riga
        assert "prima=privato" in riga
        assert "dopo=pubblico" in riga
        assert "modalita=pubblica" in riga
        # data in formato YYYY-MM-DD presente in testa alla riga
        assert re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \|", riga)
    finally:
        _pulisci(log_path)


# ---------------------------------------------------------------------------------------
# Programmazione (--programma): validazione data/ora
# ---------------------------------------------------------------------------------------

def test_programma_formato_invalido_si_ferma():
    try:
        pv.valida_quando("20 settembre 2026")
        assert False, "formato libero non deve passare"
    except pv.ErroreValidazione:
        pass


def test_programma_nel_passato_si_ferma():
    try:
        pv.valida_quando("2020-01-01 09:00")
        assert False, "una data passata non deve passare"
    except pv.ErroreValidazione:
        pass


def test_programma_vuoto_ritorna_none():
    assert pv.valida_quando("") is None
    assert pv.valida_quando(None) is None


def test_programma_futuro_valido_ritorna_datetime():
    dt = pv.valida_quando("2099-01-01 09:00")
    assert dt.year == 2099 and dt.hour == 9


def test_valida_argomenti_con_programma_imposta_modalita_programma():
    ns = _args(pubblica=False, programma="2099-01-01 09:00", conferma=False)
    piano = pv.valida_argomenti(ns)
    assert piano["modalita"] == "programma"
    assert piano["quando"].year == 2099


def test_programma_senza_selettori_disponibili_non_finge_successo():
    # Selettori data/ora NON verificati dal vivo (vedi docstring di _imposta_programmato):
    # se non li trova, deve dichiararsi fallito, non pretendere di aver programmato.
    piano = {"video_id": "RUg6TgSd79s", "modalita": "programma",
             "quando": pv.valida_quando("2099-01-01 09:00"), "esegue_davvero": True}
    pagina = FakePagina(testo_presente={"Private", "Schedule"}, radio_presenti={"PRIVATE"})
    log_path = _log_temporaneo()
    try:
        risultato = pv.esegui_pubblicazione(piano, pagina, log_path)
        assert risultato["eseguito"] is False
    finally:
        _pulisci(log_path)


# ---------------------------------------------------------------------------------------
# Runner autonomo — copiato dal pattern di test_verifica_fatti.py: senza questo, `python
# test_pubblica_video.py` uscirebbe 0 SENZA ESEGUIRE NIENTE (le funzioni test_* da sole non
# girano fuori da pytest), e un test silenzioso e' peggio di nessun test.
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    import sys as _sys
    import traceback as _tb
    import inspect as _ins

    _falliti = 0
    _casi = [(_n, _f) for _n, _f in sorted(globals().items())
             if _n.startswith("test_") and callable(_f)]
    _saltati = 0
    for _n, _f in _casi:
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
