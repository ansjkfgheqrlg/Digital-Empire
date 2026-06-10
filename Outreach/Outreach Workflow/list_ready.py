import json
with open("emails_b6_ready.json", encoding="utf-8", errors="replace") as f:
    data = json.load(f)
ready = [e for e in data if e.get("status") == "ready"]
print("Totale ready:", len(ready))
print()
for e in ready:
    print(e.get("nicchia","?").ljust(15), "|", e.get("email","?"), "|", e.get("page_name","?"))
