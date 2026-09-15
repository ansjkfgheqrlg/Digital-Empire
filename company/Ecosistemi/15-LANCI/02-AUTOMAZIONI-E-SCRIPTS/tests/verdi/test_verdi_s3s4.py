# -*- coding: utf-8 -*-
"""I test VERDI di S3/S4: per ogni gate un caso che passa sulla fixture coerente e almeno
una clausola bocciata DIVERSA dal test rosso (che sta in tests/rossi/test_rossi_s3s4.py).
Piu' il kit pubblico esempio-s3s4: sette gate passano, REG-1 blocca per via libera assente.
"""
import json
import os
import shutil
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.dirname(QUI)
SCRIPTS_ROOT = os.path.dirname(TESTS)
sys.path.insert(0, SCRIPTS_ROOT)

from scripts.gates import ReteFinta, esegui_gate  # noqa: E402

FIXTURE = os.path.join(TESTS, "fixture", "s3s4")
ESEMPIO = os.path.join(os.path.dirname(SCRIPTS_ROOT), "05-TEMPLATES-E-KIT", "esempio-s3s4")
GATE_S3S4 = ["GATE-CPY-1", "GATE-FNL-1", "GATE-EDT-1", "GATE-TSR-1", "GATE-TSR-2",
             "GATE-REG-1", "GATE-CNS-1", "GATE-MEM-1"]


def _leggi(nome, base=FIXTURE):
    with open(os.path.join(base, *nome.split("/")), encoding="utf-8") as f:
        return json.load(f)


