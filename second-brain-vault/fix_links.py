"""
fix_links.py — Aggiusta tutti i link spezzati nella wiki
Logica: per ogni [[Link]], trova il file .md più simile e rimpiazza
"""

import os
import re
from difflib import get_close_matches

WIKI_PATH = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\wiki"

# Step 1: costruisci mappa di tutti i file reali
def get_all_files(wiki_path):
    file_map = {}  # basename -> full_path
    for root, dirs, files in os.walk(wiki_path):
        for f in files:
            if f.endswith(".md"):
                basename = f[:-3]  # senza .md
                file_map[basename] = os.path.join(root, f)
    return file_map

# Step 2: normalizza un link per trovare il file corrispondente
def normalize_link(link):
    """Rimuove prefissi, sostituisce spazi con underscore, normalizza"""
    # Rimuovi prefissi tipo "Tool:", "Concept:", "Project:", ecc.
    prefixes = ["Tool: ", "Concept: ", "Project: ", "Source: ", "Synthesis: ",
                "Entity: ", "Metric: ", "Skill: ", "Full details in "]
    normalized = link
    for prefix in prefixes:
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix):]
            break

    # Sostituisce " — " con "_"
    normalized = normalized.replace(" — ", "_")
    normalized = normalized.replace(" - ", "_")
    # Sostituisce spazi con underscore
    normalized = normalized.replace(" ", "_")
    # Rimuovi caratteri speciali problematici ma mantieni lettere, numeri, underscore, trattino
    normalized = re.sub(r"[^\w\-]", "", normalized)
    return normalized

# Step 3: trova il file migliore per un link
def find_best_match(link, file_map):
    # Prova corrispondenza esatta prima
    if link in file_map:
        return link

    normalized = normalize_link(link)
    if normalized in file_map:
        return normalized

    # Prova prefissi comuni
    prefix_map = {
        "Tool: ": "Tool_",
        "Concept: ": "Concept_",
        "Project: ": "Project_",
        "Source: ": "Source_",
        "Synthesis: ": "Synthesis_",
        "Skill: ": "Skill_",
    }
    for prefix, replacement in prefix_map.items():
        if link.startswith(prefix):
            candidate = replacement + link[len(prefix):].replace(" ", "_").replace(" — ", "_")
            candidate = re.sub(r"[^\w\-]", "", candidate)
            if candidate in file_map:
                return candidate

    # Fuzzy match come fallback
    all_basenames = list(file_map.keys())
    close = get_close_matches(normalized, all_basenames, n=1, cutoff=0.6)
    if close:
        return close[0]

    # Cerca per parole chiave
    words = normalized.lower().split("_")
    words = [w for w in words if len(w) > 3]  # parole significative
    best_score = 0
    best_match = None
    for basename in all_basenames:
        lower_base = basename.lower()
        score = sum(1 for w in words if w in lower_base)
        if score > best_score and score >= len(words) * 0.6:
            best_score = score
            best_match = basename
    if best_match:
        return best_match

    return None  # nessun match trovato

# Step 4: fix di tutti i file
def fix_all_links(wiki_path):
    file_map = get_all_files(wiki_path)
    print(f"Trovati {len(file_map)} file nella wiki")

    fixed_count = 0
    broken_count = 0
    unresolvable = []

    for basename, filepath in file_map.items():
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Trova tutti i link [[...]]
        links = re.findall(r"\[\[([^\]]+)\]\]", content)

        for link in set(links):  # set per non processare duplicati
            if link in file_map:
                continue  # già valido

            best = find_best_match(link, file_map)
            if best and best != link:
                # Rimpiazza nel contenuto
                old_link = f"[[{link}]]"
                new_link = f"[[{best}]]"
                content = content.replace(old_link, new_link)
                print(f"  FIX: [[{link}]] => [[{best}]]")
                fixed_count += 1
            elif best is None:
                unresolvable.append(f"{basename}: [[{link}]]")
                broken_count += 1

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"\n=== RISULTATO ===")
    print(f"Link aggiustati: {fixed_count}")
    print(f"Link irrisolvibili: {broken_count}")
    if unresolvable:
        print(f"\nLink irrisolvibili (da gestire manualmente):")
        for u in unresolvable[:30]:
            print(f"  {u}")

if __name__ == "__main__":
    fix_all_links(WIKI_PATH)
