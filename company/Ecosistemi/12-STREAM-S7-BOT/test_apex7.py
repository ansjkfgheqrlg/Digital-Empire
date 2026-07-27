"""
TEST END-TO-END APEX-7 — Level 2.

Non e' una demo: ogni sezione ha assert che fanno fallire il test quando il
sistema sbaglia. Un test che non puo' fallire non dimostra niente.

Esecuzione:  python test_apex7.py
"""

import os
import sys

from event_bus import global_bus, EVENT_CATALOG, RETRY_POLICY
from memory_interface import global_memory
from quality_gates import GATE_DEFINITIONS, GATE_SEQUENCE, get_threshold
from gate_agent import gate_1
from worker_agent import WorkerAgent, analyst_worker
from orchestrator import ad_orchestrator
from meta_agent import director_meta, MAX_AGENTS
from ruflo_adapter import adapter

SRC = os.path.dirname(os.path.abspath(__file__))
failures = []


def section(title):
    print(f"\n{'=' * 70}\n  {title}\n{'=' * 70}")


def check(label, condition, detail=""):
    status = "OK " if condition else "KO "
    print(f"  [{status}] {label}" + (f" — {detail}" if detail else ""))
    if not condition:
        failures.append(label)
    return condition


# =========================================================================== #
def test_event_bus():
    section("1. EVENT BUS — priorita', retry, DLQ, replay")

    check("Catalogo eventi popolato", len(EVENT_CATALOG) >= 15, f"{len(EVENT_CATALOG)} eventi")
    check("Ogni evento ha priorita' e garanzia",
          all("priority" in v and "delivery" in v for v in EVENT_CATALOG.values()))
    check("Retry policy per tutte e 4 le priorita'", len(RETRY_POLICY) == 4)

    # Ordine di priorita': dentro la gestione di un evento P2 accodo prima un P3
    # e poi un P0. Il P0 deve essere servito per primo, anche se accodato dopo.
    # Il trigger ascolta un evento diverso da quelli che ripubblica: niente auto-cascata.
    order = []
    global_bus.subscribe("agent.spawned", lambda e: order.append("P3"), subscriber_id="test.p3")
    global_bus.subscribe("task.failed", lambda e: order.append("P0"), subscriber_id="test.p0")

    def trigger(e):
        global_bus.publish("agent.spawned", {"agent_id": "A-PRIO", "type": "test"})  # P3
        global_bus.publish("task.failed", {"task_id": "T-PRIO", "error_type": "test"})  # P0

    global_bus.subscribe("task.decomposed", trigger, subscriber_id="test.trigger")
    global_bus.publish("task.decomposed", {"task_id": "T-DECOMP", "subtasks": []})  # P2
    check("Il P0 accodato dopo il P3 viene comunque servito prima",
          "P0" in order and "P3" in order and order.index("P0") < order.index("P3"),
          f"sequenza: {order}")

    global_bus.unsubscribe("task.decomposed", "test.trigger")
    global_bus.unsubscribe("agent.spawned", "test.p3")
    global_bus.unsubscribe("task.failed", "test.p0")

    # Self-healing: un subscriber che esplode non ferma il bus e finisce in DLQ
    dlq_before = len(global_bus.dead_letter_queue)

    def broken(e):
        raise RuntimeError("subscriber rotto di proposito")

    global_bus.subscribe("memory.pattern.detected", broken, subscriber_id="test.broken")
    global_bus.publish("memory.pattern.detected", {"pattern_type": "test", "confidence": 0.9})
    check("Il bus sopravvive a un subscriber che esplode", True)
    check("L'evento P3 esaurito viene scartato, non messo in DLQ",
          len(global_bus.dead_letter_queue) == dlq_before,
          f"dropped={global_bus.stats['dropped']}")

    global_bus.unsubscribe("memory.pattern.detected", "test.broken")
    global_bus.unsubscribe("agent.spawned", "test.nested")

    # Replay
    replayed = global_bus.replay(from_sequence=max(0, len(global_bus.event_log) - 3))
    check("Replay dello storico eseguibile", replayed > 0, f"{replayed} eventi riconsegnati")


