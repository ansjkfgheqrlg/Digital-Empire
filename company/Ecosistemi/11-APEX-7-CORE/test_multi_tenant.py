"""
Test isolamento multi-tenant del motore APEX-7-CORE (Fase 1 fusione Ruflo/APEX-7,
piano ADR-010). Verifica che due domini concorrenti (es. youtube, stream-s7-bot)
non condividano stato: file di memoria, decision log SQLite e strategy store
devono restare separati per dominio, mentre domain="default" (carousel-machine,
skill-forge, cold-outreach) continua a scrivere nel path storico invariato.
"""
from __future__ import annotations

import shutil
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from memory.memory_system import APEX7Memory, DATA_DIR  # noqa: E402


class TestMultiTenantIsolation(unittest.TestCase):
    DOMAINS = ["test-youtube", "test-stream-s7-bot"]

    def tearDown(self):
        for domain in self.DOMAINS:
            path = DATA_DIR / domain
            if path.exists():
                shutil.rmtree(path)

    def test_domains_get_separate_directories(self):
        mem_a = APEX7Memory(domain="test-youtube")
        mem_b = APEX7Memory(domain="test-stream-s7-bot")
        self.assertNotEqual(mem_a.data_dir, mem_b.data_dir)
        self.assertTrue(str(mem_a.data_dir).endswith("test-youtube"))
        self.assertTrue(str(mem_b.data_dir).endswith("test-stream-s7-bot"))
        self.assertNotEqual(mem_a.db_path, mem_b.db_path)

    def test_decisions_do_not_cross_domains(self):
        mem_a = APEX7Memory(domain="test-youtube")
        mem_b = APEX7Memory(domain="test-stream-s7-bot")

        mem_a.log_decision("scegli canale Andrea Ciraolo", "SEO fit reale", ["altri 19 canali"], 0.9, "niche-scout")
        mem_b.log_decision("apri posizione SOL/USDC", "segnale RSI reale", ["hold"], 0.8, "trader-agent")

        decisions_a = mem_a.get_recent_decisions(10)
        decisions_b = mem_b.get_recent_decisions(10)

        self.assertEqual(len(decisions_a), 1)
        self.assertEqual(len(decisions_b), 1)
        self.assertIn("Andrea Ciraolo", decisions_a[0][1])
        self.assertIn("SOL/USDC", decisions_b[0][1])

    def test_strategy_store_isolated_per_domain(self):
        mem_a = APEX7Memory(domain="test-youtube")
        mem_b = APEX7Memory(domain="test-stream-s7-bot")

        mem_a.save_strategy("niche-scout-tier", "seleziona canale per tier+viste", ["scouting"], {}, 8.0)
        mem_b.save_strategy("dca-reentry", "rientra a media mobile", ["trading"], {}, 7.5)

        names_a = [s["name"] for s in mem_a.strategy_store]
        names_b = [s["name"] for s in mem_b.strategy_store]

        self.assertIn("niche-scout-tier", names_a)
        self.assertNotIn("dca-reentry", names_a)
        self.assertIn("dca-reentry", names_b)
        self.assertNotIn("niche-scout-tier", names_b)

    def test_default_domain_keeps_historical_path(self):
        mem = APEX7Memory(domain="default")
        self.assertEqual(mem.data_dir, DATA_DIR)
        self.assertEqual(mem.db_path, DATA_DIR / "decision_log.db")


if __name__ == "__main__":
    unittest.main()
