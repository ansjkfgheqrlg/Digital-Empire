# -*- coding: utf-8 -*-
"""Prove di `verifica_agenti.py` (S6, ecosistema 15-LANCI).

PERCHE' ESISTONO. Lo script esiste per impedire che un file `.claude/agents/lan-*.md` diverga in
silenzio dal registro. Due prove: che i 15 file veri, cosi' come sono stati scritti, passino
davvero (altrimenti lo script grida al lupo su un ecosistema sano); e che un frontmatter con un
campo inventato venga scartato (altrimenti lo script non protegge da esattamente il difetto per
cui esiste, descritto in `.claude/agents/emperator.md` SS6.6).
"""
import os
import sys

import pytest

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(QUI))

from scripts import verifica_agenti as va  # noqa: E402


# --------------------------------------------------------------- i file veri

def test_tutti_gli_agenti_reali_sono_ok():
    reg = va.carica_registro()
    mappa = {a["id"]: a["file"] for a in reg["artefatti"]}
    falliti = []
    for agente in reg["agenti"]:
        ok, problemi = va.verifica_agente(agente, mappa)
        if not ok:
            falliti.append((agente["id"], problemi))
    assert not falliti, "agenti non conformi: %r" % falliti


def test_main_esce_zero_sui_file_veri(capsys):
    assert va.main() == 0
    out = capsys.readouterr().out
    assert "15/15 agenti ok" in out


def test_il_nucleo_minimo_e_tutto_presente():
    """INV-07 visto dal lato file: ogni produttore di ogni artefatto ha un file .md."""
    reg = va.carica_registro()
    produttori = {a["produttore"] for a in reg["artefatti"]}
    id_agenti = {a["id"] for a in reg["agenti"]}
    assert produttori <= id_agenti
    for id_ in id_agenti:
        assert os.path.exists(os.path.join(va.AG, id_ + ".md"))


# ------------------------------------------------------------ frontmatter finto

FRONTMATTER_PULITO = """---
name: lan-finto
description: "Agente finto usato solo per le prove di verifica_agenti.py."
model: claude-sonnet-5
color: blue
tools: [Read, Write]
---

# lan-finto

Corpo che cita pubblico.json come artefatto prodotto, per la prova INV-22.
"""

AGENTE_FINTO = {
    "id": "lan-finto",
    "modello": "claude-sonnet-5",
    "tools": ["Read", "Write"],
    "produce": ["ART-PUB"],
}

MAPPA_FINTA = {"ART-PUB": "pubblico.json"}


def _scrivi(tmp_path, contenuto, nome="lan-finto.md"):
    p = tmp_path / nome
    p.write_text(contenuto, encoding="utf-8")
    return p


def test_frontmatter_pulito_passa(tmp_path, monkeypatch):
    monkeypatch.setattr(va, "AG", str(tmp_path))
    _scrivi(tmp_path, FRONTMATTER_PULITO)
    ok, problemi = va.verifica_agente(AGENTE_FINTO, MAPPA_FINTA)
    assert ok, problemi


def test_campo_inventato_fa_scartare_lagente(tmp_path, monkeypatch):
    """Il caso costruito apposta: un campo che l'agente reale non dichiarerebbe mai
    (`agent_id`, come nell'esempio di emperator.md SS6.6). Deve dare NO."""
    monkeypatch.setattr(va, "AG", str(tmp_path))
    sporco = FRONTMATTER_PULITO.replace(
        "tools: [Read, Write]\n---",
        "tools: [Read, Write]\nagent_id: \"XYZ-001\"\n---",
    )
    _scrivi(tmp_path, sporco)
    ok, problemi = va.verifica_agente(AGENTE_FINTO, MAPPA_FINTA)
    assert not ok
    assert any("non ammessi" in p for p in problemi)


def test_name_diverso_dallid_viene_scartato(tmp_path, monkeypatch):
    monkeypatch.setattr(va, "AG", str(tmp_path))
    sporco = FRONTMATTER_PULITO.replace("name: lan-finto", "name: lan-altro-nome")
    _scrivi(tmp_path, sporco)
    ok, problemi = va.verifica_agente(AGENTE_FINTO, MAPPA_FINTA)
    assert not ok
    assert any("name=" in p for p in problemi)


def test_model_alias_viene_scartato(tmp_path, monkeypatch):
    """ADR-014: l'alias mente e si paga un altro modello. Anche nel frontmatter conta l'id
    esplicito, mai l'alias corto."""
    monkeypatch.setattr(va, "AG", str(tmp_path))
    sporco = FRONTMATTER_PULITO.replace("model: claude-sonnet-5", "model: sonnet")
    _scrivi(tmp_path, sporco)
    ok, problemi = va.verifica_agente(AGENTE_FINTO, MAPPA_FINTA)
    assert not ok
    assert any("model=" in p for p in problemi)


def test_tools_fuori_ordine_viene_scartato(tmp_path, monkeypatch):
    monkeypatch.setattr(va, "AG", str(tmp_path))
    sporco = FRONTMATTER_PULITO.replace("tools: [Read, Write]", "tools: [Write, Read]")
    _scrivi(tmp_path, sporco)
    ok, problemi = va.verifica_agente(AGENTE_FINTO, MAPPA_FINTA)
    assert not ok
    assert any("tools=" in p for p in problemi)


def test_lan_gate_con_write_viola_inv09(tmp_path, monkeypatch):
    monkeypatch.setattr(va, "AG", str(tmp_path))
    contenuto = FRONTMATTER_PULITO.replace("name: lan-finto", "name: lan-gate")
    _scrivi(tmp_path, contenuto, nome="lan-gate.md")
    agente_gate = {"id": "lan-gate", "modello": "claude-sonnet-5",
                   "tools": ["Read", "Write"], "produce": []}
    ok, problemi = va.verifica_agente(agente_gate, {})
    assert not ok
    assert any("INV-09" in p for p in problemi)


def test_produce_non_citato_nel_corpo_viola_inv22(tmp_path, monkeypatch):
    monkeypatch.setattr(va, "AG", str(tmp_path))
    senza_citazione = FRONTMATTER_PULITO.replace(
        "Corpo che cita pubblico.json come artefatto prodotto, per la prova INV-22.",
        "Corpo che non cita affatto il file che dovrebbe produrre.",
    )
    _scrivi(tmp_path, senza_citazione)
    ok, problemi = va.verifica_agente(AGENTE_FINTO, MAPPA_FINTA)
    assert not ok
    assert any("INV-22" in p for p in problemi)


def test_file_assente_da_NO_non_eccezione(tmp_path, monkeypatch):
    monkeypatch.setattr(va, "AG", str(tmp_path))
    ok, problemi = va.verifica_agente(AGENTE_FINTO, MAPPA_FINTA)
    assert not ok
    assert any("assente" in p for p in problemi)
