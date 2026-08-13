"""
Suite dell'APEX-7 Orchestration Layer.

Meta' di questi test non verifica che il sistema funzioni: verifica che
RIFIUTI. Il difetto originale dello zip `apex7_orchestrator` era esattamente
questo — gate che certificavano al 100% mentre L6 non girava mai e gli input
assurdi passavano indisturbati. Ogni test marcato REGRESSIONE riproduce uno
di quei difetti e pretende che qui venga bloccato.

    python test_orchestration.py
"""
import asyncio
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from orchestration import (
    AuditFinding,
    ComputationNode,
    InstrumentedEventBus,
    DAGCycleError,
    DAGEngine,
    DAGMissingDependencyError,
    GateBlocked,
    GateCheck,
    GateLedger,
    GateResult,
    OrchestrationPipeline,
    Outcome,
    QualityReport,
    REQUIRED_GATE_IDS,
    SelfEvolutionSafetyGuard,
    SelfHealingEngine,
    StateSnapshot,
    gate_l1_foundation,
    gate_l2_dag,
    gate_l3_bus_memory,
    gate_l4_swarm,
    gate_l5_quality,
    gate_l6_evolution,
    gate_l7_apex,
    instrument,
    topological_order,
    verify_chain,
)
from orchestrator.ruflo_core import DynamicWorkflowRouter, EventBus, RuFLOOrchestrator


# ─────────────────────────────────────────────────────────────────────────────
# Agenti fittizi ma non-mock: restituiscono output reali e deterministici
# ─────────────────────────────────────────────────────────────────────────────

class StubAgent:
    def __init__(self, nome, payload):
        self.name = nome
        self._payload = payload

    async def execute(self, payload):
        return dict(self._payload)


def orchestratore_di_prova(score=8.0):
    orch = RuFLOOrchestrator()
    for ruolo, out in {
        "planner": {"stages": ["INTAKE", "OUTPUT"]},
        "analyst": {"pattern": "nessuna anomalia"},
        "writer": {"content": "bozza"},
        "critic": {"score": score, "weaknesses": []},
        "refiner": {"content": "bozza rifinita"},
        "meta": {"saved": True},
    }.items():
        orch.register_agent(ruolo, StubAgent(ruolo, out))
    return orch


# ─────────────────────────────────────────────────────────────────────────────

class TestCatenaDiStato(unittest.TestCase):
    def test_catena_intatta_verifica(self):
        a = StateSnapshot.create("ROOT", {"x": 1})
        b = a.chain_to("FASE_1", {"y": 2})
        c = b.chain_to("FASE_2", {"z": 3})
        self.assertTrue(verify_chain((a, b, c)))

    def test_catena_manomessa_non_verifica(self):
        a = StateSnapshot.create("ROOT", {"x": 1})
        b = a.chain_to("FASE_1", {"y": 2})
        intruso = StateSnapshot.create("FASE_2", {"z": 3}, parent_hash="0" * 64)
        self.assertFalse(verify_chain((a, b, intruso)))

    def test_snapshot_e_immutabile(self):
        a = StateSnapshot.create("ROOT", {"x": 1})
        with self.assertRaises(Exception):
            a.state_hash = "altro"


