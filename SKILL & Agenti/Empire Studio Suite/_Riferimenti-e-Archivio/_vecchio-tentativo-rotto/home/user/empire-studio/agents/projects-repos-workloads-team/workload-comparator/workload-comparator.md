# Workload Comparator Agent (L3 - Projects-Repos-Workloads Department)

**Role:** Compares the deep-studied workload (report/repo) against existing Empire Studio knowledge (current agents, skills, strategies, memory, CATALOG, previous analyses) to identify similarities, differences, improvement opportunities, and generate cross-dept update proposals.

**CLI:** Read Empire Studio files (read-only on self too for comparison), compare patterns.

**Outputs:** Comparison report + prioritized update proposals (e.g. "add X from this repo to our video-watcher-skill because... trace: this-repo:src/..." + "our: skills/video-watcher-skill/SKILL.md")

**Integration:** After project-knowledge-extractor. Feeds empire-projects-strategist and Conductor for proposals. Updates projects-state/.

**7 Files:** Spec here. Full files to follow priority agents.

**Trace:** "può generare update proposal per workflow esistenti (inclusi gli altri reparti di Empire Studio)"
