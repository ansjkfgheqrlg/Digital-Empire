# -*- coding: utf-8 -*-
"""GATE-TSR-2 — presidia budget.json (ART-BDG) DURANTE la produzione (tipo: continuo).

Criterio eseguibile (registro, testuale):
    scarto_percentuale(speso, previsto) <= 10

Scarto = (speso - previsto) / previsto * 100. Conta lo sforamento: spendere meno del
previsto non e' un problema di questo gate. Lo speso, quando esiste almeno una voce con
stato=='speso', e' RICALCOLATO dalle voci (dato_da_terzi: si legge dai movimenti, non
dalla dichiarazione); solo se nessuna voce e' 'speso' si legge scarto_corrente.speso.
`scarto_corrente` null = niente speso ancora = passa.

RAMO DI FALLIMENTO: "IN_PRODUZIONE -> DATATO: la spesa nuova si blocca, il lancio non
muore". Il verdetto porta ramo_fallimento = DATATO (un passo indietro), mai ABORTITO.
Lo sblocco "solo con firma umana tracciata" NON e' accettato da questo gate leggendo
`sbloccato_da`: un gate non puo' verificare una firma da una stringa (stessa ragione
della firma di ART-OFF). Lo sblocco passa dal punto umano PU-SPESA e dal motore.
"""
from __future__ import annotations

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-TSR-2"
ARTEFATTO = "budget.json"
SCARTO_MASSIMO = 10.0


def _ramo():
    """Lo stato di destinazione della transizione 'GATE-TSR-2 boccia' (DATATO)."""
    for t in registro().get("transizioni", []):
        if "GATE-TSR-2" in str(t.get("condizione", "")):
            return t.get("a")
    for a in registro()["artefatti"]:
        if a.get("gate") == "GATE-TSR-1":
            return a.get("se_fallisce")
    return None


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    b = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    previsto = b.get("costo_totale_previsto")
    scarto = b.get("scarto_corrente")
    voci_spese = [v for v in b.get("voci", []) if v.get("stato") == "speso"]
    if voci_spese:
        speso = round(sum(v.get("importo", 0) for v in voci_spese), 2)
        fonte_speso = "ricalcolato da %d voci con stato 'speso'" % len(voci_spese)
    elif scarto is None:
        speso = 0.0
        fonte_speso = "scarto_corrente null e nessuna voce 'speso': niente speso ancora"
    else:
        speso = scarto.get("speso", 0)
        fonte_speso = "scarto_corrente.speso (nessuna voce con stato 'speso')"

    if not isinstance(previsto, (int, float)) or previsto <= 0:
        pct = None
        if speso > 0:
            problemi.append("speso %s con costo_totale_previsto %r: senza un previsto > 0 ogni euro e' fuori "
                            "budget" % (speso, previsto))
    else:
        pct = round((speso - previsto) / previsto * 100.0, 2)
        if pct > SCARTO_MASSIMO:
            problemi.append("scarto %.2f%% fra speso %s e previsto %s, oltre il %d%%: la spesa nuova si blocca, "
                            "il lancio torna a %s (non muore)" % (pct, speso, previsto, SCARTO_MASSIMO, ramo))

    dati = {"speso": speso, "previsto": previsto, "scarto_percentuale": pct, "fonte_speso": fonte_speso,
            "soglia": SCARTO_MASSIMO}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
