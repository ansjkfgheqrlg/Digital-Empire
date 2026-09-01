# Evals — workflow-router

## PASS se:
- [ ] INGEST_LINK → yt_ingest.py lanciato con URL corretto
- [ ] run-id generato, windows-safe (no spazi, no caratteri speciali)
- [ ] frame_extractor.py lanciato con --interval 2
- [ ] routing-result.json scritto

## FAIL se:
- [ ] URL non passato a yt_ingest.py
- [ ] --interval 2 mancante in frame_extractor call
- [ ] run-id non generato
