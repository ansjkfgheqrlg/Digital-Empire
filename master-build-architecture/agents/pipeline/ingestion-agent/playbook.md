# Ingestion Playbook

1. Enumerate sources (single, folder, recursive, list, glob).
2. Clean each (remove filler, normalize).
3. Chunk semantic + source-aware + decision-relevant.
4. Tag every chunk with source/line + principle.
5. Fuse multi-source (detect overlaps, preserve provenance).
6. Output to memory/plans/ingestion-*.md + sources.json + atoms.json.
7. Log to memory/INDEX and handoff to analysts.