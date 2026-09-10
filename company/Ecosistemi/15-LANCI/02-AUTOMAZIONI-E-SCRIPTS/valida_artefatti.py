# -*- coding: utf-8 -*-
"""Valida gli artefatti di un lancio contro i propri schemi.

PERCHE' ESISTE. Lo scaglione S1 chiede quattro file compilati a mano e "validati
contro gli schemi che gia' esistono". Senza un comando che lo faccia, "validato"
e' una parola che qualcuno scrive in un checkpoint. Questo e' il pezzo piu'
piccolo possibile che la rende una prova: legge il file, lo confronta con lo
schema, e stampa la riga esatta che non torna.

  python valida_artefatti.py <slug>

Esce 0 se tutti gli artefatti presenti sono validi, 1 se almeno uno non lo e',
2 se il lancio non esiste.

NON e' la macchina a stati di S2 (`stato_lancio.py` + comando `lancio`), e non
prova a esserlo: quella arriva con MT-XV6Y e questo file le lascera' il posto.
Qui c'e' solo cio' che serve per chiudere S1 con una prova invece che con una
dichiarazione.
"""
from __future__ import annotations

import json
import os
import sys

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
SCHEMI = os.path.join(RADICE, "PIANO-MAESTRO", "29-ECOSISTEMA-LANCI", "dati", "schemi")
LANCI = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lanci")

# artefatto -> schema. Solo i quattro di S1: gli altri nove arrivano da S3 in poi.
ARTEFATTI = {
    "pubblico.json": "pubblico.schema.json",
    "certificato.json": "certificato.schema.json",
    "previsione.json": "previsione.schema.json",
    "offerta.json": "offerta.schema.json",
}


def _senza_note(dati):
    """Toglie le chiavi di servizio che cominciano con '_'.

    Un file di proposta porta una nota che spiega perche' non e' ancora
    l'artefatto. Gli schemi hanno `additionalProperties: false`, quindi la nota
    lo farebbe fallire per il motivo sbagliato: si valida il contenuto, non il
    cartello che gli sta davanti.
    """
    if isinstance(dati, dict):
        return {k: v for k, v in dati.items() if not k.startswith("_")}
    return dati


def valida(percorso_lancio: str) -> int:
    if not os.path.isdir(percorso_lancio):
        print("Lancio inesistente: %s" % percorso_lancio)
        return 2

    try:
        import jsonschema
    except ImportError:
        print("Manca jsonschema:  py -3 -m pip install jsonschema")
        return 3

    problemi = 0
    trovati = 0
    for nome, nome_schema in ARTEFATTI.items():
        percorso = os.path.join(percorso_lancio, nome)
        proposta = os.path.join(percorso_lancio, nome.replace(".json", ".PROPOSTA.json"))
        etichetta = nome
        if not os.path.exists(percorso):
            if os.path.exists(proposta):
                percorso = proposta
                etichetta = os.path.basename(proposta)
            else:
                print("  ..   %-22s assente" % nome)
                continue
        trovati += 1

        schema = json.load(open(os.path.join(SCHEMI, nome_schema), encoding="utf-8"))
        dati = _senza_note(json.load(open(percorso, encoding="utf-8")))

        errori = sorted(jsonschema.Draft202012Validator(schema).iter_errors(dati),
                        key=lambda e: list(e.absolute_path))
        if not errori:
            print("  ok   %-22s valido contro %s" % (etichetta, nome_schema))
            continue

        problemi += 1
        print("  NO   %-22s %d problemi:" % (etichetta, len(errori)))
        for e in errori[:8]:
            dove = ".".join(str(x) for x in e.absolute_path) or "(radice)"
            print("         %-34s %s" % (dove, e.message[:110]))
        if len(errori) > 8:
            print("         ... e altri %d" % (len(errori) - 8))

    print()
    print("  artefatti trovati: %d   non validi: %d" % (trovati, problemi))
    return 1 if problemi else 0


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip().splitlines()[0])
        print("Uso: python valida_artefatti.py <slug>")
        print("Lanci presenti: %s" % (", ".join(sorted(
            d for d in os.listdir(LANCI) if os.path.isdir(os.path.join(LANCI, d)))) or "nessuno"))
        return 2
    return valida(os.path.join(LANCI, sys.argv[1]))


if __name__ == "__main__":
    sys.exit(main())
