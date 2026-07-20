# yt-competitor-scout — Tools

## Tool 1: youtube_api_search_channels

**Purpose:** Cercare canali YouTube nella nicchia target con filtri.

**Input Schema:**
```json
{
  "query": "string",
  "max_results": "integer (1-50, default 10)",
  "filters": {
    "subscriber_min": "integer (default 0)",
    "subscriber_max": "integer (default null)",
    "language": "string (ISO 639-1, default 'it')",
    "country": "string (ISO 3166-1, default 'IT')"
  }
}
```

**Output Schema:**
```json
{
  "channels": [
    {
      "channel_id": "string",
      "channel_name": "string",
      "subscriber_count": "integer",
      "video_count": "integer",
      "view_count": "integer",
      "published_at": "datetime",
      "thumbnail_url": "string",
      "description": "string"
    }
  ],
  "total_results": "integer",
  "api_units_used": "integer"
}
```

**Implementation:**
```python
import requests
from typing import Dict, List, Optional

class YouTubeAPI:
    BASE_URL = "https://www.googleapis.com/youtube/v3"
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.units_used = 0
    
    def search_channels(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict] = None
    ) -> Dict:
        """Cerca canali YouTube con filtri."""
        if filters is None:
            filters = {}
        
        # Step 1: Search for channels
        search_url = f"{self.BASE_URL}/search"
        search_params = {
            "part": "snippet",
            "q": query,
            "type": "channel",
            "maxResults": min(max_results, 50),
            "key": self.api_key,
            "relevanceLanguage": filters.get("language", "it"),
            "regionCode": filters.get("country", "IT")
        }
        
        search_response = requests.get(search_url, params=search_params)
        search_data = search_response.json()
        self.units_used += 100  # Search costs 100 units
        
        if "error" in search_data:
            raise Exception(f"YouTube API error: {search_data['error']['message']}")
        
        # Step 2: Get channel statistics
        channel_ids = [item["id"]["channelId"] for item in search_data.get("items", [])]
        
        if not channel_ids:
            return {"channels": [], "total_results": 0, "api_units_used": self.units_used}
        
        channels_url = f"{self.BASE_URL}/channels"
        channels_params = {
            "part": "snippet,statistics",
            "id": ",".join(channel_ids),
            "key": self.api_key
        }
        
        channels_response = requests.get(channels_url, params=channels_params)
        channels_data = channels_response.json()
        self.units_used += 1  # Channels costs 1 unit
        
        # Filter by subscriber count
        subscriber_min = filters.get("subscriber_min", 0)
        subscriber_max = filters.get("subscriber_max", float("inf"))
        
        channels = []
        for item in channels_data.get("items", []):
            stats = item["statistics"]
            subscriber_count = int(stats.get("subscriberCount", 0))
            
            if subscriber_min <= subscriber_count <= subscriber_max:
                channels.append({
                    "channel_id": item["id"],
                    "channel_name": item["snippet"]["title"],
                    "subscriber_count": subscriber_count,
                    "video_count": int(stats.get("videoCount", 0)),
                    "view_count": int(stats.get("viewCount", 0)),
                    "published_at": item["snippet"]["publishedAt"],
                    "thumbnail_url": item["snippet"]["thumbnails"]["default"]["url"],
                    "description": item["snippet"]["description"]
                })
        
        return {
            "channels": channels,
            "total_results": len(channels),
            "api_units_used": self.units_used
        }
```

**Example Usage:**
```python
api = YouTubeAPI(api_key="YOUR_API_KEY")
result = api.search_channels(
    query="Claude Code",
    max_results=10,
    filters={"subscriber_min": 1000, "language": "it"}
)
print(f"Trovati {result['total_results']} canali")
print(f"API units usate: {result['api_units_used']}")
```

---

## Tool 2: youtube_api_get_channel_videos

**Purpose:** Ottenere i video più popolari di un canale con statistiche dettagliate.

**Input Schema:**
```json
{
  "channel_id": "string",
  "max_results": "integer (1-50, default 5)",
  "order": "string (viewCount|date|relevance, default 'viewCount')"
}
```

**Output Schema:**
```json
{
  "videos": [
    {
      "video_id": "string",
      "title": "string",
      "description": "string",
      "published_at": "datetime",
      "duration": "string (ISO 8601)",
      "view_count": "integer",
      "like_count": "integer",
      "comment_count": "integer",
      "thumbnail_url": "string",
      "tags": ["string"]
    }
  ],
  "total_results": "integer",
  "api_units_used": "integer"
}
```

