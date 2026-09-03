# Audit del Piano Editoriale 70 Video — @Legamidiamore

> Report di una Sentinella di Emperator, lavoro a freddo, solo lettura. Fonti citate riga per riga.
> Data di riferimento: 2026-09-03 (giorno 8 del piano, iniziato 2026-08-27).

---

## 1. Le 3 strategie spiegate bene

Fonte primaria: `memory/piano_editoriale_70.json` (chiave `strategie`, righe 10-38) e
`01-FLUSSI-E-PIANI/CALENDARIO-70-LEGAMIDIAMORE.md` (righe 7-12).

| | **A — Segnali & Decodifica** | **B — Tecnica & Comando** | **C — Allarme & Verità Sociale** |
|---|---|---|---|
| Canale sorgente | @PsicologiaFemminile-f8c | @PsicologiadellAttrazionee | @DinamicheSocialiAcademy |
| Target | Uomini che vogliono capire i segnali (verbali/corporei) che una donna manda senza dirli apertamente | Uomini che vogliono applicare attivamente una tecnica per aumentare la propria attrattività | Uomini disillusi dal dating moderno, in cerca di una spiegazione "perché non funziona più" |
| Formato | Lista numerata, 45-90s, voce femminile calma, ritmo alto (1 segnale/8-10s) | How-to imperativo, 45-90s, voce femminile diretta, tono coach | Narrativa "verità scomoda", 45-90s, tono serio/rivelatorio |
| Volume | 28/70 (40%) | 14/70 (20%) | 28/70 (40%) |
| KPI (vph baseline mediana pool alla generazione) | **5.1 vph** | **0.46 vph** | **0.16 vph** |
| vph riga 1 → riga ultima nel calendario | 10.62 → 0.73 | 2.33 → 0.17 | 2.28 → 0.06 |

**Qual è la scommessa più solida, sulla carta: Strategia A.**
Tre motivi verificabili, non impressioni:
1. Pool sorgente più ampio (100 candidati reali dichiarati in `frequenza`, piano_editoriale_70.json riga 16), quindi più margine di scelta e minore necessità di scendere in fondo alla lista per vph.
2. Baseline vph nettamente più alta (mediana 5.1, contro 0.46 di B e 0.16 di C — un ordine di grandezza sopra le altre due).
3. Il target di A ("segnali che una donna manda senza dirli") coincide esattamente con lo schema di titolo con il delta di velocity misurato più alto nella nicchia: `segnali_espliciti +344.4%` (`CALENDARIO-LEGAMIDIAMORE.md`, riga 11) e `genere_esplicito +311.7%` — A è l'unica strategia costruita sul framing dominante misurato, non su un'ipotesi.
Prova indiretta: dei 2 soli video finora davvero prodotti sul piano (vedi §2), entrambi appartengono ad A.

**Qual è la scommessa più rischiosa: Strategia C.**
Non è un giudizio di pancia, è nei numeri dello stesso piano:
1. KPI baseline 32 volte più basso di A (0.16 vs 5.1 vph) — è la strategia con il rendimento sorgente peggiore in assoluto, eppure riceve lo **stesso volume di A** (28/70, 40% delle risorse produttive) nonostante renda una frazione minima.
2. Il crollo di vph lungo il calendario è quasi lineare e già visibile nel piano stesso: da 2.28 vph (giorno 1) a 0.06 vph (giorno 30) — un fattore ~38x. Le righe sono ordinate per vph decrescente: significa che il pool C si sta esaurendo rapidamente e la seconda metà del mese pesca da candidati quasi fermi (0.06-0.09 vph). Lo stesso fenomeno tocca anche A (10.62→0.73, fattore ~15x) e B (2.33→0.17, fattore ~14x), ma parte da una base molto più alta.
3. Il tono di C è stato oggetto di un dubbio esplicito e recente: nel calendario precedente (05/08) DinamicheSocialiAcademy era escluso "per prudenza" perché temuto troppo simile a "dark psychology manipolativa" (`CALENDARIO-LEGAMIDIAMORE.md`, riga 44). Il 26/08 il timore è stato dichiarato smentito da uno scrape fresco e "confermato con Max" (`piano_editoriale_70.json`, riga 34) — ma è una verifica fatta una volta sola, non un controllo continuo, su una strategia che vale il 40% del volume totale.

