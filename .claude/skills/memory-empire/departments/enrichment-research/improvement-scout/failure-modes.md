# Failure Modes — improvement-scout

## FM-01: Troppi miglioramenti generici
**Causa:** Scout troppo "creativo" senza evidenza reale
**Fix:** Ogni improvement deve avere evidence = citazione diretta dall'atom. Se non c'è citazione, non è un improvement.

## FM-02: Duplicazione con gap-analyzer
**Causa:** Scout trova le stesse lacune del gap-analyzer
**Fix:** Confronta gaps.json prima di generare. Se l'improvement è già in gaps.json → skip.

## FM-03: Target skill non esistente
**Causa:** Scout propone miglioramento a una skill che non esiste
**Fix:** Verifica che `~/.claude/skills/<target>/SKILL.md` esista prima di inserirla.

## FM-04: Scout non trova nulla ma esistono miglioramenti ovvi
**Causa:** Confidence threshold troppo alto o dominio troppo ristretto
**Fix:** Espandi la scansione alle skill adiacenti. Abbassa il threshold mentale a 0.5 in prima analisi.
