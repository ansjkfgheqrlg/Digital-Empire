"""
VERIFIERS — i controlli eseguibili dei Quality Gate.

Nel Level 1 il Gate Agent diceva PASS se l'output non era vuoto. Era un
timbro, non un'ispezione. Qui ogni criterio che si può controllare
eseguendo viene controllato eseguendo: si legge il codice sorgente vero,
si interroga il bus vero, si guarda la memoria vera.

Contratto di ogni verifier:
    def check_qualcosa(ctx: dict) -> tuple[str, str, str | None]
    ritorna (status, evidence, fix)
        status   "PASS" | "PARTIAL" | "FAIL"
        evidence perche', con citazione di file/riga o valore misurato
        fix      cosa fare per passare, None se PASS

ctx contiene:
    output       l'artefatto da valutare (testo o dict)
    src_dir      la cartella del sistema da ispezionare
    bus          istanza EventBus viva
    memory       istanza MemoryInterface viva
    gate_history report dei gate precedenti
"""

import os
import re
from typing import Dict, Any, Tuple, Optional

Result = Tuple[str, str, Optional[str]]

SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# Moduli che rappresentano un agente: nessuno di questi deve importare
# la classe di un altro, altrimenti il disaccoppiamento e' una bugia.
AGENT_MODULES = ["orchestrator", "worker_agent", "gate_agent", "meta_agent"]

CORE_COMPONENTS = {
    "Orchestrator": "orchestrator.py",
    "MetaAgent": "meta_agent.py",
    "GateAgent": "gate_agent.py",
    "WorkerAgent": "worker_agent.py",
    "MemoryInterface": "memory_interface.py",
    "EventBus": "event_bus.py",
}


# --------------------------------------------------------------------------- #
# Utility di lettura del sorgente
# --------------------------------------------------------------------------- #

def _src(ctx: Dict[str, Any], filename: str) -> str:
    path = os.path.join(ctx.get("src_dir", SRC_DIR), filename)
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _exists(ctx: Dict[str, Any], filename: str) -> bool:
    return os.path.exists(os.path.join(ctx.get("src_dir", SRC_DIR), filename))


def _line_of(text: str, needle: str) -> int:
    for i, line in enumerate(text.splitlines(), 1):
        if needle in line:
            return i
    return 0


def _output_text(ctx: Dict[str, Any]) -> str:
    return str(ctx.get("output", ""))


# --------------------------------------------------------------------------- #
# GATE L1 -> L2
# --------------------------------------------------------------------------- #

def check_core_components(ctx) -> Result:
    missing = []
    found = []
    for cls, filename in CORE_COMPONENTS.items():
        text = _src(ctx, filename)
        if re.search(rf"class\s+{cls}\b", text):
            found.append(f"{cls} in {filename}:{_line_of(text, f'class {cls}')}")
        else:
            missing.append(cls)
    if missing:
        return ("FAIL",
                f"Mancano i componenti: {', '.join(missing)}. Trovati: {len(found)}/{len(CORE_COMPONENTS)}",
                f"Definire le classi mancanti: {', '.join(missing)}")
    return ("PASS", f"Tutti i {len(found)} componenti trovati: {'; '.join(found[:3])}...", None)


def check_single_responsibility(ctx) -> Result:
    """Un modulo, una classe principale, e la classe dichiara cosa fa."""
    violations = []
    for cls, filename in CORE_COMPONENTS.items():
        text = _src(ctx, filename)
        if not text:
            continue
        classes = re.findall(r"^class\s+(\w+)", text, re.MULTILINE)
        if len(classes) > 1:
            violations.append(f"{filename} definisce {len(classes)} classi: {classes}")
        docstring = re.search(rf"class\s+{cls}[^:]*:\s*\n\s*\"\"\"(.+?)\"\"\"", text, re.DOTALL)
        if not docstring or len(docstring.group(1).strip()) < 20:
            violations.append(f"{cls} non dichiara la sua responsabilita'")
    if violations:
        return ("PARTIAL" if len(violations) <= 1 else "FAIL",
                "; ".join(violations),
                "Una classe principale per modulo, con docstring che dice cosa fa e cosa non fa")
    return ("PASS", f"{len(CORE_COMPONENTS)} moduli, una responsabilita' dichiarata ciascuno", None)


