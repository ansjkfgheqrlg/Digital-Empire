from __future__ import annotations

import json
import os
import secrets
import tempfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .config import DEFAULT_ENV_FILE, Settings

CORE_SCOPES = (
    "instagram_business_basic",
    "instagram_business_content_publish",
    "instagram_business_manage_insights",
)


class AuthError(RuntimeError):
    pass


def authorization_url(settings: Settings, state: str | None = None) -> tuple[str, str]:
    if not settings.app_id or not settings.redirect_uri:
        raise AuthError("MB_INSTAGRAM_APP_ID e MB_OAUTH_REDIRECT_URI sono obbligatori")
    csrf_state = state or secrets.token_urlsafe(32)
    query = urlencode({
        "client_id": settings.app_id,
        "redirect_uri": settings.redirect_uri,
        "response_type": "code",
        "scope": ",".join(CORE_SCOPES),
        "state": csrf_state,
        "force_reauth": "true",
    })
    return f"https://www.instagram.com/oauth/authorize?{query}", csrf_state


def _form_request(url: str, fields: dict[str, str], timeout: int) -> dict:
    boundary = f"----mbos{secrets.token_hex(12)}"
    parts: list[bytes] = []
    for key, value in fields.items():
        parts.extend([
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode(),
            str(value).encode(), b"\r\n",
        ])
    parts.append(f"--{boundary}--\r\n".encode())
    request = Request(url, data=b"".join(parts), method="POST", headers={
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Accept": "application/json",
    })
    try:
        with urlopen(request, timeout=timeout) as response:
            payload = response.read().decode("utf-8")
    except HTTPError as exc:
        raise AuthError(f"OAuth HTTP {exc.code}; controllare code/redirect/app config") from exc
    except URLError as exc:
        raise AuthError(f"OAuth network error: {exc.reason}") from exc
    value = json.loads(payload)
    if not isinstance(value, dict) or not value.get("access_token"):
        raise AuthError("OAuth response senza access_token")
    return value


def _get_json(url: str, params: dict[str, str], timeout: int) -> dict:
    request = Request(f"{url}?{urlencode(params)}", headers={"Accept": "application/json"})
    try:
        with urlopen(request, timeout=timeout) as response:
            value = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise AuthError(f"Token HTTP {exc.code}; il token può essere scaduto o la config errata") from exc
    except URLError as exc:
        raise AuthError(f"Token network error: {exc.reason}") from exc
    if not isinstance(value, dict) or not value.get("access_token"):
        raise AuthError("Token response senza access_token")
    return value


def exchange_code(settings: Settings, code: str) -> dict:
    if not all((settings.app_id, settings.app_secret, settings.redirect_uri)):
        raise AuthError("App ID, App Secret e Redirect URI sono obbligatori")
    short = _form_request("https://api.instagram.com/oauth/access_token", {
        "client_id": settings.app_id,
        "client_secret": settings.app_secret,
        "grant_type": "authorization_code",
        "redirect_uri": settings.redirect_uri,
        "code": code.removesuffix("#_"),
    }, settings.request_timeout_seconds)
    long_lived = _get_json("https://graph.instagram.com/access_token", {
        "grant_type": "ig_exchange_token",
        "client_secret": settings.app_secret,
        "access_token": str(short["access_token"]),
    }, settings.request_timeout_seconds)
    if short.get("user_id"):
        long_lived["user_id"] = short["user_id"]
    return long_lived


def refresh_token(settings: Settings) -> dict:
    if not settings.access_token:
        raise AuthError("MB_IG_ACCESS_TOKEN mancante")
    return _get_json("https://graph.instagram.com/refresh_access_token", {
        "grant_type": "ig_refresh_token",
        "access_token": settings.access_token,
    }, settings.request_timeout_seconds)


def update_dotenv(token: str, user_id: str | None = None, path: Path = DEFAULT_ENV_FILE) -> None:
    """Atomically update local ignored .env and attempt owner-only permissions."""
    existing: list[str] = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    values = {"MB_IG_ACCESS_TOKEN": token}
    if user_id:
        values["MB_IG_USER_ID"] = user_id
    output: list[str] = []
    seen: set[str] = set()
    for line in existing:
        key = line.split("=", 1)[0].strip() if "=" in line and not line.lstrip().startswith("#") else ""
        if key in values:
            output.append(f"{key}={values[key]}")
            seen.add(key)
        else:
            output.append(line)
    for key, value in values.items():
        if key not in seen:
            output.append(f"{key}={value}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=".env.", dir=path.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write("\n".join(output).rstrip() + "\n")
        os.chmod(temp_name, 0o600)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
