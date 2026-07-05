"""
ai_translate.py — Riserva AI per i SOLI residui di traduzione (Half A add-on, opzionale, €0).

Il glossario deterministico traduce ~99%. Se resta qualche termine tedesco (che Gate B
bloccherebbe), qui lo si traduce con un modello GRATUITO (NVIDIA NIM / endpoint
OpenAI-compatibile — lo stesso stack $0 dell'Outreach). Interviene SOLO sui residui, raramente.

Regole:
- Nessuna chiave hardcoded: tutto da `.env`. Se `TRANSLATE_AI_KEY` è assente → DISATTIVO.
- Mai solleva eccezioni: su errore/timeout/disattivo ritorna {} → la pipeline resta col
  glossario + Gate B, identica a prima (nessun blocco nuovo, nessun crash).
- Costo: €0 (endpoint gratuito). Volume minimo (solo residui).

Config (.env):
  TRANSLATE_AI_KEY   = chiave gratuita (es. la stessa NVIDIA dell'Outreach)   [assente ⇒ off]
  TRANSLATE_AI_URL   = endpoint OpenAI-compat (default: NVIDIA NIM free)
  TRANSLATE_AI_MODEL = modello gratuito (default: Nemotron)
"""
from __future__ import annotations

import json
import os
import re
from typing import Any

DEFAULT_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
DEFAULT_MODEL = "nvidia/llama-3.1-nemotron-70b-instruct"
TIMEOUT_S = 20


def enabled() -> bool:
    """Attivo solo se è configurata una chiave (altrimenti glossario+Gate B come prima)."""
    return bool((os.environ.get("TRANSLATE_AI_KEY") or "").strip())


def translate_terms(terms: list[str]) -> dict[str, str]:
    """DE→IT per termini/etichette di equipaggiamento auto. Ritorna {originale: tradotto}.
    Non inventa fatti. Su qualunque problema → {} (fallback silenzioso e sicuro)."""
    terms = [t for t in dict.fromkeys(terms) if t and str(t).strip()]
    if not terms or not enabled():
        return {}
    key = os.environ["TRANSLATE_AI_KEY"].strip()
    url = (os.environ.get("TRANSLATE_AI_URL") or DEFAULT_URL).strip()
    model = (os.environ.get("TRANSLATE_AI_MODEL") or DEFAULT_MODEL).strip()

    prompt = (
        "Sei un traduttore automobilistico DE→IT. Traduci in italiano corretto le seguenti "
        "etichette di equipaggiamento/scheda auto. Localizza in italiano ANCHE le sigle e i nomi "
        "di enti tedeschi (es. TÜV/HU → 'revisione', AU → 'controllo emissioni', ABE, Scheckheft "
        "→ 'libretto tagliandi'). NON lasciare NESSUNA parola in tedesco. Non inventare optional, "
        "non spiegare. Mantieni invariati numeri, unità (kW, CV, km) e nomi di modello. "
        "Rispondi SOLO con un oggetto JSON {\"originale\":\"traduzione\"} senza altro testo.\n"
        + json.dumps(terms, ensure_ascii=False)
    )
    import time
    import requests
    # 4 tentativi con gestione del RATE-LIMIT (429): in un batch le chiamate sono ravvicinate,
    # non deve restare tedesco per un limite temporaneo → si attende e si ritenta.
    for attempt in range(4):
        try:
            resp = requests.post(
                url,
                timeout=TIMEOUT_S,
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={
                    "model": model,
                    "temperature": 0.0,
                    "messages": [{"role": "user", "content": prompt}],
                },
            )
            if resp.status_code == 200:
                out = _parse_json_obj(resp.json()["choices"][0]["message"]["content"])
                if out:
                    return out
            elif resp.status_code == 429:  # rate limit → aspetta (Retry-After se c'è)
                ra = (resp.headers.get("retry-after") or "").strip()
                wait = float(ra) if ra.replace(".", "", 1).isdigit() else 8.0
                time.sleep(min(wait, 15.0))
                continue
        except Exception:
            pass
        if attempt < 3:
            time.sleep(2.0 + attempt * 2.0)
    return {}


def _parse_json_obj(txt: str) -> dict[str, str]:
    """Estrae il primo oggetto JSON dal testo del modello. Tiene solo valori stringa non vuoti."""
    m = re.search(r"\{.*\}", txt or "", re.S)
    if not m:
        return {}
    try:
        obj = json.loads(m.group(0))
    except Exception:
        return {}
    if not isinstance(obj, dict):
        return {}
    out: dict[str, str] = {}
    for k, v in obj.items():
        if isinstance(v, str) and v.strip():
            out[str(k)] = v.strip()
    return out
