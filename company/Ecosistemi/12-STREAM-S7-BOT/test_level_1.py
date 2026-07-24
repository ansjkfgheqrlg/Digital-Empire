import time

# Importiamo l'infrastruttura nell'ordine corretto
from event_bus import global_bus
from memory_interface import global_memory

# Importiamo gli agenti (che al momento dell'import si iscrivono all'Event Bus)
from gate_agent import gate_1
from worker_agent import analyst_worker
from orchestrator import ad_orchestrator
from meta_agent import director_meta

def test_full_cycle():
    print("\n--- INIZIO TEST END-TO-END (APEX-7 LEVEL 1) ---\n")
    
    # 1. Tu (Max) assegni una missione all'AD
    print("MAX: 'Analizza il file ECOSISTEMA.md e dimmi se ci sono errori logici.'")
    ad_orchestrator.assign_mission("Analizza il file ECOSISTEMA.md", priority="HIGH")
    
    # Diamo al sistema il tempo di processare gli eventi sincroni
    # Dato che in L1 abbiamo implementato chiamate dirette nell'Event Bus, 
    # l'esecuzione è scesa giù fino in fondo all'albero di chiamate.
    time.sleep(2)
    
    print("\n--- STATO FINALE DEL SISTEMA ---")
    
    # Controlliamo la bacheca
    history = global_bus.get_history()
    print(f"Totale eventi registrati in bacheca: {len(history)}")
    for e in history:
        print(f" -> {e['event_type']} ({e['event_id']})")
        
    print("\n--- CONTROLLO MEMORIA ---")
    gate_reports = global_memory.storage.get("gate_reports", [])
    print(f"Report ispezioni salvati: {len(gate_reports)}")
    if gate_reports:
        print(f"Ultimo verdetto: {gate_reports[-1]['content']['result']}")

if __name__ == "__main__":
    test_full_cycle()
