import os
import argparse
import sys

def check_ready(content_path):
    print(f"Avvio scansione cartella: {content_path}")
    
    if not os.path.exists(content_path):
        print(f"Errore: La cartella {content_path} non esiste.")
        return False
        
    files = os.listdir(content_path)
    print(f"Trovati {len(files)} file nella cartella.")
    
    # Cerchiamo la caption (caption.txt o descrizione.txt)
    has_caption = any(f.endswith('.txt') or f.endswith('.md') for f in files)
    
    # Cerchiamo media (png, jpg, mp4)
    has_media = any(f.endswith(('.png', '.jpg', '.jpeg', '.mp4')) for f in files)
    
    if not has_caption:
        print("Errore: Nessun file di testo (caption) trovato.")
        
    if not has_media:
        print("Errore: Nessun file multimediale (media) trovato.")
        
    if has_caption and has_media:
        print("Cartella valida. Contenuto pronto per la pubblicazione.")
        return True
    
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verifica se una cartella è pronta per la pubblicazione.")
    parser.add_argument("--path", required=True, help="Percorso della cartella del post")
    
    args = parser.parse_args()
    
    is_ready = check_ready(args.path)
    if not is_ready:
        sys.exit(1)
    sys.exit(0)
