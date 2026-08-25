from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError
from referencing import Registry, Resource


class ContractError(ValueError):
    pass


class ContractRegistry:
    """Validates external payloads against versioned JSON Schema sources of truth."""

    def __init__(self, root: Path):
        self.schema_dir = root / "contracts" / "schemas" / "v1"

    def names(self) -> tuple[str, ...]:
        return tuple(path.stem for path in sorted(self.schema_dir.glob("*.json")))

    def schema(self, name: str) -> dict[str, Any]:
        path = (self.schema_dir / f"{name}.json").resolve()
        if self.schema_dir.resolve() not in path.parents:
            raise ContractError("Schema path escapes registry")
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            raise ContractError(f"Invalid or missing schema: {name}") from exc
        Draft202012Validator.check_schema(schema)
        return schema

    def validate(self, name: str, payload: dict[str, Any]) -> None:
        schema = self.schema(name)
        registry = Registry()
        for path in sorted(self.schema_dir.glob("*.json")):
            candidate = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(candidate)
            if "$id" in candidate:
                registry = registry.with_resource(
                    candidate["$id"], Resource.from_contents(candidate)
                )
        validator = Draft202012Validator(schema, registry=registry)
        errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.path))
        if errors:
            detail = "; ".join(self._format(error) for error in errors[:5])
            raise ContractError(f"{name} contract rejected: {detail}")

    @staticmethod
    def _format(error: ValidationError) -> str:
        location = ".".join(str(value) for value in error.absolute_path) or "$"
        return f"{location}: {error.message}"
