---
name: atomic-note-creator-skill
description: 'Creates atomic wiki notes from knowledge atoms (with full traceability) for content-forge output in Empire Studio. Ensures MKD + atomic notes pipeline. Used across all 4 departments.'
---
# atomic-note-creator-skill

**Purpose:** Turn extracted atoms (from video, web, or 4th dept deep study) into Obsidian-style atomic notes: one concept per note, wikilinks, MOC, source trace headers.

**Scripts:** scripts/create_atomic_note.py (takes atom JSON, produces .md with frontmatter trace + content)

**Templates:** atomic-note-template.md (includes "Trace: file:XXX lines:YY | Strategy: v1.1 | Timestamp: ...")

**Principles:** From content-forge2.0: every atom expanded (+), no summary, full traceability. Supports different wiki implementation styles per strategy (marketing vs projects).

**Rules:** One atom = one note. Header with exact trace. Link back to source video ID or report file.

**Integration:** Called by content-forge-wrapper-skill or project-knowledge-extractor after atom extraction. Part of Forge Team.

**Version:** v1.0

**Trace:** "content-forge2.0 to produce MKD + atomic wiki notes (with full traceability)"
