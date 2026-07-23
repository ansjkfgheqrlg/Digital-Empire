"""
🔬 ANALYST AGENT - Deep analysis & Pattern Recognition
"""
from .base_agent import BaseAgent
from typing import Dict, Any
import re

class AnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__("analyst", "Deep Analysis", "Analyst system prompt for APEX-7")

    async def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.execution_count += 1
        user_input = payload.get("input", "")
        
        analysis = {
            "intent_classification": self._classify_intent(user_input),
            "entities": self._extract_entities(user_input),
            "complexity_score": self._score_complexity(user_input),
            "memory_patterns": [],
            "recommended_strategies": [],
            "risks": []
        }

        if self.memory:
            # Pattern mining L3
            best = self.memory.get_best_strategies()
            analysis["memory_patterns"] = [{"name": s["name"], "success_rate": s.get("success_rate")} for s in best[:3]]
            # L5 knowledge
            analysis["best_practices"] = self.memory.compressed_knowledge.get("best_practices", [])[:3]
            analysis["anti_patterns_to_avoid"] = self.memory.compressed_knowledge.get("anti_patterns", [])[:3]

        # Specific analysis per type
        if "carousel" in user_input.lower() or "slide" in user_input.lower():
            analysis["slide_breakdown"] = self._analyze_carousel(user_input)
        if "cold" in user_input.lower() or "email" in user_input.lower():
            analysis["outreach_analysis"] = self._analyze_outreach(user_input)
        if len(user_input) > 1000:
            analysis["raw_notes_structure"] = self._analyze_raw_notes(user_input)

        return {
            "agent": self.name,
            "analysis": analysis,
            "timestamp": self._timestamp()
        }

    def _classify_intent(self, text: str) -> Dict:
        low = text.lower()
        scores = {
            "skill-forge": sum(1 for k in ["skill.md", "skill", "fabbrica", "appunti grezzi"] if k in low),
            "carousel-machine": sum(1 for k in ["carousel", "carosello", "slide", "grafica", "glassmorphism"] if k in low),
            "cold-outreach": sum(1 for k in ["cold", "email", "apsoc", "outreach", "sequenza"] if k in low),
            "apex-system": sum(1 for k in ["apex", "swarm", "memory", "ruflo", "architettura", "7 livelli"] if k in low)
        }
        primary = max(scores, key=scores.get) if max(scores.values()) > 0 else "generic"
        return {"primary": primary, "scores": scores, "confidence": max(scores.values())/3 if scores else 0}

    def _extract_entities(self, text: str) -> Dict:
        return {
            "target_mentioned": bool(re.search(r"destinate a:|target", text, re.I)),
            "service_mentioned": bool(re.search(r"vendergli|servizio|obiettivo", text, re.I)),
            "slide_numbers": re.findall(r"SLIDE\s*\[?\s*NUMERO\s*\]?", text, re.I),
            "has_raw_notes_placeholder": "[INSERISCI QUI" in text
        }

    def _score_complexity(self, text: str) -> int:
        length = len(text)
        placeholders = text.count("[INSERISCI")
        if length > 3000 or placeholders >=2: return 9
        if length > 1500: return 7
        if length > 500: return 5
        return 3

    def _analyze_carousel(self, text: str) -> Dict:
        slides = re.findall(r'SLIDE\s*(\d+)|slide_text|Testo esatto', text, re.I)
        return {"detected_slides": len(slides) or 1, "needs_split": len(text) > 300, "style": "glassmorphism dark luxury"}

    def _analyze_outreach(self, text: str) -> Dict:
        return {
            "framework": "APSOC" if "APSOC" in text else "unknown",
            "has_target": "TARGET" in text or "destinate" in text.lower(),
            "email_count_expected": 3,
            "constraints": ["max 100 parole email1", "mobile spacing", "tono chirurgico"]
        }

    def _analyze_raw_notes(self, text: str) -> Dict:
        lines = text.split('\n')
        return {
            "line_count": len(lines),
            "has_structure": any("LIVELLO" in l or "FASE" in l for l in lines[:20]),
            "estimated_skills_extractable": len([l for l in lines if "PROMPT" in l])
        }
