#!/usr/bin/env python3
"""
cashcow_check.py — Indice Cash Cow (0-100) di un canale YouTube dai suoi video.

Usato da: niche-scout (valida i canali candidati), niche-gate (soglia >= 60).

Idea (MKD §1.5): un cash cow non è un singolo virale, è la COSTANZA. L'indice combina:
  - velocità media (views/ora) dei video               -> "sta funzionando"
  - costanza (quanti video superano una soglia minima) -> "non è un colpo solo"
  - penalità sugli errori dichiarati (SEO/thumb/titolo) -> "quasi senza errori"

NON scarica dati da YouTube: ricevi i numeri (letti con Video IQ dall'account neutro) e li
punteggi in modo deterministico e ripetibile.

Uso:
    python cashcow_check.py --json canale.json

canale.json:
{
  "channel": "Dose Mentale",
  "videos": [
    {"title": "...", "views": 120000, "age_hours": 800, "errors": ["seo debole"]},
    {"title": "...", "views": 300000, "age_hours": 1500, "errors": []}
  ]
}
"""
from __future__ import annotations
import argparse
import json
import sys

# Soglia sotto la quale un video NON conta come "performante" (views/ora)
MIN_VPH = 20.0
# Componenti dell'indice (somma = 100)
W_SPEED = 45      # media views/ora normalizzata
W_CONSISTENCY = 40  # frazione di video sopra MIN_VPH
W_CLEAN = 15      # bonus "pochi errori"
# views/ora a cui la componente velocità satura a pieno punteggio
VPH_CAP = 200.0


def views_per_hour(v: dict) -> float:
    if not isinstance(v, dict):
        return 0.0
        
    views_raw = v.get("views")
    if views_raw is None:
        views = 0.0
    else:
        try:
            views = float(views_raw)
        except (ValueError, TypeError):
            views = 0.0
            
    age_raw = v.get("age_hours")
    if age_raw is None:
        age = 1.0
    else:
        try:
            age = max(float(age_raw), 1.0)
        except (ValueError, TypeError):
            age = 1.0
            
    return views / age


def compute(channel: dict) -> dict:
    if not isinstance(channel, dict):
        return {"index": 0, "reason": "dati canale non validi", "is_cashcow": False}
    videos = channel.get("videos", [])
    if not isinstance(videos, list) or not videos:
        return {"index": 0, "reason": "nessun video fornito", "is_cashcow": False}

    # Carica la soglia dinamica da learned_rules.json se esiste, altrimenti usa MIN_VPH
    min_vph = MIN_VPH
    import os
    try:
        rules_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "memory", "learned_rules.json"))
        if os.path.exists(rules_path):
            with open(rules_path, "r", encoding="utf-8") as f:
                rules = json.load(f)
            min_vph = float(rules.get("dynamic_min_vph", MIN_VPH))
    except Exception:
        min_vph = MIN_VPH

    vphs = [views_per_hour(v) for v in videos]
    avg_vph = sum(vphs) / len(vphs)

    # 1) velocità (satura a VPH_CAP)
    speed = W_SPEED * min(avg_vph / VPH_CAP, 1.0)

    # 2) costanza: quota di video sopra min_vph
    above = sum(1 for x in vphs if x >= min_vph)
    consistency = W_CONSISTENCY * (above / len(vphs))

    # 3) pulizia: penalità proporzionale alla quota di video con errori
    with_errors = sum(1 for v in videos if v.get("errors"))
    clean_frac = 1.0 - (with_errors / len(videos))
    clean = W_CLEAN * clean_frac

    index = round(speed + consistency + clean, 1)
    return {
        "channel": channel.get("channel", "?"),
        "index": index,
        "is_cashcow": index >= 60,
        "n_videos": len(videos),
        "avg_views_per_hour": round(avg_vph, 1),
        "min_vph_threshold": min_vph,
        "videos_above_min_vph": above,
        "videos_with_errors": with_errors,
        "breakdown": {
            "speed": round(speed, 1),
            "consistency": round(consistency, 1),
            "clean": round(clean, 1),
        },
        "soglia_gate": 60,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Indice Cash Cow di un canale (0-100).")
    ap.add_argument("--json", required=True, help="path al JSON del canale")
    args = ap.parse_args()
    with open(args.json, "r", encoding="utf-8") as f:
        channel = json.load(f)
    print(json.dumps(compute(channel), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
