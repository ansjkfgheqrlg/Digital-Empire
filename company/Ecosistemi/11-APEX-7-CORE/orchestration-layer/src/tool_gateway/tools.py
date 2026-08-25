from __future__ import annotations

import hashlib
import os
import tempfile
from pathlib import Path
from typing import Any


class PathPolicyError(PermissionError):
    pass


def _bounded_path(root: Path, relative: str, *, must_exist: bool) -> Path:
    if not relative or Path(relative).is_absolute():
        raise PathPolicyError("Path must be a non-empty relative path")
    base = root.resolve(strict=True)
    candidate = base / relative
    resolved = candidate.resolve(strict=must_exist)
    if not resolved.is_relative_to(base):
        raise PathPolicyError("Path escapes the granted workspace")
    return resolved


class RepositoryReadTool:
    def __init__(self, repository_root: Path, max_bytes: int = 1_048_576):
        self.repository_root = repository_root
        self.max_bytes = max_bytes

    async def execute(self, arguments: dict[str, Any], constraints: dict[str, Any]) -> dict:
        path = _bounded_path(self.repository_root, str(arguments.get("path", "")), must_exist=True)
        if not path.is_file():
            raise PathPolicyError("Only regular files can be read")
        allowed_prefix = constraints.get("path_prefix")
        if allowed_prefix and not path.relative_to(self.repository_root.resolve()).as_posix().startswith(
            str(allowed_prefix)
        ):
            raise PathPolicyError("Read path is outside the grant prefix")
        size = path.stat().st_size
        limit = min(int(constraints.get("max_bytes", self.max_bytes)), self.max_bytes)
        if size > limit:
            raise PathPolicyError("File exceeds the grant size limit")
        data = path.read_bytes()
        return {
            "path": path.relative_to(self.repository_root.resolve()).as_posix(),
            "size": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "content": data.decode("utf-8").replace("\r\n", "\n"),
        }


class ArtifactWriteTool:
    def __init__(self, artifact_root: Path, max_bytes: int = 1_048_576):
        self.artifact_root = artifact_root
        self.max_bytes = max_bytes
        self.artifact_root.mkdir(parents=True, exist_ok=True)

    async def execute(self, arguments: dict[str, Any], constraints: dict[str, Any]) -> dict:
        relative = str(arguments.get("path", ""))
        content = arguments.get("content")
        if not isinstance(content, str):
            raise PathPolicyError("Artifact content must be text")
        data = content.encode("utf-8")
        limit = min(int(constraints.get("max_bytes", self.max_bytes)), self.max_bytes)
        if len(data) > limit:
            raise PathPolicyError("Artifact exceeds the grant size limit")
        required_prefix = str(constraints.get("path_prefix", "adr/"))
        if not relative.startswith(required_prefix):
            raise PathPolicyError("Artifact path is outside the grant prefix")

        base = self.artifact_root.resolve(strict=True)
        target = _bounded_path(base, relative, must_exist=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.parent.resolve().is_relative_to(base):
            raise PathPolicyError("Artifact parent escapes the store")
        digest = hashlib.sha256(data).hexdigest()
        if target.exists():
            if target.is_symlink() or target.read_bytes() != data:
                raise PathPolicyError("Immutable artifact key already exists with different content")
            return {"path": relative, "size": len(data), "sha256": digest, "idempotent": True}

        descriptor, temporary_name = tempfile.mkstemp(prefix=".ocp-", dir=target.parent)
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            try:
                os.link(temporary, target)
            except FileExistsError:
                if target.is_symlink() or target.read_bytes() != data:
                    raise PathPolicyError("Concurrent immutable artifact conflict")
            return {"path": relative, "size": len(data), "sha256": digest, "idempotent": False}
        finally:
            temporary.unlink(missing_ok=True)
