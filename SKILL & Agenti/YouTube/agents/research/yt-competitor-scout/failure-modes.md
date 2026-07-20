# yt-competitor-scout — Failure Modes

## Overview
Questo documento cataloga i failure modes specifici per yt-competitor-scout, con prevenzione, detection e recovery. Segue P09 (Failure-Modes-First-Class).

---

## Failure Modes Table

| ID | Failure | Symptom | Prevention | Detection | Recovery |
|---|---|---|---|---|---|
| FM-CS-001 | API quota exceeded | `403 Quota Exceeded` error | Monitor API usage, set alerts at 90% | Check response code, log API units | Save partial report, resume tomorrow or use alt account |
| FM-CS-002 | Timeout su API call | Timeout dopo 30s | Retry con backoff esponenziale | Check timeout flag | Retry max 3x, refine query if needed |
| FM-CS-003 | 0 canali trovati | Empty channels list | Relax filters (subscriber_min=500) | Check channels count | Relax filters, suggest alternative nicchie |
| FM-CS-004 | Dati incompleti (AP01) | Missing URLs, sources | Validate schema, filter incomplete | Check required fields | Remove incomplete entries, log AP01 |
| FM-CS-005 | Nicchia troppo specifica | <5 competitor trovati | Suggest broader nicchia | Check competitor count | Suggest alternatives, relax scope |
| FM-CS-006 | Dati inconsistenti | Conflicting stats | Cross-validate sources | Validate data consistency | Discard inconsistent data, log warning |
| FM-CS-007 | Memory non aggiornato | CP missing, INDEX stale | Mandatory memory step | Check CP exists | Create CP retroactively, update INDEX |
| FM-CS-008 | Handoff fallito | Next agent can't consume | Validate handoff schema | Check handoff data | Re-generate handoff, fix schema |
| FM-CS-009 | Quality gate fallito | Report incomplete | Enforce quality gates pre-delivery | Check gate conditions | Retry with relaxed filters |
| FM-CS-010 | Rate limit YouTube | 429 Too Many Requests | Implement rate limiting | Check response code | Backoff, wait, retry |

---

## Detailed Failure Modes

### FM-CS-001: API Quota Exceeded

**Symptom:**
```
HTTP 403 Forbidden
{
  "error": {
    "code": 403,
    "message": "Quota exceeded for quota metric 'Search Requests'..."
  }
}
```

**Prevention:**
```python
# Monitor API usage
if api.units_used > 9000:  # 90% of 10,000 daily quota
    logger.warning("API quota >90%, consider stopping")
    return partial_report(quota_warning=True)
```

**Detection:**
```python
try:
    response = requests.get(url, params=params)
    if response.status_code == 403:
        error_data = response.json()
        if "quota" in error_data["error"]["message"].lower():
            raise QuotaExceededError()
except QuotaExceededError:
    logger.error("API quota exceeded")
    return handle_quota_exceeded()
```

**Recovery:**
```python
def handle_quota_exceeded():
    """Salva report parziale e suggerisce recovery."""
    partial_report = {
        "partial": True,
        "competitor_analyzed": len(channels_analyzed),
        "quota_exceeded": True,
        "recommendations": [
            "Riprendere analisi domani",
            "Usare account API alternativo",
            "Ridurre num_canali per nächste run"
        ]
    }
    
    memory.create_checkpoint(
        id="yt-competitor-scout-partial",
        description="Analisi interrotta per quota exceeded",
        output_data=partial_report,
        status="partial"
    )
    
    return partial_report
```

---

### FM-CS-002: Timeout su API Call

**Symptom:**
```
TimeoutError: HTTPSConnectionPool(host='www.googleapis.com', port=443): Read timed out. (read timeout=30)
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
    """Refine query e retry."""
    # Refine query
    refined_query = f"{original_query} italiano beginner"
    
    logger.info(f"Refining query to: {refined_query}")
    
    # Retry with refined query
    try:
        response = api_call_with_retry(url, {"q": refined_query})
        return process_response(response)
    except TimeoutError:
        logger.error("Timeout persists after refinement")
        return {"error": "timeout", "refinement_attempted": True}
```

---

### FM-CS-003: 0 Canali Trovati

**Symptom:**
```json
{
  "channels": [],
  "total_results": 0
}
```

