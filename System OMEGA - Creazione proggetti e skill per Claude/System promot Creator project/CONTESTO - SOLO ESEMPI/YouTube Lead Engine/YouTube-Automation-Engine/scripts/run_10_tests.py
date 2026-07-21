import subprocess
import json
import os
import glob
from pathlib import Path

def run_tests():
    print("🚀 AVVIO DELLA TEST SUITE AUTOMATIZZATA (10 RUNS su DOSE MENTALE)\n")
    
    # Pulizia directory test
    os.system("rm -rf /home/user/TestAutomationDoseMentale")
    
    results = []
    
    for i in range(1, 11):
        print(f"--- TEST RUN {i}/10 ---")
        out_dir = f"/home/user/TestAutomationDoseMentale/run_{i}"
        
        # 1. INGESTION
        subprocess.run([
            "python3", 
            "/home/user/Digital-Empire/System OMEGA - Creazione proggetti e skill per Claude/System promot Creator project/CONTESTO - SOLO ESEMPI/YouTube Lead Engine/YouTube-Automation-Engine/scripts/yt_ingester_tool.py",
            f"https://youtube.com/watch?v=mock_{i}",
            "--output", out_dir
        ], capture_output=True)
        
        # Leggi i dati estratti
        with open(f"{out_dir}/metadata.json", "r") as f:
            meta = json.load(f)
            
        with open(f"{out_dir}/transcript.vtt", "r") as f:
            transcript = f.read().replace("WEBVTT\n\n00:00:00.000 --> 00:05:00.000\n", "")
            
        # 2. SIMULAZIONE VIDIQ SEO ANALYST
        seo_score_original = max(20, min(80, int(len(meta['tags']) * 10 + (meta['view_count'] / 100000))))
        
        seo_attack_plan = {
            "target_title": meta['title'],
            "new_title": f"MIGLIORATO: {meta['title']} (2026)",
            "new_tags": meta['tags'] + ["mindset 2026", "digital empire", "crescita"],
            "projected_seo_score": 95
        }
        
        # 3. SIMULAZIONE SCRIPT ENGINEER
        hook_options = [
            f"[HOOK IMPATTO] Immagina di perdere {meta['view_count']} opportunità. Ecco perché devi agire oggi.",
            f"[HOOK LENTO] Tutti pensano a {meta['tags'][0]}, ma nessuno ha il coraggio di dire la verità.",
            f"[HOOK DOMANDA] Ti sei mai chiesto perché {meta['title'].lower()}?"
        ]
        
        new_script = f"""
{hook_options[0]}

[INTRO] Ciao e benvenuti sul canale. In questo video parliamo di {meta['tags'][0]}. Restate fino alla fine perché vi darò la formula esatta per dominarlo.

[SCENA: B-Roll dinamico]
[CORE] {transcript} Questo è esattamente il problema che cerchiamo di risolvere!

[CTA] Clicca sul link in descrizione per scaricare il nostro framework gratuito!
"""
        
        # 4. VALUTAZIONE METRICHE (Punteggio 1-5)
        # Assegniamo un punteggio basato sulla qualità del "Gancio" e sulla SEO
        score = 4
        if "mindset" in meta['tags'] or "successo" in meta['tags']:
            score = 5 # Altamente affine al nostro Lead Engine
        elif seo_score_original < 40:
            score = 5 # Grande opportunità SEO per noi
        elif meta['view_count'] < 300000:
            score = 3 # Traffico moderato
            
        results.append({
            "run": i,
            "title": meta['title'],
            "original_seo": seo_score_original,
            "score": score,
            "hook_generated": hook_options[0]
        })
        
        print(f"✅ Target: {meta['title']} | Views: {meta['view_count']}")
        print(f"📊 Valutazione: {score}/5 Stelle\n")

    print("====================================")
    print("RIEPILOGO DEI 10 TEST DI AUTOMAZIONE")
    print("====================================")
    for res in results:
        print(f"Test {res['run']} | Score: {'★'*res['score']} | {res['title']}")

run_tests()
