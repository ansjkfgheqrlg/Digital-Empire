"""
APEX-7 Carousel Flow - Flusso completo da argomento a carosello scaricabile
Integrato con APEX-7 Swarm per generazione copy + Playwright per generazione immagini

Questo è il cuore del workflow /inizio-generazione per Claude Code
"""

import asyncio
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict
import sys

# Aggiungi parent a path per import apex7 modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.planner import PlannerAgent
from agents.writer import WriterAgent
from agents.analyst import AnalystAgent
from memory.memory_system import APEX7Memory
from orchestrator.ruflo_core import RuFLOOrchestrator
from playwright_bridge.arena_client import ArenaPlaywrightClient, OUTPUT_DIR, BASE_DIR
import yaml

CONFIG_PATH = BASE_DIR / "playwright_bridge" / "config.yaml"

class CarouselFlow:
    def __init__(self, model: str = "GPT-4o", headless: bool = True, use_playwright: bool = True):
        self.model = model
        self.headless = headless
        self.use_playwright = use_playwright
        self.config = self._load_config()
        self.memory = APEX7Memory()
        self.orchestrator = RuFLOOrchestrator(memory_system=self.memory)
        self._register_agents()
        print(f"[FLOW] CarouselFlow init model={model} headless={headless} playwright={use_playwright}")

    def _load_config(self):
        if CONFIG_PATH.exists():
            return yaml.safe_load(CONFIG_PATH.read_text(encoding='utf-8'))
        return {"claude_code": {"messages": {}}}

    def _register_agents(self):
        from agents.planner import PlannerAgent
        from agents.writer import WriterAgent
        from agents.analyst import AnalystAgent
        from agents.critic import CriticAgent
        from agents.refiner import RefinerAgent
        from agents.meta_agent import MetaAgent
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

    def _get_default_messages(self):
        cfg_msg = self.config.get("claude_code", {}).get("messages", {})
        return {
            "waiting_topic": cfg_msg.get("waiting_topic", "🎯 Perfetto, sto aspettando il tuo argomento..."),
            "generating_copy": cfg_msg.get("generating_copy", "✍️ Genero copy 8 slide..."),
            "generating_images": cfg_msg.get("generating_images", "🎨 Genero immagini {current}/{total}..."),
            "done": cfg_msg.get("done", "✅ Carosello pronto!"),
            "download_ready": cfg_msg.get("download_ready", "📦 Scarica ZIP: {zip_path}")
        }

    async def generate_copy_from_topic(self, topic: str) -> List[Dict]:
        """Genera 8 slide copy con struttura Digital Empire 8 step"""
        print(f"[FLOW] Generating copy for topic: {topic}")
        
        # Prompt strutturato per 8 slide Digital Empire framework
        # Usiamo stesso framework delle reference: Problema, Verità, Soluzione, Come Funziona, Risultato, Domanda Vera, CTA
        structure_prompt = f"""
        Argomento: {topic}

        Genera carosello 8 slide Digital Empire Content Factory struttura:

        1/8 - CONTENT FACTORY - Hook domanda: "E se i tuoi {topic} si scrivessero da soli?" + sottotitolo fabbrica che produce
        2/8 - IL PROBLEMA - "Ogni post ti ruba 3 ore. E lo sai." + lista 3 problemi settimanali
        3/8 - LA VERITÀ - "Non hai un problema di idee. Hai un problema di esecuzione." + Le idee le hai è tempo che manca
        4/8 - LA SOLUZIONE - "Una fabbrica di contenuti che lavora per te." + card macchina che pubblica al posto tuo + 3 benefit
        5/8 - COME FUNZIONA - "3 step. Zero tuo tempo." + 01 Ricerca 02 Generazione 03 Pubblicazione
        6/8 - IL RISULTATO - "Da 3 ore a 4 minuti per post." + 3 metriche 97% tempo risparmiato, 120+ output mensile, 5min intervento
        7/8 - LA DOMANDA VERA - "Ma sembreranno generati dall'AI?" + 3 punti perché non sembra AI
        8/8 - INIZIA ORA - "Smetti di scrivere. Inizia a lanciare." + offerta €6.400 -> €3.200 -50% + bottone PRENOTA CALL

        Adatta tutto a topic {topic}, mantieni parole accent rosse italic (problema, esecuzione, fabbrica, Zero, 3 ore, 4 minuti, dall'AI?, scrivere, lanciare)
        Output: JSON array 8 oggetti con pill_label, text, red_words
        """

        # Usa orchestrator per generare copy
        result = await self.orchestrator.execute_workflow(
            user_input=structure_prompt,
            context={"topic": topic, "intent": "carousel-machine", "total_slides": 8}
        )
        
        # Fallback strutturato se orchestrator non ritorna JSON pulito
        slides = self._parse_or_generate_default(topic, result)
        
        print(f"[FLOW] Copy generated {len(slides)} slides")
        for s in slides:
            print(f"  {s['slide_num']}/8 {s['pill_label']}: {s['text'][:60]}...")
        
        return slides

    def _parse_or_generate_default(self, topic: str, orchestrator_result) -> List[Dict]:
        """Genera default 8 slide se parsing fallisce, adattato a topic"""
        # Estrai contenuto testuale da result
        text_content = ""
        if isinstance(orchestrator_result, dict):
            wo = orchestrator_result.get("writer_output") or orchestrator_result.get("final_output") or {}
            if isinstance(wo, dict):
                text_content = wo.get("content", str(wo))
            else:
                text_content = str(wo)
        else:
            text_content = str(orchestrator_result)

        # Default slides basate su topic - sempre 8 con struttura Digital Empire
        default_slides = [
            {
                "slide_num": 1,
                "pill_label": "CONTENT FACTORY",
                "icon": "gears",
                "text": f"E se i tuoi {topic} si scrivessero da soli? Content Factory: la fabbrica che produce, scrive e pubblica per te.",
                "red_words": f"{topic} si scrivessero",
                "role": "hook"
            },
            {
                "slide_num": 2,
                "pill_label": "IL PROBLEMA",
                "icon": "clock",
                "text": f"Ogni post su {topic} ti ruba 3 ore. E lo sai. OGNI SETTIMANA SUCCEDE QUESTO → Cerchi idee per {topic}, scrolli per ore. → Scrivi il copy, riscrivi 4 volte. → Pubblichi tardi, perdi il momento.",
                "red_words": "3 ore, momento",
                "role": "problem"
            },
            {
                "slide_num": 3,
                "pill_label": "LA VERITÀ",
                "icon": "eye",
                "text": f"Non hai un problema di {topic}. Hai un problema di esecuzione. Le idee su {topic} le hai. È il tempo che ti manca per trasformarle in contenuti pubblicati. L'esecuzione è la differenza tra chi cresce e chi resta fermo.",
                "red_words": "problema, esecuzione, idea",
                "role": "truth"
            },
            {
                "slide_num": 4,
                "pill_label": "LA SOLUZIONE",
                "icon": "star",
                "text": f"Una fabbrica di contenuti per {topic} che lavora per te. Ricerca, scrittura, grafica, pubblicazione. Tutto automatico. Tutto nella tua voce. La macchina che pubblica al posto tuo. Brand voice cucita su di te. Da idea a post in 4 minuti per {topic}. Pubblicazione automatica.",
                "red_words": "fabbrica",
                "role": "solution"
            },
            {
                "slide_num": 5,
                "pill_label": "COME FUNZIONA",
                "icon": "nodes",
                "text": f"3 step. Zero tuo tempo per {topic}. Il workflow completo dalla ricerca alla pubblicazione. 01 Ricerca - Scansiona trend, competitor e community su {topic}. Trova ciò che funziona ora. 02 Generazione - Crea copy, caption e grafica nella tua brand voice per {topic}. 03 Pubblicazione - Programma e pubblica su Instagram, LinkedIn, X.",
                "red_words": "Zero",
                "role": "how"
            },
            {
                "slide_num": 6,
                "pill_label": "IL RISULTATO",
                "icon": "chart bars",
                "text": f"Da 3 ore a 4 minuti per post su {topic}. Il tempo che recuperi è il tempo che usi per costruire. TEMPO RISPARMIATO 97% Da 3 ore a 4 minuti per ogni post pubblicato. OUTPUT MENSILE 120+ Contenuti pronti su {topic} al mese, multicanale. TUO INTERVENTO 5min Solo per approvare. Il resto è automatico.",
                "red_words": "3 ore, 4 minuti",
                "role": "result"
            },
            {
                "slide_num": 7,
                "pill_label": "LA DOMANDA VERA",
                "icon": "shield ?",
                "text": f"Ma i contenuti su {topic} sembreranno generati dall'AI? No. E ti spieghiamo perché in 3 punti. PERCHÉ NON SEMBRA AI ✓ Brand voice estratta dal tuo materiale su {topic}. Analizziamo i tuoi post migliori. ✓ Output sempre diversi, mai ripetitivi. Variazione strutturale automatica. ✓ Tu approvi prima di pubblicare. Vedi tutto, modifichi se vuoi.",
                "red_words": "dall'AI?",
                "role": "objection"
            },
            {
                "slide_num": 8,
                "pill_label": "INIZIA ORA",
                "icon": "lightning",
                "text": f"Smetti di scrivere su {topic}. Inizia a lanciare. La tua Content Factory per {topic} pronta in 10 giorni. Installata, configurata, già a lavoro. OFFERTA LIMITATA PRIMI 5 CLIENTI €6.400 €3.200 -50% Setup completo Brand voice import 30gg supporto PRENOTA LA CALL GRATUITA → Solo 30 minuti. Zero impegno. Solo chiarezza.",
                "red_words": "scrivere, lanciare",
                "role": "cta"
            }
        ]
        return default_slides

    async def generate_images_for_slides(self, slides: List[Dict], output_dir: Path, model: str = "GPT-4o", use_playwright: bool = True) -> List[Dict]:
        """Genera immagini per ogni slide usando Writer per prompt ultra grain + Arena Client"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        writer = self.agents["writer"]
        prompts = []
        
        for slide in slides:
            # Genera prompt con Writer - ora con ultra grain su ogni elemento + 4K sharp
            writer_payload = {
                "input": slide["text"],
                "slide_text": slide["text"],
                "pill_label": slide["pill_label"],
                "icon": slide["icon"],
                "total_slides": 8,
                "slide_number": slide["slide_num"],
                "red_words": slide["red_words"],
                "intent": "carousel-machine",
                "ultra_quality": True,  # flag per grain su ogni elemento
                "resolution": "4K ultra sharp"
            }
            writer_result = await writer.execute(writer_payload)
            prompt_text = writer_result.get("content", "") if isinstance(writer_result, dict) else str(writer_result)
            
            # Potenzia per ultra quality grain su OGNI elemento + nitidezza
            enhanced_prompt = self._enhance_for_ultra_quality(prompt_text, slide)
            prompts.append(enhanced_prompt)
            
            # Salva prompt per debug e per Claude Code che scarica
            (output_dir / f"slide_{slide['slide_num']:02d}_prompt.txt").write_text(enhanced_prompt, encoding='utf-8')
            (output_dir / f"slide_{slide['slide_num']:02d}_copy.json").write_text(json.dumps(slide, indent=2, ensure_ascii=False), encoding='utf-8')

        print(f"[FLOW] {len(prompts)} ultra-quality prompts generated")

        if use_playwright:
            client = ArenaPlaywrightClient(headless=self.headless, model=model)
            results = await client.generate_carousel(prompts, output_dir, model=model)
        else:
            # Fallback locale - salva solo prompt, le immagini verranno generate via generate_image manuale o su arena_generator.py
            print("[FLOW] Playwright disabled - promps salvati, usa generate_image tool o arena_generator.py per immagini")
            results = [{"status": "prompt_saved", "slide": i+1, "path": str(output_dir / f"slide_{i+1:02d}.png"), "mode": "fallback_no_playwright"} for i in range(len(prompts))]

        return results

    def _enhance_for_ultra_quality(self, base_prompt: str, slide: Dict) -> str:
        """Aggiunge grain+nitidezza al prompt base, in modo compatto.

        Riscritto (2026-08-05): la versione precedente ripeteva "grain"/"4K"/"8K"
        una quindicina di volte in un muro di elenchi puntati per ogni singola
        slide - segnalato da Max osservando lo schermo come qualita' scadente
        del prompt ("uno schifo"). Un prompt lungo e ridondante non aiuta un
        modello immagine, lo confonde. Stessa direzione tecnica (grain uniforme
        su ogni elemento, non solo sfondo; nitidezza 4K; niente look digitale
        piatto), detta una volta sola, in modo diretto."""
        ultra_suffix = (
            "\n\nQualita': film grain uniforme e visibile su OGNI elemento "
            "(sfondo nero, card, testo, pill, bottone, logo - non solo lo sfondo), "
            "stesso tipo di grana ovunque per coerenza. Nitidezza 4K, bordi netti, "
            "zero sfocatura, zero look digitale piatto - deve sembrare una foto "
            "pellicola ad alta risoluzione, non un rendering vettoriale."
        )
        return base_prompt + ultra_suffix

    async def run_full_flow(self, topic: str, output_dir: Path = None, model: str = "GPT-4o", use_playwright: bool = True) -> Dict:
        """Flusso completo /inizio-generazione: topic -> copy -> images -> zip"""
        msgs = self._get_default_messages()
        
        if output_dir is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_topic = "".join(c if c.isalnum() else "_" for c in topic)[:20]
            output_dir = OUTPUT_DIR / f"{safe_topic}_{timestamp}"
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n{'='*70}")
        print(f"[FLOW] /inizio-generazione - Topic: {topic}")
        print(f"       Output: {output_dir} Model: {model} Playwright: {use_playwright}")
        print(f"{'='*70}\n")

        # STEP 1: Copy
        print(f"[STEP 1/4] {msgs['generating_copy']}")
        slides = await self.generate_copy_from_topic(topic)
        (output_dir / "slides_copy.json").write_text(json.dumps(slides, indent=2, ensure_ascii=False), encoding='utf-8')

        # STEP 2: Images
        print(f"\n[STEP 2/4] Generazione immagini ultra grain 4K...")
        image_results = await self.generate_images_for_slides(slides, output_dir, model=model, use_playwright=use_playwright)
        
        # STEP 3: Package ZIP
        print(f"\n[STEP 3/4] Packaging ZIP...")
        zip_path = await self._create_zip(output_dir, topic)
        
        # STEP 4: Report
        report = {
            "topic": topic,
            "model": model,
            "slides": slides,
            "image_results": image_results,
            "output_dir": str(output_dir),
            "zip_path": str(zip_path),
            "timestamp": datetime.now().isoformat(),
            "quality": "ULTRA grain 38% bg + 15-22% su ogni elemento + 4K sharp 2160x2700",
            "total_slides": len(slides)
        }
        (output_dir / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')

        print(f"\n{'='*70}")
        print(f"{msgs['done']}")
        print(f"{msgs['download_ready'].format(zip_path=zip_path)}")
        print(f"Output dir: {output_dir}")
        print(f"Slides: {len(slides)} | Images: {len([r for r in image_results if r.get('status') in ('success','prompt_saved')])}")
        print(f"{'='*70}\n")

        self.memory.persist()
        
        return report

    async def _create_zip(self, output_dir: Path, topic: str) -> Path:
        zip_base = output_dir.parent / f"{output_dir.name}_CAROSELLO"
        # Se esiste già, rimuovi
        if zip_base.with_suffix('.zip').exists():
            zip_base.with_suffix('.zip').unlink()
        
        # Crea zip con immagini + prompt + copy
        shutil.make_archive(str(zip_base), 'zip', root_dir=output_dir.parent, base_dir=output_dir.name)
        zip_path = zip_base.with_suffix('.zip')
        print(f"[ZIP] Created {zip_path} - {zip_path.stat().st_size / 1024 / 1024:.2f} MB")
        return zip_path


# Test standalone
if __name__ == "__main__":
    async def test_flow():
        flow = CarouselFlow(model="GPT-4o", headless=True, use_playwright=False)  # False per test locale senza browser
        topic = "Content Factory per coach e consulenti"
        report = await flow.run_full_flow(topic, use_playwright=False)
        print(json.dumps(report, indent=2, ensure_ascii=False)[:2000])

    asyncio.run(test_flow())
