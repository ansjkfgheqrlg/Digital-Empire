import json
from collections import Counter

with open("emails_b6_ready.json", encoding="utf-8", errors="replace") as f:
    data = json.load(f)

statuses = Counter(e.get("status", "?") for e in data)
print("Status breakdown:", dict(statuses))

sent = [e for e in data if e.get("status") == "sent"]
ready = [e for e in data if e.get("status") == "ready"]
print(f"Inviate: {len(sent)} | Ancora ready: {len(ready)}")
