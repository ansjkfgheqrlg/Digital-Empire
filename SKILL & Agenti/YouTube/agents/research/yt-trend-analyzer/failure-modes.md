# yt-trend-analyzer — Failure Modes

## Overview
Questo documento cataloga i failure modes specifici per yt-trend-analyzer, con prevenzione, detection e recovery. Segue P09 (Failure-Modes-First-Class).

---

## Failure Modes Table

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-TA-001 | Google Trends quota exceeded | `429 Too Many Requests` | Monitor API usage, set alerts at 90% | Check response code, log API units | Save partial report, resume in 1 hour or use alt account |
| FM-TA-002 | Keyword Planner quota exceeded | `403 Quota Exceeded` | Monitor monthly quota | Check response code | Save partial, use alt account or reduce scope |
| FM-TA-003 | Timeout su API call | Timeout dopo 30s | Retry con backoff esponenziale | Check timeout flag | Retry max 3x, extend timeframe if needed |
| FM-TA-004 | 0 trend trovati | Empty trends list | Use broader niche initially | Check trends count | Suggest alternative nicchie, relax scope |
| FM-TA-005 | Dati incompleti (AP01) | Missing sources, API traces | Validate schema, filter incomplete | Check required fields | Remove incomplete entries, log AP01 |
| FM-TA-006 | Nicchia troppo specifica | <10 trend trovati | Suggest broader niche | Check trend count | Suggest alternatives, extend timeframe |
| FM-TA-007 | Dati inconsistenti | Conflicting stats | Cross-validate sources | Validate data consistency | Discard inconsistent data, log warning |
| FM-TA-008 | Memory non aggiornato | CP missing, INDEX stale | Mandatory memory step | Check CP exists | Create CP retroactively, update INDEX |
| FM-TA-009 | Handoff fallito | Next agent can't consume | Validate handoff schema | Check handoff data | Re-generate handoff, fix schema |
| FM-TA-010 | Quality gate fallito | Report incomplete | Enforce quality gates pre-delivery | Check gate conditions | Retry with extended timeframe or broader niche |
| FM-TA-011 | Forecast confidenza bassa | Confidence <0.7 | Use sufficient historical data | Check confidence value | Extend timeframe, gather more data |
| FM-TA-012 | Stagionalità insufficiente | <3 mesi dati | Require minimum 3 months data | Check data length | Extend timeframe, use competitor data |

---

## Detailed Failure Modes

### FM-TA-001: Google Trends Quota Exceeded

**Symptom:**
```
HTTP 429 Too Many Requests
{
  "error": {
    "code": 429,
    "message": "Quota exceeded for Google Trends API"
  }
}
```

**Prevention:**
```python
# Monitor API usage
if api.calls_used > 90:  # 90% of 100/hour quota
    logger.warning("Google Trends quota >90%, consider stopping")
    return partial_report(quota_warning=True)
```

**Detection:**
```python
try:
    response = requests.get(url, params=params)
    if response.status_code == 429:
        raise QuotaExceededError()
except QuotaExceededError:
    logger.error("Google Trends quota exceeded")
    return handle_quota_exceeded()
```

**Recovery:**
```python
def handle_quota_exceeded():
    """Salva report parziale e suggerisce recovery."""
    partial_report = {
        "partial": True,
        "quota_exceeded": True,
        "recommendations": [
            "Riprendere analisi tra 1 ora",
            "Usare account API alternativo",
            "Ridurre competitor_channels a 5"
        ]
    }
    
    memory.create_checkpoint(
        id="yt-trend-analyzer-partial",
        description="Analisi interrotta per quota exceeded",
        output_data=partial_report,
        status="partial"
    )
    
    return partial_report
```

---

### FM-TA-002: Keyword Planner Quota Exceeded

**Symptom:**
```
HTTP 403 Forbidden
{
  "error": {
    "code": 403,
    "message": "Quota exceeded for Keyword Planner API"
  }
}
```

**Prevention:**
```python
# Monitor monthly quota
if api.calls_used > 9000:  # 90% of 10,000/month quota
    logger.warning("Keyword Planner quota >90%, consider stopping")
    return partial_report(quota_warning=True)
```

