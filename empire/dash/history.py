"""
empire.dash.history — Storico dei KPI e trend temporali.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-05)
Governo: MANDATO Art.8 + ADR-008
"""
import json
import time
from pathlib import Path
from empire.paths import repo_root, rel


def get_history_dir() -> Path:
    """Ritorna la cartella destinata agli snapshot storici."""
    d = repo_root() / "empire" / ".data" / "history"
    d.mkdir(parents=True, exist_ok=True)
    return d


def save_snapshot(data: dict) -> str:
    """Salva uno snapshot dei KPI correnti con nome file basato sulla data odierna YYYY-MM-DD."""
    history_dir = get_history_dir()
    today_str = time.strftime("%Y-%m-%d")
    out_file = history_dir / f"{today_str}.json"

    # Salva solo metriche rilevanti per il trend
    snap = {
        "date": today_str,
        "timestamp": time.time(),
        "link_rotti": data.get("link_rotti", 0),
        "artefatti_adr008": data.get("artefatti_adr008", 0),
        "agenti_cf_grade": data.get("agenti_cf_grade", 0),
        "spazio_sprecato": data.get("spazio_sprecato", 0.0),
        "anticipi_incassati": data.get("anticipi_incassati", 0)
    }

    # Scrittura atomica o sovrascrittura idempotente per lo stesso giorno
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(snap, f, indent=2, ensure_ascii=False)
        
    return rel(out_file)


def get_history_trend(days: int = 14) -> dict[str, dict]:
    """Scansiona la directory degli snapshot e restituisce un dizionario ordinato per data."""
    history_dir = get_history_dir()
    trend = {}
    
    # Raccoglie tutti i file YYYY-MM-DD.json
    for p in history_dir.glob("*-*-*.json"):
        # Controlla la validità del nome
        name = p.stem
        if len(name) == 10 and name.count("-") == 2:
            try:
                with open(p, "r", encoding="utf-8") as f:
                    snap_data = json.load(f)
                trend[name] = snap_data
            except Exception:
                pass

    # Limita ai più recenti N giorni
    sorted_dates = sorted(trend.keys())[-days:]
    return {date: trend[date] for date in sorted_dates}
