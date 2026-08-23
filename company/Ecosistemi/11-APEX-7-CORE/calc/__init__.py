"""
APEX-7 Calc Layer — il calcolatore dell'Impero.

Calcola: percentuali, variazioni, crescita composta, probabilita' composte,
Bayes, probabilita' di superare una soglia, Monte Carlo, scenari calibrati,
rendimenti netti reali, costi invisibili, rischio, royalty (incluso KDP),
prezzo ottimale.

Uso rapido:

    from calc import esegui, catalogo

    esegui({"modulo": "royalty_kdp", "prezzo": 4.99, "unita_vendute": 500,
            "costi_fissi": 300})
    esegui({"modulo": "probabilita_soglia", "valore_iniziale": 1000,
            "soglia": 5000, "tasso_atteso": 0.30, "volatilita": 0.5, "periodi": 5})
    catalogo()   # tutto cio' che sa calcolare, in JSON

Ponte verso gli altri orchestration layer: `esegui` e `catalogo` parlano solo
dict JSON-serializzabili e `esegui` non solleva mai eccezioni — un errore torna
come `ok: False` con il motivo. Chi sta dall'altra parte non deve conoscere
Python.
"""
from .core import (
    Assunzione, ErroreCalcolo, ModuloCalcolo, Parametro, REGISTRO,
    RisultatoCalcolo, SafeMath, catalogo, num, registra,
)
from .engine import esegui, esegui_certificato, esegui_grafo

__all__ = [
    "Assunzione", "ErroreCalcolo", "ModuloCalcolo", "Parametro", "REGISTRO",
    "RisultatoCalcolo", "SafeMath", "catalogo", "esegui", "esegui_certificato",
    "esegui_grafo", "num", "registra",
]
