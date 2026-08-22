"""
arena_generator.py - Automazione Arena.ai per 3 stream ad alto ROI
Compatibile con GPT-4o / Claude 3.5 Sonnet su Arena
Implementa orchestrazione parallela dei 3 prompt chirurgici
"""
import json
import asyncio
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import uuid

BASE_DIR = Path(__file__).parent
PROMPTS_FILE = BASE_DIR / "prompts" / "arena_prompts.json"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Import APEX-7 components
from memory.memory_system import APEX7Memory, seed_memory
from orchestrator.ruflo_core import RuFLOOrchestrator
from agents.planner import PlannerAgent
from agents.writer import WriterAgent
from agents.analyst import AnalystAgent
from agents.critic import CriticAgent
from agents.refiner import RefinerAgent
from agents.meta_agent import MetaAgent

class ArenaClient:
    """
    Client per Arena.ai - Supporta sia vera API che simulazione locale
    Per uso reale: imposta ARENA_API_KEY env var e endpoint Arena
    """
    def __init__(self, model_preference: str = "GPT-4o", api_key: str = None):
        self.model = model_preference
        self.api_key = api_key or os.getenv("ARENA_API_KEY")
        self.simulation_mode = not bool(self.api_key)
        if self.simulation_mode:
            print(f"[ARENA CLIENT] No API key found - Running in SIMULATION mode with local APEX-7 agents ({self.model} prompt style)")

    async def generate(self, prompt_template: str, variables: Dict[str, str], stream_id: str) -> Dict[str, Any]:
        """
        Genera su Arena. Se no API key, usa swarm locale che simula GPT-4o/Claude 3.5
        """
        # Replace variables in template
        final_prompt = prompt_template
        for k, v in variables.items():
            final_prompt = final_prompt.replace(f"[{k}]", str(v)).replace(f"[{k.upper()}]", str(v)).replace(f"[INSERISCI {k.upper()}]", str(v)).replace(f"[INSERISCI TESTO SLIDE]", str(v) if k=="slide_text" else final_prompt)
            final_prompt = final_prompt.replace(f"[NUMERO]", str(v) if k=="slide_number" else final_prompt)
            final_prompt = final_prompt.replace(f"[INSERISCI TARGET, es. Concessionari Auto del Nord Italia]", variables.get("target", ""))
            final_prompt = final_prompt.replace(f"[INSERISCI SERVIZIO, es. Un sistema AI per convertire i lead in appuntamenti in showroom]", variables.get("service", ""))
            final_prompt = final_prompt.replace(f"[INSERISCI TARGET", variables.get("target",""))
            final_prompt = final_prompt.replace(f"[INSERISCI SERVIZIO", variables.get("service",""))

        if self.simulation_mode:
            # Usa APEX-7 swarm locale come mock di Arena GPT-4o
            # Questo permette di testare workflow completo senza API key
            await asyncio.sleep(0.5)  # simula latenza API
            return {
                "model": self.model,
                "stream": stream_id,
                "prompt_used": final_prompt[:200] + "...",
                "simulated": True,
                "note": "Output generato da APEX-7 local swarm (mock Arena - imposta ARENA_API_KEY per chiamata reale)"
            }
        else:
            # Qui implementare chiamata reale Arena.ai API
            # Esempio pseudocodice:
            # import aiohttp
            # async with aiohttp.ClientSession() as session:
            #   async with session.post("https://arena.ai/api/generate", headers={"Authorization": f"Bearer {self.api_key}"}, json={"model": self.model, "prompt": final_prompt}) as resp:
            #       data = await resp.json()
            #       return data
            import aiohttp
            async with aiohttp.ClientSession() as session:
                payload = {
                    "model": self.model,
                    "prompt": final_prompt,
                    "stream": stream_id,
                    "temperature": 0.7
                }
                try:
                    async with session.post("https://arena.ai/api/v1/generate", headers={"Authorization": f"Bearer {self.api_key}"}, json=payload, timeout=60) as resp:
                        result = await resp.json()
                        return result
                except Exception as e:
                    print(f"[ARENA API ERROR] {e} - fallback to simulation")
                    return {"error": str(e), "fallback": True, "prompt": final_prompt[:200]}

