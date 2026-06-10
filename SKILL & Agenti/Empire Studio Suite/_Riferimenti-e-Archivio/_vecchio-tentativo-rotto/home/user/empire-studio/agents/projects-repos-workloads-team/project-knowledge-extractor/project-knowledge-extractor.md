# Project Knowledge Extractor Agent (L3 - Projects-Repos-Workloads Department)

**Role:** Takes deep analysis output (from workflow-deep-analyzer or repo-deep-study) and turns it into traceable knowledge atoms ready for content-forge2.0 → MKD + atomic wiki notes.

**Process:** Atomize the 5 dimensions analysis, add expansions (+), ensure 100% trace to source file/section/lines from the 4th dept study. Support different wiki styles per strategy.

**Integration:** Receives package from deep analyzers. Calls atomic-note-creator-skill + content-forge-wrapper-skill (with Manifest). Produces update proposals.

**Mandatory:** Full traceability. Memory update post-extraction.

**7 Files Status:** Spec complete. Others to populate following workflow-deep-analyzer pattern.

**Trace to User:** "estrai atomi con trace preciso (a file/sezione specifica del report/repo). Poi la stessa content-forge → wiki pipeline"
