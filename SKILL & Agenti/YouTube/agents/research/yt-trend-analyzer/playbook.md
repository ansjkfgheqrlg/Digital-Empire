# yt-trend-analyzer — Playbook

## Overview
Questo playbook descrive il processo operativo completo per l'analisi dei trend YouTube. Segue il principio P10 (memory-first) e P12 (traceability).

## Process Flow

```
1. Memory Bootstrap (P10)
   ↓
2. Analyze Trend with Google Trends
   ↓
3. Analyze Competitor Activity
   ↓
4. Research Keywords
   ↓
5. Analyze Seasonality
   ↓
6. Generate Forecast
   ↓
7. Generate Report
   ↓
8. Memory Update (P10)
   ↓
9. Handoff to Next Agent
```

## Detailed Steps

### Step 1: Memory Bootstrap (P10)
**Action:** Creare checkpoint iniziale
```python
from tools.memory_manager import MemoryManager

memory = MemoryManager(base_path="memory/youtube")
checkpoint = memory.create_checkpoint(
    id="yt-trend-analyzer-start",
    description=f"Inizio analisi trend per nicchia: {nicchia}",
    input_data={
        "nicchia": nicchia,
        "competitor_channels": competitor_channels,
        "timeframe": timeframe
    },
    status="start"
)
```
**Output:** CP creato in memory/youtube/checkpoints/

---

### Step 2: Analyze Trend with Google Trends
**Action:** Analizzare trend con Google Trends API
```python
from tools.youtube_api import GoogleTrendsAPI

api = GoogleTrendsAPI()
trends_result = api.analyze(
    keyword=nicchia,
    timeframe=timeframe,
    geo="IT",
    category=0
)

trends = trends_result["trends"]
related_queries = trends_result["related_queries"]
api_units_used = trends_result["api_calls_used"]
```
**Output:** Lista trend con crescita, volume, stagionalità
**Error Handling:**
- Se 0 trend: suggerire nicchie correlate
- Se API quota exceeded: salvare parziale + warning

---

### Step 3: Analyze Competitor Activity
**Action:** Per ogni competitor, analizzare video recenti
```python
competitor_activity = []

for channel_id in competitor_channels:
    videos_result = api.get_channel_videos(
        channel_id=channel_id,
        max_results=10,
        order="date"
    )
    
    videos = videos_result["videos"]
    api_units_used += videos_result["api_units_used"]
    
    competitor_activity.extend(videos)
```
**Output:** Lista video recenti dei competitor
**Analysis:**
- Pattern di pubblicazione (frequenza, giorni, ore)
- Argomenti trattati
- Performance (views, engagement)

---

### Step 4: Research Keywords
**Action:** Ricercare keyword con Keyword Planner
```python
from tools.keyword_planner import KeywordPlannerAPI

keyword_api = KeywordPlannerAPI(credentials_path="google-ads.yaml")
keywords_result = keyword_api.research(
    seed_keywords=[nicchia],
    max_results=50,
    language="it",
    location="IT"
)

keywords = keywords_result["keywords"]
api_units_used += keywords_result["api_calls_used"]
```
**Output:** Lista keyword con volume, difficoltà, CPC, trend
**Filter:** Mantenere solo keyword con volume > 100/mese

---

### Step 5: Analyze Seasonality
**Action:** Analizzare stagionalità da trend e attività competitor
```python
from tools.seasonality import analyze_seasonality

seasonality = analyze_seasonality(
    trends=trends,
    competitor_activity=competitor_activity,
    timeframe=timeframe
)
```
**Output:** Mesi, giorni, ore migliori per pubblicare
**Analysis:**
- Pattern mensili (set-nov picco, lug-ago basso)
- Pattern settimanali (mar-gio picco, weekend basso)
- Pattern orari (15-16, 18-20 picco)

---

### Step 6: Generate Forecast
**Action:** Generare forecast trend
```python
from tools.forecast import generate_forecast

forecast = generate_forecast(
    trends=trends,
    historical_data=historical_data,
    confidence_threshold=0.7
)
```
**Output:** Forecast 3-6 mesi con confidenza
**Filter:** Mantenere solo forecast con confidenza ≥ 0.7

---

### Step 7: Generate Report
**Action:** Generare report strutturato
```python
report = {
    "nicchia": nicchia,
    "data_analisi": datetime.now().isoformat(),
    "timeframe": timeframe,
    "trend": trends,
    "keywords": keywords,
    "stagionalita": seasonality,
    "forecast": forecast,
    "recommendations": generate_recommendations(trends, keywords, seasonality)
}
```
**Output:** Report JSON completo

---

### Step 8: Memory Update (P10)
**Action:** Aggiornare memoria con risultati
```python
# Save report to knowledge base
report_path = memory.base_path / f"knowledge/trends/{nicchia}_{datetime.now().strftime('%Y%m%d')}.json"
report_path.parent.mkdir(parents=True, exist_ok=True)
report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

# Create completion checkpoint
memory.create_checkpoint(
    id="yt-trend-analyzer-complete",
    description=f"Analisi trend completata: {len(trends)} trend, {len(keywords)} keyword",
    input_data={
        "nicchia": nicchia,
        "competitor_analyzed": len(competitor_channels)
    },
    output_data={
        "trend_identified": len(trends),
        "keywords_researched": len(keywords),
        "seasonality_documented": True,
        "forecast_generated": len(forecast),
        "report_path": str(report_path)
    },
    status="complete"
)
```
**Output:** CP completato, knowledge base aggiornata, MEMORY-INDEX.md aggiornato

