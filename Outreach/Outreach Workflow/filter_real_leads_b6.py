"""
Filtra le email B6 "ready" rimuovendo i placeholder AI-generated.
I placeholder hanno pattern: città + numero (es. "esteticanapoli2.it", "legalemilano5.it")
Le email reali hanno nomi propri italiani o domini aziendali veri.
"""
import json
import re

PLACEHOLDER_PATTERNS = [
    r'estetica[a-z]+\d+\.it$',
    r'commercialista[a-z]+\d+\.it$',
    r'studiomedico[a-z]+\d+\.it$',
    r'legale[a-z]+\d+\.it$',
    r'fisio[a-z]+\d+\.it$',
    r'psicologo[a-z]+\d+\.it$',
    r'palestra[a-z]+\d+\.it$',
    r'studio[a-z]+\d+\.it$',
    r'beauty[a-z]+\d+\.it$',
    # Generic numbered patterns
    r'[a-z]+(napoli|roma|milano|torino|firenze|bologna|bari|verona)\d+\.it$',
]

def is_placeholder(email):
    email_low = email.lower()
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, email_low):
            return True
    return False

with open("emails_b6_ready.json", encoding="utf-8", errors="replace") as f:
    data = json.load(f)

ready = [e for e in data if e.get("status") == "ready"]
real = [e for e in ready if not is_placeholder(e.get("email", ""))]
placeholders = [e for e in ready if is_placeholder(e.get("email", ""))]

print(f"Ready totali: {len(ready)}")
print(f"Lead reali da inviare: {len(real)}")
print(f"Placeholder da bloccare: {len(placeholders)}")
print()
print("LEAD REALI:")
for e in real:
    print(f"  {e.get('nicchia','?'):15} | {e.get('email','?')}")
print()
print("PLACEHOLDER (verranno marcati skip):")
for e in placeholders:
    print(f"  {e.get('email','?')}")

# Marca i placeholder come "skip_placeholder"
for e in data:
    if e.get("status") == "ready" and is_placeholder(e.get("email", "")):
        e["status"] = "skip_placeholder"

with open("emails_b6_ready.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nFatto! {len(placeholders)} placeholder marcati 'skip_placeholder'.")
print(f"{len(real)} email reali rimaste con status 'ready'.")
