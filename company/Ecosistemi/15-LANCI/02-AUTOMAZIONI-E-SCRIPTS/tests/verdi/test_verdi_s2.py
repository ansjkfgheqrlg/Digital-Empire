# -*- coding: utf-8 -*-
"""I test VERDI di S2c+S2d: per ogni gate un artefatto che PASSA, e per ogni clausola del
criterio eseguibile un caso che BOCCIA con il problema atteso nel testo.

Le fixture di base stanno in tests/fixture/s2/ e sono costruite per passare tutti e sei
i gate (offerta.json si ottiene dalla proposta aggiungendo una firma con l'impronta
giusta). Ogni caso rosso-di-clausola parte da li' e rompe UNA cosa sola.
"""
import json
import os
import shutil
import sys
from datetime import date, timedelta

import pytest

QUI = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.dirname(QUI)
sys.path.insert(0, os.path.dirname(TESTS))

from scripts import gates  # noqa: E402
from scripts.gates import ReteFinta, esegui_gate, sha256_file  # noqa: E402

FIXTURE = os.path.join(TESTS, "fixture", "s2")
ARTEFATTI_BASE = ["pubblico.json", "decisione.json", "certificato.json", "ricerca.json",
                  "previsione.json", "offerta.PROPOSTA.json"]
URL_PRD = {"https://esempio.test/a": 200, "https://esempio.test/b": 200}
URL_INT = {"https://esempio.test/fonte-1": 200, "https://esempio.test/fonte-2": 200,
           "https://esempio.test/fonte-3": 200}
FIRMA = {"chi": "Max", "canale": "comando-utente",
         "riferimento": "lancio firma prova-s2 --prezzo 67 --data 15/01/2030",
         "il": "2026-09-15T10:00:00+02:00"}


def _leggi(dir_lancio, nome):
    with open(os.path.join(dir_lancio, nome), encoding="utf-8") as f:
        return json.load(f)


