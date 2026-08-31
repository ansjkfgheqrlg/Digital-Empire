# Ingestion Log — Backfill Memory Empire, video #1-5 andrei-pascu-001/cat1-copywriting

**Data:** 2026-08-27
**Operatore:** Memory Empire (backfill retroattivo, richiesto da Max)

---

## Cosa mancava

I primi 5 video ingeriti nel run `andrei-pascu-001/cat1-copywriting` (giugno-luglio 2026, i primissimi del
run, prima che il layer Memory Empire fosse operativo su questo progetto) avevano gia' un `video-analysis.md`
completo in `runs/andrei-pascu-001/cat1-copywriting/<id>/` — Stage 1-2-3-4-5 gia' eseguiti, frame letti
nativamente via visione Claude, VTT letto per intero, Knowledge Atom estratti con tracciabilita' P12 — ma
**non avevano mai ricevuto il trattamento Memory Empire**: nessuna cartella `memory-empire/knowledge/<id>/`
esisteva, quindi questi 5 video non erano mai stati archiviati integralmente ne' confrontati con le skill
Digital Empire esistenti (Stage D enrichment-research non era mai girato su di loro).

I 5 video interessati:
1. `9CuQI0Cr4Pg` — "Copywriter professionista scrive dal vivo" (video #1/29, 18m09s, analizzato 2026-06-30)
2. `qOK4WP82Bvo` — "COPYWRITING: cos'e', come funziona e come INIZIARE" (video #2/29, 17m09s, 2026-07-05)
3. `jgIgOPAnYNY` — "Come diventare un copywriter - tutorial COMPLETO" (video #3/29, 20m21s, 2026-07-09)
4. `t67-j2LiXgQ` — "Copywriting: come iniziare a lavorare come copywriter autonomo" (video #4/29, 13m17s, 2026-07-09)
5. `sTCwYnWmgcQ` — "Come diventare un copywriter con ZERO esperienza" (video #5/29, 12m29s, 2026-07-09)

---

## Cosa e' stato creato

Per ciascuno dei 5 video, cartella completa `memory-empire/knowledge/<video-id>/` con i 4 file standard
(formato allineato a cartelle di riferimento gia' esistenti nel run, es. `EBU57iVAutA/`, `hnPa2zspu3k/`):

- **ingest-manifest.json** — metadata, incluso un campo esplicito `backfill_date`/`backfill_reason` per
  tracciare che si tratta di un'archiviazione retroattiva (nessuna nuova visione dei frame, riuso del
  `video-analysis.md` gia' validato).
- **atoms.json** — 20-24 Knowledge Atom per video (110 atom totali sui 5 video), riformattati dal formato
  gia' presente in `video-analysis.md` allo schema standard Memory Empire (`{id, source, frame, category,
  section, tags, atom}`), tutti con fonte tracciabile (timestamp video + frame quando disponibile).
- **contenuto-integrale.md** — contenuto INTEGRALE, non riassunto. Per i video con overlay di schermo/testo
  scritto live (`9CuQI0Cr4Pg`, `jgIgOPAnYNY`), riorganizzato dai passaggi visivi e citazioni gia' documentati
  in `video-analysis.md`. Per i 3 video talking-head puri (`qOK4WP82Bvo`, `t67-j2LiXgQ`, `sTCwYnWmgcQ`), la
  trascrizione integrale e' stata ricostruita per deduplicazione dai file sottotitoli `.vtt` auto-generati
  (rolling captions YouTube), poi divisa per capitolo/sezione — nessun contenuto verbale accorciato o
  compattato, dichiarato esplicitamente in ogni file. Per `t67-j2LiXgQ` (che ha sia sottotitoli `.it.vtt` che
  `.en.vtt` auto-tradotti) e' stata usata la traccia italiana originale per fedelta' al parlato reale.
- **enrichment-report.md** — Stage D/E/F/G completo per ciascun video: confronto con le skill Digital Empire
  rilevanti (`copywriting`, `cro-copy-architect`, `ad-creative`, `ads`, `beast-preventivi`, `pricing`,
  `agency-scalping`), gate di qualita', nessuna modifica applicata alle skill esistenti — solo segnalazioni.

**Totale file creati:** 20 (4 file x 5 video) + questo log.

---

## Scoperte principali dell'enrichment

### 1. Scoperta maggiore — origine/convergenza del framework APSOC (video `jgIgOPAnYNY`)

Il video #3 introduce esplicitamente la formula proprietaria di Andrei Pascu **APSOC**: Attenzione -
Problema - Soluzione - Obiezioni - Call To Action. La skill Digital Empire `cro-copy-architect` ha come
framework centrale un file chiamato letteralmente **"framework-apsoc-operativo.md"**, con la stessa sequenza
di step (Attenzione - Problema - Promessa/Soluzione - **Social Proof** - Obiezioni - CTA), identica nell'ordine
e nel nome dell'acronimo, con l'aggiunta di una S di Social Proof che il framework base di Andrei non ha.
Il video #4 (`t67-j2LiXgQ`, versione ridotta a 3 step della stessa struttura, con Andrei che dice
esplicitamente "ci sarebbero altri due step che non spiego ora") conferma incrociata la stessa origine.

**Non e' stata applicata nessuna modifica** — e' una conferma retrospettiva sull'origine concettuale del
framework gia' esistente nella skill DE, non un gap da colmare. Segnalato per tracciabilita' e contesto futuro.

### 2. Conferma forte — value-based pricing per freelance (video `qOK4WP82Bvo` e `sTCwYnWmgcQ`)

Entrambi i video rigettano esplicitamente il pricing per-ora/per-parola a favore del prezzo fisso basato sul
valore generato, allineandosi fortemente a `beast-preventivi/references/stages/02-pricing.md` (gia' esistente,
value-based, 3-tier). Il video #5 aggiunge una motivazione operativa non ancora esplicita nella skill: il
pricing a percentuale sul profitto e' rischioso quando il freelance controlla solo una PARTE del funnel di
conversione (es. solo la descrizione prodotto, non il branding). Segnalato come possibile nota futura, non
applicato.

### 3. Pattern ricorrente — ricerca "voice of customer" via recensioni (video `9CuQI0Cr4Pg` e `jgIgOPAnYNY`)

Due video del backfill (oltre al gia' noto pattern generale) insegnano lo stesso metodo pratico: cercare
recensioni YouTube/Amazon del prodotto o categoria per estrarre pain point e linguaggio reale del target.
La skill generica `copywriting/SKILL.md` non ha una fase di ricerca esplicita dedicata (assume il contesto
gia' fornito). Seconda comparsa nel run — candidato per un futuro arricchimento se confermato una terza volta.

### 4. Aree segnalate per verifica futura, non completate in questa sessione

- Sovrapposizione di dominio tra il video #5 (acquisizione clienti: freelance marketplace -> outreach,
  reputazione online/LinkedIn/sito-landing) e la skill `agency-scalping` — non confrontata riga per riga per
  limiti di tempo in questa sessione, dichiarato esplicitamente nell'enrichment-report di `sTCwYnWmgcQ`.
- Possibile connessione tra "valore anticipato" (video #5) e il principio di reciprocita' gia' presumibilmente
  in `marketing-psychology` — non verificata.

---

## Regole rispettate

- **NO riassunti**: ogni `contenuto-integrale.md` contiene il contenuto vero (trascrizione ricostruita o
  passaggi visivi con citazioni dirette gia' documentati), non compattato.
- **NO invenzioni**: ogni atom ha fonte tracciabile (video-analysis.md esistente + timestamp + frame quando
  disponibile). Nessun frame descritto se non gia' letto e verificato in Stage 3 originale.
- **Nessuna skill modificata**: tutte le tensioni/scoperte sono state SOLO segnalate negli enrichment-report,
  mai applicate automaticamente — coerente con il precedente stabilito da `EBU57iVAutA` (che aveva trovato
  una tensione reale su breakdown-prezzi vs anti-pattern AP-05 e l'aveva solo segnalata).

---

## Stato dopo il backfill

I 5 video #1-5 del run `andrei-pascu-001/cat1-copywriting` sono ora completi su tutti i livelli richiesti dal
pipeline Memory Empire (Stage A-H). Il gap scoperto il 2026-08-26/27 e' chiuso. MASTER-RUN-TRACKER.md
aggiornato con una nota nello STATO GLOBALE (le spunte ✅ della tabella erano gia' corrette quanto a
video-analysis.md, ma non riflettevano l'assenza del layer Memory Empire — ora sono vere anche su quel fronte).