class ArenaGenerator:
    def __init__(self, model: str = "GPT-4o"):
        self.model = model
        self.prompts_config = json.loads(PROMPTS_FILE.read_text(encoding='utf-8'))
        self.client = ArenaClient(model_preference=model)
        self.memory = APEX7Memory()
        self.orchestrator = RuFLOOrchestrator(memory_system=self.memory)
        self._register_agents()

    def _register_agents(self):
        agents = {
            "planner": PlannerAgent(),
            "writer": WriterAgent(),
            "analyst": AnalystAgent(),
            "critic": CriticAgent(),
            "refiner": RefinerAgent(),
            "meta": MetaAgent()
        }
        for name, agent in agents.items():
            agent.attach_memory(self.memory)
            self.orchestrator.register_agent(name, agent)
        self.agents = agents

    async def run_skill_forge(self, raw_notes: str) -> Dict:
        """Stream S0 - Fabbrica delle Skill"""
        print(f"\n[STREAM S0] Skill-Forge - Model: {self.model}")
        template = next(p["template"] for p in self.prompts_config["prompts"] if p["id"] == "skill-forge")
        variables = {"raw_notes": raw_notes}
        
        # Esegui via orchestrator APEX-7
        result = await self.orchestrator.execute_workflow(
            user_input=f"SKILL-FORGE: {raw_notes[:200]}",
            context={"raw_notes": raw_notes, "intent": "skill-forge"}
        )
        
        # Salva output
        out_dir = OUTPUT_DIR / "skill-forge"
        out_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        writer_out = result.get("writer_output") or result.get("final_output") or {}
        content = writer_out.get("content") if isinstance(writer_out, dict) else str(writer_out)
        
        (out_dir / f"SKILL_{timestamp}.md").write_text(content, encoding='utf-8')
        print(f"[S0] Saved SKILL to {out_dir / f'SKILL_{timestamp}.md'}")
        return result

    async def run_carousel_machine(self, slides_texts: List[str]) -> Dict:
        """Stream S1 - Macchina Caroselli Massiva"""
        print(f"\n[STREAM S1] Carousel Machine - {len(slides_texts)} slides - Model: {self.model}")
        template = next(p["template"] for p in self.prompts_config["prompts"] if p["id"] == "carousel-machine")
        
        tasks = []
        for i, text in enumerate(slides_texts, 1):
            variables = {"slide_number": str(i), "slide_text": text}
            tasks.append(self._generate_single_slide(template, variables, i))
        
        # Esecuzione parallela massiva
        results = await asyncio.gather(*tasks)
        
        out_dir = OUTPUT_DIR / "carousel" / f"set_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        out_dir.mkdir(exist_ok=True)
        for i, res in enumerate(results, 1):
            (out_dir / f"slide_{i}_prompt.txt").write_text(res["final_prompt"], encoding='utf-8')
            # In modalità reale, qui salveresti l'immagine generata da Arena
            # res contiene image URL o base64
        
        print(f"[S1] Saved {len(results)} slide prompts to {out_dir}")
        return {"slides": results, "output_dir": str(out_dir)}

    async def _generate_single_slide(self, template: str, variables: Dict, slide_num: int):
        final_prompt = template.replace("[NUMERO]", str(variables["slide_number"])).replace("[INSERISCI TESTO SLIDE]", variables["slide_text"])
        core_result = await self.orchestrator.execute_workflow(
            user_input=f"CAROUSEL SLIDE {slide_num}: {variables['slide_text']}",
            context={"slide_text": variables["slide_text"], "slide_number": slide_num, "intent": "carousel-machine"}
        )
        arena_res = await self.client.generate(template, variables, f"S1-slide-{slide_num}")
        return {"slide": slide_num, "final_prompt": final_prompt, "apex_result": core_result, "arena": arena_res}

    async def run_cold_outreach(self, target: str, service: str) -> Dict:
        """Stream S2 - Cold Outreach APSOC"""
        print(f"\n[STREAM S2] Cold Outreach APSOC - Target: {target} - Model: {self.model}")
        template = next(p["template"] for p in self.prompts_config["prompts"] if p["id"] == "cold-outreach")
        variables = {"target": target, "service": service}
        
        result = await self.orchestrator.execute_workflow(
            user_input=f"COLD OUTREACH per {target} vendergli {service} framework APSOC",
            context={"target": target, "service": service, "intent": "cold-outreach"}
        )
        
        out_dir = OUTPUT_DIR / "outreach" / f"{target.replace(' ', '_')[:20]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        out_dir.mkdir(exist_ok=True)
        writer_out = result.get("writer_output") or {}
        content = writer_out.get("content") if isinstance(writer_out, dict) else str(writer_out)
        (out_dir / "sequenza_apsoc.txt").write_text(content, encoding='utf-8')
        
        arena_res = await self.client.generate(template, variables, "S2-cold-outreach")
        
        print(f"[S2] Saved sequence to {out_dir / 'sequenza_apsoc.txt'}")
        return {"result": result, "arena": arena_res, "output_dir": str(out_dir)}

    async def run_all_parallel(self, skill_raw_notes: str = None, carousel_texts: List[str] = None, outreach_target: str = None, outreach_service: str = None):
        """Esecuzione parallela di tutti e 3 gli stream - massima ROI"""
        print(f"\n{'='*60}\n[APEX-7] RUNNING ALL 3 STREAMS IN PARALLEL - Model: {self.model}\n{'='*60}")
        tasks = []
        if skill_raw_notes:
            tasks.append(self.run_skill_forge(skill_raw_notes))
        if carousel_texts:
            tasks.append(self.run_carousel_machine(carousel_texts))
        if outreach_target and outreach_service:
            tasks.append(self.run_cold_outreach(outreach_target, outreach_service))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        print(f"\n[APEX-7] All streams completed. Metrics: {self.orchestrator.get_metrics()}")
        self.memory.persist()
        return results


# CLI Usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="APEX-7 Arena Generator")
    parser.add_argument("--model", default="GPT-4o", choices=["GPT-4o", "Claude 3.5 Sonnet"], help="Modello Arena da usare")
    parser.add_argument("--demo", action="store_true", help="Lancia demo completa con dati esempio")
    args = parser.parse_args()

    async def demo():
        gen = ArenaGenerator(model=args.model)
        # Dati esempio
        raw_notes = """
        Voglio un sistema che prenda appunti da call con clienti concessionari, estragga automatico follow-up, crei task in CRM, e invii email personalizzata con meccanismo AI
        """
        carousel = [
            "IL LEAD E' MORTO IN 5 MINUTI",
            "73% dei lead chiama il competitor",
            "RISPOSTA IN 27 SECONDI = +38% APPUNTAMENTI",
            "NON UN CHATBOT, UN MECCANISMO",
            "Rispondi OK per vedere il flusso live"
        ]
        target = "Concessionari Auto del Nord Italia"
        service = "Un sistema AI che converte lead in appuntamenti in showroom in <2 minuti senza assunzioni extra"
        
        await gen.run_all_parallel(
            skill_raw_notes=raw_notes,
            carousel_texts=carousel,
            outreach_target=target,
            outreach_service=service
        )

    if args.demo:
        asyncio.run(demo())
    else:
        print("Usa --demo per lancio completo. Oppure importa ArenaGenerator in tuo script.")
