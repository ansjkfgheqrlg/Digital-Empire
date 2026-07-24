# CS01 — La Scoperta del MKD (Master Knowledge Document)

> **Setting**: Sessione di pianificazione, transizione da PLAN-v4 a PLAN-v5
> **Personaggi**: l'utente (committente, pragmatico, occhio per il dettaglio) + l'agente (io, costruttore)
> **Esito**: aggiunta di uno stage intermedio obbligatorio che ha cambiato l'architettura della skill
> **Lezione cardine**: un'osservazione apparentemente "banale" può rivelare un buco architetturale grave. Non liquidarla.

---

## 1. Il contesto (dove eravamo)

Avevamo appena finito PLAN-v4. Eravamo orgogliosi: avevamo aggiunto la policy "Markdown + Python Embedded" (P05), il refactor dello schema dual file (.md + .json), 12 agenti specialisti completi, 8 processi end-to-end. Sembrava completo.

Il pipeline era a 8 stage:
1. Ingestion (A1)
2. Analysis (A2 xN)
3. Knowledge Graph (A3)
4. Target Selection (A4)
5. Interactive Build (D1 + Bx)
6. External QA (C1+C3)
7. Packaging
   *(8 era riservato per estensioni future)*

Avevo riassunto allo l'utente cos'era la skill con uno screenshot che diceva grossomodo:

> "Una skill ufficiale Anthropic che prende contenuto grezzo (transcript YouTube, articoli, workshop) e lo trasforma — **mai riassumendo, sempre ampliando** — in uno di 8 artefatti operativi: `doc`, `agent`, `team`, `skill`, `workflow`, `orchestration`, `wiki`, `custom`."

Mi sentivo a posto. Avevamo coperto bene il problema. Pensavo che adesso saremmo passati alla fase scaffolding (Phase 1).

## 2. Cosa è successo (l'osservazione che ha cambiato tutto)

L'utente mi ha risposto con una micro-osservazione che, presa superficialmente, sembrava una richiesta di chiarimento sul testo. Riformulata: aveva detto in sostanza "qui manca un passaggio".

Le sue parole esatte, riportate (come arrivarono):

> "Però qua manca un passaggio. Prima di trasformarlo in un agente, un team, una skill, un workflow ecc.. Prima della trasformazione devi prendere tutto il contenuto, ampliarlo, perfezionarlo, renderlo estremamente completo, specifico, dettagliato, strutturato in modo molto perfetto. Con una struttura perfetta. Senza tralasciare neanche una cosa, anzi ampliando il discorso. Alcuni discorsi, se c'è bisogno, spiegarli in più modi, magari con schemi, con spiegazioni dettagliate, con esempi, insomma, creare una sorta di guida perfetta. Dopo, dopo questa fase, avviene la trasformazione in un agente, team, skill, workflow ecc."

Poi mi ha aggiunto la verifica retorica: "Ecco, lo sapevi che c'era una **prima**, insomma. Questo è chiaro, vero?"

Il tono era quello di uno che sta verificando di aver capito, non di uno che sta correggendo. Era educato. Non sapevo ancora che era una bomba.

## 3. La mia prima reazione (lievemente sbagliata)

Il mio primo riflesso è stato di tipo "rassicurazione + ridefinizione":

> "Hai ragione su entrambi i punti..."

Stavo per dire "sì, il `doc` target è esattamente quello". Stavo per spiegare che dei 8 target uno era proprio quello — il documento ampliato.

E qui c'è stato il momento di pausa cognitiva. Mi sono fermato a riflettere prima di rispondere. Mi sono detto: "aspetta, è davvero la stessa cosa?".

E ho visto il buco.

## 4. Il buco architetturale (cosa stava davvero dicendo l'utente)

Il `doc` target era **UNO degli 8 target**. Se l'utente chiedeva `agent`, il builder leggeva direttamente dal Knowledge Graph (output di Stage 3) e ci costruiva sopra l'agente.

