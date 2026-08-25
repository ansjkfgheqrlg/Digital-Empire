from __future__ import annotations

import hashlib
import os
import tempfile
from pathlib import Path


class SandboxViolation(PermissionError):
    pass


class BuilderSandbox:
    """Write-only build sandbox; paths cannot escape its work-item root."""

    def __init__(self, base: Path, run_id: str):
        if not run_id or any(
            char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
            for char in run_id
        ):
            raise ValueError("Invalid sandbox run id")
        self.root = (base / run_id).resolve()
        self.root.mkdir(parents=True, exist_ok=False)

    def path(self, relative: str) -> Path:
        if not relative or Path(relative).is_absolute():
            raise SandboxViolation("Sandbox path must be relative")
        target = (self.root / relative).resolve()
        if not target.is_relative_to(self.root):
            raise SandboxViolation("Sandbox path escapes the work-item root")
        return target

    def write_immutable(self, relative: str, content: str) -> dict:
        target = self.path(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        data = content.encode("utf-8")
        digest = hashlib.sha256(data).hexdigest()
        if target.exists():
            if target.is_symlink() or target.read_bytes() != data:
                raise SandboxViolation("Immutable sandbox artifact conflict")
            return {"path": relative, "sha256": digest, "size": len(data), "idempotent": True}
        descriptor, temporary_name = tempfile.mkstemp(prefix=".builder-", dir=target.parent)
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            os.link(temporary, target)
        finally:
            temporary.unlink(missing_ok=True)
        return {"path": relative, "sha256": digest, "size": len(data), "idempotent": False}
