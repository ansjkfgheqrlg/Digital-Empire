from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

OS_ROOT = Path(__file__).resolve().parents[2]
RUNTIME_ROOT = OS_ROOT / "runtime"
DEFAULT_ENV_FILE = OS_ROOT / ".env"


def load_local_env(path: Path = DEFAULT_ENV_FILE) -> None:
    """Load a minimal .env without overriding process environment variables."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


load_local_env()


def _path_env(name: str, default: Path | None = None) -> Path | None:
    value = os.environ.get(name, "").strip()
    if value:
        return Path(value).expanduser().resolve()
    return default


@dataclass(frozen=True)
class Settings:
    api_version: str
    graph_host: str
    access_token: str
    ig_user_id: str
    app_id: str
    app_secret: str
    redirect_uri: str
    public_media_dir: Path | None
    public_media_base_url: str
    state_db: Path
    live_publish_enabled: bool
    request_timeout_seconds: int

    @property
    def graph_base(self) -> str:
        return f"{self.graph_host.rstrip('/')}/{self.api_version}"

    @classmethod
    def from_env(cls) -> "Settings":
        state_default = OS_ROOT / "runtime" / "state" / "mb_os.sqlite"
        return cls(
            api_version=os.environ.get("MB_META_API_VERSION", "v25.0").strip(),
            graph_host=os.environ.get("MB_META_GRAPH_HOST", "https://graph.instagram.com").strip(),
            access_token=os.environ.get("MB_IG_ACCESS_TOKEN", "").strip(),
            ig_user_id=os.environ.get("MB_IG_USER_ID", "").strip(),
            app_id=os.environ.get("MB_INSTAGRAM_APP_ID", "").strip(),
            app_secret=os.environ.get("MB_INSTAGRAM_APP_SECRET", "").strip(),
            redirect_uri=os.environ.get("MB_OAUTH_REDIRECT_URI", "").strip(),
            public_media_dir=_path_env("MB_PUBLIC_MEDIA_DIR"),
            public_media_base_url=os.environ.get("MB_PUBLIC_MEDIA_BASE_URL", "").rstrip("/"),
            state_db=_path_env("MB_STATE_DB", state_default) or state_default,
            live_publish_enabled=os.environ.get("MB_LIVE_PUBLISH_ENABLED", "").strip() == "YES",
            request_timeout_seconds=int(os.environ.get("MB_REQUEST_TIMEOUT_SECONDS", "45")),
        )

    def ensure_local_dirs(self) -> None:
        self.state_db.parent.mkdir(parents=True, exist_ok=True)
        if self.public_media_dir:
            self.public_media_dir.mkdir(parents=True, exist_ok=True)
