# Enrichment Report — 5swDtQFyIws

**Video:** "If You Don't Understand Sales Systems, You Don't Understand Business" — Will Barron
(salesman.com), 24m06, EN
**Run:** `empire-studio/runs/max17-v10-barron-sales`
**Stage C-H eseguiti:** 2026-09-03 (la run Empire Studio 1-5 era già chiusa il 2026-09-02: questo
è l'unico degli 8 video analizzati del batch rimasto senza archiviazione in Memory Empire e senza
pagina wiki — il ciclo si chiude qui)
**Atoms disponibili:** 55 KA — framework 17, regola 15, numero 9, errore 8, fase 6; confidenza:
54 osservato, 1 inferito

---

## Stage D — Relevance / Gap / Scout

### Artefatti candidati valutati (letti prima di decidere, non solo grep)

| Artefatto | Righe lette | Esito |
|---|---|---|
| `.claude/skills/cro-call/SKILL.md` | 5.146 (struttura completa + 4 sezioni lette per intero: routing scenari, checklist pre-call, documento strategico 8 pagine, tracking & scoring) | **PATCHATO** |
| `.claude/skills/icp-radar/SKILL.md` | 77 (integrale) | **PATCHATO** |
| `.claude/skills/discovery-call-brief/SKILL.md` | 63 (integrale) | **PATCHATO** |
| `.claude/skills/proposal-gate/SKILL.md` | 76 (integrale) | **NON toccato** — vedi sotto |
| `.claude/agents/` (elenco completo) + ricerca su "conversione per fase", "pipeline" | elenco + grep mirato | **NON toccato** — nessun agente pertinente esistente, il gap diventa proposta |

### Verifica del gap (fatta di persona in questa sessione)

- **`cro-call`** — la sezione `█ SEZIONE: DOCUMENTO STRATEGICO 8 PAGINE` (riga 2033) contiene alla
  Pagina 2 la riga *"Basata su quello che ha detto in call, usando LE SUE PAROLE"*: il principio
  c'è, ma **non c'è nessuna prescrizione di aprire con una citazione diretta fra virgolette**, né
  la spiegazione del perché (bias di coerenza cognitiva), né il caso d'uso che lo rende decisivo
  (il documento letto da un socio/capo/coniuge che non era in call). Verificato leggendo la
  sezione, non solo cercandola.
- **`icp-radar`** — la scheda YAML ha `must_have`, `nice_to_have`, `esclusioni`,
  `scoring_matrix`, `angolo_outreach`, `obiezioni_tipiche_di_nicchia`. **Nessun campo trigger**: il
  profilo dice CHI è il cliente ma non QUANDO diventa comprabile. Il campo più vicino,
  `problema_evidente` dentro `must_have`, è un segnale statico ("problema visibile sul sito"), non
  un evento datato.
- **`discovery-call-brief`** — il campo `prossimo_passo_concordato` esiste ma è **stringa libera**,
  e il "Gate check pre-output" controlla `ambiente_server`, `budget_signal` e il dolore
  quantificato: **nessun controllo su data e ora del prossimo step**, che nel video è la
  condizione stessa perché la call sia considerata completata. Nessun campo trigger.
- **`cro-call` checklist pre-call** (righe 209-272) — 10 punti, **tutti lato nostro**: sito,
  landing, social, ads, provenienza, informazioni note, domande, case study, obiezioni probabili,
  setup tecnico. **Nessuna azione verso il prospect fra la prenotazione e la call.** Questo
  conferma il buco della Fase 3 (Indoctrinate) del video: non è coperto da nessuna skill esistente.
- **Agenti** — nessun agente di Digital Empire misura la conversione per fase del funnel di vendita
  interno. Ricerca su `.claude/` per "tasso di conversione per fase", "pipeline...conversione":
  **zero risultati**. La sezione "Tracking & Scoring post-call" di `cro-call` esiste ma è
  per-singola-call e per-venditore (scheda post-call, scoring a 6 criteri, analisi pipeline con
  benchmark CR 25-35%), non un cruscotto continuo di sistema.

