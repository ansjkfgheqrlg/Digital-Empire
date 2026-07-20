# yt-fliki-renderer - Tools

## Strumenti

1. **Fliki API Client** (wrapper Python)
   - `POST /v1/generate/video`
   - `GET /generate/status/{job_id}`

2. **memory_manager.py**
   ```bash
   python scripts/memory_manager.py --checkpoint "Fliki render completato" --phase 6 --trace "<run-id>"
   ```

3. **ruflo memory_store** (opzionale)

## Schema handoff
```json
{
  "in": { "script": "...", "voiceId": "it-xxx", "run_id": "..." },
  "out": { "video_path": "...", "render.json": "...", "trace": "..." }
}
```