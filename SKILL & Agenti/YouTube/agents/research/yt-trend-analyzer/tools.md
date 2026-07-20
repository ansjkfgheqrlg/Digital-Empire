# yt-trend-analyzer — Tools

## Tool 1: google_trends_analyze

**Purpose:** Analizzare trend con Google Trends API

**Input Schema:**
```json
{
  "keyword": "string",
  "timeframe": "string (e.g., '3_months', '6_months', '12_months')",
  "geo": "string (ISO 3166-1, default 'IT')",
  "category": "integer (default 0)"
}
```

**Output Schema:**
```json
{
  "trends": [
    {
      "argomento": "string",
      "crescita_percentuale": "number",
      "volume_ricerche": "number",
      "stagionalita": "string (crescente|decrescente|stabile)",
      "interest_over_time": "array of numbers"
    }
  ],
  "related_queries": [
    {
      "query": "string",
      "volume": "number",
      "growth": "string"
    }
  ],
  "api_calls_used": "integer"
}
```

**Implementation:**
```python
from pytrends.request import TrendReq
from typing import List, Dict

class GoogleTrendsAPI:
    def __init__(self):
        self.pytrends = TrendReq(hl='it-IT', tz=360)
        self.calls_used = 0
    
    def analyze(
        self,
        keyword: str,
        timeframe: str = "3_months",
        geo: str = "IT",
        category: int = 0
    ) -> Dict:
        """Analizza trend con Google Trends."""
        
        # Build payload
        self.pytrends.build_payload(
            kw_list=[keyword],
            cat=category,
            timeframe=timeframe,
            geo=geo
        )
        self.calls_used += 1
        
        # Get interest over time
        interest_df = self.pytrends.interest_over_time()
        self.calls_used += 1
        
        # Get related queries
        related_queries = self.pytrends.related_queries()
        self.calls_used += 1
        
        # Process data
        trends = []
        if not interest_df.empty:
            values = interest_df[keyword].tolist()
            growth = ((values[-1] - values[0]) / values[0] * 100) if values[0] > 0 else 0
            
            trends.append({
                "argomento": keyword,
                "crescita_percentuale": round(growth, 2),
                "volume_ricerche": sum(values),
                "stagionalita": "crescente" if growth > 10 else "decrescente" if growth < -10 else "stabile",
                "interest_over_time": values
            })
        
        # Process related queries
        related = []
        if keyword in related_queries and related_queries[keyword]['top'] is not None:
            top_df = related_queries[keyword]['top']
            for _, row in top_df.iterrows():
                related.append({
                    "query": row['query'],
                    "volume": row['value'],
                    "growth": "high" if row['value'] > 50 else "medium"
                })
        
        return {
            "trends": trends,
            "related_queries": related,
            "api_calls_used": self.calls_used
        }
```

---

## Tool 2: keyword_planner_research

**Purpose:** Ricercare keyword con Keyword Planner API

**Input Schema:**
```json
{
  "seed_keywords": ["string"],
  "max_results": "integer (default 50)",
  "language": "string (ISO 639-1, default 'it')",
  "location": "string (ISO 3166-1, default 'IT')"
}
```

**Output Schema:**
```json
{
  "keywords": [
    {
      "keyword": "string",
      "avg_monthly_searches": "integer",
      "competition": "string (LOW|MEDIUM|HIGH)",
      "cpc": "number (€)",
      "trend": "string (crescente|decrescente|stabile)"
    }
  ],
  "api_calls_used": "integer"
}
```

