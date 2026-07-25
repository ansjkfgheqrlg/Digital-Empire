import os
import argparse
import sys
import json
import requests

# CONFIGURAZIONE API MEDIATORE
# Sostituire con la propria API KEY (es. Ayrshare o webhook di Make.com)
API_KEY = os.environ.get("SOCIAL_API_KEY", "YOUR_API_KEY_HERE")
API_ENDPOINT = "https://app.ayrshare.com/api/post"

def get_caption(path):
    for filename in os.listdir(path):
        if filename.endswith('.txt') or filename.endswith('.md'):
            with open(os.path.join(path, filename), 'r', encoding='utf-8') as f:
                return f.read()
    return ""

def get_media_urls(path):
    # In un ambiente di produzione reale, l'API richiede spesso un URL pubblico.
    # Qui simuliamo la raccolta dei percorsi locali o la simulazione del caricamento.
    media_files = []
    for filename in sorted(os.listdir(path)):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.mp4')):
            media_files.append(os.path.join(path, filename))
    return media_files

def publish_to_social(content_path, brand):
    print(f"Inizio pubblicazione per il brand: {brand}")
    
    caption = get_caption(content_path)
    media_files = get_media_urls(content_path)
    
    if not caption or not media_files:
        print("Impossibile procedere: mancano media o caption.")
        return False
        
    print(f"Caption trovata ({len(caption)} caratteri).")
    print(f"Trovati {len(media_files)} file multimediali.")
    
    # Determina le piattaforme basandosi sul brand
    platforms = ["instagram"]
    if brand == "mentalita-brutale":
        platforms.append("tiktok")
        
    print(f"Piattaforme di destinazione: {', '.join(platforms)}")
    
    # Payload per Ayrshare (esempio)
    # Nota: per caricare file locali con Ayrshare bisogna convertirli o passarli a un server prima, 
    # oppure usare un Webhook di Make.com che accetta multipart/form-data.
    payload = {
        "post": caption,
        "platforms": platforms,
        # "mediaUrls": ["https://iltuoserver.com/immagine.jpg"] # URL pubblici
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # SIMULAZIONE DELLA CHIAMATA API
    print("Invio richiesta all'aggregatore Social API...")
    # response = requests.post(API_ENDPOINT, json=payload, headers=headers)
    
    # Per ora simuliamo un successo
    print("Pubblicazione completata con successo (SIMULATA)!")
    print(f"Dati inviati: {json.dumps(payload, indent=2)}")
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pubblica contenuto sui social.")
    parser.add_argument("--path", required=True, help="Percorso della cartella del post")
    parser.add_argument("--brand", required=True, choices=["digital-empire", "mentalita-brutale"], help="Brand di destinazione")
    
    args = parser.parse_args()
    
    success = publish_to_social(args.path, args.brand)
    if not success:
        sys.exit(1)
    sys.exit(0)