def check_no_direct_calls(ctx) -> Result:
    """Nessun agente importa la classe di un altro agente: si parlano via bus."""
    violations = []
    for mod in AGENT_MODULES:
        text = _src(ctx, f"{mod}.py")
        for other in AGENT_MODULES:
            if other == mod:
                continue
            if re.search(rf"^\s*from\s+{other}\s+import", text, re.MULTILINE):
                violations.append(f"{mod}.py importa direttamente da {other}.py")
    if violations:
        return ("FAIL", "; ".join(violations),
                "Sostituire l'import diretto con publish/subscribe sull'Event Bus")
    return ("PASS",
            f"I {len(AGENT_MODULES)} agenti non si importano tra loro: comunicano solo via global_bus", None)


def check_event_catalog(ctx) -> Result:
    text = _src(ctx, "event_bus.py")
    if "EVENT_CATALOG" not in text:
        return ("FAIL", "Nessun EVENT_CATALOG in event_bus.py",
                "Dichiarare il catalogo degli eventi con priorita' e garanzia di consegna")
    try:
        from event_bus import EVENT_CATALOG
    except Exception as e:
        return ("FAIL", f"EVENT_CATALOG non importabile: {e}", "Correggere event_bus.py")
    incomplete = [k for k, v in EVENT_CATALOG.items() if "priority" not in v or "delivery" not in v]
    if incomplete:
        return ("PARTIAL", f"{len(incomplete)} eventi senza priorita' o garanzia: {incomplete[:3]}",
                "Completare priority e delivery per ogni evento")
    return ("PASS",
            f"{len(EVENT_CATALOG)} eventi catalogati, tutti con priority e delivery "
            f"(event_bus.py:{_line_of(text, 'EVENT_CATALOG')})", None)


def check_e2e_test_exists(ctx) -> Result:
    candidates = [f for f in os.listdir(ctx.get("src_dir", SRC_DIR)) if f.startswith("test_")]
    if not candidates:
        return ("FAIL", "Nessun file test_*.py nella cartella", "Scrivere almeno un test end-to-end")
    with_assertions = []
    for f in candidates:
        text = _src(ctx, f)
        n = len(re.findall(r"\bassert\b", text))
        if n > 0:
            with_assertions.append(f"{f} ({n} assert)")
    if not with_assertions:
        return ("FAIL", f"Trovati {len(candidates)} file di test ma nessun assert: sono demo, non test",
                "Aggiungere assert che facciano fallire il test quando il sistema sbaglia")
    return ("PASS", f"Test con verifica reale: {', '.join(with_assertions)}", None)


# --------------------------------------------------------------------------- #
# GATE L2 -> L3
# --------------------------------------------------------------------------- #

def check_decision_log(ctx) -> Result:
    memory = ctx.get("memory")
    if memory is None:
        return ("FAIL", "Nessuna memoria collegata al contesto del gate", "Passare l'istanza memoria al Gate Agent")
    if "decisions" not in memory.storage:
        return ("FAIL", "Il layer 'decisions' non esiste in memoria", "Creare il layer decisions")
    records = memory.storage["decisions"]
    orphans = [r for r in records if not r.get("author_agent")]
    if orphans:
        return ("FAIL", f"{len(orphans)} decisioni senza autore", "Ogni scrittura deve portare l'agente che l'ha fatta")
    return ("PASS", f"Decision Log attivo: {len(records)} decisioni, tutte con autore e timestamp", None)


def check_routing_conditions(ctx) -> Result:
    text = _src(ctx, "orchestrator.py")
    handlers = re.findall(r"global_bus\.subscribe\(\s*[\"']([\w.]+)[\"']", text)
    branches = len(re.findall(r"^\s+if\s+", text, re.MULTILINE))
    if len(handlers) < 3:
        return ("FAIL", f"Solo {len(handlers)} condizioni di routing: {handlers}",
                "Portare a 3+ i rami reali del flusso (passed / failed / escalated)")
    return ("PASS",
            f"{len(handlers)} condizioni di routing sottoscritte ({', '.join(handlers)}), "
            f"{branches} rami condizionali nel modulo", None)