**Implementation:**
```python
from google.ads.googleads.client import GoogleAdsClient
from typing import List, Dict

class KeywordPlannerAPI:
    def __init__(self, credentials_path: str):
        self.client = GoogleAdsClient.load_from_storage(credentials_path)
        self.calls_used = 0
    
    def research(
        self,
        seed_keywords: List[str],
        max_results: int = 50,
        language: str = "it",
        location: str = "IT"
    ) -> Dict:
        """Ricercare keyword con Keyword Planner."""
        
        keyword_plan_idea_service = self.client.get_service("KeywordPlanIdeaService")
        
        request = self.client.get_type("GenerateKeywordIdeasRequest")
        request.language = f"languageConstants/{language}"
        request.geo_target_constants.append(f"geoTargetConstants/{location}")
        request.keyword_seed.keywords.extend(seed_keywords)
        
        response = keyword_plan_idea_service.generate_keyword_ideas(request=request)
        self.calls_used += 1
        
        keywords = []
        for result in response.results[:max_results]:
            keyword_metrics = result.keyword_idea_metrics
            
            keywords.append({
                "keyword": result.text,
                "avg_monthly_searches": keyword_metrics.avg_monthly_searches,
                "competition": keyword_metrics.competition.name,
                "cpc": keyword_metrics.low_top_of_page_bid_micros / 1_000_000,
                "trend": self._determine_trend(keyword_metrics.monthly_search_volumes)
            })
        
        return {
            "keywords": keywords,
            "api_calls_used": self.calls_used
        }
    
    def _determine_trend(self, monthly_volumes) -> str:
        """Determina trend da volumi mensili."""
        if len(monthly_volumes) < 3:
            return "stabile"
        
        recent = [mv.monthly_searches for mv in monthly_volumes[-3:]]
        older = [mv.monthly_searches for mv in monthly_volumes[:3]]
        
        avg_recent = sum(recent) / len(recent)
        avg_older = sum(older) / len(older)
        
        growth = ((avg_recent - avg_older) / avg_older * 100) if avg_older > 0 else 0
        
        if growth > 10:
            return "crescente"
        elif growth < -10:
            return "decrescente"
        else:
            return "stabile"
```

---

## Tool 3: analyze_seasonality

**Purpose:** Analizzare stagionalità da trend data

**Input Schema:**
```json
{
  "trends": "array of trend objects",
  "competitor_activity": "array of video objects",
  "timeframe": "string"
}
```

**Output Schema:**
```json
{
  "mesi_migliori": ["string"],
  "giorni_migliori": ["string"],
  "ore_migliori": ["string"],
  "motivazione": "string"
}
```

**Implementation:**
```python
from datetime import datetime
from collections import Counter
from typing import List, Dict

def analyze_seasonality(
    trends: List[Dict],
    competitor_activity: List[Dict],
    timeframe: str
) -> Dict:
    """Analizza stagionalità da trend e attività competitor."""
    
    # Analyze monthly patterns from trends
    monthly_engagement = Counter()
    for trend in trends:
        if "interest_over_time" in trend:
            for i, value in enumerate(trend["interest_over_time"]):
                month = i % 12  # Assuming monthly data
                monthly_engagement[month] += value
    
    # Top 3 months
    top_months = [m for m, _ in monthly_engagement.most_common(3)]
    month_names = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
                   "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
    mesi_migliori = [month_names[m] for m in top_months]
    
    # Analyze day patterns from competitor activity
    daily_engagement = Counter()
    for video in competitor_activity:
        if "published_at" in video:
            published = datetime.fromisoformat(video["published_at"].replace('Z', '+00:00'))
            day = published.weekday()  # 0=Monday, 6=Sunday
            daily_engagement[day] += video.get("view_count", 0)
    
    # Top 3 days
    top_days = [d for d, _ in daily_engagement.most_common(3)]
    day_names = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
    giorni_migliori = [day_names[d] for d in top_days]
    
    # Analyze hourly patterns
    hourly_engagement = Counter()
    for video in competitor_activity:
        if "published_at" in video:
            published = datetime.fromisoformat(video["published_at"].replace('Z', '+00:00'))
            hour = published.hour
            hourly_engagement[hour] += video.get("view_count", 0)
    
    # Top 2 time slots
    top_hours = [h for h, _ in hourly_engagement.most_common(2)]
    ore_migliori = [f"{h:02d}:00-{(h+2)%24:02d}:00" for h in top_hours]
    
    return {
        "mesi_migliori": mesi_migliori,
        "giorni_migliori": giorni_migliori,
        "ore_migliori": ore_migliori,
        "motivazione": f"Basato su analisi di {len(trends)} trend e {len(competitor_activity)} video competitor"
    }
```

