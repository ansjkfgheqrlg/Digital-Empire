# Esempio end-to-end — target `doc`

> Esempio realistico di output prodotto da `B1 doc-builder-agent` partendo dal sorgente comune `assets/examples/_shared/source.md` + MKD `master.md`.

## Input

- Sorgente: `_shared/source.md` (~720 parole, transcript workshop "Prompt Engineering Avanzato")
- KG: `_shared/kg.json` (12 atomi, 3 cluster)
- MKD: `_shared/master.md` (1050 parole, già completo)
- ASK answers utente:
  - Audience: "ingegneri ML in produzione (senior)"
  - Registro: "tecnico-pratico"
  - Lingua: italiano
  - Lunghezza: piena (default ≥ MKD)
  - Glossario: sì, file separato
  - FAQ: sì, da steel-manning
  - Schemi: mermaid

## Output (cosa B1 produce)

```
doc/
├── document.md         # MKD adattato con frontmatter customizzato + tono per audience senior
├── glossary.md         # 8 termini chiave + definizioni
├── faq.md              # 6 domande generate da steel-manning di claim non banali
├── changelog.md
└── README.md           # questo file
```

## Nota: B1 come "MKD adapter"

Dopo l'introduzione del MKD in PLAN-v5, il `doc-builder` non scrive il documento da zero. Adatta il `master.md` esistente:
1. Riformatta il frontmatter con audience/registro/lingua dall'ASK
2. Aggiusta il tono (es. rende il linguaggio più diretto per "senior" che già conoscono i concetti base)
3. Include/esclude sezioni se richiesto
4. Estrae `glossary.md` (presente nel MKD ma in formato unificato)
5. Genera `faq.md` da steel-manning (P4)

**Risparmio di lavoro**: B1 fa ~30% di quello che faceva pre-v5, perché il MKD ha già il contenuto canonico.

## Stats (simulati)

- Coverage atomi: 100% (eredita dal MKD)
- Lunghezza output: 1100 parole (1.53x sorgente)
- Glossario: 8 termini
- FAQ: 6 domande
- Schemi mermaid: 3