**Implementation:**
```python
def get_channel_videos(
    self,
    channel_id: str,
    max_results: int = 5,
    order: str = "viewCount"
) -> Dict:
    """Ottiene i video più popolari di un canale."""
    
    # Step 1: Get uploads playlist ID
    channel_url = f"{self.BASE_URL}/channels"
    channel_params = {
        "part": "contentDetails",
        "id": channel_id,
        "key": self.api_key
    }
    
    channel_response = requests.get(channel_url, params=channel_params)
    channel_data = channel_response.json()
    self.units_used += 1
    
    if not channel_data.get("items"):
        return {"videos": [], "total_results": 0, "api_units_used": self.units_used}
    
    uploads_playlist_id = channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    
    # Step 2: Get videos from uploads playlist
    playlist_url = f"{self.BASE_URL}/playlistItems"
    playlist_params = {
        "part": "snippet",
        "playlistId": uploads_playlist_id,
        "maxResults": min(max_results, 50),
        "key": self.api_key
    }
    
    playlist_response = requests.get(playlist_url, params=playlist_params)
    playlist_data = playlist_response.json()
    self.units_used += 1
    
    video_ids = [item["snippet"]["resourceId"]["videoId"] for item in playlist_data.get("items", [])]
    
    if not video_ids:
        return {"videos": [], "total_results": 0, "api_units_used": self.units_used}
    
    # Step 3: Get video statistics
    videos_url = f"{self.BASE_URL}/videos"
    videos_params = {
        "part": "snippet,statistics,contentDetails",
        "id": ",".join(video_ids),
        "key": self.api_key
    }
    
    videos_response = requests.get(videos_url, params=videos_params)
    videos_data = videos_response.json()
    self.units_used += 1
    
    # Sort by order
    videos = []
    for item in videos_data.get("items", []):
        stats = item["statistics"]
        videos.append({
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "published_at": item["snippet"]["publishedAt"],
            "duration": item["contentDetails"]["duration"],
            "view_count": int(stats.get("viewCount", 0)),
            "like_count": int(stats.get("likeCount", 0)),
            "comment_count": int(stats.get("commentCount", 0)),
            "thumbnail_url": item["snippet"]["thumbnails"]["high"]["url"],
            "tags": item["snippet"].get("tags", [])
        })
    
    # Sort
    if order == "viewCount":
        videos.sort(key=lambda x: x["view_count"], reverse=True)
    elif order == "date":
        videos.sort(key=lambda x: x["published_at"], reverse=True)
    
    return {
        "videos": videos[:max_results],
        "total_results": len(videos),
        "api_units_used": self.units_used
    }
```

**Example Usage:**
```python
api = YouTubeAPI(api_key="YOUR_API_KEY")
videos = api.get_channel_videos(
    channel_id="UCxxxxxxxxxxxxxxxxxxxx",
    max_results=5,
    order="viewCount"
)
for video in videos["videos"]:
    print(f"{video['title']}: {video['view_count']} views")
```

---

## Tool 3: memory_manager_checkpoint

**Purpose:** Creare checkpoint in memory/youtube/checkpoints/ per tracciare progresso.

**Input Schema:**
```json
{
  "id": "string (unique identifier)",
  "description": "string",
  "input_data": "object (optional)",
  "output_data": "object (optional)",
  "status": "string (start|progress|complete|error)"
}
```

**Output Schema:**
```json
{
  "checkpoint_path": "string (file path)",
  "timestamp": "datetime",
  "success": "boolean"
}
```