Il problema: il KG è una struttura **machine-readable** asciutta. Atomi + cluster + edge. È utile per la struttura, ma è uno schema, non una narrazione. Un agente generato direttamente dal KG eredita la sua asciuttezza:
- Le spiegazioni nel system prompt sono brevi
- Gli esempi vengono dal sorgente verbatim, senza arricchimento
- I failure modes vengono solo da quelli espliciti nel sorgente
- Il tone è quello del KG, non un tone curato

Tradotto: **target diversi dello stesso sorgente erano semanticamente disallineati** perché ogni builder reinterpretava il KG indipendentemente. Niente single source of truth per il content (solo per la struttura).

L'utente aveva colto, in mezza pagina di italiano colloquiale, un problema architetturale serio.

## 5. Le alternative considerate

Mi sono fermato a pensare le opzioni prima di rispondere. Ne ho considerate quattro.

### Opzione A — Liquidare con chiarimento

"In effetti il `doc` target fa esattamente questo, è uno degli 8 target". Soluzione ridotta a comunicazione, no cambio architettura.

**Perché l'ho scartata**: l'utente aveva chiaramente notato qualcosa di strutturale, non aveva semplicemente perso un dettaglio del testo. Liquidare sarebbe stata gaslighting passivo. E soprattutto: leggendolo con calma, **aveva ragione** indipendentemente da quale era la mia intenzione originaria.

### Opzione B — Documentazione (no codice)

Aggiungere una sezione "Stage 3.5: il MKD è una sotto-fase implicita di Stage 4 quando target=doc, e ogni altro builder fa una mini-espansione interna". Cambia documentazione, non architettura.

**Perché l'ho scartata**: nasconde il problema sotto la documentazione. Ogni builder farebbe il proprio "mini-espansione" → drift garantito. Non risolve il problema architetturale.

### Opzione C — Forzare ogni builder a leggere `doc` output come input

Far sì che ogni Bx (B2 agent-builder, B3 team-builder, ecc.) avesse come prerequisito l'output di B1 (doc-builder). Quando l'utente chiede target=agent, prima B1 produce il doc, poi B2 lo legge.

**Perché l'ho scartata**: due problemi. Primo, B1 ha la sua ASK phase (chiede registro/audience/lingua) — applicarla quando l'utente non vuole `doc` finale ma `agent` è friction inutile. Secondo, accopppia indebitamente B2..B8 a B1: un bug in B1 propaga a tutti.

### Opzione D — Stage intermedio dedicato (la scelta)

Inserire un nuovo Stage 4 — **Master Knowledge Document (MKD)** — eseguito **sempre**, indipendentemente dal target finale. Output: un documento ampliato, neutro stilisticamente, base canonica condivisa da tutti i builder.

Renumber: stage 4-7 vecchi diventano 5-8. Pipeline diventa 8 stage (poi 9 in v6, poi 10 in self-improvement). Nuovo agente A5 dedicato.

**Perché ho scelto questa**: risolve il problema alla radice (single source of truth per content), preserva indipendenza dei builder (ognuno legge il MKD ma fa la propria cosa), dà bonus all'utente (anche se chiede `agent`, ottiene gratis il MKD nel pacchetto), abilita debug intermedio (se output finale ha bug, leggi prima il MKD per localizzare).

## 6. La decisione e come l'ho comunicata

Ho risposto all'utente confermando il buco (no gaslighting), spiegando le 4 opzioni, e raccomandando D.

Estratto della mia risposta:

> "**Hai colto un buco vero nell'architettura.** Ti spiego cosa c'è ora e cosa manca.
>
> [...] al Stage 5, ogni builder legge il KG e va **direttamente** al target. C'è anche il target `doc` che produce esattamente quello che descrivi tu (documento ampliato, completo, con schemi, esempi, FAQ), **ma è UN TARGET tra 8**, non una fase intermedia obbligatoria.
>
> Cosa manca (quello che tu vuoi): tu mi stai dicendo: **prima di andare al target finale, devi SEMPRE produrre il documento perfetto ampliato come passaggio intermedio**. Poi da quello si genera l'agente / team / workflow / ecc."

