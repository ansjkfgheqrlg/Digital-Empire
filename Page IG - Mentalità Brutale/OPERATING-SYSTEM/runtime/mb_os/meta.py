from __future__ import annotations

import json
import time
from typing import Any, Protocol
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .config import Settings


class MetaApiError(RuntimeError):
    pass


class Transport(Protocol):
    def request_json(self, method: str, url: str, *, params: dict | None = None,
                     data: dict | None = None, headers: dict | None = None,
                     timeout: int = 45) -> dict: ...


class UrlLibTransport:
    def request_json(self, method: str, url: str, *, params: dict | None = None,
                     data: dict | None = None, headers: dict | None = None,
                     timeout: int = 45) -> dict:
        if params:
            url = f"{url}?{urlencode(params, doseq=True)}"
        body = None
        final_headers = {"Accept": "application/json", **(headers or {})}
        if data is not None:
            body = json.dumps(data).encode("utf-8")
            final_headers["Content-Type"] = "application/json"
        request = Request(url, data=body, headers=final_headers, method=method.upper())
        try:
            with urlopen(request, timeout=timeout) as response:
                payload = response.read().decode("utf-8")
        except HTTPError as exc:
            payload = exc.read().decode("utf-8", errors="replace")
            raise MetaApiError(f"Meta HTTP {exc.code}: {_safe_error(payload)}") from exc
        except URLError as exc:
            raise MetaApiError(f"Meta network error: {exc.reason}") from exc
        try:
            value = json.loads(payload) if payload else {}
        except json.JSONDecodeError as exc:
            raise MetaApiError("Meta ha restituito JSON non valido") from exc
        if isinstance(value, dict) and value.get("error"):
            raise MetaApiError(f"Meta API error: {_safe_error(json.dumps(value['error']))}")
        return value


def _safe_error(payload: str) -> str:
    """Return useful API errors without ever reflecting token-like fields."""
    try:
        value = json.loads(payload)
        if isinstance(value, dict):
            error = value.get("error", value)
            if isinstance(error, dict):
                keep = {key: error.get(key) for key in ("message", "type", "code", "error_subcode") if key in error}
                return json.dumps(keep, ensure_ascii=False)
    except json.JSONDecodeError:
        pass
    return payload[:300].replace("access_token", "[redacted]")


class MetaClient:
    def __init__(self, settings: Settings, transport: Transport | None = None):
        self.settings = settings
        self.transport = transport or UrlLibTransport()

    def _headers(self) -> dict[str, str]:
        if not self.settings.access_token:
            raise MetaApiError("MB_IG_ACCESS_TOKEN mancante")
        return {"Authorization": f"Bearer {self.settings.access_token}"}

    def _url(self, path: str) -> str:
        return f"{self.settings.graph_base}/{path.lstrip('/')}"

    def get(self, path: str, params: dict | None = None) -> dict:
        return self.transport.request_json(
            "GET", self._url(path), params=params, headers=self._headers(),
            timeout=self.settings.request_timeout_seconds,
        )

    def post(self, path: str, data: dict) -> dict:
        return self.transport.request_json(
            "POST", self._url(path), data=data, headers=self._headers(),
            timeout=self.settings.request_timeout_seconds,
        )

    def account_health(self) -> dict:
        response = self.get("me", {"fields": "user_id,username,account_type,media_count"})
        data = response.get("data") if isinstance(response, dict) else None
        if isinstance(data, list) and data and isinstance(data[0], dict):
            return data[0]
        return response

    def publishing_limit(self, ig_user_id: str) -> dict:
        return self.get(f"{ig_user_id}/content_publishing_limit")

    def create_image_container(self, ig_user_id: str, image_url: str, *, caption: str = "",
                               alt_text: str = "", is_carousel_item: bool = False) -> str:
        data: dict[str, Any] = {"image_url": image_url}
        if caption:
            data["caption"] = caption
        if alt_text:
            data["alt_text"] = alt_text
        if is_carousel_item:
            data["is_carousel_item"] = True
        return str(self.post(f"{ig_user_id}/media", data)["id"])

    def create_video_container(self, ig_user_id: str, video_url: str, *, caption: str = "",
                               reel: bool = False, is_carousel_item: bool = False) -> str:
        data: dict[str, Any] = {
            "video_url": video_url,
            "media_type": "REELS" if reel else "VIDEO",
        }
        if caption:
            data["caption"] = caption
        if is_carousel_item:
            data["is_carousel_item"] = True
        if reel:
            data["share_to_feed"] = True
        return str(self.post(f"{ig_user_id}/media", data)["id"])

    def create_carousel_container(self, ig_user_id: str, children: list[str], caption: str) -> str:
        return str(self.post(f"{ig_user_id}/media", {
            "media_type": "CAROUSEL",
            "children": ",".join(children),
            "caption": caption,
        })["id"])

    def container_status(self, container_id: str) -> str:
        response = self.get(container_id, {"fields": "status_code,status"})
        return str(response.get("status_code") or response.get("status") or "UNKNOWN").upper()

    def wait_until_ready(self, container_id: str, *, timeout_seconds: int = 300, poll_seconds: int = 5) -> None:
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            status = self.container_status(container_id)
            if status in {"FINISHED", "PUBLISHED"}:
                return
            if status in {"ERROR", "EXPIRED"}:
                raise MetaApiError(f"Container {container_id} in stato {status}")
            time.sleep(poll_seconds)
        raise MetaApiError(f"Timeout attesa container {container_id}")

    def publish_container(self, ig_user_id: str, container_id: str) -> str:
        return str(self.post(f"{ig_user_id}/media_publish", {"creation_id": container_id})["id"])

    def media_details(self, media_id: str) -> dict:
        return self.get(media_id, {"fields": "id,permalink,timestamp,media_type,media_product_type"})

    def media_insights(self, media_id: str, metrics: list[str]) -> dict:
        return self.get(f"{media_id}/insights", {"metric": ",".join(metrics)})
