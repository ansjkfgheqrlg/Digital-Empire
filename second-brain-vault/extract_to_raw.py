import os
import sys
import datetime
import fitz  # PyMuPDF
from slugify import slugify

# Paths
ROOT_DIR = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire"
VAULT_DIR = os.path.join(ROOT_DIR, "second-brain-vault")
RAW_DIR = os.path.join(VAULT_DIR, "raw")

# Ignore these directories recursively
IGNORE_DIRS = {
    "second-brain-vault",
    ".git",
    ".obsidian",
    ".claude",
    "node_modules",
    ".next",
    "dist",
    "build",
    "venv",
    ".venv",
    "__pycache__"
}

# Allowed extensions
ALLOWED_EXTS = {".pdf", ".md", ".txt", ".json", ".canvas", ".csv"}

def get_topic(file_path):
    # Get the relative path from ROOT_DIR, excluding the filename
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    dir_path = os.path.dirname(rel_path)
    if dir_path and dir_path != ".":
        # Keep the original folder names but handle separators
        return dir_path
    return "general"

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
        return ""

def extract_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Try a different encoding if utf-8 fails
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading text file {file_path}: {e}")
            return ""

def process_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext not in ALLOWED_EXTS:
        return False
        
    topic = get_topic(file_path)
    filename = os.path.basename(file_path)
    title = os.path.splitext(filename)[0]
    
    # Extract text
    content = ""
    if ext == ".pdf":
        content = extract_text_from_pdf(file_path)
    else:
        content = extract_text_from_file(file_path)
        
    if not content or not content.strip():
        return False # Skip empty files
        
    # Prepare destination
    topic_dir = os.path.join(RAW_DIR, topic)
    os.makedirs(topic_dir, exist_ok=True)
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    
    dest_filename = f"{today}-{slug}.md"
    dest_path = os.path.join(topic_dir, dest_filename)
    
    # If file exists, append a counter
    counter = 1
    while os.path.exists(dest_path):
        dest_filename = f"{today}-{slug}-{counter}.md"
        dest_path = os.path.join(topic_dir, dest_filename)
        counter += 1
        
    # Format template
    # Original path relative to root for source description
    rel_source = os.path.relpath(file_path, ROOT_DIR)
    
    template = f"""# {title}

> Source: File system (`{rel_source}`)
> Collected: {today}
> Published: Unknown

{content.strip()}
"""

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(template)
        
    try:
        print(f"Ingested: {rel_source} -> raw/{topic}/{dest_filename}")
    except UnicodeEncodeError:
        print(f"Ingested: [Encoding Error in Path] -> raw/{topic}/{dest_filename}")
    return True

def main():
    # Force UTF-8 for output if possible
    if sys.stdout.encoding != 'utf-8':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        
    if not os.path.exists(RAW_DIR):
        os.makedirs(RAW_DIR)
        
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        # Recursively skip ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        # Also skip if current root itself should be ignored (extra safety)
        if any(ignored in root.split(os.sep) for ignored in IGNORE_DIRS):
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            if process_file(file_path):
                count += 1
                
    print(f"\nSuccessfully extracted and ingested {count} files into raw/.")

if __name__ == "__main__":
    main()
