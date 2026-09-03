# ADR-021 — Pivot piano editoriale @Legamidiamore: sequenziale non parallelo, causa vera è la scrittura

- **Data:** 2026-09-03
- **Stato:** ATTIVO
- **Decisori:** Emperator, su ordine diretto di Max ("prendi le tue decisioni, dimmele, procedi")

## Contesto

Il piano `memory/piano_editoriale_70.json` (generato 26/8, 70 video su 30gg, 3 strategie A/B/C in
parallelo dal giorno 1) è a giorno 8 con **89,5% di ritardo**: 2 video prodotti su 19 pianificati,
entrambi Strategia A; B e C fermi a **zero** (vedi CP-20260903-016, `ANALISI-COMPLETA-20260903.md`).

Causa reale isolata oggi, non ipotizzata: `memory/coda_produzione.json` (la coda che alimenta il
bottone "Produci video" di Aureus) accetta solo video con uno script adattato già scritto A MANO
in `05-TEMPLATES-E-KIT/script-adattati/<videoId>.md` — per scelta di design (`apex7_orchestrator.
run_phase_3`, commento in codice: "un adattamento vero e' lavoro di scrittura, copiare il
transcript verbatim non e' ammesso"). Dal lancio del piano (27/8) è stato scritto **UN SOLO**
script nuovo (`CxdlEsEnZ9g`, oggi). Al ritmo reale (~1 script/settimana quando succede), 70 video
richiederebbero mesi, non 30 giorni — indipendentemente da quale mix di strategie si scelga.

**Il collo di bottiglia non è la qualità delle 3 strategie sulla carta** (l'audit interno le trova
motivate: A ha il pool più ampio e il baseline vph più alto, +344% sullo schema di titolo misurato
più forte della nicchia). **È che il piano promette un volume che la fase di scrittura non ha mai
dimostrato di reggere**, e lo fa dividendo l'unica risorsa scarsa (tempo di scrittura umano) su tre
fronti contemporaneamente fin dal primo giorno.

Trovato inoltre, nello stesso giro: uno script già scritto e mai usato, `chVKOBlEpDI.md`
(destinazione @Legamidiamore, 9,7 minuti stimati — sopra il gate reale `DURATA_MINIMA_S=480s`,
scritto il 23/8, prima ancora del piano attuale) — fermo in coda per nessun motivo tecnico.
E `memory/copy_intelligence_legamidiamore.json`, il file che `run_phase_3` legge per dare a chi
scrive lo script gli schemi "da usare/da evitare", **non esiste mai stato creato** — i dati
misurati esistono (`CALENDARIO-LEGAMIDIAMORE.md`), solo mai formalizzati nel file che la pipeline
legge davvero.

## Decisione

1. **Le 3 strategie non partono più in parallelo dal giorno 1. Si sequenziano: A prima, B e C in
   pausa dichiarata** (non cancellate — `niente si scarta`, §ADR permanente) finché Strategia A non
   dimostra una cadenza reale sostenuta di **almeno 3 video pubblicati/settimana per 3 settimane
   consecutive**. Solo a quel punto si riapre B, poi eventualmente C.
2. **Il volume dichiarato di 70/30gg è sospeso come target immediato.** Resta l'orizzonte a lungo
   termine del catalogo sorgente (100 candidati per A), ma il target operativo diventa: quanti
   video la scrittura reale riesce a produrre, misurato settimana per settimana — non un numero
   fissato a tavolino il 26/8 senza dati di throughput.
3. **`chVKOBlEpDI.md` va in coda produzione oggi stesso** — zero costo di scrittura, pronto.
4. **`memory/copy_intelligence_legamidiamore.json` viene creato oggi** dai dati già misurati in
   `CALENDARIO-LEGAMIDIAMORE.md`, così ogni brief `.DA-SCRIVERE.md` futuro per questo canale porta
   davvero gli schemi "USARE/EVITARE" invece di un file vuoto silenzioso.
5. **Strategia C non riparte senza un secondo controllo di tono**, non solo quello unico del 26/8 —
   tocca un tema sensibile (uomini "disillusi", "verità scomode") e vale comunque il 40% del
   volume totale nel piano originale.

## Alternative scartate

- **Tenere il piano com'è, sperando che la scrittura recuperi da sola** — scartata: sono già
  passati 8 giorni con lo stesso schema e il ritardo non si è ridotto, anzi si allarga (19→17
  mancanti).
- **Tagliare Strategia C a zero in modo permanente** — scartata: il piano stesso la giudica
  realistica per la nicchia (nessun sorgente reale supera vph=20.6 nemmeno nella strategia
  migliore), e il tono è stato verificato non-manipolativo una volta. Sospenderla è proporzionato,
  cancellarla sarebbe una decisione più grande di quella che i dati oggi giustificano.
- **Aumentare il volume di A subito (es. 28→40) per "compensare"** — scartata: aumentare il numero
  di righe pianificate non risolve nulla se la scrittura resta il collo di bottiglia. Prima si
  dimostra la cadenza, poi si alza il volume — non il contrario.

## Conseguenze

- `memory/piano_editoriale_70.json` riceve un blocco `_revisione_20260903` che documenta il pivot
  senza cancellare le 70 righe originali (restano l'orizzonte, non il target immediato).
- Ogni futura task di produzione per Legamidiamore, finché B/C restano in pausa, pesca solo da
  Strategia A.
- Il prossimo checkpoint di verifica cadenza va programmato a **3 settimane da oggi (24/9/2026)**:
  se Strategia A ha tenuto ≥3 video/settimana, si riapre B; altrimenti si rivede di nuovo il piano,
  non si insiste sullo stesso schema.

## Contradiction-check

Verificato contro ADR attivi: nessun conflitto. Coerente con la direttiva permanente "niente si
scarta, si rende operativo" (B/C sospese non cancellate) e con ADR-005 (i blocchi minori vanno in
BACKLOG senza fermare la costruzione — qui il blocco non è minore, da qui l'ADR invece di una riga
di backlog).
