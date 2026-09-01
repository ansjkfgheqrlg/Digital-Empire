import os
import sys

# Forza la codifica UTF-8 per stampare correttamente emoji e caratteri speciali
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

import importlib.util

def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

root_dir = os.path.dirname(__file__)

# Import dinamico per la cartella Google_Drive
drive_downloader_path = os.path.join(root_dir, "Google_Drive", "drive_downloader_mentalita.py")
drive_module = import_from_path("drive_downloader_mentalita", drive_downloader_path)
download_next_video = drive_module.download_next_video

from Core.copy_generator import generate_caption
from Instagram_Mentalita import config as mentalita_config
from Instagram_Mentalita.instagram_publisher import publish as publish_mentalita

def run_mentalita_flow(headless=False):
    os.system('') # Abilita ANSI colors su Windows
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

    print(f"{RED}==================================================")
    print(" AVVIO FLUSSO MENTALITÀ BRUTALE (Drive -> IA -> IG)")
    print(f"=================================================={RESET}")
    
    # 1. Drive: Scarica il Reel
    local_folder, topic_name = download_next_video(headless=headless)
    
    if not local_folder or not topic_name:
        print("Flusso terminato. Nessun nuovo video trovato.")
        return
        
    # Se il nome del file è generico (.mp4), impostiamo un topic descrittivo per l'AI
    if topic_name.lower() in [".mp4", "mp4", ""] or not topic_name.strip():
        topic_name = "il 90% dei tuoi problemi sono causati da una versione di te che non vuole lavorare"

        
    # Trova il file video (mp4)
    media_file = None
    for f in os.listdir(local_folder):
        if f.lower().endswith(('.mp4', '.mov', '.avi')):
            media_file = os.path.join(local_folder, f)
            break
            
    if not media_file:
        print(f"Errore: Nessun file video valido trovato in {local_folder}.")
        return
        
    # 2. AI: Genera la Caption (Team di Agenti Nemotron)
    print(f"\n--- Generazione Copy per: {topic_name} ---")
    caption = generate_caption(topic_name, brand_config=mentalita_config)
    print(f"Caption Generata:\n{caption}\n-------------------------")
    
    # 3. Pubblica su Instagram
    print("\n--- Pubblicazione su INSTAGRAM (Mentalità Brutale) ---")
    publish_mentalita(media_file, caption, headless=headless)
    
    print(f"{GREEN}\n==================================================")
    print(" FLUSSO MENTALITÀ BRUTALE COMPLETATO! ")
    print(f"=================================================={RESET}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Workflow Pubblicazione Mentalità Brutale")
    parser.add_argument("--visible", action="store_true", help="Mostra il browser in esecuzione")
    args = parser.parse_args()
    
    run_mentalita_flow(headless=not args.visible)
