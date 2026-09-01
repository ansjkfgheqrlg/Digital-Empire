# P03 — No-Summary, Always Expansion

> **Definizione canonica**: L'output rispetta o supera la lunghezza/ricchezza del sorgente. Mai compressione informativa. Per ogni atomo del sorgente, l'output contiene: spiegazione canonica, esempio sorgente, almeno un esempio aggiuntivo (`➕` etichettato), uno schema quando applicabile, connessioni con altri atomi. **Postura culturale, non solo regola.**

## Perché funziona

### 1. Il riassunto è perdita di informazione mascherata da utilità
Riassumere è il default cognitivo degli LLM perché:
- Training data premia "essere conciso"
- Token output costano (incentivo implicito)
- Pattern "guide tldr" sono ovunque nei dataset

Ma il riassunto **assume di sapere cosa è importante**. In contesti di knowledge work, raramente lo sai a priori. Quello che sembra dettaglio trascurabile oggi è la chiave domani.

Esempio: in un transcript di 1 ora su prompt engineering, una frase di passaggio "il modello non ha memoria tra conversazioni separate" può sembrare ovvia e tagliabile. Ma quando 6 mesi dopo qualcuno costruisce un agente che assume memoria persistente, quella frase era il vincolo critico mancato.

### 2. L'espansione produce comprensione, non solo materiale
Quando espandi un atomo con esempio + schema + controesempio, **scopri lacune nel tuo capire**. Il riassunto nasconde la non-comprensione; l'espansione la rivela.

Questo è un pattern noto in pedagogia: **Feynman technique** — se non sai spiegare un concetto a un principiante con esempi tuoi, non lo capisci.

### 3. L'output è materia prima per altre cose
Un documento di output da una skill verrà letto da altri agenti, altri umani, in altri contesti. **Non sai quale dettaglio servirà a chi**. L'espansione massimizza la probabilità che il materiale sia utile in usi futuri imprevisti.

## Come applicarlo (operativo)

### Le 5 regole concrete

**Regola 1 — Ratio lunghezza ≥ 1.0**
Output (parole) ≥ Sorgente (parole). Idealmente 1.2-1.5x. Enforced via `scripts/length_check.py`.

**Regola 2 — Coverage atomi 100%**
Ogni atomo del Knowledge Graph deve comparire nell'output. Verificabile via `scripts/coverage_check.py`. Soglia minima 90%, ma per MKD 100%.

**Regola 3 — Esempio per ogni atomo non banale**
Almeno 1 esempio per atomo. Se il sorgente non lo fornisce, **lo generi tu**, etichettato `➕`. Mai esempi non etichettati se inventati.

**Regola 4 — Schema dove applicabile**
Atomi con struttura (procedure, framework, comparison) hanno schema (mermaid / ASCII / tabella). Pattern P7 (Schema Generation).

**Regola 5 — Connessioni esplicite**
Cross-reference fitti tra atomi correlati (P8 Cross-Reference Weaving). Senza connessioni l'output è una lista, non una rete.

### Parole-bandiera VIETATE

Lint automatico (`scripts/no_summary_lint.py`) blocca:
- "In sintesi"
- "Riassumendo"
- "In breve"
- "In conclusione"
- "TL;DR"
- "Per farla breve"
- "I tre punti chiave"
- "In summary"
- "To summarize"
- "In short"

Uniche eccezioni: in conventions/anti-patterns.md (le citi come anti-pattern, non le usi).

### Etichettatura `➕`

Tutto ciò che generi tu (non dal sorgente) **deve** essere etichettato:

```markdown
**Esempio (sorgente):** quello che dice il sorgente verbatim

**➕ Esempio aggiuntivo:** generato da te, ancorato al dominio

**Schema:** [se generato, etichettare implicitamente — è ovvio]

**➕ Controesempio:** generato da te per chiarire i confini
```

Senza etichettatura, sembra che inventi attribuendo al sorgente = disonestà intellettuale.

## Esempi

### Esempio 1 — content-forge MKD

Sorgente reale: transcript di un workshop di 3041 parole su preventivi.
MKD output (Stage 4): 5743 parole = **1.88x** sorgente.

Atomi del KG: 18. MKD ha 18 sezioni H3 (1:1).
Esempi `➕` aggiunti: 19 (uno per atomo non banale).
Schemi mermaid generati: 3.
Cross-reference interni: ~30.

Risultato: l'utente che legge il MKD impara più dal MKD che dal sorgente originale, **perché il MKD esplicita ciò che il sorgente assumeva**.

### Esempio 2 — Errore reale evitato

