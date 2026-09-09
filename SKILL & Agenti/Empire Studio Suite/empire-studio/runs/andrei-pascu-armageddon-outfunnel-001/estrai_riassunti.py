# -*- coding: utf-8 -*-
"""Estrae 'In questa lezione...' + 'Riassunto lezione' da ogni _page_raw.txt in un unico file."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.join(HERE, "lessons")

out = []
for n in range(1, 21):
    d = os.path.join(LESSONS, f"lezione-{n:02d}")
    raw_path = os.path.join(d, "_page_raw.txt")
    if not os.path.isfile(raw_path):
        continue
    with open(raw_path, encoding="utf-8") as f:
        testo = f.read()

    start = testo.find("In questa lezione")
    end = testo.find("Completa e continua", start if start >= 0 else 0)
    if start == -1:
        corpo = "[NON TROVATO 'In questa lezione']\n" + testo[:800]
    else:
        corpo = testo[start:end if end != -1 else start + 6000].strip()

    out.append(f"\n\n{'='*90}\n### LEZIONE {n:02d}\n{'='*90}\n{corpo}\n")

with open(os.path.join(HERE, "_TUTTI_I_RIASSUNTI.md"), "w", encoding="utf-8") as f:
    f.write("".join(out))

print(f"[OK] scritto _TUTTI_I_RIASSUNTI.md, {len(out)} lezioni")
