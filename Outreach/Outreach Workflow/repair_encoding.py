import json

def fix_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    
    # Se il file contiene nulls tra i caratteri (UTF-16-LE scambiato per UTF-8)
    if b'\x00' in content:
        print("Rilevato UTF-16/Nulls, tento la conversione...")
        try:
            # Prova a decodificare come UTF-16
            text = content.decode('utf-16')
            # E poi ricodificare come UTF-8 pulito
            content = text.encode('utf-8')
        except:
            # Rimuovi solo i nulls se non è vero UTF-16
            content = content.replace(b'\x00', b'')
    
    try:
        data = json.loads(content.decode('utf-8', errors='ignore'))
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"File {path} riparato con successo.")
    except Exception as e:
        print(f"Errore riparazione: {e}")

if __name__ == "__main__":
    fix_file('emails_perfect_batch.json')
