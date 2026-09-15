# -*- coding: utf-8 -*-
"""Prove di `avanza` e dei comandi umani (S2b, micro-task MT-3XWC).

I gate veri li costruisce un'altra mano: qui si iniettano gate FINTI tramite
monkeypatch di `gates.esegui_gate` (lo stesso oggetto-modulo che il motore usa),
cosi' le prove sono deterministiche e non dipendono da quali gate esistano gia'.
Un gate finto qui e' legittimo perche' a essere provato e' il MOTORE, non il gate.
"""
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone

import pytest

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(QUI))

from scripts import lancio as cli  # noqa: E402
from scripts import stato_lancio as sl  # noqa: E402
from scripts.gates import _comune as gates  # noqa: E402


@pytest.fixture
def lanci_finti(tmp_path, monkeypatch):
    d = tmp_path / "lanci"
    d.mkdir()
    monkeypatch.setattr(sl, "LANCI", str(d))
    return d


def _nuovo(slug="prova", prodotto="Prova"):
    lancio = sl.Lancio(slug)
    lancio.crea(prodotto)
    return lancio


def _scrivi(lancio, nome, dati):
    p = os.path.join(lancio.dir, *nome.split("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


def _stato(lancio):
    return json.load(open(lancio.path_stato, encoding="utf-8"))


def _aggiorna_stato(lancio, **campi):
    s = _stato(lancio)
    s.update(campi)
    lancio._scrivi_stato(s)


def _file(lancio):
    """Elenco di tutti i file dentro la cartella del lancio (per l'idempotenza)."""
    out = []
    for radice, _, nomi in os.walk(lancio.dir):
        for n in nomi:
            out.append(os.path.relpath(os.path.join(radice, n), lancio.dir))
    return sorted(out)


def _gate_finti(monkeypatch, verdetti):
    """verdetti: {GATE-ID: True | False | [problemi] | None(=non costruito)}.
    Un gate non elencato e' 'non costruito', come nella realta' di oggi."""
    chiamati = []

    def finto(gate_id, dir_lancio, rete=None):
        chiamati.append(gate_id)
        v = verdetti.get(gate_id)
        if v is None:
            return gates.Verdetto(gate=gate_id, passa=False,
                                  problemi=["controllo non costruito: manca scripts/gates/%s.py"
                                            % gates.nome_modulo(gate_id)])
        if v is True:
            return gates.Verdetto(gate=gate_id, passa=True, dati={"finto": True})
        problemi = v if isinstance(v, list) else ["bocciato dal gate finto"]
        return gates.Verdetto(gate=gate_id, passa=False, problemi=problemi)

    monkeypatch.setattr(gates, "esegui_gate", finto)
    return chiamati


def _iso(dt):
    return dt.isoformat(timespec="seconds")


ORA = lambda: datetime.now(timezone.utc)  # noqa: E731


# ------------------------------------------------------------ lock e ingresso

def test_lock_preso_da_1_e_non_scrive_nulla(lanci_finti, capsys):
    lancio = _nuovo()
    prima = _file(lancio)
    with sl.Lock(lancio.path_lock):
        codice = sl.avanza("prova")
        fuori = capsys.readouterr().out
    assert codice == 1
    assert "occupato" in fuori and str(os.getpid()) in fuori and "dal 20" in fuori
    assert _file(lancio) == prima  # nessun verbale, nessuno stato riscritto
    assert _stato(lancio)["stato"] == "IDEA"


def test_lancio_inesistente_da_2(lanci_finti):
    assert sl.avanza("mai-creato") == 2


def test_json_rotto_da_2_e_rinomina_rotto(lanci_finti):
    lancio = _nuovo()
    with open(os.path.join(lancio.dir, "pubblico.json"), "w", encoding="utf-8") as f:
        f.write("{non sono json")
    verbali_prima = sorted(os.listdir(lancio.dir_verbali))
    assert sl.avanza("prova") == 2
    assert not os.path.exists(os.path.join(lancio.dir, "pubblico.json"))
    assert os.path.exists(os.path.join(lancio.dir, "pubblico.json.rotto"))
    assert sorted(os.listdir(lancio.dir_verbali)) == verbali_prima  # nessun'altra scrittura


# --------------------------------------------------------- gate non costruiti

def test_lancio_vuoto_senza_gate_costruiti_da_3_con_verbale_ambiente(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {})  # niente e' costruito
    lancio = _nuovo()
    assert sl.avanza("prova") == 3
    ambiente = [n for n in os.listdir(lancio.dir_verbali) if "ambiente" in n]
    assert len(ambiente) == 1
    corpo = json.load(open(os.path.join(lancio.dir_verbali, ambiente[0]), encoding="utf-8"))
    assert "controllo non costruito" in corpo["problema"]
    assert corpo["gate"] == "GATE-PUB-1"
    assert _stato(lancio)["stato"] == "IDEA"


def test_ambiente_ripetuto_non_crea_un_secondo_verbale(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {})
    lancio = _nuovo()
    assert sl.avanza("prova") == 3
    prima = _file(lancio)
    assert sl.avanza("prova") == 3
    assert _file(lancio) == prima


# ---------------------------------------------------------- transizione vera

def test_gate_che_passano_fanno_la_transizione_idea_valutato(lanci_finti, monkeypatch):
    chiamati = _gate_finti(monkeypatch, {"GATE-PUB-1": True, "GATE-STR-1": True})
    lancio = _nuovo()
    _scrivi(lancio, "pubblico.json", {"schema_version": "1.0.0"})
    _scrivi(lancio, "decisione.json", {"schema_version": "1.0.0"})
    codice = sl.avanza("prova")
    s = _stato(lancio)
    # VALUTATO -> ISTRUITO chiede GATE-PRD-1, che non e' costruito: 3, ma la prima
    # transizione e' fatta e salvata (il 3 "lascia il lavoro fatto e si riprende")
    assert codice == 3
    assert s["stato"] == "VALUTATO"
    assert chiamati[:2] == ["GATE-PUB-1", "GATE-STR-1"]  # nell'ordine elencato
    assert s["storia"][-1]["da"] == "IDEA" and s["storia"][-1]["a"] == "VALUTATO"
    assert s["gate"]["GATE-PUB-1"]["passa"] is True
    assert s["impronte"]["pubblico.json"] == gates.sha256_file(
        os.path.join(lancio.dir, "pubblico.json"))
    assert s["impronte"]["decisione.json"]
    assert s["bloccato_da"] is None
    nomi = os.listdir(lancio.dir_verbali)
    assert any("transizione" in n for n in nomi)
    assert "gate-GATE-PUB-1-t1.json" in nomi and "gate-GATE-STR-1-t1.json" in nomi


def test_gate_che_boccia_da_1_stato_invariato_bloccato_da(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {"GATE-PUB-1": ["nessun pubblico verificato"], "GATE-STR-1": True})
    lancio = _nuovo()
    assert sl.avanza("prova") == 1
    s = _stato(lancio)
    assert s["stato"] == "IDEA"
    assert s["bloccato_da"]["gate"] == "GATE-PUB-1"
    assert s["bloccato_da"]["problemi"] == ["nessun pubblico verificato"]
    assert s["gate"]["GATE-PUB-1"]["passa"] is False
    v = json.load(open(os.path.join(lancio.dir_verbali, "gate-GATE-PUB-1-t1.json"), encoding="utf-8"))
    assert v["passa"] is False and v["tentativo"] == 1 and "impronte_ingresso" in v


def test_ramo_di_fallimento_str_1_porta_in_archiviato(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {"GATE-PUB-1": True, "GATE-STR-1": ["una domanda ha risposto no"]})
    lancio = _nuovo()
    assert sl.avanza("prova") == 1
    s = _stato(lancio)
    assert s["stato"] == "ARCHIVIATO"
    assert s["bloccato_da"]["gate"] == "GATE-STR-1"
    assert s["storia"][-1]["perche"] == "GATE-STR-1 boccia"


# ------------------------------------------------------------- idempotenza

def test_secondo_avanza_identico_non_crea_file_nuovi_e_da_lo_stesso_codice(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {"GATE-PUB-1": ["bocciato"], "GATE-STR-1": True})
    lancio = _nuovo()
    c1 = sl.avanza("prova")
    prima = _file(lancio)
    dal = _stato(lancio)["bloccato_da"]["dal"]
    c2 = sl.avanza("prova")
    assert (c1, c2) == (1, 1)
    assert _file(lancio) == prima
    v = json.load(open(os.path.join(lancio.dir_verbali, "gate-GATE-PUB-1-t1.json"), encoding="utf-8"))
    assert v["tentativo"] == 1 and "ultimo_controllo_il" in v
    assert _stato(lancio)["bloccato_da"]["dal"] == dal  # "da quando" non si azzera


def test_il_tentativo_cresce_solo_se_un_ingresso_cambia(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {"GATE-PUB-1": ["bocciato"], "GATE-STR-1": True})
    lancio = _nuovo()
    _scrivi(lancio, "pubblico.json", {"v": 1})
    sl.avanza("prova")
    sl.avanza("prova")
    assert not os.path.exists(os.path.join(lancio.dir_verbali, "gate-GATE-PUB-1-t2.json"))
    _scrivi(lancio, "pubblico.json", {"v": 2})
    sl.avanza("prova")
    assert os.path.exists(os.path.join(lancio.dir_verbali, "gate-GATE-PUB-1-t2.json"))


def test_a_vuoto_non_scrive_niente(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {"GATE-PUB-1": True, "GATE-STR-1": True})
    lancio = _nuovo()
    prima = _file(lancio)
    stato_prima = open(lancio.path_stato, encoding="utf-8").read()
    codice = sl.avanza("prova", a_vuoto=True)
    assert codice in (0, 3)
    assert _file(lancio) == prima
    assert open(lancio.path_stato, encoding="utf-8").read() == stato_prima
    assert _stato(lancio)["stato"] == "IDEA"


def test_solo_gate_esegue_un_solo_controllo_e_scrive_solo_il_suo_verbale(lanci_finti, monkeypatch):
    chiamati = _gate_finti(monkeypatch, {"GATE-PUB-1": True, "GATE-STR-1": True})
    lancio = _nuovo()
    assert sl.avanza("prova", solo_gate="GATE-STR-1") == 0
    assert chiamati == ["GATE-STR-1"]
    nuovi = [n for n in os.listdir(lancio.dir_verbali) if n.startswith("gate-")]
    assert nuovi == ["gate-GATE-STR-1-t1.json"]
    assert _stato(lancio)["stato"] == "IDEA"  # nessuna transizione


# --------------------------------------------------------- impronte a monte

def test_impronta_cambiata_a_monte_manda_a_valle_in_da_rivedere(lanci_finti, monkeypatch):
    chiamati = _gate_finti(monkeypatch, {"GATE-PUB-1": True, "GATE-STR-1": True})
    lancio = _nuovo()
    _scrivi(lancio, "pubblico.json", {"v": 1})
    _scrivi(lancio, "decisione.json", {"v": 1})
    sl.avanza("prova")  # IDEA -> VALUTATO, impronte di pubblico e decisione salvate
    assert _stato(lancio)["stato"] == "VALUTATO"
    _scrivi(lancio, "pubblico.json", {"v": 2})  # cambia a monte
    chiamati.clear()
    sl.avanza("prova", a_vuoto=True)
    # decisione dipende da pubblico: entrambi si rivedono, e i loro gate si rieseguono
    assert chiamati[:2] == ["GATE-PUB-1", "GATE-STR-1"]
    sl.avanza("prova")
    s = _stato(lancio)
    assert "decisione.json" not in s["da_rivedere"]  # ripassati -> tolti
    assert s["impronte"]["pubblico.json"] == gates.sha256_file(os.path.join(lancio.dir, "pubblico.json"))


def test_da_rivedere_che_boccia_blocca_senza_cambiare_stato(lanci_finti, monkeypatch):
    verdetti = {"GATE-PUB-1": True, "GATE-STR-1": True}
    _gate_finti(monkeypatch, verdetti)
    lancio = _nuovo()
    _scrivi(lancio, "pubblico.json", {"v": 1})
    _scrivi(lancio, "decisione.json", {"v": 1})
    sl.avanza("prova")
    _scrivi(lancio, "pubblico.json", {"v": 2})
    verdetti["GATE-STR-1"] = ["la decisione non regge piu'"]
    assert sl.avanza("prova") == 1
    s = _stato(lancio)
    assert s["stato"] == "VALUTATO"
    assert "decisione.json" in s["da_rivedere"]
    assert s["bloccato_da"]["gate"] == "GATE-STR-1"


# -------------------------------------------------- transizioni con persona

def test_gate_off_1_che_boccia_apre_pu_prezzo_con_comando_eseguibile(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {"GATE-OFF-1": ["firma assente"]})
    lancio = _nuovo()
    _aggiorna_stato(lancio, stato="ISTRUITO")
    assert sl.avanza("prova") == 1
    s = _stato(lancio)
    assert s["stato"] == "ISTRUITO"
    aperti = {p["id"]: p for p in s["punti_umani_aperti"]}
    assert "PU-PREZZO" in aperti
    assert aperti["PU-PREZZO"]["come_si_esce"] == "lancio firma prova --prezzo N --data gg/mm/aaaa"
    assert aperti["PU-PREZZO"]["scadenza_il"] is not None  # 14 giorni dal registro


def test_pronto_senza_via_libera_apre_pu_apertura_e_ritorna_0(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {})
    lancio = _nuovo()
    _aggiorna_stato(lancio, stato="PRONTO")
    assert sl.avanza("prova") == 0
    s = _stato(lancio)
    assert s["stato"] == "PRONTO"
    p = s["punti_umani_aperti"][0]
    assert p["id"] == "PU-APERTURA" and p["scadenza_il"] is None
    assert p["come_si_esce"] == "lancio via-libera prova"


def test_pronto_con_via_libera_apre_e_chiude_alla_data(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {})
    lancio = _nuovo()
    _aggiorna_stato(lancio, stato="PRONTO")
    _scrivi(lancio, "apertura.json", {"schema_version": "1.0.0"})
    lancio.via_libera(chi="Max")
    _scrivi(lancio, "offerta.json", {"data_chiusura": (date.today() + timedelta(days=3)).isoformat()})
    assert sl.avanza("prova") == 0
    assert _stato(lancio)["stato"] == "APERTO"
    _scrivi(lancio, "offerta.json", {"data_chiusura": date.today().isoformat()})
    # CHIUSO -> APPRESO chiede GATE-CNS-1, non costruito: 3, ma la chiusura e' fatta
    assert sl.avanza("prova") == 3
    s = _stato(lancio)
    assert s["stato"] == "CHIUSO"
    assert s["storia"][-1]["perche"] == "data di chiusura raggiunta"


# ---------------------------------------------------------- punti umani

def test_punto_umano_scaduto_senza_default_porta_in_sospeso(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {})
    lancio = _nuovo()
    ieri = _iso(ORA() - timedelta(days=1))
    _aggiorna_stato(lancio, stato="ISTRUITO", punti_umani_aperti=[
        {"id": "PU-PREZZO", "aperto_il": _iso(ORA() - timedelta(days=15)), "scadenza_il": ieri,
         "domanda": "Confermi?", "come_si_esce": "lancio firma prova --prezzo N --data gg/mm/aaaa"}])
    assert sl.avanza("prova") == 1
    s = _stato(lancio)
    assert s["stato"] == "SOSPESO"
    sp = s["sospensione"]
    assert sp["stato_di_partenza"] == "ISTRUITO"
    assert sp["orologi_congelati"] == {"PU-PREZZO": ieri}
    assert sp["come_si_esce"] == "lancio riprendi prova"
    rev = datetime.fromisoformat(sp["revisione_il"])
    assert (rev.date() - date.today()).days in (6, 7)
    assert any("sospensione" in n for n in os.listdir(lancio.dir_verbali))


def test_punto_umano_scaduto_con_default_applica_il_default_alla_proposta(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {"GATE-OFF-1": ["firma assente"]})
    lancio = _nuovo()
    _scrivi(lancio, "offerta.PROPOSTA.json", {"schema_version": "1.0.0", "prezzo": 47})
    _aggiorna_stato(lancio, stato="ISTRUITO", punti_umani_aperti=[
        {"id": "PU-RUOLO", "aperto_il": _iso(ORA() - timedelta(days=8)),
         "scadenza_il": _iso(ORA() - timedelta(days=1)), "domanda": "?", "come_si_esce": "x"}])
    sl.avanza("prova")
    prop = json.load(open(os.path.join(lancio.dir, "offerta.PROPOSTA.json"), encoding="utf-8"))
    assert prop["ruolo_prodotto"] == "vendita"
    assert prop["ruolo_scelto_per_silenzio"] is True
    assert prop["ruolo_revisione_il"]
    s = _stato(lancio)
    assert "PU-RUOLO" not in [p["id"] for p in s["punti_umani_aperti"]]
    assert s["stato"] == "ISTRUITO"  # nessuna sospensione: c'era un default


def test_punto_umano_si_chiude_quando_la_causa_sparisce(lanci_finti, monkeypatch):
    _gate_finti(monkeypatch, {"GATE-OFF-1": True})
    lancio = _nuovo()
    _scrivi(lancio, "offerta.PROPOSTA.json", {"schema_version": "1.0.0", "durata_carrello_gg": 5})
    _aggiorna_stato(lancio, stato="ISTRUITO", punti_umani_aperti=[
        {"id": "PU-PREZZO", "aperto_il": _iso(ORA()), "scadenza_il": _iso(ORA() + timedelta(days=14)),
         "domanda": "?", "come_si_esce": "x"}])
    lancio.firma(47, date.today() + timedelta(days=10), chi="Max")
    assert sl.avanza("prova") == 3  # DATATO -> IN_PRODUZIONE chiede GATE-TSR-1, non costruito
    s = _stato(lancio)
    assert s["stato"] == "DATATO"
    assert s["punti_umani_aperti"] == []


# ------------------------------------------------------ sospendi / riprendi

def test_sospendi_e_riprendi_congelano_e_ripristinano_gli_orologi(lanci_finti):
    lancio = _nuovo()
    scadenza = ORA() + timedelta(days=5)
    _aggiorna_stato(lancio, stato="ISTRUITO", punti_umani_aperti=[
        {"id": "PU-PREZZO", "aperto_il": _iso(ORA()), "scadenza_il": _iso(scadenza),
         "domanda": "?", "come_si_esce": "x"}])
    lancio.sospendi("aspettiamo il listino", date.today() + timedelta(days=30))
    s = _stato(lancio)
    assert s["stato"] == "SOSPESO" and s["stato_di_partenza"] == "ISTRUITO"
    assert s["sospensione"]["orologi_congelati"]["PU-PREZZO"] == _iso(scadenza)
    assert s["sospensione"]["motivo"] == "aspettiamo il listino"
    assert sl.avanza("prova") == 1  # sospeso: avanza non fa niente e lo dice
    lancio.riprendi()
    s = _stato(lancio)
    assert s["stato"] == "ISTRUITO" and s["sospensione"] is None and s["stato_di_partenza"] is None
    nuova = datetime.fromisoformat(s["punti_umani_aperti"][0]["scadenza_il"])
    residuo = nuova - ORA()
    assert timedelta(days=4, hours=23) < residuo <= timedelta(days=5, seconds=5)
    nomi = os.listdir(lancio.dir_verbali)
    assert any("sospensione" in n for n in nomi) and any("ripresa" in n for n in nomi)


def test_riprendi_senza_sospensione_e_un_errore_chiaro(lanci_finti):
    lancio = _nuovo()
    with pytest.raises(sl.ErroreLancio):
        lancio.riprendi()


def test_abbandona_porta_in_abortito_e_dice_cosa_si_salva(lanci_finti):
    lancio = _nuovo()
    _scrivi(lancio, "pubblico.json", {
        "schema_version": "1.0.0", "lancio_id": "prova", "misurato_il": "2026-09-10T12:00:00+02:00",
        "canali": [{"id": "c", "tipo": "lista-email", "posseduto": True, "raggiungibili_verificati": 0,
                    "prova": {"tipo": "nessuna", "riferimento": "x", "data": "2026-09-10"}}],
        "totale_raggiungibile_verificato": 0})
    _scrivi(lancio, "decisione.json", {"non": "valido"})
    lancio.abbandona("non c'e' pubblico")
    s = _stato(lancio)
    assert s["stato"] == "ABORTITO"
    abbandono = [n for n in os.listdir(lancio.dir_verbali) if "abbandono" in n]
    corpo = json.load(open(os.path.join(lancio.dir_verbali, abbandono[0]), encoding="utf-8"))
    assert corpo["si_salva"] == ["pubblico.json"]
    assert sl.avanza("prova") == 0  # stato finale: niente da fare, niente da scrivere


# ---------------------------------------------------------------- firma

def test_firma_senza_proposta_da_2(lanci_finti):
    _nuovo()
    assert cli.main(["firma", "prova", "--prezzo", "47", "--data", "01/01/2030"]) == 2


def test_firma_valida_scrive_offerta_con_impronta_della_proposta(lanci_finti):
    lancio = _nuovo()
    _scrivi(lancio, "offerta.PROPOSTA.json", {"schema_version": "1.0.0", "lancio_id": "x",
                                              "prezzo": 37, "durata_carrello_gg": 7, "valuta": "EUR"})
    p_prop = os.path.join(lancio.dir, "offerta.PROPOSTA.json")
    sha_prima = gates.sha256_file(p_prop)
    assert cli.main(["firma", "prova", "--prezzo", "47", "--data", "01/03/2030", "--chi", "Max",
                     "--ruolo", "vendita"]) == 0
    off = json.load(open(os.path.join(lancio.dir, "offerta.json"), encoding="utf-8"))
    assert off["prezzo"] == 47 and off["lancio_id"] == "prova"
    assert off["data_apertura"] == "2030-03-01" and off["data_chiusura"] == "2030-03-08"
    assert off["durata_carrello_gg"] == 7 and off["ruolo_prodotto"] == "vendita"
    assert off["firma"]["chi"] == "Max" and off["firma"]["canale"] == "comando-utente"
    assert off["firma"]["riferimento"] == "lancio firma"
    assert off["firma"]["proposta_impronta"] == sha_prima
    assert gates.sha256_file(p_prop) == sha_prima  # la PROPOSTA non si tocca
    assert any("firma" in n for n in os.listdir(lancio.dir_verbali))


def test_firma_rifiuta_prezzo_zero_e_date_passate(lanci_finti):
    lancio = _nuovo()
    _scrivi(lancio, "offerta.PROPOSTA.json", {"durata_carrello_gg": 7})
    assert cli.main(["firma", "prova", "--prezzo", "0", "--data", "01/01/2030"]) == 2
    assert cli.main(["firma", "prova", "--prezzo", "47", "--data", "01/01/2020"]) == 2
    assert cli.main(["firma", "prova", "--prezzo", "47", "--data", "2030-01-01"]) == 2
    assert not os.path.exists(os.path.join(lancio.dir, "offerta.json"))


def test_via_libera_senza_apertura_da_2(lanci_finti):
    lancio = _nuovo()
    assert cli.main(["via-libera", "prova"]) == 2
    _scrivi(lancio, "apertura.json", {"schema_version": "1.0.0"})
    assert cli.main(["via-libera", "prova", "--chi", "Max"]) == 0
    ape = json.load(open(os.path.join(lancio.dir, "apertura.json"), encoding="utf-8"))
    assert ape["via_libera"]["chi"] == "Max" and ape["via_libera"]["canale"] == "comando-utente"


# ---------------------------------------------------------------- comando

def test_comando_avanza_espone_il_codice_del_motore(lanci_finti, monkeypatch, capsys):
    _gate_finti(monkeypatch, {"GATE-PUB-1": ["bocciato"], "GATE-STR-1": True})
    _nuovo()
    assert cli.main(["avanza", "prova"]) == 1
    assert "bloccato" in capsys.readouterr().out
    assert cli.main(["avanza", "prova", "--a-vuoto"]) == 1


def test_stato_mostra_bloccato_da_e_punti_umani(lanci_finti, monkeypatch, capsys):
    _gate_finti(monkeypatch, {"GATE-OFF-1": ["firma assente"]})
    lancio = _nuovo()
    _aggiorna_stato(lancio, stato="ISTRUITO")
    sl.avanza("prova")
    capsys.readouterr()
    assert cli.main(["stato", "prova"]) == 0
    fuori = capsys.readouterr().out
    assert "bloccato da: GATE-OFF-1" in fuori
    assert "PU-PREZZO" in fuori and "lancio firma prova" in fuori


def test_crea_con_esempio_senza_cartella_crea_vuoto_e_da_0(lanci_finti, monkeypatch, capsys):
    monkeypatch.setattr(cli, "ESEMPIO", str(lanci_finti / "non-esiste"))
    assert cli.main(["crea", "prova", "--prodotto", "Prova", "--con-esempio"]) == 0
    assert "non c'e'" in capsys.readouterr().out
    assert sl.Lancio("prova").artefatti_presenti() == {}


def test_crea_con_esempio_copia_e_riscrive_lancio_id(lanci_finti, monkeypatch, tmp_path):
    esempio = tmp_path / "esempio"
    (esempio / "copy").mkdir(parents=True)
    (esempio / "pubblico.json").write_text('{"lancio_id": "esempio", "x": 1}', encoding="utf-8")
    (esempio / "copy" / "manifest.json").write_text('{"lancio_id": "esempio"}', encoding="utf-8")
    (esempio / "LEGGIMI.md").write_text("ciao", encoding="utf-8")
    (esempio / "stato.json").write_text('{"stato": "APPRESO"}', encoding="utf-8")
    monkeypatch.setattr(cli, "ESEMPIO", str(esempio))
    assert cli.main(["crea", "nuovo", "--prodotto", "Nuovo", "--con-esempio"]) == 0
    lancio = sl.Lancio("nuovo")
    assert json.load(open(os.path.join(lancio.dir, "pubblico.json"), encoding="utf-8"))["lancio_id"] == "nuovo"
    assert json.load(open(os.path.join(lancio.dir, "copy", "manifest.json"), encoding="utf-8"))["lancio_id"] == "nuovo"
    assert _stato(lancio)["stato"] == "IDEA"  # lo stato.json dell'esempio NON sovrascrive


# ------------------------------------------------------ tabella vs registro

def test_tabella_transizioni_coerente_col_registro():
    """La tabella nel motore e' un dict: questo test e' cio' che le impedisce di
    divergere in silenzio dal registro (fonte di verita')."""
    reg = gates.registro()
    trans = {(t["da"], t["a"]): t for t in reg["transizioni"]}
    id_gate = {g["id"] for g in reg["gate"]}
    file_di = {a["id"]: a["file"] for a in reg["artefatti"]}
    presidia = {g["id"]: file_di[g["presidia"]] for g in reg["gate"]}

    def a_monte_di(nome):
        return sl.dipendenze_di_file(nome)

    for da, t in sl.TRANSIZIONI_SISTEMA.items():
        chiave = (da, t["a"])
        assert chiave in trans, "transizione %s -> %s non nel registro" % chiave
        assert trans[chiave]["autorizza"] == "sistema"
        cond = trans[chiave]["condizione"]
        citati = [g for g in id_gate if g in cond]
        # ogni gate citato dal registro sta nel dict, e l'ultimo del dict e' citato
        for g in citati:
            assert g in t["gate"], "%s citato dal registro ma non nel motore per %s" % (g, chiave)
        assert t["gate"][-1] in citati
        # ogni gate del dict o e' citato, o presidia un ingresso (a monte) di uno citato
        for g in t["gate"]:
            assert g in id_gate
            if g in cond:
                continue
            a_monte = set()
            for c in citati:
                coda = [presidia[c]]
                while coda:
                    f = coda.pop()
                    for d in a_monte_di(f):
                        if d not in a_monte:
                            a_monte.add(d)
                            coda.append(d)
            assert presidia[g] in a_monte, "%s non e' ne' citato ne' a monte in %s" % (g, chiave)

    for (da, g), a in sl.RAMI_FALLIMENTO.items():
        assert (da, a) in trans, "ramo %s -> %s non nel registro" % (da, a)
        assert g in trans[(da, a)]["condizione"] and "boccia" in trans[(da, a)]["condizione"]

    for da, t in sl.TRANSIZIONI_PERSONA.items():
        assert trans[(da, t["a"])]["autorizza"] == "persona"
        for g in t["gate"]:
            assert g in trans[(da, t["a"])]["condizione"]
        if t["punto_umano"]:
            assert sl.voce_punto_umano(t["punto_umano"]) is not None

    for g, pu in sl.PUNTO_UMANO_DEL_GATE.items():
        assert g in id_gate and sl.voce_punto_umano(pu) is not None
    for stato, lista in sl.GATE_CONTINUI.items():
        for g in lista:
            assert gates.voce_gate(g).get("tipo") == "continuo"
