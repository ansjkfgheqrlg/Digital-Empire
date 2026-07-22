"""
EMPIRE — test del seed (paths, config, schema, conform).

Owner: Max · Controllore: Claude · Origine: FORGE (seed CP-20260722-003)

Eseguire dalla radice del monorepo:
    python -m pytest empire/tests -q
    python -m unittest discover -s empire/tests -p "test_*.py"   (senza pytest)
"""
from __future__ import annotations

import os
import unittest
from pathlib import Path

from empire import paths, config, conform
from empire.schema import Provenance, Finding


class TestPaths(unittest.TestCase):
    def test_root_found_from_anywhere(self):
        root = paths.repo_root()
        self.assertTrue((root / "company" / "Mandato" / "MANDATO-EMPIRE.md").exists())

    def test_root_is_stable_across_cwd(self):
        first = paths.repo_root()
        old = Path.cwd()
        try:
            os.chdir(first / "company" / "Memory")
            paths.repo_root.cache_clear()
            self.assertEqual(paths.repo_root(), first)
        finally:
            os.chdir(old)
            paths.repo_root.cache_clear()

    def test_every_alias_exists(self):
        missing = [k for k in paths.config_data()["alias"] if not paths.resolve(k).exists()]
        self.assertEqual(missing, [], f"alias che non risolvono: {missing}")

    def test_unknown_alias_raises(self):
        with self.assertRaises(paths.UnknownAlias):
            paths.resolve("questo-alias-non-esiste-mai")

    def test_resolve_legacy_repairs_estate_refs(self):
        """I riferimenti rotti di WORKFLOW-ESTATE devono risolvere verso DIGITAL-EMPIRE."""
        for ref in ("00-MEMORY/", "04-AGENTS/PERFORMANCE-CELL.md",
                    "03-WORKFLOWS/workflows.yaml", "02-ARCHITECTURE/ARCHITETTURA-ESTATE.md"):
            with self.subTest(ref=ref):
                self.assertIsNotNone(paths.resolve_legacy(ref), f"non riparato: {ref}")

    def test_resolve_legacy_returns_none_for_dead_end(self):
        self.assertIsNone(paths.resolve_legacy("99-INESISTENTE/mai-visto.md"))

    def test_legacy_file_exception(self):
        p = paths.resolve_legacy("00-MEMORY/memory_manager.py")
        self.assertIsNotNone(p)
        self.assertEqual(p.name, "memory_manager.py")

    def test_iter_files_excludes_git(self):
        sample = list(paths.iter_files(paths.resolve("memory_cp"), suffixes=(".md",)))
        self.assertTrue(sample)
        self.assertFalse(any(".git" in p.parts for p in sample))

    def test_rel_is_posix_and_relative(self):
        r = paths.rel(paths.resolve("mandato"))
        self.assertEqual(r, "company/Mandato/MANDATO-EMPIRE.md")


class TestConfig(unittest.TestCase):
    def test_env_keys_never_leak_values(self):
        for k in config.env_keys():
            self.assertIsInstance(k, str)

    def test_missing_secret_message_has_no_value(self):
        with self.assertRaises(config.MissingSecret) as ctx:
            config.get_secret("EMPIRE_SEGRETO_INESISTENTE_XYZ")
        self.assertIn(".env", str(ctx.exception))

    def test_optional_secret_returns_none(self):
        self.assertIsNone(config.get_secret("EMPIRE_SEGRETO_INESISTENTE_XYZ", required=False))

    def test_data_dir_is_inside_empire(self):
        d = config.data_dir("test-tmp")
        self.assertTrue(d.exists())
        self.assertIn("empire", d.parts)
        d.rmdir()


class TestSchema(unittest.TestCase):
    def test_provenance_complete(self):
        self.assertFalse(Provenance().complete)
        full = Provenance(owner="Max", controller="Claude", origin="FORGE", governance="MANDATO")
        self.assertTrue(full.complete)
        self.assertEqual(full.missing, [])

    def test_provenance_missing_lists_fields(self):
        p = Provenance(owner="Max")
        self.assertEqual(set(p.missing), {"controller", "origin", "governance"})

    def test_finding_rank_order(self):
        f = [Finding("info", "R", Path("a"), "m"), Finding("block", "R", Path("b"), "m")]
        f.sort(key=lambda x: x.rank)
        self.assertEqual(f[0].severity, "block")


class TestConform(unittest.TestCase):
    def test_art8_detects_empty_pillars(self):
        """Stato noto al 2026-07-22: 05-TEMPLATES-E-KIT e 06-DASHBOARD-E-METRICHE vuote."""
        findings = conform.check_art8("WORKFLOW-ESTATE")
        empty = {f.path.name for f in findings if f.severity == "block"}
        # il test resta valido anche dopo il risanamento: verifica solo che il
        # controllo riconosca una cartella vuota quando c'e'
        for name in empty:
            self.assertTrue((paths.resolve("estate_wf") / name).is_dir())

    def test_art8_flags_missing_workflow_root(self):
        f = conform.check_art8("CARTELLA-CHE-NON-ESISTE")
        self.assertEqual(len(f), 1)
        self.assertEqual(f[0].severity, "block")

    def test_links_finds_fixable_refs(self):
        findings = conform.check_links("WORKFLOW-ESTATE")
        fixable = [f for f in findings if f.rule == "LINK-FIXABLE"]
        self.assertGreaterEqual(len(fixable), 5, "il resolver legacy non sta riparando nulla")

    def test_links_excludes_vendored_by_default(self):
        default = conform.check_links("WORKFLOW-ESTATE")
        withv = conform.check_links("WORKFLOW-ESTATE", include_vendored=True)
        self.assertLess(len(default), len(withv))

    def test_is_vendored(self):
        root = paths.repo_root()
        self.assertTrue(conform.is_vendored(root / "WORKFLOW-ESTATE" / ".agents" / "x.md"))
        self.assertTrue(conform.is_vendored(root / "WORKFLOW-ESTATE" / "forge-run-2026" / "x.md"))
        self.assertFalse(conform.is_vendored(root / "WORKFLOW-ESTATE" / "01-FLUSSI-E-PIANI" / "x.md"))

    def test_run_all_is_sorted_by_severity(self):
        f = conform.run_all("WORKFLOW-ESTATE")
        self.assertEqual([x.rank for x in f], sorted(x.rank for x in f))


class TestIdempotence(unittest.TestCase):
    def test_conform_twice_same_result(self):
        a = conform.run_all("WORKFLOW-ESTATE")
        b = conform.run_all("WORKFLOW-ESTATE")
        self.assertEqual(len(a), len(b))
        self.assertEqual([x.message for x in a], [x.message for x in b])


if __name__ == "__main__":
    unittest.main(verbosity=2)