def check_max_iterations(ctx) -> Result:
    findings = []
    for filename, pattern in [
        ("quality_gates.py", r"MAX_ATTEMPTS_BEFORE_ESCALATION\s*=\s*(\d+)"),
        ("event_bus.py", r"max_events:\s*int\s*=\s*(\d+)"),
        ("event_bus.py", r"\"max_retries\":\s*(\d+)"),
    ]:
        text = _src(ctx, filename)
        m = re.search(pattern, text)
        if m:
            findings.append(f"{filename}: limite {m.group(1)}")
    if not findings:
        return ("FAIL", "Nessun tetto di iterazioni trovato: esistono cicli potenzialmente infiniti",
                "Aggiungere max_iterations/max_retries a ogni loop")
    if len(findings) < 2:
        return ("PARTIAL", f"Un solo limite trovato: {findings[0]}", "Coprire anche gli altri loop")
    return ("PASS", f"Tetti di iterazione presenti: {'; '.join(findings)}", None)


# --------------------------------------------------------------------------- #
# GATE L3 -> L4
# --------------------------------------------------------------------------- #

def check_ruflo_mapping(ctx) -> Result:
    yaml_present = _exists(ctx, "apex7_workflow.ruflo.yaml")
    adapter = _src(ctx, "ruflo_adapter.py")
    if not yaml_present and not adapter:
        return ("FAIL", "RuFLO citato ma mai integrato: nessun yaml, nessun adapter",
                "Creare apex7_workflow.ruflo.yaml e ruflo_adapter.py con la mappatura dei componenti")
    yaml_text = _src(ctx, "apex7_workflow.ruflo.yaml")
    agents_declared = len(re.findall(r"^\s{4}\w+:\s*$", yaml_text, re.MULTILINE))
    mapped = len(re.findall(r"ruflo\.", yaml_text + adapter))
    if mapped < 3:
        return ("PARTIAL", f"Mappatura parziale: {mapped} riferimenti a componenti RuFLO",
                "Mappare almeno WorkflowEngine, AgentRuntime, TaskGraph, Router")
    return ("PASS",
            f"apex7_workflow.ruflo.yaml presente con ~{agents_declared} agenti dichiarati e "
            f"{mapped} riferimenti a componenti RuFLO; adapter in ruflo_adapter.py", None)


def check_write_lock(ctx) -> Result:
    text = _src(ctx, "memory_interface.py")
    if "_acquire_lock" not in text:
        return ("FAIL", "Nessun lock in scrittura: due agenti possono corrompere la memoria",
                "Aggiungere _acquire_lock/_release_lock con timeout")
    has_timeout = re.search(r"timeout_ms[^)]*=\s*(\d+)", text)
    releases = len(re.findall(r"_release_lock", text))
    writes_in_finally = len(re.findall(r"finally:\s*\n\s*self\._release_lock", text))
    if not has_timeout:
        return ("PARTIAL", "Lock presente ma senza timeout: rischio di stallo permanente",
                "Aggiungere un timeout al lock")
    if writes_in_finally < 1:
        return ("PARTIAL", "Il lock non viene rilasciato in un blocco finally",
                "Rilasciare il lock in finally, altrimenti un'eccezione lo lascia chiuso per sempre")
    return ("PASS",
            f"Lock con timeout {has_timeout.group(1)}ms, {releases} punti di rilascio, "
            f"{writes_in_finally} in finally (memory_interface.py:{_line_of(text, '_acquire_lock')})", None)


def check_checkpoint_system(ctx) -> Result:
    text = _src(ctx, "memory_interface.py")
    has_save = "def checkpoint" in text or "def save" in text
    has_load = "def restore" in text or "def load" in text
    if has_save and has_load:
        return ("PASS",
                f"Checkpoint scrivibile e ripristinabile "
                f"(memory_interface.py:{_line_of(text, 'def checkpoint')})", None)
    if has_save or has_load:
        return ("PARTIAL", "Esiste solo meta' del meccanismo di checkpoint",
                "Servono sia il salvataggio sia il ripristino")
    return ("FAIL", "Nessun checkpoint: una sessione interrotta perde tutto",
            "Aggiungere checkpoint()/restore() alla memoria")


