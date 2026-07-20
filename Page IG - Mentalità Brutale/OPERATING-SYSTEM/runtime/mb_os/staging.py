from __future__ import annotations

import hashlib
import shutil
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

from .config import Settings
from .models import ContentManifest, MediaAsset


class StagingError(RuntimeError):
    pass


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class AssetStager:
    """Map local media into a public HTTPS mirror, using content-addressed names."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def plan(self, manifest: ContentManifest) -> list[dict]:
        result = []
        for asset in manifest.media:
            if asset.public_url:
                result.append({"action": "reuse_public_url", "source": asset.public_url, "target": asset.public_url})
            else:
                source = Path(asset.path or "").expanduser().resolve()
                target_ext = self._target_extension(manifest, asset, source)
                result.append({
                    "action": "convert_and_copy" if target_ext != source.suffix.lower() else "copy",
                    "source": str(source),
                    "target_extension": target_ext,
                })
        return result

    def stage_all(self, manifest: ContentManifest) -> list[str]:
        return [self.stage(manifest, asset) for asset in manifest.media]

    def preflight_all(self, urls: list[str]) -> list[dict]:
        return [self.preflight(url) for url in urls]

    def preflight(self, url: str) -> dict:
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise StagingError("Preflight richiede URL HTTPS pubblico")
        request = Request(url, method="HEAD", headers={"User-Agent": "MB-OS/1.0"})
        try:
            with urlopen(request, timeout=self.settings.request_timeout_seconds) as response:
                status = int(response.status)
                content_type = response.headers.get("Content-Type", "")
                length = response.headers.get("Content-Length")
        except HTTPError as exc:
            raise StagingError(f"Media preflight HTTP {exc.code}") from exc
        except URLError as exc:
            raise StagingError(f"Media preflight network error: {exc.reason}") from exc
        if not 200 <= status < 300:
            raise StagingError(f"Media preflight status inatteso: {status}")
        return {"url": url, "status": status, "content_type": content_type, "content_length": length}

    def stage(self, manifest: ContentManifest, asset: MediaAsset) -> str:
        if asset.public_url:
            parsed = urlparse(asset.public_url)
            if parsed.scheme != "https" or not parsed.netloc:
                raise StagingError("public_url deve essere HTTPS")
            return asset.public_url

        if not self.settings.public_media_dir or not self.settings.public_media_base_url:
            raise StagingError("MB_PUBLIC_MEDIA_DIR e MB_PUBLIC_MEDIA_BASE_URL sono obbligatori per asset locali")
        source = Path(asset.path or "").expanduser().resolve()
        if not source.is_file():
            raise StagingError(f"Asset locale assente: {source}")
        target_ext = self._target_extension(manifest, asset, source)
        target_name = f"{_sha256(source)[:24]}{target_ext}"
        target = self.settings.public_media_dir / target_name
        target.parent.mkdir(parents=True, exist_ok=True)

        if target_ext == ".jpg" and source.suffix.lower() not in {".jpg", ".jpeg"}:
            self._convert_to_jpeg(source, target)
        elif not target.exists():
            shutil.copy2(source, target)
        return f"{self.settings.public_media_base_url}/{quote(target_name)}"

    @staticmethod
    def _target_extension(manifest: ContentManifest, asset: MediaAsset, source: Path) -> str:
        if manifest.format == "REEL" or asset.media_type == "VIDEO":
            return source.suffix.lower()
        return ".jpg"

    @staticmethod
    def _convert_to_jpeg(source: Path, target: Path) -> None:
        try:
            from PIL import Image
        except ImportError as exc:
            raise StagingError("Pillow non installato: pip install -r runtime/requirements.txt") from exc
        with Image.open(source) as image:
            rgb = image.convert("RGB")
            rgb.save(target, format="JPEG", quality=92, optimize=True, progressive=True)
