import os
import re

WIKI_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\wiki"

def deep_clean():
    count = 0
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                
                # Remove lines starting with "> Raw:"
                new_lines = [line for line in lines if not line.strip().startswith('> Raw: [[')]
                
                if len(new_lines) != len(lines):
                    with open(path, 'w', encoding='utf-8') as file:
                        file.writelines(new_lines)
                    count += 1
                    
    print(f"Removed Raw links from {count} files.")

if __name__ == "__main__":
    deep_clean()