**Verdetto**: gap reale su tre fronti patchabili in modo additivo (citazione verbatim nel
documento strategico, trigger nell'ICP, data/ora del prossimo step nel brief) + due gap che
richiedono costruzione nuova e quindi restano proposte (indottrinamento pre-call, misura per fase).

### Perché `proposal-gate` NON è stato toccato

`proposal-gate` è un gate a 9 criteri già molto stretto (problem-first, awareness, pricing a
catalogo, prove verificabili, scope 7gg, proprietà codice, supporto 90gg, brand voice, timing
48h). Il video suggerirebbe di aggiungere un criterio "il documento apre con le parole del
prospect", ma **il criterio 1 lo copre già**: *"Il problema è descritto con le parole/dati del
cliente (non marketing generico)"*. Aggiungere un criterio quasi-duplicato avrebbe reso il gate più
lungo senza renderlo più stretto: la stessa conoscenza è stata invece messa dove mancava davvero,
cioè nel documento che il gate controlla (`cro-call`, Pagina 2). Nessuna patch decorativa.

---

## Stage E — Gate (permission-guard)

Le tre patch sono **additive**: `git diff --numstat` → **+29 / 0** su `icp-radar`, **+11 / -1** su
`discovery-call-brief`, **+24 / 0** su `cro-call`. L'unica "cancellazione" è la riga
`"prossimo_passo_concordato": "string"` del brief JSON, riscritta identica con la virgola finale
necessaria per aggiungere i tre campi successivi — nessun contenuto rimosso.

- **Attribuzione in linea obbligatoria**: ogni blocco aggiunto porta
  `(fonte: 5swDtQFyIws - Will Barron, mm:ss)`.
- **Nessuna contraddizione con le regole esistenti**: la patch a `cro-call` rafforza la Regola
  Assoluta #6 già presente (*"Il prezzo va sempre presentato DOPO il valore"*) e specializza una
  riga che già diceva "usando LE SUE PAROLE"; la patch a `discovery-call-brief` non blocca la
  scrittura del brief (segnala, non ferma), coerente col fatto che il gate bloccante di reparto è
  `proposal-gate`, non questa skill.
- **Line endings preservati e verificati prima/dopo**: `icp-radar` e `discovery-call-brief` erano
  LF-only e sono rimasti LF-only; `cro-call/SKILL.md` era interamente CRLF (5.146 righe) ed è
  rimasto interamente CRLF (5.170 righe). Nessuna conversione introdotta.
- **Frontmatter YAML non toccato** in nessuno dei tre file.

**Riserva registrata**: l'uplift "10-20% di conversione aggiungendo il business case" è un numero
dichiarato a voce dall'autore, senza campione, periodo o metodologia. Non è stato scritto dentro
nessuna skill come benchmark: resta solo nell'archivio e nella pagina wiki, marcato come claim
dell'autore. Le patch applicate contengono solo regole operative falsificabili (apri con una
citazione, compila il trigger, fissa data e ora), mai promesse di risultato.

---

## Stage F — Patch applicate (3 file, 5 blocchi, +64 righe, 0 cancellazioni di contenuto)

### 1. `.claude/skills/cro-call/SKILL.md` — +24 righe, 0 cancellazioni

Sezione `█ SEZIONE: DOCUMENTO STRATEGICO 8 PAGINE` → `## 4. PAGINA 2 — LA TUA SITUAZIONE` →
sottosezione "Riformula della Situazione Attuale".

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| "usando LE SUE PAROLE" come principio, senza formato né obbligo | Blocco **OBBLIGATORIO**: la pagina 2 apre con 2-4 righe fra virgolette trascritte dalla call, con template `"[frase]" — [Nome], call del [data]` | KA-014, KA-040 |
| Nessuna spiegazione del perché funziona | **Bias di coerenza cognitiva**: un documento che riparte dalle tue parole invita a discutere la tua analisi, uno che riparte dalle sue lo mette nella posizione di confermare se stesso | KA-040 |
| Nessuna considerazione del lettore che non era in call | Il caso socio/capo/coniuge: chi non era in call non ha vissuto la parte emotiva e legge solo numeri — la citazione diretta è l'unico pezzo che riporta l'emozione in una stanza dove tu non ci sei | KA-019, KA-043 |
| Nessun errore dichiarato | Errore da evitare: tradurre le parole del prospect in "linguaggio da agenzia", con esempio concreto ("certi mesi non arriva niente" ≠ "flusso di lead non prevedibile con stagionalità non presidiata") | KA-040 |