**Prevention:**
```python
# Use lenient filters initially
filters = {
    "subscriber_min": 1000,  # Start with reasonable threshold
    "language": "it"
}
```

**Detection:**
```python
if len(channels) == 0:
    logger.warning("0 channels found with current filters")
    return handle_no_channels()
```

**Recovery:**
```python
def handle_no_channels():
    """Relax filters and retry."""
    # Relax filters
    relaxed_filters = {
        "subscriber_min": 500,  # Reduced threshold
        "language": "it"
    }
    
    logger.info("Relaxing filters and retrying")
    
    # Retry with relaxed filters
    channels_result = api.search_channels(query=nicchia, filters=relaxed_filters)
    
    if len(channels_result["channels"]) == 0:
        # Suggest alternatives
        return {
            "channels": [],
            "suggestions": [
                f"Rilassare nicchia a '{nicchia.split()[0]}'",
                "Considerare nicchia correlata",
                "Valutare lingua diversa (es. inglese)"
            ]
        }
    
    return channels_result
```

---

### FM-CS-004: Dati Incompleti (AP01)

**Symptom:**
```json
{
  "video_id": "abc123",
  "title": "Video Title",
  "description": null,  // Missing
  "thumbnail_url": ""   // Empty
}
```

**Prevention:**
```python
# Validate required fields
REQUIRED_FIELDS = ["video_id", "title", "view_count", "thumbnail_url"]

def validate_video_data(video):
    for field in REQUIRED_FIELDS:
        if not video.get(field):
            raise IncompleteDataError(f"Missing required field: {field}")
```

**Detection:**
```python
incomplete_videos = []
for video in videos:
    try:
        validate_video_data(video)
    except IncompleteDataError as e:
        logger.warning(f"AP01 detected: {e}")
        incomplete_videos.append(video)
```

**Recovery:**
```python
def handle_incomplete_data(videos):
    """Filter out incomplete entries."""
    complete_videos = []
    
    for video in videos:
        try:
            validate_video_data(video)
            complete_videos.append(video)
        except IncompleteDataError:
            logger.warning(f"Removing incomplete video: {video.get('video_id')}")
    
    if len(complete_videos) < 5:
        logger.warning("Too many incomplete videos, quality gate may fail")
    
    return complete_videos
```

---

### FM-CS-005: Nicchia Troppo Specifica

**Symptom:**
```json
{
  "competitor_analyzed": 3,
  "warning": "Nicchia troppo specifica, pochi competitor trovati"
}
```

**Prevention:**
```python
# Check competitor count early
if len(channels) < 5:
    logger.warning("Low competitor count, niche may be too specific")
```

**Detection:**
```python
if len(channels_analyzed) < 5:
    return handle_small_niche()
```

**Recovery:**
```python
def handle_small_niche():
    """Suggest broader niche."""
    suggestions = [
        f"Rilassare nicchia a '{nicchia.split()[0]}'",
        "Considerare nicchia correlata",
        "Valutare formato video più breve (5-8 minuti)"
    ]
    
    return {
        "competitor_analyzed": len(channels_analyzed),
        "warning": "Nicchia troppo specifica, pochi competitor trovati",
        "suggestions": suggestions
    }
```

---

### FM-CS-006: Dati Inconsistenti

**Symptom:**
```json
{
  "subscriber_count": 10000,
  "video_count": 5,
  "avg_views": 50000  // Inconsistent: views > subscribers
}
```

**Prevention:**
```python
# Cross-validate stats
def validate_stats(channel):
    if channel["video_count"] > 0:
        avg_views = channel["view_count"] / channel["video_count"]
        if avg_views > channel["subscriber_count"] * 10:
            raise InconsistentDataError("Views unusually high vs subscribers")
```

**Detection:**
```python
try:
    validate_stats(channel)
except InconsistentDataError as e:
    logger.warning(f"Data inconsistency: {e}")
```

**Recovery:**
```python
def handle_inconsistent_data(channel):
    """Discard inconsistent data, log warning."""
    logger.warning(f"Discarding inconsistent channel: {channel['channel_name']}")
    
    # Log to failure modes
    memory.log_failure_mode(
        id="FM-CS-006",
        description="Data inconsistency detected",
        channel_data=channel
    )
    
    return None  # Discard
```

---

### FM-CS-007: Memory Non Aggiornato