class TestDAG(unittest.TestCase):
    @staticmethod
    def _somma(inputs, upstream):
        return {"valore": float(inputs.get("n", 0)) + 1.0}

    def test_ordine_topologico_rispetta_le_dipendenze(self):
        nodi = {
            "c": ComputationNode("c", ["b"], self._somma),
            "b": ComputationNode("b", ["a"], self._somma),
            "a": ComputationNode("a", [], self._somma),
        }
        self.assertEqual(topological_order(nodi), ["a", "b", "c"])

    def test_ciclo_scoperto_prima_di_eseguire(self):
        nodi = [
            ComputationNode("a", ["b"], self._somma),
            ComputationNode("b", ["a"], self._somma),
        ]
        with self.assertRaises(DAGCycleError):
            DAGEngine(nodi)

    def test_dipendenza_inesistente_bloccata(self):
        with self.assertRaises(DAGMissingDependencyError):
            DAGEngine([ComputationNode("a", ["fantasma"], self._somma)])

    def test_circuit_breaker_degrada_invece_di_far_cadere_il_grafo(self):
        def esplode(inputs, upstream):
            raise ValueError("boom")

        motore = DAGEngine([
            ComputationNode("rotto", [], esplode, fallback_fn=lambda i: {"valore": -1.0}),
            ComputationNode("sano", [], self._somma),
        ])
        res, _ = motore.execute({"n": 1})
        self.assertEqual(res["rotto"].status, "DEGRADED")
        self.assertTrue(res["rotto"].fallback_applied)
        self.assertEqual(res["sano"].status, "SUCCESS")

    def test_REGRESSIONE_nodo_con_dipendenza_rotta_non_sparisce(self):
        """Il DAG dello zip lasciava cadere in silenzio i nodi non risolvibili."""
        def esplode(inputs, upstream):
            raise ValueError("boom")

        motore = DAGEngine([
            ComputationNode("padre", [], esplode),
            ComputationNode("figlio", ["padre"], self._somma),
        ])
        res, _ = motore.execute({})
        self.assertIn("figlio", res, "il nodo dipendente e' sparito dal risultato")
        self.assertEqual(res["figlio"].status, "BLOCKED")
        self.assertEqual(res["padre"].status, "FAILED")

    def test_valori_non_finiti_rilevati(self):
        motore = DAGEngine([ComputationNode("nan", [], lambda i, u: {"v": float("nan")})])
        res, _ = motore.execute({})
        self.assertEqual(motore.non_finite_outputs(res), ["nan.v=nan"])


class TestContrattoDeiGate(unittest.TestCase):
    def test_gate_senza_check_e_rifiutato(self):
        with self.assertRaises(ValueError):
            GateResult.build("VUOTO", 1, 1.0, ())

    def test_REGRESSIONE_un_check_fallito_impedisce_il_pass(self):
        """Niente 'score alto quindi passa': un solo check rosso blocca."""
        checks = tuple(GateCheck(f"C{i}", "prova", True) for i in range(9))
        checks += (GateCheck("C9", "prova rossa", False, "motivo"),)
        res = GateResult.build("PROVA", 1, 0.85, checks)
        self.assertAlmostEqual(res.score, 0.9)
        self.assertFalse(res.passed, "score 90% sopra soglia 85% ma con un check rosso")