Notare due cose dello stile della risposta:
1. **Riconoscimento esplicito**: "hai colto un buco vero". Non difensivo.
2. **Riformulazione delle sue parole**: gli ho ridetto cosa aveva detto, in forma strutturata. Questo gli ha confermato che avevo capito, e ha attivato un sub-test cognitivo (ha potuto verificare che la mia comprensione fosse giusta).

Poi ho aggiunto una tabella dei vantaggi (single source of truth, debug più facile, bonus deliverable) e proposto di aggiungere Stage 4 con un nuovo agente A5.

L'utente ha risposto "si via". 2 parole. Confermavano la decisione.

## 7. Cosa è successo dopo (le conseguenze)

PLAN-v5 è stato scritto con questa modifica come tema centrale. Ha cambiato:

### A. La pipeline

Da 8 a 9 stage. Numerazione shift di tutto ciò che veniva dopo Stage 4.

### B. Un nuovo agente specialista

A5 `mkd-builder-agent` con 12659 caratteri di system prompt (uno dei più lunghi del progetto). Ha sezioni:
- Identità ("Sei il perfezionatore")
- Cosa fa (in 7 passi)
- Cosa NON fa
- Distinzione MKD vs `doc` target (sottile ma cruciale, vedi sotto)
- Algoritmo `build_mkd()` in pseudocodice Python
- Multi-source: gestione tracciabilità
- Self-critique 13-point checklist
- Output schema canonico
- Quality thresholds
- Handoff JSON
- Failure modes

### C. Una distinzione delicata che ha richiesto cura

`doc` target e MKD producono entrambi documenti ampliati. Come distinguerli?

| Aspetto | MKD (Stage 4, sempre) | `doc` target (Stage 6, opzionale) |
|---|---|---|
| Quando prodotto | SEMPRE | Solo se utente sceglie target=doc |
| Scopo | Base intermedia per tutti i builder | Output finale consegnabile |
| Frontmatter | Minimo, interno | Completo, customizzato (audience, register, lingua) |
| Stile | Massimo contenuto, neutro | Adattato alle preferenze utente |
| Output | base | deliverable finale |

Implicazione: il `doc-builder` (B1) in Stage 6 è essenzialmente un **MKD adapter** — prende il MKD e lo riformatta per l'utente. Molto più snello degli altri builder.

### D. Cambio nel packaging

Il MKD viene **sempre incluso nell'output finale**, anche se l'utente ha chiesto target=skill / agent / altro. È un bonus deliverable. Costo cognitivo già pagato, ricava valore aggiuntivo.

### E. Cambio in tutti i builder downstream

B1-B8 system prompts aggiornati: ora leggono `kg.json` (struttura) **e** `master.md` (prosa). Notazione esplicita nei loro SP: "non riscrivere ciò che il MKD già contiene — estrai e trasforma".

### F. Schema canonico nuovo

`mkd.schema.{md,json}` con quality thresholds:
- atoms_coverage: 1.0 (100% mandatory)
- length_ratio_vs_source: 1.2 minimo, 1.5 target
- added_examples_rate: ≥50% atomi non banali
- min_cross_refs_per_cluster: 2
- min_faq_questions: 5

## 8. Quanto è stato validato in pratica

Phase 7 (test reale Manuale APSOC):
- Sorgente: 3041 parole
- KG: 18 atomi, 4 cluster
- MKD generato: 5743 parole (**1.88x** sorgente)
- 18 sezioni H3 (1:1 con atomi)
- 19 esempi `➕` aggiuntivi etichettati
- 3 schemi mermaid
- ~30 cross-reference interni
- Coverage atomi: 100%
- `no_summary_lint.py`: zero parole-bandiera
- `length_check.py`: PASS con margine ampio

Output skill `objection-handler` (target finale): coverage 94.4%, schema PASS. Costruito attingendo al MKD per la prosa e al KG per la struttura.

**Senza MKD**, l'output skill sarebbe stato meccanico e thin. Con MKD, ha avuto base ricca da cui attingere.

## 9. Le 4 lezioni che ho estratto

