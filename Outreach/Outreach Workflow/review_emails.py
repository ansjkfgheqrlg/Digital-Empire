"""
Viewer terminale per emails_ready.json.
Mostra ogni email numerata con oggetti alternativi, corpo completo e separatori.
Usalo per revisionare prima di inviare.

Run:
  python review_emails.py
  python review_emails.py > emails_preview.txt   # salva su file
"""
import json
import sys

INPUT_PATH = "emails_ready.json"


def main():
    with open(INPUT_PATH, encoding="utf-8") as f:
        emails = json.load(f)

    ready  = [e for e in emails if e.get("status") == "ready"]
    totale = len(emails)

    print(f"\n{'='*65}")
    print(f"  emails_ready.json — {len(ready)} pronte su {totale} totali")
    print(f"{'='*65}")

    # Raggruppa per nicchia
    per_nicchia: dict[str, list] = {}
    for e in ready:
        n = e.get("nicchia", "altro")
        per_nicchia.setdefault(n, []).append(e)

    print("\nNicchie:")
    for n, lst in sorted(per_nicchia.items()):
        print(f"  {n:<20} {len(lst):>2} email")
    print()

    for i, e in enumerate(ready, 1):
        print(f"\n{'-'*65}")
        print(f"  #{i:02d}  [{e.get('nicchia','?')}]  {e['page_name']}")
        print(f"  To: {e['email']}  |  {e.get('citta','')}")
        print(f"{'-'*65}")
        print(f"\nOGGETTO A: {e['oggetto']}")
        if e.get("oggetto_b"):
            print(f"OGGETTO B: {e['oggetto_b']}")
        if e.get("oggetto_c"):
            print(f"OGGETTO C: {e['oggetto_c']}")
        print(f"\n{e['corpo']}")

    print(f"\n{'='*65}")
    print(f"  Fine — {len(ready)} email pronte")
    print(f"  Prossimo step: python send_ready.py")
    print(f"{'='*65}\n")


if __name__ == "__main__":
    main()
