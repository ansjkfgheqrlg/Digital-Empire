#!/usr/bin/env python3
"""
seo_score.py — Punteggio SEO deterministico dei metadati di un video YouTube.

Usato da: seo-analyst (valuta i candidati), metadata-optimizer (ripunteggia i propri
metadati), seo-gate (RICALCOLA in modo indipendente prima di approvare la pubblicazione).

Modello semplice, trasparente e ripetibile (0-100), coerente coi 5 elementi certificanti
del MKD §2.4. NON chiama API né inventa dati: punteggia solo ciò che gli passi.

Uso:
    python seo_score.py --json metadati.json
    python seo_score.py --title "..." --description "..." --tags "a,b,c" \
                        --keyword "keyword principale" --subtitles true --thumbnail true

Output: JSON con punteggio totale e breakdown per componente.
Exit code 0 sempre (è uno strumento di misura, non un gate).
"""
from __future__ import annotations
import argparse
import json
import sys

# Pesi dei 5 elementi certificanti (somma = 100)
WEIGHTS = {
    "title": 25,        # keyword presente + lunghezza sensata + non vuoto
    "description": 25,  # lunghezza + prime 2 righe + keyword + link/CTA
    "tags": 20,         # numero + presenza keyword tra i tag
    "thumbnail": 15,    # presente (brief) = elemento non trascurabile
    "subtitles": 15,    # presenti = indicizzati da YouTube
}


def _norm(s: str) -> str:
    return (s or "").strip().lower()


def score_title(title: str, keyword: str) -> tuple[float, list[str]]:
    notes = []
    title_clean = (title or "").strip()
    if not title_clean:
        return 0.0, ["titolo vuoto"]
    pts = 1.0  # non vuoto -> base
    frac = 0.4
    n = len(title_clean)
    if 20 <= n <= 70:
        frac += 0.3
    else:
        notes.append(f"lunghezza titolo {n} fuori 20-70")
    if keyword and _norm(keyword) in _norm(title_clean):
        frac += 0.3
    else:
        notes.append("keyword principale assente nel titolo")
    return round(WEIGHTS["title"] * min(frac, 1.0), 1), notes


def score_description(description: str, keyword: str) -> tuple[float, list[str]]:
    notes = []
    d = description or ""
    if not d.strip():
        return 0.0, ["descrizione vuota"]
    frac = 0.2
    if len(d) >= 200:
        frac += 0.3
    else:
        notes.append("descrizione < 200 caratteri")
    first_two = "\n".join(d.splitlines()[:2])
    if len(first_two.strip()) >= 40:
        frac += 0.2
    else:
        notes.append("prime 2 righe deboli (hook+valore mancante)")
    if keyword and _norm(keyword) in _norm(d):
        frac += 0.15
    else:
        notes.append("keyword assente nella descrizione")
    if ("http" in d) or ("iscriv" in _norm(d)) or ("link" in _norm(d)):
        frac += 0.15
    else:
        notes.append("nessun link/CTA nella descrizione")
    return round(WEIGHTS["description"] * min(frac, 1.0), 1), notes


def score_tags(tags: list[str], keyword: str) -> tuple[float, list[str]]:
    notes = []
    # Assicuriamoci che tags sia una lista
    if not isinstance(tags, list):
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]
        else:
            tags = []
    
    # Sanitizziamo gli elementi e deduplichiamo mantenendo l'ordine
    cleaned_tags = []
    seen = set()
    for t in tags:
        if t is not None:
            ts = str(t).strip()
            if ts and ts.lower() not in seen:
                seen.add(ts.lower())
                cleaned_tags.append(ts)
                
    tags = cleaned_tags
    if not tags:
        return 0.0, ["nessun tag"]
    frac = 0.0
    n = len(tags)
    if n >= 8:
        frac += 0.6
    elif n >= 4:
        frac += 0.4
    else:
        frac += 0.2
        notes.append(f"solo {n} tag (consigliati >=8)")
    if keyword and any(_norm(keyword) in _norm(t) for t in tags):
        frac += 0.4
    else:
        notes.append("keyword non presente tra i tag")
    return round(WEIGHTS["tags"] * min(frac, 1.0), 1), notes


def _to_bool(v) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return bool(v)
    if isinstance(v, str):
        return v.strip().lower() in {"1", "true", "yes", "si", "sì", "y"}
    return False


def score_flag(present: bool, key: str, label: str) -> tuple[float, list[str]]:
    if present:
        return float(WEIGHTS[key]), []
    return 0.0, [f"{label} assente"]


def compute(meta: dict) -> dict:
    if not isinstance(meta, dict):
        meta = {}
    keyword = str(meta.get("keyword") or "").strip()
    title = str(meta.get("title") or "").strip()
    description = str(meta.get("description") or "").strip()
    tags = meta.get("tags")
    if tags is None:
        tags = []
        
    t, tn = score_title(title, keyword)
    d, dn = score_description(description, keyword)
    g, gn = score_tags(tags, keyword)
    th, thn = score_flag(_to_bool(meta.get("thumbnail")), "thumbnail", "miniatura (brief)")
    su, sun = score_flag(_to_bool(meta.get("subtitles")), "subtitles", "sottotitoli")
    
    # Correzione del refuso grammaticale
    sun_clean = []
    for note in sun:
        if note == "sottotitoli assente":
            sun_clean.append("sottotitoli assenti")
        else:
            sun_clean.append(note)
            
    total = round(t + d + g + th + su, 1)
    return {
        "total": total,
        "breakdown": {"title": t, "description": d, "tags": g, "thumbnail": th, "subtitles": su},
        "notes": tn + dn + gn + thn + sun_clean,
        "pass_soglia_70": total >= 70,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Punteggio SEO deterministico (0-100).")
    ap.add_argument("--json", help="path a un file JSON con i metadati")
    ap.add_argument("--title", default="")
    ap.add_argument("--description", default="")
    ap.add_argument("--tags", default="", help="tag separati da virgola")
    ap.add_argument("--keyword", default="")
    ap.add_argument("--thumbnail", default="false")
    ap.add_argument("--subtitles", default="false")
    args = ap.parse_args()

    if args.json:
        with open(args.json, "r", encoding="utf-8") as f:
            meta = json.load(f)
    else:
        meta = {
            "title": args.title,
            "description": args.description,
            "tags": [t for t in args.tags.split(",") if t.strip()],
            "keyword": args.keyword,
            "thumbnail": _to_bool(args.thumbnail),
            "subtitles": _to_bool(args.subtitles),
        }

    result = compute(meta)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
