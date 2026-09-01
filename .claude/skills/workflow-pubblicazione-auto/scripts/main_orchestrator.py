import os
import sys
from instagram_bot import publish_to_instagram
from tiktok_bot import publish_to_tiktok

def main(content_dir, platform="both", headless=False):
    """
    Legge il contenuto dalla cartella specificata e lo pubblica.
    content_dir: La cartella contenente il media (.mp4 o .jpg/.png) e la caption (caption.txt)
    platform: 'instagram', 'tiktok' o 'both'
    headless: True per non vedere il browser, False per vedere le azioni
    """
    
    if not os.path.exists(content_dir):
        print(f"Errore: La cartella {content_dir} non esiste.")
        return
        
    # Trova il file media (prendiamo il primo mp4 o immagine)
    media_file = None
    for f in os.listdir(content_dir):
        if f.lower().endswith(('.mp4', '.jpg', '.jpeg', '.png')):
            media_file = os.path.join(content_dir, f)
            break
            
    if not media_file:
        print(f"Errore: Nessun file video/immagine trovato in {content_dir}.")
        return
        
    # Trova la caption
    caption_file = os.path.join(content_dir, 'caption.txt')
    if not os.path.exists(caption_file):
        print(f"Errore: File caption.txt non trovato in {content_dir}.")
        return
        
    with open(caption_file, 'r', encoding='utf-8') as f:
        caption = f.read().strip()
        
    print(f"File trovato: {media_file}")
    print(f"Caption trovata ({len(caption)} caratteri)")
    
    if platform in ['instagram', 'both']:
        print("\n=== AVVIO PUBBLICAZIONE INSTAGRAM ===")
        publish_to_instagram(media_file, caption, headless=headless)
        
    if platform in ['tiktok', 'both']:
        print("\n=== AVVIO PUBBLICAZIONE TIKTOK ===")
        # TikTok accetta solo video
        if media_file.lower().endswith('.mp4'):
            publish_to_tiktok(media_file, caption, headless=headless)
        else:
            print("Saltato TikTok: il file non è un video (.mp4).")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Pubblica automaticamente su IG e TikTok")
    parser.add_argument("folder", help="Percorso della cartella contenente media e caption.txt")
    parser.add_argument("--platform", choices=['instagram', 'tiktok', 'both'], default='both', help="Piattaforma di destinazione")
    parser.add_argument("--visible", action="store_true", help="Mostra il browser (headless=False)")
    
    args = parser.parse_args()
    
    main(args.folder, platform=args.platform, headless=not args.visible)
