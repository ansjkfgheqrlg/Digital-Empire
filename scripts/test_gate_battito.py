#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_gate_battito.py — prova vera del gate del battito (scripts/gate_battito_hook.py).

Non verifica che il file esista: gli costruisce sotto un transcript finto per ogni caso e
guarda cosa risponde davvero. Dal 7º giro (2026-09-09) la regola sul blocco di codice si e'
invertita di nuovo: il battito vero e' una TABELLA markdown, MAI dentro ``` (il 6º giro
voleva il contrario, bocciato da Max sull'aspetto — vedi verifica_recap.py). I casi 4, 5 e
9-10 sono quelli che decidono se il gate distingue bene una CONSEGNA vera da un ESEMPIO di
documentazione, e se blocca davvero un fence.

    py -3 scripts/test_gate_battito.py
"""

import io
import json
import os
import subprocess
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass  # console senza reconfigure (Python vecchio): meglio provarci che bloccare il test

QUI = os.path.dirname(os.path.abspath(__file__))
HOOK = os.path.join(QUI, "gate_battito_hook.py")
if QUI not in sys.path:
    sys.path.insert(0, QUI)
from verifica_recap import costruisci, costruisci_missione  # noqa: E402

MISSIONE_OK = costruisci_missione(
    "scrivo il modulo di export PDF",
    "PDF pronto senza passare da Canva",
    ["motore HTML->PDF", "template con logo", "test su 3 preventivi veri"],
)

MISSIONE_ROTTA = """🔴 **Sto facendo:** scrivo il modulo
🔴 **Obiettivo:**
🔴 Fasi:
│
├─🔴→ fase 1
├─🔴→ fase 2"""

BATTITO_OK = costruisci(
    "letto il libro, trovato il punto che cede",
    "costruisco il controllo automatico",
    "lo provo su sei casi veri",
    "nessuna, sto lavorando da solo",
    "normale", 100, 40,
)

BATTITO_ROTTO = """**⏱️ RECAP — 40%**

| |
|:---:|
| 🟩 Fatto: |
| letto il libro |
| - Sto facendo: costruisco il controllo |
| 🟩 Farò: |
| lo provo |
| 🟩 Forze: |
| nessuna |
| ↓ |
| 🟩 Assetto: |
| acceso |
| 🟩 Potere: tanto% |"""


def transcript(testo_assistente, chiesto="vai"):
    """`testo_assistente` puo' essere una stringa o una LISTA di blocchi di testo.

    La lista serve a riprodurre un turno lungo: piu' messaggi dell'assistente intervallati
    da strumenti, che e' esattamente lo scenario in cui il gate ha sbagliato la prima volta.
    """
    fd, percorso = tempfile.mkstemp(suffix=".jsonl")
    os.close(fd)
    pezzi = testo_assistente if isinstance(testo_assistente, list) else [testo_assistente]
    righe = [{"type": "user", "message": {"role": "user", "content": chiesto}}]
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


def esegui(testo, stop_attivo=False, chiesto="vai"):
    percorso = transcript(testo, chiesto)
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

    ("2. battito conforme, tabella, in cima, NESSUN fence -> passa",
     BATTITO_OK + "\n\nDettagli sotto, come sempre.", False, False),

    ("3. battito rotto (tabella malformata), in cima -> BLOCCA (problemi di forma)",
     BATTITO_ROTTO, False, True),

    ("4. battito conforme ma dentro ``` -> BLOCCA (vietato dal 7º giro)",
     "```\n" + BATTITO_OK + "\n```\n\nDettagli sotto.", False, True),

    ("5. battito conforme (tabella) ma NON in cima -> BLOCCA (posizione)",
     "Prima ti racconto la bella notizia, poi il battito.\n\n" + BATTITO_OK,
     False, True),

    ("6. esempio dentro ``` con prosa PRIMA E DOPO (documentazione) -> passa",
     "Lo schema del battito e' questo:\n\n```\n" + BATTITO_ROTTO + "\n```\n\nChiaro?", False, False),

    ("7. battito rotto ma stop_hook_active -> passa (anti-loop)",
     BATTITO_ROTTO, True, False),

    # --- il caso pagato in produzione, 2026-09-05 sera ---
    ("8. turno lungo: messaggi intermedi + battito (tabella, no fence) in cima all'ultimo -> passa",
     ["Ricevuto, Max. Parto col lavoro.",
      "Ho finito la prima parte, ora salvo.",
      BATTITO_OK + "\n\nChiuso, il codice e' EMP-RWKX."], False, False),

    ("9. turno lungo ma il battito e' sotto la prosa nel SUO messaggio -> BLOCCA",
     ["Parto col lavoro.",
      "Ti racconto prima com'e' andata, poi il battito.\n\n" + BATTITO_OK],
     False, True),

    # --- il caso pagato in produzione, 2026-09-09 (7º giro: la regola del fence si e' invertita) ---
    ("10. battito vero come tabella, senza altro testo -> passa (ORA e' il formato giusto)",
     BATTITO_OK, False, False),

    # --- il caso pagato in produzione, 2026-09-09 (5º giro: niente piu' bordo) ---
    ("11. battito con Forze ad albero (gruppi nominati), tabella, no fence -> passa",
     costruisci(
         "chiuso il lavoro sui gruppi", "niente altro", "niente in sospeso",
         [("sentinelle", ["controlla budget", "controlla secret"]),
          ("doom bot", ["autoripara i test"])],
         "GOD EMPEROR DOOM", 100, 90,
     ) + "\n\nFatto.", False, False),

    # --- Missione (§6.11, ordine di Max 2026-09-09) ---
    ("12. Missione conforme, in cima, no fence -> passa",
     MISSIONE_OK + "\n\nDettagli sopra.", False, False),

    ("13. Missione rotta (Obiettivo vuoto, manca l'ultima fase) -> BLOCCA",
     MISSIONE_ROTTA, False, True),

    ("14. Missione conforme ma dentro ``` -> BLOCCA (stesso motivo del battito)",
     "```\n" + MISSIONE_OK + "\n```", False, True),

    ("15. Missione conforme ma NON in cima -> BLOCCA (posizione)",
     "Prima ti dico una cosa.\n\n" + MISSIONE_OK, False, True),

    # --- casi 16-17, aggiunti il 2026-09-10 dopo un fallimento in produzione ---
    # Max ha scritto `Missione`, Emperator ha risposto a braccio, e il gate ha taciuto:
    # sapeva validare una Missione malfatta, non accorgersi di una Missione MANCANTE.
    ("16. Max chiede `Missione` e la risposta non ne porta nessuna -> BLOCCA (era dovuta)",
     "Ti riassumo lo stato del lavoro in una tabella, con le percentuali.", False, True,
     "Missione"),

    ("17. `missione` dentro una frase (non e' il comando) -> passa",
     "Ti riassumo lo stato del lavoro.", False, False,
     "a che punto e' la missione secondo te?"),
]


def main():
    esiti = []
    for caso in CASI:
        nome, testo, stop_attivo, deve_bloccare = caso[:4]
        chiesto = caso[4] if len(caso) > 4 else "vai"
        r = esegui(testo, stop_attivo, chiesto)
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
