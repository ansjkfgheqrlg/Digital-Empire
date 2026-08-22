"""
🔍 CRITIC AGENT - Quality scoring su 5 dimensioni
"""
from .base_agent import BaseAgent
from typing import Dict, Any

QUALITY_MATRIX = {
    "Completezza": {"weight": 0.25, "threshold": 8, "metric": "Coverage"},
    "Precisione": {"weight": 0.25, "threshold": 8, "metric": "Accuracy"},
    "Creatività": {"weight": 0.20, "threshold": 7, "metric": "Novelty"},
    "Actionability": {"weight": 0.20, "threshold": 8, "metric": "Usable"},
    "Coerenza": {"weight": 0.10, "threshold": 9, "metric": "Logic"}
}

class CriticAgent(BaseAgent):
    def __init__(self):
        super().__init__("critic", "Evaluate & Score", "Critic for APEX-7")

    async def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.execution_count += 1
        # Prende output del writer
        writer_output = payload.get("writer_output") or payload.get("content") or payload.get("input", "")
        if isinstance(writer_output, dict):
            content_str = writer_output.get("content", str(writer_output))
        else:
            content_str = str(writer_output)

        dimensions = self._score_dimensions(content_str, payload)
        overall = sum(dimensions[k]["score"] * QUALITY_MATRIX[k]["weight"] for k in dimensions)

        weaknesses = [f"{k}: {v['reason']} (score {v['score']})" for k, v in dimensions.items() if v["score"] < QUALITY_MATRIX[k]["threshold"]]
        strengths = [f"{k}: {v['score']}/10" for k, v in dimensions.items() if v["score"] >= QUALITY_MATRIX[k]["threshold"]]

        critique_id = None
        if self.memory:
            critique_id = self.memory.log_critique(
                task_id=payload.get("task_id", "unknown"),
                score=overall,
                dimensions=dimensions,
                weaknesses=weaknesses
            )
            # update strategy store if score high
            if overall >= 8.0 and payload.get("intent"):
                self.memory.save_strategy(f"High-Quality {payload['intent']}", "Pattern with high critic score", [payload['intent']], {}, overall)

        return {
            "agent": self.name,
            "score": round(overall, 2),
            "dimensions": dimensions,
            "weaknesses": weaknesses,
            "strengths": strengths,
            "quality_matrix": QUALITY_MATRIX,
            "verdict": "PASS" if overall >= 7.5 else "FAIL_RETRY" if overall >= 4.0 else "FAIL_RESTART",
            "critique_id": critique_id,
            "timestamp": self._timestamp()
        }

    def _score_dimensions(self, content: str, payload: Dict) -> Dict[str, Dict]:
        length = len(content)
        # Heuristics semplici ma efficaci
        has_yaml = "---" in content and "name:" in content
        has_sections = sum(1 for s in ["# OBIETTIVO", "# TRIGGER", "# REGOLE", "# WORKFLOW"] if s in content)
        has_steps = content.count("STEP") + content.count("Email") + content.count("SLIDE")
        has_actionable = "1." in content or "2." in content

        return {
            "Completezza": {
                "score": 9 if has_sections >=4 else 8 if has_sections>=2 else 6 if length>500 else 3,
                "reason": f"Sections found {has_sections}/4, len {length}",
                "threshold": 8
            },
            "Precisione": {
                "score": 9 if has_yaml or "APSOC" in content or "glassmorphism" in content.lower() else 7 if length>300 else 4,
                "reason": "Chirurgical keywords + YAML" if has_yaml else "Generic precision",
                "threshold": 8
            },
            "Creatività": {
                "score": 8 if "Digital Empire" in content or "Piramide Evolutiva" in content else 7,
                "reason": "Original framing present" if "Digital Empire" in content else "Standard but usable",
                "threshold": 7
            },
            "Actionability": {
                "score": 9 if has_steps >=3 and has_actionable else 7 if has_actionable else 4,
                "reason": f"Steps {has_steps}, actionable {has_actionable}",
                "threshold": 8
            },
            "Coerenza": {
                "score": 9 if length>200 and not ("TODO" in content) else 6,
                "reason": "Coherent flow, no TODO placeholders" if "TODO" not in content else "Contains TODO",
                "threshold": 9
            }
        }
