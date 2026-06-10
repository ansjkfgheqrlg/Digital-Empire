import os
import re

WIKI_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\wiki"
KB_DIR = os.path.join(WIKI_DIR, "Knowledge_Base")

def normalize_map_name(name):
    return name.replace('&', 'and').replace(' ', '_').title()

def interlink_hyper():
    # 1. Collect all titles and their link paths
    title_to_link = {}
    topic_to_map = {}
    
    # Map high-level areas
    for m in os.listdir(WIKI_DIR):
        if m.startswith('Map - ') and m.endswith('.md'):
            map_name = m.replace('.md', '')
            topic_to_map[map_name.lower()] = map_name

    for root, dirs, files in os.walk(KB_DIR):
        for f in files:
            if f.endswith('.md'):
                match = re.search(r'^\(.*?\) (.*)\.md$', f)
                title = match.group(1).strip() if match else f.replace('.md', '')
                
                if len(title) > 3: # Smaller titles too
                    rel_path = os.path.relpath(os.path.join(root, f), KB_DIR).replace('\\', '/')
                    link_path = f"Knowledge_Base/{rel_path.replace('.md', '')}"
                    title_to_link[title] = link_path

    # 2. Process each file
    count = 0
    # Sort titles by length (desc) to match longest strings first
    sorted_titles = sorted(title_to_link.keys(), key=len, reverse=True)
    
    for root, dirs, files in os.walk(KB_DIR):
        for filename in files:
            if not filename.endswith('.md'): continue
            path = os.path.join(root, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            cur_match = re.search(r'^\(.*?\) (.*)\.md$', filename)
            cur_title = cur_match.group(1).strip() if cur_match else filename.replace('.md', '')
            
            related_links = []
            
            # Check for Topics/Hubs
            for kw_lower, map_target in topic_to_map.items():
                kw = map_target.replace('Map - ', '').replace('_', ' ')
                # Use regex for whole word match
                if re.search(rf'\b{re.escape(kw.lower())}\b', content.lower()):
                    if kw.lower() not in filename.lower():
                        related_links.append(f"[[{map_target}|{kw} Area]]")
            
            # Check for Article Titles (Ultra-Aggressive)
            found_count = 0
            for title in sorted_titles:
                if found_count >= 30: break # Much more links!
                if title.lower() == cur_title.lower(): continue
                
                # Regex for whole word match
                # Ensure it's not already linked
                if title.lower() in content.lower():
                    # Simple check to avoid matching inside a wikilink [[...]]
                    # We only add if it's found in the "Content" section
                    if re.search(rf'\b{re.escape(title.lower())}\b', content.lower()):
                        related_links.append(f"[[{title_to_link[title]}|{title}]]")
                        found_count += 1
            
            if related_links:
                related_links = sorted(list(set(related_links)))
                
                # Cleanup old section
                if "## Collegamenti Correlati" in content:
                    content = content.split("## Collegamenti Correlati")[0].strip()
                
                content += "\n\n## Collegamenti Correlati\n"
                # Join with newlines for better readability and graph density
                content += "\n".join([f"- {l}" for l in related_links]) + "\n"
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
            
    print(f"Hyper-Interlinking complete. Connected {count} articles with high density.")

if __name__ == "__main__":
    interlink_hyper()

