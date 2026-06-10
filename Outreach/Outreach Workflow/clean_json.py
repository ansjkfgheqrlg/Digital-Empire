import json
import os

def clean_mojibake(text):
    if not text: return text
    # Fix common mojibake from windows-1252 to utf-8 interpretation
    replacements = {
        "": "à", # This is a guess, but often  in Italian contexts is à, è, ì, ò, ù
        "Ǹ": "à",
        "": "è",
        "": "é",
        "": "ì",
        "": "ò",
        "": "ù",
        "'": "à",
        "^": "è",
        "_": "ù",
        "Ǹ": "à",
    }
    # Actually, a better way is to handle the known corruptions I saw:
    # "perchǸ" -> "perché"
    # "gi" -> "già"
    # "pi" -> "più"
    # "^" -> "è"
    text = text.replace("perchǸ", "perché")
    text = text.replace("gi", "già")
    text = text.replace("pi", "più")
    text = text.replace("^", "è")
    text = text.replace("", "à") # generic fallback for common italian accented char
    return text

def clean_file(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        if 'corpo' in item:
            item['corpo'] = clean_mojibake(item['corpo'])
        if 'oggetto' in item:
            item['oggetto'] = clean_mojibake(item['oggetto'])
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"File {file_path} pulito dai caratteri corrotti.")

if __name__ == "__main__":
    clean_file('emails_perfect_batch.json')
