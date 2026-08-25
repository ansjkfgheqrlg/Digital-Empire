from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from plan_memory.index import PlanIndex
from plan_memory.manifest import IntegrityError, PlanManifest


class PlanMemoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = PlanIndex.build(PROJECT)

    def test_manifest_has_seven_levels_and_l7_authority(self) -> None:
        manifest = PlanManifest.load(PROJECT)
        self.assertEqual(list(range(1, 8)), [record.level for record in manifest.records])
        approved = [record.level for record in manifest.records if record.is_approved]
        self.assertEqual([7], approved)

    def test_query_returns_citations_and_hashes(self) -> None:
        result = self.index.search("PostgreSQL stato canonico RuFlo executor", limit=3)
        self.assertEqual("EVIDENCE_FOUND", result["status"])
        self.assertTrue(result["results"])
        for hit in result["results"]:
            citation = hit["citation"]
            path = PROJECT / citation["file"]
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(digest, citation["sha256"])
            self.assertGreaterEqual(citation["line_end"], citation["line_start"])

    def test_highest_approved_level_is_authoritative(self) -> None:
        result = self.index.search("architettura definitiva control plane RuFlo", limit=8)
        authoritative = [hit for hit in result["results"] if hit["authoritative"]]
        self.assertTrue(authoritative)
        self.assertTrue(all(hit["citation"]["level"] == 7 for hit in authoritative))

    def test_unknown_query_returns_insufficient_evidence(self) -> None:
        result = self.index.search("xylophonic-quasar-9173")
        self.assertEqual("INSUFFICIENT_EVIDENCE", result["status"])
        self.assertEqual([], result["results"])

    def test_hash_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PROJECT / "plans", root / "plans")
            shutil.copytree(PROJECT / "memory_store" / "plans", root / "memory_store" / "plans")
            target = root / "plans" / "level-07-final-production-blueprint.md"
            target.write_text(target.read_text(encoding="utf-8") + "\ntampered\n", encoding="utf-8")
            with self.assertRaises(IntegrityError):
                PlanManifest.load(root)

    def test_approved_only_never_returns_superseded_plan(self) -> None:
        result = self.index.search("Builder Swarm", limit=8, approved_only=True)
        self.assertEqual("EVIDENCE_FOUND", result["status"])
        self.assertTrue(all(hit["citation"]["status"] == "APPROVED" for hit in result["results"]))


if __name__ == "__main__":
    unittest.main()
