import os
import datetime
import re

# Paths
VAULT_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault"
RAW_DIR = os.path.join(VAULT_DIR, "raw")
WIKI_DIR = os.path.join(VAULT_DIR, "wiki")
KB_DIR = os.path.join(WIKI_DIR, "Knowledge_Base")
INDEX_FILE = os.path.join(WIKI_DIR, "index.md")
LOG_FILE = os.path.join(WIKI_DIR, "log.md")

def get_today():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def clean_content(content):
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if line.startswith('# ') and not new_lines: continue
        if line.startswith('> Source:') or line.startswith('> Collected:') or line.startswith('> Published:'): continue
        new_lines.append(line)
    return '\n'.join(new_lines).strip()

def process_wiki():
    today = get_today()
    os.makedirs(KB_DIR, exist_ok=True)
    
    # Pre-clean existing maps to avoid duplicates with different casing/symbols
    for item in os.listdir(WIKI_DIR):
        if item.startswith("Map - ") and item.endswith(".md"):
            os.remove(os.path.join(WIKI_DIR, item))

    index_entries = []
    
    # Recursively walk RAW_DIR
    for root, dirs, files in os.walk(RAW_DIR):
        rel_topic_path = os.path.relpath(root, RAW_DIR)
        
        for f in files:
            if not f.endswith('.md'): continue
            
            raw_path = os.path.join(root, f)
            with open(raw_path, 'r', encoding='utf-8') as rf:
                raw_content = rf.read()
            
            match = re.search(r'^# (.+)$', raw_content, re.MULTILINE)
            title = match.group(1) if match else f.replace('.md', '').replace('-', ' ').title()
            
            # Destination path mirrors raw structure
            wiki_topic_kb_path = os.path.join(KB_DIR, rel_topic_path)
            os.makedirs(wiki_topic_kb_path, exist_ok=True)
            
            # Clean topic name for display
            display_topic = rel_topic_path.replace('\\', ' > ').replace('/', ' > ')
            if display_topic == ".": display_topic = "General"
            
            wiki_filename = f"({os.path.basename(rel_topic_path)}) {f}" if rel_topic_path != "." else f
            wiki_path = os.path.join(wiki_topic_kb_path, wiki_filename)
            
            body = clean_content(raw_content)
            
            # Top-level topic for Map
            top_topic_raw = rel_topic_path.split(os.sep)[0] if rel_topic_path != "." else "General"
            top_topic = top_topic_raw.replace('&', 'and').replace(' ', '_').title()
            
            # Wikilink WITHOUT .md extension
            clean_rel_topic_path = rel_topic_path.replace('\\', '/')
            link_path = f"Knowledge_Base/{clean_rel_topic_path}/{wiki_filename.replace('.md', '')}"
            
            article = f"""# {title}
            
> Path: [[Map - {top_topic}|{display_topic}]]
> Raw: [[../../raw/{clean_rel_topic_path}/{f}|Original Source]]

## Content

{body}
"""
            with open(wiki_path, 'w', encoding='utf-8') as wf:
                wf.write(article)
            
            index_entries.append({
                'topic': display_topic,
                'top_topic': top_topic,
                'title': title,
                'link_path': link_path
            })

    # Create Top-Level Topic Maps
    top_topics = sorted(list(set(e['top_topic'] for e in index_entries)))
    for tt in top_topics:
        map_filename = f"Map - {tt}.md"
        map_path = os.path.join(WIKI_DIR, map_filename)
        with open(map_path, 'w', encoding='utf-8') as mf:
            mf.write(f"# Area: {tt}\n\n")
            mf.write(f"[[index|Torna all'Indice Principale]]\n\n")
            mf.write("## Documenti in questa Area (Gerarchia Completa)\n")
            relevant = [e for e in index_entries if e['top_topic'] == tt]
            # Group by sub-topic
            current_st = None
            for e in sorted(relevant, key=lambda x: x['topic']):
                if e['topic'] != current_st:
                    current_st = e['topic']
                    mf.write(f"\n### {current_st}\n")
                mf.write(f"- [[{e['link_path']}|{e['title']}]]\n")

    # Write index.md
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write("# 🏛️ Digital Empire - Master Index\n\n")
        f.write("Benvenuto nella tua Knowledge Base iper-organizzata. Tutto il materiale di Digital Empire è stato categorizzato preservando la struttura originale dei file.\n\n")
        f.write("## 🗺️ Aree Strategiche (Mappe Master)\n")
        for tt in top_topics:
            f.write(f"- [[Map - {tt}|{tt}]]\n")
            
        f.write("\n---\n\n## 📚 Tutti i Documenti (Indice Alfabetico per Area)\n")
        current_tt = None
        for entry in sorted(index_entries, key=lambda x: (x['top_topic'], x['topic'], x['title'])):
            if entry['top_topic'] != current_tt:
                current_tt = entry['top_topic']
                f.write(f"\n### Area: {current_tt}\n")
            
            f.write(f"- [[{entry['link_path']}|{entry['title']}]] — *({entry['topic']})*\n")

    print(f"Successfully compiled {len(index_entries)} hierarchical wiki articles.")

if __name__ == "__main__":
    process_wiki()

