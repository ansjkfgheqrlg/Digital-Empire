# yt-trend-analyzer — Memory

## Memory Mandate (P10)
**OGNI azione DEVE essere tracciata in memory.** Questo è non-negotiable.

### Required Artifacts
1. **Checkpoint (CP):** OGNI step significativo → CP in `memory/youtube/checkpoints/`
2. **Decision (DEC):** OGNI decisione importante → DEC in `memory/youtube/decisions/`
3. **Session (SES):** OGNI sessione → SES in `memory/youtube/sessions/`
4. **Knowledge:** OGNI risultato → Knowledge in `memory/youtube/knowledge/trends/`
5. **INDEX Update:** OGNI CP/DEC/SES → Aggiornare `memory/youtube/MEMORY-INDEX.md`

---

## Two-Layer Memory

### Short-Term (Session)
- Contesto conversazione corrente
- Dati temporanei durante analisi
- Stato intermedio (trend analizzati, keyword ricercate)

### Long-Term (Persistent)
- **Checkpoints:** Progresso analisi
- **Decisions:** Decisioni prese (nicchia, timeframe, ecc.)
- **Knowledge:** Report trend completi
- **State:** Stato ecosistema YouTube

---

## Shared State

```json
{
  "yt_trend_analyzer": {
    "last_run": "2026-07-20T14:30:00",
    "nicchie_analizzate": ["Claude Code", "AI coding"],
    "trend_identificati": 24,
    "keywords_ricercate": 50,
    "forecast_generated": 6,
    "api_units_used": 1900,
    "cps": [
      "CP-001-trend-start",
      "CP-002-trend-complete"
    ],
    "decs": [
      "DEC-002-timeframe-scelto"
    ],
    "reports": [
      "memory/youtube/knowledge/trends/Claude_Code_20260720.json",
      "memory/youtube/knowledge/trends/AI_coding_20260720.json"
    ]
  }
}
```

---

## Update Protocol

### Step 1: Before Action
```python
# Load previous state
state = memory.load_state("yt_trend_analyzer")
previous_runs = state.get("nicchie_analizzate", [])
```

### Step 2: During Action
```python
# Track progress
for trend in trends:
    analyze_trend(trend)
    memory.log_progress(f"Analyzed trend: {trend['argomento']}")
```

### Step 3: After Action
```python
# Create checkpoint
memory.create_checkpoint(
    id="yt-trend-analyzer-complete",
    description=f"Analisi completata: {len(trends)} trend, {len(keywords)} keyword",
    output_data={
        "nicchia": nicchia,
        "trend_identified": len(trends),
        "keywords_researched": len(keywords),
        "seasonality_documented": True,
        "forecast_generated": len(forecast),
        "report_path": report_path
    },
    status="complete"
)

# Update state
state = memory.load_state("yt_trend_analyzer")
state["nicchie_analizzate"].append(nicchia)
state["trend_identificati"] += len(trends)
state["keywords_ricercate"] += len(keywords)
state["forecast_generated"] += len(forecast)
state["cps"].append("CP-002-trend-complete")
state["reports"].append(report_path)
memory.save_state("yt_trend_analyzer", state)

# Update INDEX
memory.update_index(
    entry=f"- [CP-002] {timestamp}: Analisi trend per {nicchia}"
)
```

---

## Research→Plan→Reset→Implement

### Research
- Raccogliere dati trend (Google Trends, competitor activity)
- Analizzare keyword (volumi, difficoltà, CPC)
- Identificare stagionalità (mesi, giorni, ore)
- Generare forecast (3-6 mesi, confidenza)

### Plan
- Strutturare report
- Definire raccomandazioni
- Pianificare handoff a next agent

### Reset
- Clear temporary data
- Validate final report
- Check quality gates

### Implement
- Save report to knowledge base
- Create final checkpoint
- Update MEMORY-INDEX
- Execute handoff

---

## Memory Update Examples