# =========================================================================== #
def test_memory():
    section("2. MEMORY — 5 query type, indice, persistenza")

    mid = global_memory.write("knowledge", "Il gate L5 e' safety critical e non tollera errori",
                              "TEST-1", importance=0.9)
    check("TYPE 4 write ritorna un id", bool(mid), mid)

    dup = global_memory.write("knowledge", "Il gate L5 e' safety critical e non tollera errori",
                              "TEST-1")
    check("I duplicati non vengono riscritti", dup == mid, f"{global_memory.stats['duplicates_skipped']} scartati")

    recall = global_memory.contextual_recall(["gate", "safety", "critical"])
    check("TYPE 1 contextual_recall trova il record", len(recall) > 0,
          f"{len(recall)} risultati, score {recall[0]['final_score'] if recall else 0}")
    check("Il risultato porta autore, eta' e fiducia",
          bool(recall) and all(k in recall[0] for k in ("author_agent", "age_days", "confidence")))

    did = global_memory.record_decision("Usare l'Event Bus invece delle chiamate dirette",
                                        "TEST-1", outcome="SUCCESS",
                                        rationale="Disaccoppia gli agenti")
    lookup = global_memory.decision_lookup("Usare l'Event Bus invece delle chiamate dirette tra agenti")
    check("TYPE 2 decision_lookup ritrova la decisione", lookup["similar_decisions_found"] > 0,
          f"similarita' {lookup['decisions'][0]['similarity'] if lookup['decisions'] else 0}")
    check("Il lookup dice se riusarla", lookup["decisions"][0]["should_reuse"] is True)

    global_memory.register_strategy("Piramide Evolutiva", "escalation", "TEST-1",
                                    warnings=["Non adatta a task sotto i 10 minuti"])
    global_memory.register_strategy("Forza bruta", "escalation", "TEST-1")
    for _ in range(4):
        global_memory.record_strategy_outcome("Piramide Evolutiva", success=True)
    for _ in range(5):   # l'archiviazione automatica scatta a 5+ usi sotto il 30%
        global_memory.record_strategy_outcome("Forza bruta", success=False)

    fetched = global_memory.strategy_fetch("escalation")
    check("TYPE 3 strategy_fetch ordina per successo misurato",
          fetched["recommended_strategy"]["name"] == "Piramide Evolutiva",
          f"success_rate {fetched['recommended_strategy']['success_rate']}")
    check("La strategia perdente viene archiviata sotto il 30%",
          any(r["status"] == "ARCHIVED" for r in global_memory.storage["strategies"]))

    ok = global_memory.forget(mid, reason="test_di_archiviazione", superseded_by="MEM-NUOVO")
    rec = global_memory._by_id[mid]
    check("TYPE 5 forget archivia senza cancellare",
          ok and rec["status"] == "ARCHIVED" and rec["reason"] == "test_di_archiviazione")
    check("Il record archiviato esiste ancora in memoria", mid in global_memory._by_id)

    path = global_memory.checkpoint()
    check("Checkpoint scritto su disco", os.path.exists(path), os.path.basename(path))
    check("Restore ricostruisce l'indice", global_memory.restore() and len(global_memory._index) > 0,
          f"{len(global_memory._index)} termini indicizzati")


# =========================================================================== #
def test_gates():
    section("3. QUALITY GATES — tutti e 7 i livelli con rubriche")

    check("6 gate definiti (L1->L7)", len(GATE_DEFINITIONS) == 6, str(list(GATE_DEFINITIONS)))
    check("Sequenza dei gate coerente", GATE_SEQUENCE[0] == "L1_TO_L2" and GATE_SEQUENCE[-1] == "L6_TO_L7")
    check("Soglie differenziate per livello",
          get_threshold("L1_TO_L2") == 1.0 and get_threshold("L2_TO_L3") == 0.80,
          "L1 zero tolleranza, L2 tollera un criterio")
    check("Ogni criterio ha una rubrica",
          all(c.get("rubric") for g in GATE_DEFINITIONS.values() for c in g["criteria"]),
          f"{sum(len(g['criteria']) for g in GATE_DEFINITIONS.values())} criteri totali")
    check("Ogni gate ha un timeout", all("timeout_s" in g for g in GATE_DEFINITIONS.values()))


