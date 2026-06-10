import os
import re

WIKI_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\wiki"
KB_DIR = os.path.join(WIKI_DIR, "Knowledge_Base")

KEYWORDS = {
    "Agency": "Map - Agency Empire",
    "Funnel": "Map - Infobusiness",
    "Webinar": "Map - Infobusiness",
    "Outreach": "Map - Outreach",
    "Claude": "Map - Progetti Claude",
    "Skill": "Map - Skill Agenti",
    "Marketing": "Map - Marketing Ai",
    "Siti": "Map - Crea Siti",
    "Lancio": "Map - Lancio Corso Skill Beast",
    "Ebook": "Map - Lanco Ebook"
}

def interlink():
    files = [f for f in os.listdir(KB_DIR) if f.endswith('.md')]
    count = 0
    
    for filename in files:
        path = os.path.join(KB_DIR, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        # Add a "See Also" section at the end based on keywords found in content
        related = []
        for kw, target in KEYWORDS.items():
            if kw.lower() in content.lower() and target not in filename:
                related.append(f"[[{target}|{kw} Hub]]")
        
        if related:
            related = list(set(related)) # Dedupe
            content += "\n\n## Related Hubs\n" + ", ".join(related) + "\n"
            modified = True
            
        if modified:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            
    print(f"Interlinked {count} files with Hub maps.")

if __name__ == "__main__":
    interlink()
