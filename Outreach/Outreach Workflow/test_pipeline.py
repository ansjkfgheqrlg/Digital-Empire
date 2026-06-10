"""
Test pipeline email — Digital Empire
======================================
Testa i Team 2-5 con lead finti realistici.
Non richiede token Facebook. Non invia email.
Utile per verificare la qualita' delle email APSOC generate da NVIDIA.

Uso: python test_pipeline.py
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY", "").strip()
if not OPENROUTER_KEY:
    print("ERRORE: OPENROUTER_API_KEY non trovata nel file .env")
    sys.exit(1)

# Lead finti realistici — rappresentano i 3 template A/B/C
LEAD_TEST = [
    {
        "page_name": "Fisioterapia Bianchi",
        "website": "https://fisioterapiabianchi.it",
        "email": "info@fisioterapiabianchi.it",
        "settore": "fisioterapista",
        "citta": "Milano",
        "score": 85,
        "template": "A",  # Senza sito ottimizzato
        "pain_point": "Nessuna presenza online efficace — pazienti trovano competitor su Google",
        "key_observation": "Pagina Facebook attiva ma nessun sito professionale",
        "settore_calibrato": "salute",
    },
    {
        "page_name": "Ristorante Da Marco",
        "website": "https://ristorantedamarco.it",
        "email": "prenotazioni@ristorantedamarco.it",
        "settore": "ristorante",
        "citta": "Roma",
        "score": 72,
        "template": "B",  # Ads attivi + funnel scarso
        "pain_point": "Spende su ads Facebook ma la landing page converte male",
        "key_observation": "Ads attivi per pranzo di lavoro, landing page lenta e senza prenotazione online",
        "settore_calibrato": "ristorante",
    },
    {
        "page_name": "Studio Legale Verdi",
        "website": "https://studiolegale-verdi.it",
        "email": "info@studiolegale-verdi.it",
        "settore": "avvocato",
        "citta": "Torino",
        "score": 78,
        "template": "C",  # AI implementation
        "pain_point": "Processi manuali ripetitivi (redazione contratti, raccolta documenti) che consumano 15+ ore/settimana",
        "key_observation": "Studio con 5 avvocati, gestione clienti ancora su email e fogli Excel",
        "settore_calibrato": "consulente",
    },
]


def test_pipeline():
    print("\n" + "=" * 62)
    print("  DIGITAL EMPIRE — TEST PIPELINE EMAIL")
    print("  Team 2 → 3 → 4 → 5 con 3 lead realistici")
    print("  Nessuna email inviata")
    print("=" * 62)

    from agents.copy_knowledge import CopyKnowledgeAgent
    from agents.strategist import StrategistAgent
    from agents.writer import EmailWriterAgent
    from agents.humanizer import HumanizerAgent

    copy_knowledge = CopyKnowledgeAgent(OPENROUTER_KEY)
    strategist = StrategistAgent(OPENROUTER_KEY)
    writer = EmailWriterAgent(OPENROUTER_KEY)
    humanizer = HumanizerAgent(OPENROUTER_KEY)

    risultati = []

    for i, lead in enumerate(LEAD_TEST, 1):
        print(f"\n{'─'*62}")
        print(f"  LEAD {i}/3: {lead['page_name']} ({lead['citta']}) — Template {lead['template']}")
        print(f"{'─'*62}")

        # Team 2: Copy Knowledge
        print(f"\n[TEAM 2] Preparazione briefing pack...")
        lead_con_briefing = copy_knowledge.run([lead])[0]
        pack = lead_con_briefing.get("copy_briefing_pack", {})
        apertura = pack.get("apertura_suggerita", {})
        print(f"  Apertura suggerita oggetto: {apertura.get('oggetto', '—')}")
        print(f"  Prima riga: {apertura.get('prima_riga', '—')[:80]}...")

        # Team 3: Strategy
        print(f"\n[TEAM 3] Generazione brief strategico...")
        lead_con_strategy = strategist.run([lead_con_briefing])[0]
        brief = lead_con_strategy.get("strategy_brief", {})
        print(f"  Angolo: {brief.get('hook_angle', '—')[:80]}...")
        print(f"  Tono: {brief.get('nota_tono', '—')}")

        # Team 4: Writer
        print(f"\n[TEAM 4] Scrittura email NVIDIA Nemotron...")
        writer_output = writer.run([lead_con_strategy])
        if not writer_output:
            print("  ERRORE: email non generata (rate limit persistente o errore API)")
            risultati.append({"lead": lead["page_name"], "template": lead["template"], "email": {}, "approvata": False})
            continue
        lead_con_email = writer_output[0]
        oggetto = lead_con_email.get("oggetto", "N/A")
        corpo = lead_con_email.get("corpo", "N/A")
        email = {"oggetto": oggetto, "corpo": corpo}
        parole = len(corpo.split()) if corpo != "N/A" else 0

        print(f"\n  OGGETTO: {oggetto}")
        print(f"\n  CORPO ({parole} parole):")
        print("  " + corpo.replace("\n", "\n  "))

        # Team 5: QA
        print(f"\n[TEAM 5] QA 3-check...")
        approvate, da_rivedere = humanizer.run([lead_con_email])

        if approvate:
            lead_finale = approvate[0]
            score = lead_finale.get("qa_score_media", 0)
            print(f"  RISULTATO: APPROVATA (score {score:.1f}/10)")
        elif da_rivedere:
            lead_in_revisione = da_rivedere[0]
            score = lead_in_revisione.get("qa_score_media", 0)
            feedback = lead_in_revisione.get("qa_feedback", "")
            print(f"  RISULTATO: DA RIVEDERE (score {score:.1f}/10)")
            print(f"  Feedback: {feedback[:120]}...")

            # Revisione
            print(f"\n[TEAM 4] Revisione con feedback...")
            lead_rivisto = writer.revise(lead_in_revisione)
            if lead_rivisto is None:
                print(f"  REVISIONE: fallita (rate limit persistente)")
            else:
                corpo_rev = lead_rivisto.get("corpo", "")
                print(f"  VERSIONE RIVISTA ({len(corpo_rev.split())} parole):")
                print("  " + corpo_rev.replace("\n", "\n  "))

                # Secondo QA
                approvate2, scartate = humanizer.run([lead_rivisto])
                if approvate2:
                    score2 = approvate2[0].get("qa_score_media", 0)
                    print(f"  SECONDO QA: APPROVATA (score {score2:.1f}/10)")
                else:
                    print(f"  SECONDO QA: SCARTATA (non soddisfa standard qualita')")

        risultati.append({
            "lead": lead["page_name"],
            "template": lead["template"],
            "email": email,
            "approvata": bool(approvate),
        })

    print(f"\n{'='*62}")
    print("  RIEPILOGO TEST")
    print(f"{'='*62}")
    for r in risultati:
        stato = "APPROVATA" if r["approvata"] else "RIVISTA"
        print(f"  [{r['template']}] {r['lead']}: {stato}")
    print(f"{'='*62}\n")


if __name__ == "__main__":
    test_pipeline()
