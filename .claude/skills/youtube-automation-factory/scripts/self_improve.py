#!/usr/bin/env python3
"""
self_improve.py — Script per il sistema di auto-miglioramento deterministico.
Legge il registro storico 'memory/performance_logs.json', analizza le tendenze
(CTR, ritenzione, keyword fallimentari) e aggiorna 'memory/learned_rules.json'.
"""
import os
import json
from datetime import datetime

MEMORY_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "memory"))
LOGS_FILE = os.path.join(MEMORY_DIR, "performance_logs.json")
RULES_FILE = os.path.join(MEMORY_DIR, "learned_rules.json")

def load_json(file_path, default):
    if not os.path.exists(file_path):
        return default
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(file_path, data):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Errore durante il salvataggio di {file_path}: {e}")
        return False

def analyze():
    logs = load_json(LOGS_FILE, [])
    if not logs:
        # Se non ci sono log, inizializziamo learned_rules.json con una struttura vuota
        empty_rules = {
            "low_performing_keywords": [],
            "low_performing_voices": [],
            "successful_hook_types": [],
            "high_performing_tags": [],
            "dynamic_min_vph": 20.0,
            "last_updated": datetime.now().isoformat()
        }
        save_json(RULES_FILE, empty_rules)
        print("Nessun log delle performance trovato. Creato learned_rules.json vuoto.")
        return

    # Inizializziamo raccoglitori statistiche
    keywords_stats = {} # keyword -> {"runs": 0, "picco_calo": 0, "ctr_sum": 0.0}
    voices_stats = {}   # voice -> {"runs": 0, "retention_sum": 0.0}
    hooks_stats = {}    # hook_type -> {"runs": 0, "retention_sum": 0.0, "high_retention": 0}
    tags_stats = {}     # tag -> {"runs": 0, "ctr_sum": 0.0}

    for run in logs:
        keyword = run.get("keyword", "").strip().lower()
        voice = run.get("voice", "").strip()
        hook_type = run.get("hook_type", "").strip()
        tags = run.get("tags", [])
        metrics = run.get("metrics", {})
        
        vph = float(metrics.get("views_per_hour", 0.0))
        ctr = float(metrics.get("ctr", 0.0))
        retention = float(metrics.get("retention_rate", 0.0))
        curve_type = str(metrics.get("curve_type", "")).strip().lower()

        # 1) Analisi Keyword
        if keyword:
            if keyword not in keywords_stats:
                keywords_stats[keyword] = {"runs": 0, "picco_calo": 0, "ctr_sum": 0.0}
            keywords_stats[keyword]["runs"] += 1
            keywords_stats[keyword]["ctr_sum"] += ctr
            if curve_type == "picco-poi-calo":
                keywords_stats[keyword]["picco_calo"] += 1

        # 2) Analisi Voce
        if voice:
            if voice not in voices_stats:
                voices_stats[voice] = {"runs": 0, "retention_sum": 0.0}
            voices_stats[voice]["runs"] += 1
            voices_stats[voice]["retention_sum"] += retention

        # 3) Analisi Hook
        if hook_type:
            if hook_type not in hooks_stats:
                hooks_stats[hook_type] = {"runs": 0, "retention_sum": 0.0, "high_retention": 0}
            hooks_stats[hook_type]["runs"] += 1
            hooks_stats[hook_type]["retention_sum"] += retention
            if retention >= 50.0: # Soglia empirica di buona retention
                hooks_stats[hook_type]["high_retention"] += 1

        # 4) Analisi Tag
        for t in tags:
            t_clean = str(t).strip().lower()
            if t_clean:
                if t_clean not in tags_stats:
                    tags_stats[t_clean] = {"runs": 0, "ctr_sum": 0.0}
                tags_stats[t_clean]["runs"] += 1
                tags_stats[t_clean]["ctr_sum"] += ctr

    # Apprendimento delle Regole
    low_perf_keywords = []
    for kw, stats in keywords_stats.items():
        avg_ctr = stats["ctr_sum"] / stats["runs"]
        # Se più di metà delle volte fa "picco-poi-calo" o ha CTR medio < 4.0%
        if (stats["picco_calo"] / stats["runs"] >= 0.5) or (avg_ctr < 4.0):
            low_perf_keywords.append(kw)

    low_perf_voices = []
    for vc, stats in voices_stats.items():
        avg_ret = stats["retention_sum"] / stats["runs"]
        # Se la voce genera una ritenzione media inferiore al 35%
        if avg_ret < 35.0:
            low_perf_voices.append(vc)

    succ_hooks = []
    for hk, stats in hooks_stats.items():
        # Hook con tasso di successo (retention >= 50%) superiore al 60% dei casi
        success_rate = stats["high_retention"] / stats["runs"]
        if success_rate >= 0.6:
            succ_hooks.append(hk)

    high_perf_tags = []
    for tg, stats in tags_stats.items():
        # Tag associati a video con CTR medio > 7.0%
        avg_ctr = stats["ctr_sum"] / stats["runs"]
        if avg_ctr >= 7.0:
            high_perf_tags.append(tg)

    # 5) Calcolo VPH dinamico (mediana dei VPH storici, clampato tra 5.0 e 50.0)
    vph_list = []
    for run in logs:
        metrics = run.get("metrics", {})
        vph = float(metrics.get("views_per_hour", 0.0))
        if vph > 0.0:
            vph_list.append(vph)

    if vph_list:
        vph_list.sort()
        n_vph = len(vph_list)
        if n_vph % 2 == 1:
            median_vph = vph_list[n_vph // 2]
        else:
            median_vph = (vph_list[n_vph // 2 - 1] + vph_list[n_vph // 2]) / 2.0
        dynamic_min_vph = max(5.0, min(median_vph, 50.0))
    else:
        dynamic_min_vph = 20.0

    # Scrittura delle regole apprese
    rules = {
        "low_performing_keywords": sorted(low_perf_keywords),
        "low_performing_voices": sorted(low_perf_voices),
        "successful_hook_types": sorted(succ_hooks),
        "high_performing_tags": sorted(high_perf_tags),
        "dynamic_min_vph": round(dynamic_min_vph, 1),
        "last_updated": datetime.now().isoformat()
    }

    save_json(RULES_FILE, rules)
    print("Auto-miglioramento completato con successo. 'memory/learned_rules.json' aggiornato.")

if __name__ == "__main__":
    analyze()