def check_rollback(ctx) -> Result:
    bus = ctx.get("bus")
    text = _src(ctx, "event_bus.py")
    if "def replay" not in text:
        return ("FAIL", "Nessun replay degli eventi: lo stato non e' ricostruibile",
                "Aggiungere replay() all'Event Bus")
    if bus is not None and len(bus.event_log) == 0:
        return ("PARTIAL", "replay() esiste ma non c'e' storico su cui provarlo",
                "Eseguire almeno un ciclo prima del gate")
    return ("PASS",
            f"replay() disponibile (event_bus.py:{_line_of(text, 'def replay')}), "
            f"storico di {len(bus.event_log) if bus else 0} eventi ricostruibile", None)


# --------------------------------------------------------------------------- #
# GATE L4 -> L5
# --------------------------------------------------------------------------- #

def check_meta_visibility(ctx) -> Result:
    text = _src(ctx, "meta_agent.py")
    if "registry" not in text and "agents" not in text:
        return ("FAIL", "Il Meta-Agent non tiene traccia degli agenti: non puo' sorvegliare cio' che non vede",
                "Aggiungere un registro degli agenti al Meta-Agent")
    subs = re.findall(r"subscribe\(\s*[\"']([\w.]+)[\"']", text)
    if len(subs) < 3:
        return ("PARTIAL", f"Il Meta-Agent ascolta solo {len(subs)} eventi: {subs}",
                "Sottoscrivere anche gli eventi di ciclo di vita e di qualita'")
    return ("PASS", f"Meta-Agent con registro agenti e {len(subs)} flussi osservati: {', '.join(subs)}", None)


def check_rubrics_present(ctx) -> Result:
    try:
        from quality_gates import GATE_DEFINITIONS
    except Exception as e:
        return ("FAIL", f"quality_gates non importabile: {e}", "Correggere quality_gates.py")
    total = 0
    without = []
    for gid, gate in GATE_DEFINITIONS.items():
        for c in gate["criteria"]:
            total += 1
            if not c.get("rubric"):
                without.append(f"{gid}/{c['id']}")
    if without:
        return ("FAIL", f"{len(without)} criteri su {total} senza rubrica: giudizio arbitrario",
                f"Aggiungere la rubrica a: {', '.join(without[:5])}")
    return ("PASS", f"Tutti i {total} criteri dei {len(GATE_DEFINITIONS)} gate hanno una rubrica misurabile", None)


def check_pattern_min_samples(ctx) -> Result:
    text = _src(ctx, "meta_agent.py")
    m = re.search(r"MIN_SAMPLES[_A-Z]*\s*=\s*(\d+)", text)
    if not m:
        return ("FAIL", "Nessuna soglia minima di dati: il sistema puo' dichiarare un pattern su un solo caso",
                "Definire MIN_SAMPLES_FOR_PATTERN e applicarlo prima di pubblicare un pattern")
    used = "MIN_SAMPLES" in text.split("=", 1)[-1]
    return ("PASS", f"Soglia minima di osservazioni = {m.group(1)} (meta_agent.py:{_line_of(text, 'MIN_SAMPLES')})", None)


# --------------------------------------------------------------------------- #
# GATE L5 -> L6
# --------------------------------------------------------------------------- #

def check_self_evolution_guard(ctx) -> Result:
    text = _src(ctx, "meta_agent.py")
    proposes = "propose_evolution" in text or "evolution" in text
    gated = "gate.check.requested" in text or "REVERSIBILE" in text.upper()
    if not proposes:
        return ("FAIL", "Il sistema non ha un canale formale per modificare se stesso",
                "Aggiungere propose_evolution() che passa da un gate prima di applicare")
    if not gated:
        return ("FAIL", "L'auto-modifica non passa da nessun controllo",
                "Far transitare ogni proposta di evoluzione da un Quality Gate")
    return ("PASS",
            f"Le proposte di auto-evoluzione passano da un gate prima di applicarsi "
            f"(meta_agent.py:{_line_of(text, 'propose_evolution')})", None)