**Detection:**
```python
try:
    response = requests.post(url, json=payload)
    if response.status_code == 403:
        error_data = response.json()
        if "quota" in error_data["error"]["message"].lower():
            raise QuotaExceededError()
except QuotaExceededError:
    logger.error("Keyword Planner quota exceeded")
    return handle_keyword_quota_exceeded()
```

**Recovery:**
```python
def handle_keyword_quota_exceeded():
    """Salva report parziale e suggerisce recovery."""
    partial_report = {
        "partial": True,
        "quota_exceeded": True,
        "recommendations": [
            "Riprendere analisi prossimo mese",
            "Usare account Google Ads alternativo",
            "Ridurre max_results a 20"
        ]
    }
    
    return partial_report
```

---

### FM-TA-003: Timeout su API Call

**Symptom:**
```
TimeoutError: HTTPSConnectionPool(host='trends.google.com', port=443): Read timed out. (read timeout=30)
```

**Prevention:**
```python
# Retry con backoff esponenziale
def api_call_with_retry(url, params, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=30)
            return response
        except TimeoutError:
            wait_time = 2 ** attempt  # 1s, 2s, 4s
            logger.warning(f"Timeout attempt {attempt+1}, waiting {wait_time}s")
            time.sleep(wait_time)
    
    raise TimeoutError(f"Failed after {max_retries} attempts")
```

**Detection:**
```python
try:
    response = api_call_with_retry(url, params)
except TimeoutError as e:
    logger.error(f"API call timeout: {e}")
    return handle_timeout()
```

**Recovery:**
```python
def handle_timeout():
    """Extend timeframe e retry."""
    # Extend timeframe
    extended_timeframe = "6_months" if timeframe == "3_months" else "12_months"
    
    logger.info(f"Extending timeframe to: {extended_timeframe}")
    
    # Retry with extended timeframe
    try:
        response = api_call_with_retry(url, {"timeframe": extended_timeframe})
        return process_response(response)
    except TimeoutError:
        logger.error("Timeout persists after extension")
        return {"error": "timeout", "timeframe_extended": True}
```

---

### FM-TA-004: 0 Trend Trovati

**Symptom:**
```json
{
  "trends": [],
  "total_results": 0
}
```

**Prevention:**
```python
# Use lenient filters initially
keyword = nicchia  # Start with exact match
```

**Detection:**
```python
if len(trends) == 0:
    logger.warning("0 trends found with current keyword")
    return handle_no_trends()
```

**Recovery:**
```python
def handle_no_trends():
    """Suggest alternative nicchie."""
    suggestions = [
        f"Rilassare nicchia a '{nicchia.split()[0]}'",
        "Considerare nicchia correlata",
        "Valutare lingua diversa (es. inglese)"
    ]
    
    return {
        "trends": [],
        "suggestions": suggestions
    }
```

---

### FM-TA-005: Dati Incompleti (AP01)

**Symptom:**
```json
{
  "trend": "Claude Code tutorial",
  "crescita": 450,
  "fonte": null  // Missing
}
```

**Prevention:**
```python
# Validate required fields
REQUIRED_FIELDS = ["argomento", "crescita_percentuale", "volume_ricerche"]

def validate_trend_data(trend):
    for field in REQUIRED_FIELDS:
        if not trend.get(field):
            raise IncompleteDataError(f"Missing required field: {field}")
```

**Detection:**
```python
incomplete_trends = []
for trend in trends:
    try:
        validate_trend_data(trend)
    except IncompleteDataError as e:
        logger.warning(f"AP01 detected: {e}")
        incomplete_trends.append(trend)
```

**Recovery:**
```python
def handle_incomplete_data(trends):
    """Filter out incomplete entries."""
    complete_trends = []
    
    for trend in trends:
        try:
            validate_trend_data(trend)
            complete_trends.append(trend)
        except IncompleteDataError:
            logger.warning(f"Removing incomplete trend: {trend.get('argomento')}")
    
    if len(complete_trends) < 10:
        logger.warning("Too many incomplete trends, quality gate may fail")
    
    return complete_trends
```

---

### FM-TA-006: Nicchia Troppo Specifica

**Symptom:**
```json
{
  "trend_identified": 8,
  "warning": "Nicchia troppo specifica, pochi trend trovati"
}
```

**Prevention:**
```python
# Check trend count early
if len(trends) < 10:
    logger.warning("Low trend count, niche may be too specific")
```

