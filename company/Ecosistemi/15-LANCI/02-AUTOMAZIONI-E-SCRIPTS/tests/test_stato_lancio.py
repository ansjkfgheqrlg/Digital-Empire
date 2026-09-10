# -*- coding: utf-8 -*-
"""Prove della macchina a stati (S2a, micro-task MT-XV6Y).

PERCHE' ESISTONO. Il criterio di chiusura di S2 e' che `avanza` su un lancio
vuoto esca con codice 1 e non zero. Quel comando e' S2b, ma poggia interamente
su questo modulo: se il lock non tiene o la validazione si fida di un campo
salvato, il gate di S2b sara' verde per il motivo sbagliato.
"""
import json
import os
import sys

import pytest

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(QUI))

from scripts import lancio as cli  # noqa: E402
from scripts import stato_lancio as sl  # noqa: E402


@pytest.fixture
def lanci_finti(tmp_path, monkeypatch):
    d = tmp_path / "lanci"
    d.mkdir()
    monkeypatch.setattr(sl, "LANCI", str(d))
    return d


# --------------------------------------------------------------- creazione

def test_crea_parte_da_idea_e_scrive_lo_stato(lanci_finti):
    dati = sl.Lancio("prova").crea("Prova")
    assert dati["stato"] == "IDEA"
    assert (lanci_finti / "prova" / "stato.json").exists()


def test_creare_due_volte_non_sovrascrive(lanci_finti):
    """Il difetto piu' caro possibile: ricreare un lancio in corso e perderlo."""
    sl.Lancio("prova").crea("Prova")
    with pytest.raises(sl.ErroreLancio) as e:
        sl.Lancio("prova").crea("Un altro nome")
    assert "esiste gia'" in str(e.value)
    assert json.load(open(lanci_finti / "prova" / "stato.json",
                          encoding="utf-8"))["prodotto"] == "Prova"


def test_un_identificativo_sporco_viene_rifiutato(lanci_finti):
    for cattivo in ("../fuori", "con spazio", "", "slash/dentro"):
        with pytest.raises(sl.ErroreLancio):
            sl.Lancio(cattivo)


def test_leggere_un_lancio_inesistente_lo_dice_chiaro(lanci_finti):
    with pytest.raises(sl.ErroreLancio) as e:
        sl.Lancio("mai-creato").stato()
    assert "inesistente" in str(e.value)


# -------------------------------------------------------------------- lock

def test_il_lock_e_esclusivo(lanci_finti):
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    with sl.Lock(lancio.path_lock, attesa_massima_s=0.2):
        with pytest.raises(sl.ErroreLancio) as e:
            with sl.Lock(lancio.path_lock, attesa_massima_s=0.2):
                pass
    assert "occupato da un'altra sessione" in str(e.value)


def test_il_lock_si_libera_all_uscita(lanci_finti):
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    with sl.Lock(lancio.path_lock, attesa_massima_s=0.2):
        pass
    assert not os.path.exists(lancio.path_lock)
    with sl.Lock(lancio.path_lock, attesa_massima_s=0.2):
        pass  # si riprende senza errore


def test_il_lock_dice_chi_lo_tiene(lanci_finti):
    """Un lock orfano deve poter essere capito, non solo trovato."""
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    with sl.Lock(lancio.path_lock):
        dentro = json.load(open(lancio.path_lock, encoding="utf-8"))
    assert dentro["pid"] == os.getpid()
    assert "preso_il" in dentro


# -------------------------------------------------------------- validazione

def _artefatto(lancio, nome, dati):
    with open(os.path.join(lancio.dir, nome), "w", encoding="utf-8", newline="\n") as f:
        json.dump(dati, f, ensure_ascii=False)


def test_un_artefatto_assente_e_assente_non_valido(lanci_finti):
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    assert lancio.valida_artefatto("pubblico.json") == ["assente"]
    assert lancio.artefatti_presenti() == {}


def test_un_artefatto_rotto_riporta_il_campo_esatto(lanci_finti):
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    _artefatto(lancio, "pubblico.json", {"schema_version": "1.0.0"})
    problemi = lancio.valida_artefatto("pubblico.json")
    assert problemi
    assert any("lancio_id" in p for p in problemi)


def test_la_validita_e_ricalcolata_non_letta_da_un_campo(lanci_finti):
    """IL controllo che conta. Un file che dichiara di essere valido non lo e'
    per questo: altrimenti basta scrivere 'valido: true' per passare un gate."""
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    _artefatto(lancio, "pubblico.json",
               {"schema_version": "1.0.0", "valido": True, "gate": "passato"})
    assert lancio.valida_artefatto("pubblico.json"), \
        "un artefatto che si dichiara valido deve comunque fallire lo schema"


def test_json_illeggibile_non_fa_esplodere_il_programma(lanci_finti):
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    with open(os.path.join(lancio.dir, "pubblico.json"), "w", encoding="utf-8") as f:
        f.write("{non sono json")
    problemi = lancio.valida_artefatto("pubblico.json")
    assert problemi and "JSON non leggibile" in problemi[0]


def test_una_proposta_non_conta_come_artefatto(lanci_finti):
    """E' il vincolo che impedisce a un prezzo non firmato di sembrare firmato."""
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    _artefatto(lancio, "offerta.PROPOSTA.json", {"prezzo": 67})
    assert "offerta.json" not in lancio.artefatti_presenti()
    assert lancio.artefatti_presenti() == {}


def test_le_chiavi_di_servizio_non_fanno_fallire_lo_schema(lanci_finti):
    """Gli schemi hanno additionalProperties: false. Una nota di servizio
    farebbe fallire il file per il motivo sbagliato."""
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    _artefatto(lancio, "pubblico.json", {
        "_nota": "spiegazione di servizio",
        "schema_version": "1.0.0",
        "lancio_id": "prova",
        "misurato_il": "2026-09-10T12:00:00+02:00",
        "canali": [{"id": "c", "tipo": "lista-email", "posseduto": True,
                    "raggiungibili_verificati": 0,
                    "prova": {"tipo": "nessuna", "riferimento": "x", "data": "2026-09-10"}}],
        "totale_raggiungibile_verificato": 0,
    })
    assert lancio.valida_artefatto("pubblico.json") == []


# ------------------------------------------------------------------ verbali

def test_ogni_creazione_lascia_un_verbale(lanci_finti):
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    verbali = os.listdir(lancio.dir_verbali)
    assert len(verbali) == 1 and "creazione" in verbali[0]


# ------------------------------------------------------------------- comando

def test_il_comando_dice_quando_un_pezzo_non_esiste_ancora(lanci_finti, capsys):
    """Meglio dire 'non e' costruito' che far finta di eseguire."""
    assert cli.main(["avanza", "prova"]) == 2
    fuori = capsys.readouterr().out
    assert "non e' ancora costruito" in fuori and "MT-3XWC" in fuori


def test_valida_da_uscita_1_quando_qualcosa_non_torna(lanci_finti, capsys):
    lancio = sl.Lancio("prova")
    lancio.crea("Prova")
    _artefatto(lancio, "pubblico.json", {"schema_version": "1.0.0"})
    assert cli.main(["valida", "prova"]) == 1


def test_un_lancio_inesistente_da_2_non_3(lanci_finti):
    """2 = parametri sbagliati (colpa di chi chiama). 3 = errore di sistema."""
    assert cli.main(["stato", "mai-creato"]) == 2
