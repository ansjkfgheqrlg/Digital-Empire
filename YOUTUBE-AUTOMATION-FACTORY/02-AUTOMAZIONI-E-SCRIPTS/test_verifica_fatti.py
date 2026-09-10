# -*- coding: utf-8 -*-
"""Test di verifica_fatti.py (A4-RC-02). Nessuna dipendenza da un video reale: solo testi
sintetici, come richiesto dalla misura in RIPASSO_COSTRUTTIVO.py — "passa un test con una
data alterata"."""
from __future__ import annotations

from verifica_fatti import verifica_fatti, estrai_fatti, _confronta_numeri, _tokenizza


FONTE = (
    "Maria Bianchi e' nata nel 1995 a Torino. Da 30 anni lavora come infermiera. "
    "Il fratello di Maria Bianchi si chiama Paolo. Durante l'intervista ha detto: "
    "\"non ho mai smesso di crederci\". Ha compiuto 45 anni quest'anno."
)


# --------------------------------------------------------------------------------------
# La misura dichiarata dalla regola A4-RC-02: una data alterata produce un BLOCCO
# --------------------------------------------------------------------------------------
def test_data_alterata_produce_blocco():
    script_alterato = (
        "Maria Bianchi e' nata nel 1996 a Torino. Da 30 anni lavora come infermiera."
    )
    risultato = verifica_fatti(script_alterato, FONTE)
    assert risultato["esito"] == "BLOCCO"
    valori_discordanti = [d["valore"] for d in risultato["discordanze"]]
    assert "1996" in valori_discordanti


def test_stesso_fatto_coerente_passa():
    script_fedele = "Maria Bianchi e' nata nel 1995 a Torino. Da 30 anni lavora come infermiera."
    risultato = verifica_fatti(script_fedele, FONTE)
    assert risultato["esito"] == "passa"
    assert risultato["conteggio"]["discordanti"] == 0


def test_cifra_eta_alterata_produce_blocco():
    script_alterato = "Ha compiuto 50 anni quest'anno."
    risultato = verifica_fatti(script_alterato, FONTE)
    assert risultato["esito"] == "BLOCCO"
    assert any(d["valore"] == "50" for d in risultato["discordanze"])


def test_citazione_riscritta_e_discordante():
    script_alterato = 'Durante l\'intervista ha detto: "non ho mai smesso di lottare".'
    risultato = verifica_fatti(script_alterato, FONTE)
    citazioni = [f for f in risultato["fatti"] if f["famiglia"] == "citazioni"]
    assert citazioni, "la citazione fra virgolette deve essere estratta"
    assert citazioni[0]["esito"] == "discordante"
    assert risultato["esito"] == "BLOCCO"


def test_citazione_identica_e_coerente():
    script_fedele = 'Durante l\'intervista ha detto: "non ho mai smesso di crederci".'
    risultato = verifica_fatti(script_fedele, FONTE)
    citazioni = [f for f in risultato["fatti"] if f["famiglia"] == "citazioni"]
    assert citazioni and citazioni[0]["esito"] == "coerente"


def test_nome_mai_visto_e_non_verificabile_non_blocca():
    script_nuovo = "Giuseppe Verdi ha commentato la notizia con entusiasmo."
    risultato = verifica_fatti(script_nuovo, FONTE)
    nomi = [f for f in risultato["fatti"] if f["famiglia"] == "nomi_propri"]
    assert any(n["esito"] == "non_verificabile" for n in nomi)
    # un fatto non verificabile non basta da solo a bloccare (limite dichiarato nel modulo)
    assert risultato["esito"] == "passa"


def test_estrai_fatti_trova_le_cinque_famiglie_sulla_fonte():
    fatti = estrai_fatti(FONTE)
    assert "Maria Bianchi" in fatti["nomi_propri"]
    assert fatti["citazioni"] == ["non ho mai smesso di crederci"]
    assert fatti["relazioni"] and fatti["relazioni"][0][0] == "il fratello di"


def test_confronta_numeri_funzione_pura():
    tok_fonte = _tokenizza("nel 1995 a Torino")
    tok_script = _tokenizza("nel 1996 a Torino")
    risultati = _confronta_numeri(tok_script, tok_fonte)
    assert any(r["esito"] == "discordante" and r["valore"] == "1996" for r in risultati)


def test_testi_vuoti_non_esplodono():
    risultato = verifica_fatti("", "")
    assert risultato["esito"] == "passa"
    assert risultato["conteggio"] == {"coerenti": 0, "discordanti": 0, "non_verificabili": 0}


# ---------------------------------------------------------------------------
# Runner autonomo (aggiunto 2026-09-10). Senza questo, `python test_<nome>.py`
# usciva 0 SENZA ESEGUIRE NIENTE: i test in stile pytest sono sole funzioni, e un
# file che esce 0 in silenzio sembra un test verde mentre non ha provato nulla.
# Un test silente e' peggio di nessun test, perche' rassicura. Ora gira in
# entrambi i modi: `pytest` e `python test_<nome>.py`.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys as _sys, traceback as _tb
    _falliti = 0
    _casi = [(_n, _f) for _n, _f in sorted(globals().items())
             if _n.startswith("test_") and callable(_f)]
    import inspect as _ins
    _saltati = 0
    for _n, _f in _casi:
        # I casi che chiedono una fixture di pytest (tmp_path, monkeypatch...) non possono
        # girare qui: si dichiarano SALTATI, non falliti. Chiamarli "falliti" farebbe
        # scattare un allarme falso ogni volta, e un allarme che grida sempre viene spento.
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