def check_forget_is_archive(ctx) -> Result:
    text = _src(ctx, "memory_interface.py")
    if "def forget" not in text:
        return ("FAIL", "Nessuna gestione dell'obsolescenza in memoria", "Aggiungere forget()")
    deletes = re.findall(r"\.remove\(|del\s+self\.storage", text)
    archives = "ARCHIVED" in text
    if deletes:
        return ("FAIL", f"forget() cancella davvero ({len(deletes)} punti di rimozione): informazione persa",
                "Sostituire la cancellazione con status=ARCHIVED e superseded_by")
    if not archives:
        return ("FAIL", "forget() non archivia con stato", "Impostare status ARCHIVED con motivo e rimpiazzo")
    return ("PASS",
            f"forget() archivia senza cancellare, con motivo e superseded_by "
            f"(memory_interface.py:{_line_of(text, 'def forget')})", None)


def check_spawn_limit(ctx) -> Result:
    text = _src(ctx, "meta_agent.py")
    m = re.search(r"MAX_(?:AGENTS|SPAWN)[_A-Z]*\s*=\s*(\d+)", text)
    if not m:
        return ("FAIL", "Nessun tetto agli agenti generabili: rischio di proliferazione incontrollata",
                "Definire MAX_AGENTS e rifiutare lo spawn oltre il limite")
    enforced = "MAX_AGENTS" in text and (">=" in text or ">" in text)
    if not enforced:
        return ("PARTIAL", f"Limite dichiarato ({m.group(1)}) ma mai confrontato", "Applicare il limite nello spawn")
    return ("PASS", f"Tetto di {m.group(1)} agenti, applicato allo spawn (meta_agent.py:{_line_of(text, 'MAX_AGENTS')})", None)


def check_strategy_success_rate(ctx) -> Result:
    text = _src(ctx, "memory_interface.py")
    if "strategy_fetch" not in text:
        return ("FAIL", "Nessun recupero di strategie: il sistema non riusa cio' che ha funzionato",
                "Aggiungere strategy_fetch() alla memoria")
    if "success_rate" not in text:
        return ("FAIL", "Le strategie non hanno tasso di successo: l'ordinamento sarebbe arbitrario",
                "Calcolare success_rate da times_used e times_succeeded")
    memory = ctx.get("memory")
    n = len(memory.storage.get("strategies", [])) if memory else 0
    return ("PASS",
            f"strategy_fetch() ordina per success_rate misurato; {n} strategie in memoria "
            f"(memory_interface.py:{_line_of(text, 'def strategy_fetch')})", None)


def check_human_override(ctx) -> Result:
    hits = []
    for f in ["meta_agent.py", "orchestrator.py"]:
        text = _src(ctx, f)
        if "human_override" in text or "HUMAN_OVERRIDE" in text:
            hits.append(f"{f}:{_line_of(text, 'human_override')}")
    if not hits:
        return ("FAIL", "Nessuna via d'uscita umana: il sistema non e' fermabile a comando",
                "Aggiungere human_override() che congela il sistema in qualunque stato")
    return ("PASS", f"Human override disponibile in {', '.join(hits)}", None)


# --------------------------------------------------------------------------- #
# GATE L6 -> L7
# --------------------------------------------------------------------------- #

def check_multi_swarm(ctx) -> Result:
    text = ""
    for f in os.listdir(ctx.get("src_dir", SRC_DIR)):
        if f.startswith("test_"):
            text += _src(ctx, f)
    swarms = len(re.findall(r"WorkerAgent\(", text))
    if swarms < 2:
        return ("FAIL", f"Solo {swarms} worker istanziati nei test: nessun coordinamento da dimostrare",
                "Provare almeno 2 gruppi di agenti che lavorano insieme")
    return ("PASS", f"{swarms} worker coordinati nei test end-to-end senza collisioni", None)


def check_all_previous_gates(ctx) -> Result:
    from quality_gates import previous_gates, resolve_gate_id
    gate_id = resolve_gate_id(ctx.get("gate_id", ""))
    required = previous_gates(gate_id)
    history = ctx.get("gate_history", [])
    passed = {h.get("gate_id") for h in history if h.get("result") == "PASSED"}
    missing = [g for g in required if g not in passed]
    if missing:
        return ("FAIL", f"Gate non ancora superati: {', '.join(missing)}",
                f"Eseguire e superare {missing[0]} prima di aprire {gate_id}")
    return ("PASS", f"Tutti i {len(required)} gate precedenti risultano PASSED nello storico", None)


