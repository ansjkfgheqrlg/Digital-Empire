#!/usr/bin/env python3
"""
build_candidate_pool.py — Pool di candidati REALI per il piano editoriale @Legamidiamore.

Legge le cache fresche `memory/channel_videos/<canale>.json` (scritte da
`youtube_hunter_playwright.py`), filtra/dedupe, etichetta con gli schemi titolo misurati
in `CALENDARIO-LEGAMIDIAMORE.md` ed esclude i video gia' prodotti (`memory/video_prodotti.json`).
Non inventa nulla: ogni riga del pool ha un videoId/url tracciabile nella cache di oggi.

Correzione reale trovata il 2026-08-26 (non un'assunzione): due dei 6 canali storicamente
cachati NON sono piu' nella nicchia dopo verifica fresca via Playwright:
  - @ciraolone -> canale AI/tech (Claude Code, CapCut, tutorial), non psicologia/relazioni.
  - @linguaggiosegretodelcorpo-6589 -> scuola di ballo (Arthur Murray, valzer, tango), non
    linguaggio del corpo/attrazione nonostante il nome del canale.
Esclusi qui esplicitamente come fonte primaria. @codicedonna resta escluso come fonte primaria
per campione troppo piccolo (3 video), stessa cautela gia' in CALENDARIO-LEGAMIDIAMORE.md.

Correzione reale #2: MIN_VPH=20.0 di cashcow_check.py (tarato su altri canali/nicchie) non e'
raggiunto da NESSUN video reale in questa nicchia oggi (top reale ~10.6 vph). Non si applica
qui come soglia assoluta: si usa un ranking RELATIVO per canale (i migliori N per canale),
altrimenti il pool risulterebbe vuoto per un artefatto di soglia, non per scarsita' reale.

Uso:
    python build_candidate_pool.py
    python build_candidate_pool.py --min-age-hours 24 --out ../memory/candidate_pool_70_20260826.json
"""
from __future__ import annotations
import argparse
import glob
import json
import os
import re
from datetime import datetime

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
CACHE_DIR = os.path.join(FACTORY_DIR, "memory", "channel_videos")
PRODOTTI_PATH = os.path.join(FACTORY_DIR, "memory", "video_prodotti.json")

# Non sono fonti di contenuto da replicare: il canale stesso e un progetto diverso (in pausa).
CANALI_ESCLUSI_NON_FONTE = {"Legamidiamore", "dosementale"}

# Verificati OGGI (fresh scrape) come fuori nicchia — vedi docstring. Esclusi come fonte
# primaria: se in futuro tornano in nicchia, rimuovere qui dopo nuova verifica reale.
CANALI_FUORI_NICCHIA = {"ciraolone", "linguaggiosegretodelcorpo-6589"}

# Campione troppo piccolo per essere una fonte primaria affidabile (non per contenuto).
CANALI_CAMPIONE_PICCOLO = {"codicedonna"}

# Schemi titolo misurati (delta di velocity reale, CALENDARIO-LEGAMIDIAMORE.md) — regex
# volutamente semplici, servono a ETICHETTARE il candidato, non a giudicarlo.
SCHEMI_TITOLO = {
    "segnali_espliciti": re.compile(r"\bsegn[ao]l[ei]\b", re.IGNORECASE),
    "genere_esplicito": re.compile(r"\b(donn[ae]|uomo|uomini)\b", re.IGNORECASE),
    "numero_secco": re.compile(r"\b\d+\b"),
    "parentesi": re.compile(r"[\(\)]"),
    "comando_maiuscolo": re.compile(r"\b[A-ZÀ-Ù]{3,}\b"),
    "allarme_negativo": re.compile(
        r"\b(blocc\w*|distrugg\w*|sbagli\w*|errore|mai|non\s+(?:fare|dire))\b", re.IGNORECASE),
    "interpellazione_diretta": re.compile(r"\b(tu|ti|te)\b", re.IGNORECASE),
}


def _load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _prodotti_ids() -> set[str]:
    if not os.path.exists(PRODOTTI_PATH):
        return set()
    try:
        dati = _load_json(PRODOTTI_PATH)
    except Exception:
        return set()
    return {v.get("source_video_id") for v in dati if isinstance(v, dict) and v.get("source_video_id")}


def _schemi_rilevati(titolo: str) -> list[str]:
    return [nome for nome, rx in SCHEMI_TITOLO.items() if rx.search(titolo or "")]


