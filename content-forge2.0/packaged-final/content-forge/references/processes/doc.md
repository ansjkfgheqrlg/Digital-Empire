# Process: `doc` — Expanded Markdown Document

> Builder: `doc-builder-agent` (B1)
> Stage: 5
> Tempo medio stimato: 1 turno utente + 1-2 iterazioni

---

## 1. Identità

Il target `doc` produce **un documento markdown unico**, ampliato e riscritto integralmente dal sorgente, organizzato in capitoli, sezioni, esempi, schemi, glossario e FAQ. È il target più "leggero" come complessità ma il più ricco come densità informativa.

Non è un riassunto. Non è un re-formatting. È una **riscrittura ampliata** in cui ogni atomo del KG diventa almeno un paragrafo, e ogni cluster di atomi diventa un capitolo strutturato con esempi propri e schemi propri.

## 2. Forma canonica dell'output

```
output/
├── document.md                # il documento principale
├── glossary.md                # termini chiave + definizione
├── faq.md                     # generata da steel-manning (P4)
├── changelog.md               # cosa è cambiato tra iterazioni
└── README.md                  # come è stato costruito + indice
```

`document.md` ha questa struttura canonica:

```markdown
---
title: <titolo>
source: <path al sorgente>
generated_by: content-forge
generated_at: <ISO timestamp>
forge_target: doc
forge_version: <semver>
audience: <chi è il lettore>
register: <formale|tecnico|divulgativo>
language: it|en|...
---

# <Titolo>

> Documento generato da `content-forge` a partire da `<sorgente>`.
> Etichetta: tutto ciò che non è nel sorgente è marcato con ➕.

## Indice

- [Premessa](#premessa)
- [Capitolo 1 — ...](#cap-1)
- ...
- [Glossario](glossary.md)
- [FAQ](faq.md)

## Premessa
<contesto + chi parla + cosa imparerai>

## Capitolo 1 — <nome cluster>

### 1.1 <atomo 1>
<spiegazione canonica ampliata>

**Esempio (sorgente):** ...
**➕ Esempio aggiuntivo:** ...
**Schema:**
```
<ascii o mermaid>
```

### 1.2 <atomo 2>
...

## Capitolo 2 — ...

...

## Cross-reference
- [[atomo-1]] → [[atomo-5]] (perché)
- ...

## Glossario rapido
(vedi glossary.md per la versione completa)
```

## 3. Input atteso (dal Conductor)

```
inputs/
├── kg.json                    # knowledge graph completo
├── atoms/                     # atomi individuali (file json o md)
├── source_meta.json           # info sul sorgente (lunghezza, tipo, lingua)
└── user_answers.json          # risposte ASK
```

## 4. PLAN (cosa fa il builder appena spawnato)

1. Legge `kg.json` e identifica i **cluster** (gruppi di atomi semanticamente vicini). Ogni cluster diventerà un capitolo.
2. All'interno di ogni cluster, ordina gli atomi per dipendenza (P3) → sequenza dei sotto-capitoli.
3. Stima la lunghezza attesa: somma per ogni atomo (paragrafo canonico ~150 parole + esempio ~80 + schema opzionale ~50).
4. Definisce il TOC (Table of Contents) provvisorio.
5. Identifica i candidati a glossario (termini definiti nel sorgente o nuovi introdotti).
6. Identifica i candidati a FAQ (obiezioni/dubbi impliciti dal sorgente).
7. Restituisce al Conductor il PLAN per mostrarlo all'utente prima della ASK phase.

## 5. ASK (domande all'utente, generate da D1 sul KG specifico)

Esempio di domande adattive (D1 le adatta in base al KG):

1. **Audience**: "Il KG mostra che il sorgente assume conoscenza di concetti X, Y, Z. L'audience del documento finale conosce questi concetti o no?"
2. **Registro**: "Formale, tecnico, divulgativo o conversazionale?"
3. **Lingua**: "Italiano, inglese, o mantieni la lingua del sorgente (<lang>)?"
4. **Lunghezza minima**: "Il sorgente è <N> parole. Il documento finale è atteso ≥ <N>. Vuoi un floor più alto?"
5. **Schemi**: "Includere diagrammi mermaid, schemi ASCII, tabelle, o tutti?"
6. **Glossario**: "Glossario sì/no? E se sì, in coda al documento o file separato?"
7. **FAQ**: "Generata da steel-manning sì/no?"
8. **Convenzioni di citazione**: "Devo citare il sorgente per ogni paragrafo o solo nei punti chiave?"

## 6. BUILD (ordine di scrittura)

1. **Scaffold**: scrive frontmatter + TOC vuoto.
2. **Premessa**: scrive il contesto basato sul KG (chi parla, di cosa, perché vale la pena leggere).
3. **Per ogni capitolo (cluster)**:
   a. Intro del cluster (1 paragrafo che dice cosa imparerai)
   b. Per ogni atomo del cluster:
      - Spiegazione canonica (P1) ampliata
      - Esempio dal sorgente (P2)
      - Esempio aggiuntivo generato (P2 + etichetta ➕)
      - Schema se applicabile (P7)
      - Obiezione/controesempio se applicabile (P4)
   c. Outro del cluster (transizione verso il prossimo)
4. **Cross-reference** (P8): scansiona il documento e aggiunge link interni dove un atomo richiama un altro.
5. **Glossario**: estrae termini dai paragrafi marcati come definizione.
6. **FAQ**: prende le obiezioni generate (P4) e le formula come domande con risposte.
7. **README**: scrive il README di handoff (indice, come è stato costruito, modello di Forge usato, ecc.).

## 7. Self-critique (interna al builder, era C2)

Il builder, dopo BUILD, attiva un sub-step di critica indipendente — cambiando lente: legge il proprio output come se non l'avesse scritto, cercando:

- **Riassunto strisciante**: ci sono frasi tipo "in sintesi", "riassumendo", "in breve", "i tre punti chiave sono"? → rimuovere/riscrivere.
- **Esempi mancanti**: c'è qualche atomo senza un esempio concreto?
- **Schemi mancanti**: c'è qualche cluster procedurale senza un diagramma?
- **Salti logici**: ci sono affermazioni che il sorgente non supporta e che non sono etichettate come ➕?
- **Lunghezza per atomo**: ci sono atomi trattati in meno di 100 parole quando il sorgente li tratta più estesamente?
- **Coerenza terminologica**: termini definiti diversamente in capitoli diversi?

Output del self-critique: `self-critique.md` con lista di rilievi azionabili. Se ≥1 rilievo bloccante → loop BUILD su quel rilievo. Se solo warning → annotati per la critique esterna.

## 8. Critique esterna (C1 + C3)

- **C1 `coverage-verifier-agent`**: confronta `kg.json` vs `document.md` con `coverage_check.py` (match lessicale + embedding). Tutti gli atomi devono comparire. Soglia 95%.
- **C3 `target-schema-validator-agent`**: verifica conformità a `references/schemas/doc.schema.md`: frontmatter presente con campi obbligatori, TOC sincronizzato con i capitoli, file canonici presenti.

## 9. Iterate

Se la critique esterna ritorna fail, il Conductor passa il `qa-report.md` al builder, che:
1. Identifica i fix richiesti
2. Decide se rifare l'intero documento o patchare in-place
3. Patch in-place se ≤5 rilievi, rifa from scratch se >5 o se la struttura è sbagliata
4. Rilancia self-critique + critique esterna

Loop max 3 volte. Se al 3° fail si chiede all'utente.

## 10. Failure modes noti

| Failure | Sintomo | Mitigazione |
|---|---|---|
| Atomi non coperti | C1 segnala <95% | Capitolo dedicato agli atomi orfani |
| Output più corto del sorgente | length_check.py fail | Espandere capitoli più sintetici con esempi/schemi |
| Esempi tutti dal sorgente | Nessun ➕ | Forzare generazione di 1 esempio aggiuntivo per atomo |
| Linguaggio "asciutto" | self-critique segnala compressione | Riscrivere paragrafi con stile più discorsivo |
| TOC desincronizzato | C3 fail | Rigenerare TOC dopo BUILD |

## 11. Esempio realistico (mini)

Input: trascript YouTube di 8000 parole su "prompt engineering avanzato".
KG: 47 atomi, 8 cluster (es. "few-shot", "CoT", "self-consistency", "RAG-prompting", ...).
ASK answers: audience tecnica, registro tecnico, italiano, lunghezza ≥ 8000 parole, mermaid+ascii sì, glossario sì, FAQ sì.

Output:
- `document.md`: ~12000 parole, 8 capitoli, 47 sezioni, 47 esempi dal sorgente + 47 ➕, 18 schemi mermaid, 4 schemi ascii
- `glossary.md`: 23 termini
- `faq.md`: 12 domande generate da steel-manning
- `README.md`: indice + razionale

Coverage check: 100% atomi coperti. Length check: 1.5x sorgente. Schema validator: OK.

## 12. Handoff al Conductor

Builder restituisce al Conductor:
- path della cartella `output/`
- `build-report.json` con statistiche (atomi coperti, lunghezza, n. esempi, n. schemi, tempo, token)
- `next-suggestions.md` con eventuali suggerimenti (es. "questo documento sarebbe ottimo anche come `wiki` — vuoi che lo trasformi anche in quella forma?")

---

## 13. 📎 Appendice — Lint anti-summary (embedded)

### Parole-bandiera e pattern di compressione (regex)

```python
# Usato da no_summary_lint.py — il builder deve EVITARE questi pattern nel doc
import re

FORBIDDEN_PHRASES_IT = [
    r"\bin\s+sintesi\b",
    r"\briassumendo\b",
    r"\bin\s+breve\b",
    r"\bin\s+conclusione\b",
    r"\btl;dr\b",
    r"\bper\s+farla\s+breve\b",
    r"\bdunque\s*,\s+i\s+tre\b",
    r"\bi\s+(?:tre|quattro|cinque)\s+punti\s+chiave\b",
]
FORBIDDEN_PHRASES_EN = [
    r"\bin\s+summary\b",
    r"\bto\s+summarize\b",
    r"\bin\s+short\b",
    r"\btl;dr\b",
    r"\bthe\s+(?:three|four|five)\s+key\s+points\b",
]
PATTERNS = [re.compile(p, re.I) for p in FORBIDDEN_PHRASES_IT + FORBIDDEN_PHRASES_EN]

def find_summary_smells(text: str) -> list[tuple[int, str]]:
    """Ritorna lista (offset, match) di smell anti-summary trovati."""
    return [(m.start(), m.group(0)) for p in PATTERNS for m in p.finditer(text)]
```

### Cluster → capitolo (pseudo)

```python
def cluster_to_chapter(cluster: dict) -> dict:
    """Trasforma un cluster del KG in una sezione di capitolo del doc."""
    return {
        "title": cluster["label"],
        "intro_one_liner": cluster.get("summary_one_liner", ""),  # ironico ma utile internamente
        "sections": [
            {
                "atom_id": atom["id"],
                "atom_title": atom["title"],
                "canonical_explanation": "",   # da scrivere
                "source_example": atom.get("source_example", ""),
                "forge_example": "",           # generato, etichettato ➕
                "schema": "",                  # se applicabile
                "objection": ""                # da P4 se applicabile
            }
            for atom in cluster["atoms"]
        ],
        "outro": ""
    }
```