**Strategia B non è né la più solida né la più rischiosa: è un test deliberatamente contenuto.** Il piano lo dice esplicitamente — usa solo il 61% del pool disponibile (23 candidati validi) "per lasciare margine" (`piano_editoriale_70.json`, riga 25). È la strategia con meno esposizione, in entrambe le direzioni.

---

## 2. Gap piano-vs-realtà (giorni 1-8)

### Video pianificati, giorno per giorno (fonte: `memory/piano_editoriale_70.json`, chiave `righe`)

| Giorno | Data pubblicazione prevista | Strategie previste | Video pianificati |
|---|---|---|---|
| 1 | 2026-08-27 | A, B, C | 3 |
| 2 | 2026-08-28 | A, C | 2 |
| 3 | 2026-08-29 | A, B, C | 3 |
| 4 | 2026-08-30 | A, B, C | 3 |
| 5 | 2026-08-31 | A, C | 2 |
| 6 | 2026-09-01 | A, B | 2 |
| 7 | 2026-09-02 | A, C | 2 |
| 8 | 2026-09-03 | A, C | 2 |
| **Totale** | | | **19 video pianificati** |

Per strategia sui giorni 1-8: **A = 8** (ogni giorno), **B = 4** (giorni 1,3,4,6 — nota: il giorno 6 il piano NON prevede C, un buco nel calendario stesso), **C = 7** (giorni 1,2,3,4,5,7,8).

### Video davvero prodotti (fonte: `memory/video_prodotti.json`, 5 voci totali)

| source_video_id | Titolo | Prodotto il | Corrisponde al piano? |
|---|---|---|---|
| mkaNzHTBw1M | "Dopo i 70 anni, camminare non basta più..." | 2026-08-03 | **No** — fuori tema/nicchia (anziani/salute), non è nella lista dei 70. Con ogni probabilità residuo della pipeline "fantasma" su canale Dose Mentale, ritirata (vedi nota in `YOUTUBE-PERFORMANCE-DASHBOARD.md`, riga 22: "`run_youtube_apex7.py` ... pipeline fantasma su un canale 'Dose Mentale' fisso ... ritirata in TASK-YT-005"). |
| eax7OPi1q0M | "Familiari tossici: i 3 segnali che Dio ti sta già allontanando da loro" | 2026-08-04 | **No** — stesso motivo, fuori nicchia/piano. |
| q8p6uwsMn2U | "5 SEGNALI che una Donna Vuole che TU Faccia la Prima Mossa" | 2026-08-17 | **No** — coerente con la nicchia Legamidiamore ma non è una riga delle 70 (verificato via grep sul JSON del piano: nessuna corrispondenza). Prodotto prima ancora della generazione del piano 70 (26/08) e prima anche del calendario a 10 giorni precedente — è un pilota fuori-piano, non un'esecuzione di riga. |
| **8_RZCbkuIQk** | "7 Tocchi Che Fanno Innamorare Una Donna Di Te" | **2026-08-29** | **Sì — Giorno 1, Strategia A.** Pubblicazione prevista 2026-08-27: prodotto con **2 giorni di ritardo**. |
| **CxdlEsEnZ9g** | "7 SEGNALI che una DONNA si sta innamorando" | **2026-09-03** | **Sì — Giorno 2, Strategia A.** Pubblicazione prevista 2026-08-28: prodotto con **6 giorni di ritardo**. |

### Il numero secco