**Detection:**
```python
if len(trends) < 10:
    return handle_small_niche()
```

**Recovery:**
```python
def handle_small_niche():
    """Suggest broader niche."""
    suggestions = [
        f"Rilassare nicchia a '{nicchia.split()[0]}'",
        "Considerare nicchia correlata",
        "Estendere timeframe a 6 mesi"
    ]
    
    return {
        "trend_identified": len(trends),
        "warning": "Nicchia troppo specifica, pochi trend trovati",
        "suggestions": suggestions
    }
```

---

### FM-TA-007: Dati Inconsistenti

**Symptom:**
```json
{
  "volume_ricerche": 100,
  "crescita_percentuale": 500  // Inconsistent: high growth, low volume
}
```

**Prevention:**
```python
# Cross-validate stats
def validate_trend_stats(trend):
    if trend["volume_ricerche"] < 100 and trend["crescita_percentuale"] > 200:
        raise InconsistentDataError("High growth with low volume is suspicious")
```

**Detection:**
```python
try:
    validate_trend_stats(trend)
except InconsistentDataError as e:
    logger.warning(f"Data inconsistency: {e}")
```

**Recovery:**
```python
def handle_inconsistent_data(trend):
    """Discard inconsistent data, log warning."""
    logger.warning(f"Discarding inconsistent trend: {trend['argomento']}")
    
    # Log to failure modes
    memory.log_failure_mode(
        id="FM-TA-007",
        description="Data inconsistency detected",
        trend_data=trend
    )
    
    return None  # Discard
```

---

### FM-TA-008: Memory Non Aggiornato

**Symptom:**
```bash
ls memory/youtube/checkpoints/CP-*trend*.md
# No files found
```

**Prevention:**
```python
# Mandatory memory step
def analyze_trends(nicchia):
    # Step 1: Memory bootstrap (MANDATORY)
    memory.create_checkpoint(id="start", ...)
    
    # ... analysis ...
    
    # Step 8: Memory update (MANDATORY)
    memory.create_checkpoint(id="complete", ...)
```

**Detection:**
```python
# Check if CP exists
checkpoint_path = memory.checkpoints_path / f"CP-{id}.md"
if not checkpoint_path.exists():
    logger.error(f"Memory not updated: {checkpoint_path} missing")
    handle_missing_memory()
```

**Recovery:**
```python
def handle_missing_memory():
    """Create CP retroactively."""
    logger.warning("Creating memory checkpoint retroactively")
    
    memory.create_checkpoint(
        id="yt-trend-analyzer-retroactive",
        description="Memory checkpoint created retroactively",
        status="retroactive"
    )
```

---

### FM-TA-009: Handoff Fallito

**Symptom:**
```python
next_agent.consume_data(handoff_data)
# Error: Invalid schema
```

**Prevention:**
```python
# Validate handoff schema
HANDOFF_SCHEMA = {
    "nicchia": str,
    "keywords": list,
    "trends": list,
    "seasonality": dict,
    "report_path": str
}

def validate_handoff_schema(data):
    for field, field_type in HANDOFF_SCHEMA.items():
        if field not in data:
            raise HandoffSchemaError(f"Missing field: {field}")
        if not isinstance(data[field], field_type):
            raise HandoffSchemaError(f"Invalid type for {field}")
```

**Detection:**
```python
try:
    validate_handoff_schema(handoff_data)
except HandoffSchemaError as e:
    logger.error(f"Handoff schema error: {e}")
    handle_handoff_failure()
```

**Recovery:**
```python
def handle_handoff_failure():
    """Re-generate handoff with correct schema."""
    logger.warning("Re-generating handoff data")
    
    handoff_data = {
        "nicchia": nicchia,
        "keywords": keywords,
        "trends": trends,
        "seasonality": seasonality,
        "report_path": report_path
    }
    
    # Validate again
    validate_handoff_schema(handoff_data)
    
    return handoff_data
```

---

### FM-TA-010: Quality Gate Fallito

**Symptom:**
```json
{
  "quality_gate": {
    "passed": false,
    "failed_conditions": ["trend_identified < 10"]
  }
}
```

