"""
Lead Analyzer Orchestrator — Team DEEP-INTEL Coordinator

Coordina 3 sub-agent in parallelo + 1 agent di sintesi sequenziale.

ARCHITETTURA:
  FASE A — Parallelo (ThreadPoolExecutor):
    ├── Sub-Agent A: ResearchAgent    — scrapa sito, no AI
    ├── Sub-Agent B: CROAuditAgent    — analisi CRO via AI (dipende da Research)
    └── Sub-Agent C: CompetitorAgent  — lookup DB + AI (indipendente)

  FASE B — Sequenziale (dopo FASE A):
    └── InsightAgent — sintetizza tutti i dati in insight_brief

Gira SOLO per lead con score >= min_score E con sito web (senza sito, skip).
I lead esclusi passano direttamente al Strategist standard (nessuna analisi profonda).

Output per ogni lead analizzato:
  - website_intelligence (ResearchAgent)
  - cro_audit (CROAuditAgent)
  - competitor_intel (CompetitorAgent)
  - insight_brief (InsightAgent)
  - deep_analysis: True / False
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from agents.research   import ResearchAgent
from agents.cro_audit  import CROAuditAgent
from agents.competitor import CompetitorAgent
from agents.insight    import InsightAgent


class LeadAnalyzerOrchestrator:
    """
    Orchestratore del Team DEEP-INTEL.
    Coordina 3 sub-agent paralleli + 1 agent di sintesi per ogni lead hot/warm.
    """

    def __init__(
        self,
        openrouter_api_key: str,
        db_path: str = None,
        min_score: int = 60,
        max_workers_per_lead: int = 2,
    ):
        self.min_score = min_score
        self.max_workers = max_workers_per_lead

        self.research   = ResearchAgent()
        self.cro_audit  = CROAuditAgent(openrouter_api_key)
        self.competitor = CompetitorAgent(openrouter_api_key, db_path=db_path)
        self.insight    = InsightAgent(openrouter_api_key)

    # ──────────────────────────────────────────────────────────────────────
    # Single-lead analysis
    # ──────────────────────────────────────────────────────────────────────

    def _analyze_lead(self, lead: dict) -> dict:
        """
        Esegue la pipeline completa su un singolo lead:
        1. Research + Competitor in parallelo
        2. CRO Audit (dopo Research, usa website_intelligence)
        3. Insight synthesis (dopo tutti e 3)
        """
        nome = lead.get("page_name", "?")

        # FASE A1 — Research + Competitor in parallelo
        with ThreadPoolExecutor(max_workers=2) as ex:
            fut_research    = ex.submit(self.research.analyze, lead)
            fut_competitor  = ex.submit(self.competitor.analyze, lead)

            research_result    = fut_research.result()
            competitor_result  = fut_competitor.result()

        # FASE A2 — CRO Audit (dopo Research — usa website_intelligence)
        cro_result = self.cro_audit.audit(research_result)

        # Merge intermedio
        enriched = {
            **lead,
            "website_intelligence": research_result.get("website_intelligence", {}),
            "cro_audit":            cro_result.get("cro_audit", {}),
            "competitor_intel":     competitor_result.get("competitor_intel", {}),
        }

        # FASE B — Insight synthesis
        final = self.insight.synthesize(enriched)
        final["deep_analysis"] = True

        print(f"[LEAD_ANALYZER] ✓ {nome}")
        return final

    # ──────────────────────────────────────────────────────────────────────
    # Batch processing
    # ──────────────────────────────────────────────────────────────────────

    def run(self, leads: list) -> list:
        """
        Analizza l'intero batch.
        Lead idonei (score >= min_score + ha sito) → analisi profonda.
        Lead non idonei → fast-pass (nessuna analisi, direct to Strategist).
        """
        eligible  = [l for l in leads if l.get("score", 0) >= self.min_score and l.get("website")]
        fast_pass = [l for l in leads if l not in eligible]

        print(f"\n[LEAD_ANALYZER] {'='*55}")
        print(f"[LEAD_ANALYZER] Team DEEP-INTEL — analisi profonda lead")
        print(f"[LEAD_ANALYZER] Score soglia: {self.min_score}+  |  Con sito: richiesto")
        print(f"[LEAD_ANALYZER] Lead idonei:  {len(eligible)}")
        print(f"[LEAD_ANALYZER] Fast-pass:    {len(fast_pass)} (score basso o no sito)")

        # Fast-pass: aggiunge marker deep_analysis=False
        fast_results = [{**l, "deep_analysis": False} for l in fast_pass]

        if not eligible:
            print(f"[LEAD_ANALYZER] Nessun lead idoneo — tutti fast-pass")
            return fast_results

        # Analisi profonda: max_workers lead in parallelo
        deep_results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._analyze_lead, lead): lead
                for lead in eligible
            }
            for future in as_completed(futures):
                lead = futures[future]
                try:
                    result = future.result()
                    deep_results.append(result)
                except Exception as e:
                    nome = lead.get("page_name", "?")
                    print(f"[LEAD_ANALYZER] ✗ {nome}: {e}")
                    deep_results.append({**lead, "deep_analysis": False})

        # Merge e riordina per score (più alti prima)
        all_results = deep_results + fast_results
        all_results.sort(key=lambda x: x.get("score", 0), reverse=True)

        n_deep = sum(1 for r in all_results if r.get("deep_analysis"))
        n_insight = sum(
            1 for r in all_results
            if r.get("insight_brief", {}).get("available")
        )
        print(f"[LEAD_ANALYZER] {'='*55}")
        print(f"[LEAD_ANALYZER] Analisi profonda completata: {n_deep}/{len(leads)}")
        print(f"[LEAD_ANALYZER] Insight brief prodotti: {n_insight}/{len(leads)}")

        return all_results
