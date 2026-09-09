#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_gate_battito.py — prova vera del gate del battito (scripts/gate_battito_hook.py).

Non verifica che il file esista: gli costruisce sotto un transcript finto per ogni caso e
guarda cosa risponde davvero. Dal 6º giro (2026-09-09) la regola sul blocco di codice si e'
invertita: il battito vero DEVE stare dentro ``` in cima al messaggio (prima girava il
contrario). I casi 6 e 9-10 sono quelli che decidono se il gate distingue bene una
CONSEGNA vera da un ESEMPIO di documentazione.

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
if QUI not in sys.path:
    sys.path.insert(0, QUI)
from verifica_recap import costruisci  # noqa: E402  (dopo l'import di sys/os sopra)

BATTITO_OK = costruisci(
    "letto il libro, trovato il punto che cede",
    "costruisco il controllo automatico",
    "lo provo su sei casi veri",
    "nessuna, sto lavorando da solo",
    "normale", 100, 40,
)

BATTITO_ROTTO = """**⏱️ RECAP — 40%**
🟠 Fatto:
letto il libro
- Sto facendo: costruisco il controllo
🟠 Farò:
lo provo
🟠 Forze:
nessuna
↓
🟠 Assetto:
acceso
🟠 Potere: tanto%"""


def transcript(testo_assistente):
    """`testo_assistente` puo' essere una stringa o una LISTA di blocchi di testo.

    La lista serve a riprodurre un turno lungo: piu' messaggi dell'assistente intervallati
    da strumenti, che e' esattamente lo scenario in cui il gate ha sbagliato la prima volta.
    """
    fd, percorso = tempfile.mkstemp(suffix=".jsonl")
    os.close(fd)
    pezzi = testo_assistente if isinstance(testo_assistente, list) else [testo_assistente]
    righe = [{"type": "user", "message": {"role": "user", "content": "vai"}}]
    for i, t in enumerate(pezzi):
        righe.append({"type": "assistant", "message": {"role": "assistant",
                                                       "content": [{"type": "text", "text": t}]}})
        if i < len(pezzi) - 1:
            # fra un messaggio e l'altro c'e' uno strumento, come nella vita vera
            righe.append({"type": "assistant", "message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "t%d" % i, "name": "Bash", "input": {}}]}})
            righe.append({"type": "user", "message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "t%d" % i, "content": "ok"}]}})
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

    ("2. battito conforme, dentro ``` in cima -> passa",
     "```\n" + BATTITO_OK + "\n```\n\nDettagli sotto, come sempre.", False, False),

    ("3. battito rotto, dentro ``` in cima -> BLOCCA (problemi di forma)",
     "```\n" + BATTITO_ROTTO + "\n```", False, True),

    ("4. battito conforme ma NON dentro ``` -> BLOCCA (manca il blocco di codice)",
     BATTITO_OK, False, True),

    ("5. battito conforme dentro ``` ma NON in cima -> BLOCCA (posizione)",
     "Prima ti racconto la bella notizia, poi il battito.\n\n```\n" + BATTITO_OK + "\n```",
     False, True),

    ("6. esempio dentro ``` con prosa PRIMA E DOPO (documentazione) -> passa",
     "Lo schema del battito e' questo:\n\n```\n" + BATTITO_ROTTO + "\n```\n\nChiaro?", False, False),

    ("7. battito rotto ma stop_hook_active -> passa (anti-loop)",
     "```\n" + BATTITO_ROTTO + "\n```", True, False),

    # --- il caso pagato in produzione, 2026-09-05 sera ---
    ("8. turno lungo: messaggi intermedi + battito dentro ``` in cima all'ultimo -> passa",
     ["Ricevuto, Max. Parto col lavoro.",
      "Ho finito la prima parte, ora salvo.",
      "```\n" + BATTITO_OK + "\n```\n\nChiuso, il codice e' EMP-RWKX."], False, False),

    ("9. turno lungo ma il battito e' sotto la prosa nel SUO messaggio -> BLOCCA",
     ["Parto col lavoro.",
      "Ti racconto prima com'e' andata, poi il battito.\n\n```\n" + BATTITO_OK + "\n```"],
     False, True),

    # --- il caso pagato in produzione, 2026-09-09 (6º giro: la regola si e' invertita) ---
    ("10. battito vero dentro ``` senza altro testo -> passa (ORA e' il formato giusto)",
     "```\n" + BATTITO_OK + "\n```", False, False),

    # --- il caso pagato in produzione, 2026-09-09 (5º giro: niente piu' bordo) ---
    ("11. battito con Forze ad albero (gruppi nominati), dentro ``` -> passa",
     "```\n" + costruisci(
         "chiuso il lavoro sui gruppi", "niente altro", "niente in sospeso",
         [("sentinelle", ["controlla budget", "controlla secret"]),
          ("doom bot", ["autoripara i test"])],
         "GOD EMPEROR DOOM", 100, 90,
     ) + "\n```\n\nFatto.", False, False),
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