def costruisci_pool(min_age_hours: float) -> dict:
    prodotti = _prodotti_ids()
    per_canale = {}
    visti_id = {}
    scartati_prodotti = scartati_eta = scartati_duplicati = 0

    for path in sorted(glob.glob(os.path.join(CACHE_DIR, "*.json"))):
        nome_file = os.path.splitext(os.path.basename(path))[0]
        try:
            cache = _load_json(path)
        except Exception as e:
            print(f"[!] {nome_file}: cache illeggibile ({e}), saltato.")
            continue

        handle = cache.get("handle", "@" + nome_file).lstrip("@")
        if handle in CANALI_ESCLUSI_NON_FONTE:
            continue

        ruolo = "primaria"
        if handle in CANALI_FUORI_NICCHIA:
            ruolo = "escluso_fuori_nicchia"
        elif handle in CANALI_CAMPIONE_PICCOLO:
            ruolo = "riserva_campione_piccolo"

        candidati = []
        for v in cache.get("videos", []):
            vid = v.get("videoId")
            views = v.get("views")
            eta = v.get("age_hours")
            titolo = v.get("title") or ""
            if not vid or views is None or eta is None:
                continue
            if vid in prodotti:
                scartati_prodotti += 1
                continue
            if eta < min_age_hours:
                scartati_eta += 1
                continue
            if vid in visti_id:
                scartati_duplicati += 1
                continue
            visti_id[vid] = handle
            vph = views / max(eta, 1.0)
            candidati.append({
                "videoId": vid,
                "url": v.get("url") or f"https://www.youtube.com/watch?v={vid}",
                "title": titolo,
                "views": views,
                "age_hours": eta,
                "vph": round(vph, 2),
                "canale_sorgente": handle,
                "ruolo_canale": ruolo,
                "schemi_titolo": _schemi_rilevati(titolo),
            })

        candidati.sort(key=lambda c: -c["vph"])
        per_canale[handle] = {
            "ruolo": ruolo,
            "fetched_at": cache.get("fetched_at"),
            "n_totale_cache": len(cache.get("videos", [])),
            "n_candidati_validi": len(candidati),
            "candidati": candidati,
        }

    pool_primario = [
        c for dati in per_canale.values() if dati["ruolo"] == "primaria"
        for c in dati["candidati"]
    ]
    pool_riserva = [
        c for dati in per_canale.values() if dati["ruolo"] == "riserva_campione_piccolo"
        for c in dati["candidati"]
    ]

    return {
        "generato_il": datetime.now().isoformat(),
        "min_age_hours": min_age_hours,
        "nota_min_vph": (
            "MIN_VPH=20.0 (cashcow_check.py) NON applicato come soglia assoluta: nessun video "
            "reale in questa nicchia oggi lo raggiunge (top reale ~10-11 vph). Selezione per "
            "riga fatta per ranking relativo dentro ogni canale, non per soglia globale."
        ),
        "canali_esclusi_fuori_nicchia_oggi": sorted(CANALI_FUORI_NICCHIA),
        "canali_riserva_campione_piccolo": sorted(CANALI_CAMPIONE_PICCOLO),
        "scartati": {
            "gia_prodotti": scartati_prodotti,
            "troppo_recenti": scartati_eta,
            "duplicati_cross_canale": scartati_duplicati,
        },
        "n_pool_primario": len(pool_primario),
        "n_pool_riserva": len(pool_riserva),
        "per_canale": per_canale,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Costruisce il pool di candidati reali per il piano editoriale.")
    ap.add_argument("--min-age-hours", type=float, default=24.0)
    ap.add_argument("--out", default=None,
                     help="Path output. Default: memory/candidate_pool_70_<oggi>.json")
    args = ap.parse_args()

    out_path = args.out or os.path.join(
        FACTORY_DIR, "memory", f"candidate_pool_70_{datetime.now():%Y%m%d}.json")

    pool = costruisci_pool(args.min_age_hours)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(pool, f, ensure_ascii=False, indent=2)

    print(f"[+] Pool scritto in {out_path}")
    print(f"    Pool primario: {pool['n_pool_primario']} candidati")
    print(f"    Pool riserva (campione piccolo): {pool['n_pool_riserva']} candidati")
    print(f"    Scartati: {pool['scartati']}")
    print("\n  Per canale:")
    for handle, dati in pool["per_canale"].items():
        print(f"    {handle:32s} [{dati['ruolo']:26s}] {dati['n_candidati_validi']:>3} candidati validi "
              f"(cache: {dati['n_totale_cache']}, fetch {dati['fetched_at']})")

    if pool["n_pool_primario"] < 90:
        print(f"\n[!] Pool primario ({pool['n_pool_primario']}) sotto la soglia di margine (90) "
              f"per 70 slot su 3 strategie distinte. Vedi piano: alzare --max-video sui canali "
              f"piu' prolifici o accettare riuso controllato dello stesso canale in giorni diversi "
              f"(mai lo stesso video due volte). Mai un link inventato.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