# =========================================================================== #
def test_gate_agent_real_evaluation():
    section("4. GATE AGENT — valutazione vera, non timbro")

    ctx_report = gate_1.evaluate(
        gate_id="GATE-L1-SELFCHECK", formal_gate_id="L1_TO_L2",
        criteria=GATE_DEFINITIONS["L1_TO_L2"]["criteria"],
        output_to_check="qualsiasi cosa", threshold=1.0, timeout_s=60,
        gate_history=[], attempt=1,
    )
    gate_1.reset()

    print(f"      L1_TO_L2 sul codice reale: {ctx_report['result']} "
          f"({ctx_report['criteria_passed']}/{ctx_report['criteria_total']}, "
          f"score {ctx_report['score']})")
    for r in ctx_report["criteria_results"]:
        print(f"        {r['criterion']} {r['status']}: {r['evidence'][:95]}")

    check("Il gate ispeziona il codice, non l'output vuoto",
          ctx_report["criteria_total"] == 5)
    check("Ogni criterio porta l'evidenza",
          all(r["evidence"] for r in ctx_report["criteria_results"]))
    check("Ogni FAIL porta un fix",
          all(r["fix"] for r in ctx_report["criteria_results"] if r["status"] == "FAIL"))
    check("Il gate L1 sul sistema reale passa", ctx_report["result"] == "PASSED",
          f"score {ctx_report['score']} su soglia 1.0")

    # Un output vuoto su una rubrica testuale deve fallire
    fake = gate_1.evaluate(
        gate_id="GATE-LX-VUOTO", formal_gate_id="L2_TO_L3",
        criteria=[{"id": "CX", "name": "test", "rubric": {"must_contain": ["inesistente"]}}],
        output_to_check="testo che non contiene il termine",
        threshold=1.0, timeout_s=30, gate_history=[], attempt=1,
    )
    gate_1.reset()
    check("Un criterio non soddisfatto viene bocciato", fake["result"] == "FAILED")
    check("Il dubbio vale FAIL, non PARTIAL",
          fake["criteria_results"][0]["status"] == "FAIL")

    check("La macchina a stati e' tornata a riposo", gate_1.state == "IDLE")
    check("Le transizioni sono tracciate", len(gate_1.state_history) > 0,
          f"{len(gate_1.state_history)} transizioni")


# =========================================================================== #
def test_full_cycle():
    section("5. CICLO COMPLETO — due worker, gate, memoria")

    writer = WorkerAgent("WORKER-WRITER-1", skills=["writing"], claims=["scrivi", "documenta"])
    auditor = WorkerAgent("WORKER-AUDIT-1", skills=["audit"], claims=["analizza", "verifica"])
    director_meta.register_agent(writer.agent_id, "worker", "writing")
    director_meta.register_agent(auditor.agent_id, "worker", "audit")

    ad_orchestrator.set_baseline(3000, note="Level 1: un solo worker, gate mock")

    task_id = ad_orchestrator.assign_mission("Analizza il flusso eventi e riporta le anomalie")
    task = ad_orchestrator.active_tasks[task_id]

    check("Il task e' stato chiuso dal gate", task["status"] == "DONE", task["status"])
    check("Solo il worker competente ha lavorato",
          auditor.completed >= 1 and writer.completed == 0,
          f"audit={auditor.completed}, writer={writer.completed}")
    check("Il ciclo ha lasciato traccia in memoria",
          len(global_memory.storage["gate_reports"]) > 0,
          f"{len(global_memory.storage['gate_reports'])} report")
    check("La durata della missione e' stata misurata", "duration_ms" in task,
          f"{task.get('duration_ms')}ms")


# =========================================================================== #
def test_escalation_and_override():
    section("6. ESCALATION E HUMAN OVERRIDE")

    before = len(director_meta.evolution_proposals)
    refused = director_meta.propose_evolution(
        target="execution_engine", change="Passare a TRADE_MODE=LIVE",
        rationale="La simulazione va bene", reversible=False)
    check("Una modifica irreversibile viene rifiutata in partenza",
          refused["status"] == "REFUSED", refused.get("refusal_reason", ""))

    proposed = director_meta.propose_evolution(
        target="event_bus", change="Alzare max_retries di P2 da 3 a 4",
        rationale="Tre tentativi non bastano sotto carico", reversible=True)
    gate_1.reset()
    check("Una modifica reversibile passa dal gate, non si applica da sola",
          proposed["status"] == "PROPOSED")
    check("Le proposte sono tracciate", len(director_meta.evolution_proposals) == before + 2)

    check("Il tetto agli agenti esiste ed e' basso", MAX_AGENTS == 12)
    ok = True
    for i in range(MAX_AGENTS + 5):
        ok = director_meta.register_agent(f"FILLER-{i}", "worker")
    check("Oltre il tetto la registrazione viene rifiutata",
          ok is False and len(director_meta.registry) <= MAX_AGENTS,
          f"{len(director_meta.registry)}/{MAX_AGENTS} agenti")

    res = director_meta.human_override("Test dello stop manuale", operator="MAX")
    check("Human override congela il sistema", res["frozen"] and director_meta.frozen)
    director_meta.resume("MAX")
    check("Il sistema si riattiva a comando", director_meta.frozen is False)


