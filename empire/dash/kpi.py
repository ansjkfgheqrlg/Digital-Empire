"""
empire.dash.kpi — Definizione dichiarativa dei KPI.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-05)
Governo: MANDATO Art.8 + ADR-008
"""
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class KPI:
    id: str
    label: str
    source: str
    fmt: str  # int, pct, mb, status, float, text
    owner: str
    good: str | None = None
    warn: str | None = None
    bad: str | None = None

    def evaluate_status(self, val: Any) -> str:
        """Ritorna lo stato visuale del KPI: green, yellow, red o gray se n/d."""
        if val is None or val == "n/d":
            return "gray"

        # Tipi di dato numerico
        try:
            num = float(val)
        except (ValueError, TypeError):
            # Se non è numerico, confronta come stringa o ritorna green come default
            return "green"

        # Valutazione formule semplici
        # es: good="== 0", warn="<= 5", bad="> 5"
        for thresh, color in [(self.good, "green"), (self.warn, "yellow"), (self.bad, "red")]:
            if not thresh:
                continue
            try:
                op, threshold_val = thresh.strip().split(" ", 1)
                threshold_num = float(threshold_val)
                if op == "==" and num == threshold_num:
                    return color
                elif op == ">" and num > threshold_num:
                    return color
                elif op == "<" and num < threshold_num:
                    return color
                elif op == ">=" and num >= threshold_num:
                    return color
                elif op == "<=" and num <= threshold_num:
                    return color
                elif op == "!=" and num != threshold_num:
                    return color
            except Exception:
                pass

        return "green"


# Definizione dichiarativa dei KPI
KPI_REGISTRY = [
    # 1. Salute Aziendale
    KPI(id="agenti_progettati", label="Agenti Progettati", source="loader.load_agents", fmt="int", owner="GAEL"),
    KPI(id="agenti_cf_grade", label="Agenti CF-Grade", source="loader.load_agents.cf_grade", fmt="int", owner="GAEL", good=">= 10"),
    KPI(id="ecosistemi_completi", label="Ecosistemi Completi", source="loader.load_ecosystems", fmt="int", owner="CLAUDE", good="== 10", warn=">= 8", bad="< 8"),
    KPI(id="artefatti_adr008", label="Conformi ADR-008", source="registry.census.provenance", fmt="int", owner="FORGE"),
    KPI(id="link_rotti", label="Link Rotti", source="registry.links.dead_end", fmt="int", owner="FORGE", good="== 0", warn="<= 5", bad="> 5"),
    KPI(id="workflow_conformi", label="Workflow Art. 8", source="registry.conform.workflow", fmt="int", owner="FORGE", good=">= 1"),
    KPI(id="spazio_sprecato", label="Spazio Duplicato", source="registry.dupes.wasted", fmt="mb", owner="FORGE", good="< 1.0", warn="<= 30.0", bad="> 30.0"),

    # 2. Performance (Telemetry)
    KPI(id="runs_giornalieri", label="Esecuzioni/gg", source="inspect.telemetry.runs", fmt="int", owner="CLAUDE"),
    KPI(id="scorecard_5d", label="Scorecard 5D", source="inspect.scorecard", fmt="float", owner="CLAUDE", good=">= 4.5", warn=">= 3.5", bad="< 3.5"),
    KPI(id="first_pass_rate", label="First-pass Rate", source="inspect.first_pass", fmt="pct", owner="CLAUDE", good=">= 90", warn=">= 75", bad="< 75"),
    KPI(id="ttd_medio", label="TTD Medio vs Bench", source="inspect.ttd", fmt="duration", owner="CLAUDE"),
    KPI(id="tip_aperti", label="TIP Aperti / Recurred", source="inspect.feedback", fmt="int", owner="CLAUDE", good="== 0", warn="<= 3", bad="> 3"),
    KPI(id="traceability_rate", label="Checkpoint Coverage", source="inspect.traceability", fmt="pct", owner="CLAUDE", good=">= 95", warn=">= 80", bad="< 80"),

    # 3. Revenue e Commerciale
    KPI(id="anticipi_incassati", label="Anticipi Chiusi", source="commercial.revenue.closed", fmt="int", owner="MAX", good=">= 5", warn=">= 2", bad="< 2"),
    KPI(id="decisioni_attive", label="Veto Scaduto", source="memory.decisions.active", fmt="int", owner="CLAUDE"),
]