**Prevention:**
```python
# Enforce quality gates
QUALITY_GATES = {
    "trend_identified": {"min": 10, "max": None},
    "keywords_researched": {"min": 20, "max": None},
    "seasonality_documented": {"required": True},
    "forecast_confidence": {"min": 0.7, "max": 1.0}
}

def check_quality_gates(report):
    for gate, constraints in QUALITY_GATES.items():
        if "min" in constraints:
            value = report.get(gate, 0)
            if value < constraints["min"]:
                return False, f"{gate} < {constraints['min']}"
    return True, None
```

**Detection:**
```python
passed, failed_condition = check_quality_gates(report)
if not passed:
    logger.warning(f"Quality gate failed: {failed_condition}")
    handle_quality_gate_failure()
```

**Recovery:**
```python
def handle_quality_gate_failure():
    """Retry with extended timeframe or broader niche."""
    logger.info("Retrying with extended timeframe")
    
    # Extend timeframe
    timeframe = "6_months" if timeframe == "3_months" else "12_months"
    
    # Retry analysis
    trends_result = google_trends_api.analyze(keyword=nicchia, timeframe=timeframe)
    
    # Re-check quality gates
    return analyze_and_check(trends_result)
```

---

### FM-TA-011: Forecast Confidenza Bassa

**Symptom:**
```json
{
  "forecast": [
    {
      "periodo": "3 mesi",
      "confidenza": 0.65
    }
  ]
}
```

**Prevention:**
```python
# Require sufficient historical data
if len(historical_data) < 3:
    logger.warning("Insufficient historical data for forecast")
    return {"forecast": [], "warning": "Dati insufficienti per forecast"}
```

**Detection:**
```python
for f in forecast:
    if f["confidenza"] < 0.7:
        logger.warning(f"Low confidence forecast: {f['periodo']} ({f['confidenza']})")
```

**Recovery:**
```python
def handle_low_confidence_forecast():
    """Extend timeframe and gather more data."""
    logger.info("Extending timeframe for better forecast")
    
    # Extend timeframe
    extended_timeframe = "6_months" if timeframe == "3_months" else "12_months"
    
    # Gather more historical data
    more_data = gather_historical_data(nicchia, extended_timeframe)
    
    # Re-generate forecast
    forecast = generate_forecast(
        trends=trends,
        historical_data=more_data,
        confidence_threshold=0.7
    )
    
    return forecast
```

---

### FM-TA-012: Stagionalità Insufficiente

**Symptom:**
```json
{
  "stagionalita": {
    "mesi_migliori": [],
    "giorni_migliori": [],
    "ore_migliori": []
  }
}
```

**Prevention:**
```python
# Require minimum data
if len(competitor_activity) < 30:
    logger.warning("Insufficient competitor data for seasonality analysis")
    return {"stagionalita": {}, "warning": "Dati insufficienti per stagionalità"}
```

**Detection:**
```python
if not seasonality["mesi_migliori"]:
    logger.warning("Seasonality data incomplete")
    handle_insufficient_seasonality()
```

**Recovery:**
```python
def handle_insufficient_seasonality():
    """Use competitor data as fallback."""
    logger.info("Using competitor data for seasonality")
    
    # Analyze competitor activity
    competitor_seasonality = analyze_competitor_seasonality(competitor_activity)
    
    # Merge with trend seasonality
    merged_seasonality = merge_seasonality(trends_seasonality, competitor_seasonality)
    
    return merged_seasonality
```

---

## Global Rules

1. **Log ALL failures:** Ogni failure mode deve essere loggato in `memory/youtube/logs/yt-trend-analyzer.log`
2. **P09 compliance:** OGNI failure mode ha prevenzione, detection, recovery
3. **P10 compliance:** OGNI recovery crea CP e aggiorna MEMORY-INDEX
4. **Silent observer:** Failure modes osservati da silent-observer-agent (PT07)
5. **Continuous improvement:** Failure modes usati per migliorare agente (P10 loops)

---

## Trace

- **P09:** Failure-Modes-First-Class
- **P10:** Self-Improvement-Loops
- **PT07:** Silent-Observer
- **CS03:** SI with observer (mistake was assuming SI without observer = drift)
- **CS04:** Bugs in real test (enforced real-test + bug logging)

---

**Version:** 1.0  
**Created:** 2026-07-20  
**Owner:** Gael  
**Supervision:** Max
