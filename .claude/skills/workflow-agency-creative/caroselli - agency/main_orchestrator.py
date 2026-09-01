import os
import sys
import argparse

# Forza l'output standard e degli errori a supportare UTF-8 per evitare crash con emoji su Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from Agents.orchestrator_agent import get_final_carousel_plan
from ArenaAI.arena_generator import generate_carousel_visuals
from GoogleDrive.drive_uploader import upload_carousel

def run_workflow(headless=False, custom_topic=None, count=1):
    print("==================================================")
    print(f" AVVIO WORKFLOW IBRIDO ({count} carosello/i)")
    print("==================================================")
    
    for i in range(count):
        print(f"\n>>> Generazione carosello {i+1} di {count} <<<")
        # 1. Mente: Generazione Copy con Team AI Nemotron
        slides_plan, descrizione, topic_name = get_final_carousel_plan(topic=custom_topic)
        
        if not slides_plan:
            print(f"\n[Errore] Il Team AI ha fallito la generazione del copy per il carosello {i+1}.")
            continue
            
        print("\n--- Copy Approvato dal Team AI ---")
        print(f"Argomento: {topic_name}")
        print(f"Slide Totali: {len(slides_plan)}")
        for slide in slides_plan:
            print(f"  [{slide['slide_numero']}] {slide['testo_esatto']}")
        print(f"Descrizione post:\n{descrizione}")
        print("----------------------------------\n")
        
        # 2. Braccia: Generazione Grafica su Arena.ai via Playwright
        local_folder = generate_carousel_visuals(slides_plan, topic_name, headless=headless)
        
        if not local_folder or not os.path.exists(local_folder):
            print("\n[Errore] Generazione immagini fallita o cartella locale non trovata.")
            continue
            
        # Salva la descrizione in un file locale descrizione.txt così da caricarla su Google Drive
        desc_file_path = os.path.join(local_folder, "descrizione.txt")
        try:
            with open(desc_file_path, "w", encoding="utf-8") as f:
                f.write(descrizione)
            print(f"[Orchestrator] Descrizione salvata in: {desc_file_path}")
        except Exception as err:
            print(f"[Orchestrator] Errore nel salvataggio della descrizione: {err}")
            
        # 3. Distribuzione: Upload su Google Drive
        upload_carousel(local_folder, topic_name, descrizione=descrizione, headless=headless)
        
    print("\n==================================================")
    print(" WORKFLOW COMPLETATO CON SUCCESSO! ")
    print("==================================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Workflow Ibrido Caroselli Agency")
    parser.add_argument("--visible", action="store_true", help="Mostra il browser in esecuzione")
    parser.add_argument("--topic", type=str, default=None, help="Forza un argomento specifico (es. 'Come scrivere email a freddo')")
    parser.add_argument("--count", type=int, default=1, help="Numero di caroselli da generare consecutivamente")
    args = parser.parse_args()
    
    run_workflow(headless=not args.visible, custom_topic=args.topic, count=args.count)
