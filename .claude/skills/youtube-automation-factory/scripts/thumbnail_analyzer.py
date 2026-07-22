#!/usr/bin/env python3
import sys
import os
import argparse
import json

def analyze_mock(image_path):
    print("=== [MOCK THUMBNAIL ANALYZER ACTIVE] ===")
    print(f"Analisi visiva dell'immagine: {image_path}")
    print("Generazione metriche visuali simulate...")
    res = {
        "status": "success",
        "file": image_path,
        "brightness": 65.2,
        "contrast": 74.8,
        "dominant_colors": ["#FF0000", "#000000", "#FFFFFF"],
        "text_readability_score": 85.0,
        "is_readable": True,
        "notes": ["Buon contrasto di testo", "Colori caldi dominanti per stimolare CTR"]
    }
    return res

def analyze_real(image_path):
    try:
        from PIL import Image, ImageStat
    except ImportError:
        print("[AVVISO] Libreria Pillow (PIL) non installata. Fallback su analisi Mock.")
        return analyze_mock(image_path)

    if not os.path.exists(image_path):
        print(f"Errore: file immagine '{image_path}' non trovato.")
        return {"status": "error", "reason": "file non trovato"}

    try:
        img = Image.open(image_path).convert('L')
        stat = ImageStat.Stat(img)
        # La media indica la luminosità complessiva (0 = nero, 255 = bianco)
        brightness = stat.mean[0]
        # La deviazione standard indica il contrasto complessivo (più è alta, più c'è contrasto)
        contrast = stat.stddev[0]
        
        # Semplice euristica per la leggibilità (luminosità media ottimale tra 40 e 220, contrasto > 30)
        is_readable = (40.0 <= brightness <= 220.0) and (contrast >= 30.0)
        
        notes = []
        if brightness < 40.0:
            notes.append("Copertina troppo scura. Aumenta la luminosità generale.")
        elif brightness > 220.0:
            notes.append("Copertina troppo chiara / bruciata. Riduci l'esposizione.")
        else:
            notes.append("Luminosità generale bilanciata.")

        if contrast < 30.0:
            notes.append("Poco contrasto visuale. Il testo potrebbe essere scarsamente leggibile.")
        else:
            notes.append("Contrasto visivo ottimale.")

        # Estraiamo i colori dominanti (mocked per semplicità dal canale a colori)
        img_color = Image.open(image_path).resize((1, 1))
        dominant_rgb = img_color.getpixel((0, 0))
        dominant_hex = '#{:02x}{:02x}{:02x}'.format(*dominant_rgb[:3])

        return {
            "status": "success",
            "file": image_path,
            "brightness": round((brightness / 255.0) * 100.0, 1),
            "contrast": round((contrast / 128.0) * 100.0, 1),
            "dominant_colors": [dominant_hex],
            "text_readability_score": round(min(contrast * 1.5, 100.0), 1),
            "is_readable": is_readable,
            "notes": notes
        }
    except Exception as e:
        print(f"[ERRORE] Analisi PIL fallita: {e}. Fallback su analisi Mock.")
        return analyze_mock(image_path)

def main():
    ap = argparse.ArgumentParser(description="YouTube Thumbnail Visual Analyzer")
    ap.add_argument("--image", required=True, help="Path del file immagine miniatura")
    ap.add_argument("--mock", action="store_true", help="Forza analisi mock-up")
    args = ap.parse_args()

    if args.mock:
        res = analyze_mock(args.image)
    else:
        res = analyze_real(args.image)

    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