---

### Step 9: Handoff to Next Agent
**Action:** Passare risultati a agente successivo
```python
# Handoff to yt-keyword-researcher
handoff_data = {
    "nicchia": nicchia,
    "keywords": keywords,
    "trends": trends,
    "seasonality": seasonality,
    "report_path": str(report_path)
}

# Log handoff
memory.create_checkpoint(
    id="yt-trend-analyzer-handoff",
    description=f"Handoff a yt-keyword-researcher per nicchia: {nicchia}",
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
- competitor_channels=8
- timeframe="3_months"

**Execution:**
1. Memory bootstrap → CP-001-trend-start created
2. Google Trends: 12 trend analizzati (crescita media +180%)
3. Competitor activity: 8 canali, 80 video recenti
4. Keywords: 25 keyword ricercate (volume medio 3500/mese)
5. Seasonality: mesi (set-nov), giorni (mar-gio), ore (15-16, 18-20)
6. Forecast: 3 previsioni (confidenza 0.85)
7. Report: 12 trend, 25 keyword, stagionalità completa, 3 forecast
8. Memory update → CP-001-trend-complete created, report saved
9. Handoff → Dati passati a yt-keyword-researcher

**Output:**
```json
{
  "nicchia": "Claude Code",
  "trend": [
    {
      "argomento": "Claude Code tutorial italiano",
      "crescita_percentuale": 450,
      "volume_ricerche": 1200,
      "stagionalita": "crescente",
      "opportunita": "alta"
    }
  ],
  "keywords": [
    {
      "keyword": "claude code tutorial",
      "avg_monthly_searches": 5000,
      "competition": "MEDIUM",
      "cpc": 0.50,
      "trend": "crescente"
    }
  ],
  "stagionalita": {
    "mesi_migliori": ["settembre", "ottobre", "novembre"],
    "giorni_migliori": ["martedì", "mercoledì", "giovedì"],
    "ore_migliori": ["15:00-17:00", "18:00-20:00"]
  },
  "forecast": [
    {
      "periodo": "3 mesi",
      "trend_previsto": "crescente",
      "motivazione": "Crescita media recente: 180%",
      "confidenza": 0.85
    }
  ]
}
```
**Time:** 18 minuti  
**API Units:** 950 (Google Trends: 2, Keyword Planner: 1, YouTube: 80)

---

### Example 2: Edge Case (Nessun Trend Trovato)
**Input:**
- nicchia="nicchia troppo specifica"
- competitor_channels=8

**Execution:**
1. Memory bootstrap → CP created
2. Google Trends: 0 trend trovati
3. Suggest alternatives: "Claude Code Python", "AI coding italiano"
4. Retry with broader niche
5. Report parziale con warning

**Output:**
```json
{
  "nicchia": "nicchia troppo specifica",
  "warning": "Nessun trend trovato, nicchia troppo specifica",
  "suggestions": [
    "Rilassare nicchia a 'Claude Code'",
    "Considerare nicchia correlata 'AI coding italiano'"
  ]
}
```

---

### Example 3: Failure Recovery (API Quota Exceeded)
**Input:**
- nicchia="AI coding"
- competitor_channels=8

**Execution:**
1. Memory bootstrap → CP created
2. Google Trends: 5 trend analizzati
3. API call #6: quota exceeded (100 requests/hour)
4. Save partial, warning to user
5. Memory update → CP created (status="partial", quota_exceeded=true)

**Output:**
```json
{
  "nicchia": "AI coding",
  "partial": true,
  "quota_exceeded": true,
  "trend_analyzed": 5,
  "recommendations": [
    "Riprendere analisi tra 1 ora",
    "Usare account API alternativo",
    "Ridurre competitor_channels a 5"
  ]
}
```

---

## Quality Gates

Prima di consegnare il report, verificare:
- [ ] ≥10 trend identificati (o warning giustificato)
- [ ] ≥20 keyword analizzate
- [ ] Stagionalità documentata (mesi, giorni, ore)
- [ ] Forecast con confidenza ≥0.7
- [ ] OGNI dato ha fonte tracciabile (API, data)
- [ ] Checkpoint creato in memory/youtube/checkpoints/
- [ ] Report salvato in memory/youtube/knowledge/trends/
- [ ] MEMORY-INDEX.md aggiornato
- [ ] Handoff loggato (se applicabile)

---

## Monitoring

**Metrics:**
- Tempo esecuzione (target: <20 minuti)
- API units usate (target: <1000 per run)
- Trend identificati (target: ≥10)
- Keywords analizzate (target: ≥20)

**Alerts:**
- Quota <10% (warning)
- Timeout >3 tentativi (error)
- Error rate >5% (critical)

---

## Troubleshooting

**Problem:** 0 trend trovati
**Solution:** Rilassare nicchia, suggerire alternative

**Problem:** API quota exceeded
**Solution:** Salvare parziale, riprendere dopo 1 ora o usare account alternativo

**Problem:** Timeout su API call
**Solution:** Retry automatico (max 3 tentativi), poi fallback a dati cached

**Problem:** Dati inconsistenti
**Solution:** Validare dati con schema, scartare entry incomplete

---

**Version:** 1.0  
**Created:** 2026-07-20  
**Owner:** Gael  
**Supervision:** Max
