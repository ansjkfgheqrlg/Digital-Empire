# P1 — CRITICA S2 (DENARO E VERITÀ) — DRAFT-V1-A-lanci.md + DRAFT-V1-B-capacita.md

**Autore:** Sentinella S2, angolo denaro e verità
**Data:** 2026-09-10
**Bersaglio:** `DRAFT-V1-A-lanci.md` (860 righe, 27 azioni AP-004/005/008/033 + AP-034..060) e `DRAFT-V1-B-capacita.md` (492 righe, 4 verdetti AP-006/012/018/019+020)
**Metodo:** verifica sul disco, mai a memoria. Nessun file di produzione toccato. Un solo file scritto: questo.

---

## 1. Classifica delle azioni

Quattro caselle: **EURO DIRETTO** (produce o registra un incasso), **ABILITA UN EURO** (contenuto/decisione che, se il resto esiste, influenza direttamente una vendita), **SOLO INFRASTRUTTURA** (schema/gate/script/parametro di governo), **SOLO DOCUMENTO** (testo che descrive, cataloga o dichiara, senza toccare un funnel vivo).

### Draft A — LANCI (27 azioni, headings verificati: 4 Famiglia A + 23 Famiglia B)

| Azione | Casella | Perché |
|---|---|---|
| AP-004 | ABILITA | Testo di ancoraggio + struttura a due lanci — cambia cosa vede un compratore, *se* il funnel esiste |
| AP-005 | ABILITA | Copy ads/countdown reale — ma "prima della firma [data_apertura] è aria", dice il rango 9 dello stesso draft |
| AP-008 | INFRASTRUTTURA | Campo schema `transizioni[]` + criterio gate |
| AP-033 | ABILITA | Incentivo reale (sconto futuro) — campo opzionale + testo |
| AP-034 (`catena.py`) | INFRASTRUTTURA | Script di controllo, zero righe di copy |
| AP-035 | INFRASTRUTTURA | Generatore di pagina |
| AP-036 | INFRASTRUTTURA | Pattern nuovo, dichiarato "non serve al primo lancio" |
| AP-037 | DOCUMENTO | Cartella vuota in attesa di popolamento |
| AP-038 | DOCUMENTO | Travaso di 22 formule già scritte altrove — zero contenuto nuovo |
| AP-039 | INFRASTRUTTURA | Griglia dichiarata nel registro |
| AP-040 | INFRASTRUTTURA | Campo schema `concretezza` |
| AP-041 | INFRASTRUTTURA | Soglia di gate parametrizzata (vedi §4 — è anche un numero inventato) |
| AP-042 | DOCUMENTO | Articolo di legge (§13) + ADR-029 |
| AP-043 | DOCUMENTO | Articolo di legge (§14) |
| AP-044 (controlli 9-13) | INFRASTRUTTURA | Cinque controlli automatici in più |
| AP-046b/047b/048b | INFRASTRUTTURA | Regole di gate (scomposizione bundle, fonte prova, config sconto) |
| AP-050 | INFRASTRUTTURA | Campo schema + regola di manutenzione |
| AP-051 | ABILITA | Blocco di copy reale (ancora prima del prezzo) |
| AP-052 | INFRASTRUTTURA | Criterio di gate anti-scarsità-finta |
| AP-053 | DOCUMENTO | Formula di copy dichiarata **esplicitamente inapplicabile al primo lancio** ("in configurazione tripwire non si usa") |
| AP-054 | ABILITA | Contenuto reale mancante (l'obiezione mai nominata), diretto contro il concorrente |
| AP-055 | DOCUMENTO | Riga di ricerca interna (prezzo concorrente in un JSON) |
| AP-056 | ABILITA | Recupero di un funnel **già scritto e già esistente** — l'unica azione vicina a un vero acceleratore di cassa |
| AP-057 | INFRASTRUTTURA | Criterio di gate sulla pagina di consegna |
| AP-058 | INFRASTRUTTURA | Parametro (tetto di parole) nel criterio di uscita di una fase |
| AP-059 | DOCUMENTO | File di vocabolario nuovo |
| AP-060 | INFRASTRUTTURA | Criterio di gate, **esplicitamente attivo solo sul secondo lancio (Mastery), non sul primo** |

**Totali Draft A (27):** EURO DIRETTO **0** · ABILITA UN EURO **6** (AP-004, 005, 033, 051, 054, 056) · SOLO INFRASTRUTTURA **14** · SOLO DOCUMENTO **7**

### Draft B — capacità (7 interventi eseguibili, tabella §9)

| Azione | Casella | Perché |
|---|---|---|
| Contratto d'ingresso `beast-preventivi` (AP-006A+AP-020a) | INFRASTRUTTURA | Gate d'ingresso su un processo che gira **≈0 volte/mese** (fatto verificato dal draft stesso: `handoffs/` un solo file, di giugno) |
| Chiusura tensione breakdown-prezzi (AP-006B) | DOCUMENTO | Codifica di una regola in un file di riferimento, nessun preventivo in coda a cui si applichi oggi |
| Validazione a monte `market-report-pdf` (AP-020b) | INFRASTRUTTURA | Gate di qualità su uno script già esistente |
| Ramificazione comportamentale `emails` (AP-012) | DOCUMENTO | File di riferimento nuovo, **nessuna campagna email attiva lo consuma oggi** |
| Correzione callout falso `revops` (AP-012) | DOCUMENTO | Correzione di un refuso interno |
| Budget di sforzo `content-forge` (AP-019) | DOCUMENTO | Regola dichiarata dal suo stesso autore come "senza un incidente misurato dietro" (§6.2) |
| BACKLOG + puntatori (AP-018 NO-GO + fix `skill-forge`) | DOCUMENTO | Una riga in un file e una correzione di refuso |

**Totali Draft B (7):** EURO DIRETTO **0** · ABILITA UN EURO **0** · SOLO INFRASTRUTTURA **2** · SOLO DOCUMENTO **5**

### Totale combinato (34 azioni eseguibili nei due draft)

| Casella | N | % |
|---|---|---|
| EURO DIRETTO | 0 | 0% |
| ABILITA UN EURO | 6 | 17,6% |
| SOLO INFRASTRUTTURA | 16 | 47,1% |
| SOLO DOCUMENTO | 12 | 35,3% |

**In faccia:** zero azioni su 34 producono o registrano un euro. La maggioranza assoluta (82,4%) è infrastruttura di governo o documento — esattamente la coppia di caselle che la missione dichiarata ("un piano eseguibile che FA INCASSARE, non altra documentazione") dice di voler evitare. Delle 6 azioni "abilita un euro", **tutte** dipendono da almeno uno tra: la firma di Max su prezzo/ruolo (non data), Brevo collegato (non fatto), una cassa vera (non provata) — tre cose che **entrambi i draft dichiarano fuori dal proprio perimetro** ("il piano non tocca S0", Draft A tabella §5.1; "NON tocca l'ecosistema LANCI", intestazione Draft B).

---

## 2. Il piano stesso è il pezzo 26 di ULTIMO METRO? **SÌ.**

Prova, non opinione.

1. **ADR-016** (`company/Memory/decisions/ADR-016-ultimo-metro.md`) fissa la legge: *«Un pezzo di lavoro non è "fatto" finché non è uscito. Finito e non pubblicato ha lo stesso valore economico di non fatto: zero. Con in più il costo di averlo prodotto.»* Misurato il 2026-09-03: 25 pezzi finiti mai usciti, 2.137 MB, il più vecchio fermo da 135 giorni.
2. Questi due draft sono **1.352 righe** di specifica — campi di schema, criteri di gate, articoli di legge, vocabolari — per un ecosistema (`LANCI`) che oggi **non ha ancora aperto un solo carrello**. Verificato ora sul disco: `.claude/skills/fabbrica-siti/scripts/` contiene solo `canone_sync.py` e `galleria.py` — **`catena.py` non esiste**, nonostante sia "l'azione a più alto rendimento del piano intero" secondo lo stesso Draft A (rango 1, §8).
3. `company/Memory/tesoreria/entrate.jsonl` e `spese.jsonl` — riverificati ora — sono **entrambi a zero righe**. Non un euro misurato, né in entrata né in uscita, in tutta l'azienda.
4. La tabella §7.1 di Draft A elenca essa stessa i tre gesti umani ancora aperti che bloccano un incasso vero: Brevo (`MT-FJF6`), cassa vera (`MT-32RU`), consegna+rimborso (`MT-CV7N`), più `PU-RUOLO` e `PU-PREZZO` (scadenza 12/09, non firmati). **Nessuna delle 34 azioni classificate al §1 tocca uno di questi cinque punti.**
5. Il documento è dichiarato **destinato a P1 → P2 → P3**, cioè **altri tre giri di critica scritta prima che una sola riga tocchi un funnel vivo** (Draft A frontespizio: "Stato: DRAFT V1 — destinato a tre giri di critica"). Questo documento stesso, che stai leggendo ora, è parte di quella catena.
6. Draft B lo dice quasi da solo, e poi lo mette fuori perimetro: §7 punto 4, *«`tesoreria/entrate.jsonl` e `spese.jsonl` sono entrambi a zero righe. […] È il caso più puro di ULTIMO METRO applicato a un organo interno.»* — seguito da: *«Fuori dal perimetro di questo piano.»* Il draft riconosce la malattia e scrive la diagnosi in un file che nessuno curerà, perché l'ha dichiarata fuori scope nello stesso respiro.

**Conclusione:** i due draft sono, per definizione di ADR-016, un candidato diretto a diventare il **pezzo 26 e 27**: lavoro "finito" (una volta approvati) che non produce un euro finché tre gesti umani fuori dal loro perimetro non vengono chiusi — e nel frattempo generano **ulteriore lavoro finito** (P2, P3) prima che uno qualunque dei due tocchi il problema che li ha generati.

---

## 3. Stime di effort smontate

### `catena.py` — dichiarato T3, 4-8h (AP-034, "i controlli 8, 3, 5 sono banali… i controlli 7 e 2 richiedono Playwright, che è già in casa")

Riverifica dei singoli controlli richiesti dalla stessa riga COSA di AP-034:

| Controllo | Difficoltà reale | Perché la stima "banale" non regge |
|---|---|---|
| 3 (og:image duplicato) | Facile | Confronto metadati, vero |
| 5 (anni scritti a mano) | Facile | Regex, vero |
| 8 + AP-032 (catena CTA→cassa, footer una sola volta) | Media | Serve un crawler con grafo pagine/CTA, non solo richieste HTTP singole |
| 7 (corpo prezzo ≥ corpo testo servizio) | **Alta** | Richiede estrazione di stili calcolati via Playwright, euristica per distinguere "testo prezzo" da "testo di servizio", soglie da tarare — è lo stesso controllo che il §10 punto 4 del Draft A ammette può produrre **falsi positivi** |
| 2 (accento oltre soglia) | **Alta** | Stessa famiglia di 7: conteggio colori distinti su tutto il DOM, definizione di cosa conta come "accento" — non è mai banale in pratica |
| 6 (prezzo/scadenza dentro immagine con alt vuoto) | **Alta, sottostimata** | Senza OCR non si può sapere se un'immagine "contiene" un prezzo — nel testo AP-034 non è nemmeno menzionato come problema, eppure è il controllo più difficile tecnicamente degli otto |
| 1 (bottone diretto a pagamento senza pre-cassa) | Media | Richiede una classificazione del ruolo del prodotto/pagina, non solo un check statico |
| 4 (campo editabile che non entra nel calcolo mostrato) | **Alta** | Il caso misurato nello studio (`apsales.eu/landing-page`) è un bug specifico di un calcolatore ROI. Automatizzarlo in generale richiede capire semanticamente cosa "entra nel calcolo" — non è scriptabile con un pattern generico in poche righe |

**La stima non include, e per sua stessa ammissione dovrebbe:** la taratura sulle 52 pagine già catturate **prima** di agganciare il gate — il Draft A lo dice esplicitamente al §10 punto 4 ("farlo girare sulle 52 pagine… se produce FAIL su pagine corrette, si taratura prima di attivarlo") ma **quella taratura non è nelle 4-8h dichiarate in AP-034**, è un lavoro scoperto e non contato.

**Poi arriva AP-044**, che aggiunge i controlli 9-13 con la dicitura *"T2 aggiuntivo su AP-034 (9, 12, 13 sono banali; 10 e 11 richiedono parsing)"* — cioè **1-3h in più** per cinque controlli nuovi, di cui almeno due (10 — verificare che una somma di scomposizione-bundle torni matematicamente; 13 — discrepanza di naming tipo "Armageddon"/"Armageggon", che è correzione ortografica euristica) sono più vicini a un piccolo motore di parsing/fuzzy-matching che a "banale".

**Ricalcolo onesto**, sommando AP-034 + AP-044 (13 controlli totali) e includendo la taratura che il draft stesso richiede prima del collegamento al gate:

- Scaffolding, parsing manifesto, arg `--manifesto/--solo/--json`: 1h
- Controlli banali (3, 5, 9, 12): 1-1,5h
- Controllo 8 + dedup footer (AP-032): 2-3h
- Controlli 7 e 2 (Playwright, stili calcolati, soglie): 4-6h
- Controllo 6 (euristica senza OCR, con tutti i limiti che comporta): 2-3h
- Controllo 1 (classificazione ruolo pagina): 1-2h
- Controllo 4 (verifica semantica calcolo): 2-4h, risultato comunque fragile
- Controlli 10, 11, 13: 3-4h
- **Taratura sulle 52 pagine + triage falsi positivi (richiesta esplicitamente dal draft stesso, §10.4, mai messa in un effort):** 2-4h

**Totale realistico: 18-30h**, contro le **5-11h dichiarate** (4-8h AP-034 + 1-3h AP-044). **Sottostima di un fattore 2,5-3×**, e la parte più grande del salto — la taratura anti-falsi-positivi — è un lavoro che il draft **stesso** identifica come necessario in un'altra sezione, senza mai farlo entrare nel numero di ore.

---

## 4. Numeri inventati

| Numero | Dove | Fonte dichiarata | Verifica | Verdetto |
|---|---|---|---|---|
| **27-47 €** fascia prezzo Manuale | AP-004 §3.3, riga "Fascia prezzo proposta" | Nessuna citata nella riga stessa | La tabella dei prodotti del concorrente (§1 del dossier) non contiene questa fascia; nessun documento letto la giustifica | **Inventato, e presentato senza il disclaimer che lo stesso AP-004 usa due righe sotto per il tasso di conversione ("numero di comodo dichiarato")** — incoerenza di trasparenza dentro la stessa azione |
| **100 €** valore `opzione_futura` (Manuale→Mastery) | AP-033 §3.12, riga PERCHÉ | *«nel caso concreto del Manuale l'opzione futura ha un candidato ovvio»* | Verificato `ANATOMIA-DEI-LANCI.md` righe 308-312: l'esempio reale di Andrei è **199 €** di sconto su Funnel Operator. Il draft non deriva 100 € da quel numero né da alcun calcolo (non è una percentuale dichiarata del prezzo Mastery 397 €, non è la metà del 199 € di Andrei con una motivazione) | **Inventato, definito "candidato ovvio" senza esserlo** |
| **150 € e 400 €** soglie di `GATE-CPY-1` (fonti esterne richieste) | AP-041 §"soglia_rapporto_minima" | `ANATOMIA-DEI-LANCI.md` Parte IV | Verificato riga per riga: la fonte contiene **esattamente tre punti misurati** — 98€→0 fonti, 400€→2 fonti, 999€→5 fonti — e una soglia diversa, **349 €**, per "la prova sociale vera compare solo sopra i 349 €". **150 € non compare in nessun punto della fonte.** E il draft usa **400 €** come soglia per richiedere "prova sociale con faccia e nome", mentre la fonte misura quella soglia a **349 €** | **150 € è inventato di sana pianta (curve-fitting su 3 punti); 400 € sostituisce silenziosamente il 349 € realmente misurato con un numero diverso, senza dichiararlo** |
| **"Massimo 3 rami per sequenza"** | Draft B, AP-012 §4.4 punto 5, attribuito a "KA-07 (che è la parte che quasi tutti saltano)" | outFunnel Lezione 15, KA-07 | Letto il file sorgente per intero (`.../lezione-15/lesson-analysis.md`, riga 29): KA-07 dice testualmente *«un principiante dovrebbe iniziare con tag e segmentazioni semplici; non personalizzare OGNI step, va trovato un equilibrio con tempo/budget disponibili»* — **nessun numero, in nessuna forma** | **Inventato: un limite numerico preciso ("3") attribuito a una fonte che contiene solo un avvertimento qualitativo, senza dichiararlo come stima propria** |

**Pattern comune alle quattro:** in tre casi su quattro (27-47€, 100€, "3 rami") il numero non ha **nessuna** fonte dichiarata — non è nemmeno marcato come stima, a differenza di quanto lo stesso Draft A fa correttamente altrove (es. AP-004, il tasso di conversione tripwire→mastery è esplicitamente marcato `"stato": "assunto"` con motivazione). Nel quarto caso (150/400€) la fonte esiste ma viene letta con più precisione di quella che contiene — tre punti diventano due soglie nette, e una soglia misurata (349€) viene silenziosamente sostituita da un'altra (400€).

---

## 5. IL BUCO — la lezione grossa che nessuno dei due draft converte in azione

**La lezione:** il vantaggio competitivo reale di Andrei Pascu non è un funnel più pulito — è che **non scrive mai pagine nuove per lanciare**. `SINTESI-METODO.md` §3 lo misura: *«Il lancio: si specchia il negozio, lo si spoglia, si punta tutto a una cassa»* e la conclusione esplicita: *«Costo del metodo, misurato: un lancio non richiede di scrivere pagine nuove. Richiede di copiare, spogliare e ripuntare. È la ragione per cui può lanciare spesso.»* Il metodo mirror-di-lancio è già classificato come "pattern" con precedente in ADR-024, ed è la **prima** delle "CINQUE COSE DA RUBARE SUBITO" del documento stesso: *«Il mirror di lancio — lanciare senza scrivere pagine nuove.»*

**Il buco:** Digital Empire ha, per ammissione di ADR-016, **25 pezzi finiti e mai usciti** — 5 libri pronti (tre con manoscritto, copertina, dati Amazon compilati: "non manca niente"), 16 video, altri 4 video di fine agosto. Il metodo che Andrei usa per lanciare *spesso ed economicamente* — prendere un asset già scritto, spogliarlo, puntarlo a una cassa sola — è **esattamente** lo strumento che serve a smaltire quel magazzino. Non un magazzino di teoria: un magazzino misurato, con nome (ULTIMO METRO), con un numero (2.137 MB), con un'età (135 giorni sul pezzo più vecchio).

**Nessuno dei due draft lo fa.** Draft A applica il mirror-di-lancio **a un solo asset** trovato per caso (AP-056, `chiamata-formazione.netlify.app`, scoperto per errore mentre si studiava il concorrente) e lo tratta come un evento isolato, non come un metodo da applicare sistematicamente al resto del magazzino ULTIMO METRO. Le altre 22 azioni della Famiglia B costruiscono invece l'apparato opposto: schemi, gate, griglie di punteggio, criteri obbligatori — cioè la disciplina che Andrei applica **solo dove converte** (`SINTESI-METODO.md` §5), non il metodo con cui lui produce **volume** di lanci a basso costo. Draft B, dal canto suo, nomina esplicitamente il problema ULTIMO METRO al §7 punto 4 e lo dichiara **fuori perimetro** nello stesso paragrafo.

**Il risultato:** 34 azioni tra i due draft ingegnerizzano in dettaglio microscopico UN lancio nuovo (il Manuale), mentre il metodo più economico e già misurato per trasformare in cassa i 25 pezzi **già finiti e già pagati in tempo-lavoro** non viene proposto da nessuna parte come azione sistematica. È il buco più costoso, perché è l'unico dei due studi che punta dritto al problema che l'azienda ha già nominato come il suo più grave (ADR-016) e nessuno lo raccoglie.

---

## 6. La sequenza che incassa prima — cinque azioni, in ordine, con motivo

Draft A mette `catena.py` (AP-034) al rango 1 per "rendimento" — euro/rischio per ora spesa — con la giustificazione che il controllo 8 "azzera ogni euro che il copy ha guadagnato". L'argomento presuppone che esistano già: un funnel pubblicato, traffico che lo visita, un copy che converte, e una cassa collegata. **Nessuna di queste quattro cose esiste oggi.** Un linter statico protegge un tubo in cui non scorre ancora acqua. Ordine proposto:

1. **Censire e verificare `chiamata-formazione.netlify.app` (contenuto in AP-056), OGGI, isolato dal resto del registro.** 18.770 px, 506 blocchi, già puntato su Mastery 397€, fermo su staging. Se è ancora raggiungibile e lo stampo di cassa di Andrei (AP-035, sei variabili) gli si applica in un pomeriggio, questo è l'asset più vicino a un incasso che l'azienda possiede **oggi**, non fra tre giri di critica. Motivo: è l'unico dei 34 item che non richiede costruire nulla di nuovo — solo verificare e collegare.
2. **Portare a Max, ATTIVAMENTE e nella stessa giornata, `PU-RUOLO` e `PU-PREZZO` — non aspettare la scadenza del 12/09.** Draft A stesso ammette (tabella §7.1) che senza questa firma `GATE-OFF-1` non può chiudere e S2 non può chiudersi. È un gesto umano, ma ADR-026 dice di portarlo attivamente, non di lasciarlo scritto ad aspettare. Motivo: è il singolo blocco più vicino alla cassa fra tutti quelli elencati nei due draft, e nessuna delle 34 azioni lo tocca.
3. **Chiudere i tre gesti S0 che i draft dichiarano esplicitamente "non toccati": Brevo (`MT-FJF6`), cassa vera (`MT-32RU`), consegna+rimborso (`MT-CV7N`).** Questi non sono infrastruttura per dopo: sono, letteralmente, l'unica differenza fra "un prodotto in vendita" e "un prodotto non in vendita". Motivo: senza questi tre, ogni euro di lavoro sulle altre 34 azioni è lavoro su un negozio senza cassa.
4. **Scrivere a mano UNA pagina di vendita minima per il Manuale, fuori dal registro/schema**, usando lo stampo di pre-cassa a sei variabili (già pattern esistente in `fabbrica-siti/pattern/pre-cassa/`, non serve costruire il generatore AP-035 per usarlo una volta) e il testo di ancoraggio di AP-004. Motivo: applica letteralmente il metodo di Andrei — non costruire l'apparato, copiare lo stampo e lanciare — e produce un funnel vendibile prima che esista `catena.py`.
5. **Solo a questo punto, `catena.py` (AP-034)** — come controllo sul funnel che ora esiste davvero, con traffico reale che ci passa sopra, non come prerequisito teorico di un funnel che non c'è. A quel punto il suo rendimento è reale: protegge euro che stanno effettivamente arrivando, non euro ipotetici.

**Perché l'ordine del Draft A è sbagliato nel merito, non solo nella forma:** ranking per "rendimento" ha senso solo se il denominatore (rischio evitato) è comparabile fra le opzioni. Il rischio che `catena.py` evita (un copy che converte ma con una cassa rotta) è un rischio **di secondo ordine**, attivabile solo dopo che il rischio di primo ordine — nessun prezzo deciso, nessuna cassa collegata, nessun canale confermato vivo (lo stesso Draft A ammette al §10 punto 3 che *"il canale previsto è spento dal 29/07/2026"*) — è stato risolto. Costruire il controllo di qualità prima della cosa da controllare è ingegneria alla rovescia.

---

## 7. LA MIA OBIEZIONE PIÙ FORTE

**Il piano ottimizza tutto tranne le tre cose che accenderebbero un incasso, e le dichiara fuori dal proprio perimetro nello stesso documento che promette di far incassare.**

La missione dichiarata è: *"trasformare lo studio Andrei Pascu in un piano eseguibile che FA INCASSARE Digital Empire, non in altra documentazione."* Il risultato misurato: 34 azioni, zero delle quali produce o registra un euro (§1), 82% delle quali sono infrastruttura di governo o documenti, e le uniche tre cose che davvero separano l'azienda da un primo incasso — la firma di Max su prezzo/ruolo, Brevo collegato, una cassa vera — sono esplicitamente escluse ("il piano non tocca S0", Draft A §5.1; "NON tocca l'ecosistema LANCI", intestazione Draft B). Nel frattempo il documento stesso è dichiarato **destinato a due giri di critica ulteriori (P2, P3)** prima che una riga tocchi un funnel vivo.

Questo non è un piano che fa incassare rimandato di poco: è, per la definizione data dall'azienda stessa in ADR-016, **lo stesso pattern che ha prodotto 25 pezzi finiti e mai pubblicati** — lavoro elaborato, ben scritto, meticolosamente referenziato, che si ferma esattamente prima del punto in cui incontrerebbe un cliente pagante. La differenza fra questi due draft e i 5 libri pronti in `libri_pronti/` è che i libri hanno almeno un prodotto finito dietro; qui il prodotto finito è **il piano di come, un giorno, si costruirà l'apparato che permetterà di decidere se vendere qualcosa che nessuno ha ancora deciso di vendere.**

Un'azienda a zero euro misurati (`entrate.jsonl`, riverificato: 0 righe) non ha bisogno del suo tredicesimo controllo di gate. Ha bisogno che qualcuno prenda l'asset già scritto (AP-056), gli metta un prezzo (gesto di Max, non ancora fatto), gli colleghi una cassa (gesto tecnico, non ancora fatto), e lo mandi a un lettore. Tutto il resto — comprese queste 1.352 righe — può aspettare che il primo euro sia arrivato.

---

## Connessioni
- `competitor/Andrei Pascu/piano-implementazione/DRAFT-V1-A-lanci.md` — bersaglio §1, §2, §3, §5, §6
- `competitor/Andrei Pascu/piano-implementazione/DRAFT-V1-B-capacita.md` — bersaglio §1, §2
- `company/Memory/decisions/ADR-016-ultimo-metro.md` — fonte §2
- `company/Memory/decisions/ADR-028-niente-blocca-tutto.md` — contesto §2, §6
- `competitor/Andrei Pascu/ANDREI-PASCU-DOSSIER-COMPLETO.md` · `site-study/SINTESI-METODO.md` — fonte §5
- `competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md` — verifica numeri §4
- `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/andrei-pascu-armageddon-outfunnel-001/lessons/lezione-15/lesson-analysis.md` — verifica numero §4
- `company/Memory/tesoreria/entrate.jsonl` · `spese.jsonl` — riverificati, 0 righe entrambi
- `.claude/skills/fabbrica-siti/scripts/` — riverificato, `catena.py` non esiste
