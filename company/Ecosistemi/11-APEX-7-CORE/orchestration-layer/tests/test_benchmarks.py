from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from benchmarks.memory_eval import evaluate_plan_memory
from benchmarks.w9 import percentile, run_w9_benchmark


class MemoryBenchmarkTests(unittest.TestCase):
    def test_memory_targets_and_insufficient_evidence(self) -> None:
        report = evaluate_plan_memory(PROJECT)
        self.assertGreaterEqual(report["recall_at_5"], 0.95)
        self.assertEqual(1.0, report["citation_hash_accuracy"])
        self.assertEqual(1.0, report["unsupported_accuracy"])
        self.assertEqual(0, report["cross_tenant_leakage"])


class BaselineBenchmarkTests(unittest.IsolatedAsyncioTestCase):
    async def test_all_local_hard_gates_pass_and_ruflo_is_blocked(self) -> None:
        report = await run_w9_benchmark(PROJECT)
        self.assertTrue(all(report["hard_gates"].values()))
        self.assertEqual(30, report["local_runtime"]["cases"])
        self.assertEqual(20, report["load"]["completed"])
        self.assertEqual("BLOCKED", report["ruflo_comparison"]["status"])
        self.assertFalse(report["ruflo_comparison"]["fabricated_results"])

    def test_percentile_is_bounded(self) -> None:
        self.assertEqual(1, percentile([1, 2, 3, 4], 0.01))
        self.assertEqual(4, percentile([1, 2, 3, 4], 1.0))


if __name__ == "__main__":
    unittest.main()
