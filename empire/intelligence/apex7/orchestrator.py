"""Meta-Orchestrator (APEX-7 core).

Flusso:
  GOAL -> Planner -> [Writer || Analyst] -> Critic
       -> (score >= threshold ? OUTPUT : Refiner) x N -> Meta-Agent -> Memory
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from .agents import (Planner, Writer, Analyst, Critic, Refiner, MetaAgent)
from .backends import LocalMockBackend
from .memory import MemoryEcosystem
from .quality import QualityScorer

SEED_STRATEGIES = [
    ("Piramide Evolutiva", "Ogni livello migliora il precedente",
     ["planning", "architecture"]),
    ("Critique-Before-Output", "Auto-critica obbligatoria prima di ogni output",
     ["quality_control", "all_outputs"]),
    ("Memory-First Design", "Ogni azione memorizzata con contesto",
     ["system_design", "persistence"]),
]


class Orchestrator:
    def __init__(self, memory: MemoryEcosystem | None = None,
                 backend=None, max_refinements: int = 3,
                 pass_threshold: float = 7.5):
        self.memory = memory or MemoryEcosystem()
        self.backend = backend or LocalMockBackend()
        self.scorer = QualityScorer()
        self.max_refinements = max_refinements
        self.pass_threshold = pass_threshold
        self._seed()

    def _seed(self) -> None:
        for name, desc, app in SEED_STRATEGIES:
            self.memory.add_strategy(name, desc, app)

    def run(self, goal: str) -> dict:
        print(f"\n=== APEX-7 ORCHESTRATOR ===\nGOAL: {goal}\n")
        self.memory.set_working(task=goal, phase="INTAKE",
                                agents=["planner"])
        self.memory.record_decision(
            "Avvio workflow apex7_prompt_generation",
            "Produrre output di qualita con loop critica/refine + memoria",
            ["Risposta singola senza loop", "Nessuna memoria persistente"],
            confidence=0.9,
        )

        ctx = {"goal": goal, "iteration": 0}
        ctx = Planner(self.backend, self.memory).run(ctx)

        final = None
        for i in range(self.max_refinements + 1):
            ctx["iteration"] = i
            self.memory.set_working(phase=f"EXECUTION iter {i}",
                                    agents=["writer", "analyst", "critic"])

            # STAGE 2: esecuzione PARALLELA Writer + Analyst
            with ThreadPoolExecutor(max_workers=2) as ex:
                fw = ex.submit(Writer(self.backend, self.memory).run, dict(ctx))
                fa = ex.submit(Analyst(self.backend, self.memory).run, dict(ctx))
                ctx = fw.result()
                ctx.update(fa.result())

            # STAGE 3: Critic
            ctx = Critic(self.backend, self.memory).run(ctx)
            score = self.scorer.score(ctx["scores"])
            print(f"  >> Iteration {i} score: {score}")

            if self.scorer.passed(ctx["scores"], self.pass_threshold):
                print("  >> Score >= soglia -> OUTPUT")
                final = ctx
                break

            if i < self.max_refinements:
                print("  >> Sotto soglia -> Refine...")
                ctx = Refiner(self.backend, self.memory).run(ctx)
            else:
                print("  >> Max refinements raggiunti -> OUTPUT (best effort)")
                final = ctx

        # STAGE 5: Meta-Agent (gate + persist)
        final = MetaAgent(self.backend, self.memory).run(final)
        self.memory.add_snapshot(
            "v7.0-APEX", "Full system con swarm + memory", score, "current")
        self.memory.set_working(phase="DONE", agents=[])
        return final
