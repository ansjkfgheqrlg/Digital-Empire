import os
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from GoogleDrive.drive_uploader import upload_carousel
import config

def run():
    topic_name = "Il_tuo_advertising_brucia_sold"
    local_dir = os.path.join(config.LOCAL_DOWNLOAD_DIR, topic_name)
    
    # Leggi la descrizione
    desc_path = os.path.join(local_dir, "descrizione.txt")
    descrizione = ""
    if os.path.exists(desc_path):
        with open(desc_path, "r", encoding="utf-8") as f:
            descrizione = f.read()
            
    print(f"[*] Avvio upload per {topic_name}...")
    upload_carousel(local_dir, topic_name, descrizione=descrizione, headless=True)
    print("[*] Finito.")

if __name__ == "__main__":
    run()