**Implementation:**
```python
import json
from datetime import datetime
from pathlib import Path

class MemoryManager:
    def __init__(self, base_path: str = "memory/youtube"):
        self.base_path = Path(base_path)
        self.checkpoints_path = self.base_path / "checkpoints"
        self.checkpoints_path.mkdir(parents=True, exist_ok=True)
    
    def create_checkpoint(
        self,
        id: str,
        description: str,
        input_data: Optional[Dict] = None,
        output_data: Optional[Dict] = None,
        status: str = "progress"
    ) -> Dict:
        """Crea un checkpoint nella memoria."""
        
        timestamp = datetime.now().isoformat()
        checkpoint_file = self.checkpoints_path / f"CP-{id}.md"
        
        content = f"""# Checkpoint: {id}

**Timestamp:** {timestamp}  
**Description:** {description}  
**Status:** {status}

## Input Data
```json
{json.dumps(input_data or {}, indent=2)}
```

## Output Data
```json
{json.dumps(output_data or {}, indent=2)}
```

---
*Created by yt-competitor-scout*
"""
        
        checkpoint_file.write_text(content, encoding="utf-8")
        
        # Update MEMORY-INDEX.md
        self._update_index(id, description, timestamp)
        
        return {
            "checkpoint_path": str(checkpoint_file),
            "timestamp": timestamp,
            "success": True
        }
    
    def _update_index(self, id: str, description: str, timestamp: str):
        """Aggiorna MEMORY-INDEX.md con nuovo checkpoint."""
        index_file = self.base_path / "MEMORY-INDEX.md"
        
        if not index_file.exists():
            index_file.write_text("# MEMORY-INDEX.md\n\n## Checkpoints\n", encoding="utf-8")
        
        content = index_file.read_text(encoding="utf-8")
        
        # Add new checkpoint entry if not exists
        checkpoint_entry = f"- [{id}] {timestamp}: {description}\n"
        if checkpoint_entry not in content:
            content += checkpoint_entry
            index_file.write_text(content, encoding="utf-8")
```

**Example Usage:**
```python
memory = MemoryManager(base_path="memory/youtube")
checkpoint = memory.create_checkpoint(
    id="yt-competitor-scout-start",
    description="Inizio analisi competitor per nicchia: Claude Code",
    input_data={"nicchia": "Claude Code", "canali": 10},
    status="start"
)
print(f"Checkpoint creato: {checkpoint['checkpoint_path']}")
```

---

## Tool 4: competitor_report_generator

**Purpose:** Generare report strutturato sull'analisi competitor.

**Input Schema:**
```json
{
  "nicchia": "string",
  "channels_data": "array of channel objects",
  "gaps": "array of gap strings",
  "best_practices": "array of practice strings",
  "opportunities": "array of opportunity strings"
}
```

**Output Schema:**
```json
{
  "report": {
    "nicchia": "string",
    "data_analisi": "datetime",
    "competitor_analyzed": "integer",
    "competitor": "array",
    "gap_mercato": "array",
    "best_practices": "array",
    "opportunita": "array",
    "recommendations": "array"
  },
  "report_path": "string"
}
```

**Implementation:**
```python
def generate_competitor_report(
    self,
    nicchia: str,
    channels_data: List[Dict],
    gaps: List[str],
    best_practices: List[str],
    opportunities: List[str]
) -> Dict:
    """Genera report strutturato sull'analisi competitor."""
    
    report = {
        "nicchia": nicchia,
        "data_analisi": datetime.now().isoformat(),
        "competitor_analyzed": len(channels_data),
        "competitor": channels_data,
        "gap_mercato": gaps,
        "best_practices": best_practices,
        "opportunita": opportunities,
        "recommendations": self._generate_recommendations(gaps, opportunities)
    }
    
    # Save report
    report_path = self.base_path / f"knowledge/competitors/{nicchia}_{datetime.now().strftime('%Y%m%d')}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    
    return {
        "report": report,
        "report_path": str(report_path)
    }

def _generate_recommendations(self, gaps: List[str], opportunities: List[str]) -> List[str]:
    """Genera raccomandazioni basate su gap e opportunità."""
    recommendations = []
    
    for gap in gaps:
        recommendations.append(f"Creare contenuto su: {gap}")
    
    for opp in opportunities:
        recommendations.append(f"Sfruttare opportunità: {opp}")
    
    return recommendations
```

---

## Dependencies

**Required Packages:**
```bash
pip install requests python-dotenv
```

**Environment Variables:**
```bash
# .env
YOUTUBE_API_KEY=your_api_key_here
```

**Rate Limits:**
- YouTube Data API: 10,000 units/day
- Cost per search: 100 units
- Cost per channel: 1 unit
- Cost per video: 1 unit

---

## Testing

**Test Cases:**
```python
def test_search_channels():
    api = YouTubeAPI(api_key="test_key")
    result = api.search_channels(query="test", max_results=5)
    assert "channels" in result
    assert "api_units_used" in result

def test_get_channel_videos():
    api = YouTubeAPI(api_key="test_key")
    result = api.get_channel_videos(channel_id="test_id", max_results=5)
    assert "videos" in result
    assert "api_units_used" in result

def test_create_checkpoint():
    memory = MemoryManager()
    result = memory.create_checkpoint(id="test", description="test")
    assert result["success"] == True
```

---

**Version:** 1.0  
**Created:** 2026-07-20  
**Owner:** Gael  
**Supervision:** Max
