from __future__ import annotations

import json
import statistics
from datetime import datetime, timedelta, timezone
from typing import Any

from .meta import MetaClient
from .state import StateStore

COMMON_METRICS = ["reach", "views", "likes", "comments", "saved", "shares", "total_interactions"]
REEL_METRICS = COMMON_METRICS + ["ig_reels_avg_watch_time", "ig_reels_video_view_total_time", "reels_skip_rate"]


def parse_insights(response: dict) -> dict[str, int | float | None]:
    result: dict[str, int | float | None] = {}
    for item in response.get("data", []):
        name = item.get("name")
        if not name:
            continue
        value: int | float | None = None
        total_value = item.get("total_value")
        if isinstance(total_value, dict) and isinstance(total_value.get("value"), (int, float)):
            value = total_value["value"]
        values = item.get("values")
        if value is None and isinstance(values, list) and values:
            candidate = values[0].get("value") if isinstance(values[0], dict) else None
            if isinstance(candidate, (int, float)):
                value = candidate
        result[str(name)] = value
    return result


def quality_action_rate(metrics: dict[str, Any]) -> float | None:
    reach = metrics.get("reach")
    if not isinstance(reach, (int, float)) or reach <= 0:
        return None
    values = {
        key: value if isinstance(value, (int, float)) else 0
        for key, value in metrics.items()
    }
    weighted = (
        5 * values.get("shares", 0)
        + 4 * values.get("saved", 0)
        + 3 * values.get("comments", 0)
        + values.get("likes", 0)
    )
    return round(weighted / reach * 100, 4)


class AnalyticsService:
    def __init__(self, client: MetaClient, store: StateStore):
        self.client = client
        self.store = store

    def collect(self, content_id: str, media_id: str, media_type: str) -> dict:
        normalized_type = media_type.upper()
        requested = REEL_METRICS if normalized_type == "REEL" else COMMON_METRICS
        response = self.client.media_insights(media_id, requested)
        metrics = parse_insights(response)
        score = quality_action_rate(metrics)
        self.store.record_metrics(content_id, media_id, normalized_type, metrics, score)
        return {
            "content_id": content_id,
            "media_id": media_id,
            "media_type": normalized_type,
            "metrics": metrics,
            "quality_action_rate": score,
            "note": "null indica dato assente/ritardato, non zero",
        }

    def report(self, days: int = 28) -> dict:
        since = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat().replace("+00:00", "Z")
        rows = self.store.metric_rows_since(since)
        scores = [float(row["quality_action_rate"]) for row in rows if row["quality_action_rate"] is not None]
        by_type: dict[str, list[float]] = {}
        for row in rows:
            score = row["quality_action_rate"]
            if score is not None:
                by_type.setdefault(str(row["media_type"]), []).append(float(score))
        return {
            "window_days": days,
            "snapshots": len(rows),
            "overall_median_quality_action_rate": statistics.median(scores) if scores else None,
            "by_media_type": {
                key: {"n": len(values), "median_quality_action_rate": statistics.median(values)}
                for key, values in by_type.items()
            },
            "decision_guard": "Nessun pattern promosso da questo report senza n>=3 e confronto stesso formato.",
        }