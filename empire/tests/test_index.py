"""
EMPIRE — test di empire.index (lotto G-A, Gael).

Owner: Gael · Controllore: Claude · Origine: FORGE (CP-20260722)
"""
from __future__ import annotations

import unittest

from empire import index as idx


class TestBuildIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = idx.build_index()

    def test_all_kinds_present(self):
        for kind in ("agents", "departments", "ecosystems", "workflows", "skills"):
            self.assertIn(kind, self.data)

    def test_agents_over_200(self):
        self.assertGreater(len(self.data["agents"]), 200)

    def test_cache_files_written(self):
        self.assertTrue(idx.INDEX_PATH.exists())
        self.assertTrue(idx.META_PATH.exists())

    def test_rebuild_twice_same_counts_no_duplicates(self):
        first = {k: len(v) for k, v in idx.build_index().items()}
        second = {k: len(v) for k, v in idx.build_index().items()}
        self.assertEqual(first, second)


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx.build_index()

    def test_find_watchdog(self):
        results = idx.search("watchdog")
        ids = [r.get("id") for r in results]
        self.assertIn("ops-watchdog", ids)

    def test_find_restricted_to_kind(self):
        results = idx.search("watchdog", kind="agents")
        self.assertTrue(all(r["kind"] == "agents" for r in results))

    def test_empty_query_returns_empty(self):
        self.assertEqual(idx.search(""), [])

    def test_search_is_case_insensitive(self):
        lower = idx.search("watchdog")
        upper = idx.search("WATCHDOG")
        self.assertEqual({r["id"] for r in lower}, {r["id"] for r in upper})


class TestStats(unittest.TestCase):
    def test_stats_counts_match_index(self):
        data = idx.load_index()
        st = idx.stats()
        self.assertEqual(st["counts"]["agents"], len(data["agents"]))

    def test_agents_by_ecosystem_sums_to_total_known(self):
        st = idx.stats()
        total = sum(st["agents_by_ecosystem"].values())
        self.assertEqual(total, st["counts"]["agents"])


if __name__ == "__main__":
    unittest.main()