class TestGateBloccanti(unittest.TestCase):
    def test_l1_blocca_campo_obbligatorio_mancante(self):
        radice = StateSnapshot.create("ROOT", {"a": 1})
        ingresso = radice.chain_to("INPUT", {"task": "x"})
        res = gate_l1_foundation([radice, ingresso], {"task": "x"}, required_fields=["capitale"])
        self.assertFalse(res.passed)
        self.assertIn("C1.3", [c.check_id for c in res.failures])

    def test_l1_blocca_valore_non_finito(self):
        radice = StateSnapshot.create("ROOT", {"a": 1})
        payload = {"task": "x", "n": float("inf")}
        ingresso = radice.chain_to("INPUT", payload)
        res = gate_l1_foundation([radice, ingresso], payload, numeric_fields=["n"])
        self.assertFalse(res.passed)
        self.assertIn("C1.4", [c.check_id for c in res.failures])

    def test_l2_blocca_nodo_critico_caduto(self):
        motore = DAGEngine([ComputationNode("k", [], lambda i, u: (_ for _ in ()).throw(ValueError("x")))])
        res_dag, _ = motore.execute({})
        res = gate_l2_dag(res_dag, critical_nodes=["k"])
        self.assertFalse(res.passed)

    def test_l3_blocca_con_dlq_non_vuota(self):
        bus = InstrumentedEventBus()
        bus.subscribe("evento", lambda e: (_ for _ in ()).throw(RuntimeError("handler rotto")))
        bus.publish_sync("evento", {"x": 1})
        self.assertEqual(bus.dlq_size, 1)
        res = gate_l3_bus_memory(bus, None)
        self.assertFalse(res.passed)
        self.assertIn("C3.1", [c.check_id for c in res.failures])

    def test_l4_blocca_ruolo_mancante(self):
        res = gate_l4_swarm(["planner"], ["planner", "critic"], {"out": 1})
        self.assertFalse(res.passed)
        self.assertIn("C4.1", [c.check_id for c in res.failures])

    def test_REGRESSIONE_l4_blocca_output_tutto_mock(self):
        """Lo swarm dello zip restituiva dict scritti a mano e passava lo stesso."""
        res = gate_l4_swarm(
            ["planner"], ["planner"],
            {"planner_output": {"mock": True, "content": "Mock output"}},
        )
        self.assertFalse(res.passed)
        self.assertIn("C4.5", [c.check_id for c in res.failures])

    def test_l5_blocca_score_sotto_soglia(self):
        rep = QualityReport(score=4.0, threshold=7.5,
                            audits=(AuditFinding("A", False),), min_audits=1)
        self.assertFalse(gate_l5_quality(rep).passed)

    def test_l5_blocca_audit_critico(self):
        rep = QualityReport(score=9.0, threshold=7.5,
                            audits=(AuditFinding("A", True, "CRITICAL", "grave"),), min_audits=1)
        res = gate_l5_quality(rep)
        self.assertFalse(res.passed)
        self.assertIn("C5.2", [c.check_id for c in res.failures])

    def test_l5_blocca_probabilita_che_non_fanno_100(self):
        rep = QualityReport(
            score=9.0, threshold=7.5, audits=(AuditFinding("A", False),), min_audits=1,
            outcomes=(Outcome("BEST", 30.0, 10.0), Outcome("BASE", 30.0, 5.0)),
        )
        res = gate_l5_quality(rep)
        self.assertFalse(res.passed)
        self.assertIn("C5.4", [c.check_id for c in res.failures])

    def test_l5_blocca_distribuzione_piatta(self):
        rep = QualityReport(
            score=9.0, threshold=7.5, audits=(AuditFinding("A", False),), min_audits=1,
            outcomes=(Outcome("BEST", 50.0, 7.0), Outcome("WORST", 50.0, 7.0)),
        )
        res = gate_l5_quality(rep)
        self.assertFalse(res.passed)
        self.assertIn("C5.8", [c.check_id for c in res.failures])

    def test_l5_non_emette_check_di_calibrazione_senza_esiti(self):
        """Un check che non si applica non viene emesso 'passato': non viene emesso."""
        rep = QualityReport(score=9.0, threshold=7.5,
                            audits=(AuditFinding("A", False),), min_audits=1)
        ids = [c.check_id for c in gate_l5_quality(rep).checks]
        self.assertNotIn("C5.4", ids)
        self.assertEqual(ids, ["C5.1", "C5.2", "C5.3"])


class TestEvoluzione(unittest.TestCase):
    def test_invariante_mai_mutato_e_richiede_override_umano(self):
        exp = SelfEvolutionSafetyGuard.evaluate(
            "gate_l1_foundation", {"overall_score": 0.5}, {"overall_score": 5.0})
        self.assertEqual(exp.status, "REJECTED")
        self.assertTrue(exp.human_override_required)

    def test_regressione_viene_riportata_indietro(self):
        exp = SelfEvolutionSafetyGuard.evaluate(
            "tuning", {"overall_score": 1.0}, {"overall_score": 0.5})
        self.assertEqual(exp.status, "ROLLED_BACK")

    def test_miglioramento_nel_rumore_non_si_adotta(self):
        exp = SelfEvolutionSafetyGuard.evaluate(
            "tuning", {"overall_score": 1.0}, {"overall_score": 1.01})
        self.assertEqual(exp.status, "REJECTED")

    def test_REGRESSIONE_l6_blocca_se_non_e_mai_stato_interrogato(self):
        """Nello zip L6 era importato e mai chiamato, e nessuno se ne accorgeva."""
        res = gate_l6_evolution([])
        self.assertFalse(res.passed)
        self.assertIn("C6.1", [c.check_id for c in res.failures])


