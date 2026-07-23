"""
EMPIRE — test di empire.loader (lotto G-A, Gael).

Owner: Gael · Controllore: Claude · Origine: FORGE (CP-20260722)

Eseguire dalla radice del monorepo:
    python -m pytest empire/tests/test_loader.py -q
    python -m unittest discover -s empire/tests -p "test_*.py"
"""
from __future__ import annotations

import tempfile
import time
import unittest
from pathlib import Path

from empire import loader
from empire.schema import Agent


# ---------------------------------------------------------------- fixtures sintetiche
# I 4 formati realmente osservati campionando il monorepo (vedi docstring di loader.py):
# tabella, blockquote frontmatter+bold, bullet frontmatter, nessun campo esplicito.

_FMT_TABLE = """> Fonte: PIANO-MAESTRO/06 sez. 09

# ops-fake-agent — Agente Finto

## Identità

| Campo | Valore |
|---|---|
| ID | `ops-fake-agent` |
| Ruolo | Watchdog di prova |
| Tier modello | **Haiku** |
| Reparto | L2 STORAGE-ASSETS |
"""

_FMT_FRONTMATTER_BLOCKQUOTE = """---
Type: ENTITY
Status: Active
Created: 2026-06-17
---

# ceo-advisor-fake — Advisor Finto

> **ID:** CEO-FAKE-001 · **Tier:** Sonnet · **Ruolo:** consulente di prova
"""

_FMT_FRONTMATTER_BULLET = """---
Type: TOOL
Status: Active
---

# ISP-FAKE — Ispettore Finto

- **ID**: `isp-fake`
- **Tier**: `opus`
- **Tipo**: coordinator
"""

_FMT_NO_FIELDS = """# AGENTE / RUOLO: FAKE ROLE (Descrizione)
> **Reparto:** 10-MEMORY / 08-INTELLIGENCE

## Funzione Operativa
- Fa cose di prova, senza campo ID esplicito.
"""


