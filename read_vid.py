import json

for i in range(1, 5):
    try:
        with open(f"vid{i}.json", encoding="utf-16") as f:
            data = json.load(f)
            title = data.get("title", "")
            desc = data.get("description", "")[:800]
            print(f"\n--- VIDEO {i} ---")
            print(f"Title: {title}")
            print(f"Desc: {desc}")
    except Exception as e:
        print(f"Error reading vid{i}.json: {e}")
