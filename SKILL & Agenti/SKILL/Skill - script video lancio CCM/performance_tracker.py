#!/usr/bin/env python3
"""
Performance Tracker — Digital Empire / Claude Code Mastery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Questo modulo è specializzato unicamente sull'analitica social.
A differenza di lancio_updater (che traccia i KPI finanziari e di funnel),
il performance_tracker.py è un CRM analitico per gli script video pubblicati.
Calcola Engagement Rate, Save Rate e scova quali Hook performano meglio.

Uso:
    python performance_tracker.py log --id script_01 --platform IG --views 1500 --saves 30
    python performance_tracker.py report
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

sys.stdout.reconfigure(encoding='utf-8')

PERFORMANCE_DB_PATH = Path("social_performance.json")

class PerformanceTracker:
    def __init__(self):
        self.db = self._load_db()

    def _load_db(self) -> List[Dict]:
        if PERFORMANCE_DB_PATH.exists():
            with open(PERFORMANCE_DB_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save_db(self):
        with open(PERFORMANCE_DB_PATH, "w", encoding="utf-8") as f:
            json.dump(self.db, f, ensure_ascii=False, indent=4)

    def calculate_metrics(self, data: Dict) -> Dict:
        """Calcola i KPI automatici in base ai dati grezzi inseriti."""
        views = float(data.get("views", 0))
        likes = float(data.get("likes", 0))
        comments = float(data.get("comments", 0))
        saves = float(data.get("saves", 0))
        shares = float(data.get("shares", 0))

        if views == 0:
            return data

        engagement_total = likes + comments + saves + shares
        
        data["engagement_rate_pct"] = round((engagement_total / views) * 100, 2)
        data["save_rate_pct"] = round((saves / views) * 100, 2)
        
        # Una metrica interna Custom per definire il peso virale (Save & Shares pesano di più).
        weighted_score = (likes * 1) + (comments * 2) + (shares * 3) + (saves * 4)
        data["viral_score"] = round(weighted_score, 2)

        return data

    def log_performance(
        self, 
        script_id: str, 
        platform: str, 
        hook_type: str, 
        views: int,
        likes: int = 0,
        comments: int = 0,
        saves: int = 0,
        shares: int = 0
    ):
        """Registra e aggiorna una prestazione."""
        
        # Cerca se esiste già il log per ID e Piattaforma per poter fare un update
        existing = next((item for item in self.db if item["script_id"] == script_id and item["platform"] == platform), None)
        
        data = {
            "script_id": script_id,
            "platform": platform,
            "hook_type": hook_type,
            "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "views": views,
            "likes": likes,
            "comments": comments,
            "saves": saves,
            "shares": shares
        }

        data = self.calculate_metrics(data)

        if existing:
            existing.update(data)
            print(f"✅ Aggiornate metriche per script '{script_id}' su {platform}.")
        else:
            self.db.append(data)
            print(f"✅ Nuovo log registrato: '{script_id}' su {platform}.")

        self._save_db()

    def generate_report(self):
        """Genera un report dettagliato in console."""
        if not self.db:
            print("⚠️ Nessun dato ancora registrato. Esegui log prima.")
            return

        print("="*60)
        print("  SOCIAL PERFORMANCE REPORT — EMPIRE ANALYTICS")
        print("="*60)
        
        total_views = sum(int(item.get("views", 0)) for item in self.db)
        total_saves = sum(int(item.get("saves", 0)) for item in self.db)
        
        print(f"\n📊 METRICHE GLOBALI")
        print(f"  Totale Visualizzazioni  : {total_views}")
        print(f"  Totale Salvataggi       : {total_saves}")
        print(f"  Script analizzati       : {len(self.db)}")
        
        hook_perf = {}
        for item in self.db:
            ht = item["hook_type"]
            if ht not in hook_perf:
                hook_perf[ht] = {"views": 0, "saves": 0, "count": 0}
            hook_perf[ht]["views"] += item["views"]
            hook_perf[ht]["saves"] += item["saves"]
            hook_perf[ht]["count"] += 1

        print(f"\n🏆 PERFORMANCE PER TIPO DI HOOK")
        for ht, metrics in hook_perf.items():
            if metrics["views"] > 0:
                avg_save_rate = round((metrics["saves"] / metrics["views"]) * 100, 2)
            else:
                avg_save_rate = 0.0
            print(f"  [{ht.upper()}] — Usa in {metrics['count']} video | Save Rate: {avg_save_rate}%")
        
        # Ordina per Viral Score
        sorted_db = sorted(self.db, key=lambda x: x.get("viral_score", 0), reverse=True)
        
        print(f"\n🔥 TOP 3 SCRIPT PIÙ PERFORMANTI (Per Viral Score)")
        for i, item in enumerate(sorted_db[:3]):
            print(f"  {i+1}. {item['script_id']} ({item['platform']}) | Views: {item['views']} | Viral Score: {item.get('viral_score', 0)}")
        
        print("\n" + "="*60)


def demo():
    tracker = PerformanceTracker()
    tracker.log_performance("demo_script_1", "TikTok", "Affermazione_Shock", 3000, 150, 10, 45, 5)
    tracker.log_performance("demo_script_1", "IG_Reel", "Affermazione_Shock", 1200, 60, 4, 30, 2)
    tracker.log_performance("demo_script_2", "TikTok", "Lista_Risorse", 8000, 400, 30, 200, 40)
    tracker.generate_report()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Performance Tracker per Video Scripts")
    parser.add_argument("command", choices=["log", "report", "demo"], help="Azione da eseguire")
    
    # Argomenti per il "log"
    parser.add_argument("--id", help="ID/Nome identificativo dello script")
    parser.add_argument("--platform", choices=["TikTok", "IG_Reel", "YouTube"], help="Piattaforma social")
    parser.add_argument("--hook_type", default="Generico", help="Il tipo di hook (Affermazione_Shock, Tutorial, etc.)")
    parser.add_argument("--views", type=int, default=0)
    parser.add_argument("--likes", type=int, default=0)
    parser.add_argument("--comments", type=int, default=0)
    parser.add_argument("--saves", type=int, default=0)
    parser.add_argument("--shares", type=int, default=0)
    
    args = parser.parse_args()

    tracker = PerformanceTracker()

    if args.command == "demo":
        demo()
    elif args.command == "report":
        tracker.generate_report()
    elif args.command == "log":
        if not args.id or not args.platform:
            print("Errore: Durante un 'log' devi fornire almeno --id, --platform e --views.")
            exit(1)
        tracker.log_performance(
            args.id, args.platform, args.hook_type,
            args.views, args.likes, args.comments, args.saves, args.shares
        )
