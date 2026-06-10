import os
import re

WIKI_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\wiki"
STUBS_DIR = os.path.join(WIKI_DIR, "Knowledge_Base", "Stubs")

def create_stubs():
    os.makedirs(STUBS_DIR, exist_ok=True)
    
    # 1. Collect all existing files
    all_files = set()
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith('.md'):
                all_files.add(f.replace('.md', ''))
                rel_path = os.path.relpath(os.path.join(root, f), WIKI_DIR).replace('\\', '/').replace('.md', '')
                all_files.add(rel_path)

    # 2. Find all broken links
    broken = set()
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                links = re.findall(r'\[\[(.*?)(\|.*?)?\]\]', content)
                for target, _ in links:
                    target = target.strip()
                    if not target or target.startswith('http') or target == 'index': continue
                    if target not in all_files:
                        broken.add(target)

    # 3. Create stubs for broken links
    created_count = 0
    for target in broken:
        # Sanitize filename
        safe_name = re.sub(r'[^\w\s-]', '', target).strip()
        if not safe_name: continue
        
        stub_path = os.path.join(STUBS_DIR, f"{safe_name}.md")
        
        # Avoid overwriting if multiple paths lead to same safe_name
        if os.path.exists(stub_path): continue
        
        with open(stub_path, 'w', encoding='utf-8') as f:
            f.write(f"# {target}\n\n")
            f.write(f"> [!NOTE]\n")
            f.write(f"> Questo è un **Knowledge Stub** (Segnaposto). \n")
            f.write(f"> Il contenuto originale per '{target}' non è stato trovato durante l'importazione automatica, \n")
            f.write(f"> ma il link è stato preservato perché rappresenta un concetto rilevante per Digital Empire.\n\n")
            f.write(f"## Prossimi Passi\n")
            f.write(f"- [ ] Integrare il materiale mancante\n")
            f.write(f"- [ ] Espandere il concetto basandosi sui documenti correlati\n\n")
            f.write(f"--- \n*Creato automaticamente come parte del consolidamento del Second Brain.*")
            
        created_count += 1
        
    print(f"Created {created_count} Knowledge Stubs to fill grey dots.")

if __name__ == "__main__":
    create_stubs()
