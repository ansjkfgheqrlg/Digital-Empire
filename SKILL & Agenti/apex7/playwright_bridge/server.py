"""
FastAPI Server per bridge Claude Code <-> Arena Playwright
Claude Code può chiamare questo server via HTTP per generare caroselli

Endpoints:
POST /inizio-generazione {topic, model} -> avvia generazione
GET /status/{job_id} -> stato generazione
GET /download/{job_id} -> zip download
WS /ws -> websocket per log realtime

Avvio: uvicorn playwright_bridge.server:app --host 0.0.0.0 --port 8000
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import uuid
import json
import asyncio
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from playwright_bridge.carousel_flow import CarouselFlow

app = FastAPI(title="Digital Empire - Carousel Factory Bridge", version="2.0-ultra-grain")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "outputs" / "carousel"

# In-memory job store
jobs: dict = {}

class GenerateRequest(BaseModel):
    topic: str
    model: str = "GPT-4o"
    use_playwright: bool = True
    headless: bool = True

class GenerateResponse(BaseModel):
    job_id: str
    status: str
    topic: str
    message: str

@app.get("/")
def root():
    return {
        "service": "Digital Empire Carousel Factory - Ultra Grain 4K Bridge",
        "version": "2.0",
        "quality": "ULTRA grain 38% bg + 15-22% su ogni elemento + 4K sharp 2160x2700",
        "commands": ["/inizio-generazione", "/inzio-generazione", "/inizio-carosello"],
        "endpoints": {
            "POST /inizio-generazione": "Avvia generazione carosello",
            "GET /status/{job_id}": "Stato job",
            "GET /download/{job_id}": "Download ZIP"
        },
        "playwright": "Attivo - collega Claude Code ad Arena.ai",
        "models": ["GPT-4o", "Claude 3.5 Sonnet"]
    }

@app.post("/inizio-generazione", response_model=GenerateResponse)
@app.post("/inzio-generazione", response_model=GenerateResponse)  # typo support
async def inizio_generazione(req: GenerateRequest, background_tasks: BackgroundTasks):
    """
    Entry point per comando /inizio-generazione
    Claude Code chiama questo endpoint quando utente digita /inizio-generazione + fornisce argomento
    """
    job_id = str(uuid.uuid4())[:8]
    
    jobs[job_id] = {
        "job_id": job_id,
        "topic": req.topic,
        "model": req.model,
        "status": "queued",
        "progress": "0/8",
        "created": datetime.now().isoformat(),
        "output_dir": None,
        "zip_path": None,
        "report": None,
        "logs": [f"[{datetime.now().isoformat()}] Job {job_id} creato - topic: {req.topic}"]
    }
    
    # Avvia background task
    background_tasks.add_task(run_generation_task, job_id, req.topic, req.model, req.use_playwright, req.headless)
    
    return GenerateResponse(
        job_id=job_id,
        status="queued",
        topic=req.topic,
        message=f"🎯 /inizio-generazione attivato - Job {job_id} - Topic '{req.topic}' - Generazione 8 slide ultra grain 4K in corso..."
    )

async def run_generation_task(job_id: str, topic: str, model: str, use_playwright: bool, headless: bool):
    try:
        jobs[job_id]["status"] = "generating_copy"
        jobs[job_id]["logs"].append(f"[{datetime.now().isoformat()}] Genero copy 8 slide per topic '{topic}'")
        
        flow = CarouselFlow(model=model, headless=headless, use_playwright=use_playwright)
        report = await flow.run_full_flow(topic, model=model, use_playwright=use_playwright)
        
        jobs[job_id]["status"] = "completed"
        jobs[job_id]["progress"] = "8/8"
        jobs[job_id]["output_dir"] = report["output_dir"]
        jobs[job_id]["zip_path"] = report["zip_path"]
        jobs[job_id]["report"] = report
        jobs[job_id]["logs"].append(f"[{datetime.now().isoformat()}] Completato - ZIP: {report['zip_path']}")
        
    except Exception as e:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["logs"].append(f"[{datetime.now().isoformat()}] Errore: {str(e)}")
        import traceback
        jobs[job_id]["logs"].append(traceback.format_exc())

@app.get("/status/{job_id}")
def get_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job non trovato")
    return jobs[job_id]

@app.get("/download/{job_id}")
def download_zip(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job non trovato")
    
    job = jobs[job_id]
    if job["status"] != "completed":
        raise HTTPException(status_code=400, detail=f"Job non completato - status {job['status']}")
    
    zip_path = Path(job["zip_path"])
    if not zip_path.exists():
        raise HTTPException(status_code=404, detail="ZIP non trovato")
    
    return FileResponse(
        path=str(zip_path),
        filename=zip_path.name,
        media_type="application/zip"
    )

@app.get("/list")
def list_outputs():
    """Lista tutti i caroselli generati"""
    outputs = []
    if OUTPUT_DIR.exists():
        for d in sorted(OUTPUT_DIR.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
            if d.is_dir():
                report_file = d / "report.json"
                if report_file.exists():
                    try:
                        report = json.loads(report_file.read_text(encoding='utf-8'))
                        outputs.append({
                            "dir": d.name,
                            "topic": report.get("topic"),
                            "timestamp": report.get("timestamp"),
                            "zip": report.get("zip_path"),
                            "slides": report.get("total_slides")
                        })
                    except:
                        pass
    return {"total": len(outputs), "outputs": outputs}

# CLI: uvicorn playwright_bridge.server:app --reload --port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("playwright_bridge.server:app", host="0.0.0.0", port=8000, reload=True)
