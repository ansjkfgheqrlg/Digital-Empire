---
name: visual-analyzer-skill
description: 'Detailed visual "passaggi mostrati" analysis skill for frames extracted from videos or "screenshots" of reports/repos (for 4th dept). CLI + optional OCR. Part of Empire Studio multi-strategy visual depth requirement.'
---
# visual-analyzer-skill

**Purpose:** Analyze extracted frames or document "screenshots" (for projects dept: render key md sections as text "frames"). Produce >60 word descriptions per visual. Identify "passaggi che si mostrano" (steps, UI, diagrams, code structures shown).

**Scripts:** scripts/analyze_visual.py (describe frame using rules from youtube-design-system-strategy-v1.1 or projects-strategy)

**Templates:** visual-report-template.md

**Principles:** Depth over breadth. Every visual tied to source timestamp or file:section trace. For 4th dept: treat report sections as "frames".

**Rules:** Description must include context, what is shown, implications for knowledge. No generic. For videos: link to "come funziona" dimension.

**Integration:** After frame-extractor. Feeds video-watcher or workflow-deep-analyzer (for projects "visual" of architecture diagrams in reports).

**Version:** v1.0

**Trace to User:** "passaggi che si mostrano" + "il video deve essere visto"
