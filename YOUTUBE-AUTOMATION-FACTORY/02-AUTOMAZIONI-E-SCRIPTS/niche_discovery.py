#!/usr/bin/env python3
"""
Reparto INTELLIGENCE — agente `niche-scout` (nuovo, 2026-08-05).

Tool ADVISORY: propone sotto-nicchie/temi su cui concentrare la produzione, sulla base
dell'esperienza reale gia' misurata — non cambia mai CANALE_TARGET/PRIMARY_NICHE (stesso
principio di channel_discovery.py: proposte, non decisioni).

Perche' "sotto-nicchie dentro quella attuale" e non "nicchie nuove indovinate": una nicchia
scollegata dai dati sarebbe un'invenzione, non una proposta "sulla base dell'esperienza"
(richiesta esplicita di Max). Quello che i dati permettono di dire davvero e' quali TEMI,
fra quelli gia' misurati sul campo, hanno velocity piu' alta — un segnale concreto, non
un'idea a caso.

Fonti reali usate (nessuna generata da questo script):
- memory/channel_videos/*.json — tutti i canali gia' raccolti (via youtube_hunter_playwright.py
  o channel_discovery.py): titoli e velocity reali.
- Gli schemi TEMATICI (non stilistici) di copy_study_dosementale.SCHEMI — salute_eta,
  relazioni, religioso — riusati identici, non ridefiniti, per restare comparabili con lo
  studio gia' scritto sul canale target.

Il confronto e' aggregato su TUTTI i canali cache disponibili, non solo @dosementale: piu'
fonti ci sono (channel_discovery.py ne aggiunge), piu' il segnale e' solido. Con una sola
fonte lo dice esplicitamente nell'output — non nasconde la debolezza del campione.

Uso:
    python niche_discovery.py
    python niche_discovery.py --min-campione 5
"""
import os
import sys
import json
import glob
import argparse
import statistics
from datetime import datetime

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
FACTORY_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
CACHE_DIR = os.path.join(FACTORY_DIR, "memory", "channel_videos")
PROPOSTE_PATH = os.path.join(FACTORY_DIR, "memory", "proposte_nicchie.json")

sys.path.insert(0, SCRIPT_DIR)
import copy_study_dosementale as copy_study  # noqa: E402

# Solo gli schemi TEMATICI (argomento del video), non quelli di scrittura del titolo
# (numero_secco, domanda, comando_maiuscolo...): una sotto-nicchia e' un tema, non uno stile.
_TEMI = [s for s in copy_study.SCHEMI if s[0] in ("salute_eta", "relazioni", "religioso")]


def carica_tutti_i_canali() -> dict[str, list[dict]]:
    """Ogni canale cache -> lista video con 'vph' calcolato. Nessun dato inventato: un canale
    senza cache reale semplicemente non compare."""
    canali = {}
    for percorso in glob.glob(os.path.join(CACHE_DIR, "*.json")):
        try:
            dati = json.load(open(percorso, encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        video = [v for v in dati.get("videos", []) if v.get("views") and v.get("age_hours")]
        for v in video:
            v["vph"] = v["views"] / max(v["age_hours"], 1.0)
        if video:
            canali[dati.get("handle", os.path.basename(percorso))] = video


    return canali


def main():
    ap = argparse.ArgumentParser(description="Propone sotto-nicchie reali (advisory, non cambia CANALE_TARGET).")
    ap.add_argument("--min-campione", type=int, default=3)
    args = ap.parse_args()

    canali = carica_tutti_i_canali()
    if not canali:
        raise SystemExit("[!] Nessuna cache canale trovata in memory/channel_videos/. "
                         "Lancia prima youtube_hunter_playwright.py o channel_discovery.py.")

    tutti_i_video = [v for video in canali.values() for v in video]
    risultati = copy_study.analizza(tutti_i_video, args.min_campione)
    risultati_tematici = [r for r in risultati if r["schema"] in {t[0] for t in _TEMI}]

    proposte = []
    for r in risultati_tematici:
        if r["verdetto"] == "campione insufficiente":
            continue
        proposte.append({
            "tema": r["schema"], "descrizione": r["descrizione"],
            "delta_pct_velocity": r["delta_pct"], "verdetto": r["verdetto"],
            "n_video_con_tema": r["n_con"], "n_video_totali_campione": len(tutti_i_video),
        })
    proposte.sort(key=lambda p: -p["delta_pct_velocity"])

    os.makedirs(os.path.dirname(PROPOSTE_PATH), exist_ok=True)
    with open(PROPOSTE_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "generato": datetime.now().isoformat(),
            "canali_analizzati": sorted(canali.keys()),
            "n_video_totali": len(tutti_i_video),
            "nota": "Proposte di TEMA dentro la nicchia esistente, misurate sui canali in cache. "
                    "Non e' un cambio di nicchia: CANALE_TARGET cambia solo per decisione "
                    "esplicita di Gael/Max. Con un solo canale in cache il segnale e' debole "
                    "(vedi canali_analizzati) — piu' fonti da channel_discovery.py lo rafforzano.",
            "proposte": proposte,
        }, f, ensure_ascii=False, indent=2)

    print(f"[+] {len(canali)} canali in cache, {len(tutti_i_video)} video totali analizzati.")
    print(f"[+] {len(proposte)} temi con verdetto misurabile → {PROPOSTE_PATH}\n")
    for p in proposte:
        print(f"    {p['tema']:16} {p['delta_pct_velocity']:+7.1f}%  {p['verdetto']}  "
             f"({p['n_video_con_tema']} video)")


if __name__ == "__main__":
    main()
