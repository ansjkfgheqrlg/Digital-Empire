import os
import re

WIKI_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\wiki"

def fix_links():
    count = 0
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Replace [[Path/File.md]] with [[Path/File]]
                # Regex to find [[...]] and remove .md before | or ]]
                new_content = re.sub(r'\[\[(.*?)\.md(\|.*?)?\]\]', r'[[\1\2]]', content)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    count += 1
                    
    print(f"Fixed links in {count} files.")

if __name__ == "__main__":
    fix_links()
