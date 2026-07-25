"""
Definizione formale dei Quality Gates per APEX-7.

Ogni gate è un cancello tra due livelli: senza il suo PASS il sistema non
avanza. Ogni criterio porta con sé la rubrica con cui va misurato, così il
Gate Agent non deve inventarsi il metro di giudizio ogni volta.

RUBRICA — chiavi ammesse:
  must_contain      lista di termini: TUTTI devono comparire nell'output
  any_of            lista di termini: ne basta UNO
  must_not_contain  lista di termini: nessuno deve comparire (indizi di finto)
  min_occurrences   {termine: n} il termine deve comparire almeno n volte
  min_length        lunghezza minima dell'output in caratteri
  verify            nome di una funzione in VERIFIERS per un controllo eseguibile

Un criterio con verify viene valutato in modo programmatico e vince sugli
altri campi: quello che si può controllare eseguendo, si controlla eseguendo.
"""

from typing import Dict, Any, List

# Soglie: percentuale minima di criteri superati per passare il gate.
# Non sono uguali per tutti — un gate di sicurezza non tollera nulla.
GATE_DEFINITIONS: Dict[str, Dict[str, Any]] = {

    # ------------------------------------------------------------------ #
    "L1_TO_L2": {
        "name": "Fondamenta -> Struttura Connessa",
        "threshold": 1.0,          # 5/5 obbligatori
        "timeout_s": 60,
        "tolerance": "Nessuna: le fondamenta o ci sono o non ci sono",
        "criteria": [
            {
                "id": "C1",
                "name": "Componenti base definiti",
                "description": "Tutti i 5 componenti base (Orchestrator, Meta-Agent, Gate Agent, Worker, Memory) sono definiti.",
                "rubric": {"verify": "check_core_components"},
            },
            {
                "id": "C2",
                "name": "Responsabilità unica",
                "description": "Ogni componente ha una responsabilità unica e dichiarata.",
                "rubric": {"verify": "check_single_responsibility"},
            },
            {
                "id": "C3",
                "name": "Zero dipendenze circolari",
                "description": "Nessun componente chiama un altro direttamente: tutto passa dall'Event Bus.",
                "rubric": {"verify": "check_no_direct_calls"},
            },
            {
                "id": "C4",
                "name": "Interfacce definite",
                "description": "Le interfacce di comunicazione (event types) sono catalogate e rispettate.",
                "rubric": {"verify": "check_event_catalog"},
            },
            {
                "id": "C5",
                "name": "Test end-to-end",
                "description": "Almeno 1 scenario end-to-end eseguibile che dimostra il flusso completo.",
                "rubric": {"verify": "check_e2e_test_exists"},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    "L2_TO_L3": {
        "name": "Struttura -> Loop Adattivi",
        "threshold": 0.80,         # 4/5, tolleranza 1
        "timeout_s": 90,
        "tolerance": "Un criterio può mancare: i loop si tarano sul campo",
        "criteria": [
            {
                "id": "C1",
                "name": "Feedback loop documentato e testato",
                "description": "Esiste un ciclo output -> valutazione -> correzione, dimostrato da un test.",
                "rubric": {"must_contain": ["feedback", "loop"], "any_of": ["test", "verifica"]},
            },
            {
                "id": "C2",
                "name": "Decision Log validato",
                "description": "Ogni decisione finisce in un log con schema fisso e autore.",
                "rubric": {"verify": "check_decision_log"},
            },
            {
                "id": "C3",
                "name": "Almeno 3 condizioni di routing",
                "description": "Il flusso si biforca su almeno 3 condizioni reali, non su rami finti.",
                "rubric": {"verify": "check_routing_conditions"},
            },
            {
                "id": "C4",
                "name": "Loop con max_iterations",
                "description": "Ogni loop ha un tetto di iterazioni: nessun ciclo può girare all'infinito.",
                "rubric": {"verify": "check_max_iterations"},
            },
            {
                "id": "C5",
                "name": "Soglia di score calibrata su dati reali",
                "description": "La soglia di accettazione nasce da esecuzioni misurate, non da un numero scelto a caso.",
                "rubric": {"any_of": ["threshold", "soglia"], "must_contain": ["score"]},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    "L3_TO_L4": {
        "name": "Loop -> Parallelismo + RuFLO",
        "threshold": 0.833,        # 5/6
        "timeout_s": 120,
        "tolerance": "Un criterio su sei può restare aperto",
        "criteria": [
            {
                "id": "C1",
                "name": "RuFLO mappato",
                "description": "Le capacità di RuFLO sono mappate su componenti APEX-7 concreti, non citate a parole.",
                "rubric": {"verify": "check_ruflo_mapping"},
            },
            {
                "id": "C2",
                "name": "Race condition gestite",
                "description": "Gli accessi concorrenti alla memoria sono protetti da lock con timeout.",
                "rubric": {"verify": "check_write_lock"},
            },
            {
                "id": "C3",
                "name": "Schema Event Bus definito",
                "description": "Ogni evento ha priorità, garanzia di consegna e publisher dichiarati.",
                "rubric": {"verify": "check_event_catalog"},
            },
            {
                "id": "C4",
                "name": "Checkpoint implementabile",
                "description": "Lo stato può essere fotografato e ripreso: esiste un meccanismo di checkpoint.",
                "rubric": {"verify": "check_checkpoint_system"},
            },
            {
                "id": "C5",
                "name": "Baseline di performance",
                "description": "Esiste una misura di partenza contro cui confrontare i miglioramenti.",
                "rubric": {"any_of": ["baseline", "benchmark"], "must_contain": ["ms"]},
            },
            {
                "id": "C6",
                "name": "Rollback testato",
                "description": "Il sistema sa tornare indietro: replay o rollback dimostrato.",
                "rubric": {"verify": "check_rollback"},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    "L4_TO_L5": {
        "name": "Parallelismo -> Intelligence",
        "threshold": 0.80,         # 4/5
        "timeout_s": 120,
        "tolerance": "Un criterio può mancare",
        "criteria": [
            {
                "id": "C1",
                "name": "Meta-Agent vede tutti gli agenti",
                "description": "Il Meta-Agent ha visibilità sullo stato di ogni agente attivo.",
                "rubric": {"verify": "check_meta_visibility"},
            },
            {
                "id": "C2",
                "name": "Quality scoring calibrato",
                "description": "Il punteggio di qualità deriva da criteri con rubrica, non da un giudizio arbitrario.",
                "rubric": {"verify": "check_rubrics_present"},
            },
            {
                "id": "C3",
                "name": "Pattern detection con soglia minima di dati",
                "description": "Nessun pattern viene dichiarato sotto un numero minimo di osservazioni.",
                "rubric": {"verify": "check_pattern_min_samples"},
            },
            {
                "id": "C4",
                "name": "Knowledge graph con schema",
                "description": "La conoscenza è collegata da relazioni tipizzate, non da testo libero.",
                "rubric": {"any_of": ["relation", "relazione", "graph", "link"]},
            },
            {
                "id": "C5",
                "name": "Adaptive prompting provato su 3+ scenari",
                "description": "Il prompt si adatta al contesto ed è stato provato su almeno 3 scenari diversi.",
                "rubric": {"min_occurrences": {"scenario": 3}},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    "L5_TO_L6": {
        "name": "Intelligence -> Self-Evolving",
        "threshold": 1.0,          # 5/5 — safety critical
        "timeout_s": 180,
        "tolerance": "Zero: qui il sistema inizia a modificare se stesso",
        "criteria": [
            {
                "id": "C1",
                "name": "L'auto-evoluzione non destabilizza",
                "description": "Le modifiche che il sistema fa a se stesso sono reversibili e verificate da un gate.",
                "rubric": {"verify": "check_self_evolution_guard"},
            },
            {
                "id": "C2",
                "name": "La compressione non perde informazione critica",
                "description": "Comprimere la memoria non cancella: archivia con motivo e rimpiazzo.",
                "rubric": {"verify": "check_forget_is_archive"},
            },
            {
                "id": "C3",
                "name": "Lo spawning di agenti ha un tetto",
                "description": "Esiste un limite massimo di agenti generabili e viene applicato.",
                "rubric": {"verify": "check_spawn_limit"},
            },
            {
                "id": "C4",
                "name": "Ranking delle strategie su metriche reali",
                "description": "Le strategie sono ordinate per tasso di successo misurato sugli usi passati.",
                "rubric": {"verify": "check_strategy_success_rate"},
            },
            {
                "id": "C5",
                "name": "Human override sempre possibile",
                "description": "In ogni stato esiste una via per fermare il sistema a mano.",
                "rubric": {"verify": "check_human_override"},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    "L6_TO_L7": {
        "name": "Self-Evolving -> APEX",
        "threshold": 1.0,          # 7/7 — zero tolleranza
        "timeout_s": 300,
        "tolerance": "Zero: APEX è la dichiarazione che il sistema regge da solo",
        "criteria": [
            {
                "id": "C1",
                "name": "Coordinamento multi-swarm testato",
                "description": "Più gruppi di agenti lavorano insieme senza pestarsi i piedi, con prova eseguita.",
                "rubric": {"verify": "check_multi_swarm"},
            },
            {
                "id": "C2",
                "name": "Tutti i gate precedenti superati",
                "description": "Nessun gate da L1 a L6 è rimasto aperto o saltato.",
                "rubric": {"verify": "check_all_previous_gates"},
            },
            {
                "id": "C3",
                "name": "Test end-to-end su caso reale",
                "description": "Il sistema è stato provato su un caso d'uso vero, non su un mock.",
                "rubric": {"verify": "check_e2e_test_exists"},
            },
            {
                "id": "C4",
                "name": "Performance >= 150% della baseline",
                "description": "Il sistema è misurabilmente piu veloce o piu efficiente della sua stessa baseline.",
                "rubric": {"verify": "check_performance_vs_baseline"},
            },
            {
                "id": "C5",
                "name": "Consistenza della memoria verificata",
                "description": "Nessun record orfano, nessuna scrittura senza autore, nessun lock rimasto aperto.",
                "rubric": {"verify": "check_memory_consistency"},
            },
            {
                "id": "C6",
                "name": "Self-healing su 2+ tipi di guasto",
                "description": "Il sistema si è ripreso da almeno due guasti diversi senza intervento umano.",
                "rubric": {"verify": "check_self_healing"},
            },
            {
                "id": "C7",
                "name": "Documentazione completa e aggiornata",
                "description": "Chi apre il sistema domani capisce come funziona senza chiedere a nessuno.",
                "rubric": {"verify": "check_documentation"},
            },
        ],
    },
}

# Ordine di attraversamento dei gate — serve al criterio "tutti i precedenti".
GATE_SEQUENCE: List[str] = [
    "L1_TO_L2", "L2_TO_L3", "L3_TO_L4", "L4_TO_L5", "L5_TO_L6", "L6_TO_L7",
]

# Dopo quanti fallimenti consecutivi un gate smette di riprovare ed escala.
MAX_ATTEMPTS_BEFORE_ESCALATION = 3


def get_gate(gate_id: str) -> Dict[str, Any]:
    """Ritorna la definizione completa di un gate."""
    return GATE_DEFINITIONS.get(gate_id, {})


def get_gate_criteria(gate_id: str) -> List[Dict[str, Any]]:
    """Ritorna i criteri di un gate specifico. Compatibile con il Level 1."""
    return GATE_DEFINITIONS.get(gate_id, {}).get("criteria", [])


def get_threshold(gate_id: str) -> float:
    """La percentuale minima di criteri da superare per passare il gate."""
    return GATE_DEFINITIONS.get(gate_id, {}).get("threshold", 1.0)


def previous_gates(gate_id: str) -> List[str]:
    """Tutti i gate che vengono prima di questo nella sequenza."""
    if gate_id not in GATE_SEQUENCE:
        return []
    return GATE_SEQUENCE[: GATE_SEQUENCE.index(gate_id)]


def resolve_gate_id(raw_id: str) -> str:
    """
    Accetta sia l'id formale (L3_TO_L4) sia quello operativo generato
    dall'Orchestrator (GATE-L1-TASK-ABC123) e ritorna l'id formale.
    """
    if raw_id in GATE_DEFINITIONS:
        return raw_id
    for gate_id in GATE_SEQUENCE:
        level = gate_id.split("_")[0]          # "L3"
        if f"-{level}-" in raw_id or raw_id.startswith(f"GATE-{level}"):
            return gate_id
    return "L1_TO_L2"
