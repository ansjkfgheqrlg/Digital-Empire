"""Agent Swarm — ruoli specializzati (Planner/Writer/Analyst/Critic/Refiner/Meta).

Ogni agente è una classe con `run(ctx) -> ctx` (ctx = dizionario di stato
condiviso lungo il workflow). Gli agenti di generazione usano il Backend.
"""
from __future__ import annotations

from typing import Any

from .quality import QualityScorer


class Agent:
    role = "agent"

    def __init__(self, backend, memory):
        self.backend = backend
        self.memory = memory

    def run(self, ctx: dict) -> dict:
        raise NotImplementedError

    def _log(self, msg: str) -> None:
        print(f"  [{self.role:>7}] {msg}")


class Planner(Agent):
    role = "PLANNER"

    def run(self, ctx: dict) -> dict:
        goal = ctx["goal"]
        self._log(f"Decomposing goal: {goal}")
        ctx["task_graph"] = [
            "Define objective & constraints",
            "Gather context from memory",
            "Generate candidate solution",
            "Critique & refine",
            "Persist learnings",
        ]
        ctx["priority"] = ["critique", "generate", "context", "persist", "define"]
        return ctx


class Writer(Agent):
    role = "WRITER"

    def run(self, ctx: dict) -> dict:
        it = ctx.get("iteration", 0)
        prompt = f"GOAL: {ctx['goal']} | ITER: {it}"
        draft = self.backend.complete("You are a WRITER.", prompt)
        ctx["draft"] = draft
        self._log(f"Draft produced ({len(draft)} chars)")
        return ctx


class Analyst(Agent):
    role = "ANALYST"

    def run(self, ctx: dict) -> dict:
        analysis = self.backend.complete(
            "You are an ANALYST.", f"ANALYZE: {ctx['goal']}")
        ctx["analysis"] = analysis
        self._log("Context analysis added")
        return ctx


class Critic(Agent):
    role = "CRITIC"

    def run(self, ctx: dict) -> dict:
        # Se il backend espone `score` (es. LLMBackend), il Critic diventa
        # uno scorer vero sul draft. Altrimenti usa l'euristica mock.
        if hasattr(self.backend, "score"):
            scores = self.backend.score(
                "Sei un critico esperto. Valuta l'output su 5 dimensioni "
                "(completezza, precisione, creativita, actionability, coerenza) "
                "da 0 a 10.",
                f"GOAL: {ctx['goal']}\nDRAFT: {ctx.get('draft','')}",
            )
            ctx["critique"] = "LLM critique applicata al draft."
        else:
            it = ctx.get("iteration", 0)
            base = 5.5 + it * 0.9
            scores = {
                "completezza":   min(10, base + 0.3),
                "precisione":    min(10, base),
                "creativita":    min(10, base - 0.5),
                "actionability": min(10, base + 0.2),
                "coerenza":      min(10, base + 0.1),
            }
            ctx["critique"] = (
                f"Iteration {it}: weakest = coerenza/creativita. "
                f"Servono piu struttura e azioni concrete.")
        ctx["scores"] = scores
        self._log(f"Score = {QualityScorer().score(scores)}")
        return ctx


class Refiner(Agent):
    role = "REFINER"

    def run(self, ctx: dict) -> dict:
        it = ctx.get("iteration", 0)
        prompt = (f"GOAL: {ctx['goal']} | ITER: {it} | "
                  f"CRITIQUE: {ctx.get('critique','')}")
        improved = self.backend.complete("You are a REFINER.", prompt)
        ctx["draft"] = improved
        self._log("Draft refined")
        return ctx


class MetaAgent(Agent):
    role = "META"

    def run(self, ctx: dict) -> dict:
        self._log("Final gate + memory save")
        self.memory.update_strategy_usage("Piramide Evolutiva")
        self.memory.update_strategy_usage("Critique-Before-Output")
        return ctx
