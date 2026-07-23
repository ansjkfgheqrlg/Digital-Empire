"""
EMPIRE — test di empire.flow (lotto G-C, Gael).

Owner: Gael · Controllore: Claude · Origine: FORGE (CP-20260722, brief GEM-06)
"""
from __future__ import annotations

import shutil
import unittest
from datetime import datetime, timedelta, timezone

from empire.flow import dag, gate, spec, state, queue as flowqueue, runner


# ---------------------------------------------------------------- gate.eval_expression

class TestEvalExpression(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(gate.eval_expression("contattati >= 7", {"contattati": 7}))

    def test_simple_false(self):
        self.assertFalse(gate.eval_expression("contattati >= 7", {"contattati": 3}))

    def test_missing_fact_is_false(self):
        self.assertFalse(gate.eval_expression("x >= 1", {}))

    def test_and(self):
        facts = {"a": 5, "b": 5}
        self.assertTrue(gate.eval_expression("a >= 5 and b >= 5", facts))
        self.assertFalse(gate.eval_expression("a >= 5 and b >= 10", facts))

    def test_or(self):
        facts = {"a": 1, "b": 5}
        self.assertTrue(gate.eval_expression("a >= 10 or b >= 5", facts))
        self.assertFalse(gate.eval_expression("a >= 10 or b >= 10", facts))

    def test_all_operators(self):
        facts = {"x": 5}
        self.assertTrue(gate.eval_expression("x == 5", facts))
        self.assertTrue(gate.eval_expression("x != 4", facts))
        self.assertTrue(gate.eval_expression("x <= 5", facts))
        self.assertTrue(gate.eval_expression("x < 6", facts))

    def test_no_eval_of_arbitrary_code(self):
        # __import__ non è un nome valido nella grammatica -> deve fallire a
        # tokenizzare, MAI essere eseguito come Python.
        with self.assertRaises(gate.ExpressionError):
            gate.eval_expression("__import__('os').system('echo x')", {})


# ---------------------------------------------------------------- dag

class TestDag(unittest.TestCase):
    def test_topological_order_simple_chain(self):
        edges = {"a": [], "b": ["a"], "c": ["b"]}
        order = dag.topological_order(edges)
        self.assertLess(order.index("a"), order.index("b"))
        self.assertLess(order.index("b"), order.index("c"))

    def test_cycle_detected(self):
        edges = {"a": ["b"], "b": ["a"]}
        with self.assertRaises(dag.CycleError):
            dag.topological_order(edges)

    def test_unlocked_respects_dependencies(self):
        edges = {"a": [], "b": ["a"], "c": ["b"]}
        self.assertEqual(dag.unlocked(edges, done=set()), ["a"])
        self.assertEqual(dag.unlocked(edges, done={"a"}), ["b"])
        self.assertEqual(dag.unlocked(edges, done={"a", "b"}), ["c"])


# ---------------------------------------------------------------- spec + gates reali

class TestSpecRealFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = spec.load_spec()

    def test_six_workflows_estate_present(self):
        for wf in ("WF-S1-CONCESSIONARI", "WF-S2-MANUALE", "WF-S3-PAGINE",
                   "WF-S4-MENTALITA", "WF-S5-YOUTUBE", "WF-S6-REBRAND-PROMO"):
            self.assertIn(wf, self.spec.workflows)

    def test_six_gates_defined(self):
        ids = {g.id for g in self.spec.gates}
        self.assertEqual(ids, {"Gate-DEC", "Gate-FUNNEL", "Gate-CONTATTI",
                                "Gate-S4", "Gate-S5", "Gate-REV"})

    def test_all_deadlines_have_timezone(self):
        for g in self.spec.gates:
            self.assertIsNotNone(g.deadline.tzinfo)

    def test_validate_no_dead_depends(self):
        findings = spec.validate(self.spec)
        dead = [f for f in findings if f.rule == "FLOW-DEPENDS-DEAD"]
        self.assertEqual(dead, [], f"depends morti trovati: {dead}")

    def test_dag_from_real_spec_has_no_cycle(self):
        edges = dag.from_flow_spec(self.spec)
        order = dag.topological_order(edges)  # non deve sollevare CycleError
        self.assertGreater(len(order), 0)


class TestGatesOnRealData(unittest.TestCase):
    """Gate 3 del brief: valuta i 6 gate estate sui dati REALI di oggi.
    Alcuni sono rossi/pending: e' la verita', non un bug (WF-MASTER §3)."""

    @classmethod
    def setUpClass(cls):
        cls.s = spec.load_spec()
        cls.now = datetime.now(timezone.utc).astimezone()
        cls.results = gate.evaluate_all(cls.s.gates, now=cls.now, facts=gate.load_facts())

    def test_six_results(self):
        self.assertEqual(len(self.results), 6)

    def test_every_result_is_one_of_three_states(self):
        for r in self.results:
            self.assertIn(r.status, ("PENDING", "GREEN", "RED"))

    def test_funnel_gate_reflects_real_placeholder_bug(self):
        """Verifica indipendente, non delegata al valore del gate: il file ha
        ancora il placeholder Stripe -> il gate DEVE trovarlo, non dichiararsi verde
        solo perché qualcun altro lo ha scritto in una dashboard (vedi CP-20260722-003/009)."""
        from empire.paths import repo_root
        p = repo_root() / "Crea siti" / "Siti CCM" / "manuale.html"
        funnel = next(r for r in self.results if r.id == "Gate-FUNNEL")
        if p.exists() and "YOUR_STRIPE" in p.read_text(encoding="utf-8", errors="replace"):
            self.assertIn(funnel.status, ("RED", "PENDING"))
            self.assertNotEqual(funnel.status, "GREEN")

    def test_dec_gate_uses_recorded_fact_not_guess(self):
        dec = next(r for r in self.results if r.id == "Gate-DEC")
        # la deadline (21/07 20:00) e' nel passato rispetto a 'oggi' del progetto:
        # deve essere GREEN o RED, mai PENDING.
        self.assertIn(dec.status, ("GREEN", "RED"))


# ---------------------------------------------------------------- state + runner (DoD-4/5/9)

class TestStateAndRunner(unittest.TestCase):
    def setUp(self):
        self.step_ids = [f"TEST-STEP-{i}" for i in range(5)]
        for sid in self.step_ids:
            state._path(sid).unlink(missing_ok=True)
        gate_key = "gate_TEST-GATE"
        state._path(gate_key).unlink(missing_ok=True)

    def tearDown(self):
        for sid in self.step_ids:
            state._path(sid).unlink(missing_ok=True)
        state._path("gate_TEST-GATE").unlink(missing_ok=True)

    def test_step_with_open_dependency_cannot_start(self):
        edges = {self.step_ids[1]: [self.step_ids[0]]}
        ok, msg = runner.start_step(self.step_ids[1], edges=edges, actor="test")
        self.assertFalse(ok)
        self.assertIn("bloccato", msg)

    def test_step_starts_once_dependency_done(self):
        edges = {self.step_ids[1]: [self.step_ids[0]]}
        runner.done_step(self.step_ids[0], actor="test", evidence="fatto")
        ok, msg = runner.start_step(self.step_ids[1], edges=edges, actor="test")
        self.assertTrue(ok)

    def test_done_twice_does_not_duplicate(self):
        ok1, _ = runner.done_step(self.step_ids[2], actor="test", evidence="ev1")
        ok2, msg2 = runner.done_step(self.step_ids[2], actor="test", evidence="ev2")
        self.assertTrue(ok1)
        self.assertFalse(ok2)
        self.assertIn("già chiuso", msg2)
        self.assertEqual(len(state.history(self.step_ids[2])), 1)

    def test_five_step_flow_with_two_human_steps(self):
        """Simula un flusso di 5 passi con dipendenze, di cui 2 human (DoD-4 del brief)."""
        s0, s1, s2, s3, s4 = self.step_ids
        edges = {s1: [s0], s2: [s1], s3: [s2], s4: [s3]}

        ok, _ = runner.start_step(s1, edges=edges, actor="test")
        self.assertFalse(ok, "s1 non deve partire: s0 e' ancora aperto")

        runner.done_step(s0, actor="Max", evidence="human: confermato a voce")
        ok, _ = runner.start_step(s1, edges=edges, actor="test")
        self.assertTrue(ok)
        runner.done_step(s1, actor="test", evidence="script eseguito")

        ok, _ = runner.start_step(s2, edges=edges, actor="test")
        self.assertTrue(ok)
        # s2 e' 'human' e non si chiude da solo: nessuna chiamata a done_step
        # -> deve restare IN_PROGRESS, mai DONE
        self.assertEqual(runner.step_status(s2), "IN_PROGRESS")
        self.assertFalse(state.is_done(s2))

        ok, msg = runner.start_step(s3, edges=edges, actor="test")
        self.assertFalse(ok, "s3 non deve partire: s2 (human) non e' confermato")

    def test_gate_human_never_auto_closes(self):
        # gate 'human' sintetico con deadline passata: senza conferma esplicita
        # deve risultare RED automatico, mai GREEN da solo (GEM-06 §3).
        g = spec.Gate(id="TEST-GATE", deadline=datetime.now(timezone.utc) - timedelta(days=1),
                       type="human", green_if="x >= 1", on_red="escalation")
        result_before = gate.evaluate(g, now=datetime.now(timezone.utc))
        self.assertEqual(result_before.status, "RED", "deadline passata senza conferma -> RED automatico")

        runner.confirm_gate("TEST-GATE", actor="Max", evidence="confermato")
        result_after = gate.evaluate(g, now=datetime.now(timezone.utc), human_confirmed=True)
        self.assertEqual(result_after.status, "GREEN")
        self.assertTrue(state.is_done("gate_TEST-GATE"))


# ---------------------------------------------------------------- queue

class TestQueue(unittest.TestCase):
    def test_precedence_order_respected(self):
        reqs = [
            flowqueue.SwarmRequest(stream="S5", requested_by="a"),
            flowqueue.SwarmRequest(stream="S1", requested_by="b"),
            flowqueue.SwarmRequest(stream="S6", requested_by="c"),
        ]
        winner, queued = flowqueue.admit(reqs)
        self.assertEqual(winner.stream, "S1")
        self.assertEqual([r.stream for r in queued], ["S6", "S5"])

    def test_only_one_winner(self):
        reqs = [flowqueue.SwarmRequest(stream="S2", requested_by="a"),
                flowqueue.SwarmRequest(stream="S2", requested_by="b", eur_ora=100)]
        winner, queued = flowqueue.admit(reqs)
        self.assertEqual(winner.requested_by, "b")  # eur_ora piu' alto a parita' di stream
        self.assertEqual(len(queued), 1)

    def test_budget_guard_rejects_all_below_20_percent(self):
        reqs = [flowqueue.SwarmRequest(stream="S1", requested_by="a")]
        winner, queued = flowqueue.admit(reqs, budget_pct=15.0)
        self.assertIsNone(winner)
        self.assertEqual(len(queued), 1)


if __name__ == "__main__":
    unittest.main()