### 2. `.claude/skills/icp-radar/SKILL.md` — +29 righe, 0 cancellazioni

Due blocchi: un campo nuovo nella scheda YAML + una sezione nuova prima di "## Connessioni".

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| La scheda ICP diceva CHI è il cliente, mai QUANDO diventa comprabile | Nuovo blocco YAML `trigger_evento` con `lista_trigger_osservati`, `segnale_ricercabile`, `dolore_specifico` — ricavati dai clienti già vinti, non indovinati | KA-015, KA-048 |
| Nessun criterio per capire se l'ICP scritto è buono | Nuova sezione **"Test del riconoscimento in 1 secondo"**: si scrivono le due versioni del messaggio (generica vs operativa) e si confrontano; se non si riesce a scrivere la seconda, mancano campi nella scheda — quasi sempre `trigger_evento` o `dolore_specifico` | KA-007, KA-022, KA-029 |

Nella sezione nuova è riportato per intero l'esempio operativo mostrato a schermo nel video
(segmento + fascia $20K-$200K/mese + risultato a 30 giorni + garanzia + meccanismo + dolore
riconoscibile), tradotto in italiano ma senza tagli.

### 3. `.claude/skills/discovery-call-brief/SKILL.md` — +11 / -1 (una riga riscritta identica con la virgola)

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| `prossimo_passo_concordato` come stringa libera ("ti mando la proposta") | Due campi nuovi: `prossimo_passo_data_ora` (`YYYY-MM-DD HH:MM \| null`) e `prossimo_passo_in_calendario` (booleano) | KA-033 |
| Il Gate check pre-output non controllava la data del prossimo step | Nuovo punto di gate: senza data e ora precise già in calendario **la discovery call non è chiusa** — non blocca il brief ma diventa il primo punto delle `domande_irrisolte`, perché il "ti faccio sapere" senza data è la causa più comune di trattative che muoiono dopo una call andata bene | KA-033 |
| Nessun campo per il "perché proprio ora" | Campo `trigger_evento` nel brief + punto di gate: senza trigger il preventivo non ha urgenza propria e T-proposal-writer dovrebbe costruirla dal nulla | KA-048 |

---

## I 5 CONSIGLI (regola permanente di Digital Empire)

### 1. Cosa migliorare in Digital Empire con questa conoscenza

**Il buco non è nella call, è intorno alla call.** `cro-call` (5.146 righe) è più profondo di
questo video *dentro* la conversazione — 12 domande, 5 tecniche di gestione risposta, 10 obiezioni
scriptate, documento a 8 pagine. Ma il processo di vendita di Digital Empire, guardato come
sistema, ha due tratti scoperti e uno non misurato:

- **fra "ha prenotato" e "è in call"**: zero azioni verso il prospect (verificato: la checklist
  pre-call di `cro-call` è tutta lato nostro);
- **fra "call finita bene" e "documento inviato"**: nessun requisito di data e ora del prossimo
  step (ora segnalato dalla patch al brief);
- **nessun tasso di conversione per fase**: non sappiamo dove il processo perde le persone.

La cosa da migliorare per prima è la più economica: **scrivere l'ICP dell'agenzia CRO con i campi
che ora `icp-radar` prevede** (fascia di fatturato del cliente target, trigger tipico, dolore nelle
sue parole) e usarlo come filtro di ingresso alle discovery call. Oggi `icp-radar` è usato per le
nicchie di outreach, ma non risulta un ICP scritto e vincolante per l'agenzia stessa.

