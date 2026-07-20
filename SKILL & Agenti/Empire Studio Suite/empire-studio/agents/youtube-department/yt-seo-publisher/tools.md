# yt-seo-publisher - Tools

## Strumenti

1. **YouTube Data API v3** (wrapper Python)
   - videos.insert
   - thumbnails.set

2. **memory_manager.py**
   ```bash
   python scripts/memory_manager.py --checkpoint "Video pubblicato su YouTube" --phase 7 --trace "<run-id>"
   ```

3. **ruflo memory_store**

## Schema handoff
```json
{
  "in": { "video_path": "...", "title": "...", "description": "..." },
  "out": { "youtube_url": "...", "video_id": "...", "publish.json": "..." }
}
```