from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


@dataclass(frozen=True)
class SkillDefinition:
    name: str
    version: str
    status: str
    risk: str
    capabilities: tuple[str, ...]
    input_schema: dict[str, Any]
    output_schema: dict[str, Any]


class SkillRegistry:
    def __init__(self, skills_dir: Path):
        self.skills_dir = skills_dir
        self._skills: dict[str, SkillDefinition] = {}
        self.load_skills()

    def load_skills(self) -> None:
        if not self.skills_dir.exists():
            return
        for skill_path in self.skills_dir.iterdir():
            if not skill_path.is_dir():
                continue
            manifest_file = skill_path / "manifest.yaml"
            input_file = skill_path / "schemas" / "input.json"
            output_file = skill_path / "schemas" / "output.json"

            if not (manifest_file.exists() and input_file.exists() and output_file.exists()):
                continue

            manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
            input_schema = json.loads(input_file.read_text(encoding="utf-8"))
            output_schema = json.loads(output_file.read_text(encoding="utf-8"))

            Draft202012Validator.check_schema(input_schema)
            Draft202012Validator.check_schema(output_schema)

            name = manifest["metadata"]["id"]
            self._skills[name] = SkillDefinition(
                name=name,
                version=manifest["metadata"]["version"],
                status=manifest["spec"]["status"],
                risk=manifest["spec"]["riskClass"],
                capabilities=tuple(manifest["spec"].get("capabilities", [])),
                input_schema=input_schema,
                output_schema=output_schema,
            )

    def get(self, skill_name: str) -> SkillDefinition | None:
        return self._skills.get(skill_name)

    def list_skills(self) -> list[str]:
        return sorted(self._skills.keys())
