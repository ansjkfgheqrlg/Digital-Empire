#!/usr/bin/env python3
"""
Script Structure Calculator for Short-Form Script Engine.

Calculates timing, word counts, and retention hook placement
for any video duration and type combination.

Usage:
    python structure_calculator.py --duration 60 --type educativo
    python structure_calculator.py --duration 30 --type azione --format visual
"""

import argparse
import json
import math


# ═══════════════════════════════════════════
# DURATION RANGES PER VIDEO TYPE
# ═══════════════════════════════════════════

TYPE_RANGES = {
    "azione":    {"min": 15, "max": 45,  "ideale": 30},
    "educativo": {"min": 60, "max": 180, "ideale": 90},
    "prova":     {"min": 30, "max": 90,  "ideale": 60},
    "trend":     {"min": 7,  "max": 30,  "ideale": 15}
}

# Italian speech rate: ~2.5-2.8 words/second for energetic delivery
WORDS_PER_SEC = 2.7

# Payload internal time distribution per type
PAYLOAD_DISTRIBUTION = {
    "azione": {
        "steps": [
            {"name": "PROBLEMA visualizzato", "proportion": 0.25, "note": "Mostra il problema"},
            {"name": "FIX",                   "proportion": 0.50, "note": "Soluzione in 1-3 step"},
            {"name": "RISULTATO",             "proportion": 0.25, "note": "Cosa cambia dopo il fix"}
        ]
    },
    "educativo": {
        "steps": [
            {"name": "CONTESTO",          "proportion": 0.15, "note": "Perché è importante"},
            {"name": "FRAMEWORK/METODO",  "proportion": 0.50, "note": "Punti numerati + retention hooks"},
            {"name": "ESEMPIO CONCRETO",  "proportion": 0.20, "note": "Caso reale"},
            {"name": "TAKEAWAY",          "proportion": 0.15, "note": "Lezione in 1 frase (≤12 parole)"}
        ]
    },
    "prova": {
        "steps": [
            {"name": "PRIMA",                 "proportion": 0.20, "note": "Situazione iniziale con numeri"},
            {"name": "COSA ABBIAMO FATTO",    "proportion": 0.35, "note": "2-3 interventi chiave"},
            {"name": "DOPO",                  "proportion": 0.20, "note": "Risultati con numeri"},
            {"name": "PERCHÉ HA FUNZIONATO",  "proportion": 0.25, "note": "Lezione trasferibile"}
        ]
    },
    "trend": {
        "steps": [
            {"name": "TREND SETUP",  "proportion": 0.15, "note": "Audio/format trending"},
            {"name": "TWIST CRO",    "proportion": 0.55, "note": "Applicazione CRO al trend"},
            {"name": "PUNCHLINE",    "proportion": 0.30, "note": "Battuta finale memorabile"}
        ]
    }
}


