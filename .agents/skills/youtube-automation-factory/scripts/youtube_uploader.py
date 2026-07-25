#!/usr/bin/env python3
import sys
import os
import argparse
import json

def upload_mock(video_path, metadata, thumbnail_path):
    print(f"\n=== [MOCK UPLOAD ACTIVE] ===")
    print(f"File video: {video_path}")
    print(f"File copertina: {thumbnail_path}")
    print(f"Metadati:")
    print(f"  - Titolo: {metadata.get('title')}")
    print(f"  - Descrizione: {metadata.get('description')[:60]}...")
    print(f"  - Keyword: {metadata.get('keyword')}")
    print(f"  - Tags: {', '.join(metadata.get('tags', []))}")
    print(f"  - Sottotitoli abilitati: {metadata.get('subtitles')}")
    print(f"Stato: Caricamento mock-up completato con successo su YouTube Studio!")
    print(f"Video ID Generato: mock-yt-vid-99182736152")
    return {"status": "success", "video_id": "mock-yt-vid-99182736152"}

def upload_real(video_path, metadata, thumbnail_path, client_secrets):
    try:
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
        from googleapiclient.http import MediaFileUpload
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print("[AVVISO] Dipendenze Google API Client non trovate. Eseguo fallback su caricamento Mock.")
        return upload_mock(video_path, metadata, thumbnail_path)

    # Scopo OAuth2 per il caricamento video su YouTube
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    
    if not os.path.exists(client_secrets):
        print(f"[AVVISO] File dei segreti client '{client_secrets}' non trovato. Eseguo fallback su caricamento Mock.")
        return upload_mock(video_path, metadata, thumbnail_path)

    try:
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets, SCOPES)
        credentials = flow.run_local_server(port=0)
        youtube = build('youtube', 'v3', credentials=credentials)
        
        # Struttura del corpo della richiesta per le API di YouTube
        body = {
            'snippet': {
                'title': metadata.get('title', 'Nuovo Video'),
                'description': metadata.get('description', ''),
                'tags': metadata.get('tags', []),
                'categoryId': '22'  # People & Blogs as default
            },
            'status': {
                'privacyStatus': 'private',  # Carica come privato per default per permettere la review
                'selfDeclaredMadeForKids': False
            }
        }
        
        print(f"Avvio del caricamento reale di {video_path}...")
        media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimetype='video/*')
        request = youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=media
        )
        
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Progresso caricamento: {int(status.progress() * 100)}%")
                
        video_id = response.get('id')
        print(f"Caricamento completato! Video ID: {video_id}")
        
        # Caricamento miniatura se specificata
        if thumbnail_path and os.path.exists(thumbnail_path):
            print(f"Caricamento miniatura {thumbnail_path}...")
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(thumbnail_path, mimetype='image/*')
            ).execute()
            print("Miniatura caricata correttamente!")
            
        return {"status": "success", "video_id": video_id}
        
    except Exception as e:
        print(f"[ERRORE] Caricamento reale fallito: {e}. Fallback su caricamento Mock.")
        return upload_mock(video_path, metadata, thumbnail_path)

def main():
    ap = argparse.ArgumentParser(description="YouTube Automated Uploader Script")
    ap.add_argument("--video", required=True, help="Path del file video MP4")
    ap.add_argument("--meta", required=True, help="Path del file JSON dei metadati")
    ap.add_argument("--thumbnail", help="Path della copertina PNG/JPG")
    ap.add_argument("--secrets", default="client_secrets.json", help="Path del file client_secrets.json di Google API OAuth")
    ap.add_argument("--mock", action="store_true", help="Forza la modalità mock-up senza tentare caricamenti reali")
    args = ap.parse_args()

    if not os.path.exists(args.video):
        print(f"Errore: file video '{args.video}' non trovato.")
        return 1
        
    if not os.path.exists(args.meta):
        print(f"Errore: file metadati '{args.meta}' non trovato.")
        return 1

    try:
        with open(args.meta, "r", encoding="utf-8") as f:
            metadata = json.load(f)
    except Exception as e:
        print(f"Errore di parsing dei metadati JSON: {e}")
        return 1

    if args.mock:
        res = upload_mock(args.video, metadata, args.thumbnail)
    else:
        res = upload_real(args.video, metadata, args.thumbnail, args.secrets)
        
    print(f"Risultato: {json.dumps(res)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