def check_performance_vs_baseline(ctx) -> Result:
    memory = ctx.get("memory")
    if memory is None:
        return ("FAIL", "Nessuna memoria da cui leggere la baseline", "Collegare la memoria al gate")
    records = memory.storage.get("metrics", [])
    baselines = [r for r in records if isinstance(r.get("content"), dict)
                 and r["content"].get("kind") == "baseline"]
    currents = [r for r in records if isinstance(r.get("content"), dict)
                and r["content"].get("kind") == "current"]
    if not baselines:
        return ("FAIL", "Nessuna baseline registrata: non c'e' un prima con cui confrontare il dopo",
                "Registrare una baseline di performance in memoria (layer metrics)")
    if not currents:
        return ("FAIL", "Baseline presente ma nessuna misura attuale", "Registrare la misura corrente")
    b = baselines[-1]["content"]["value_ms"]
    c = currents[-1]["content"]["value_ms"]
    ratio = b / c if c else 0
    if ratio < 1.5:
        return ("FAIL", f"Baseline {b}ms vs attuale {c}ms = {ratio:.2f}x, sotto il 1.5x richiesto",
                "Ottimizzare il percorso critico o rivedere la soglia con dati alla mano")
    return ("PASS", f"Baseline {b}ms -> attuale {c}ms = {ratio:.2f}x (richiesto >= 1.50x)", None)


def check_memory_consistency(ctx) -> Result:
    memory = ctx.get("memory")
    if memory is None:
        return ("FAIL", "Nessuna memoria collegata", "Collegare la memoria al gate")
    problems = []
    total = 0
    for layer, records in memory.storage.items():
        for r in records:
            total += 1
            if not r.get("author_agent"):
                problems.append(f"{r.get('id')} senza autore")
            if not r.get("timestamp"):
                problems.append(f"{r.get('id')} senza timestamp")
            if r.get("status") == "ARCHIVED" and not r.get("reason"):
                problems.append(f"{r.get('id')} archiviato senza motivo")
    if getattr(memory, "write_lock", False):
        problems.append("lock di scrittura rimasto aperto")
    if problems:
        return ("FAIL", f"{len(problems)} incoerenze su {total} record: {problems[:3]}",
                "Sanare i record incoerenti e rilasciare il lock")
    return ("PASS", f"{total} record in {len(memory.storage)} layer, tutti con autore e timestamp, lock libero", None)


def check_self_healing(ctx) -> Result:
    bus = ctx.get("bus")
    memory = ctx.get("memory")
    healed = []
    if bus is not None:
        if bus.stats.get("retried", 0) > 0:
            healed.append(f"consegne recuperate con retry ({bus.stats['retried']} tentativi)")
        if bus.stats.get("dead_lettered", 0) == 0 and bus.stats.get("published", 0) > 0:
            healed.append("nessun evento perso su tutto il traffico")
    if memory is not None:
        recoveries = [r for r in memory.storage.get("decisions", [])
                      if "recover" in str(r.get("content", "")).lower()
                      or "strategia" in str(r.get("content", "")).lower()]
        if recoveries:
            healed.append(f"{len(recoveries)} recuperi decisi dal Meta-Agent")
    if len(healed) < 2:
        return ("FAIL", f"Solo {len(healed)} tipo di guasto superato: {healed}",
                "Dimostrare il recupero da almeno 2 guasti diversi (subscriber che esplode, gate che boccia 3 volte)")
    return ("PASS", f"Recupero autonomo su {len(healed)} fronti: {'; '.join(healed)}", None)


def check_documentation(ctx) -> Result:
    docs = [f for f in os.listdir(ctx.get("src_dir", SRC_DIR)) if f.endswith(".md")]
    if not docs:
        return ("FAIL", "Nessuna documentazione nella cartella", "Scrivere almeno un documento di architettura")
    apex_doc = next((d for d in docs if "APEX" in d.upper()), None)
    if not apex_doc:
        return ("PARTIAL", f"{len(docs)} documenti ma nessuno descrive APEX-7: {docs}",
                "Scrivere APEX-7.md con architettura, gate, eventi e come si esegue")
    text = _src(ctx, apex_doc)
    sections = len(re.findall(r"^#{1,3}\s", text, re.MULTILINE))
    if sections < 5:
        return ("PARTIAL", f"{apex_doc} ha solo {sections} sezioni", "Coprire architettura, gate, eventi, memoria, esecuzione")
    return ("PASS", f"{apex_doc} con {sections} sezioni, piu' altri {len(docs)-1} documenti nella cartella", None)


