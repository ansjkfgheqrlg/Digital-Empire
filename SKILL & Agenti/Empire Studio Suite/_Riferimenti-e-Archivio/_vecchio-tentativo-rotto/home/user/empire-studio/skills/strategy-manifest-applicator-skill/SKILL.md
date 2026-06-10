---
name: strategy-manifest-applicator-skill
description: 'Applies multi-strategy manifests (from generate_strategy_manifest.py) to workflows in Empire Studio. Enforces "Regola Obbligatoria: leggi Strategy Manifest" in all teams. Supports per-dept (youtube|tiktok|web|projects) strategies.'
---
# strategy-manifest-applicator-skill

**Purpose:** Read manifest, select rules/templates/decision-trees, apply to current ingestion/analysis/forge. Log application in strategy-applications/.

**Scripts:** scripts/apply_manifest.py (reads JSON, sets env vars or passes to agents, validates compliance)

**Templates:** manifest-application-log.md

**Principles:** Multiple specific strategies (not generic). Versioned. Trace which strategy used for which atom/output.

**Rules:** Mandatory before any dept work. For projects: enforce read-only + trace-mandatory + update-proposal.

**Integration:** Strategy Coordinator generates, this skill + department-strategist apply in L2 teams and L3 agents. Used in Conductor Stage 0.

**Version:** v1.0

**Trace:** "multi-strategy system (not one generic strategy), full memory... strategy-applications/strategy-versions"
