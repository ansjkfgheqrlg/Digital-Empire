#!/usr/bin/env python3
"""Minimal, fail-closed Instagram Graph API carousel adapter.

No token is read from tracked files and no request is made unless ``publish``
is called explicitly. The adapter expects already-hosted HTTPS slide URLs;
Instagram's container API cannot consume local filesystem paths.
"""
from __future__ import annotations

import hashlib
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class MetaConfig:
    ig_user_id: str
    access_token: str
    graph_version: str = "v23.0"
    graph_base: str = "https://graph.facebook.com"

    @classmethod
    def from_env(cls) -> "MetaConfig":
        user = os.getenv("META_IG_USER_ID", "").strip()
        token = os.getenv("META_ACCESS_TOKEN", "").strip()
        version = os.getenv("META_GRAPH_VERSION", "v23.0").strip()
        if not user or not token:
            raise RuntimeError("META_IG_USER_ID e META_ACCESS_TOKEN devono essere configurati solo nell'ambiente")
        if not version or "/" in version or "?" in version:
            raise RuntimeError("META_GRAPH_VERSION non valido")
        return cls(user, token, version)


class MetaApiError(RuntimeError):
    pass


def _key(urls: list[str], caption: str) -> str:
    value = json.dumps({"urls": urls, "caption": caption}, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _https_urls(urls: list[str]) -> None:
    if not 2 <= len(urls) <= 10:
        raise ValueError("un carousel Instagram richiede da 2 a 10 immagini")
    for url in urls:
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError(f"asset non valido: serve un URL HTTPS pubblico ({url!r})")


def _post(config: MetaConfig, endpoint: str, fields: dict[str, str]) -> dict[str, Any]:
    url = f"{config.graph_base.rstrip('/')}/{config.graph_version}/{endpoint.lstrip('/')}"
    payload = dict(fields)
    payload["access_token"] = config.access_token
    request = urllib.request.Request(
        url,
        data=urllib.parse.urlencode(payload).encode("utf-8"),
        headers={"Accept": "application/json", "User-Agent": "DigitalEmpire-S4/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        # Non includere mai token o query string nei messaggi di errore.
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise MetaApiError(f"Meta API HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise MetaApiError(f"Meta API non raggiungibile: {exc.reason if hasattr(exc, 'reason') else exc}") from exc
    if not isinstance(body, dict) or body.get("error"):
        raise MetaApiError(f"risposta Meta API non valida: {body!r}")
    return body


def publish_carousel(config: MetaConfig, image_urls: list[str], caption: str, state_file: Path) -> str:
    """Create, publish and persist one carousel, idempotently.

    State is written only after the parent publish call returns an Instagram
    media id. Re-running the same content therefore cannot create duplicates.
    """
    _https_urls(image_urls)
    caption = caption.strip()
    if not caption:
        raise ValueError("caption vuota")
    content_key = _key(image_urls, caption)
    state: dict[str, Any] = {}
    if state_file.exists():
        try:
            state = json.loads(state_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"state Meta corrotto: {state_file}") from exc
    previous = state.get(content_key)
    if isinstance(previous, dict) and previous.get("status") == "published":
        return str(previous["media_id"])

    children: list[str] = []
    for image_url in image_urls:
        response = _post(config, config.ig_user_id, {
            "image_url": image_url,
            "is_carousel_item": "true",
        })
        creation_id = response.get("id")
        if not creation_id:
            raise MetaApiError(f"container figlio senza id: {response!r}")
        children.append(str(creation_id))

    parent = _post(config, config.ig_user_id, {
        "media_type": "CAROUSEL",
        "children": ",".join(children),
        "caption": caption,
    })
    parent_id = parent.get("id")
    if not parent_id:
        raise MetaApiError(f"container padre senza id: {parent!r}")
    published = _post(config, f"{config.ig_user_id}/media_publish", {"creation_id": str(parent_id)})
    media_id = published.get("id")
    if not media_id:
        raise MetaApiError(f"pubblicazione senza media id: {published!r}")

    state[content_key] = {"status": "published", "media_id": str(media_id), "children": children}
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return str(media_id)
