import os
import re

SOURCE_FILE = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\manuale_raw.txt"

def debug_parse():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    # Skip index
    parts_start = list(re.finditer(r'^PARTE 1 —', text, flags=re.MULTILINE))
    if len(parts_start) > 1:
        text = text[parts_start[1].start():]

    parts = re.findall(r'^PARTE \d+ — .*$', text, flags=re.MULTILINE)
    print(f"Found {len(parts)} parts:")
    for p in parts:
        print(f"  {p.strip()}")

if __name__ == "__main__":
    debug_parse()
