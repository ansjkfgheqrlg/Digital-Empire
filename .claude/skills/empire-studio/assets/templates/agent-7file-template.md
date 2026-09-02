# Template - I 7 file canonici di un agente Empire Studio

Ogni agente vive in `agents/<reparto>/<nome>/` e ha ESATTAMENTE questi 7 file,
ognuno SOSTANZIALE (>= 12 righe, >= 400 char, niente marker proibiti). Questo
file mostra la struttura attesa di ciascuno. Gli agenti reali costruiti in Fase 1
(es. `agents/youtube-department/yt-channel-ingester/`) sono il modello vivo.

---

## 1. `<nome>.md` - Spec
```
# <nome> (L3 - <Reparto>)

**Ruolo:** una frase precisa.
**Reparto:** <reparto> · **Livello:** L3 · **Lead:** <department-lead>
**Skill usate:** <tier2 skill che impugna, con path>
**Input (handoff in):** <cosa riceve dal lead/conductor, schema>
**Output (handoff out):** <cosa produce, path, schema>
**Quando si attiva:** <trigger>
**Trace (P12):** a quale requisito utente / principio risponde.
```

## 2. `system-prompt.md` - Prompt operativo (in italiano)
Identita', regole non negoziabili (gli invarianti rilevanti), tono, cosa fa e
cosa NON fa, come riporta al lead. E' il testo che Claude assume quando "diventa"
questo agente.

## 3. `tools.md` - Strumenti
Tool/CLI/script che usa con comandi esatti (es. `python scripts/yt_ingest.py
--input ... --output ...`), schemi I/O in JSON, e i memory hook (quale CP/stato
aggiorna).

## 4. `playbook.md` - Passi + esempi
Sequenza operativa passo-passo + 3-5 esempi reali (happy / edge / failure-recovery)
ancorati ai casi d'uso dell'utente (video design, canale marketing, repo, ...).

## 5. `evals.md` - Casi di test
5+ casi discriminanti con prompt, output atteso, criterio di voto (es. "frame
reali presenti? descrizioni non generiche? trace su ogni atomo?"), target di voto.

## 6. `failure-modes.md` - Tabella (P09)
| Failure | Sintomo | Prevenzione | Detection | Recovery |
Almeno 5 righe reali specifiche dell'agente.

## 7. `memory.md` - Protocollo memory (P10)
Cosa registra in `memory/` e quando: quali CP/DEC/stati, in quali categorie,
con quale trace. Esempio: "dopo l'ingest -> CP in checkpoints + entry in
knowledge-state + agent-state".

---

**Regola d'oro:** il `validator.py` rifiuta qualunque di questi file se e' troppo
corto o contiene marker proibiti. Un agente non e' "fatto" finche' i 7 file non
passano il validator.
