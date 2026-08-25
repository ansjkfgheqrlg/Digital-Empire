from __future__ import annotations

import gzip
import hashlib
import io
import json
import tarfile
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = [
    "README.md", "pyproject.toml", "alembic.ini", "src", "contracts", "policies",
    "prompts", "skills", "migrations", "operations", "privacy", "deploy",
    "builder_swarm/agents.yaml", "builder_swarm/workflow.yaml", "builder_swarm/prompts",
    "builder_swarm/gates/architecture.yaml", "builder_swarm/gates/implementation.yaml",
    "builder_swarm/gates/release.yaml", "memory_store/plans", "memory_store/index",
    "plans/level-07-final-production-blueprint.md", "release/rings.yaml", "release/version.json",
    "scripts/bootstrap_local_operator.py", "scripts/local_operator_client.py", "docs/api/openapi.json",
]
FORBIDDEN_PARTS = {".env", "node_modules", "__pycache__", ".git", "dist", "sandboxes"}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files() -> list[Path]:
    result = []
    for relative in INCLUDE:
        path = ROOT / relative
        candidates = [path] if path.is_file() else path.rglob("*")
        for candidate in candidates:
            if not candidate.is_file():
                continue
            rel = candidate.relative_to(ROOT)
            if any(part in FORBIDDEN_PARTS for part in rel.parts):
                continue
            if candidate.suffix.casefold() in FORBIDDEN_SUFFIXES:
                raise RuntimeError(f"Forbidden key material in package: {rel}")
            result.append(candidate)
    return sorted(set(result), key=lambda path: path.as_posix())


def main() -> int:
    target_dir = ROOT / "release" / "candidate"
    target_dir.mkdir(parents=True, exist_ok=True)
    package_files = files()
    version = json.loads((ROOT / "release/version.json").read_text(encoding="utf-8"))
    manifest = {
        "release_id": version["release_id"],
        "release_type": version["release_type"],
        "created_at": version["created_at"],
        "prr_required_for_production": "GO",
        "current_prr": "NO_GO",
        "ruflo_execution": False,
        "r2_enabled": False,
        "r3_enabled": False,
        "files": [
            {"path": str(path.relative_to(ROOT)), "sha256": sha(path), "size": path.stat().st_size}
            for path in package_files
        ],
    }
    manifest_path = target_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    package_files.append(manifest_path)

    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode="w", format=tarfile.PAX_FORMAT) as archive:
        for path in sorted(package_files, key=lambda item: item.as_posix()):
            relative = path.relative_to(ROOT)
            info = archive.gettarinfo(str(path), arcname=f"orchestration-layer/{relative}")
            info.mtime = 0
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            with path.open("rb") as stream:
                archive.addfile(info, stream)
    package_path = target_dir / "ocp-0.1.0-pilot.tar.gz"
    with package_path.open("wb") as output:
        with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as compressed:
            compressed.write(raw.getvalue())
    digest = sha(package_path)
    (target_dir / "SHA256SUMS").write_text(f"{digest}  {package_path.name}\n")
    print(json.dumps({"package": str(package_path), "files": len(package_files), "size": package_path.stat().st_size, "sha256": digest}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