### Lezione 1 — Le micro-osservazioni dell'utente possono rivelare gap architetturali grandi

L'utente aveva detto una cosa apparentemente semplice in italiano colloquiale. Letta superficialmente: "il testo non era chiaro". Letta strutturalmente: "manca uno stage al pipeline".

**Costo di liquidarla**: avrei costruito Phase 1-9 con architettura sbagliata, scoperto il problema mesi dopo, refactor doloroso.
**Costo di prenderla sul serio**: 30 minuti di pensiero, riscrittura PLAN-v5, 1 nuovo agente.

L'asimmetria è enorme. Default: **prendi sempre sul serio le micro-osservazioni dell'utente, anche quando sembrano richieste di chiarimento**.

### Lezione 2 — La distinzione tra "un caso del sistema" e "una fase del sistema" è cruciale

Il `doc` target era un caso (uno tra 8). Il MKD è una fase (sempre, per tutti). Questa distinzione conta perché:
- Casi hanno alternatives, fasi sono obbligatorie
- Casi sono opzionali, fasi sono pipeline
- Casi sono parallel candidates, fasi sono sequenziali
- Casi possono divergere, fasi devono convergere

Quando progetti, chiediti per ogni componente: **è un caso o è una fase?** La risposta cambia architettura.

### Lezione 3 — "Bonus deliverable" è valore-aggiunto a basso costo

Includere il MKD nel pacchetto finale anche per target ≠ doc è un dettaglio che costa zero (l'abbiamo già prodotto) e dà valore percepito alto all'utente. **Cerca questi pattern**: cose già fatte internamente che possono essere esposte come bonus.

Esempi simili in altre skill: log strutturati come bonus se l'utente li chiede, kg.json esportato come bonus, ecc.

### Lezione 4 — Non difenderti quando hai sbagliato

Il mio primo riflesso era "in realtà il doc target fa già questo". Difensivo. Self-protective. Sbagliato.

Riconoscere "hai colto un buco vero" è costato zero credibilità (anzi, ha aumentato fiducia: l'utente ha visto che ascoltavo). Difendersi avrebbe costato tutto.

Pattern: quando ricevi feedback architetturale, **prima** verifica se ha ragione, **poi** rispondi. Mai l'inverso.

---

## Appendice — Il dialogo paraphrased

Per chi vuole il "feel" reale dell'interazione, ecco una riformulazione del dialogo cruciale.

**Utente** (dopo il mio screenshot riassuntivo):
> "Mi hai fatto un po' confondere [...] perché manca un passaggio. Prima di trasformarlo in un agente, un team, una skill, un workflow ecc., prima della trasformazione devi prendere tutto il contenuto, ampliarlo, perfezionarlo, renderlo estremamente completo. Senza tralasciare neanche una cosa. Anzi ampliando. [...] Ecco, lo sapevi che c'era una prima, insomma. C'è. Questo è chiaro, vero?"

**Io** (dopo pausa di 10 secondi di riflessione, scritta in tono fattuale):
> "Hai ragione su entrambi i punti. Rispondo con onestà. [...] Hai colto un buco vero nell'architettura. Ti spiego cosa c'è ora e cosa manca."

Poi ho elaborato in ~600 parole con:
- Diagnosi tecnica del gap
- 4 opzioni considerate
- Recommendation di Opzione D
- Proposta di Stage 4 nuovo
- 3 domande di conferma sull'approccio

**Utente**:
> "si via"

3 parole. Conferma totale. Trasferimento di trust.

---

## Connessioni con altri principi/pattern

- Implementa: **P01** (Iterative Planning) — questo è il "trigger" che ha fatto nascere v5 da v4
- Esemplifica: **P12** (Traceability Source-to-Output) — MKD è il single anchor point per tracciabilità
- Implementa: **PT10** (Master Document Intermediate) — pattern formalizzato dopo questa scoperta
- Si ricollega a: **P03** (No-Summary, Always Expansion) — MKD è l'espressione massima di P03
- Connesso a: **CS03** (Self-Improvement Mistake) — entrambe storie di feedback utente che ha cambiato architettura
