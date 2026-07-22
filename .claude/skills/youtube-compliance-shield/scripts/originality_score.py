#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
originality_score.py — punteggio di TRASFORMAZIONE di un video replicato (0-100).

Perche' esiste: YouTube monetizza contenuto originale o significativamente trasformato e penalizza
il "contenuto riutilizzato". Questo tool rende la valutazione DETERMINISTICA e ripetibile, invece
di lasciarla al "secondo me e' abbastanza diverso".

5 dimensioni, ognuna 0-20:
  script        0 = traduzione letterale        20 = riscritto, angolo/esempi propri
  voice         0 = audio dell'originale        20 = voce nuova (Fliki/propria) + musica con licenza
  visual        0 = clip/frame dell'originale   20 = archivio con licenza o materiale proprio
  structure     0 = identica scaletta           20 = hook/ordine/CTA ripensati
  added_value   0 = nessun apporto              20 = contesto/dati/esempi/commento propri

Verdetto:
  >= 70  VERDE   (trasformazione sufficiente)
  50-69  GIALLO  (correggere prima di pubblicare)
  <  50  ROSSO   (re-upload mascherato: NON pubblicare)

REGOLA DURA: voice == 0 oppure visual == 0  ->  ROSSO comunque, a qualunque totale.
Motivo: significa che stai usando i FILE di un altro, non la sua idea.

Uso:
  python originality_score.py --script 15 --voice 20 --visual 20 --structure 12 --added-value 10
  python originality_score.py --json dati.json
"""

import argparse
import json
import sys

DIMENSIONS = ("script", "voice", "visual", "structure", "added_value")
MAX_PER_DIM = 20

LABELS = {
    "script": "Script",
    "voice": "Voce/audio",
    "visual": "Visivo",
    "structure": "Struttura",
    "added_value": "Valore aggiunto",
}

# Dimensioni che, se a zero, indicano uso di FILE altrui -> blocco automatico.
HARD_ZERO_BLOCK = ("voice", "visual")

THRESHOLD_GREEN = 70
THRESHOLD_YELLOW = 50


def _clamp(value, lo=0, hi=MAX_PER_DIM):
    """Riporta il voto nell'intervallo valido. Un input fuori scala e' un errore di compilazione,
    non un motivo per far esplodere il calcolo: lo si limita e lo si segnala."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return lo, True
    if v < lo:
        return lo, True
    if v > hi:
        return hi, True
    return v, False


def compute(data: dict) -> dict:
    """Calcola punteggio e verdetto. `data` ha le 5 chiavi di DIMENSIONS (0-20 ciascuna)."""
    scores = {}
    notes = []
    for dim in DIMENSIONS:
        raw = data.get(dim, 0)
        val, corrected = _clamp(raw)
        scores[dim] = val
        if corrected:
            notes.append(f"{LABELS[dim]}: valore '{raw}' fuori scala 0-{MAX_PER_DIM}, riportato a {val:g}")

    total = round(sum(scores.values()), 1)

    # Regola dura: uso di file altrui su voce o visivo -> rosso a prescindere.
    hard_block = [d for d in HARD_ZERO_BLOCK if scores[d] == 0]

    if hard_block:
        verdict = "ROSSO"
        reason = (
            "Uso di materiale altrui su "
            + " e ".join(LABELS[d] for d in hard_block)
            + " (voto 0): e' un re-upload, non una trasformazione."
        )
    elif total >= THRESHOLD_GREEN:
        verdict = "VERDE"
        reason = f"Trasformazione sufficiente ({total:g}/100, soglia {THRESHOLD_GREEN})."
    elif total >= THRESHOLD_YELLOW:
        verdict = "GIALLO"
        reason = (
            f"Trasformazione insufficiente ({total:g}/100): pubblicabile solo dopo le correzioni."
        )
    else:
        verdict = "ROSSO"
        reason = f"Re-upload mascherato ({total:g}/100, sotto {THRESHOLD_YELLOW}). Non pubblicare."

    # Suggerimenti: le dimensioni piu' deboli sono quelle su cui conviene intervenire.
    weakest = sorted(DIMENSIONS, key=lambda d: scores[d])
    actions = [
        f"Alza «{LABELS[d]}» (ora {scores[d]:g}/{MAX_PER_DIM})"
        for d in weakest
        if scores[d] < 12
    ]

    return {
        "tool": "originality_score",
        "dimensioni": {LABELS[d]: scores[d] for d in DIMENSIONS},
        "total": total,
        "verdetto": verdict,
        "motivo": reason,
        "blocco_automatico": bool(hard_block),
        "gate_compliance_pass": verdict == "VERDE",
        "azioni": actions,
        "note": notes,
        "soglie": {"verde": THRESHOLD_GREEN, "giallo": THRESHOLD_YELLOW},
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Punteggio di trasformazione (0-100) di un video replicato.")
    p.add_argument("--json", help="file JSON con le 5 dimensioni")
    for dim in DIMENSIONS:
        p.add_argument(f"--{dim.replace('_', '-')}", default=0, help=f"{LABELS[dim]} 0-{MAX_PER_DIM}")
    args = p.parse_args()

    if args.json:
        with open(args.json, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {dim: getattr(args, dim) for dim in DIMENSIONS}

    print(json.dumps(compute(data), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
