# yt-competitor-scout — Memory

## Memory Mandate (P10)
**OGNI azione DEVE essere tracciata in memory.** Questo è non-negotiable.

### Required Artifacts
1. **Checkpoint (CP):** OGNI step significativo → CP in `memory/youtube/checkpoints/`
2. **Decision (DEC):** OGNI decisione importante → DEC in `memory/youtube/decisions/`
3. **Session (SES):** OGNI sessione → SES in `memory/youtube/sessions/`
4. **Knowledge:** OGNI risultato → Knowledge in `memory/youtube/knowledge/competitors/`
5. **INDEX Update:** OGNI CP/DEC/SES → Aggiornare `memory/youtube/MEMORY-INDEX.md`

---

## Two-Layer Memory

### Short-Term (Session)
- Contesto conversazione corrente
- Dati temporanei durante analisi
- Stato intermedio (canali analizzati, gap trovati)

### Long-Term (Persistent)
- **Checkpoints:** Progresso analisi
- **Decisions:** Decisioni prese (nicchia, filtri, ecc.)
- **Knowledge:** Report competitor completi
- **State:** Stato ecosistema YouTube

---

## Shared State

```json
{
  "yt_competitor_scout": {
    "last_run": "2026-07-20T14:30:00",
    "nicchie_analizzate": ["Claude Code", "AI coding"],
    "competitor_analizzati": 18,
    "gap_identificati": 10,
    "best_practices": 14,
    "opportunita": 6,
    "api_units_used": 1700,
    "cps": [
      "CP-001-competitor-start",
      "CP-002-competitor-complete"
    ],
    "decs": [
      "DEC-001-nicchia-scelta"
    ],
    "reports": [
      "memory/youtube/knowledge/competitors/Claude_Code_20260720.json",
      "memory/youtube/knowledge/competitors/AI_coding_20260720.json"
    ]
  }
}
```

---

## Update Protocol

### Step 1: Before Action
```python
# Load previous state
state = memory.load_state("yt_competitor_scout")
previous_runs = state.get("nicchie_analizzate", [])
```

### Step 2: During Action
```python
# Track progress
for channel in channels:
    analyze_channel(channel)
    memory.log_progress(f"Analyzed channel: {channel['channel_name']}")
```

### Step 3: After Action
```python
# Create checkpoint
memory.create_checkpoint(
    id="yt-competitor-scout-complete",
    description=f"Analisi completata: {len(channels_analyzed)} canali",
    output_data={
        "nicchia": nicchia,
        "competitor_analyzed": len(channels_analyzed),
        "gap_identified": len(gaps),
        "report_path": report_path
    },
    status="complete"
)

# Update state
state = memory.load_state("yt_competitor_scout")
state["nicchie_analizzate"].append(nicchia)
state["competitor_analizzati"] += len(channels_analyzed)
state["gap_identificati"] += len(gaps)
state["cps"].append("CP-001-competitor-complete")
state["reports"].append(report_path)
memory.save_state("yt_competitor_scout", state)

# Update INDEX
memory.update_index(
    entry=f"- [CP-001] {timestamp}: Analisi competitor per {nicchia}"
)
```

---

## Research→Plan→Reset→Implement

### Research
- Raccogliere dati competitor (canali, video, stats)
- Analizzare pattern (formati, durata, hook, CTA)
- Identificare gap e opportunità

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

### Example 1: After Search Channels
```python
memory.create_checkpoint(
    id="yt-competitor-scout-search",
    description=f"Cercati {len(channels)} canali per nicchia: {nicchia}",
    output_data={
        "canali_trovati": len(channels),
        "filters_used": filters,
        "api_units_used": api_units_used
    },
    status="progress"
)
```

**Memory Artifacts Created:**
- `memory/youtube/checkpoints/CP-001-competitor-search.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

### Example 2: After Analyze Channels
```python
memory.create_checkpoint(
    id="yt-competitor-scout-analysis",
    description=f"Analizzati {len(channels_analyzed)} canali, {total_videos} video",
    output_data={
        "canali_analizzati": len(channels_analyzed),
        "video_esaminati": total_videos,
        "patterns_found": len(patterns)
    },
    status="progress"
)
```

**Memory Artifacts Created:**
- `memory/youtube/checkpoints/CP-002-competitor-analysis.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

