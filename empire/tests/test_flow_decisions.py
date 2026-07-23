"""
EMPIRE — test di empire.flow.decisions e empire.flow.evidence (LOTTO 2, completamento
Workflow Estate).

Owner: Claude · Origine: FORGE (CP-20260723)

I test isolano stato e fatti in cartelle temporanee: nessun test deve poter scrivere
nei fatti veri dell'azienda, altrimenti eseguire la suite cambierebbe il colore dei gate.
"""
from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from empire.flow import decisions, evidence, gate


ROME = timezone(timedelta(hours=2))


def _decision(did="DEC-EST-001", deadline="2026-07-21T20:00:00+02:00", fact=None):
    d = {"id": did, "topic": "prezzo", "default": "EUR 67", "veto_deadline": deadline}
    if fact:
        d["fact"] = fact
    return d


class _IsolatedState(unittest.TestCase):
    """Ogni test parte da uno stato e da fatti vuoti, su disco temporaneo."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name)
        self._patches = [
            mock.patch.object(decisions._state, "STATE_DIR", root / "state"),
            mock.patch.object(gate, "FACTS_DIR", root / "facts"),
            mock.patch.object(gate, "FACTS_PATH", root / "facts" / "facts.json"),
        ]
        for p in self._patches:
            p.start()

    def tearDown(self):
        for p in self._patches:
            p.stop()
        self._tmp.cleanup()


# ------------------------------------------------------------------ nome del fatto

class TestFactName(unittest.TestCase):
    def test_explicit_wins(self):
        self.assertEqual(decisions.fact_name_for(_decision(fact="pippo")), "pippo")

    def test_derived_from_trailing_number(self):
        self.assertEqual(decisions.fact_name_for(_decision("DEC-EST-004")), "dec_004_attiva")

    def test_derivation_matches_gate_dec_convention(self):
        # Gate-DEC in workflows.yaml ha green_if "dec_001_attiva >= 1": se questa
        # convenzione si rompe, il gate torna rosso senza che nessuno se ne accorga.
        self.assertEqual(decisions.fact_name_for(_decision("DEC-EST-001")), "dec_001_attiva")


# ------------------------------------------------------------------ default piu' veto

class TestDefaultPlusVeto(_IsolatedState):
    def test_before_deadline_is_pending_and_writes_nothing(self):
        future = (datetime.now(ROME) + timedelta(days=2)).isoformat()
        st = decisions.apply_all([_decision(deadline=future)])
        self.assertEqual(st[0].state, "IN_ATTESA")
        self.assertEqual(gate.load_facts().get("dec_001_attiva"), None)

    def test_after_deadline_becomes_active_and_writes_fact(self):
        past = (datetime.now(ROME) - timedelta(days=1)).isoformat()
        st = decisions.apply_all([_decision(deadline=past)])
        self.assertEqual(st[0].state, "ATTIVA")
        self.assertEqual(gate.load_facts().get("dec_001_attiva"), 1)

    def test_fact_carries_its_source(self):
        past = (datetime.now(ROME) - timedelta(days=1)).isoformat()
        decisions.apply_all([_decision(deadline=past)])
        src = gate.load_facts().get("_sources", {}).get("dec_001_attiva", "")
        self.assertIn("ADR-EST-006", src)
        self.assertIn("DEC-EST-001", src)

    def test_veto_blocks_activation(self):
        past = (datetime.now(ROME) - timedelta(days=1)).isoformat()
        ok, _ = decisions.register_veto("DEC-EST-001", actor="Max", reason="prezzo troppo basso")
        self.assertTrue(ok)
        st = decisions.apply_all([_decision(deadline=past)])
        self.assertEqual(st[0].state, "VETO")
        self.assertEqual(gate.load_facts().get("dec_001_attiva"), 0)
        self.assertIn("Max", st[0].reason)

    def test_veto_requires_a_reason(self):
        ok, msg = decisions.register_veto("DEC-EST-002", actor="Max", reason="   ")
        self.assertFalse(ok)
        self.assertIn("reason", msg)

    def test_veto_is_idempotent(self):
        decisions.register_veto("DEC-EST-001", actor="Max", reason="no")
        ok, msg = decisions.register_veto("DEC-EST-001", actor="Max", reason="no")
        self.assertFalse(ok)
        self.assertIn("gia'", msg)

    def test_apply_all_is_idempotent(self):
        past = (datetime.now(ROME) - timedelta(days=1)).isoformat()
        decisions.apply_all([_decision(deadline=past)])
        first = gate.load_facts()
        decisions.apply_all([_decision(deadline=past)])
        self.assertEqual(first, gate.load_facts())

    def test_dry_run_writes_nothing(self):
        past = (datetime.now(ROME) - timedelta(days=1)).isoformat()
        st = decisions.apply_all([_decision(deadline=past)], write=False)
        self.assertEqual(st[0].state, "ATTIVA")
        self.assertEqual(gate.load_facts(), {})

    def test_missing_deadline_stays_pending(self):
        st = decisions.apply_all([_decision(deadline=None)])
        self.assertEqual(st[0].state, "IN_ATTESA")


# ------------------------------------------------------------------ evidenza

class TestEvidence(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._p = mock.patch.object(evidence, "repo_root", lambda: self.root)
        self._p.start()

    def tearDown(self):
        self._p.stop()
        self._tmp.cleanup()

    def _write(self, rel: str, text: str) -> Path:
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def test_counts_only_valued_rows(self):
        self._write("lead.csv", "Nome,Ultimo Contatto\nA,2026-07-22\nB,\nC,2026-07-21\n")
        ev = evidence.compute({"kind": "csv_rows", "path": "lead.csv",
                               "column": "Ultimo Contatto", "label": "contattati"})
        self.assertIn("2/3", ev.value)

    def test_missing_source_is_declared_not_zero(self):
        ev = evidence.compute({"kind": "csv_rows", "path": "assente.csv", "label": "x"})
        self.assertIn("non esiste", ev.warning)

    def test_test_filename_raises_warning(self):
        self._write("test_lead_finti.csv", "Nome\nA\n")
        ev = evidence.compute({"kind": "csv_rows", "path": "test_lead_finti.csv", "label": "x"})
        self.assertIn("DATI DI PROVA", ev.warning)

    def test_test_content_raises_warning(self):
        self._write("lead.csv", "Nome,Indirizzo\nAutosalone,Via Finta 1 Milano\n")
        ev = evidence.compute({"kind": "csv_rows", "path": "lead.csv", "label": "x"})
        self.assertIn("DATI DI PROVA", ev.warning)

    def test_untraceable_rows_are_flagged(self):
        # Nomi perfettamente plausibili: nessuna regex li smaschera. L'unica prova
        # che siano reali e' che esistano a monte — qui non esistono.
        self._write("lead.csv", "Concessionaria,Ultimo Contatto\nAutoElite Milano,2026-07-22\n")
        self._write("Outreach/altro.csv", "nome\nQualcun Altro\n")
        ev = evidence.compute({"kind": "csv_rows", "path": "lead.csv",
                               "column": "Ultimo Contatto", "label": "x",
                               "key_column": "Concessionaria",
                               "cross_check_glob": "Outreach/**/*.csv"})
        self.assertIn("tracciabilita'", ev.warning)

    def test_traceable_rows_are_not_flagged(self):
        self._write("lead.csv", "Concessionaria,Ultimo Contatto\nAutoElite Milano,2026-07-22\n")
        self._write("Outreach/scrape.csv", "nome\nAutoElite Milano\n")
        ev = evidence.compute({"kind": "csv_rows", "path": "lead.csv",
                               "column": "Ultimo Contatto", "label": "x",
                               "key_column": "Concessionaria",
                               "cross_check_glob": "Outreach/**/*.csv"})
        self.assertEqual(ev.warning, "")

    def test_glob_reports_absence(self):
        ev = evidence.compute({"kind": "glob", "pattern": "07-VIDEO-RUN/*/05-STATO.md",
                               "label": "run"})
        self.assertIn("nessun file", ev.value)

    def test_unknown_kind_does_not_raise(self):
        ev = evidence.compute({"kind": "boh", "label": "x"})
        self.assertIn("sconosciuto", ev.warning)

    def test_no_spec_returns_none(self):
        self.assertIsNone(evidence.compute(None))


# ------------------------------------------------------------------ gate + evidenza

class TestGateWithEvidence(unittest.TestCase):
    def _gate(self, **kw):
        from empire.flow.spec import Gate
        base = dict(id="Gate-X", deadline=datetime.now(ROME) - timedelta(days=1),
                    type="human", green_if="x >= 1", on_red="fai il fallback")
        base.update(kw)
        return Gate(**base)

    def test_evidence_never_turns_a_gate_green(self):
        g = self._gate(evidence={"kind": "glob", "pattern": "*", "label": "tutto"})
        r = gate.evaluate(g, facts={})
        self.assertEqual(r.status, "RED")  # evidenza abbondante, conferma umana assente

    def test_broken_evidence_does_not_break_the_gate(self):
        g = self._gate(evidence={"kind": "csv_rows", "path": "/percorso/inesistente"})
        r = gate.evaluate(g, facts={})
        self.assertEqual(r.status, "RED")
        self.assertTrue(r.evidence)

    def test_on_red_applied_only_marks_red_gates(self):
        g = self._gate()
        r = gate.evaluate(g, facts={}, on_red_applied=True)
        self.assertEqual(r.status, "RED")
        self.assertTrue(r.on_red_applied)

    def test_on_red_applied_is_not_set_on_green(self):
        g = self._gate()
        r = gate.evaluate(g, facts={}, human_confirmed=True, on_red_applied=True)
        self.assertEqual(r.status, "GREEN")
        self.assertFalse(r.on_red_applied)


if __name__ == "__main__":
    unittest.main()