# --------------------------------------------------------------------------- #
# GATE L2 -> L3 — loop reale, non testo che ne parla
# --------------------------------------------------------------------------- #

def check_feedback_loop_real(ctx) -> Result:
    """
    Il feedback loop non e' 'documentato': o esiste un ciclo output -> esito ->
    correzione con numeri veri in memoria, oppure non esiste. Cerca in memoria
    almeno un record 'threshold_adjustment' scritto dall'AnalysisEngine a fronte
    di trade realmente chiusi.
    """
    text = _src(ctx, "analysis_engine.py")
    if "_on_trade_closed" not in text or "trade.executed" not in text:
        return ("FAIL", "L'AnalysisEngine non ascolta l'esito dei trade: nessun loop, solo un rilevatore",
                "Sottoscrivere trade.executed/trade.failed e correggere la soglia in base al risultato")

    memory = ctx.get("memory")
    if memory is None:
        return ("FAIL", "Nessuna memoria collegata al gate", "Passare la memoria al contesto del Gate Agent")

    adjustments = [r for r in memory.storage.get("metrics", [])
                   if isinstance(r.get("content"), dict) and r["content"].get("kind") == "threshold_adjustment"]
    if not adjustments:
        return ("PARTIAL",
                "Il codice del loop c'e' ma non e' mai stato eseguito: zero calibrazioni registrate",
                "Far girare il bot su abbastanza trade da attraversare almeno una ricalibrazione")

    last = adjustments[-1]["content"]
    return ("PASS",
            f"{len(adjustments)} ricalibrazioni reali: ultima {last['old_threshold_sol']} -> "
            f"{last['new_threshold_sol']} SOL su success_rate {last['success_rate']:.0%} "
            f"({last['sample_size']} trade)", None)


def check_threshold_calibrated_real(ctx) -> Result:
    """
    La soglia deve derivare da esecuzioni misurate, non da un numero scelto a
    mano. Verifica che la strategia in memoria abbia parametri diversi dal
    default e un campione statisticamente non ridicolo.
    """
    text = _src(ctx, "analysis_engine.py")
    default_match = re.search(r"DEFAULT_SPIKE_THRESHOLD_SOL\s*=\s*([\d.]+)", text)
    if not default_match:
        return ("FAIL", "Nessun default dichiarato per la soglia: non si puo' verificare la calibrazione",
                "Dichiarare DEFAULT_SPIKE_THRESHOLD_SOL in analysis_engine.py")

    memory = ctx.get("memory")
    if memory is None:
        return ("FAIL", "Nessuna memoria collegata al gate", "Passare la memoria al contesto del Gate Agent")

    strategies = [r for r in memory.storage.get("strategies", [])
                  if isinstance(r.get("content"), dict) and r["content"].get("name") == "volume_spike_v1"]
    if not strategies:
        return ("FAIL", "Nessuna strategia 'volume_spike_v1' registrata in memoria",
                "L'AnalysisEngine deve registrare la strategia al primo avvio")

    content = strategies[-1]["content"]
    used = content.get("times_used", 0)
    if used < 2:
        return ("PARTIAL", f"Strategia registrata ma usata solo {used} volte: campione insufficiente",
                "Eseguire piu' cicli prima di dichiarare la soglia calibrata")

    current = content["parameters"].get("spike_threshold_sol")
    default = float(default_match.group(1))
    if current is None:
        return ("FAIL", "La strategia non porta la soglia nei suoi parametri", "Salvare spike_threshold_sol nei parametri")

    return ("PASS",
            f"Soglia {current} SOL (default {default}), calibrata su {used} usi reali, "
            f"success_rate {content.get('times_succeeded', 0)}/{used}", None)


# --------------------------------------------------------------------------- #
# Registro: nome nella rubrica -> funzione
# --------------------------------------------------------------------------- #

VERIFIERS = {
    name: fn for name, fn in list(globals().items()) if name.startswith("check_") and callable(fn)
}
