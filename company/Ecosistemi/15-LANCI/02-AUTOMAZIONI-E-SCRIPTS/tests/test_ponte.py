# -*- coding: utf-8 -*-
"""Prove del ponte (ADR-014). Nessuna prova lancia `claude` davvero: l'esecutore
e' iniettato, e cio' che si verifica e' l'argv, lo stdin, il registro delle
chiamate e il tetto."""
import json
import os
import sys

import pytest

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(QUI))

from scripts import ponte  # noqa: E402
from scripts import stato_lancio as sl  # noqa: E402
from scripts.gates import _comune as gates  # noqa: E402


class EsecutoreFinto:
    def __init__(self, stdout='{"total_cost_usd": 0.093, "result": "ok"}', codice=0):
        self.stdout, self.codice, self.chiamate = stdout, codice, []

    def __call__(self, argv, stdin_testo):
        self.chiamate.append((list(argv), stdin_testo))
        return self.codice, self.stdout


def _righe(d):
    p = os.path.join(str(d), "registro-chiamate.jsonl")
    if not os.path.exists(p):
        return []
    return [json.loads(r) for r in open(p, encoding="utf-8") if r.strip()]


def test_argv_ha_il_modello_esplicito_del_registro_e_il_prompt_va_in_stdin(tmp_path):
    ese = EsecutoreFinto()
    modello_atteso = next(a["modello"] for a in gates.registro()["agenti"] if a["id"] == "lan-gate")
    prompt = "riga 1\nriga 2\nriga 3"
    ponte.invoca("lan-gate", prompt, str(tmp_path), esecutore=ese)
    argv, stdin = ese.chiamate[0]
    assert argv == ["claude", "-p", "--agent", "lan-gate", "--model", modello_atteso,
                    "--output-format", "json"]
    assert modello_atteso.startswith("claude-") and modello_atteso not in ("sonnet", "opus", "haiku")
    assert stdin == prompt  # tutte e tre le righe, da stdin, mai in argv
    assert prompt not in " ".join(argv)


def test_ogni_agente_del_registro_ha_un_modello_esplicito():
    for a in gates.registro()["agenti"]:
        assert ponte.modello_di(a["id"]).startswith("claude-")


def test_esecutore_finto_lascia_una_riga_con_il_costo_letto(tmp_path):
    ese = EsecutoreFinto('{"total_cost_usd": 0.25, "modelUsage": {"%s": {}}}'
                         % ponte.modello_di("lan-pub-censore"))
    risposta = ponte.invoca("lan-pub-censore", "conta", str(tmp_path), esecutore=ese)
    assert risposta["total_cost_usd"] == 0.25
    righe = _righe(tmp_path)
    assert len(righe) == 1
    r = righe[0]
    assert r["esito"] == "ok" and r["total_cost_usd"] == 0.25
    assert r["agente"] == "lan-pub-censore" and r["modello"] == ponte.modello_di("lan-pub-censore")
    assert r["lancio_id"] == tmp_path.name and r["nota"] is None
    assert set(r) == {"il", "lancio_id", "agente", "modello", "durata_s", "total_cost_usd",
                      "esito", "prompt_sha256", "nota"}
    assert ponte.costi(str(tmp_path)) == 0.25


def test_tetto_raggiunto_non_chiama_e_solleva_erroretetto(tmp_path):
    ese = EsecutoreFinto('{"total_cost_usd": 10.0}')
    ponte.invoca("lan-gate", "a", str(tmp_path), esecutore=ese, tetto_usd=15.0)
    ponte.invoca("lan-gate", "b", str(tmp_path), esecutore=ese, tetto_usd=15.0)
    assert ponte.costi(str(tmp_path)) == 20.0
    with pytest.raises(ponte.ErroreTetto):
        ponte.invoca("lan-gate", "c", str(tmp_path), esecutore=ese, tetto_usd=15.0)
    assert len(ese.chiamate) == 2  # la terza NON e' partita
    ultima = _righe(tmp_path)[-1]
    assert ultima["esito"] == "tetto" and ultima["total_cost_usd"] == 0.0
    assert ponte.costi(str(tmp_path)) == 20.0


def test_il_tetto_di_default_e_quello_del_registro():
    assert ponte.tetto_registro() == gates.registro()["ponte"]["tetto_spesa_per_lancio_usd"]


def test_agente_sconosciuto_e_un_errore_chiaro_senza_chiamata(tmp_path):
    ese = EsecutoreFinto()
    with pytest.raises(sl.ErroreLancio):
        ponte.invoca("lan-inventato", "x", str(tmp_path), esecutore=ese)
    assert ese.chiamate == [] and _righe(tmp_path) == []


def test_risposta_non_json_lascia_una_riga_errore(tmp_path):
    ese = EsecutoreFinto(stdout="non json", codice=1)
    with pytest.raises(ponte.ErrorePonte):
        ponte.invoca("lan-gate", "x", str(tmp_path), esecutore=ese)
    r = _righe(tmp_path)[-1]
    assert r["esito"] == "errore" and "non JSON" in r["nota"]


def test_modello_diverso_da_quello_chiesto_finisce_in_nota(tmp_path):
    ese = EsecutoreFinto('{"total_cost_usd": 0.1, "modelUsage": {"claude-sonnet-4-6": {}}}')
    ponte.invoca("lan-gate", "x", str(tmp_path), esecutore=ese)
    assert "diverso" in _righe(tmp_path)[-1]["nota"]


def test_costi_e_una_somma_letta_e_le_righe_rotte_non_azzerano(tmp_path):
    p = tmp_path / "registro-chiamate.jsonl"
    p.write_text('{"total_cost_usd": 1.5}\nriga rotta\n{"total_cost_usd": 0.5}\n', encoding="utf-8")
    assert ponte.costi(str(tmp_path)) == 2.0
    assert ponte.costi(str(tmp_path / "non-esiste")) == 0.0
