# -*- coding: utf-8 -*-
"""I test ROSSI di S3/S4 (micro-task MT-GEKH, MT-69CE), copiati dal campo `test_rosso`
del registro (PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml), non inventati
(04-COSTRUZIONE.md §7). Nove casi per otto gate: GATE-MEM-1 ne dichiara due.

Un test rosso e' il caso che il gate DEVE BLOCCARE. Scritto PRIMA del gate:
- fase A: fallisce perche' il modulo non esiste (esegui_gate ritorna 'controllo non
  costruito', e qui si pretende che il gate abbia bocciato PER LA RAGIONE GIUSTA);
- fase C: passa perche' il gate esiste e boccia.

Annotazione di fase A (2026-09-15): 9 su 9 fallivano con 'controllo non costruito'.
"""
import json
import os
import shutil
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.dirname(QUI)
sys.path.insert(0, os.path.dirname(TESTS))

from scripts.gates import ReteFinta, esegui_gate  # noqa: E402

FIXTURE = os.path.join(TESTS, "fixture", "s3s4")


def _leggi(nome):
    with open(os.path.join(FIXTURE, *nome.split("/")), encoding="utf-8") as f:
        return json.load(f)


def _scrivi(dir_lancio, nome, dati):
    p = os.path.join(dir_lancio, *nome.split("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


def _lancio(tmp_path):
    """Una cartella di lancio con TUTTI gli artefatti della fixture (validi e coerenti)."""
    d = tmp_path / "lanci" / "prova-s3s4"
    shutil.copytree(FIXTURE, d, ignore=shutil.ignore_patterns("_genera.py", "__pycache__"))
    return str(d)


def _rete_ok():
    """Tutte le pagine del funnel della fixture rispondono 200."""
    return ReteFinta({p["url"]: 200 for p in _leggi("funnel.json")["pagine"]})


def _blocca(v):
    """Il gate ha bocciato davvero: non passa, e non per 'controllo non costruito'."""
    assert v.passa is False
    assert not any("controllo non costruito" in p for p in v.problemi), v.problemi
    assert v.problemi, "un gate che boccia deve dire perche'"
    return v


# GATE-CPY-1: "un testo con punteggio 85 ma un blocco al 30% dei suoi punti deve BLOCCARE"
def test_rosso_cpy_1_punteggio_85_ma_un_blocco_al_30_percento(tmp_path):
    d = _lancio(tmp_path)
    m = _leggi("copy/manifest.json")
    m["punteggio_totale"] = 85
    m["pezzi"][0]["punteggio"]["blocchi"][1] = {"nome": "promessa", "punti": 9, "punti_massimi": 30,
                                                "assegnato_da": "giudice", "ancora": None}
    _scrivi(d, "copy/manifest.json", m)
    v = _blocca(esegui_gate("GATE-CPY-1", d, ReteFinta()))
    assert any("30" in p or "promessa" in p for p in v.problemi), v.problemi


# GATE-FNL-1: "un funnel con tutte le pagine a 200 ma senza transazione di prova deve BLOCCARE"
def test_rosso_fnl_1_pagine_a_200_ma_senza_transazione_di_prova(tmp_path):
    d = _lancio(tmp_path)
    fn = _leggi("funnel.json")
    fn["prova_cassa"] = {"stato": "incassato", "fornitore": "fornitore-di-esempio",
                         "riferimento_transazione": None, "importo": None, "eseguita_il": None,
                         "consegna_verificata": None}
    _scrivi(d, "funnel.json", fn)
    _blocca(esegui_gate("GATE-FNL-1", d, _rete_ok()))


# GATE-EDT-1: "un piano con un contenuto che punta a una pagina inesistente deve BLOCCARE"
def test_rosso_edt_1_contenuto_verso_pagina_inesistente(tmp_path):
    d = _lancio(tmp_path)
    ed = _leggi("editoriale.json")
    ed["contenuti"][2]["destinazione"] = "pagina-che-non-esiste"
    _scrivi(d, "editoriale.json", ed)
    v = _blocca(esegui_gate("GATE-EDT-1", d, ReteFinta()))
    assert any("pagina-che-non-esiste" in p for p in v.problemi), v.problemi


# GATE-TSR-1: "un budget senza costo_macchina_previsto deve BLOCCARE"
def test_rosso_tsr_1_budget_senza_costo_macchina(tmp_path):
    d = _lancio(tmp_path)
    b = _leggi("budget.json")
    del b["costo_macchina_previsto"]
    _scrivi(d, "budget.json", b)
    v = _blocca(esegui_gate("GATE-TSR-1", d, ReteFinta()))
    assert any("costo_macchina_previsto" in p for p in v.problemi), v.problemi


# GATE-TSR-2: "uno scarto dell'11% deve bloccare la spesa nuova e NON uccidere il lancio"
# = verdetto passa False, ramo_fallimento DATATO (un passo indietro, non ABORTITO), scarto 11 nei dati.
def test_rosso_tsr_2_scarto_11_percento_blocca_la_spesa_senza_uccidere_il_lancio(tmp_path):
    d = _lancio(tmp_path)
    b = _leggi("budget.json")
    previsto = b["costo_totale_previsto"]
    b["scarto_corrente"] = {"speso": round(previsto * 1.11, 2), "previsto": previsto, "percentuale": 11.0,
                            "sbloccato_da": None, "sbloccato_il": None}
    _scrivi(d, "budget.json", b)
    v = _blocca(esegui_gate("GATE-TSR-2", d, ReteFinta()))
    assert v.ramo_fallimento == "DATATO", v.ramo_fallimento
    assert v.ramo_fallimento != "ABORTITO"
    assert abs(v.dati["scarto_percentuale"] - 11.0) < 0.05, v.dati


# GATE-REG-1: "una lista con nove voci vere e una falsa deve BLOCCARE"
def test_rosso_reg_1_nove_voci_vere_e_una_falsa(tmp_path):
    d = _lancio(tmp_path)
    ap = _leggi("apertura.json")
    assert len(ap["lista_sincronizzazione"]) == 10
    ap["lista_sincronizzazione"][7]["esito"] = False
    _scrivi(d, "apertura.json", ap)
    v = _blocca(esegui_gate("GATE-REG-1", d, _rete_ok()))
    assert any(ap["lista_sincronizzazione"][7]["voce"] in p for p in v.problemi), v.problemi


# GATE-CNS-1: "un consuntivo con ricavo dichiarato a mano e origine assente deve BLOCCARE"
def test_rosso_cns_1_ricavo_a_mano_e_origine_assente(tmp_path):
    d = _lancio(tmp_path)
    c = _leggi("consuntivo.json")
    del c["origine"]
    c["ricavo_lordo"] = 999.0
    _scrivi(d, "consuntivo.json", c)
    v = _blocca(esegui_gate("GATE-CNS-1", d, ReteFinta()))
    assert any("origine" in p for p in v.problemi), v.problemi


# GATE-MEM-1 (a): "un debrief con tre schemi generici e uno scarto del 40% senza causa deve BLOCCARE"
def test_rosso_mem_1a_scarto_40_percento_senza_causa(tmp_path):
    d = _lancio(tmp_path)
    c = _leggi("consuntivo.json")
    prev = _leggi("previsione.json")["scenari"]["atteso"]["ricavo_lordo"]
    c["ricavo_lordo"] = round(prev * 0.6, 2)                       # -40% rispetto all'atteso
    c["ordini"]["numero"] = int(round(c["ricavo_lordo"] / c["ordini"]["prezzo_medio"]))
    _scrivi(d, "consuntivo.json", c)
    db = _leggi("debrief.json")
    db["cause"] = []
    db["schemi"] = [{"testo": "Schema generico numero %d senza un contenuto vero" % i, "forza": "osservazione",
                     "si_applica_quando": "sempre, per ogni lancio", "conferme": 0, "smentite": 0}
                    for i in range(3)]
    _scrivi(d, "debrief.json", db)
    v = _blocca(esegui_gate("GATE-MEM-1", d, ReteFinta()))
    assert any("ricavo_lordo" in p and "causa" in p for p in v.problemi), v.problemi


# GATE-MEM-1 (b): "un record di memoria con corpo 'ok' e fonti vuote deve BLOCCARE"
def test_rosso_mem_1b_record_con_corpo_ok_e_fonti_vuote(tmp_path):
    d = _lancio(tmp_path)
    db = _leggi("debrief.json")
    db["schemi"][0] = {"testo": "ok", "forza": "regola", "si_applica_quando": "", "conferme": 0, "smentite": 0,
                       "artefatto_di_origine": ""}
    _scrivi(d, "debrief.json", db)
    _blocca(esegui_gate("GATE-MEM-1", d, ReteFinta()))
