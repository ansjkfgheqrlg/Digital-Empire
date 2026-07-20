# yt-competitor-scout — Playbook

## Overview
Questo playbook descrive il processo operativo completo per l'analisi dei competitor YouTube. Segue il principio P10 (memory-first) e P12 (traceability).

## Process Flow

```
1. Memory Bootstrap (P10)
   ↓
2. Search Competitor Channels
   ↓
3. Analyze Each Channel
   ↓
4. Identify Gaps & Opportunities
   ↓
5. Generate Report
   ↓
6. Memory Update (P10)
   ↓
7. Handoff to Next Agent
```

## Detailed Steps

### Step 1: Memory Bootstrap (P10)
**Action:** Creare checkpoint iniziale
```python
from tools.memory_manager import MemoryManager

memory = MemoryManager(base_path="memory/youtube")
checkpoint = memory.create_checkpoint(
    id="yt-competitor-scout-start",
    description=f"Inizio analisi competitor per nicchia: {nicchia}",
    input_data={
        "nicchia": nicchia,
        "keyword_opzionale": keyword,
        "numero_canali": num_canali,
        "numero_video": num_video
    },
    status="start"
)
```
**Output:** CP creato in memory/youtube/checkpoints/

---

### Step 2: Search Competitor Channels
**Action:** Cercare canali YouTube nella nicchia
```python
from tools.youtube_api import YouTubeAPI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

api = YouTubeAPI(api_key=api_key)
channels_result = api.search_channels(
    query=nicchia,
    max_results=num_canali,
    filters={
        "subscriber_min": 1000,
        "language": "it",
        "country": "IT"
    }
)

channels = channels_result["channels"]
api_units_used = channels_result["api_units_used"]
```
**Output:** Lista canali con metadata (subscriber, video_count, ecc.)
**Error Handling:**
- Se 0 canali: rilassare filtri (subscriber_min=500)
- Se API quota exceeded: salvare parziale + warning

---

### Step 3: Analyze Each Channel
**Action:** Per ogni canale, analizzare top video
```python
channels_analysis = []

for channel in channels:
    # Get top videos
    videos_result = api.get_channel_videos(
        channel_id=channel["channel_id"],
        max_results=num_video,
        order="viewCount"
    )
    
    videos = videos_result["videos"]
    api_units_used += videos_result["api_units_used"]
    
    # Extract patterns
    patterns = extract_patterns(videos)
    
    # Identify strengths/weaknesses
    strengths = identify_strengths(channel, videos)
    weaknesses = identify_weaknesses(channel, videos)
    
    channels_analysis.append({
        "channel": channel,
        "top_videos": videos,
        "patterns": patterns,
        "strengths": strengths,
        "weaknesses": weaknesses
    })
```
**Helper Functions:**
```python
def extract_patterns(videos: List[Dict]) -> Dict:
    """Estrae pattern dai video (formati, durata, hook, CTA)."""
    durations = [parse_duration(v["duration"]) for v in videos]
    avg_duration = sum(durations) / len(durations) if durations else 0
    
    # Extract hooks from descriptions
    hooks = [v["description"][:100] for v in videos if v["description"]]
    
    # Extract CTAs
    ctas = []
    for v in videos:
        desc = v["description"].lower()
        if "iscriviti" in desc:
            ctas.append("Iscriviti")
        if "commenta" in desc:
            ctas.append("Commenta")
        if "condividi" in desc:
            ctas.append("Condividi")
    
    return {
        "avg_duration_minutes": avg_duration / 60,
        "common_hooks": hooks[:5],
        "common_ctas": list(set(ctas))
    }

def identify_strengths(channel: Dict, videos: List[Dict]) -> List[str]:
    """Identifica punti di forza del canale."""
    strengths = []
    
    # High engagement
    avg_views = sum(v["view_count"] for v in videos) / len(videos) if videos else 0
    if avg_views > 10000:
        strengths.append("Alta visibilità (media >10K views)")
    
    # Consistent uploads
    if channel["video_count"] > 50:
        strengths.append("Produzione consistente (>50 video)")
    
    # Large subscriber base
    if channel["subscriber_count"] > 10000:
        strengths.append(f"Base subscriber ampia ({channel['subscriber_count']})")
    
    return strengths

def identify_weaknesses(channel: Dict, videos: List[Dict]) -> List[str]:
    """Identifica punti di debolezza del canale."""
    weaknesses = []
    
    # Low engagement rate
    if channel["subscriber_count"] > 0:
        avg_views = sum(v["view_count"] for v in videos) / len(videos) if videos else 0
        engagement_rate = avg_views / channel["subscriber_count"]
        if engagement_rate < 0.1:
            weaknesses.append(f"Basso engagement rate ({engagement_rate:.2%})")
    
    # Inconsistent uploads
    if channel["video_count"] < 10:
        weaknesses.append("Produzione inconsistente (<10 video)")
    
    # No clear CTA
    has_cta = any("iscriviti" in v["description"].lower() for v in videos)
    if not has_cta:
        weaknesses.append("CTA mancante o poco chiara")
    
    return weaknesses
```
**Output:** Lista canali analizzati con patterns, strengths, weaknesses