### Example 1: After Google Trends Analysis
```python
memory.create_checkpoint(
    id="yt-trend-analyzer-google-trends",
    description=f"Google Trends: {len(trends)} trend analizzati",
    output_data={
        "trend_analyzed": len(trends),
        "api_calls_used": api.calls_used,
        "quota_remaining": 100 - api.calls_used
    },
    status="progress"
)
```

**Memory Artifacts Created:**
- `memory/youtube/checkpoints/CP-002-trend-google-trends.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

### Example 2: After Competitor Activity Analysis
```python
memory.create_checkpoint(
    id="yt-trend-analyzer-competitor",
    description=f"Competitor activity: {len(competitor_channels)} canali, {len(competitor_activity)} video",
    output_data={
        "competitor_analyzed": len(competitor_channels),
        "video_analyzed": len(competitor_activity),
        "api_calls_used": api_units_used
    },
    status="progress"
)
```

**Memory Artifacts Created:**
- `memory/youtube/checkpoints/CP-003-trend-competitor.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

### Example 3: After Keyword Research
```python
memory.create_checkpoint(
    id="yt-trend-analyzer-keywords",
    description=f"Keywords: {len(keywords)} keyword ricercate",
    output_data={
        "keywords_researched": len(keywords),
        "avg_volume": sum(k["avg_monthly_searches"] for k in keywords) / len(keywords),
        "api_calls_used": keyword_api.calls_used
    },
    status="progress"
)
```

**Memory Artifacts Created:**
- `memory/youtube/checkpoints/CP-004-trend-keywords.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

### Example 4: After Generate Report
```python
# Save report to knowledge base
report_path = memory.base_path / f"knowledge/trends/{nicchia}_{date}.json"
report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False))

# Create completion checkpoint
memory.create_checkpoint(
    id="yt-trend-analyzer-complete",
    description=f"Report generato: {len(trends)} trend, {len(keywords)} keyword",
    output_data={
        "report_path": str(report_path),
        "trend_identified": len(trends),
        "keywords_researched": len(keywords),
        "seasonality_documented": True,
        "forecast_generated": len(forecast)
    },
    status="complete"
)
```

**Memory Artifacts Created:**
- `memory/youtube/knowledge/trends/Claude_Code_20260720.json`
- `memory/youtube/checkpoints/CP-007-trend-complete.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

### Example 5: After Handoff
```python
memory.create_checkpoint(
    id="yt-trend-analyzer-handoff",
    description=f"Handoff a yt-keyword-researcher per nicchia: {nicchia}",
    output_data={
        "next_agent": "yt-keyword-researcher",
        "data_passed": {
            "nicchia": nicchia,
            "keywords": keywords,
            "trends": trends,
            "seasonality": seasonality,
            "report_path": report_path
        }
    },
    status="handoff"
)
```

**Memory Artifacts Created:**
- `memory/youtube/checkpoints/CP-008-trend-handoff.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

## Memory Verification Checklist

Prima di completare l'analisi, verificare:
- [ ] CP start creato
- [ ] CP progress creati (Google Trends, competitor, keywords, seasonality, forecast)
- [ ] CP complete creato
- [ ] CP handoff creato (se applicabile)
- [ ] DEC creati (decisioni importanti)
- [ ] Report salvato in knowledge/
- [ ] MEMORY-INDEX.md aggiornato
- [ ] State aggiornato (shared_state)
- [ ] OGNI CP ha timestamp, description, input/output data

---

## Integration with Memory Manager

```python
from tools.memory_manager import MemoryManager

# Initialize
memory = MemoryManager(base_path="memory/youtube")

# Create checkpoint
cp = memory.create_checkpoint(
    id="yt-trend-analyzer-start",
    description="Inizio analisi trend",
    input_data={"nicchia": nicchia, "competitor_channels": competitor_channels},
    status="start"
)

# Create decision
dec = memory.create_decision(
    id="DEC-002-timeframe-scelto",
    context="Analisi trend",
    decision=f"Timeframe scelto: {timeframe}",
    rationale="Timeframe bilanciato tra dati sufficienti e attualità",
    consequences=f"Analisi copre ultimi {timeframe}"
)

