import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.AI_Team import writer_agent
from Core.AI_Team import reviewer_agent

def generate_perfect_copy(topic, system_prompt, max_iterations=3):
    """
    Coordina il Writer e il Reviewer per generare il copy finale.
    """
    print(f"\n[AI Orchestrator] Inizio processo creativo per: {topic}")
    
    # 1. Generazione iniziale
    current_draft = writer_agent.generate_initial_draft(topic, system_prompt)
    
    for i in range(max_iterations):
        print(f"[AI Orchestrator] Iterazione {i+1}/{max_iterations}")
        
        # 2. Revisione
        approved, feedback = reviewer_agent.review_copy(topic, current_draft)
        
        if approved:
            print("[AI Orchestrator] Copy approvato dal Reviewer!")
            return current_draft
        else:
            print(f"[AI Orchestrator] Copy rifiutato. Feedback: {feedback[:100]}...")
            # 3. Raffinamento
            current_draft = writer_agent.refine_draft(topic, current_draft, feedback, system_prompt)
            
    print("[AI Orchestrator] Raggiunto limite iterazioni. Restituisco l'ultima bozza.")
    return current_draft