class TestLoadFrontmatter(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def _write(self, name: str, content: str) -> Path:
        p = self.dir / name
        p.write_text(content, encoding="utf-8")
        return p

    def test_no_frontmatter_returns_empty_dict_not_crash(self):
        p = self._write("a.md", _FMT_TABLE)
        self.assertEqual(loader.load_frontmatter(p), {})

    def test_frontmatter_parsed(self):
        p = self._write("b.md", _FMT_FRONTMATTER_BLOCKQUOTE)
        fm = loader.load_frontmatter(p)
        self.assertEqual(fm.get("Type"), "ENTITY")
        self.assertEqual(fm.get("Status"), "Active")

    def test_missing_file_returns_empty_dict(self):
        self.assertEqual(loader.load_frontmatter(self.dir / "nope.md"), {})

    def test_unicode_content_does_not_raise(self):
        p = self._write("emoji.md", "# 🧠 Agente\n\n- **ID**: emoji-agent\n")
        loader.load_frontmatter(p)  # non deve sollevare


class TestExtractField(unittest.TestCase):
    def test_table_format(self):
        self.assertEqual(loader._extract_field(_FMT_TABLE, "ID"), "ops-fake-agent")
        self.assertEqual(loader._extract_field(_FMT_TABLE, "Tier modello"), "Haiku")

    def test_blockquote_bold_format(self):
        val = loader._extract_field(_FMT_FRONTMATTER_BLOCKQUOTE, "ID")
        self.assertEqual(val, "CEO-FAKE-001")

    def test_bullet_bold_format(self):
        val = loader._extract_field(_FMT_FRONTMATTER_BULLET, "ID")
        self.assertEqual(val, "isp-fake")

    def test_absent_field_returns_none_not_raise(self):
        self.assertIsNone(loader._extract_field(_FMT_NO_FIELDS, "ID"))

    def test_multiple_labels_first_match_wins(self):
        val = loader._extract_field(_FMT_TABLE, "Tier", "Ruolo")
        self.assertEqual(val, "Watchdog di prova")


class TestIdFromFilename(unittest.TestCase):
    def test_strips_agente_prefix(self):
        p = Path("AGENTE-CLAUDE.md")
        self.assertEqual(loader._id_from_filename(p), "CLAUDE")

    def test_keeps_id_without_known_prefix(self):
        p = Path("INT-A00-int-director.md")
        self.assertEqual(loader._id_from_filename(p), "INT-A00-int-director")


class TestTitleFromContent(unittest.TestCase):
    def test_em_dash_title_split(self):
        title = loader._title_from_content(_FMT_TABLE, fallback="x")
        self.assertEqual(title, "Agente Finto")

    def test_fallback_when_no_heading(self):
        title = loader._title_from_content("nessun heading qui", fallback="fallback-id")
        self.assertEqual(title, "fallback-id")


class TestLoadAgentsOnFixture(unittest.TestCase):
    """load_agents scandisce path reali via empire.paths — qui verifichiamo solo che
    il parsing dei 4 formati campionati non sollevi mai, usando i loader interni
    a livello di singolo file (non l'intera scansione, che è testata sul monorepo
    reale in TestLoadAgentsRealRepo qui sotto)."""

    def test_all_sampled_formats_parse_without_raising(self):
        for content in (_FMT_TABLE, _FMT_FRONTMATTER_BLOCKQUOTE,
                         _FMT_FRONTMATTER_BULLET, _FMT_NO_FIELDS):
            with tempfile.TemporaryDirectory() as td:
                p = Path(td) / "x.md"
                p.write_text(content, encoding="utf-8")
                fm = loader.load_frontmatter(p)
                text = loader._read(p)
                # deve poter costruire un Agent minimale senza eccezioni
                agent = Agent(
                    id=loader._extract_field(text, "ID") or loader._id_from_filename(p),
                    name=loader._title_from_content(text, fallback=p.stem),
                    path=p,
                    prov=loader._provenance(p, fm),
                )
                self.assertTrue(agent.id)


class TestLoadAgentsRealRepo(unittest.TestCase):
    """Gate G-A: run reale sul monorepo. Conferma i numeri misurati in CP-20260722."""

    @classmethod
    def setUpClass(cls):
        t0 = time.time()
        cls.agents = loader.load_agents()
        cls.elapsed = time.time() - t0

    def test_more_than_200_agents_found(self):
        self.assertGreater(len(self.agents), 200)

    def test_load_under_ten_seconds(self):
        self.assertLess(self.elapsed, 10.0)

    def test_every_agent_has_id_and_path(self):
        for a in self.agents:
            self.assertTrue(a.id)
            self.assertTrue(a.path.exists())

    def test_known_agent_ops_watchdog_present(self):
        ids = {a.id for a in self.agents}
        self.assertIn("ops-watchdog", ids)

    def test_ecosystem_correct_for_ecosistemi_source(self):
        watchdog = next(a for a in self.agents if a.id == "ops-watchdog")
        self.assertEqual(watchdog.ecosystem, "09-OPERATIONS")

    def test_no_duplicate_paths(self):
        paths_seen = [str(a.path) for a in self.agents]
        self.assertEqual(len(paths_seen), len(set(paths_seen)))


class TestLoadOtherKindsRealRepo(unittest.TestCase):
    def test_load_ecosystems_returns_ten(self):
        ecos = loader.load_ecosystems()
        self.assertEqual(len(ecos), 10)

    def test_load_workflows_extracts_referenced_paths(self):
        wfs = loader.load_workflows()
        self.assertTrue(any(wf.referenced_paths for wf in wfs))

    def test_load_skills_nonempty(self):
        skills = loader.load_skills()
        self.assertGreater(len(skills), 0)

    def test_load_departments_nonempty(self):
        depts = loader.load_departments()
        self.assertGreater(len(depts), 0)


if __name__ == "__main__":
    unittest.main()
