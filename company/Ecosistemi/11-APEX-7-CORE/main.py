"""
APEX-7 Main Entry - Sistema Completo Adaptive Prompt Execution
"""
import asyncio
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))

from memory.memory_system import seed_memory
from orchestrator.ruflo_core import RuFLOOrchestrator
from agents.planner import PlannerAgent
from agents.writer import WriterAgent
from agents.analyst import AnalystAgent
from agents.critic import CriticAgent
from agents.refiner import RefinerAgent
from agents.meta_agent import MetaAgent

async def run_apex7_system(user_input: str, context: dict = None):
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                        APEX-7 SYSTEM                         ║
║              Adaptive Prompt EXecution Engine                 ║
║                      v7.0-APEX LIVE                          ║
╠══════════════════════════════════════════════════════════════╣
║ Input: {user_input[:50]:<50} ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Init memory (seed if first time)
    try:
        mem = seed_memory()
        print("[MAIN] Memory seeded with 4 decisions + 3 strategies + architecture snapshot v7.0-APEX")
    except Exception as e:
        from memory.memory_system import APEX7Memory
        mem = APEX7Memory()
        print(f"[MAIN] Memory loaded existing (seed error: {e})")

    # Init orchestrator
    orch = RuFLOOrchestrator(memory_system=mem)
    
    # Register 6 agents
    agents = {
        "planner": PlannerAgent(),
        "writer": WriterAgent(),
        "analyst": AnalystAgent(),
        "critic": CriticAgent(),
        "refiner": RefinerAgent(),
        "meta": MetaAgent()
    }
    for name, agent in agents.items():
        agent.attach_memory(mem)
        orch.register_agent(name, agent)

    mem.set_task(user_input, context)
    
    # Execute workflow completo
    result = await orch.execute_workflow(user_input, context)
    
    print(f"""
┌──────────────────────────────────────────────────────────────┐
│ FINAL RESULT - Score: {result.get('critique_score', result.get('critique_output', {}).get('score', 'N/A'))}
│ Metrics: {orch.get_metrics()}
│ Memory: {mem.session_id}
└──────────────────────────────────────────────────────────────┘
    """)
    
    final = result.get("final_output") or result.get("writer_output") or result
    if isinstance(final, dict) and "final_output" in final:
        print("\n=== FINAL OUTPUT ===\n")
        print(str(final["final_output"])[:5000])
    elif isinstance(final, dict) and "content" in final:
        print("\n=== FINAL OUTPUT ===\n")
        print(final["content"][:5000])
    else:
        print("\n=== FINAL RESULT DUMP ===\n")
        print(str(result)[:5000])
    
    return result

if __name__ == "__main__":
    # Input dal tuo metodo
    test_input = """
    Sei il Chief Forge Architect di Digital Empire. Trasforma questi appunti grezzi:
    Voglio sistema che prende transcript call concessionari, estrae dolore lead non risposti, genera sequenza APSOC, e crea carosello Instagram 5 slide con meccanismo Risposta 27 sec -> Qualifica -> Appuntamento
    in SKILL.md eseguibile.
    """
    
    if len(sys.argv) > 1:
        test_input = " ".join(sys.argv[1:])
    
    asyncio.run(run_apex7_system(test_input))
