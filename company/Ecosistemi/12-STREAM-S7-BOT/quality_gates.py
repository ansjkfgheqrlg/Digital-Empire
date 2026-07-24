"""
Definizione formale dei Quality Gates per APEX-7
"""

GATE_DEFINITIONS = {
    "L1_TO_L2": {
        "name": "Fondamenta -> Struttura Connessa",
        "threshold": 1.0,  # 5/5 -> 100% required
        "criteria": [
            {
                "id": "C1",
                "name": "Componenti base definiti",
                "description": "Tutti i 5 componenti base (Orchestrator, Meta-Agent, Gate Agent, Worker, Memory) sono definiti."
            },
            {
                "id": "C2",
                "name": "Responsabilità unica",
                "description": "Ogni componente ha una responsabilità unica chiara."
            },
            {
                "id": "C3",
                "name": "Zero dipendenze circolari",
                "description": "Nessun componente chiama un altro direttamente (tutto via Event Bus)."
            },
            {
                "id": "C4",
                "name": "Interfacce definite",
                "description": "Le interfacce di comunicazione (event types) sono definite e rispettate."
            },
            {
                "id": "C5",
                "name": "Test End-to-End",
                "description": "Almeno 1 test scenario end-to-end implementato per dimostrare il flusso."
            }
        ]
    }
}

def get_gate_criteria(gate_id: str) -> dict:
    """Ritorna i criteri di un gate specifico dal Database virtuale."""
    return GATE_DEFINITIONS.get(gate_id, {})
