import os
import sys

from Google_Drive.drive_downloader import download_next_carousel
from Core.copy_generator import generate_caption
from Instagram.instagram_publisher import publish as publish_ig
from LinkedIn.linkedin_publisher import publish as publish_linkedin

def run_agency_flow(headless=False):
    print("==================================================")
    print(" AVVIO FLUSSO AGENCY (Drive -> IA -> IG -> LinkedIn)")
    print("==================================================")
    
    local_folder, topic_name = download_next_carousel(headless=headless)
    
    if not local_folder or not topic_name:
        print("Flusso terminato. Nessun nuovo contenuto trovato.")
        return
        
    media_file = None
    for f in os.listdir(local_folder):
        if f.lower().endswith(('.pdf', '.mp4', '.jpg', '.jpeg', '.png')):
            media_file = os.path.join(local_folder, f)
            break
            
    if not media_file:
        print(f"Errore: Nessun file valido trovato in {local_folder}.")
        return
        
    print(f"\n--- Generazione Copy per: {topic_name} ---")
    caption = generate_caption(topic_name)
    print(f"Caption Generata:\n{caption}\n-------------------------")
    
    print("\n--- Pubblicazione su INSTAGRAM ---")
    publish_ig(media_file, caption, headless=headless)
    
    # print("\n--- Pubblicazione su LINKEDIN ---")
    # publish_linkedin(media_file, caption, headless=headless)
    
    print("\n==================================================")
    print(" FLUSSO AGENCY COMPLETATO CON SUCCESSO! ")
    print("==================================================")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Workflow Pubblicazione Agency")
    parser.add_argument("--visible", action="store_true", help="Mostra il browser in esecuzione")
    args = parser.parse_args()
    
    run_agency_flow(headless=not args.visible)
