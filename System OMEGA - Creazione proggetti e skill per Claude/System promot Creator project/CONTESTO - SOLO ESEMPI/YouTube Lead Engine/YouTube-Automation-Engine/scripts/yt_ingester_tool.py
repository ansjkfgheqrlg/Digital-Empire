#!/usr/bin/env python3
import argparse
import json
import subprocess
import os
from pathlib import Path

def get_video_metadata(url):
    """
    Utilizza yt-dlp per estrarre i metadati di base senza scaricare il file video.
    """
    print(f"[Ingester] Estrazione metadati da: {url}")
    try:
        # Usa yt-dlp per scaricare il JSON dump (solo metadati)
        result = subprocess.run(
            ['yt-dlp', '-j', '--skip-download', url],
            capture_output=True, text=True, check=True
        )
        data = json.loads(result.stdout)
        
        metadata = {
            "title": data.get("title", ""),
            "channel": data.get("uploader", ""),
            "description": data.get("description", ""),
            "tags": data.get("tags", []),
            "view_count": data.get("view_count", 0),
            "upload_date": data.get("upload_date", ""),
            "duration": data.get("duration", 0),
            "original_url": url
        }
        return metadata
    except subprocess.CalledProcessError as e:
        print(f"[Errore] yt-dlp ha fallito: {e.stderr}")
        return None
    except FileNotFoundError:
        print("[Errore] yt-dlp non trovato. Assicurati che sia installato nel sistema (pip install yt-dlp).")
        return None

def get_video_transcript(url, output_dir):
    """
    Scarica i sottotitoli generati o manuali usando yt-dlp.
    """
    print(f"[Ingester] Download trascrizione per: {url}")
    try:
        # Comando per scaricare i sottotitoli (preferisce it, poi en, auto-generati se manuali non esistono)
        cmd = [
            'yt-dlp',
            '--skip-download',
            '--write-sub',
            '--write-auto-sub',
            '--sub-lang', 'it,en',
            '--sub-format', 'json3/vtt/srt',
            '-o', os.path.join(output_dir, '%(id)s.%(ext)s'),
            url
        ]
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"[Ingester] Sottotitoli salvati in {output_dir}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[Errore] yt-dlp non è riuscito a estrarre i sottotitoli: {e.stderr}")
        return False

def main():
    parser = argparse.ArgumentParser(description="YouTube Ingester per Automazione")
    parser.add_argument("url", help="URL del video YouTube da ingerire")
    parser.add_argument("--output", default="./ingest_output", help="Cartella di destinazione")
    
    args = parser.parse_args()
    
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Estrazione metadati per il SEO Analyst
    metadata = get_video_metadata(args.url)
    if metadata:
        meta_path = output_dir / "metadata.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4, ensure_ascii=False)
        print(f"[Ingester] Metadati SEO esportati in: {meta_path}")
    
    # Step 2: Download Trascrizione per lo Script Engineer
    get_video_transcript(args.url, output_dir)
    
    print("\n[OK] Pipeline di Ingestion completata. File pronti per l'analisi e la riscrittura.")

if __name__ == "__main__":
    main()
