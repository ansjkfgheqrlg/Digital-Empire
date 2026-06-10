"""
Fix deliverability: rimuove i link https://agency-empire-landing.vercel.app
dalle email B6 già preparate (prima email fredda → ZERO link).
Il link andrà solo nel follow-up #2 (giorno 7).

Run: python fix_b6_remove_links.py
"""
import json, re

LINK = "https://agency-empire-landing.vercel.app"
FILES = ["emails_b6_ready.json", "emails_b5_ready.json"]

for fname in FILES:
    try:
        with open(fname, encoding="utf-8", errors="replace") as f:
            emails = json.load(f)
    except Exception as e:
        print(f"Skip {fname}: {e}")
        continue

    fixed = 0
    for email in emails:
        corpo = email.get("corpo", "")
        if LINK in corpo:
            # Rimuove la riga intera che contiene il link
            lines = corpo.split("\n")
            new_lines = [l for l in lines if LINK not in l]
            # Rimuove righe vuote consecutive in eccesso
            cleaned = re.sub(r'\n{3,}', '\n\n', "\n".join(new_lines)).strip()
            email["corpo"] = cleaned
            fixed += 1

    with open(fname, "w", encoding="utf-8") as f:
        json.dump(emails, f, ensure_ascii=False, indent=2)

    print(f"{fname}: rimosso link da {fixed}/{len(emails)} email")

print("\nFatto! Le email B6 ora non hanno link nella prima email fredda.")
print("Il link https://agency-empire-landing.vercel.app va nel follow-up #2 (giorno 7).")
