import os
import re

WIKI_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\wiki"

def garbage_link_cleanup():
    count = 0
    total_removed = 0
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Regex to find [[ ... ]]
                def fix_garbage(match):
                    inner = match.group(1)
                    # Garbage criteria:
                    # 1. Contains JSON characters: { } " :
                    # 2. Contains more than one [ or ]
                    # 3. Very long
                    if any(c in inner for c in ['{', '}', '"', ':', '$']) or len(inner) > 120 or inner.count('[') > 0:
                        return "" # REMOVE IT
                    return match.group(0) # Keep it

                new_content = re.sub(r'\[\[(.*?)(\|.*?)?\]\]', fix_garbage, content)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    count += 1
                    total_removed += (content.count('[[') - new_content.count('[['))
                    
    print(f"Cleaned garbage links in {count} files. Total removed: {total_removed}")

if __name__ == "__main__":
    garbage_link_cleanup()
