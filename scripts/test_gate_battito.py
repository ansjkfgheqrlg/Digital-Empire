#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_gate_battito.py — prova vera del gate del battito (scripts/gate_battito_hook.py).

Non verifica che il file esista: gli costruisce sotto un transcript finto per ogni caso e
guarda cosa risponde davvero. I sei casi sono quelli che decidono se il gate e' utile o
dannoso -- soprattutto il quinto, che e' quello che lo renderebbe insopportabile se sbagliato.

    py -3 scripts/test_gate_battito.py
"""

import io
import json
import os
import subprocess
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
HOOK = os.path.join(QUI, "gate_battito_hook.py")

BATTITO_OK = """**⏱️ RECAP — 40%**

🟠 **Fatto:** letto il libro e trovato il punto che cede
🟠 **Sto facendo:** costruisco il controllo che scatta da solo
🟠 **Farò:** lo provo su sei casi veri prima di dirlo fatto
🟠 **Forze:** nessuna, sto lavorando da solo
🟠 **Assetto:** normale
🟠 **Potere:** 100%"""

BATTITO_ROTTO = """**⏱️ RECAP — 40%**
🟠 **Fatto:** letto il libro
- Sto facendo: costruisco il controllo
🟠 **Farò:** lo provo
🟠 **Forze:** nessuna
🟠 **Assetto:** acceso
🟠 **Potere:** tanto%"""


def transcript(testo_assistente):
    fd, percorso = tempfile.mkstemp(suffix=".jsonl")
    os.close(fd)
    righe = [
        {"type": "user", "message": {"role": "user", "content": "vai"}},
        {"type": "assistant", "message": {"role": "assistant",
                                          "content": [{"type": "text", "text": testo_assistente}]}},
    ]
    with io.open(percorso, "w", encoding="utf-8") as f:
        for r in righe:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return percorso


def esegui(testo, stop_attivo=False):
    percorso = transcript(testo)
    try:
        payload = {"transcript_path": percorso, "stop_hook_active": stop_attivo}
        p = subprocess.run([sys.executable, HOOK],
                           input=json.dumps(payload).encode("utf-8"),
                           capture_output=True)
        out = p.stdout.decode("utf-8", "replace").strip()
        if not out:
            return None
        return json.loads(out)
    finally:
        try:
            os.unlink(percorso)
        except Exception:
            pass


CASI = [
    ("1. messaggio senza battito -> passa",
     "Max, ho finito il lavoro. Il file e' salvato e pushato.", False, False),

    ("2. battito conforme in cima -> passa",
     BATTITO_OK + "\n\nDettagli sotto, come sempre.", False, False),

    ("3. battito rotto -> BLOCCA",
     BATTITO_ROTTO, False, True),

    ("4. battito conforme ma NON in cima -> BLOCCA",
     "Prima ti racconto la bella notizia, poi il battito.\n\n" + BATTITO_OK, False, True),

    ("5. esempio dentro ``` (documentazione) -> passa",
     "Lo schema del battito e' questo:\n\n```\n" + BATTITO_ROTTO + "\n```\n\nChiaro?", False, False),

    ("6. battito rotto ma stop_hook_active -> passa (anti-loop)",
     BATTITO_ROTTO, True, False),
]


def main():
    esiti = []
    for nome, testo, stop_attivo, deve_bloccare in CASI:
        r = esegui(testo, stop_attivo)
        ha_bloccato = bool(r and r.get("decision") == "block")
        ok = (ha_bloccato == deve_bloccare)
        esiti.append(ok)
        print("%s  %s" % ("OK  " if ok else "FALLITO", nome))
        if not ok:
            print("     atteso blocco=%s, ottenuto=%s" % (deve_bloccare, ha_bloccato))
        elif ha_bloccato:
            prima = [x for x in r["reason"].split("\n") if x.strip().startswith("-")][:3]
            for x in prima:
                print("       %s" % x.strip())

    print("")
    print("%d/%d casi passati" % (sum(esiti), len(esiti)))
    return 0 if all(esiti) else 1


if __name__ == "__main__":
    sys.exit(main())