def _scrivi(dir_lancio, nome, dati):
    p = os.path.join(dir_lancio, *nome.split("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


def _lancio(tmp_path):
    d = tmp_path / "lanci" / "prova-s3s4"
    shutil.copytree(FIXTURE, d, ignore=shutil.ignore_patterns("_genera.py", "__pycache__"))
    return str(d)


def _rete_ok(base=FIXTURE):
    return ReteFinta({p["url"]: 200 for p in _leggi("funnel.json", base)["pagine"]})


def _boccia(v, frammento):
    assert v.passa is False
    assert any(frammento in p for p in v.problemi), (frammento, v.problemi)
    assert v.ramo_fallimento, "un gate che boccia deve dire dove torna il lancio"
    return v


# ------------------------------------------------------------------ tutti passano

def test_tutti_gli_otto_gate_passano_sulla_fixture_coerente(tmp_path):
    d = _lancio(tmp_path)
    for g in GATE_S3S4:
        v = esegui_gate(g, d, _rete_ok())
        assert v.passa is True, (g, v.problemi)
        assert v.problemi == [] and v.ramo_fallimento is None
        assert v.dati, "un gate che passa riporta i numeri misurati"


def test_artefatto_assente_e_detto_assente(tmp_path):
    d = _lancio(tmp_path)
    for g, nome in [("GATE-CPY-1", "copy/manifest.json"), ("GATE-FNL-1", "funnel.json"),
                    ("GATE-EDT-1", "editoriale.json"), ("GATE-TSR-1", "budget.json"), ("GATE-TSR-2", "budget.json"),
                    ("GATE-REG-1", "apertura.json"), ("GATE-CNS-1", "consuntivo.json"), ("GATE-MEM-1", "debrief.json")]:
        p = os.path.join(d, *nome.split("/"))
        if os.path.exists(p):
            os.remove(p)
        v = esegui_gate(g, d, _rete_ok())
        assert v.passa is False and v.problemi == ["assente"], (g, v.problemi)


def test_schema_non_passato_elenca_gli_errori_prima_di_tutto(tmp_path):
    d = _lancio(tmp_path)
    b = _leggi("budget.json")
    b["pareggio"]["calcolato_da"] = "a-mano"
    _scrivi(d, "budget.json", b)
    v = esegui_gate("GATE-TSR-1", d, ReteFinta())
    assert v.passa is False and v.problemi[0].startswith("schema: pareggio.calcolato_da")


# ------------------------------------------------------------------ GATE-CPY-1

def test_cpy_1_prova_con_riferimento_non_risolvibile_boccia(tmp_path):
    d = _lancio(tmp_path)
    m = _leggi("copy/manifest.json")
    m["pezzi"][0]["affermazioni"][0]["riferimento"] = "certificato.json#bandiere_rosse[99]"
    _scrivi(d, "copy/manifest.json", m)
    _boccia(esegui_gate("GATE-CPY-1", d, ReteFinta()), "fuori misura")


def test_cpy_1_prova_che_cita_il_testo_stesso_boccia(tmp_path):
    d = _lancio(tmp_path)
    m = _leggi("copy/manifest.json")
    m["pezzi"][0]["affermazioni"][0]["riferimento"] = "copy/pagina-vendita.md#riga-3"
    _scrivi(d, "copy/manifest.json", m)
    _boccia(esegui_gate("GATE-CPY-1", d, ReteFinta()), "il file deve essere uno fra")


def test_cpy_1_file_del_pezzo_mancante_boccia(tmp_path):
    d = _lancio(tmp_path)
    os.remove(os.path.join(d, "copy", "email-1.md"))
    _boccia(esegui_gate("GATE-CPY-1", d, ReteFinta()), "non esiste")


def test_cpy_1_totale_sotto_80_boccia(tmp_path):
    d = _lancio(tmp_path)
    m = _leggi("copy/manifest.json")
    m["punteggio_totale"] = 79
    _scrivi(d, "copy/manifest.json", m)
    _boccia(esegui_gate("GATE-CPY-1", d, ReteFinta()), "sotto la soglia 80")


# ------------------------------------------------------------------ GATE-FNL-1

def test_fnl_1_riapre_le_pagine_e_non_crede_al_codice_salvato(tmp_path):
    d = _lancio(tmp_path)
    fn = _leggi("funnel.json")
    rete = ReteFinta({p["url"]: 200 for p in fn["pagine"]})
    rete.risposte[fn["pagine"][1]["url"]] = 404
    v = _boccia(esegui_gate("GATE-FNL-1", d, rete), "risponde 404")
    assert set(rete.chiamate) == {p["url"] for p in fn["pagine"]}
    assert v.dati["pagine_200"] == 2


def test_fnl_1_url_non_dichiarato_alla_rete_finta_e_irraggiungibile(tmp_path):
    d = _lancio(tmp_path)
    _boccia(esegui_gate("GATE-FNL-1", d, ReteFinta()), "irraggiungibile")


def test_fnl_1_evento_da_registro_server_non_basta(tmp_path):
    d = _lancio(tmp_path)
    fn = _leggi("funnel.json")
    fn["pagine"][2]["evento_conversione"]["prova"]["origine"] = "registro-server"
    _scrivi(d, "funnel.json", fn)
    _boccia(esegui_gate("GATE-FNL-1", d, _rete_ok()), "piattaforma-misura")


def test_fnl_1_incassato_senza_rimborso_non_basta(tmp_path):
    d = _lancio(tmp_path)
    fn = _leggi("funnel.json")
    fn["prova_cassa"]["stato"] = "incassato"
    _scrivi(d, "funnel.json", fn)
    _boccia(esegui_gate("GATE-FNL-1", d, _rete_ok()), "incassato_e_rimborsato")


# ------------------------------------------------------------------ GATE-EDT-1

def test_edt_1_giorno_del_carrello_scoperto_boccia(tmp_path):
    d = _lancio(tmp_path)
    ed = _leggi("editoriale.json")
    tolto = ed["contenuti"].pop(3)
    _scrivi(d, "editoriale.json", ed)
    v = _boccia(esegui_gate("GATE-EDT-1", d, ReteFinta()), "giorno %s del carrello" % tolto["data_uscita"])
    assert v.dati["giorni_scoperti"] == [tolto["data_uscita"]]


def test_edt_1_campo_obbligatorio_vuoto_boccia(tmp_path):
    d = _lancio(tmp_path)
    ed = _leggi("editoriale.json")
    ed["contenuti"][0]["canale"] = ""
    _scrivi(d, "editoriale.json", ed)
    _boccia(esegui_gate("GATE-EDT-1", d, ReteFinta()), "campi obbligatori vuoti: canale")


def test_edt_1_destinazione_per_url_e_per_ruolo_sono_entrambe_risolvibili(tmp_path):
    d = _lancio(tmp_path)
    ed = _leggi("editoriale.json")
    assert {c["destinazione"] for c in ed["contenuti"]} >= {"vendita", "https://esempio.invalid/manuale"}
    assert esegui_gate("GATE-EDT-1", d, ReteFinta()).passa


# ------------------------------------------------------------------ GATE-TSR-1

def test_tsr_1_oltre_tetto_boccia_con_lo_scostamento(tmp_path):
    d = _lancio(tmp_path)
    b = _leggi("budget.json")
    b["tetto"] = 100.0
    _scrivi(d, "budget.json", b)
    _boccia(esegui_gate("GATE-TSR-1", d, ReteFinta()), "oltre il tetto 100.0 (scostamento 165.0)")


def test_tsr_1_pareggio_dichiarato_diverso_dal_ricalcolo_boccia(tmp_path):
    d = _lancio(tmp_path)
    b = _leggi("budget.json")
    b["pareggio"]["copie"] = 2
    _scrivi(d, "budget.json", b)
    v = _boccia(esegui_gate("GATE-TSR-1", d, ReteFinta()), "ricalcolato 6")
    assert v.dati["pareggio_copie_ricalcolato"] == 6


def test_tsr_1_prezzo_di_previsione_diverso_da_offerta_boccia(tmp_path):
    d = _lancio(tmp_path)
    o = _leggi("offerta.json")
    o["prezzo"] = 97.0
    _scrivi(d, "offerta.json", o)
    _boccia(esegui_gate("GATE-TSR-1", d, ReteFinta()), "un'altra offerta")


# ------------------------------------------------------------------ GATE-TSR-2

def test_tsr_2_senza_scarto_corrente_passa_e_lo_dice(tmp_path):
    d = _lancio(tmp_path)
    v = esegui_gate("GATE-TSR-2", d, ReteFinta())
    assert v.passa and v.dati["speso"] == 0.0 and "niente speso ancora" in v.dati["fonte_speso"]


def test_tsr_2_speso_ricalcolato_dalle_voci_non_dal_campo(tmp_path):
    d = _lancio(tmp_path)
    b = _leggi("budget.json")
    b["voci"][0]["stato"] = "speso"                       # 200 di pubblicita' spesi davvero
    b["voci"][0]["importo"] = 300.0                       # ...anzi 300: +13% sul previsto 265
    b["scarto_corrente"] = {"speso": 10.0, "previsto": 265.0, "percentuale": -96.0,
                            "sbloccato_da": None, "sbloccato_il": None}   # il campo mente
    _scrivi(d, "budget.json", b)
    v = _boccia(esegui_gate("GATE-TSR-2", d, ReteFinta()), "oltre il 10%")
    assert v.dati["speso"] == 300.0 and "ricalcolato" in v.dati["fonte_speso"]
    assert v.ramo_fallimento == "DATATO"


def test_tsr_2_scarto_al_10_percento_esatto_passa(tmp_path):
    d = _lancio(tmp_path)
    b = _leggi("budget.json")
    b["scarto_corrente"] = {"speso": round(b["costo_totale_previsto"] * 1.10, 2), "previsto": b["costo_totale_previsto"],
                            "percentuale": 10.0, "sbloccato_da": None, "sbloccato_il": None}
    _scrivi(d, "budget.json", b)
    assert esegui_gate("GATE-TSR-2", d, ReteFinta()).passa


# ------------------------------------------------------------------ GATE-REG-1

def test_reg_1_via_libera_con_chi_vuoto_e_non_dato(tmp_path):
    d = _lancio(tmp_path)
    ap = _leggi("apertura.json")
    ap["via_libera"]["chi"] = ""
    _scrivi(d, "apertura.json", ap)
    _boccia(esegui_gate("GATE-REG-1", d, _rete_ok()), "via libera non dato")


def test_reg_1_canale_fuori_lista_boccia(tmp_path):
    d = _lancio(tmp_path)
    ap = _leggi("apertura.json")
    ap["via_libera"]["canale"] = "comando-utente"
    _scrivi(d, "apertura.json", ap)
    assert esegui_gate("GATE-REG-1", d, _rete_ok()).passa
    # lo schema chiude la lista: un canale inventato cade gia' allo schema, e il gate lo dice
    ap["via_libera"]["canale"] = "scritto-da-un-agente"
    _scrivi(d, "apertura.json", ap)
    v = esegui_gate("GATE-REG-1", d, _rete_ok())
    assert not v.passa and any("via_libera.canale" in p for p in v.problemi)


def test_reg_1_ricalcola_gli_artefatti_a_monte_e_non_crede_al_file(tmp_path):
    d = _lancio(tmp_path)
    pub = _leggi("pubblico.json")
    pub["canali"] = []                                     # minItems 1: non valido
    _scrivi(d, "pubblico.json", pub)
    v = _boccia(esegui_gate("GATE-REG-1", d, _rete_ok()), "pubblico.json non valido")
    assert v.dati["artefatti_validi_ricalcolati"]["pubblico.json"] is False
    os.remove(os.path.join(d, "ricerca.json"))
    _boccia(esegui_gate("GATE-REG-1", d, _rete_ok()), "ricerca.json assente")


# ------------------------------------------------------------------ GATE-CNS-1

def test_cns_1_periodo_che_non_copre_il_carrello_boccia(tmp_path):
    d = _lancio(tmp_path)
    c = _leggi("consuntivo.json")
    c["periodo"]["al"] = "2026-08-07"
    _scrivi(d, "consuntivo.json", c)
    _boccia(esegui_gate("GATE-CNS-1", d, ReteFinta()), "anteriore alla chiusura del carrello 2026-08-09")


def test_cns_1_ordini_incoerenti_col_ricavo_boccia(tmp_path):
    d = _lancio(tmp_path)
    c = _leggi("consuntivo.json")
    c["ordini"]["numero"] = 20                             # 658 / 47 = 14, tolleranza 1
    _scrivi(d, "consuntivo.json", c)
    v = _boccia(esegui_gate("GATE-CNS-1", d, ReteFinta()), "non coerente")
    assert v.dati["ordini_ricalcolati"] == 14


def test_cns_1_un_ordine_di_tolleranza_e_ricavo_zero_sono_legittimi(tmp_path):
    d = _lancio(tmp_path)
    c = _leggi("consuntivo.json")
    c["ordini"]["numero"] = 15
    _scrivi(d, "consuntivo.json", c)
    assert esegui_gate("GATE-CNS-1", d, ReteFinta()).passa
    c["ricavo_lordo"] = 0.0
    c["ordini"] = {"numero": 0, "prezzo_medio": 0.0}
    _scrivi(d, "consuntivo.json", c)
    assert esegui_gate("GATE-CNS-1", d, ReteFinta()).passa


# ------------------------------------------------------------------ GATE-MEM-1

def test_mem_1_scarto_oltre_10_con_causa_scritta_passa(tmp_path):
    d = _lancio(tmp_path)
    c = _leggi("consuntivo.json")
    c["ricavo_lordo"] = 423.0
    c["ordini"]["numero"] = 9
    _scrivi(d, "consuntivo.json", c)
    db = _leggi("debrief.json")
    db["cause"] = [{"voce": v, "causa": "la lista ha aperto meno del previsto: tasso di comodo troppo alto",
                    "cosa_faremmo_di_diverso": "misurare il tasso di apertura su un invio prima della previsione",
                    "misurata": False} for v in ("ricavo_lordo", "ordini")]
    _scrivi(d, "debrief.json", db)
    v = esegui_gate("GATE-MEM-1", d, ReteFinta())
    assert v.passa, v.problemi
    assert v.dati["scarti"]["ricavo_lordo"]["scarto_percentuale"] == -40.0


def test_mem_1_artefatto_di_origine_inesistente_boccia(tmp_path):
    d = _lancio(tmp_path)
    db = _leggi("debrief.json")
    db["schemi"][1]["artefatto_di_origine"] = "sondaggio.json"
    _scrivi(d, "debrief.json", db)
    _boccia(esegui_gate("GATE-MEM-1", d, ReteFinta()), "'sondaggio.json' non esiste")


def test_mem_1_controfirma_vuota_boccia(tmp_path):
    d = _lancio(tmp_path)
    db = _leggi("debrief.json")
    db["controfirma"]["chi"] = "  "
    _scrivi(d, "debrief.json", db)
    _boccia(esegui_gate("GATE-MEM-1", d, ReteFinta()), "controfirma.chi assente")


def test_mem_1_meno_di_tre_schemi_boccia(tmp_path):
    d = _lancio(tmp_path)
    db = _leggi("debrief.json")
    db["schemi"] = db["schemi"][:2]
    _scrivi(d, "debrief.json", db)
    v = esegui_gate("GATE-MEM-1", d, ReteFinta())
    assert not v.passa and any("schemi" in p for p in v.problemi)


# ------------------------------------------------------------------ il kit pubblico

def test_esempio_s3s4_sette_gate_passano_e_reg_1_blocca_per_via_libera():
    assert os.path.isdir(ESEMPIO), ESEMPIO
    rete = _rete_ok(ESEMPIO)
    for g in GATE_S3S4:
        v = esegui_gate(g, ESEMPIO, rete)
        if g == "GATE-REG-1":
            assert not v.passa and any("via libera non dato" in p for p in v.problemi), v.problemi
        else:
            assert v.passa, (g, v.problemi)
    fn = _leggi("funnel.json", ESEMPIO)
    assert fn["prova_cassa"]["riferimento_transazione"] == "ESEMPIO-nessuna-transazione-vera"
    leggimi = open(os.path.join(ESEMPIO, "LEGGIMI.md"), encoding="utf-8").read()
    assert "ReteVera" in leggimi and 1 <= len(leggimi.strip().splitlines()) <= 10
