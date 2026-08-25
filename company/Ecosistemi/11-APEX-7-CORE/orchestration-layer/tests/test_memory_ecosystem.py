from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from orchestrator.memory import (
    CheckpointWriter,
    KnowledgeBase,
    RulesEngine,
)


class MemoryEcosystemTests(unittest.TestCase):
    def test_checkpoint_writer_and_retrieval(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            writer = CheckpointWriter(Path(tmpdir))
            rec = writer.write_checkpoint(
                checkpoint_id="CP-TEST-001",
                workflow_id="wf-123",
                tenant_id="tenant-alpha",
                workflow_type="repository_adr",
                status="COMPLETED",
                event_count=8,
                context={"artifact": "adr/001.md"},
                summary="Sample completed workflow",
            )
            self.assertEqual(rec.checkpoint_id, "CP-TEST-001")
            self.assertTrue(rec.data_hash.startswith("sha256:"))

            fetched = writer.get_checkpoint("CP-TEST-001")
            self.assertIsNotNone(fetched)
            self.assertEqual(fetched.workflow_id, "wf-123")
            self.assertEqual(writer.list_checkpoints(), ["CP-TEST-001"])

    def test_rules_engine_loads_and_evaluates(self):
        root = Path(__file__).resolve().parent.parent
        rules_dir = root / "memory_store" / "rules"
        engine = RulesEngine(rules_dir)
        rules = engine.list_rules()
        self.assertGreaterEqual(len(rules), 6)

        # Context evaluation
        valid_ctx = {
            "workflow_id": "wf-1",
            "is_write": True,
            "idempotency_key": "key-123",
            "risk": "R1",
        }
        res = engine.evaluate_context(valid_ctx)
        self.assertTrue(all(r.passed for r in res))

        # Invalid context (missing idempotency on write)
        invalid_ctx = {
            "workflow_id": "wf-1",
            "is_write": True,
            "idempotency_key": None,
            "risk": "R1",
        }
        res2 = engine.evaluate_context(invalid_ctx)
        self.assertTrue(any(not r.passed and r.rule_id == "R-003" for r in res2))

    def test_knowledge_base_search(self):
        root = Path(__file__).resolve().parent.parent
        memory_dir = root / "memory_store"
        kb = KnowledgeBase(memory_dir)
        matches = kb.search("PostgreSQL")
        self.assertGreaterEqual(len(matches), 1)
        self.assertEqual(matches[0].entry_id, "R-003")


if __name__ == "__main__":
    unittest.main()
