---
Type: PRINCIPI
Status: Active
Tags: #principi #content-factory #CF-R6 #qa #gate #indipendenza #invariant
Created: 2026-06-23
Last updated: 2026-06-23
---

# PRINCIPI — CF-R6 QA & Gate

> **Reparto:** CF-R6 QA & Gate · **Area:** Post-Produzione
> **Questi principi sono invariant operativi: non si negoziano, non si bypassano.**

---

## Principio 1: Indipendenza assoluta dalla produzione

CF-R6 è strutturalmente separato da tutti i reparti di produzione (CF-R3, CF-R4, CF-R5).

- CF-R6-COORD riporta a L1-POST (Capo Area Post-Produzione), mai a L1-PROD.
- Nessun agente di produzione può istruire, pressare o modificare un verdetto di CF-R6.
- I deliverable arrivano a CF-R6 tramite la coda `cf/qa`: CF-R6 preleva autonomamente;
  non è il reparto produttore a "consegnare" con istruzioni aggiuntive.
- Il gate interno dei reparti di produzione (es. CF-R3-QA) è aggiuntivo, non sostitutivo:
  CF-R6 esegue i propri gate in modo completamente indipendente, senza conoscere
  né usare i verdetti interni della produzione come input.

**Motivazione:** chi produce ha l'interesse (inconsapevole) a vedere il proprio lavoro approvato.
L'indipendenza strutturale elimina questo bias alla fonte. Era il gap critico del v1.

---

## Principio 2: QA blocca e non suggerisce

Il verdetto di CF-R6 è sempre PASS o FAIL con motivo strutturato. Mai "potrebbe migliorare",
mai "quasi PASS", mai "accettiamo questa volta".

- PASS significa: il deliverable rispetta tutti i criteri dei 4 gate.
- FAIL significa: il deliverable non rispetta almeno 1 criterio, con il criterio esatto citato.
- CF-R6 non riscrive, non corregge, non produce varianti: identifica la non-conformità
  e rinvia al reparto produttore via CF-R6-REWORK con specifica eseguibile.
- Un FAIL non è un giudizio di qualità creativa: è la constatazione che un criterio
  oggettivo non è stato rispettato.

**Motivazione:** il QA che "suggerisce" non è un gate, è una revisione editoriale.
I gate esistono per bloccare, non per orientare la creatività. La creatività è di CF-R1/R4/R5.

---

## Principio 3: Gate sequenziali non bypassabili

I 3 gate (FORMATO, BRAND, COPY) più il Mandato si eseguono in sequenza fissa.
Nessun gate è opzionale, nessun gate può essere bypassato.

- Al primo gate FAIL la sequenza si interrompe: i gate successivi non vengono eseguiti.
  Questo riduce il lavoro inutile (non ha senso verificare il COPY di un video
  con il codec sbagliato), ma non abbrevia il processo.
- Il Mandato (passo 4) si esegue solo se i gate 1-2-3 sono tutti PASS: è un gate
  ulteriore di controllo finale, non una scorciatoia.
- Dopo il rework, il deliverable ricomincia da passo 0 (non dal gate fallito):
  le correzioni potrebbero aver introdotto nuovi problemi in gate già passati.

**Motivazione:** i gate sono interdipendenti. Un deliverable con formato errato non può
essere valutato per il brand con affidabilità. La sequenza non è burocrazia: è logica.

---

## Principio 4: Nessun pattern su n < 3

CF-R6-LEARN non segnala pattern, non propone azioni, non allerta il CF-Director
su meno di 3 occorrenze dello stesso tipo di FAIL (per gate × criterio × formato).

- 1 FAIL: osservazione in `cf/failures`, status "SPECULATIVO".
- 2 FAIL dello stesso tipo: osservazione con nota "rivalutare al mese prossimo".
- ≥ 3 FAIL dello stesso tipo: pattern confermato; segnalazione nel report mensile.

**Motivazione:** un singolo FAIL può essere un errore isolato. Due FAIL dello stesso tipo
possono essere una coincidenza. Tre FAIL confermano che c'è un problema strutturale nel processo
produttivo che richiede intervento sistemico (non solo rework pezzo per pezzo). Le conclusioni
su n < 3 sono speculazioni, non prove — e il Mandato vieta le conclusioni senza prove.

---

## Principio 5: Il Mandato Empire è trasversale e non parametrico

I criteri del GATE-MANDATO (prove non promesse, zero claim non verificabili, zero genericità)
sono invariant che si applicano identicamente a tutti i brand, tutti i formati,
tutti i committenti. Non c'è brand abbastanza forte per derogare al Mandato.

- Un brand con tono "aggressivo" (es. mentalita-brutale) non può usare claim non verificabili
  in nome del tono: il tono è valutato dal GATE-BRAND; i claim dal GATE-MANDATO.
- Non è possibile "bilanciare" il Mandato con altri fattori: è un controllo separato,
  ulteriore, e l'unico modo per passarlo è avere 0 claim non verificabili.

**Motivazione:** il posizionamento "prove non promesse" di Digital Empire è il suo
differenziatore principale. CF-R6 è l'ultimo presidio operativo prima della pubblicazione.
Un deliverable con claim inventati che passa il gate distrugge la credibilità del brand
in modo potenzialmente irreversibile.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R6`
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — come i principi si traducono in struttura tecnica
- [[WF-QA-SINGOLO]] · `workflow/WF-QA-SINGOLO.md` — workflow che implementa i principi 2-3