### 2. Quale skill nuova creare

**`pre-call-indoctrination`** — genera la sequenza che oggi non esiste per il tratto fra
prenotazione e call: 1 email di conferma con link a una pagina, la pagina di conferma con video di
benvenuto + audit/questionario che il prospect compila prima (equivalente del "Selling Systems
Audit"), e un blocco FAQ costruito sulle 4 obiezioni classiche del ticket DE (prezzo → chi siete →
funziona per il mio caso → perché non lo faccio da solo). Verificato che non esista: ricerca su
`indottrin|indoctrinat|pre-call|precall` in `.claude/skills` e `.claude/agents` — gli unici match
sono `cro-call` (checklist di ricerca lato nostro) e `discovery-call-brief` (post-call). Input
naturale: la scheda ICP + il pricing a catalogo già fissato in `proposal-gate` (EUR 4.000 / 3.500 /
2.500 / 8.000), così la FAQ può dichiarare il prezzo prima della call come fa Barron.

### 3. Quale agente nuovo serve

**`sales-funnel-auditor`** — un agente che legge le schede post-call già previste da `cro-call`
(sezione Tracking & Scoring) e i brief prodotti da `discovery-call-brief`, e restituisce **il tasso
di conversione per fase**: lead→meeting prenotato, meeting→discovery completata (col nuovo criterio
data/ora), discovery→business case inviato, business case→chiuso. Verificato che non esista: nessun
agente in `.claude/agents/` copre la misura del funnel di vendita interno (gli `outreach-*` fanno
intelligence sul lead, `cro-empire` fa supervisione strategica, `cfo-empire` conta i costi non le
conversioni). È l'agente che trasforma il grafico "Sales Activity vs Revenue" del video da metafora
a cruscotto: senza numeri per fase, "il sistema perde gente" resta un'opinione.

### 4. Quale workflow nuovo costruire

**`post-call → business case + next step`**, un workflow a due uscite obbligatorie dalla stessa
esecuzione: (a) genera il documento strategico (già previsto da `cro-call` Scenario 4), (b) crea
l'evento in calendario per il prossimo step con la data raccolta nel brief e il promemoria. Oggi
sono due azioni manuali separate e la seconda si perde: il video le tratta come **una fase sola non
completabile a metà**. Il workflow chiude anche il ciclo con `proposal-gate` (che già impone
l'invio entro 48h dalla discovery call): oggi quel timer esiste come criterio ma nessuno lo fa
partire.

### 5. Quale skill o workflow ESISTENTE potenziare, e con quale pezzo preciso

**Fatto in questa sessione, non proposto**: `cro-call/SKILL.md`, sezione DOCUMENTO STRATEGICO 8
PAGINE, Pagina 2 "Riformula della Situazione Attuale" — aggiunto il blocco obbligatorio della
**citazione diretta fra virgolette** con il template, la spiegazione del bias di coerenza cognitiva,
il caso del lettore che non era in call, e l'errore da evitare (tradurre in linguaggio da agenzia).
È il pezzo preciso che mancava: la skill diceva "usa le sue parole" ma non diceva *come* né
*perché*, e senza il perché la riga veniva applicata come parafrasi gentile invece che come
citazione.

**Dichiarazione di ciò che NON serviva fare** (regola: il "niente da fare" si dichiara):

- **`proposal-gate`** non è stato toccato: il suo criterio 1 già impone il problema descritto con le
  parole del cliente. Aggiungere un criterio quasi identico avrebbe allungato il gate senza
  stringerlo.
- **`beast-preventivi`, `cro-copy-architect`, `cold-email`** non sono stati toccati: il contributo
  di Barron sull'outreach (Right Person / Right Timing / Right Message, ipotesi audace, un solo
  obiettivo per touchpoint) è già coperto — e con testi veri, che il video non fornisce — da APSOC,
  dal framework Barnum/Rainbow + 5 Pilastri e dalla Bibbia dei Messaggi. Qui l'Impero è già più
  avanti della fonte.