### Example 3: After Identify Gaps
```python
memory.create_decision(
    id="DEC-001-gap-identification",
    context=f"Nicchia: {nicchia}",
    decision=f"Identificati {len(gaps)} gap di mercato",
    rationale="Gap basati su analisi competitor e pattern mancanti",
    consequences=f"Opportunità per {len(opportunities)} strategie di contenuto"
)
```

**Memory Artifacts Created:**
- `memory/youtube/decisions/DEC-001-gap-identification.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

### Example 4: After Generate Report
```python
# Save report to knowledge base
report_path = memory.base_path / f"knowledge/competitors/{nicchia}_{date}.json"
report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False))

# Create completion checkpoint
memory.create_checkpoint(
    id="yt-competitor-scout-complete",
    description=f"Report generato: {len(channels_analyzed)} competitor, {len(gaps)} gap",
    output_data={
        "report_path": str(report_path),
        "competitor_analyzed": len(channels_analyzed),
        "gap_identified": len(gaps),
        "best_practices": len(best_practices),
        "opportunities": len(opportunities)
    },
    status="complete"
)
```

**Memory Artifacts Created:**
- `memory/youtube/knowledge/competitors/Claude_Code_20260720.json`
- `memory/youtube/checkpoints/CP-003-competitor-complete.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

### Example 5: After Handoff
```python
memory.create_checkpoint(
    id="yt-competitor-scout-handoff",
    description=f"Handoff a yt-trend-analyzer per nicchia: {nicchia}",
    output_data={
        "next_agent": "yt-trend-analyzer",
        "data_passed": {
            "nicchia": nicchia,
            "competitor_channels": [ch["channel_id"] for ch in channels_analyzed],
            "gaps": gaps,
            "report_path": report_path
        }
    },
    status="handoff"
)
```

**Memory Artifacts Created:**
- `memory/youtube/checkpoints/CP-004-competitor-handoff.md`
- `memory/youtube/MEMORY-INDEX.md` updated

---

## Memory Verification Checklist

Prima di completare l'analisi, verificare:
- [ ] CP start creato
- [ ] CP progress creati (search, analysis, gaps)
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
    id="yt-competitor-scout-start",
    description="Inizio analisi competitor",
    input_data={"nicchia": nicchia},
    status="start"
)

# Create decision
dec = memory.create_decision(
    id="DEC-001-nicchia-scelta",
    context="Analisi competitor",
    decision=f"Nicchia scelta: {nicchia}",
    rationale="Nicchia con potenziale di crescita",
    consequences="Focus su questa nicchia per prossimi video"
)

# Update state
memory.update_state(
    key="yt_competitor_scout.last_run",
    value=datetime.now().isoformat()
)

# Update INDEX
memory.update_index(
    entry=f"- [CP-001] {cp['timestamp']}: Inizio analisi competitor per {nicchia}"
)
```

---

## Self-Improvement (P10 Loops)

### Loop 1: Failure Analysis
```python
# After each run, analyze failures
failures = memory.load_failures("yt-competitor-scout")

for failure in failures:
    # Extract lesson
    lesson = extract_lesson(failure)
    
    # Update playbook
    update_playbook(lesson)
    
    # Log improvement
    memory.log_improvement(
        agent="yt-competitor-scout",
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
    "canali_analizzati": []
}

for run in memory.load_runs("yt-competitor-scout"):
    metrics["tempo_esecuzione"].append(run["tempo"])
    metrics["api_units_used"].append(run["api_units"])
    metrics["canali_analizzati"].append(run["canali"])

# Identify bottlenecks
avg_tempo = sum(metrics["tempo_esecuzione"]) / len(metrics["tempo_esecuzione"])
if avg_tempo > 15:
    logger.warning("Average execution time >15 min, optimize needed")
```

### Loop 3: Meta-Recursive Self-Improvement
```python
# Use this agent's output to improve itself
def self_improve():
    """Migliora yt-competitor-scout basandosi su run precedenti."""
    
    # Load all previous runs
    runs = memory.load_runs("yt-competitor-scout")
    
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
        agent="yt-competitor-scout",
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
│   ├── CP-001-competitor-start.md
│   ├── CP-002-competitor-search.md
│   ├── CP-003-competitor-analysis.md
│   ├── CP-004-competitor-complete.md
│   └── CP-005-competitor-handoff.md
├── decisions/
│   └── DEC-001-gap-identification.md
├── sessions/
│   └── SES-001-competitor-analysis.md
├── knowledge/
│   └── competitors/
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
