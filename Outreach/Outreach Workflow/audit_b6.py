import json
from collections import Counter

with open("emails_b6_ready.json", encoding="utf-8", errors="replace") as f:
    data = json.load(f)

statuses = Counter(e.get("status", "?") for e in data)
print("Status breakdown completo:", dict(statuses))
print(f"Totale email: {len(data)}")

# Mostra le send_failed recenti (ultime 10)
failed = [e for e in data if e.get("status") == "send_failed"]
print(f"\nSend_failed ({len(failed)} totali) - ultime 5:")
for e in failed[-5:]:
    print(f"  {e.get('nicchia','?'):15} | {e.get('email','?')}")

# Check se ci sono ancora skip_placeholder
skip = [e for e in data if e.get("status") == "skip_placeholder"]
print(f"\nSkip placeholder: {len(skip)}")