Su **19 video pianificati per i giorni 1-8, solo 2 risultano davvero prodotti** — entrambi Strategia A, nessuno confermato pubblicato (vedi sotto). Percentuale di esecuzione: **10,5%**. Ritardo: **89,5%** (17 video su 19 mancano all'appello, otto giorni dopo la data di lancio dichiarata).

**Il ritardo non è distribuito uniformemente fra le strategie — colpisce B e C al 100%:**
- Strategia A: 8 pianificati, 2 prodotti → **75% di ritardo**, ma è l'unica strategia con esecuzione reale.
- Strategia B: 4 pianificati, **0 prodotti → 100% di ritardo**.
- Strategia C: 7 pianificati, **0 prodotti → 100% di ritardo**.

Anche i 2 video prodotti non risultano confermati come pubblicati sul canale: la dashboard più recente (`06-DASHBOARD-E-METRICHE/YOUTUBE-PERFORMANCE-DASHBOARD.md`, aggiornata 2026-09-03 12:17, run sul video CxdlEsEnZ9g) mostra F5 "Pubblicazione" completata come **preparazione metadati** (SEO score 100) ma stato fabbrica **"🟡 PARZIALE (fermata alla fase 5, --phase limitato)"** e **F6 Audit "Non eseguita ⚪ N/D — Manifest published_videos.json (video reale pubblicato)"** (righe 9, 19). In altre parole: nemmeno per il video più recente c'è conferma che sia realmente andato online, solo che i metadati sono pronti.

**Caveat sui dati**: `video_prodotti.json` è dichiaratamente incompleto/non aggiornato (indicato nel brief) e questo audit lo conferma — contiene 3 voci su 5 estranee al piano dei 70 video (probabilmente residui di una pipeline ritirata su un altro canale). Il numero reale di video prodotti potrebbe essere leggermente diverso se esiste un log più aggiornato altrove non incluso nei file indicati; ma anche nella lettura più generosa possibile (contando anche q8p6uwsMn2U come "vicino" al piano) il quadro non cambia in modo sostanziale: la produzione reale è a una frazione minima rispetto alle 19 righe attese per il giorno 8.

---

## 3. Decisioni strutturali documentate (con fonte)

| Decisione | Motivazione dichiarata | Fonte |
|---|---|---|
| Escluso @codicedonna come fonte | "solo 3 video in cache, campione troppo piccolo per un riferimento affidabile" | `CALENDARIO-LEGAMIDIAMORE.md`, riga 42 |
| DinamicheSocialiAcademy inizialmente escluso (calendario 10gg del 05/08) | Temuto "contenuto più dark psychology/manipolativo, da valutare con Max se è il tono giusto ... non escluso per principio, escluso per prudenza in questo primo giro" | `CALENDARIO-LEGAMIDIAMORE.md`, righe 43-45 |
| DinamicheSocialiAcademy poi incluso e promosso a Strategia C (piano 70, 26/08) | "Tono verificato il 2026-08-26 (fresh scrape): critica sociale sulla crisi relazionale maschile, NON dark psychology manipolativa come temuto ... confermato con Max prima di assegnare volume" | `piano_editoriale_70.json`, riga 34 |
| Volume Strategia B basso deliberatamente (14/70, non 28) | "il canale reale ha solo 23 candidati validi oggi, si usa il 61% del pool per lasciare margine" | `piano_editoriale_70.json`, riga 25 |
| @ciraolone e @linguaggiosegretodelcorpo-6589 esclusi come fonte (nello scraping fresco del 26/08, erano in cache dal 05/08) | Risultati "fuori nicchia oggi (rispettivamente canale AI/tech e scuola di ballo)" | `CALENDARIO-70-LEGAMIDIAMORE.md`, riga 4 |
| MIN_VPH=20.0 di `cashcow_check.py` non usato come soglia assoluta per nessuna delle 3 strategie | "non e' raggiunto da nessun video reale in questa nicchia oggi (top reale ~10.6 vph)... si usa un ranking relativo per canale" | `CALENDARIO-70-LEGAMIDIAMORE.md`, riga 5, ripreso nei KPI di ogni strategia in `piano_editoriale_70.json` |
| `run_youtube_apex7.py` (pipeline fantasma su canale "Dose Mentale" fisso) ritirata | Era "mai collegata alle fasi reali F1-F6" ed era l'unica altra scrittrice della dashboard | `YOUTUBE-PERFORMANCE-DASHBOARD.md`, riga 22 (TASK-YT-005) |

Nessuna voce specifica su "legamidiamore" / "piano_editoriale" / strategia A-B-C è stata trovata in `memory/decision_log.json` (verificato con ricerca full-text sul file, 1789 righe) — le uniche voci `DEC-nicchia-001` presenti riguardano la selezione del canale @ciraolone per un progetto completamente diverso (Manuale Claude Code / Low-Code Business Architect), non Legamidiamore. Le decisioni strutturali sul piano 70 vivono solo nei due file calendario e nel piano stesso, non nel decision log strutturato — è una lacuna di tracciabilità, non necessariamente un problema di merito.

`memory/copy_intelligence_legamidiamore.json` **non esiste** (verificato via glob sulla cartella `memory/`) — non c'è un file di copy intelligence dedicato a questo canale separato dai due calendari.

---

## 4. Segnali di rischio nel piano stesso

**I KPI dichiarati sono bassissimi in termini assoluti, ed è un fatto della nicchia, non pigrizia del piano.** Il piano lo dice esplicitamente: nemmeno il video reale più performante trovato nello scraping del 26/08 raggiunge la soglia MIN_VPH=20 usata altrove nella fabbrica per il gate cash-cow (top reale ~10.6 vph, cioè circa metà della soglia standard). Usare una soglia relativa al posto di quella assoluta è una scelta onesta e documentata, non un tentativo di abbassare l'asticella senza dirlo.

Detto questo, tre rischi restano scoperti e vale la pena nominarli con i numeri reali:

1. **Strategia C: 0.16 vph mediano è già ai limiti della rilevabilità statistica.** Un video sorgente da 0.16-0.06 viste/ora impiega settimane a raggiungere anche solo poche centinaia di visualizzazioni. Il piano investe il 40% del volume (28 video) su un pool con questo rendimento medio, scommettendo sul fatto che l'angolo "verità sociale" converta meglio del vph grezzo del sorgente lascia intendere — ma è un'ipotesi non testata nel piano stesso, solo dichiarata.

2. **Il pool si esaurisce dentro il mese stesso.** Ordinando le righe per vph decrescente (come fa il piano), la seconda metà di ogni strategia pesca sorgenti già vicini allo zero: C arriva a 0.06 vph entro il giorno 22, A scende sotto 1 vph già dal giorno 25. Questo significa che il piano, così come costruito, garantisce un decadimento di qualità della fonte via via che il mese avanza — un rischio strutturale indipendente dall'esecuzione, che nessuno dei tre KPI dichiarati (le mediane "alla generazione") comunica a chi legge solo la riga sintetica delle 3 strategie.

3. **La verifica "non è dark psychology" su Strategia C è un controllo puntuale, non ricorrente**, su una strategia che tiene lo stesso peso della più solida (A) pur con un rendimento sorgente 32 volte più basso. Dato che C tocca un tema sensibile (uomini "disillusi", "verità scomode" sul dating), varrebbe la pena che il controllo tono non fosse un episodio isolato del 26/08 ma un check ricorrente lungo l'esecuzione dei 28 video.

**Conclusione onesta**: il piano è realistico sui numeri della nicchia (non finge una domanda che non c'è), ma l'esecuzione è ferma quasi ovunque tranne che su un sottoinsieme minimo di Strategia A, e le strategie B e C — che insieme sono il 60% del volume promesso — non hanno ancora prodotto un solo video otto giorni dopo il lancio dichiarato.
