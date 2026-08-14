"""
APEX-7 Calc Layer — motore e ponte verso gli altri layer.

Tre modi di chiamarlo, dal piu' semplice al piu' garantito:

  1. `esegui(richiesta)`      — un calcolo. dict in, dict out.
  2. `esegui_grafo(passi)`    — piu' calcoli in catena: l'output di uno alimenta
                                l'altro, risolto in ordine topologico dal DAG
                                dell'orchestration layer.
  3. `esegui_certificato(...)` — come sopra, ma attraverso i 7 quality gate.

`esegui` e `catalogo` accettano e restituiscono SOLO dati JSON-serializzabili:
sono il punto di innesto per il ponte con gli altri orchestration layer, che non
possono scambiarsi oggetti Python. Un layer esterno chiede `catalogo()` per
sapere cosa questo sa calcolare, poi manda richieste.
"""
from __future__ import annotations

import time
from typing import Any, Dict, List, Mapping, Optional, Sequence

from .core import (
    REGISTRO, Assunzione, ErroreCalcolo, RisultatoCalcolo, arrotonda, catalogo,
)
from . import denaro as _denaro       # noqa: F401  (registrano i moduli)
from . import probabilita as _prob    # noqa: F401


def _assunzioni_usate(modulo, richiesta: Mapping[str, Any]) -> List[Assunzione]:
    """Quali default sono entrati nel risultato senza che l'utente li dichiarasse."""
    fuori: List[Assunzione] = []
    from .denaro import RIFERIMENTI
    for p in modulo.parametri:
        if p.obbligatorio or p.default is None:
            continue
        if richiesta.get(p.nome) is None:
            fonte = RIFERIMENTI.get(p.nome, {}).get("fonte", "default del modulo")
            fuori.append(Assunzione(p.nome, float(p.default), fonte))
    return fuori