class TestGateL7(unittest.TestCase):
    @staticmethod
    def _verde(gate_id, level):
        return GateResult.build(gate_id, level, 0.5, (GateCheck("C", "ok", True),))

    def _tutti_verdi(self):
        return {g: self._verde(g, i + 1) for i, g in enumerate(REQUIRED_GATE_IDS)}

    def test_certifica_quando_tutto_e_a_posto(self):
        res = gate_l7_apex(self._tutti_verdi(), e2e_duration_ms=10.0)
        self.assertTrue(res.passed, res.failures)

    def test_REGRESSIONE_blocca_se_l6_non_e_stato_eseguito(self):
        """Il difetto centrale dello zip: L7 controllava solo L1..L5."""
        gate = self._tutti_verdi()
        del gate["GATE_L6_EVOLUTION"]
        res = gate_l7_apex(gate, e2e_duration_ms=10.0)
        self.assertFalse(res.passed)
        self.assertIn("C7.1", [c.check_id for c in res.failures])

    def test_blocca_oltre_lo_sla(self):
        res = gate_l7_apex(self._tutti_verdi(), e2e_duration_ms=900.0, sla_ms=500.0)
        self.assertFalse(res.passed)
        self.assertIn("C7.4", [c.check_id for c in res.failures])

    def test_blocca_con_self_healing_irrisolto(self):
        healing = SelfHealingEngine()
        healing.handle_failure("Timeout", "modulo", lambda: False, "nessun fallback")
        res = gate_l7_apex(self._tutti_verdi(), e2e_duration_ms=10.0,
                           unresolved_healing=healing.unresolved)
        self.assertFalse(res.passed)
        self.assertIn("C7.6", [c.check_id for c in res.failures])


class TestLedger(unittest.TestCase):
    def test_REGRESSIONE_non_certifica_con_gate_mancanti(self):
        """Il report dello zip stampava '100% PASS L1-L7' da stringa fissa."""
        ledger = GateLedger()
        ledger.record(GateResult.build("GATE_L1_FOUNDATION", 1, 0.5, (GateCheck("C", "ok", True),)))
        self.assertFalse(ledger.certified)
        self.assertIn("NON CERTIFICATO", ledger.render())
        self.assertIn("gate mai eseguiti", ledger.render())

    def test_record_bloccante_solleva(self):
        ledger = GateLedger()
        rosso = GateResult.build("GATE_X", 1, 1.0, (GateCheck("C", "ko", False, "motivo"),))
        with self.assertRaises(GateBlocked):
            ledger.record(rosso)
        self.assertIn("GATE_X", ledger.results)


class TestEventBusStrumentato(unittest.TestCase):
    def test_consegna_riuscita_non_sporca_la_dlq(self):
        bus = InstrumentedEventBus()
        visti = []
        bus.subscribe("ok", visti.append)
        bus.publish_sync("ok", {"a": 1})
        self.assertEqual(len(visti), 1)
        self.assertEqual(bus.dlq_size, 0)
        self.assertEqual(bus.failed_deliveries, [])

    def test_handler_che_solleva_finisce_in_dlq(self):
        bus = InstrumentedEventBus()
        bus.subscribe("ko", lambda e: (_ for _ in ()).throw(RuntimeError("rotto")))
        bus.publish_sync("ko", {"a": 1})
        self.assertEqual(bus.dlq_size, 1)
        self.assertEqual(len(bus.failed_deliveries), 1)

    def test_async_publish_registra_i_fallimenti(self):
        bus = InstrumentedEventBus()
        bus.subscribe("ko", lambda e: (_ for _ in ()).throw(RuntimeError("rotto")))
        asyncio.run(bus.publish("ko", {"a": 1}))
        self.assertEqual(bus.dlq_size, 1)

    def test_REGRESSIONE_il_bus_nudo_perde_i_fallimenti(self):
        """Perche' il layer strumenta il bus: quello del motore non registra nulla."""
        nudo = EventBus()
        nudo.subscribe("ko", lambda e: (_ for _ in ()).throw(RuntimeError("rotto")))
        nudo.publish_sync("ko", {"a": 1})
        self.assertFalse(hasattr(nudo, "dead_letter_queue"))
        self.assertEqual(getattr(nudo, "dlq_size", 0), 0)

    def test_instrument_preserva_le_sottoscrizioni_esistenti(self):
        orch = RuFLOOrchestrator()
        sottoscrizioni_prima = set(orch.event_bus.subscribers)
        bus = instrument(orch)
        self.assertIsInstance(bus, InstrumentedEventBus)
        self.assertIs(orch.event_bus, bus)
        self.assertTrue(sottoscrizioni_prima.issubset(set(bus.subscribers)))
        self.assertIs(instrument(orch), bus, "instrument deve essere idempotente")


