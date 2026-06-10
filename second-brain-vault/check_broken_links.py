import os
import re

WIKI_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\wiki"

def find_broken_links():
    all_files = set()
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith('.md'):
                # Add filename without extension
                all_files.add(f.replace('.md', ''))
                # Also add full path from WIKI_DIR without extension
                rel_path = os.path.relpath(os.path.join(root, f), WIKI_DIR).replace('\\', '/')
                all_files.add(rel_path.replace('.md', ''))

    broken_links = {}
    
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Find all [[links]]
                links = re.findall(r'\[\[(.*?)(\|.*?)?\]\]', content)
                for link_target, _ in links:
                    link_target = link_target.strip()
                    # Check if link_target is in all_files
                    if link_target not in all_files:
                        if link_target not in broken_links:
                            broken_links[link_target] = []
                        broken_links[link_target].append(f)
                        
    return broken_links

if __name__ == "__main__":
    broken = find_broken_links()
    print(f"Found {len(broken)} unique broken links.")
    # Print first 20 to see what they look like
    for i, (target, sources) in enumerate(sorted(broken.items())):
        if i >= 50: break
        print(f"Target: {target} (Found in {len(sources)} files)")