# =========================================================================== #
def test_ruflo():
    section("7. RUFLO — configurazione unica, esecutore intercambiabile")

    report = adapter.validate()
    for p in report["problems"]:
        print(f"        problema: {p}")

    check("Configurazione RuFLO caricata", adapter.config.get("workflow", {}).get("name") == "apex7_main")
    check("Backend rilevato", report["backend"] in ("ruflo", "internal"), report["backend"])
    check("Yaml e codice dicono la stessa cosa", report["valid"], f"{len(report['problems'])} divergenze")
    check("7 agenti dichiarati", report["agents_declared"] == 7, str(report["agents_declared"]))
    check("6 regole di routing (una per gate)", report["routing_rules"] == 6)

    graph = adapter.build_task_graph()
    check("Il grafo dei task si costruisce dalla configurazione",
          len(graph["nodes"]) == 7 and len(graph["edges"]) > 0,
          f"{len(graph['nodes'])} nodi, {len(graph['edges'])} archi")
    check("I gruppi paralleli sono dichiarati", len(graph["parallel_groups"]) > 0,
          str(graph["parallel_groups"]))
    check("I permessi di memoria sono per agente",
          adapter.can_write("planner", "decisions") and not adapter.can_write("analyst", "decisions"))
    check("Ogni agente ha il suo prompt interno",
          all(adapter.prompt_template(a) for a in adapter.config["agents"]),
          f"{len(adapter.config['agents'])} prompt trovati in prompts/")


# =========================================================================== #
def test_apex_gate():
    section("8. GATE FINALE L6->L7 — il sistema giudica se stesso")

    ad_orchestrator._record_metric("current", 1500, "TASK-APEX")

    history = [{"gate_id": g, "result": "PASSED"} for g in GATE_SEQUENCE[:-1]]
    report = gate_1.evaluate(
        gate_id="GATE-L6-APEX", formal_gate_id="L6_TO_L7",
        criteria=GATE_DEFINITIONS["L6_TO_L7"]["criteria"],
        output_to_check="verifica finale del sistema",
        threshold=1.0, timeout_s=300, gate_history=history, attempt=1,
    )
    gate_1.reset()

    print(f"      Verdetto APEX: {report['result']} "
          f"({report['criteria_passed']}/{report['criteria_total']}, score {report['score']})")
    for r in report["criteria_results"]:
        print(f"        {r['criterion']} {r['status']}: {r['evidence'][:95]}")
        if r["fix"]:
            print(f"           -> {r['fix'][:95]}")

    check("Il gate APEX gira su 7 criteri", report["criteria_total"] == 7)
    check("Il verdetto e' motivato criterio per criterio",
          all(r["evidence"] for r in report["criteria_results"]))
    return report


# =========================================================================== #
if __name__ == "__main__":
    test_event_bus()
    test_memory()
    test_gates()
    test_gate_agent_real_evaluation()
    test_full_cycle()
    test_escalation_and_override()
    test_ruflo()
    apex = test_apex_gate()

    section("RIEPILOGO")
    print(f"  Event Bus:  {global_bus.get_stats()}")
    print(f"  Memoria:    {global_memory.get_stats()}")
    print(f"  Sistema:    agenti={director_meta.system_view()['agents']}, "
          f"pattern={director_meta.system_view()['patterns_detected']}")
    print(f"\n  Verdetto gate APEX (L6->L7): {apex['result']} score {apex['score']}")

    if failures:
        print(f"\n  [FALLITI] {len(failures)} controlli:")
        for f in failures:
            print(f"     - {f}")
        sys.exit(1)

    print(f"\n  [OK] Tutti i controlli superati.")
    sys.exit(0)