def esegui(richiesta: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Esegue un calcolo. Contratto:
        in  -> {"modulo": "<id>", "<parametro>": <numero>, ...}
        out -> {"modulo", "ok", "valori", "assunzioni", "avvisi", "errore", "durata_ms"}

    Non solleva mai: un errore torna come `ok: False` con il motivo. Chi sta
    dall'altra parte del ponte non deve gestire eccezioni Python.
    """
    t0 = time.perf_counter()
    id_modulo = str(richiesta.get("modulo", "")).strip()

    if id_modulo not in REGISTRO:
        vicini = [m for m in REGISTRO if id_modulo and id_modulo in m]
        suggerimento = f" Forse intendevi: {vicini}." if vicini else ""
        return RisultatoCalcolo(
            modulo=id_modulo or "(nessuno)", ok=False,
            errore=f"modulo sconosciuto: '{id_modulo}'.{suggerimento} "
                   f"Usa catalogo() per l'elenco completo ({len(REGISTRO)} disponibili).",
            durata_ms=(time.perf_counter() - t0) * 1000.0,
        ).to_dict()

    modulo = REGISTRO[id_modulo]
    try:
        valori = modulo.fn(richiesta)
        avvisi: List[str] = []
        for k, v in valori.items():
            if isinstance(v, float) and v == float("inf"):
                avvisi.append(f"'{k}' e' infinito: la condizione non e' raggiungibile")
        return RisultatoCalcolo(
            modulo=id_modulo, ok=True, valori=arrotonda(valori),
            assunzioni=_assunzioni_usate(modulo, richiesta), avvisi=avvisi,
            durata_ms=(time.perf_counter() - t0) * 1000.0,
        ).to_dict()
    except ErroreCalcolo as e:
        return RisultatoCalcolo(modulo=id_modulo, ok=False, errore=str(e),
                                durata_ms=(time.perf_counter() - t0) * 1000.0).to_dict()
    except Exception as e:   # un bug nel modulo non deve far cadere il chiamante
        return RisultatoCalcolo(modulo=id_modulo, ok=False,
                                errore=f"errore interno del modulo ({type(e).__name__}): {e}",
                                durata_ms=(time.perf_counter() - t0) * 1000.0).to_dict()


def esegui_grafo(passi: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    """
    Piu' calcoli in catena. Ogni passo:
        {"nome": "...", "modulo": "...", "dipende_da": ["..."],
         "parametri": {...},
         "prendi": {"<mio_parametro>": "<passo>.<valore_prodotto>"}}

    `prendi` e' il collegamento: aggancia un parametro di questo passo a un
    valore calcolato da un passo precedente. L'ordine di esecuzione lo decide il
    DAG dell'orchestration layer (cicli e dipendenze inesistenti bloccano prima
    di eseguire).
    """
    from orchestration import ComputationNode, DAGEngine

    def costruisci(passo: Mapping[str, Any]):
        def calcola(_inputs: Mapping[str, Any], upstream: Mapping[str, Any]) -> Dict[str, Any]:
            parametri = dict(passo.get("parametri", {}))
            for mio, riferimento in (passo.get("prendi", {}) or {}).items():
                sorgente, _, campo = str(riferimento).partition(".")
                if sorgente not in upstream:
                    raise ErroreCalcolo(
                        f"'{riferimento}': il passo '{sorgente}' non e' fra le dipendenze dichiarate")
                prodotti = upstream[sorgente].get("valori", {})
                if campo not in prodotti:
                    raise ErroreCalcolo(
                        f"'{riferimento}': il passo '{sorgente}' non produce '{campo}' "
                        f"(produce: {sorted(prodotti)})")
                parametri[mio] = prodotti[campo]
            esito = esegui({"modulo": passo["modulo"], **parametri})
            if not esito["ok"]:
                raise ErroreCalcolo(f"passo '{passo.get('nome')}': {esito['errore']}")
            return esito
        return ComputationNode(str(passo["nome"]), list(passo.get("dipende_da", [])), calcola)

    motore = DAGEngine([costruisci(p) for p in passi])
    risultati, log = motore.execute({})
    return {
        "ok": all(r.usable for r in risultati.values()),
        "passi": {nome: (r.output if r.usable else {"ok": False, "errore": r.error})
                  for nome, r in risultati.items()},
        "stati": {nome: r.status for nome, r in risultati.items()},
        "ordine": motore.order,
        "log": log,
    }


def esegui_certificato(richiesta: Mapping[str, Any], orchestrator=None) -> Dict[str, Any]:
    """
    Un calcolo attraverso i 7 quality gate. Serve quando il numero prodotto
    diventa una decisione: la scorecard dice se ci si puo' contare.

    Gli esiti di `scenari_calibrati` diventano la distribuzione che il gate L5
    verifica (probabilita' che sommano a 100, nessuna stima puntuale travestita).
    """
    from orchestration import (
        AuditFinding, OrchestrationPipeline, Outcome, QualityReport,
        gate_l1_foundation, gate_l5_quality, GateLedger, StateSnapshot,
    )

    esito = esegui(richiesta)
    radice = StateSnapshot.create("CALC_ROOT", {"modulo": esito["modulo"]})
    ingresso = radice.chain_to("CALC_INPUT", dict(richiesta))
    ledger = GateLedger()

    ledger.record(gate_l1_foundation([radice, ingresso], dict(richiesta),
                                     required_fields=["modulo"]), blocking=False)

    esiti_dist: tuple = ()
    if esito["ok"] and richiesta.get("modulo") == "scenari_calibrati":
        esiti_dist = (
            Outcome("MIGLIORE", float(richiesta.get("prob_migliore_pct", 25.0)),
                    float(richiesta["valore_migliore"])),
            Outcome("BASE", float(richiesta.get("prob_base_pct", 50.0)),
                    float(richiesta["valore_base"])),
            Outcome("PEGGIORE", float(richiesta.get("prob_peggiore_pct", 25.0)),
                    float(richiesta["valore_peggiore"])),
        )

    audit = (
        AuditFinding("AUDIT_CALCOLO_RIUSCITO", triggered=not esito["ok"], severity="CRITICAL",
                     note=esito.get("errore") or ""),
        AuditFinding("AUDIT_ASSUNZIONI", triggered=bool(esito["assunzioni"]), severity="MEDIUM",
                     note=f"{len(esito['assunzioni'])} parametri presi da default, non dichiarati"),
        AuditFinding("AUDIT_AVVISI", triggered=bool(esito["avvisi"]), severity="LOW",
                     note="; ".join(esito["avvisi"])),
    )
    ledger.record(gate_l5_quality(QualityReport(
        score=10.0 if esito["ok"] else 0.0, threshold=7.5,
        audits=audit, outcomes=esiti_dist, min_audits=3)), blocking=False)

    return {"calcolo": esito,
            "certificato": ledger.all_passed,
            "scorecard": ledger.scorecard(),
            "referto": ledger.render()}


__all__ = ["esegui", "esegui_grafo", "esegui_certificato", "catalogo", "REGISTRO"]
