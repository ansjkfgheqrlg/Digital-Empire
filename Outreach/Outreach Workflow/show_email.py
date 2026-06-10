"""Genera e stampa 1 email per il primo lead del CSV."""
import os, sys, json
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))

from agents.copy_knowledge import CopyKnowledgeAgent
from agents.strategist import StrategistAgent
from agents.writer import EmailWriterAgent

lead = {
    "page_name": "Clinica Odontoiatrica Mancini",
    "email": "info@clinicaodontoiatricamancini.it",
    "settore": "dentista",
    "settore_calibrato": "dentista",
    "citta": "Milano",
    "website": "",
    "score": 70,
    "template": "A",
    "page_id": "test_001",
    "pain_point": "Nessun sito web — i pazienti non riescono a trovarli online",
    "key_observation": "Studio dentistico senza presenza web cercabile su Google",
}

key = os.getenv("OPENROUTER_API_KEY", "")

print("1/3 CopyKnowledge...")
ck = CopyKnowledgeAgent(key)
lead = ck._prepara_pack(lead)

print("2/3 Strategist...")
st = StrategistAgent(key)
lead = st._genera_brief(lead)

print("3/3 Writer...")
wr = EmailWriterAgent(key)
result = wr._scrivi_email(lead)

print("\n" + "="*60)
print(f"OGGETTO: {result.get('oggetto', '')}")
print("="*60)
print(result.get("corpo", ""))
print("="*60)
