import os
import re

root_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(root_dir, "arena_home.html")

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Rimuoviamo gli script per non inquinare i risultati
clean_content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)

print("--- RICERCA TAG CON DIRECT/BATTLE DOPO LA PULIZIA DEGLI SCRIPT ---")
# Cerchiamo tutti i tag che contengono le parole "Direct" o "Battle" (case-insensitive) come testo interno
pattern = r'(<[^>]+>[^<]*(?:Direct|Battle)[^<]*</[^>]+>)'
matches = re.findall(pattern, clean_content, re.IGNORECASE)
for m in matches[:50]:
    print(m.strip())
