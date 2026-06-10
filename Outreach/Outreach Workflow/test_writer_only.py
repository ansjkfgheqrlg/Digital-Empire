"""
Test writer only — mostra le 3 email senza QA.
Usato per valutare la qualita' NVIDIA senza blocchi da rate limit.
"""
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

load_dotenv(Path(__file__).parent / ".env")
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY", "").strip()
if not OPENROUTER_KEY:
    print("ERRORE: OPENROUTER_API_KEY mancante")
    sys.exit(1)

LEADS = [
    {
        "page_name": "Fisioterapia Bianchi",
        "website": "https://fisioterapiabianchi.it",
        "email": "info@fisioterapiabianchi.it",
        "settore": "fisioterapista",
        "citta": "Milano",
        "score": 85,
        "template": "A",
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
        "template": "B",
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
        "template": "C",
        "pain_point": "Processi manuali ripetitivi: 15+ ore/settimana",
        "key_observation": "Studio con 5 avvocati, gestione clienti su email e Excel",
        "settore_calibrato": "consulente",
    },
]


def main():
    from agents.copy_knowledge import CopyKnowledgeAgent
    from agents.strategist import StrategistAgent
    from agents.writer import EmailWriterAgent

    ck = CopyKnowledgeAgent(OPENROUTER_KEY)
    st = StrategistAgent(OPENROUTER_KEY)
    wr = EmailWriterAgent(OPENROUTER_KEY)

    for i, lead in enumerate(LEADS, 1):
        print(f"\n{'='*62}")
        print(f"  EMAIL {i}/3 — {lead['page_name']} ({lead['citta']}) | Template {lead['template']}")
        print(f"{'='*62}")

        lead = ck.run([lead])[0]
        time.sleep(5)

        lead = st.run([lead])[0]
        time.sleep(8)

        out = wr.run([lead])
        if out:
            e = out[0]
            print(f"\n  OGGETTO A : {e.get('oggetto', '')}")
            print(f"  OGGETTO B : {e.get('oggetto_b', '')}")
            print(f"  OGGETTO C : {e.get('oggetto_c', '')}")
            corpo = e.get("corpo", "")
            print(f"\n  CORPO ({len(corpo.split())} parole):")
            print("  " + corpo.replace("\n", "\n  "))
        else:
            print("  ERRORE: email non generata (rate limit persistente)")

        if i < 3:
            print(f"\n  [attendo 5s prima del prossimo lead...]")
            time.sleep(5)

    print(f"\n{'='*62}")
    print("  DONE — valuta le email sopra")
    print(f"{'='*62}\n")


if __name__ == "__main__":
    main()