class TestPipelineIntegrata(unittest.TestCase):
    def test_run_completo_certifica_tutti_e_sette_i_gate(self):
        pipeline = OrchestrationPipeline(orchestratore_di_prova(score=8.0), memory=None)
        esito = pipeline.run_sync("progetta un carosello", sla_ms=60_000.0)

        self.assertIsNone(esito.blocked_at, esito.ledger.render())
        self.assertTrue(esito.certified, esito.ledger.render())
        eseguiti = set(esito.ledger.results)
        self.assertEqual(eseguiti, set(REQUIRED_GATE_IDS) | {"GATE_L7_APEX"})
        self.assertIn("GATE_L6_EVOLUTION", eseguiti, "L6 non e' stato eseguito")
        self.assertIn("CERTIFICATO", esito.ledger.render())

    def test_REGRESSIONE_l6_gira_davvero_dentro_la_pipeline(self):
        pipeline = OrchestrationPipeline(orchestratore_di_prova(), memory=None)
        esito = pipeline.run_sync("task", sla_ms=60_000.0)
        self.assertTrue(esito.experiments, "la guardia di evoluzione non e' stata interrogata")
        stati = {e.status for e in esito.experiments}
        self.assertIn("REJECTED", stati)      # invariante protetto
        self.assertIn("ROLLED_BACK", stati)   # regressione riportata indietro

    def test_catena_di_stato_intatta_a_fine_run(self):
        pipeline = OrchestrationPipeline(orchestratore_di_prova(), memory=None)
        esito = pipeline.run_sync("task", sla_ms=60_000.0)
        self.assertTrue(verify_chain(tuple(esito.chain)))
        self.assertGreaterEqual(len(esito.chain), 5)

    def test_pipeline_si_ferma_al_gate_che_non_passa(self):
        pipeline = OrchestrationPipeline(orchestratore_di_prova(), memory=None)
        esito = pipeline.run_sync("task", required_fields=["campo_inesistente"], sla_ms=60_000.0)
        self.assertEqual(esito.blocked_at, "GATE_L1_FOUNDATION")
        self.assertFalse(esito.certified)
        self.assertNotIn("GATE_L7_APEX", esito.ledger.results)

    def test_qualita_scadente_blocca_a_l5(self):
        # score 5.0: sotto soglia ma sopra 4.0, cosi' il router raffina invece
        # di far ripartire il workflow (vedi TestDifettiDelMotore piu' sotto).
        pipeline = OrchestrationPipeline(orchestratore_di_prova(score=5.0), memory=None)
        esito = pipeline.run_sync("task", quality_threshold=7.5, sla_ms=60_000.0)
        self.assertEqual(esito.blocked_at, "GATE_L5_QUALITY")

    def test_sla_superato_blocca_a_l7(self):
        pipeline = OrchestrationPipeline(orchestratore_di_prova(), memory=None)
        esito = pipeline.run_sync("task", sla_ms=0.001)
        self.assertEqual(esito.blocked_at, "GATE_L7_APEX")

    def test_ruolo_non_registrato_blocca_a_l4(self):
        orch = orchestratore_di_prova()
        del orch.agents_registry["critic"]
        esito = OrchestrationPipeline(orch, memory=None).run_sync("task", sla_ms=60_000.0)
        self.assertEqual(esito.blocked_at, "GATE_L4_SWARM")


