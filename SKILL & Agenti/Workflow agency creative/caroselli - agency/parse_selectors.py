import os
import re

root_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(root_dir, "arena_home.html")

if not os.path.exists(html_path):
    print(f"[X] Il file {html_path} non esiste!")
    exit(1)

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

print("--- RICERCA DI BATTLE / DIRECT / BATTLE MODE ---")
# Cerca tag contenenti parole chiave
for match in re.finditer(r'<[^>]+(?:battle|direct|chatgpt|medium)[^>]*>', content, re.IGNORECASE):
    print(match.group(0))

print("\n--- RICERCA TESTUALE DEI TAG INTERNI (es. Battle, Direct) ---")
# Cerca blocchi di testo e i loro tag circostanti
matches = re.findall(r'(<[^>]+>[^<]*(?:battle|direct|chatgpt|medium|image|file|upload|model)[^<]*</[^>]+>)', content, re.IGNORECASE)
for m in matches[:30]:
    print(m.strip())

print("\n--- STRUTTURA DELLE AREE DI BATTLE / DIRECT SELEZIONATE ---")
# Vediamo se c'è del testo specifico o bottoni
for btn in re.findall(r'<button[^>]*>.*?</button>', content, re.IGNORECASE | re.DOTALL):
    if any(k in btn.lower() for k in ["battle", "direct", "image", "upload", "file"]):
        print(f"BUTTON: {btn.strip()}")