---

### Step 4: Identify Gaps & Opportunities
**Action:** Analizzare dati per identificare gap e opportunità
```python
# Identify gaps
gaps = identify_gaps(channels_analysis, nicchia)

# Identify best practices
best_practices = extract_best_practices(channels_analysis)

# Identify opportunities
opportunities = identify_opportunities(gaps, best_practices, nicchia)
```
**Helper Functions:**
```python
def identify_gaps(channels_analysis: List[Dict], nicchia: str) -> List[str]:
    """Identifica gap di mercato non coperti."""
    gaps = []
    
    # Check for missing languages
    languages = set()
    for ch in channels_analysis:
        for v in ch["top_videos"]:
            if "italiano" in v["title"].lower():
                languages.add("italiano")
    
    if "italiano" not in languages:
        gaps.append("Nessun contenuto in italiano trovato")
    
    # Check for missing formats
    formats = ["tutorial", "review", "comparison", "project"]
    found_formats = set()
    for ch in channels_analysis:
        for v in ch["top_videos"]:
            title = v["title"].lower()
            for fmt in formats:
                if fmt in title:
                    found_formats.add(fmt)
    
    for fmt in formats:
        if fmt not in found_formats:
            gaps.append(f"Formato '{fmt}' non presidiato")
    
    # Check for missing sub-topics
    sub_topics = ["beginner", "advanced", "comparison", "project-based"]
    found_topics = set()
    for ch in channels_analysis:
        for v in ch["top_videos"]:
            title = v["title"].lower()
            for topic in sub_topics:
                if topic in title:
                    found_topics.add(topic)
    
    for topic in sub_topics:
        if topic not in found_topics:
            gaps.append(f"Sotto-topic '{topic}' non coperto")
    
    return gaps

def extract_best_practices(channels_analysis: List[Dict]) -> List[str]:
    """Estrae best practices dai canali di successo."""
    practices = []
    
    # Analyze top performers
    top_channels = sorted(
        channels_analysis,
        key=lambda x: x["channel"]["subscriber_count"],
        reverse=True
    )[:3]
    
    for ch in top_channels:
        patterns = ch["patterns"]
        
        # Duration pattern
        if 8 <= patterns["avg_duration_minutes"] <= 12:
            practices.append("Durata ottimale 8-12 minuti")
        
        # Hook pattern
        if patterns["common_hooks"]:
            practices.append("Hook chiaro nei primi 15 secondi")
        
        # CTA pattern
        if "Iscriviti" in patterns["common_ctas"]:
            practices.append("CTA 'Iscriviti' chiara alla fine")
    
    # Thumbnail pattern (from video titles)
    practices.append("Thumbnail con testo grande e leggibile")
    
    # Consistency pattern
    consistent_channels = [
        ch for ch in channels_analysis
        if ch["channel"]["video_count"] > 50
    ]
    if consistent_channels:
        practices.append("Pubblicazione consistente (almeno 1/settimana)")
    
    return list(set(practices))

def identify_opportunities(
    gaps: List[str],
    best_practices: List[str],
    nicchia: str
) -> List[str]:
    """Identifica opportunità concrete."""
    opportunities = []
    
    # First-mover opportunities
    if "Nessun contenuto in italiano trovato" in gaps:
        opportunities.append(f"Primo canale italiano su {nicchia}")
    
    # Format opportunities
    for gap in gaps:
        if "non presidiato" in gap:
            format_name = gap.split("'")[1]
            opportunities.append(f"Serie '{format_name}' su {nicchia}")
    
    # Differentiation opportunities
    opportunities.append("Serie 'Zero to Hero' (da beginner a esperto)")
    opportunities.append("Confronti diretti con competitor (es. Claude vs Copilot)")
    opportunities.append("Project-based learning (progetti reali)")
    
    return opportunities[:5]  # Top 5 opportunities
```
**Output:** Lista gap, best practices, opportunità

