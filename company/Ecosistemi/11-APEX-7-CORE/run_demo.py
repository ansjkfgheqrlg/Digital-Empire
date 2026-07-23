"""
Run Demo - Dimostra intero sistema APEX-7 con tutti i livelli
"""
import asyncio
from arena_generator import ArenaGenerator

async def full_demo():
    print("""
🏗️ SISTEMA COMPLETO: ARCHITETTURA A 7 LIVELLI CON SWARM + MEMORY
DEMO LIVE - Esecuzione parallela 3 stream ad alto ROI
    """)
    
    gen = ArenaGenerator(model="GPT-4o")
    
    # Dati presi dal tuo esempio originale ma potenziati
    raw_notes_ecommerce = """
    FASE ANALISI: Ho call con e-commerce moda che perdono 68% carrelli abbandonati per mancanza follow-up immediato
    IDEE: AI che manda WhatsApp in 30sec con foto prodotto lasciato + coupon dinamico 10% + video UGC recensione
    LOGICA: Trigger abbandono -> Check magazzino -> Genera messaggio personalizzato con nome prodotto -> Invia foto HD -> Se non risposta in 5min -> Secondo messaggio con urgenza stock limitato
    OBIETTIVO: Recuperare +22% carrelli senza intervento umano
    """
    
    carousel_copy = [
        "CARRELLI ABBANDONATI = SOLDI BRUCIATI",
        "68% dei tuoi clienti scappa prima di pagare",
        "IL PROBLEMA NON È IL PREZZO",
        "È CHE NON GLI RISPONDI IN 30 SECONDI",
        "SISTEMA AI: FOTO + COUPON + URGENZA",
        "RECUPERO +22% SENZA UMANO",
        "RISPONDI 'RECUPERO' PER VIDEO 2MIN"
    ]
    
    target = "E-commerce Moda DTC Italia con fatturato 1-10M"
    service = "Sistema AI WhatsApp che recupera carrelli abbandonati con foto prodotto + coupon dinamico + urgenza in 30 secondi, senza operatore"

    results = await gen.run_all_parallel(
        skill_raw_notes=raw_notes_ecommerce,
        carousel_texts=carousel_copy,
        outreach_target=target,
        outreach_service=service
    )
    
    print("\n✅ DEMO COMPLETATA - Controlla outputs/ per risultati")
    print(f"Memory session: {gen.memory.session_id}")
    print(f"Decisions logged: {len(gen.memory.get_recent_decisions(100))}")
    print(f"Orchestrator metrics: {gen.orchestrator.get_metrics()}")
    
    # Mostra compressed knowledge
    print("\n📚 Compressed Knowledge:")
    print(f"Lessons: {gen.memory.compressed_knowledge['lessons_learned'][:2]}")
    print(f"Best Practices: {gen.memory.compressed_knowledge['best_practices'][:2]}")

if __name__ == "__main__":
    asyncio.run(full_demo())
