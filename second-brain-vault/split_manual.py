import os
import re
import shutil

SOURCE_FILE = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\manuale_raw_v2.txt"
BASE_RAW_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\raw\formazzione\manuale-completo-claude-code-business"

def slugify(text):
    # Limit length to 100 chars
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text[:100]

def parse_manual():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Skip index: Find first line starting with PARTE 1 (after line 80)
    start_line = 0
    for i, line in enumerate(lines):
        if i > 80 and "PARTE 1" in line.upper():
            start_line = i
            break
            
    lines = lines[start_line:]
    
    current_part = "Parte 1 - Fondamenta"
    current_chapter = None
    current_section = None
    
    buffer = []
    
    def save():
        nonlocal buffer, current_part, current_chapter, current_section
        if not buffer: return
        
        # Build relative path
        rel_path = slugify(current_part)
        if current_chapter:
            rel_path = os.path.join(rel_path, slugify(current_chapter))
            
        full_dir = os.path.join(BASE_RAW_DIR, rel_path)
        os.makedirs(full_dir, exist_ok=True)
        
        filename = "overview.md"
        if current_section:
            filename = slugify(current_section) + ".md"
            
        full_path = os.path.join(full_dir, filename)
        title = current_section or current_chapter or current_part
        
        with open(full_path, 'a', encoding='utf-8') as f:
            if f.tell() == 0:
                f.write(f"# {title}\n\n")
            f.write("".join(buffer).strip() + "\n\n")
        buffer = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            buffer.append(line)
            continue
            
        # Check for Part or Chapter
        # We only consider lines that are likely HEADERS (short, all caps or starting with PARTE/CAPITOLO)
        is_part = stripped.upper().startswith("PARTE ")
        is_chap = stripped.upper().startswith("CAPITOLO ")
        
        if is_part or is_chap:
            save()
            if is_part:
                current_part = stripped
                current_chapter = None
                current_section = None
            else:
                current_chapter = stripped
                current_section = None
            continue
            
        # Check for Section X.Y — 
        section_match = re.match(r'^(\d+\.\d+) — (.*)$', stripped)
        if section_match:
            save()
            current_section = stripped
            continue
            
        buffer.append(line)
        
    save()

if __name__ == "__main__":
    if os.path.exists(BASE_RAW_DIR):
        shutil.rmtree(BASE_RAW_DIR)
    parse_manual()