---

### Step 5: Generate Report
**Action:** Generare report strutturato
```python
from tools.report_generator import generate_competitor_report

report_result = generate_competitor_report(
    nicchia=nicchia,
    channels_data=channels_analysis,
    gaps=gaps,
    best_practices=best_practices,
    opportunities=opportunities
)

report = report_result["report"]
report_path = report_result["report_path"]
```
**Output:** Report JSON salvato in memory/youtube/knowledge/competitors/

---

### Step 6: Memory Update (P10)
**Action:** Aggiornare memoria con risultati
```python
# Create completion checkpoint
memory.create_checkpoint(
    id="yt-competitor-scout-complete",
    description=f"Analisi competitor completata: {len(channels_analysis)} canali analizzati",
    input_data={
        "nicchia": nicchia,
        "canali_trovati": len(channels),
        "canali_analizzati": len(channels_analysis)
    },
    output_data={
        "gap_identificati": len(gaps),
        "best_practices": len(best_practices),
        "opportunita": len(opportunities),
        "report_path": report_path
    },
    status="complete"
)

# Save to knowledge base
knowledge_path = memory.base_path / f"knowledge/competitors/{nicchia}_{datetime.now().strftime('%Y%m%d')}.json"
knowledge_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
```
**Output:** CP completato, knowledge base aggiornata, MEMORY-INDEX.md aggiornato

---

### Step 7: Handoff to Next Agent
**Action:** Passare risultati a agente successivo
```python
# Handoff to yt-trend-analyzer
handoff_data = {
    "nicchia": nicchia,
    "competitor_channels": [ch["channel"]["channel_id"] for ch in channels_analysis],
    "gaps": gaps,
    "best_practices": best_practices,
    "opportunities": opportunities,
    "report_path": report_path
}

# Log handoff
memory.create_checkpoint(
    id="yt-competitor-scout-handoff",
    description=f"Handoff a yt-trend-analyzer per nicchia: {nicchia}",
    output_data=handoff_data,
    status="handoff"
)
```
**Output:** Handoff loggato, dati passati a agente successivo

---

## Examples

### Example 1: Happy Path (Nicchia "Claude Code")
**Input:**
- nicchia="Claude Code"
- num_canali=10
- num_video=5

**Execution:**
1. Memory bootstrap → CP-001-competitor-start created
2. Search channels → 8 canali trovati (subscriber >1000)
3. Analyze channels → 8 canali analizzati, 40 video esaminati
4. Identify gaps → 5 gap trovati (no italiano, no comparison, no project-based, no beginner, no advanced)
5. Generate report → Report con 8 competitor, 5 gap, 7 best practices, 3 opportunità
6. Memory update → CP-001-competitor-complete created, report saved
7. Handoff → Dati passati a yt-trend-analyzer