def calculate_structure(duration: int, tipo_video: str) -> dict:
    """
    Calculate the complete timing structure for a video.

    Args:
        duration: total video duration in seconds
        tipo_video: 'azione' | 'educativo' | 'prova' | 'trend'

    Returns:
        dict with block timing, word counts, retention hooks, and warnings
    """

    tipo = tipo_video.lower()
    tipo_range = TYPE_RANGES.get(tipo)

    if not tipo_range:
        return {"error": f"Tipo '{tipo_video}' non riconosciuto. Usa: azione, educativo, prova, trend"}

    # ── Warnings ──
    warnings = []
    if duration < tipo_range["min"]:
        warnings.append(
            f"⚠️ {duration}s è sotto il minimo per {tipo} ({tipo_range['min']}s). "
            f"Considera di allungare o cambiare tipo."
        )
    elif duration > tipo_range["max"]:
        warnings.append(
            f"⚠️ {duration}s è sopra il massimo per {tipo} ({tipo_range['max']}s). "
            f"Considera di accorciare o passare a long-form."
        )

    # ── Calculate block durations ──

    # Hook: always 2-3 sec
    hook_sec = 3 if duration > 15 else 2

    # Tension: scales with duration, 0 for trend
    if tipo == "trend" or duration < 20:
        tension_sec = 0
    elif duration <= 30:
        tension_sec = 4
    elif duration <= 60:
        tension_sec = 6
    elif duration <= 90:
        tension_sec = 8
    else:
        tension_sec = 10

    # CTA: scales slightly with duration
    if duration <= 15:
        cta_sec = 2
    elif duration <= 30:
        cta_sec = 4
    elif duration <= 60:
        cta_sec = 6
    elif duration <= 90:
        cta_sec = 7
    else:
        cta_sec = 10

    # Payload: everything else
    payload_sec = duration - hook_sec - tension_sec - cta_sec
    payload_sec = max(payload_sec, 5)

    # ── Calculate word counts ──
    total_words = int(duration * WORDS_PER_SEC)
    hook_words = int(hook_sec * WORDS_PER_SEC)
    tension_words = int(tension_sec * WORDS_PER_SEC)
    payload_words = int(payload_sec * WORDS_PER_SEC)
    cta_words = int(cta_sec * WORDS_PER_SEC)

    # ── Calculate retention hooks ──
    if payload_sec <= 15 or tipo == "trend":
        retention_count = 0
        retention_positions = []
    elif payload_sec <= 30:
        retention_count = 1
        retention_positions = [hook_sec + tension_sec + payload_sec // 2]
    else:
        retention_count = max(1, payload_sec // 25)
        interval = payload_sec / (retention_count + 1)
        retention_positions = [
            int(hook_sec + tension_sec + interval * (i + 1))
            for i in range(retention_count)
        ]

    # ── Calculate payload internal structure ──
    dist = PAYLOAD_DISTRIBUTION.get(tipo, {})
    payload_steps = []
    if dist:
        for step in dist["steps"]:
            step_sec = max(2, round(payload_sec * step["proportion"]))
            step_words = int(step_sec * WORDS_PER_SEC)
            payload_steps.append({
                "nome": step["name"],
                "durata_sec": step_sec,
                "parole": step_words,
                "nota": step["note"]
            })

    # ── Build visual map ──
    bar_payload = "=" * max(3, payload_sec // 3)
    visual_map = (
        f"[HOOK {hook_sec}s]"
        f"{'[TENS ' + str(tension_sec) + 's]' if tension_sec > 0 else ''}"
        f"[{bar_payload}PAYLOAD {payload_sec}s{bar_payload}]"
        f"[CTA {cta_sec}s]"
    )

    return {
        "input": {
            "durata_totale": duration,
            "tipo_video": tipo,
            "range_consigliato": f"{tipo_range['min']}-{tipo_range['max']}s (ideale: {tipo_range['ideale']}s)"
        },
        "blocchi": {
            "B1_HOOK":     {"durata_sec": hook_sec,     "parole": hook_words,     "nota": "1 frase, max 15 parole"},
            "B2_TENSIONE": {"durata_sec": tension_sec,   "parole": tension_words,   "nota": "2-3 frasi bridge" if tension_sec > 0 else "N/A per trend"},
            "B3_PAYLOAD":  {"durata_sec": payload_sec,   "parole": payload_words,   "struttura_interna": payload_steps},
            "B4_CTA":      {"durata_sec": cta_sec,       "parole": cta_words,       "nota": "1 CTA chiara"}
        },
        "retention_hooks": {
            "quanti": retention_count,
            "posizioni_sec": retention_positions,
            "regola": f"1 ogni ~{payload_sec // (retention_count + 1)}s" if retention_count > 0 else "Non necessari"
        },
        "totali": {
            "parole_stimate": total_words,
            "velocita_parlata": f"{WORDS_PER_SEC} parole/sec"
        },
        "visual_map": visual_map,
        "warnings": warnings
    }


def format_output(result: dict, fmt: str = "text") -> str:
    """Format the result for display."""

    if fmt == "json":
        return json.dumps(result, indent=2, ensure_ascii=False)

    if "error" in result:
        return f"❌ {result['error']}"

    lines = []
    inp = result["input"]
    blocks = result["blocchi"]
    ret = result["retention_hooks"]
    totals = result["totali"]

    lines.append("=" * 60)
    lines.append(f"  STRUTTURA SCRIPT: {inp['tipo_video'].upper()} — {inp['durata_totale']}s")
    lines.append(f"  Range consigliato: {inp['range_consigliato']}")
    lines.append("=" * 60)

    # Warnings
    for w in result.get("warnings", []):
        lines.append(f"\n  {w}")

    # Visual map
    lines.append(f"\n  {result['visual_map']}\n")

    # Block table
    lines.append(f"  {'BLOCCO':<15} {'DURATA':<10} {'PAROLE':<10} {'NOTA'}")
    lines.append(f"  {'-'*60}")
    for block_name, block_data in blocks.items():
        name_short = block_name.replace("B1_", "").replace("B2_", "").replace("B3_", "").replace("B4_", "")
        nota = block_data.get("nota", "")
        lines.append(f"  {name_short:<15} {block_data['durata_sec']:<10}s {block_data['parole']:<10} {nota}")

    # Payload internal structure
    payload_steps = blocks["B3_PAYLOAD"].get("struttura_interna", [])
    if payload_steps:
        lines.append(f"\n  PAYLOAD — Struttura interna:")
        for step in payload_steps:
            lines.append(f"    ├── {step['nome']}: {step['durata_sec']}s (~{step['parole']} parole)")
            lines.append(f"    │   {step['nota']}")

    # Retention hooks
    lines.append(f"\n  RETENTION HOOKS: {ret['quanti']}")
    if ret["posizioni_sec"]:
        positions_str = ", ".join(f"~{p}s" for p in ret["posizioni_sec"])
        lines.append(f"  Posizioni: {positions_str}")
        lines.append(f"  Regola: {ret['regola']}")

    # Totals
    lines.append(f"\n  TOTALE: ~{totals['parole_stimate']} parole ({totals['velocita_parlata']})")
    lines.append("=" * 60)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Script Structure Calculator")
    parser.add_argument("--duration", "-d", type=int, required=True, help="Video duration in seconds")
    parser.add_argument("--type", "-t", required=True, choices=["azione", "educativo", "prova", "trend"])
    parser.add_argument("--format", "-f", default="text", choices=["text", "json", "visual"])

    args = parser.parse_args()
    result = calculate_structure(args.duration, args.type)
    print(format_output(result, args.format))


if __name__ == "__main__":
    main()