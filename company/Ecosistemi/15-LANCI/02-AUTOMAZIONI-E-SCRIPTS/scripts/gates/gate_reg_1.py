# -*- coding: utf-8 -*-
"""GATE-REG-1 — presidia apertura.json (ART-APE): l'ultimo controllo prima di PRONTO.

Criterio eseguibile (registro, testuale):
    tutte le voci della lista_sincronizzazione hanno esito==true
    AND via_libera.canale in canali_firma_ammessi
    AND tutti gli artefatti da ART-PUB a ART-BDG sono validi contro il proprio schema

La validita' degli artefatti e' RICALCOLATA dai file con valida_contro_schema (dato_da_terzi:
mai letta dallo stato ne' dal campo `artefatti_ricalcolati` del file stesso, che viene
solo riportato per confronto). Gli artefatti sono, nell'ordine del registro: pubblico,
decisione, certificato, ricerca, previsione, offerta, copy/manifest, funnel, editoriale,
budget.

Via libera: se `via_libera` manca, o `chi`/`canale` sono vuoti, il problema e' "via libera
non dato" — e' il punto umano PU-APERTURA, senza default e senza scadenza. Un canale fuori
dalla lista chiusa del registro e' rifiutato: nessun agente ha permesso di scrittura su
quell'oggetto, e il canale e' la prova che non l'ha scritto un agente.
"""
from __future__ import annotations

from ._comune import Verdetto, leggi_artefatto, registro, valida_contro_schema

ID = "GATE-REG-1"
ARTEFATTO = "apertura.json"
ARTEFATTI_A_MONTE = ["pubblico.json", "decisione.json", "certificato.json", "ricerca.json",
                     "previsione.json", "offerta.json", "copy/manifest.json", "funnel.json",
                     "editoriale.json", "budget.json"]


def _ramo():
    for a in registro()["artefatti"]:
        if a.get("gate") == ID:
            return a.get("se_fallisce")
    return None


def esegui(dir_lancio: str, rete) -> Verdetto:
    ramo = _ramo()
    errori = valida_contro_schema(dir_lancio, ARTEFATTO)
    if errori:
        pref = "" if errori == ["assente"] else "schema: "
        return Verdetto(ID, False, [pref + e for e in errori], {}, ramo)
    ap = leggi_artefatto(dir_lancio, ARTEFATTO)
    problemi: list[str] = []

    lista = ap.get("lista_sincronizzazione", [])
    false = [v for v in lista if v.get("esito") is not True]
    for v in false:
        problemi.append("lista_sincronizzazione: voce %r con esito %r, serve true" % (v.get("voce"), v.get("esito")))

    canali = list(registro().get("canali_firma_ammessi", []))
    vl = ap.get("via_libera")
    if not isinstance(vl, dict) or not vl.get("chi") or not vl.get("canale"):
        problemi.append("via libera non dato: nessuna persona ha autorizzato l'apertura (PU-APERTURA, senza "
                        "default e senza scadenza)")
    elif vl.get("canale") not in canali:
        problemi.append("via_libera.canale %r non e' nella lista chiusa %s: una firma fuori canale non e' "
                        "una firma" % (vl.get("canale"), canali))

    validi = {}
    for nome in ARTEFATTI_A_MONTE:
        errs = valida_contro_schema(dir_lancio, nome)
        validi[nome] = not errs
        if errs:
            if errs == ["assente"]:
                problemi.append("artefatto %s assente" % nome)
            else:
                problemi.append("artefatto %s non valido contro lo schema: %s%s"
                                % (nome, "; ".join(errs[:3]), " (+%d)" % (len(errs) - 3) if len(errs) > 3 else ""))

    dichiarati = {r.get("artefatto"): r.get("valido") for r in ap.get("artefatti_ricalcolati", [])}
    dati = {"voci_sincronizzazione": len(lista), "voci_false": len(false),
            "via_libera_chi": (vl or {}).get("chi") if isinstance(vl, dict) else None,
            "via_libera_canale": (vl or {}).get("canale") if isinstance(vl, dict) else None,
            "artefatti_validi_ricalcolati": validi, "artefatti_validi_dichiarati": dichiarati}
    return Verdetto(ID, not problemi, problemi, dati, ramo if problemi else None)
