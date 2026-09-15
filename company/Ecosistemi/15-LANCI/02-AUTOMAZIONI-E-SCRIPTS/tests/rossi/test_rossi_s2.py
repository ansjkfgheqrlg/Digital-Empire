# -*- coding: utf-8 -*-
"""I sei test ROSSI di S2c+S2d (micro-task MT-4GNU, MT-GHZ6), copiati dal campo
`test_rosso` del registro (PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml) e
non inventati (04-COSTRUZIONE.md §7).

Un test rosso e' il caso che il gate DEVE BLOCCARE. Scritto PRIMA del gate:
- fase A: fallisce perche' il modulo non esiste (esegui_gate ritorna 'controllo non
  costruito'... e l'asserzione qui sotto pretende che il gate abbia bocciato PER LA
  RAGIONE GIUSTA, non per assenza);
- fase C: passa perche' il gate esiste e boccia.

Per distinguere le due fasi ogni test asserisce che il problema NON sia 'controllo non
costruito': un gate assente non e' un gate che blocca.
"""
import json
import os
import shutil
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.dirname(QUI)
sys.path.insert(0, os.path.dirname(TESTS))

from scripts.gates import ReteFinta, esegui_gate, sha256_file  # noqa: E402

FIXTURE = os.path.join(TESTS, "fixture", "s2")
ARTEFATTI_BASE = ["pubblico.json", "decisione.json", "certificato.json", "ricerca.json",
                  "previsione.json", "offerta.PROPOSTA.json"]


def _leggi(nome):
    with open(os.path.join(FIXTURE, nome), encoding="utf-8") as f:
        return json.load(f)


def _scrivi(dir_lancio, nome, dati):
    with open(os.path.join(dir_lancio, nome), "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)


def _lancio(tmp_path):
    """Una cartella di lancio con tutti gli artefatti di base validi."""
    d = tmp_path / "lanci" / "prova-s2"
    d.mkdir(parents=True)
    for n in ARTEFATTI_BASE:
        shutil.copy(os.path.join(FIXTURE, n), d / n)
    return str(d)


def _blocca(v):
    """Il gate ha bocciato davvero: non passa, e non per 'controllo non costruito'."""
    assert v.passa is False
    assert not any("controllo non costruito" in p for p in v.problemi), v.problemi
    assert v.problemi, "un gate che boccia deve dire perche'"


# GATE-PUB-1: "un pubblico.json con 3 canali tutti a raggiungibili_verificati=0 deve BLOCCARE"
def test_rosso_pub_1_tre_canali_a_zero(tmp_path):
    d = _lancio(tmp_path)
    pub = _leggi("pubblico.json")
    canale = pub["canali"][0]
    pub["canali"] = []
    for i in range(3):
        c = json.loads(json.dumps(canale))
        c["id"] = "canale-%d" % i
        c["raggiungibili_verificati"] = 0
        pub["canali"].append(c)
    pub["totale_raggiungibile_verificato"] = 0
    _scrivi(d, "pubblico.json", pub)
    _blocca(esegui_gate("GATE-PUB-1", d, ReteFinta()))


# GATE-STR-1: "una decisione con una sola risposta 'no' deve BLOCCARE"
def test_rosso_str_1_una_sola_risposta_no(tmp_path):
    d = _lancio(tmp_path)
    dec = _leggi("decisione.json")
    dec["domande"][2]["risposta"] = "no"
    _scrivi(d, "decisione.json", dec)
    _blocca(esegui_gate("GATE-STR-1", d, ReteFinta()))


# GATE-PRD-1: "un prodotto con un link morto deve BLOCCARE senza intervento umano"
def test_rosso_prd_1_un_link_morto(tmp_path):
    d = _lancio(tmp_path)
    crt = _leggi("certificato.json")
    _scrivi(d, "certificato.json", crt)
    rete = ReteFinta({"https://esempio.test/a": 200, "https://esempio.test/b": 404})
    _blocca(esegui_gate("GATE-PRD-1", d, rete))


# GATE-INT-1: "una ricerca con 20 frasi plausibili e zero fonti raggiungibili deve BLOCCARE"
def test_rosso_int_1_venti_frasi_zero_fonti_raggiungibili(tmp_path):
    d = _lancio(tmp_path)
    ric = _leggi("ricerca.json")
    base = ric["frasi"][0]
    ric["frasi"] = []
    for i in range(20):
        f = json.loads(json.dumps(base))
        f["testo"] = "Frase plausibile numero %d, ben scritta e mai detta da nessuno" % (i + 1)
        f["fonte"]["url"] = "https://inventato.test/thread/%d" % (i + 1)
        ric["frasi"].append(f)
    for i, c in enumerate(ric["campione_verificato"]):
        c["url"] = "https://inventato.test/thread/%d" % (i + 1)
        c["raggiungibile"] = True  # l'analista lo dichiara: il gate non si fida
    _scrivi(d, "ricerca.json", ric)
    _blocca(esegui_gate("GATE-INT-1", d, ReteFinta()))  # nessun url risponde


# GATE-PRV-1: "una previsione con un tasso di conversione dichiarato 'misurato' e senza
# fonte deve BLOCCARE"
def test_rosso_prv_1_tasso_misurato_senza_fonte(tmp_path):
    d = _lancio(tmp_path)
    prv = _leggi("previsione.json")
    for a in prv["assunzioni"]:
        if a["nome"] == "tasso_acquisto_atteso":
            a["stato"] = "misurato"
            a["fonte"] = None
            a["da_dove_viene_se_assunto"] = None
    _scrivi(d, "previsione.json", prv)
    _blocca(esegui_gate("GATE-PRV-1", d, ReteFinta()))


# GATE-OFF-1 (a): "un offerta.json con firma.chi='Max' scritta da un agente e canale non
# ammesso deve BLOCCARE"
def test_rosso_off_1a_firma_scritta_da_un_agente_canale_non_ammesso(tmp_path):
    d = _lancio(tmp_path)
    off = _leggi("offerta.PROPOSTA.json")
    off.pop("_nota", None)
    off["firma"] = {"chi": "Max", "canale": "agente-lan-off-conductor",
                    "riferimento": "auto-riparazione ciclo 3",
                    "proposta_impronta": sha256_file(os.path.join(d, "offerta.PROPOSTA.json")),
                    "il": "2026-09-15T10:00:00+02:00"}
    _scrivi(d, "offerta.json", off)
    _blocca(esegui_gate("GATE-OFF-1", d, ReteFinta()))


# GATE-OFF-1 (b): "una firma valida su una proposta poi rigenerata deve BLOCCARE per hash
# non corrispondente"
def test_rosso_off_1b_proposta_rigenerata_dopo_la_firma(tmp_path):
    d = _lancio(tmp_path)
    off = _leggi("offerta.PROPOSTA.json")
    off.pop("_nota", None)
    off["firma"] = {"chi": "Max", "canale": "comando-utente",
                    "riferimento": "lancio firma prova-s2 --prezzo 67 --data 15/01/2030",
                    "proposta_impronta": sha256_file(os.path.join(d, "offerta.PROPOSTA.json")),
                    "il": "2026-09-15T10:00:00+02:00"}
    _scrivi(d, "offerta.json", off)
    # la proposta viene rigenerata DOPO la firma: cambia un prezzo, l'impronta non torna piu'
    prop = _leggi("offerta.PROPOSTA.json")
    prop["prezzo"] = 97
    _scrivi(d, "offerta.PROPOSTA.json", prop)
    _blocca(esegui_gate("GATE-OFF-1", d, ReteFinta()))
