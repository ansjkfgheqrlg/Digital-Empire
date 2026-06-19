---
Type: PRINCIPI
Status: Active
Tags: #principi #content-factory #CF-R1 #brief #qualita
Created: 2026-06-19
Last updated: 2026-06-19
---

# Principi Operativi — CF-R1 Strategia & Brief

> **Reparto:** CF-R1 Strategia & Brief · **Ecosistema:** 03-CONTENT-FACTORY
> Questi principi governano ogni decisione del reparto. Non sono linee guida:
> sono invarianti. Una violazione è un'eccezione che richiede ADR esplicito.

---

## Principio 1: Nessun contenuto senza brief approvato

Nessun reparto di produzione (R3, R4, R5) riceve un ordine senza `brief.json` con
gate CF-R1-QA = PASS in `orders/<id>/state.json`. Non esistono eccezioni per urgenza,
per ordini semplici, o per brand "già conosciuti". La complessità apparente dell'ordine
non riduce il requisito: un brief semplice richiede pochi minuti; un brief saltato
richiede rework in produzione.

Il gate CF-R1-QA è il sigillo di questo principio: bloccante, non advisory.

---

## Principio 2: brand_kit + icp obbligatori — mai un default generico

Ogni brief è parametrizzato sul brand specifico dell'ordine. Non esiste un "brand
generico" o un "icp di default": ogni ordine porta il suo `brand_kit` e il suo `icp.json`,
validati da CF-R2. CF-R1-ANALYST carica quei file specifici; CF-R1-ANGLE produce
angle coerenti con quella voce; CF-R1-HOOK seleziona il hook_type per quell'icp.

Un brief senza brand_kit_ref o icp_ref è strutturalmente incompleto — il gate lo blocca.
Questo è il pattern 11 del Piano Maestro ("multi-tenant a ordine") applicato alla fase
di strategia: niente è hard-coded su un singolo brand.

---

## Principio 3: Angolo conforme al Mandato prima del brief

CF-R1-COORD verifica la conformità al Mandato Empire (Art.2 — "prove non promesse",
Art.3 — zero genericità) PRIMA che l'angle venga inserito nel brief. Un angle che
richiederebbe claim non verificabili (es. "guadagna X in Y giorni" senza prova reale)
viene bloccato a monte, non dopo la produzione.

CF-R1-ANGLE segnala esplicitamente ogni angle che contiene dati da verificare:
il campo `nota` nel JSON dell'angle indica se un dato richiede fonte o va sostituito
con [DM]. Il brief non esce senza questa verifica.

---

## Principio 4: La libreria formule è il terreno di partenza, non il soffitto

CF-R1-ANGLE usa la libreria formule come base di lavoro, non come lista chiusa di
possibilità. Se la libreria non copre una combinazione brand/formato/icp, CF-R1-ANGLE
può proporre una formula nuova — ma la documenta come "non in libreria" e segnala a
CF-R1-LEARN per integrazione dopo validazione (≥3 casi con first_pass_rate ≥0.80).

Il contrario è vietato: non si inventa un hook_type per soddisfare il gate. Un
hook_type non in libreria fa fallire il gate CF-R1-QA — è corretto che lo faccia.

---

## Principio 5: Trend datato è un trend scartato — senza eccezioni

La soglia delle 48h dalla data del trend alla ricezione è dura. Non esiste "era quasi
fresco", "l'argomento è ancora rilevante", o "il committente ha chiesto lo stesso".
Un trend datato >48h viene archiviato con motivo strutturato e il WF-TREND-BRIEF si
ferma. La rilevanza editoriale di un trend non è valutata da CF-R1-TREND: quella
è la decisione di 08-INTELLIGENCE nel momento in cui invia il brief.

Questo principio protegge l'ecosistema dal produrre contenuti trend su eventi già
superati — che danneggiano la credibilità del brand più di non aver pubblicato nulla.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R1`
- [[WF-BRIEF]] · `workflow/WF-BRIEF.md`
- [[WF-TREND-BRIEF]] · `workflow/WF-TREND-BRIEF.md`
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
