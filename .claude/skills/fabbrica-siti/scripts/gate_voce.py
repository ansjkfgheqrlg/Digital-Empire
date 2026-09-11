#!/usr/bin/env python3
"""gate_voce.py — il gate della voce (Dossier 37, Asse A / C1.4).

Deterministico: quattro controlli su un COPY.md diviso in sezioni (`## N…`). Exit 0 = PASS, 1 = FAIL.

  1. LISTA NERA     nessuna parola vietata (VOCE.md V10)
  2. LA PROVOCAZIONE PAGA  ogni frase che finisce con "?" o che e' esattamente "No." ha, entro
                    200 caratteri dopo, una cifra, un %, un € o una data — altrimenti e' una
                    provocazione senza numero (V3/V4)
  3. PARLA UNA PERSONA  almeno un pronome/verbo di prima persona per sezione (V1)
  4. ZERO BARNUM    nessuna delle formule universali (V8)

Uso:  python gate_voce.py <COPY.md> [--sezioni-esenti N19,N3]
"""
import re, sys, argparse, pathlib, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")  # console cp1252

LISTA_NERA = ["stronz", "cazz", "cagat", " mid ", "brokie", "lol", " jk", "daddy", "merd", "fottut"]
BARNUM = [
    "se sei qui è perché", "se sei qui e' perche'", "senti il peso", "sei disinformato", "non sei tu che sei",
    "meriti di più", "meriti di piu'", "il tuo potenziale", "libertà finanziaria", "cambiare vita",
]
PRIMA_PERSONA = re.compile(r"\b(io|noi|ho|abbiamo|ci|mi|nostr[oaie]|mio|mia|installiamo|costruiamo|facciamo|siamo|ti diciamo|ti mostriamo|ti garantiamo|rifacciamo|proponiamo|mettiamo|vediamo|stiamo)\b", re.I)
NUMERO = re.compile(r"\d|%|€")

# le sezioni le cui domande sono titoli di FAQ/obiezioni: la risposta e' la frase dopo, dentro i 200 char
def sezioni(testo: str):
    parti = re.split(r"^## (N\d+[^\n]*)$", testo, flags=re.M)
    out = []
    for i in range(1, len(parti), 2):
        out.append((parti[i].strip(), parti[i + 1]))
    return out

def pulisci(riga: str) -> str:
    riga = re.sub(r"^\[[^\]]+\]\s*", "", riga)        # [ruolo]
    riga = re.sub(r"\*\*|\*|«|»|“|”", "", riga)         # grassetti, virgolette tipografiche
    return riga.strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("copy")
    ap.add_argument("--sezioni-esenti", default="N19", help="sezioni senza obbligo di prima persona (es. coda legale)")
    a = ap.parse_args()
    testo = pathlib.Path(a.copy).read_text(encoding="utf-8")
    esenti = set(x.strip() for x in a.sezioni_esenti.split(",") if x.strip())
    errori = []

    # 1 — lista nera, su tutto il file
    basso = " " + testo.lower() + " "
    for p in LISTA_NERA:
        if p in basso:
            errori.append(f"LISTA NERA: «{p.strip()}» compare nel copy")

    # 4 — Barnum, su tutto il file
    for b in BARNUM:
        if b in basso:
            errori.append(f"BARNUM: «{b}» compare nel copy")

    for titolo, corpo in sezioni(testo):
        nome = titolo.split()[0]
        # righe di testo: solo quelle che iniziano con [ruolo] (le righe **meta** in grassetto si saltano)
        righe = [pulisci(r) for r in corpo.splitlines() if r.startswith("[")]
        piatto = " ".join(righe)
        # le domande del lettore ([q], [q1]…, [dm]) sono parole sue, non provocazioni nostre: escluse dal controllo 2
        nostre = " ".join(pulisci(r) for r in corpo.splitlines() if r.startswith("[") and not re.match(r"\[(q\d*|dm)\]", r))

        # 3 — prima persona
        if nome not in esenti and not PRIMA_PERSONA.search(piatto):
            errori.append(f"{nome}: nessuna prima persona (V1)")

        # 2 — la provocazione paga: frasi con "?" o "No." → numero entro 200 char
        for m in re.finditer(r"[^.?!]*\?|(?<![\w])No\.", nostre):
            fine = m.end()
            dopo = nostre[fine:fine + 200]
            if not NUMERO.search(dopo):
                frase = m.group(0).strip()
                errori.append(f"{nome}: provocazione senza numero entro 200 caratteri -> «{frase[:70]}»")

    if errori:
        print("GATE VOCE -- FAIL")
        for e in errori:
            print("  [X]", e)
        sys.exit(1)
    print(f"GATE VOCE -- PASS ({len(sezioni(testo))} sezioni, lista nera 0, Barnum 0, prima persona ok, provocazioni pagate)")
    sys.exit(0)

if __name__ == "__main__":
    main()
