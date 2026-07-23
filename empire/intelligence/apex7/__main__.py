"""Demo end-to-end di APEX-7: avvia l'Orchestrator su un goal reale e
esporta la Memory in JSON (schema spec-compliant).

Backend:
  - default: LocalMockBackend (offline)
  - se esporti OPENAI_API_KEY: usa LLMBackend reale (modello in APEX_MODEL,
    default gpt-4o-mini). Opzionale: APEX_BASE_URL per endpoint compatibili.
"""
from __future__ import annotations

import os

from .backends import LocalMockBackend, LLMBackend
from .memory import MemoryEcosystem
from .orchestrator import Orchestrator


def main() -> None:
    mem = MemoryEcosystem("apex7_demo.db")

    if os.getenv("OPENAI_API_KEY"):
        backend = LLMBackend(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=os.getenv("APEX_MODEL", "gpt-4o-mini"),
            base_url=os.getenv("APEX_BASE_URL"),
        )
        print("[APEX-7] Backend: LLM reale")
    else:
        backend = LocalMockBackend()
        print("[APEX-7] Backend: LocalMockBackend "
              "(setta OPENAI_API_KEY per usare un LLM)")

    orch = Orchestrator(memory=mem, backend=backend)

    goal = ("Genera un prompt ottimizzato per l'onboarding di un nuovo "
            "developer su Empire Desk")
    result = orch.run(goal)

    print("\n=== FINAL OUTPUT (draft) ===")
    print(result.get("draft"))
    print("\n=== ANALYSIS ===")
    print(result.get("analysis"))

    mem.export_json("apex7_memory.json")
    print("\n[OK] Memory esportata in apex7_memory.json")
    mem.close()


if __name__ == "__main__":
    main()