# Update state
memory.update_state(
    key="yt_trend_analyzer.last_run",
    value=datetime.now().isoformat()
)

# Update INDEX
memory.update_index(
    entry=f"- [CP-001] {cp['timestamp']}: Inizio analisi trend per {nicchia}"
)
```

---

## Self-Improvement (P10 Loops)

### Loop 1: Failure Analysis
```python
# After each run, analyze failures
failures = memory.load_failures("yt-trend-analyzer")

for failure in failures:
    # Extract lesson
    lesson = extract_lesson(failure)
    
    # Update playbook
    update_playbook(lesson)
    
    # Log improvement
    memory.log_improvement(
        agent="yt-trend-analyzer",
        failure_id=failure["id"],
        lesson=lesson,
        timestamp=datetime.now().isoformat()
    )
```

### Loop 2: Performance Optimization
```python
# Track performance metrics
metrics = {
    "tempo_esecuzione": [],
    "api_units_used": [],
    "trend_identified": [],
    "keywords_researched": []
}

for run in memory.load_runs("yt-trend-analyzer"):
    metrics["tempo_esecuzione"].append(run["tempo"])
    metrics["api_units_used"].append(run["api_units"])
    metrics["trend_identified"].append(run["trend"])
    metrics["keywords_researched"].append(run["keywords"])

# Identify bottlenecks
avg_tempo = sum(metrics["tempo_esecuzione"]) / len(metrics["tempo_esecuzione"])
if avg_tempo > 20:
    logger.warning("Average execution time >20 min, optimize needed")
```

### Loop 3: Meta-Recursive Self-Improvement
```python
# Use this agent's output to improve itself
def self_improve():
    """Migliora yt-trend-analyzer basandosi su run precedenti."""
    
    # Load all previous runs
    runs = memory.load_runs("yt-trend-analyzer")
    
    # Identify patterns
    successful_patterns = []
    failed_patterns = []
    
    for run in runs:
        if run["status"] == "complete":
            successful_patterns.append(run["approach"])
        else:
            failed_patterns.append(run["failure_mode"])
    
    # Update system prompt
    update_system_prompt(
        successful_patterns=successful_patterns,
        failed_patterns=failed_patterns
    )
    
    # Log meta-improvement
    memory.log_meta_improvement(
        agent="yt-trend-analyzer",
        runs_analyzed=len(runs),
        successful_patterns=len(successful_patterns),
        failed_patterns=len(failed_patterns),
        timestamp=datetime.now().isoformat()
    )
```

---

## Trace

- **P10:** Memory-first (OGNI azione tracciata)
- **P12:** Traceability (OGNI dato con fonte)
- **PT07:** Silent-Observer (osservazione senza side-effects)
- **CS03:** SI with observer (mistake was assuming SI without observer = drift)
- **CS04:** Bugs in real test (enforced real-test + bug logging)
- **PT08:** Meta-Recursive (agent improves itself based on runs)

---

## Memory File Locations

```
memory/youtube/
├── checkpoints/
│   ├── CP-001-trend-start.md
│   ├── CP-002-trend-google-trends.md
│   ├── CP-003-trend-competitor.md
│   ├── CP-004-trend-keywords.md
│   ├── CP-005-trend-seasonality.md
│   ├── CP-006-trend-forecast.md
│   ├── CP-007-trend-complete.md
│   └── CP-008-trend-handoff.md
├── decisions/
│   └── DEC-002-timeframe-scelto.md
├── sessions/
│   └── SES-002-trend-analysis.md
├── knowledge/
│   └── trends/
│       ├── Claude_Code_20260720.json
│       └── AI_coding_20260720.json
├── state/
│   └── youtube-state.json
└── MEMORY-INDEX.md
```

---

**Version:** 1.0  
**Created:** 2026-07-20  
**Owner:** Gael  
**Supervision:** Max
