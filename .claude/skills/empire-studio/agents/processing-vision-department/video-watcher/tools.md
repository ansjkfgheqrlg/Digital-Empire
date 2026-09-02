# video-watcher - Tools

## Strumenti che usa
1. **frame_extractor.py** (via frame-extractor-skill) - prerequisito: produce i PNG.
   ```
   python scripts/frame_extractor.py --run <run-id> --max-frames 12 --height 360
   ```
   Output: `runs/<run-id>/frames/frame-NNN.png` + `frames/manifest.json`.

2. **Read (visione nativa di Claude)** - lo strumento chiave. L'agente apre ogni
   PNG e lo VEDE. Non c'e' comando shell: e' la capacita' multimodale di Claude.
   Per ogni `frame-NNN.png` -> Read -> descrizione reale.

3. **transcript** - `runs/<run-id>/<id>.<lang>.vtt` (da yt_ingest) per la sincronia
   testo/immagine.

4. **memory_manager.py** - per i checkpoint a fine visione.
   ```
   python scripts/memory_manager.py --checkpoint "video <id> guardato: N frame, M atomi visivi" --phase 3 --trace "video <id>"
   ```

## Schema input (handoff in)
```json
{ "run_id": "run-...", "video_id": "...", "frames_dir": "runs/.../frames",
  "manifest": "frames/manifest.json", "transcript": "runs/.../id.en.vtt" }
```

## Schema output (video-analysis + atoms.json)
```json
{ "video_id": "...", "frames_seen": 12,
  "visual_timeline": [
    {"frame": "frame-003.png", "timestamp": "0:12:34", "chapter": "...",
     "visual_description": "<cio' che Claude ha visto>",
     "key_passage": "<cio' che il testo non dice>"}
  ],
  "atoms": [ {"atom": "...", "trace": "<id>#0:12:34 + frame-003.png",
              "source_type": "visual+transcript", "inferred": false} ] }
```

## Regola
Se un frame e' nero/illeggibile o il Read fallisce, l'agente NON inventa: segnala
il frame come "non leggibile" e procede con gli altri (vedi failure-modes.md).
