from __future__ import annotations

import json
import subprocess
import sys
import tarfile
import unittest
from pathlib import Path

import yaml

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from orchestrator.release import ReleaseController, ReleaseRing, RolloutError


class RolloutTests(unittest.TestCase):
    def test_one_ring_at_a_time_and_hard_gate(self) -> None:
        controller = ReleaseController("r1", "NO_GO")
        with self.assertRaises(RolloutError):
            controller.promote(ReleaseRing.SHADOW, hard_gates_pass=True)
        with self.assertRaises(RolloutError):
            controller.promote(ReleaseRing.TEST, hard_gates_pass=False)
        self.assertEqual(ReleaseRing.DEV, controller.ring)

    def test_prr_no_go_blocks_production(self) -> None:
        controller = ReleaseController("r1", "NO_GO")
        for ring in (
            ReleaseRing.TEST, ReleaseRing.SHADOW, ReleaseRing.CANARY_5,
            ReleaseRing.CANARY_25, ReleaseRing.PILOT,
        ):
            controller.promote(ring, hard_gates_pass=True)
        with self.assertRaises(RolloutError):
            controller.promote(ReleaseRing.PROD, hard_gates_pass=True)
        self.assertEqual(ReleaseRing.PILOT, controller.ring)

    def test_rollback_is_terminal(self) -> None:
        controller = ReleaseController("r1", "GO")
        controller.promote(ReleaseRing.TEST, hard_gates_pass=True)
        controller.rollback("test")
        with self.assertRaises(RolloutError):
            controller.promote(ReleaseRing.SHADOW, hard_gates_pass=True)


class PackageTests(unittest.TestCase):
    def test_package_manifest_and_forbidden_material(self) -> None:
        subprocess.run([sys.executable, "scripts/build_pilot_package.py"], cwd=PROJECT, check=True, capture_output=True)
        package = PROJECT / "release/candidate/ocp-0.1.0-pilot.tar.gz"
        manifest = json.loads((PROJECT / "release/candidate/manifest.json").read_text())
        self.assertEqual("NO_GO", manifest["current_prr"])
        self.assertFalse(manifest["ruflo_execution"])
        with tarfile.open(package, "r:gz") as archive:
            names = archive.getnames()
        self.assertFalse(any("node_modules" in name or "__pycache__" in name for name in names))
        self.assertFalse(any(name.endswith((".pem", ".key", ".env")) for name in names))

    def test_package_is_reproducible(self) -> None:
        script = [sys.executable, "scripts/build_pilot_package.py"]
        subprocess.run(script, cwd=PROJECT, check=True, capture_output=True)
        first = (PROJECT / "release/candidate/ocp-0.1.0-pilot.tar.gz").read_bytes()
        subprocess.run(script, cwd=PROJECT, check=True, capture_output=True)
        second = (PROJECT / "release/candidate/ocp-0.1.0-pilot.tar.gz").read_bytes()
        self.assertEqual(first, second)

    def test_compose_and_container_are_nonproduction_hardened(self) -> None:
        compose = yaml.safe_load((PROJECT / "deploy/compose/docker-compose.yml").read_text())
        self.assertEqual(
            {"postgres", "opa", "migrate", "pilot-api", "pilot-worker", "pilot-outbox", "pilot-cli"},
            set(compose["services"]),
        )
        self.assertTrue(compose["services"]["pilot-cli"]["read_only"])
        self.assertTrue(compose["services"]["pilot-api"]["read_only"])
        self.assertEqual("127.0.0.1:8000:8000", compose["services"]["pilot-api"]["ports"][0])
        self.assertIn("no-new-privileges:true", compose["services"]["pilot-cli"]["security_opt"])
        dockerfile = (PROJECT / "deploy/pilot/Dockerfile").read_text()
        self.assertIn("USER 10001:10001", dockerfile)
        self.assertNotIn("COPY . .", dockerfile)


if __name__ == "__main__":
    unittest.main()