class TestConsumatoreReale(unittest.TestCase):
    """
    `ArenaGenerator` (skill-forge, carousel-machine, cold-outreach) e' il
    consumatore di produzione agganciato alla pipeline certificata. Qui si
    verifica la logica di salvataggio senza toccare il disco ne' Arena.
    """

    class _Esito:
        def __init__(self, certificato):
            self.certified = certificato
            self.blocked_at = None if certificato else "GATE_L5_QUALITY"

    @staticmethod
    def _generatore(strict):
        from arena_generator import ArenaGenerator
        g = ArenaGenerator.__new__(ArenaGenerator)   # niente I/O, niente Arena
        g.strict = strict
        return g

    def test_strict_impedisce_di_salvare_output_non_certificato(self):
        g = self._generatore(strict=True)
        self.assertTrue(g._blocca_scrittura("s", self._Esito(False)))
        self.assertFalse(g._blocca_scrittura("s", self._Esito(True)))

    def test_senza_strict_salva_ma_avvisa(self):
        g = self._generatore(strict=False)
        self.assertFalse(g._blocca_scrittura("s", self._Esito(False)))
        self.assertFalse(g._blocca_scrittura("s", self._Esito(True)))

    def test_i_tre_stream_passano_dalla_pipeline_certificata(self):
        """Nessuno stream deve chiamare execute_workflow direttamente."""
        import inspect
        import arena_generator
        sorgente = inspect.getsource(arena_generator.ArenaGenerator)
        self.assertNotIn(
            "self.orchestrator.execute_workflow", sorgente,
            "uno stream chiama ancora il workflow nudo, saltando i 7 gate",
        )
        for metodo in ("run_skill_forge", "_generate_single_slide", "run_cold_outreach"):
            corpo = inspect.getsource(getattr(arena_generator.ArenaGenerator, metodo))
            self.assertIn("_esegui_certificato", corpo, f"{metodo} non passa dai gate")


class TestDifettiDelMotore(unittest.TestCase):
    """
    Difetti PREESISTENTI di `orchestrator/ruflo_core.py`, trovati durante
    l'innesto e NON corretti qui (il motore condiviso non si tocca, ADR-003).
    Questi test li fissano perche' non vengano riscoperti da zero, e provano
    che l'orchestration layer li contiene invece di ereditarli.
    Riparazione tracciata in BACKLOG.md.
    """

    def test_DIFETTO_loop_count_non_accumula_fra_restart(self):
        """
        Causa della ricorsione infinita: `execute_workflow` genera un task_id
        nuovo a ogni giro, quindi il contatore del router riparte da zero e un
        punteggio < 4.0 fa ripartire il workflow per sempre. Qui si dimostra il
        difetto senza innescarlo.
        """
        router = DynamicWorkflowRouter()
        for _ in range(5):
            scelta = router.next_stage("CRITIQUE", {"critique_score": 2.0, "task_id": f"id-{_}"})
            self.assertEqual(scelta, "INTAKE", "con task_id sempre nuovo si riparte all'infinito")
        # con un task_id stabile il contatore accumula e il ciclo si chiude
        stabile = DynamicWorkflowRouter()
        scelte = [stabile.next_stage("CRITIQUE", {"critique_score": 2.0, "task_id": "fisso"})
                  for _ in range(5)]
        self.assertEqual(scelte[0], "INTAKE")
        self.assertIn("OUTPUT", scelte, "con id stabile il ciclo termina")

    def test_DIFETTO_print_non_ascii_nel_percorso_principale(self):
        """
        `execute_workflow` stampa '\\u2192': su console cp1252 solleva
        UnicodeEncodeError nel flusso normale. Il layer lo neutralizza con
        stdout_tollerante() invece di lasciarlo decidere l'esito di un run.
        """
        import io
        from orchestration import stdout_tollerante

        stretto = io.TextIOWrapper(io.BytesIO(), encoding="cp1252", errors="strict")
        with self.assertRaises(UnicodeEncodeError):
            stretto.write("[FLOW] → CRITIQUE")
            stretto.flush()

        pipeline = OrchestrationPipeline(orchestratore_di_prova(), memory=None)
        esito = pipeline.run_sync("task", sla_ms=60_000.0)
        self.assertTrue(esito.certified, esito.ledger.render())


if __name__ == "__main__":
    unittest.main(verbosity=2)