**Symptom:**
```bash
ls memory/youtube/checkpoints/CP-*competitor*.md
# No files found
```

**Prevention:**
```python
# Mandatory memory step
def analyze_competitors(nicchia):
    # Step 1: Memory bootstrap (MANDATORY)
    memory.create_checkpoint(id="start", ...)
    
    # ... analysis ...
    
    # Step 6: Memory update (MANDATORY)
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
        id="yt-competitor-scout-retroactive",
        description="Memory checkpoint created retroactively",
        status="retroactive"
    )
```

---

### FM-CS-008: Handoff Fallito

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
    "competitor_channels": list,
    "gaps": list,
    "best_practices": list,
    "opportunities": list,
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
        "competitor_channels": [ch["channel_id"] for ch in channels_analyzed],
        "gaps": gaps,
        "best_practices": best_practices,
        "opportunities": opportunities,
        "report_path": report_path
    }
    
    # Validate again
    validate_handoff_schema(handoff_data)
    
    return handoff_data
```

---

### FM-CS-009: Quality Gate Fallito

**Symptom:**
```json
{
  "quality_gate": {
    "passed": false,
    "failed_conditions": ["competitor_analyzed < 5"]
  }
}
```

**Prevention:**
```python
# Enforce quality gates
QUALITY_GATES = {
    "competitor_analyzed": {"min": 5, "max": None},
    "gaps_identified": {"min": 3, "max": None},
    "best_practices": {"min": 5, "max": None},
    "opportunities": {"min": 3, "max": None}
}

def check_quality_gates(report):
    for gate, constraints in QUALITY_GATES.items():
        value = report.get(gate, 0)
        if constraints["min"] and value < constraints["min"]:
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
    """Retry with relaxed filters."""
    logger.info("Retrying with relaxed filters")
    
    # Relax filters
    filters["subscriber_min"] = max(100, filters["subscriber_min"] - 500)
    
    # Retry analysis
    channels_result = api.search_channels(query=nicchia, filters=filters)
    
    # Re-check quality gates
    return analyze_and_check(channels_result)
```

---

### FM-CS-010: Rate Limit YouTube

**Symptom:**
```
HTTP 429 Too Many Requests
{
  "error": {
    "code": 429,
    "message": "Rate limit exceeded"
  }
}
```

**Prevention:**
```python
# Implement rate limiting
import time

class RateLimiter:
    def __init__(self, max_calls=10, period=60):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
    
    def wait_if_needed(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < self.period]
        
        if len(self.calls) >= self.max_calls:
            sleep_time = self.period - (now - self.calls[0])
            logger.info(f"Rate limit reached, sleeping {sleep_time:.1f}s")
            time.sleep(sleep_time)
        
        self.calls.append(time.time())
```

**Detection:**
```python
try:
    rate_limiter.wait_if_needed()
    response = requests.get(url, params=params)
    if response.status_code == 429:
        raise RateLimitError()
except RateLimitError:
    logger.error("Rate limit exceeded")
    handle_rate_limit()
```

**Recovery:**
```python
def handle_rate_limit():
    """Backoff and retry."""
    wait_time = 60  # Wait 60 seconds
    logger.info(f"Rate limit exceeded, waiting {wait_time}s")
    time.sleep(wait_time)
    
    # Retry
    response = requests.get(url, params=params)
    return process_response(response)
```

---

## Global Rules

1. **Log ALL failures:** Ogni failure mode deve essere loggato in `memory/youtube/logs/yt-competitor-scout.log`
2. **P09 compliance:** OGNI failure mode ha prevenzione, detection, recovery
3. **P10 compliance:** OGNI recovery crea CP e aggiorna MEMORY-INDEX
4. **Silent observer:** Failure modes osservati da silent-observer-agent (PT07)
5. **Continuous improvement:** Failure modes usati per migliorare agente (P10 loops)

---

## Failure Mode Log Template

```markdown
## FM-CS-XXX: [Failure Title]

**Timestamp:** 2026-07-20 14:30:00  
**Nicchia:** Claude Code  
**Symptom:** [Description]  
**Root Cause:** [Analysis]  
**Prevention Applied:** [What was done]  
**Detection Method:** [How detected]  
**Recovery Action:** [What was done]  
**Outcome:** [Success/Failure]  
**Lesson Learned:** [What to improve]

---
```

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