def _scrivi(dir_lancio, nome, dati):
    with open(os.path.join(dir_lancio, nome), "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


def _firma(dir_lancio):
    """offerta.json = proposta + firma con l'impronta della proposta corrente."""
    off = _leggi(dir_lancio, "offerta.PROPOSTA.json")
    off.pop("_nota", None)
    off["firma"] = dict(FIRMA, proposta_impronta=sha256_file(
        os.path.join(dir_lancio, "offerta.PROPOSTA.json")))
    _scrivi(dir_lancio, "offerta.json", off)
    return off


@pytest.fixture
def lancio(tmp_path):
    d = tmp_path / "lanci" / "prova-s2"
    d.mkdir(parents=True)
    for n in ARTEFATTI_BASE:
        shutil.copy(os.path.join(FIXTURE, n), d / n)
    return str(d)


def _boccia_con(v, testo):
    assert v.passa is False
    assert any(testo in p for p in v.problemi), "atteso %r in %r" % (testo, v.problemi)


def _passa(v):
    assert v.passa is True, v.problemi
    assert v.problemi == []
    assert v.ramo_fallimento is None


# ====================================================================== scoperta

def test_i_sei_gate_sono_costruiti():
    for g in ("GATE-PUB-1", "GATE-STR-1", "GATE-PRD-1", "GATE-INT-1", "GATE-PRV-1", "GATE-OFF-1"):
        assert g in gates.gate_costruiti()
        mod = gates.trova_gate(g)
        assert mod.ID == g and mod.ARTEFATTO in gates.ARTEFATTI


@pytest.mark.parametrize("gate_id", ["GATE-PUB-1", "GATE-STR-1", "GATE-PRD-1",
                                     "GATE-INT-1", "GATE-PRV-1", "GATE-OFF-1"])
def test_artefatto_assente_boccia_con_assente(gate_id, tmp_path):
    d = tmp_path / "vuoto"
    d.mkdir()
    v = esegui_gate(gate_id, str(d), ReteFinta())
    _boccia_con(v, "assente")
    assert v.ramo_fallimento  # lo stato di destinazione e' sempre noto


@pytest.mark.parametrize("gate_id,nome", [("GATE-PUB-1", "pubblico.json"), ("GATE-STR-1", "decisione.json"),
                                          ("GATE-PRD-1", "certificato.json"), ("GATE-INT-1", "ricerca.json"),
                                          ("GATE-PRV-1", "previsione.json")])
def test_schema_rotto_boccia_elencando_gli_errori(gate_id, nome, lancio):
    a = _leggi(lancio, nome)
    a["schema_version"] = "9.9.9"
    _scrivi(lancio, nome, a)
    _boccia_con(esegui_gate(gate_id, lancio, ReteFinta()), "schema: schema_version")


# ====================================================================== GATE-PUB-1

def test_pub_passa_e_non_apre_la_rete(lancio):
    rete = ReteFinta()
    v = esegui_gate("GATE-PUB-1", lancio, rete)
    _passa(v)
    assert v.dati["somma_verificata"] == 1000 and v.dati["canali_con_prova_valida"] == 2
    assert rete.chiamate == []


def test_pub_prova_nessuna_vale_zero(lancio):
    p = _leggi(lancio, "pubblico.json")
    p["canali"][0]["prova"]["tipo"] = "nessuna"
    p["totale_raggiungibile_verificato"] = 200
    _scrivi(lancio, "pubblico.json", p)
    v = esegui_gate("GATE-PUB-1", lancio, ReteFinta())
    _boccia_con(v, "prova.tipo 'nessuna' non ammessa")
    assert v.dati["somma_verificata"] == 200


def test_pub_prova_piu_vecchia_di_30_giorni(lancio):
    p = _leggi(lancio, "pubblico.json")
    p["canali"][0]["prova"]["data"] = "2026-07-01"   # misurato_il = 2026-09-01
    p["totale_raggiungibile_verificato"] = 200
    _scrivi(lancio, "pubblico.json", p)
    _boccia_con(esegui_gate("GATE-PUB-1", lancio, ReteFinta()), "anteriore a 30 giorni")


def test_pub_prova_a_30_giorni_esatti_passa(lancio):
    p = _leggi(lancio, "pubblico.json")
    p["canali"][0]["prova"]["data"] = "2026-08-02"
    _scrivi(lancio, "pubblico.json", p)
    _passa(esegui_gate("GATE-PUB-1", lancio, ReteFinta()))


def test_pub_totale_dichiarato_diverso_dal_ricalcolo(lancio):
    p = _leggi(lancio, "pubblico.json")
    p["totale_raggiungibile_verificato"] = 5000
    _scrivi(lancio, "pubblico.json", p)
    _boccia_con(esegui_gate("GATE-PUB-1", lancio, ReteFinta()), "dichiarato 5000 ma ricalcolato 1000")


def test_pub_somma_zero_con_prove_valide(lancio):
    p = _leggi(lancio, "pubblico.json")
    for c in p["canali"]:
        c["raggiungibili_verificati"] = 0
    p["totale_raggiungibile_verificato"] = 0
    _scrivi(lancio, "pubblico.json", p)
    _boccia_con(esegui_gate("GATE-PUB-1", lancio, ReteFinta()), "nessun pubblico verificato")


# ====================================================================== GATE-STR-1

def test_str_passa(lancio):
    v = esegui_gate("GATE-STR-1", lancio, ReteFinta())
    _passa(v)
    assert v.dati["si"] == 5 and v.dati["no"] == 0


def test_str_file_citato_non_esiste(lancio):
    d = _leggi(lancio, "decisione.json")
    d["domande"][1]["sostenuta_da"] = "non-esiste.json"
    _scrivi(lancio, "decisione.json", d)
    v = esegui_gate("GATE-STR-1", lancio, ReteFinta())
    _boccia_con(v, "sostenuta_da 'non-esiste.json' non e' un file esistente")
    assert v.dati["file_mancanti"] == ["non-esiste.json"]


def test_str_file_fuori_dalla_cartella_del_lancio_non_vale(lancio):
    d = _leggi(lancio, "decisione.json")
    fuori = os.path.join(os.path.dirname(lancio), "altro.json")
    with open(fuori, "w", encoding="utf-8") as f:
        f.write("{}")
    d["domande"][1]["sostenuta_da"] = "../altro.json"        # esiste, ma fuori dal lancio
    d["domande"][2]["sostenuta_da"] = os.path.abspath(__file__)  # assoluto: non vale
    _scrivi(lancio, "decisione.json", d)
    v = esegui_gate("GATE-STR-1", lancio, ReteFinta())
    assert v.passa is False and len(v.dati["file_mancanti"]) == 2


def test_str_domande_duplicate_non_sono_cinque(lancio):
    d = _leggi(lancio, "decisione.json")
    d["domande"][4]["id"] = "D1-prodotto-esiste"
    _scrivi(lancio, "decisione.json", d)
    _boccia_con(esegui_gate("GATE-STR-1", lancio, ReteFinta()), "mancano ['D5-nessun-lancio-in-conflitto']")


def test_str_esito_archiviato_non_prosegue(lancio):
    d = _leggi(lancio, "decisione.json")
    d["esito"] = "archiviato"
    d["ragione_archiviazione"] = "prova"
    _scrivi(lancio, "decisione.json", d)
    _boccia_con(esegui_gate("GATE-STR-1", lancio, ReteFinta()), "esito dichiarato 'archiviato'")


# ====================================================================== GATE-PRD-1

def test_prd_passa_e_riapre_ogni_link(lancio):
    rete = ReteFinta(URL_PRD)
    v = esegui_gate("GATE-PRD-1", lancio, rete)
    _passa(v)
    assert sorted(rete.chiamate) == sorted(URL_PRD)
    assert v.dati["link_vivi"] == 2 and v.dati["byte_reali"] > 0


def test_prd_bandiera_presente(lancio):
    c = _leggi(lancio, "certificato.json")
    c["bandiere_rosse"][3]["presente"] = True
    _scrivi(lancio, "certificato.json", c)
    _boccia_con(esegui_gate("GATE-PRD-1", lancio, ReteFinta(URL_PRD)), "bandiere rosse presenti (1): RF4")


def test_prd_file_prodotto_inesistente(lancio):
    c = _leggi(lancio, "certificato.json")
    c["file_prodotto"]["percorso"] = "non/esiste/prodotto.pdf"
    _scrivi(lancio, "certificato.json", c)
    _boccia_con(esegui_gate("GATE-PRD-1", lancio, ReteFinta(URL_PRD)), "non esiste")


def test_prd_file_prodotto_vuoto_e_percorso_assoluto(lancio, tmp_path):
    vuoto = tmp_path / "vuoto.pdf"
    vuoto.write_bytes(b"")
    c = _leggi(lancio, "certificato.json")
    c["file_prodotto"]["percorso"] = str(vuoto)
    _scrivi(lancio, "certificato.json", c)
    _boccia_con(esegui_gate("GATE-PRD-1", lancio, ReteFinta(URL_PRD)), "dimensione 0 byte")
    vuoto.write_bytes(b"pdf di prova")
    _passa(esegui_gate("GATE-PRD-1", lancio, ReteFinta(URL_PRD)))


def test_prd_link_senza_esito_registrato(lancio):
    c = _leggi(lancio, "certificato.json")
    c["link_testati"][0]["codice"] = None
    _scrivi(lancio, "certificato.json", c)
    _boccia_con(esegui_gate("GATE-PRD-1", lancio, ReteFinta(URL_PRD)), "esito non registrato (codice null)")


def test_prd_link_irraggiungibile_alla_riapertura(lancio):
    v = esegui_gate("GATE-PRD-1", lancio, ReteFinta({"https://esempio.test/a": 200}))
    _boccia_con(v, "link morto: https://esempio.test/b risponde irraggiungibile")


def test_prd_link_registrato_diverso_dal_riaperto(lancio):
    v = esegui_gate("GATE-PRD-1", lancio, ReteFinta({"https://esempio.test/a": 200,
                                                     "https://esempio.test/b": 301}))
    _boccia_con(v, "registrato 200 ma riaperto 301")


def test_prd_retroattiva_senza_debito(lancio):
    c = _leggi(lancio, "certificato.json")
    c["debito_collaudo"] = "          "   # passa lo schema (minLength 10), non il gate
    _scrivi(lancio, "certificato.json", c)
    _boccia_con(esegui_gate("GATE-PRD-1", lancio, ReteFinta(URL_PRD)), "retroattiva senza debito_collaudo")


def test_prd_integrale_senza_debito_passa(lancio):
    c = _leggi(lancio, "certificato.json")
    c["modalita"] = "integrale"
    c["debito_collaudo"] = None
    _scrivi(lancio, "certificato.json", c)
    _passa(esegui_gate("GATE-PRD-1", lancio, ReteFinta(URL_PRD)))


def test_prd_esito_non_consegnabile(lancio):
    c = _leggi(lancio, "certificato.json")
    c["esito"] = "non-consegnabile"
    _scrivi(lancio, "certificato.json", c)
    _boccia_con(esegui_gate("GATE-PRD-1", lancio, ReteFinta(URL_PRD)), "'non-consegnabile'")


# ====================================================================== GATE-INT-1

def test_int_passa_e_riapre_il_campione(lancio):
    rete = ReteFinta(URL_INT)
    v = esegui_gate("GATE-INT-1", lancio, rete)
    _passa(v)
    assert sorted(rete.chiamate) == sorted(URL_INT)
    assert v.dati["frasi"] == 15 and v.dati["campione_vivo"] == 3


def test_int_meno_di_15_frasi(lancio):
    r = _leggi(lancio, "ricerca.json")
    r["frasi"] = r["frasi"][:14]
    _scrivi(lancio, "ricerca.json", r)
    _boccia_con(esegui_gate("GATE-INT-1", lancio, ReteFinta(URL_INT)), "schema: frasi")  # lo schema (minItems) precede la clausola


def test_int_frase_senza_url(lancio):
    r = _leggi(lancio, "ricerca.json")
    r["frasi"][3]["fonte"]["url"] = "   "
    _scrivi(lancio, "ricerca.json", r)
    _boccia_con(esegui_gate("GATE-INT-1", lancio, ReteFinta(URL_INT)), "frase 4 senza fonte.url")


def test_int_campione_sotto_i_tre(lancio):
    r = _leggi(lancio, "ricerca.json")
    r["campione_verificato"] = r["campione_verificato"][:2]
    _scrivi(lancio, "ricerca.json", r)
    _boccia_con(esegui_gate("GATE-INT-1", lancio, ReteFinta(URL_INT)), "schema: campione_verificato")


def test_int_campione_dichiarato_non_raggiungibile(lancio):
    r = _leggi(lancio, "ricerca.json")
    r["campione_verificato"][0]["raggiungibile"] = False
    _scrivi(lancio, "ricerca.json", r)
    _boccia_con(esegui_gate("GATE-INT-1", lancio, ReteFinta(URL_INT)), "raggiungibile dichiarato False")


def test_int_campione_morto_alla_riapertura(lancio):
    rete = ReteFinta(dict(URL_INT, **{"https://esempio.test/fonte-2": 404}))
    _boccia_con(esegui_gate("GATE-INT-1", lancio, rete), "fonte-2: irraggiungibile alla riapertura del gate (codice 404)")


def test_int_campione_non_fonte_di_nessuna_frase(lancio):
    r = _leggi(lancio, "ricerca.json")
    r["campione_verificato"][0]["url"] = "https://esempio.test/estranea"
    _scrivi(lancio, "ricerca.json", r)
    rete = ReteFinta(dict(URL_INT, **{"https://esempio.test/estranea": 200}))
    _boccia_con(esegui_gate("GATE-INT-1", lancio, rete), "non e' la fonte di nessuna frase")


def test_int_testo_ritrovato_controllato_sul_corpo(lancio):
    r = _leggi(lancio, "ricerca.json")
    r["campione_verificato"][0]["testo_ritrovato"] = True
    _scrivi(lancio, "ricerca.json", r)
    frase = r["frasi"][0]["testo"]
    con = ReteFinta(dict(URL_INT, **{"https://esempio.test/fonte-1": (200, "<p>%s</p>" % frase.upper())}))
    v = esegui_gate("GATE-INT-1", lancio, con)
    _passa(v)
    assert v.dati["testi_controllati"] == 1
    senza = ReteFinta(dict(URL_INT, **{"https://esempio.test/fonte-1": (200, "<p>altro</p>")}))
    _boccia_con(esegui_gate("GATE-INT-1", lancio, senza), "non contiene nessuna delle")


# ====================================================================== GATE-PRV-1

def test_prv_passa_e_ricalcola(lancio):
    v = esegui_gate("GATE-PRV-1", lancio, ReteFinta())
    _passa(v)
    assert v.dati["ricavo_ricalcolato"] == {"pessimista": 33.5, "atteso": 301.5, "ottimista": 1206.0}


def test_prv_scenario_mancante(lancio):
    p = _leggi(lancio, "previsione.json")
    p["scenari"].pop("ottimista")
    _scrivi(lancio, "previsione.json", p)
    _boccia_con(esegui_gate("GATE-PRV-1", lancio, ReteFinta()), "schema: scenari: 'ottimista' is a required property")


def test_prv_ricavo_non_torna_con_la_formula(lancio):
    p = _leggi(lancio, "previsione.json")
    p["scenari"]["atteso"]["ricavo_lordo"] = 5000
    _scrivi(lancio, "previsione.json", p)
    _boccia_con(esegui_gate("GATE-PRV-1", lancio, ReteFinta()), "scenario atteso: ricavo_lordo dichiarato 5000 ma la formula da' 301.50")


def test_prv_misurato_senza_fonte_anche_se_passa_lo_schema(lancio):
    p = _leggi(lancio, "previsione.json")
    p["assunzioni"][2]["fonte"] = "     "   # minLength 3 soddisfatta, ma e' vuota
    _scrivi(lancio, "previsione.json", p)
    _boccia_con(esegui_gate("GATE-PRV-1", lancio, ReteFinta()), "dichiarata 'misurato' ma senza fonte")


def test_prv_pubblico_diverso_da_art_pub(lancio):
    p = _leggi(lancio, "previsione.json")
    p["ingressi"]["pubblico_raggiungibile"] = 50000
    for s in p["scenari"].values():
        s["ricavo_lordo"] = round(50000 * s["tasso_visita"] * s["tasso_acquisto"] * 67, 2)
    _scrivi(lancio, "previsione.json", p)
    _boccia_con(esegui_gate("GATE-PRV-1", lancio, ReteFinta()), "non coincide con pubblico.json")


def test_prv_prezzo_diverso_dall_offerta(lancio):
    o = _leggi(lancio, "offerta.PROPOSTA.json")
    o["prezzo"] = 97
    _scrivi(lancio, "offerta.PROPOSTA.json", o)
    _boccia_con(esegui_gate("GATE-PRV-1", lancio, ReteFinta()), "non coincide con il prezzo dell'offerta (97)")


def test_prv_valutatore_formule_e_sicuro():
    from scripts.gates.gate_prv_1 import analizza_formula, valuta_prodotto
    assert analizza_formula("ricavo_lordo = a * b × 2.5") == ("ricavo_lordo", ["a", "b", "2.5"], None)
    assert analizza_formula("ricavo_lordo = a + b")[2].startswith("formula: ammesso solo il prodotto")
    assert analizza_formula("ricavo_lordo = __import__('os')")[2]
    assert analizza_formula("x = a * ")[2]
    assert analizza_formula(None)[2]
    assert valuta_prodotto(["a", "b", "2.5"], {"a": 2, "b": 4}) == (20.0, None)
    assert valuta_prodotto(["a", "c"], {"a": 2, "b": 4})[1].startswith("fattore 'c'")
    assert valuta_prodotto(["a"], {"a": True})[1]


# ====================================================================== GATE-OFF-1

def test_off_passa_con_firma_valida(lancio):
    _firma(lancio)
    v = esegui_gate("GATE-OFF-1", lancio, ReteFinta())
    _passa(v)
    assert v.dati["somma_bonus_con_fonte"] == 137 and v.dati["bonus_senza_fonte"] == ["Bonus senza fonte"]
    assert round(v.dati["rapporto_ricalcolato"], 2) == 3.04


def test_off_data_in_formato_gg_mm_aaaa_passa(lancio):
    o = _leggi(lancio, "offerta.PROPOSTA.json")
    o["data_apertura"] = (date.today() + timedelta(days=30)).strftime("%d/%m/%Y")
    _scrivi(lancio, "offerta.PROPOSTA.json", o)
    _firma(lancio)
    _passa(esegui_gate("GATE-OFF-1", lancio, ReteFinta()))


def test_off_solo_proposta_boccia_come_caso_normale(lancio):
    v = esegui_gate("GATE-OFF-1", lancio, ReteFinta())
    _boccia_con(v, "offerta non firmata: esiste solo la proposta")
    assert v.ramo_fallimento == "ISTRUITO" and len(v.dati["proposta_sha256"]) == 64


def test_off_proposta_assente_accanto_alla_firma(lancio):
    _firma(lancio)
    os.remove(os.path.join(lancio, "offerta.PROPOSTA.json"))
    _boccia_con(esegui_gate("GATE-OFF-1", lancio, ReteFinta()), "proposta assente")


def test_off_impronta_non_corrisponde(lancio):
    off = _firma(lancio)
    off["firma"]["proposta_impronta"] = "0" * 64
    _scrivi(lancio, "offerta.json", off)
    _boccia_con(esegui_gate("GATE-OFF-1", lancio, ReteFinta()), "la firma decade")


def test_off_canale_fuori_dalla_lista_del_registro(lancio, monkeypatch):
    from scripts.gates import gate_off_1
    _firma(lancio)
    reg = dict(gates.registro())
    reg["canali_firma_ammessi"] = ["file-fuori-agenti"]
    monkeypatch.setattr(gate_off_1, "registro", lambda: reg)
    _boccia_con(esegui_gate("GATE-OFF-1", lancio, ReteFinta()), "firma.canale 'comando-utente' non e' fra i canali ammessi")


def test_off_prezzo_zero_e_evasivo_per_la_vendita(lancio):
    off = _firma(lancio)
    off["prezzo"] = 0
    _scrivi(lancio, "offerta.json", off)
    v = esegui_gate("GATE-OFF-1", lancio, ReteFinta())
    assert v.passa is False and any("schema: prezzo" in p for p in v.problemi)
    from scripts.gates.gate_off_1 import _evasivo
    assert _evasivo(0, "vendita") and not _evasivo(0, "acquisizione-contatti")
    assert _evasivo("NON LO SO", "vendita") and _evasivo(" da  definire ", "vendita") and _evasivo("tbd", "vendita")
    assert not _evasivo(67, "vendita")


def test_off_data_apertura_passata(lancio):
    o = _leggi(lancio, "offerta.PROPOSTA.json")
    o["data_apertura"] = "2020-01-01"
    _scrivi(lancio, "offerta.PROPOSTA.json", o)
    _firma(lancio)
    _boccia_con(esegui_gate("GATE-OFF-1", lancio, ReteFinta()), "non e' futura")


def test_off_data_apertura_illeggibile(lancio):
    o = _leggi(lancio, "offerta.PROPOSTA.json")
    o["data_apertura"] = "prossimamente"
    _scrivi(lancio, "offerta.PROPOSTA.json", o)
    _firma(lancio)
    _boccia_con(esegui_gate("GATE-OFF-1", lancio, ReteFinta()), "non e' una data valida")


def test_off_durata_carrello_zero(lancio):
    off = _firma(lancio)
    off["durata_carrello_gg"] = 0
    _scrivi(lancio, "offerta.json", off)
    v = esegui_gate("GATE-OFF-1", lancio, ReteFinta())
    _boccia_con(v, "durata_carrello_gg")


def test_off_ruolo_non_ammesso(lancio):
    off = _firma(lancio)
    off["ruolo_prodotto"] = "non-deciso"
    _scrivi(lancio, "offerta.json", off)
    _boccia_con(esegui_gate("GATE-OFF-1", lancio, ReteFinta()), "ruolo_prodotto")


def test_off_rapporto_sotto_soglia_con_bonus_senza_fonte(lancio):
    o = _leggi(lancio, "offerta.PROPOSTA.json")
    for b in o["struttura"]["bonus"]:
        b["fonte_valore"] = None      # tutti i bonus valgono zero: rapporto 1.0
    o["struttura"]["valore_dichiarato"] = 67
    o["struttura"]["rapporto_valore_prezzo"] = 1.0
    _scrivi(lancio, "offerta.PROPOSTA.json", o)
    _firma(lancio)
    v = esegui_gate("GATE-OFF-1", lancio, ReteFinta())
    _boccia_con(v, "rapporto valore/prezzo ricalcolato 1.00 < soglia 3")
    assert v.dati["somma_bonus_con_fonte"] == 0


def test_off_valore_dichiarato_gonfiato_viene_ricalcolato(lancio):
    o = _leggi(lancio, "offerta.PROPOSTA.json")
    o["struttura"]["valore_dichiarato"] = 1203     # conta anche il bonus senza fonte
    o["struttura"]["rapporto_valore_prezzo"] = 17.96
    _scrivi(lancio, "offerta.PROPOSTA.json", o)
    _firma(lancio)
    v = esegui_gate("GATE-OFF-1", lancio, ReteFinta())
    _boccia_con(v, "valore_dichiarato 1203 ma ricalcolato 204.00")
    _boccia_con(v, "rapporto_valore_prezzo 17.96 ma ricalcolato 3.04")


def test_off_soglia_dichiarata_nel_file_vince_sul_default(lancio):
    o = _leggi(lancio, "offerta.PROPOSTA.json")
    o["struttura"]["soglia_rapporto_minima"] = 5
    _scrivi(lancio, "offerta.PROPOSTA.json", o)
    _firma(lancio)
    _boccia_con(esegui_gate("GATE-OFF-1", lancio, ReteFinta()), "< soglia 5")


# ====================================================================== il kit d'esempio

ESEMPIO = os.path.join(gates._comune.ECOSISTEMA, "05-TEMPLATES-E-KIT", "esempio")


def test_kit_esempio_passa_i_cinque_gate_e_off_blocca_perche_non_firmata():
    assert os.path.isdir(ESEMPIO), ESEMPIO
    rete = ReteFinta({"https://example.com/": 200, "https://www.iana.org/domains/reserved": 200,
                      "https://www.python.org/": 200})
    for g in ("GATE-PUB-1", "GATE-STR-1", "GATE-PRD-1", "GATE-INT-1", "GATE-PRV-1"):
        _passa(esegui_gate(g, ESEMPIO, rete))
    _boccia_con(esegui_gate("GATE-OFF-1", ESEMPIO, rete), "offerta non firmata")
