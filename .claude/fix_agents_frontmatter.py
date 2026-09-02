"""
Fix all agent .md files in .claude/agents/ to have proper Claude Code frontmatter.
Each agent needs:
  ---
  name: filename-without-md
  description: "extracted from content"
  model: haiku|sonnet|opus
  ---
"""
import os
import re

AGENTS_DIR = os.path.dirname(os.path.abspath(__file__)) + "/agents"

# Model mapping based on tier info
TIER_MAP = {
    "opus": "opus",
    "t3": "opus",
    "t3-opus": "opus",
    "sonnet": "sonnet",
    "t2": "sonnet",
    "t2-sonnet": "sonnet",
    "haiku": "haiku",
    "t1": "haiku",
    "t1-haiku": "haiku",
}

def has_proper_frontmatter(content):
    """Check if file already has name + description in YAML frontmatter."""
    if not content.startswith("---"):
        return False
    # Find closing ---
    second_dash = content.find("---", 3)
    if second_dash == -1:
        return False
    front = content[3:second_dash]
    has_name = bool(re.search(r'^name:', front, re.MULTILINE))
    has_desc = bool(re.search(r'^description:', front, re.MULTILINE))
    return has_name and has_desc

def extract_info(content, filename):
    """Extract description and model tier from agent file content."""
    name = filename.replace(".md", "")

    # Try to find role/description from content
    desc_candidates = []

    # Pattern 1: **Ruolo:** text
    m = re.search(r'\*\*Ruolo:\*\*\s*(.+?)(?:\n|$)', content)
    if m:
        desc_candidates.append(m.group(1).strip())

    # Pattern 2: **role:** text (YAML-like in content)
    m = re.search(r'role:\s*(.+?)(?:\n|$)', content)
    if m:
        val = m.group(1).strip()
        if len(val) > 10 and not val.startswith('['):
            desc_candidates.append(val)

    # Pattern 3: ## Identita' section followed by text
    m = re.search(r'## (?:Identit|Identity|Responsabilit).*?\n\n(.+?)(?:\n\n|\n---)', content, re.DOTALL)
    if m:
        text = m.group(1).strip()
        # Take first meaningful line
        for line in text.split('\n'):
            clean = re.sub(r'\*\*.*?\*\*', '', line).strip()
            if len(clean) > 20 and not clean.startswith('#'):
                desc_candidates.append(clean)
                break

    # Pattern 4: First heading content
    m = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if m:
        heading = m.group(1).strip()
        heading = re.sub(r'[^\w\s\-/]', '', heading).strip()  # Remove emojis
        if heading and heading not in [name]:
            desc_candidates.append(heading)

    # Pattern 5: > blockquote description
    m = re.search(r'>\s*(.+?)(?:\n[^>]|\n\n)', content)
    if m:
        bq = m.group(1).strip()
        if len(bq) > 20:
            desc_candidates.append(bq)

    # Build description
    if desc_candidates:
        # Use the longest candidate that's not too long
        desc = max(desc_candidates, key=lambda x: min(len(x), 200))
        # Clean up
        desc = desc.replace('"', "'").replace('\n', ' ').strip()
        desc = re.sub(r'\s+', ' ', desc)
        # Truncate if needed
        if len(desc) > 300:
            desc = desc[:297] + "..."
    else:
        # Fallback: use filename as description
        desc = f"Agente {name} di Digital Empire"

    # Find model tier
    model = "sonnet"  # default
    content_lower = content.lower()

    # Check for tier mentions
    for keyword, tier in [
        ("t3-opus", "opus"), ("tier: opus", "opus"), ("t3", "opus"),
        ("tier modello: 3", "opus"), ("tier modello:** 3", "opus"),
        ("t1-haiku", "haiku"), ("tier: haiku", "haiku"), ("t1", "haiku"),
        ("tier modello: 1", "haiku"), ("tier modello:** 1", "haiku"),
        ("tier modello:** haiku", "haiku"),
    ]:
        if keyword in content_lower:
            model = tier
            break

    # Special overrides based on agent type
    if any(x in name for x in ["sentinel", "guild-cost", "bb-"]):
        model = "haiku"
    if any(x in name for x in ["ceo", "chief-forge"]):
        model = "opus"

    return name, desc, model

def fix_file(filepath, filename):
    """Add proper frontmatter to an agent file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if has_proper_frontmatter(content):
        return False, "already OK"

    name, desc, model = extract_info(content, filename)

    # Remove existing broken frontmatter if present
    if content.startswith("---"):
        second_dash = content.find("---", 3)
        if second_dash != -1:
            old_front = content[3:second_dash]
            content = content[second_dash + 3:].lstrip('\n')

    # Build new frontmatter
    frontmatter = f'---\nname: {name}\ndescription: "{desc}"\nmodel: {model}\n---\n\n'

    new_content = frontmatter + content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, f"name={name} model={model}"

def main():
    fixed = 0
    skipped = 0
    errors = 0

    files = sorted(os.listdir(AGENTS_DIR))

    for filename in files:
        if not filename.endswith('.md'):
            continue

        filepath = os.path.join(AGENTS_DIR, filename)

        try:
            changed, info = fix_file(filepath, filename)
            if changed:
                fixed += 1
                print(f"FIXED: {filename} -> {info}")
            else:
                skipped += 1
                print(f"SKIP:  {filename} ({info})")
        except Exception as e:
            errors += 1
            print(f"ERROR: {filename} -> {e}")

    print(f"\n=== RISULTATO ===")
    print(f"Fixed:   {fixed}")
    print(f"Skipped: {skipped}")
    print(f"Errors:  {errors}")
    print(f"Total:   {fixed + skipped + errors}")

if __name__ == "__main__":
    main()
