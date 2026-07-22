"""
EMPIRE MEMORY — test (M-A).

Owner: Max · Controllore: Claude · Origine: FORGE

Il test che conta e' `test_concurrent_ids_never_collide`: riproduce B-009, la collisione di ID
avvenuta tre volte il 2026-07-22 fra Claude e Gael.

    python -m unittest discover -s empire/tests -p "test_*.py"
"""
from __future__ import annotations

import json
import os
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from empire.memory import model, store
from empire.memory import render, parse, search, recall
from empire.memory.model import Atom, AtomError


class _IsolatedStore(unittest.TestCase):
    """Ogni test lavora su un archivio temporaneo: mai sugli atomi reali."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        d = Path(self._tmp.name)
        self._orig_atoms = store.atoms_path
        self._orig_lock = store._lock_path
        store.atoms_path = lambda: d / "atoms.jsonl"          # type: ignore[assignment]
        store._lock_path = lambda: d / ".idlock"              # type: ignore[assignment]
        # niente ID letti dai .md reali: i test devono essere deterministici
        self._orig_disk = store._DISK_SOURCES
        store._DISK_SOURCES = {}                              # type: ignore[assignment]

    def tearDown(self):
        store.atoms_path = self._orig_atoms                   # type: ignore[assignment]
        store._lock_path = self._orig_lock                    # type: ignore[assignment]
        store._DISK_SOURCES = self._orig_disk                 # type: ignore[assignment]
        self._tmp.cleanup()


class TestModel(unittest.TestCase):
    def test_kind_must_be_known(self):
        with self.assertRaises(AtomError):
            Atom(kind="inventato", title="x").validate()

    def test_title_required(self):
        with self.assertRaises(AtomError):
            Atom(kind="checkpoint", title="  ").validate()

    def test_malformed_id_rejected(self):
        with self.assertRaises(AtomError):
            Atom(kind="checkpoint", title="x", id="CP-2026-1").validate()

    def test_required_extra_enforced_on_new_atoms(self):
        with self.assertRaises(AtomError):
            Atom(kind="feedback", title="tip").validate()

    def test_required_extra_relaxed_on_imported_atoms(self):
        """Un file legacy incompleto si importa com'e': inventare un campo falsifica la storia."""
        Atom(kind="feedback", title="tip", source="DIGITAL-EMPIRE/00-MEMORY/feedback/FB-001.md").validate()

    def test_hash_ignores_id_and_timestamp(self):
        a = Atom(kind="checkpoint", title="T", body="B", id="CP-20260722-001", ts="2026-07-22T10:00:00+02:00")
        b = Atom(kind="checkpoint", title="T", body="B", id="CP-20260101-999", ts="2026-01-01T00:00:00+02:00")
        self.assertEqual(a.compute_hash(), b.compute_hash())

    def test_hash_changes_with_content(self):
        a = Atom(kind="checkpoint", title="T", body="B")
        b = Atom(kind="checkpoint", title="T", body="B diverso")
        self.assertNotEqual(a.compute_hash(), b.compute_hash())

    def test_roundtrip_dict(self):
        a = Atom(kind="plan", title="T", refs=["ADR-001"], artifacts=["x.py"])
        self.assertEqual(Atom.from_dict(a.to_dict()).title, a.title)


class TestStore(_IsolatedStore):
    def test_write_assigns_id(self):
        a = store.write(Atom(kind="checkpoint", title="primo"))
        self.assertRegex(a.id, r"^CP-\d{8}-001$")

    def test_ids_increment(self):
        ids = [store.write(Atom(kind="checkpoint", title=f"n{i}")).id for i in range(3)]
        self.assertEqual(len(set(ids)), 3)
        self.assertTrue(ids[2].endswith("003"))

    def test_concurrent_ids_never_collide(self):
        """B-009 — 20 scritture in parallelo devono produrre 20 ID distinti, zero perdite."""
        with ThreadPoolExecutor(max_workers=8) as ex:
            got = list(ex.map(lambda i: store.write(Atom(kind="checkpoint", title=f"par-{i}")),
                              range(20)))
        ids = [a.id for a in got]
        self.assertEqual(len(ids), 20)
        self.assertEqual(len(set(ids)), 20, f"COLLISIONE: {sorted(ids)}")
        self.assertEqual(len(list(store.all_atoms())), 20, "un atomo e' andato perso")

    def test_different_kinds_have_separate_sequences(self):
        cp = store.write(Atom(kind="checkpoint", title="a"))
        adr = store.write(Atom(kind="decision", title="b"))
        self.assertTrue(cp.id.startswith("CP-"))
        self.assertTrue(adr.id.startswith("ADR-"))
        self.assertTrue(adr.id.endswith("001"))

    def test_read_returns_written_atom(self):
        a = store.write(Atom(kind="checkpoint", title="leggimi", body="corpo integrale"))
        got = store.read(a.id)
        self.assertIsNotNone(got)
        self.assertEqual(got.body, "corpo integrale")

    def test_read_missing_returns_none(self):
        self.assertIsNone(store.read("CP-20260101-999"))

    def test_dedup_does_not_duplicate(self):
        a = Atom(kind="checkpoint", title="uguale", body="stesso")
        store.write(a, dedup=True)
        b = Atom(kind="checkpoint", title="uguale", body="stesso")
        store.write(b, dedup=True)
        self.assertEqual(len(list(store.all_atoms())), 1)

    def test_write_many_is_atomic_and_unique(self):
        atoms = [Atom(kind="plan", title=f"p{i}") for i in range(50)]
        store.write_many(atoms)
        ids = [a.id for a in atoms]
        self.assertEqual(len(set(ids)), 50)
        self.assertEqual(len(list(store.all_atoms())), 50)

    def test_jsonl_is_valid_and_utf8(self):
        store.write(Atom(kind="checkpoint", title="àccentata — con em dash 🧠"))
        with open(store.atoms_path(), encoding="utf-8") as fh:
            for line in fh:
                json.loads(line)

    def test_body_is_never_truncated(self):
        """memory-empire: archiviazione INTEGRALE, mai riassunti."""
        big = "riga\n" * 5000
        a = store.write(Atom(kind="checkpoint", title="lungo", body=big))
        self.assertEqual(store.read(a.id).body, big)


class TestRender(unittest.TestCase):
    def test_cp_roundtrip_preserves_key_fields(self):
        a = Atom(kind="checkpoint", id="CP-20260722-099", title="Titolo di prova",
                 ts="2026-07-22T10:00:00+02:00", actor="Claude", task="fare la cosa",
                 status="done", body="corpo del checkpoint")
        back = parse(render(a))
        self.assertEqual(back.id, a.id)
        self.assertEqual(back.title, a.title)
        self.assertEqual(back.actor, a.actor)
        self.assertEqual(back.task, a.task)
        self.assertEqual(back.ts[:10], a.ts[:10])
        self.assertEqual(back.status, "done")

    def test_render_uses_observed_cp_format(self):
        """Formato osservato in company/Memory/templates/CP-template.md, non inventato."""
        out = render(Atom(kind="checkpoint", id="CP-20260722-099", title="X"))
        self.assertTrue(out.startswith("# CP-20260722-099 — X"))
        for label in ("- **Data:**", "- **Task:**", "- **Esito:**", "- **Prossimo passo:**"):
            self.assertIn(label, out)

    def test_decision_uses_adr_format(self):
        out = render(Atom(kind="decision", id="ADR-20260722-001", title="D",
                                 status="ATTIVO", extra={"decisione": "si fa cosi'"}))
        for h in ("## Contesto", "## Decisione", "## Alternative scartate",
                  "## Conseguenze", "## Contradiction-check"):
            self.assertIn(h, out)
        self.assertIn("si fa cosi'", out)

    def test_parse_tolerates_files_without_template(self):
        a = parse("# Titolo libero\n\ntesto senza campi\n")
        self.assertEqual(a.title, "Titolo libero")
        self.assertTrue(a.body)

    def test_parse_real_checkpoint_on_disk(self):
        from empire.paths import resolve
        d = resolve("memory_cp")
        files = sorted(d.glob("CP-*.md"))
        self.assertTrue(files, "nessun checkpoint reale su disco")
        a = parse(files[-1].read_text(encoding="utf-8", errors="replace"))
        self.assertTrue(a.title, f"titolo non estratto da {files[-1].name}")
        self.assertTrue(a.id.startswith("CP-"), f"id non estratto da {files[-1].name}")


class TestSearch(_IsolatedStore):
    def _seed(self):
        store.write(Atom(kind="decision", title="Prezzo Manuale Claude Code",
                         body="EUR67 lancio", status="ATTIVO"))
        store.write(Atom(kind="checkpoint", title="EmpireDesk selftest",
                         body="16/16 PASS, modulo youtube"))
        store.write(Atom(kind="error", title="UnicodeEncodeError su Windows",
                         body="charmap codec, memory_manager.py"))

    def test_search_finds_by_title(self):
        self._seed()
        hits = search("prezzo manuale")
        self.assertTrue(hits)
        self.assertIn("Prezzo", hits[0][0].title)

    def test_search_finds_by_body(self):
        self._seed()
        self.assertTrue(search("charmap"))

    def test_search_empty_query(self):
        self.assertEqual(search("   "), [])

    def test_search_filters_by_kind(self):
        self._seed()
        hits = search("empiredesk", kind="checkpoint")
        self.assertTrue(all(a.kind == "checkpoint" for a, _ in hits))

    def test_recall_respects_line_budget(self):
        self._seed()
        out = recall("manuale", max_lines=12)
        self.assertLessEqual(len(out.splitlines()), 12)

    def test_recall_on_empty_topic_is_explicit(self):
        out = recall("argomento-che-non-esiste-mai")
        self.assertIn("nessun atomo", out)


class TestRealArchive(unittest.TestCase):
    """Controlli sull'archivio reale, se l'import e' stato eseguito."""

    def test_real_archive_is_consistent(self):
        atoms = list(store.all_atoms())
        if not atoms:
            self.skipTest("archivio vuoto: eseguire `python -m empire mem ingest --apply`")
        ids = [a.id for a in atoms]
        self.assertEqual(len(ids), len(set(ids)), "ID duplicati nell'archivio reale")
        for a in atoms:
            self.assertIn(a.kind, model.KINDS)
            self.assertTrue(a.title)
            self.assertFalse(a.ts.startswith("1970"), f"data non risolta: {a.id}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
