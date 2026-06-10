import fitz
import os

pdf_path = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\MANUALE COMPLETO DI CLAUDE CODE PER IL BUSINESS.pdf"
output_path = r"c:\Users\Utente\Desktop\qui tutto\Digital Empire\second-brain-vault\manuale_raw_v2.txt"

def extract_all():
    doc = fitz.open(pdf_path)
    full_text = []
    for i in range(len(doc)):
        page_text = doc[i].get_text()
        full_text.append(f"\n--- PAGE {i} ---\n")
        full_text.append(page_text)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("".join(full_text))
    print(f"Extracted {len(doc)} pages to {output_path}")

if __name__ == "__main__":
    extract_all()
