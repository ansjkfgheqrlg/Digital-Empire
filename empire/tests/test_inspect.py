"""
Owner: Max · Controllore: Claude · Origine: FORGE
Governo: MANDATO Art.8 + ADR-010 (test_inspect.py)
"""
from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from empire import paths
from empire.memory import store, Atom
from empire.inspect.record import (
    PerfRecord, FeedbackRecord, perf_to_atom, atom_to_perf,
    feedback_to_atom, atom_to_feedback
)
from empire.inspect.benchmarks import get_benchmark
from empire.inspect.collector import capture_run
from empire.inspect.analyst import calculate_scorecard
from empire.inspect.synth import synthesize_patterns
from empire.inspect.dispatch import dispatch_feedback, should_dispatch_tip
from empire.inspect.confirm import process_t5_confirm
from empire.inspect.report import get_organ_status, write_daily_report

TZ = timezone(timedelta(hours=2))

class TestInspectSuite(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._tmp_path = Path(self._tmp.name)
        
        # Isola store memoria
        self._orig_atoms = store.atoms_path
        self._orig_lock = store._lock_path
        store.atoms_path = lambda: self._tmp_path / "atoms.jsonl"
        store._lock_path = lambda: self._tmp_path / ".idlock"
        
        # Isola percorsi reali su disco
        self._orig_resolve = paths.resolve
        
        def mock_resolve(alias, *parts):
            if alias in ("isp_telemetry", "isp_report", "isp_state", "memory_cp"):
                base = self._tmp_path / alias
            else:
                base = self._orig_resolve(alias)
            return base.joinpath(*parts) if parts else base
            
        paths.resolve = mock_resolve

    def tearDown(self):
        store.atoms_path = self._orig_atoms
        store._lock_path = self._orig_lock
        paths.resolve = self._orig_resolve
        self._tmp.cleanup()

    # 1. PerfRecord -> Atom roundtrip
    def test_record_perf_to_atom(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-20260723-001", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        atom = perf_to_atom(perf)
        self.assertEqual(atom.kind, "perf")
        self.assertEqual(atom.actor, "gael")
        self.assertEqual(atom.task, "T-1")

    # 2. Atom -> PerfRecord roundtrip
    def test_record_atom_to_perf(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-20260723-001", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        atom = perf_to_atom(perf)
        back = atom_to_perf(atom)
        self.assertEqual(back.id, perf.id)
        self.assertEqual(back.agent, perf.agent)
        self.assertEqual(back.family, perf.family)

    # 3. FeedbackRecord -> Atom roundtrip
    def test_record_feedback_to_atom(self):
        fb = FeedbackRecord(
            id="FB-20260723-001", ftype="TIP", to="gael", micro_input="Controlla prima",
            on_perf="PERF-1", status="open", opened=datetime.now(TZ)
        )
        atom = feedback_to_atom(fb)
        self.assertEqual(atom.kind, "feedback")
        self.assertEqual(atom.status, "open")

    # 4. Atom -> FeedbackRecord roundtrip
    def test_record_atom_to_feedback(self):
        fb = FeedbackRecord(
            id="FB-20260723-001", ftype="TIP", to="gael", micro_input="Controlla prima",
            on_perf="PERF-1", status="open", opened=datetime.now(TZ)
        )
        atom = feedback_to_atom(fb)
        back = atom_to_feedback(atom)
        self.assertEqual(back.id, fb.id)
        self.assertEqual(back.ftype, fb.ftype)
        self.assertEqual(back.micro_input, fb.micro_input)

    # 5. Benchmarks default
    def test_benchmarks_default(self):
        self.assertEqual(get_benchmark("famiglia-sconosciuta"), 4.0)

    # 6. Benchmarks known
    def test_benchmarks_known(self):
        self.assertEqual(get_benchmark("build-python"), 2.0)

    # 7. capture_run saves file
    def test_capture_run_saves_file(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        captured = capture_run(perf)
        self.assertTrue(captured.id.startswith("PERF-"))
        record_file = paths.resolve("isp_telemetry", "runs", f"RUN-{captured.id}.json")
        self.assertTrue(record_file.exists())

    # 8. capture_run saves atom
    def test_capture_run_saves_atom(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        captured = capture_run(perf)
        got = store.read(captured.id)
        self.assertIsNotNone(got)
        self.assertEqual(got.actor, "gael")

    # 9. capture_run idempotence
    def test_capture_run_idempotence(self):
        now = datetime.now(TZ)
        perf1 = PerfRecord(
            id="", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        perf2 = PerfRecord(
            id="", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        c1 = capture_run(perf1)
        c2 = capture_run(perf2)
        self.assertEqual(c1.id, c2.id)

    # 10. scorecard correctness no errors
    def test_scorecard_correctness_no_errors(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, debug={"errori": 0, "retry": 0, "escalation": 0},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["correctness"], 5.0)

    # 11. scorecard correctness errors
    def test_scorecard_correctness_errors(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, debug={"errori": 1, "retry": 2, "escalation": 0},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        # 5 - min(4, 1 + 2*0.5) = 5 - 2 = 3.0
        self.assertEqual(score["correctness"], 3.0)

    # 12. scorecard correctness min limit
    def test_scorecard_correctness_min_limit(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, debug={"errori": 10, "retry": 10, "escalation": 10},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["correctness"], 1.0)

    # 13. scorecard solution first pass
    def test_scorecard_solution_first_pass(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, verification={"first_pass": True},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["solution"], 5)

    # 14. scorecard solution revision
    def test_scorecard_solution_revision(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, verification={"first_pass": False, "revisions": 1},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["solution"], 4)

    # 15. scorecard solution regression
    def test_scorecard_solution_regression(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, verification={"regression": True},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["solution"], 1)

    # 16. scorecard solution post consegna
    def test_scorecard_solution_post_consegna(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, verification={"post_consegna": True},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["solution"], 2)

    # 17. scorecard structure no files
    def test_scorecard_structure_no_files(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["structure"], 5.0)

    # 18. scorecard structure non existent
    def test_scorecard_structure_non_existent(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[Path("non-existent-file.py")], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["structure"], 1.0)

    # 19. scorecard structure existent non conformant
    def test_scorecard_structure_existent_non_conformant(self):
        # We create a dummy file without ADR-008 header
        p = self._tmp_path / "dummy.py"
        p.write_text("print('test')", encoding="utf-8")
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[p], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["structure"], 3.0)

    # 20. scorecard scope fit no dods
    def test_scorecard_scope_fit_no_dods(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, verification={"dods_total": 0},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["scope_fit"], 5.0)

    # 21. scorecard scope fit partial
    def test_scorecard_scope_fit_partial(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, verification={"dods_total": 10, "dods_verified": 8},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertEqual(score["scope_fit"], 4.2)

    # 22. scorecard efficiency under
    def test_scorecard_efficiency_under(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=1.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        # ttd_h = 1.0 vs benchmark 2.0 (ratio = 0.5 <= 0.8) -> 5
        self.assertEqual(score["efficiency"], 5)

    # 23. scorecard efficiency over
    def test_scorecard_efficiency_over(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=10.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        # ttd_h = 10.0 vs benchmark 2.0 (ratio = 5.0 > 3.0) -> 1
        self.assertEqual(score["efficiency"], 1)

    # 24. scorecard traceability
    def test_scorecard_traceability(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-TASK", workflow="WF-1", family="build-python",
            result="success", started=now, ended=now, ttd_h=0.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        score = calculate_scorecard(perf)
        self.assertFalse(score["traceability"])
        
        # Aggiungiamo un checkpoint atomico in memoria
        store.write(Atom(kind="checkpoint", title="test checkpoint", task="T-TASK"))
        score2 = calculate_scorecard(perf)
        self.assertTrue(score2["traceability"])

    # 25. synth pattern proposed
    def test_synth_pattern_proposed(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, verification={"note": "ambiente sessione senza python"},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        pats = synthesize_patterns(perf)
        self.assertEqual(len(pats), 1)
        self.assertEqual(pats[0].title, "build dichiarato senza runtime disponibile")
        self.assertEqual(pats[0].status, "proposed")

    # 26. synth pattern recurrence
    def test_synth_pattern_recurrence(self):
        now = datetime.now(TZ)
        perf = PerfRecord(
            id="PERF-1", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, verification={"note": "ambiente sessione senza python"},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        pats1 = synthesize_patterns(perf)
        pats2 = synthesize_patterns(perf)
        self.assertEqual(pats2[0].extra.get("occurrences"), 2)

    # 27. dispatch anti nagging
    def test_dispatch_anti_nagging(self):
        # Primo dispatch crea un TIP
        now = datetime.now(TZ)
        perf1 = PerfRecord(
            id="", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, verification={"note": "runtime mancante"},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        capture_run(perf1)
        tips1 = dispatch_feedback(perf1.id, dry_run=False)
        self.assertEqual(len(tips1), 1)
        
        # Secondo dispatch per lo stesso agente e famiglia entro 3 task deve essere bloccato
        perf2 = PerfRecord(
            id="", agent="gael", task="T-2", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, verification={"note": "runtime mancante"},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        capture_run(perf2)
        tips2 = dispatch_feedback(perf2.id, dry_run=False)
        self.assertEqual(len(tips2), 0)

    # 28. T5 confirm success
    def test_confirm_t5_success(self):
        now = datetime.now(TZ)
        perf1 = PerfRecord(
            id="", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, verification={"note": "runtime mancante"},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        capture_run(perf1)
        tips = dispatch_feedback(perf1.id, dry_run=False)
        self.assertEqual(len(tips), 1)
        
        # Eseguiamo una performance successiva con esito success
        perf2 = PerfRecord(
            id="", agent="gael", task="T-2", workflow="WF-1", family="build-python",
            result="success", started=now + timedelta(hours=1), ended=now + timedelta(hours=2),
            ttd_h=1.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        capture_run(perf2)
        
        updated = process_t5_confirm("build-python", "gael")
        self.assertEqual(len(updated), 1)
        self.assertEqual(updated[0].status, "confirmed")

    # 29. T5 confirm recurred
    def test_confirm_t5_recurred(self):
        now = datetime.now(TZ)
        perf1 = PerfRecord(
            id="", agent="gael", task="T-1", workflow="WF-1", family="build-python",
            result="failed", started=now, ended=now, ttd_h=0.0, verification={"note": "runtime mancante"},
            output_ref=[], scorecard={}, feedback_ids=[]
        )
        capture_run(perf1)
        tips = dispatch_feedback(perf1.id, dry_run=False)
        self.assertEqual(len(tips), 1)
        
        # Eseguiamo una performance successiva con esito failed
        perf2 = PerfRecord(
            id="", agent="gael", task="T-2", workflow="WF-1", family="build-python",
            result="failed", started=now + timedelta(hours=1), ended=now + timedelta(hours=2),
            ttd_h=1.0, output_ref=[], scorecard={}, feedback_ids=[]
        )
        capture_run(perf2)
        
        updated = process_t5_confirm("build-python", "gael")
        self.assertEqual(len(updated), 1)
        self.assertEqual(updated[0].status, "recurred")
        
        # Deve esistere l'escalation report
        esc_file = paths.resolve("isp_report", "escalation", f"ESC-{updated[0].id}.md")
        self.assertTrue(esc_file.exists())

    # 30. report status
    def test_report_status(self):
        status = get_organ_status()
        self.assertEqual(status["open_loops_count"], 0)