In Phase 9, prima della tightening dello schema, B4 (skill-builder) ha prodotto una skill `beast-preventivi` con references `/stages/` che avevano:
- 50 righe ognuno
- 0 esempi propri
- 0 schemi
- 0 anti-pattern correlato

Il sorgente parlava in modo discorsivo di "discovery call". Il reference output diceva solo: "Discovery: domande call. Ancoraggio budget. 5 segnali non-fit." — 3 frasi.

**Violazione P03**: l'output era ~10x più corto del sorgente. Inutile per chi vuole davvero capire come fare discovery.

Fix Phase 9 (Stage 7 O3 reference-expander): forza arricchimento file <150 righe a 200-400 righe con esempi, schemi, anti-pattern.

### Esempio 3 — ➕ (non da content-forge)

**Pedagogia**: la stessa filosofia in *Designing Effective Instruction* (Morrison et al.). Materiale didattico "ridotto al minimo" è dimostrabilmente peggio per retention rispetto a materiale "elaborato" (Elaborative Encoding theory, psicologia cognitiva).

**Knowledge management**: Andy Matuschak's *Evergreen Notes* — note che si auto-contengono, hanno almeno un esempio, sono linkate ad altre note. Esattamente P03 applicato a note personali.

## Anti-pattern correlato

**AP04 — LLM-Speak Output**: include riassunti automatici, aperture stereotipate ("In this guide we'll explore..."), uso di "leverage" "comprehensive" "robust" inflazionato. LLM-speak è spesso correlato a violazione P03 perché entrambi vengono da default training.

**Anti-pattern duale**: **Padding / Verbose-without-substance** — espandere aggiungendo parole vuote ("è importante notare che", "vale la pena menzionare che"). NON è P03 corretto: P03 chiede espansione **di valore informativo**, non di parole. Misura: ratio info/parola, non solo ratio parole/parole.

## Decision tree: "questo atomo è abbastanza espanso?"

```
Per ogni atomo del KG nell'output:
│
├─ Ha definizione canonica? (1-3 frasi precise)
│  └─ NO → ESPANDI
│
├─ Ha spiegazione estesa? (paragrafo che articola)
│  └─ NO → ESPANDI
│
├─ Ha almeno 1 esempio?
│  ├─ NO → ESPANDI (cerca nel sorgente, se assente genera ➕)
│  └─ SÌ → continua
│
├─ Se è atomo strutturato (procedure/framework): ha schema?
│  └─ NO → AGGIUNGI schema (mermaid/ascii/tabella)
│
├─ Ha ≥1 connessione esplicita ad altro atomo correlato?
│  └─ NO → AGGIUNGI cross-reference
│
└─ Lo apri da fresh eyes 1 mese dopo: capisci tutto senza altro context?
   ├─ NO → ESPANDI ancora
   └─ SÌ → atomo OK
```

## Quando NON espandere

- **Frontmatter YAML**: nessuna espansione, dati strutturati.
- **Code blocks**: espandere il codice = bug. Espandi semmai i commenti.
- **Tabelle di dati**: stessa regola, non aggiungere righe finte.
- **Citazioni verbatim**: mai modificare, mai espandere. Sempre `>` blockquote.
- **Target `custom` con vincolo lunghezza esplicito dall'utente**: l'utente ha chiesto SP da 3000 char per n8n? Rispetti il vincolo, e in `coverage_map.md` dichiari quali atomi sono `out_of_scope` per limite.

## Riferimenti esterni

- **Anthropic skill-creator** — Non esplicito su no-summary, ma il pattern di "espandere via esempi e test cases" è coerente.
- **Andy Matuschak**, *Evergreen Notes Should Be Atomic and Densely Linked* — fondamento concettuale.
- **Richard Feynman**, *Feynman Technique* — "se non sai spiegarlo semplicemente non lo capisci". Tradotto in: se non sai espanderlo con esempi tuoi, non lo capisci.
- **Sönke Ahrens**, *How to Take Smart Notes* — Zettelkasten method. P03 è di fatto Zettelkasten applicato a skill output.
- **Morrison, Ross, Kalman, Kemp**, *Designing Effective Instruction* — Elaborative Encoding theory in instructional design.

## Connessioni con altri principi

- Si appoggia su: P12 (Traceability) — devi tracciare quali atomi sono coperti dove
- Combina con: P11 (Anti-Summary Cultural) — P03 è il principio, P11 è la postura
- Si applica via: PT10 (Master Document Intermediate) — il MKD è l'espansione canonica del sorgente
- Validato da: scripts/coverage_check.py, scripts/length_check.py, scripts/no_summary_lint.py
