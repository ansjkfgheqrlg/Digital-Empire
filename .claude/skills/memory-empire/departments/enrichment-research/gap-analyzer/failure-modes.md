# Failure Modes — gap-analyzer

## FM-01: Falso positivo (contenuto già presente)
**Fix:** Read completo del file prima di dichiarare gap. Se in dubbio → non è un gap.

## FM-02: Skill file troppo lungo per leggere tutto
**Fix:** Leggi almeno le prime 100 righe + cerca con Grep le keywords dell'atom.