- **La postura in call** (dottore/paziente, domande prima delle soluzioni, ROI grezzo in call,
  budget dopo il valore, identificare il decision maker) è già in `cro-call`, spesso con più
  profondità: nessuna patch, sarebbe stata duplicazione.

---

## Stage H — Sintesi

**Artefatti valutati:** 5 (`cro-call`, `icp-radar`, `discovery-call-brief`, `proposal-gate`,
agenti). **Patchati:** 3. **Non toccati con motivazione scritta:** 2.
**Totale:** +64 righe, **0 cancellazioni di contenuto** (1 riga riscritta identica con virgola
JSON in `discovery-call-brief`).
**Line endings preservati:** LF dove era LF, CRLF dove era CRLF — verificato prima e dopo con
conteggio binario.

**Cosa era già coperto e non è stato duplicato:** postura del dottore, domande prima delle
soluzioni, ROI in call, budget dopo il valore, documento post-call, follow-up con valore, gate sul
preventivo, framework di outreach. Su tutti questi `cro-call` + `proposal-gate` + APSOC sono più
profondi del video.

**Tensione aperta:** una sola, dichiarata. Barron mette il **prezzo in FAQ prima della call**
($8.000 pubblicato); `cro-call` Regola Assoluta #6 dice *"il prezzo va sempre presentato DOPO il
valore, mai prima, mai da solo"*. Le due posizioni non sono conciliabili per decreto: nel modello di
Barron il prezzo pubblicato **è** un filtro di qualificazione che protegge il calendario, in quello
DE è un elemento di negoziazione da posizionare dopo la diagnosi. Non è stata applicata nessuna
patch su questo punto: la scelta è di Max, non di un video. Registrata come proposta di ADR nel
backlog.

---

## Backlog registrato (proposte, non costruite)

- **B-042** — Skill `pre-call-indoctrination` (email di conferma + pagina con video + audit
  pre-call + FAQ sulle 4 obiezioni classiche). Origine: 5swDtQFyIws, fase 3 del sistema.
- **B-043** — Agente `sales-funnel-auditor` (tassi di conversione per fase del funnel di vendita
  interno). Origine: 5swDtQFyIws, KA-003 + KA-024.
- **B-044** — Workflow `post-call → business case + next step in calendario` come singola azione
  non completabile a metà. Origine: 5swDtQFyIws, KA-033.
- **B-045** — Decisione da prendere (candidata ad ADR): pubblicare o no il prezzo prima della call.
  Tensione fra il modello Barron (prezzo in FAQ = filtro) e `cro-call` Regola Assoluta #6 (prezzo
  dopo il valore). Origine: 5swDtQFyIws, KA-010.

Queste quattro voci sono **proposte da approvare da Max**, non lavoro fatto. Non sono state scritte
in `company/Memory/BACKLOG.md` in questa sessione: il perimetro del brief era archivio + wiki +
consigli + patch sicure. Vanno riportate lì al primo passaggio su Memory.

---

## Tracciabilità

- Contenuto integrale: `memory-empire/knowledge/5swDtQFyIws/contenuto-integrale.md`
- Atoms: `memory-empire/knowledge/5swDtQFyIws/atoms.json` (55 KA, ognuno con `fonte` =
  `5swDtQFyIws#mm:ss` e `frame` = `frames/frame-NNN.png`)
- Manifest: `memory-empire/knowledge/5swDtQFyIws/ingest-manifest.json`
- Analisi visiva: `empire-studio/runs/max17-v10-barron-sales/video-analysis.md` — coverage 218/218
  frame unici, NO-FINTO PASS (con incidente dichiarato e sanato)
- Coverage report: `empire-studio/runs/max17-v10-barron-sales/coverage.md`
- Wiki: `second-brain-vault/wiki/sources/Source_Will_Barron_Sistema_Vendita_5_Fasi.md`