**Output:**
```json
{
  "nicchia": "Claude Code",
  "competitor_analyzed": 8,
  "gap_mercato": [
    "Nessun contenuto in italiano trovato",
    "Formato 'comparison' non presidiato",
    "Sotto-topic 'beginner' non coperto",
    "Sotto-topic 'advanced' non coperto",
    "Formato 'project' non presidiato"
  ],
  "best_practices": [
    "Durata ottimale 8-12 minuti",
    "Hook chiaro nei primi 15 secondi",
    "CTA 'Iscriviti' chiara alla fine",
    "Thumbnail con testo grande e leggibile",
    "Pubblicazione consistente (almeno 1/settimana)"
  ],
  "opportunita": [
    "Primo canale italiano su Claude Code",
    "Serie 'comparison' (Claude vs Copilot, Claude vs Cursor, ecc.)",
    "Serie 'Zero to Hero' (da beginner a esperto)"
  ]
}
```
**Time:** 12 minuti  
**API Units:** 850 (search: 100, channels: 8, videos: 8×5=40)

---

### Example 2: Edge Case (Nicchia Troppo Specifica)
**Input:**
- nicchia="Claude Code avanzato Python metaprogramming"
- num_canali=10

**Execution:**
1. Memory bootstrap → CP created
2. Search channels → 0 canali trovati (filtri stringenti)
3. Relax filters → subscriber_min=500, retry
4. Search channels → 3 canali trovati
5. Analyze channels → 3 canali analizzati, engagement basso
6. Identify gaps → Warning "nicchia troppo piccola"
7. Generate report → Report parziale con warning
8. Memory update → CP created (status="warning")

**Output:**
```json
{
  "nicchia": "Claude Code avanzato Python metaprogramming",
  "competitor_analyzed": 3,
  "warning": "Nicchia troppo specifica, pochi competitor trovati",
  "suggestions": [
    "Rilassare nicchia a 'Claude Code Python'",
    "Considerare nicchia correlata 'Python metaprogramming'",
    "Valutare formato video più breve (5-8 minuti)"
  ]
}
```

---

### Example 3: Failure Recovery (API Quota Exceeded)
**Input:**
- nicchia="AI coding"
- num_canali=10

**Execution:**
1. Memory bootstrap → CP created
2. Search channels → 3 canali trovati
3. Analyze channels → 3 canali analizzati
4. API call #4 → Quota exceeded (10,000 units/day)
5. Error handling → Salvato parziale, warning a utente
6. Memory update → CP created (status="partial", quota_exceeded=true)

**Output:**
```json
{
  "nicchia": "AI coding",
  "competitor_analyzed": 3,
  "partial": true,
  "quota_exceeded": true,
  "recommendations": [
    "Riprendere analisi domani",
    "Usare account API alternativo",
    "Ridurre num_canali a 5 per nächste run"
  ]
}
```

---

## Quality Gates

Prima di consegnare il report, verificare:
- [ ] ≥5 competitor analizzati (o warning giustificato)
- [ ] OGNI dato ha fonte tracciabile (URL, data)
- [ ] ≥3 gap di mercato identificati
- [ ] ≥5 best practices documentate
- [ ] ≥3 opportunità concrete suggerite
- [ ] Checkpoint creato in memory/youtube/checkpoints/
- [ ] Report salvato in memory/youtube/knowledge/competitors/
- [ ] MEMORY-INDEX.md aggiornato
- [ ] Handoff loggato (se applicabile)

---

## Monitoring

**Metrics:**
- Tempo esecuzione (target: <15 minuti)
- API units usate (target: <1000 per run)
- Canali analizzati (target: ≥5)
- Gap identificati (target: ≥3)

**Alerts:**
- Quota <10% (warning)
- Timeout >3 tentativi (error)
- Error rate >5% (critical)

---

## Troubleshooting

**Problem:** 0 canali trovati
**Solution:** Rilassare filtri (subscriber_min=500, language=any)

**Problem:** API quota exceeded
**Solution:** Salvare parziale, riprendere domani o usare account alternativo

**Problem:** Timeout su API call
**Solution:** Retry automatico (max 3 tentativi), poi fallback a dati cached

**Problem:** Dati inconsistenti
**Solution:** Validare dati con schema, scartare entry incomplete

---

**Version:** 1.0  
**Created:** 2026-07-20  
**Owner:** Gael  
**Supervision:** Max