---

## Tool 4: generate_forecast

**Purpose:** Generare forecast trend

**Input Schema:**
```json
{
  "trends": "array of trend objects",
  "historical_data": "array of historical data points",
  "confidence_threshold": "number (0.0-1.0)"
}
```

**Output Schema:**
```json
{
  "forecast": [
    {
      "periodo": "string",
      "trend_previsto": "string",
      "motivazione": "string",
      "confidenza": "number"
    }
  ]
}
```

**Implementation:**
```python
import numpy as np
from typing import List, Dict

def generate_forecast(
    trends: List[Dict],
    historical_data: List[Dict],
    confidence_threshold: float = 0.7
) -> Dict:
    """Genera forecast trend basato su dati storici."""
    
    forecast = []
    
    # 3-month forecast
    if len(historical_data) >= 3:
        recent_growth = []
        for i in range(1, len(historical_data)):
            growth = (historical_data[i]["value"] - historical_data[i-1]["value"]) / historical_data[i-1]["value"]
            recent_growth.append(growth)
        
        avg_growth = np.mean(recent_growth)
        confidence = min(0.95, 0.5 + len(recent_growth) * 0.1)
        
        if confidence >= confidence_threshold:
            trend_previsto = "crescente" if avg_growth > 0.05 else "decrescente" if avg_growth < -0.05 else "stabile"
            
            forecast.append({
                "periodo": "3 mesi",
                "trend_previsto": trend_previsto,
                "motivazione": f"Crescita media recente: {avg_growth*100:.1f}%",
                "confidenza": round(confidence, 2)
            })
    
    # 6-month forecast
    if len(historical_data) >= 6:
        long_term_growth = []
        for i in range(6, len(historical_data)):
            growth = (historical_data[i]["value"] - historical_data[i-6]["value"]) / historical_data[i-6]["value"]
            long_term_growth.append(growth)
        
        avg_long_growth = np.mean(long_term_growth)
        confidence = min(0.85, 0.4 + len(long_term_growth) * 0.08)
        
        if confidence >= confidence_threshold:
            trend_previsto = "crescente" if avg_long_growth > 0.05 else "decrescente" if avg_long_growth < -0.05 else "stabile"
            
            forecast.append({
                "periodo": "6 mesi",
                "trend_previsto": trend_previsto,
                "motivazione": f"Crescita media lungo termine: {avg_long_growth*100:.1f}%",
                "confidenza": round(confidence, 2)
            })
    
    return {"forecast": forecast}
```

---

## Dependencies

**Required Packages:**
```bash
pip install pytrends google-ads numpy python-dotenv
```

**Environment Variables:**
```bash
# .env
GOOGLE_ADS_DEVELOPER_TOKEN=your_token
GOOGLE_ADS_CLIENT_ID=your_client_id
GOOGLE_ADS_CLIENT_SECRET=your_client_secret
GOOGLE_ADS_REFRESH_TOKEN=your_refresh_token
```

**Rate Limits:**
- Google Trends: 100 requests/hour
- Keyword Planner: 10,000 queries/month
- YouTube Data API: 10,000 units/day

---

## Testing

```python
def test_google_trends_analyze():
    api = GoogleTrendsAPI()
    result = api.analyze(keyword="Claude Code", timeframe="3_months")
    assert "trends" in result
    assert len(result["trends"]) > 0

def test_keyword_planner_research():
    api = KeywordPlannerAPI(credentials_path="google-ads.yaml")
    result = api.research(seed_keywords=["Claude Code"], max_results=10)
    assert "keywords" in result
    assert len(result["keywords"]) > 0

def test_analyze_seasonality():
    trends = [{"interest_over_time": [10, 20, 30, 40]}]
    competitor_activity = [{"published_at": "2026-07-20T15:00:00Z", "view_count": 1000}]
    result = analyze_seasonality(trends, competitor_activity, "3_months")
    assert "mesi_migliori" in result
    assert "giorni_migliori" in result
    assert "ore_migliori" in result
```

---

**Version:** 1.0  
**Created:** 2026-07-20  
**Owner:** Gael  
**Supervision:** Max
