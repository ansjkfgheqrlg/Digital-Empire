# Analisi Competitor — Legami d'Amore (@Legamidiamore)

**Redatto da:** Sentinella Emperator (analisi a freddo, sessione dedicata)
**Data ricerca:** 2026-09-03
**Metodo:** lettura cache locali (`memory/channel_videos/*.json`) + tentativi di verifica live via WebFetch/WebSearch su pagine pubbliche YouTube

## ⚠️ Nota metodologica importante — leggere prima di usare questi dati

Nel corso della ricerca **YouTube ha bloccato quasi tutti i tentativi di lettura diretta e live** delle pagine canale/video dal nostro ambiente:
- Ogni fetch diretto a `youtube.com/@handle/about` o `/videos` è stato rediretto a un **consent wall GDPR** (`consent.youtube.com`), che impedisce di leggere iscritti, conteggio video e frequenza di pubblicazione in tempo reale.
- Un proxy di lettura alternativo (`r.jina.ai`) ha funzionato **solo parzialmente**: sulle pagine "about" dei 3 canali ha restituito il **nome canale** (utile per confermare la lingua) ma non le statistiche (401/CAPTCHA). Su alcune pagine-video singole invece ha funzionato per intero.
- **Conseguenza pratica**: i dati di iscritti e frequenza di pubblicazione **recente** (ultime 2-4 settimane) qui sotto sono in parte stimati dalla cache locale (datata **26 agosto 2026**, non 29 come indicato nel brief — verificato leggendo i file), non da uno scrape live di oggi. Lo dichiaro esplicitamente riga per riga. Dove non sono riuscito a verificare un dato, scrivo **NON VERIFICABILE** invece di stimarlo a caso.

---

## 1. I 3 canali sorgente principali

### 1.1 @PsicologiaFemminile-f8c

- **Lingua reale:** ITALIANO confermato. Nome canale live: **"Psicologia Femminile"** (confermato via fetch della pagina /about, oggi). Tutti i titoli in cache sono in italiano ("7 tocchi che faranno innamorare...", "6 segnali nascosti che indicano...", ecc.).
- **Iscritti:** NON VERIFICABILE oggi (pagina bloccata da consent wall/401). Non stimo un numero.
- **Frequenza di pubblicazione:** dato preso dalla cache del 26/08 (quindi proxy, non le "ultime 2-4 settimane" di oggi 3/09): nella finestra osservata risultano diversi video pubblicati entro 1-14 giorni dal fetch (es. video a 24h, 96h, 168h, 192h, 240h, 312h dal fetch), su un totale di ~91 video nella cache che coprono ~120 giorni. Stima grezza: **circa 5-7 video/settimana storicamente**, il ritmo più alto dei 3 — coerente con l'essere descritto come "il canale più prolifico".
- **Pattern titolo/thumbnail ricorrenti (dalla cache):**
  - Numeri dispari in apertura ("3", "5", "6", "7", "9", "10", "11") + "segnali/segreti/motivi che..."
  - Struttura fissa: "[N] segnali che [comportamento femminile] | Psicologia femminile"
  - Uso ricorrente di emoji 🔥 in apertura titolo per i video più recenti/pushati
  - Mix di contenuto "soft" (attrazione, corteggiamento) e contenuto più esplicito/spinto (es. titoli su sesso, tradimento, "Psicologia Oscura") — gamma più ampia della nostra
  - Molti video corti da 15-60s con hashtag in coda (#psicologia #relazioni) accanto a video "guida" più lunghi
- **Ordine di grandezza view (dalla cache):** i video recenti (ultimi giorni) partono bassi (decine-centinaia) e i video con 1-4 mesi di vita arrivano a 3.000-31.000 view. Il video più visto in cache: 31.000 view (età ~4 mesi).
- **Cosa funziona meglio di noi:** volume di pubblicazione molto più alto, ampiezza tematica (spaziano su temi più "spinti" che noi probabilmente evitiamo per policy/compliance), uso sistematico di emoji per segmentare i titoli hot.
- **Cosa non funziona/rischio:** titoli e thumbnail che sconfinano verso contenuto esplicito (rischio compliance/demonetizzazione), alta produzione ma view molto disomogenee (lunga coda di video sotto le 300 view).

### 1.2 @PsicologiadellAttrazionee

- **Lingua reale:** ITALIANO confermato. Nome canale live: **"Psicologia dell'Attrazione"**.
- **Iscritti:** NON VERIFICABILE oggi.
- **Frequenza di pubblicazione:** dalla cache (22 video totali, arco osservato fino a ~150 giorni), ritmo stimato **~1 video/settimana**, il più lento dei 3 — coerente con la descrizione del brief.
- **Pattern titolo/thumbnail ricorrenti:**
  - Titoli più "da coach" e meno da lista numerata rispetto a PsicologiaFemminile: "Come farle pensare a te senza inviarle nemmeno un messaggio", "Cosa rende un uomo davvero attraente"
  - Quando usano numeri, prevale il taglio "tecnica/comando" (es. "5 Segreti Psicologici che Fanno Impazzire le Donne di Te") — coerente con l'essere la fonte per la nostra Strategia B
  - Uso di "..." e frasi tra parentesi per creare curiosity gap ("Pensavo Di Non Essere Attraente... (Poi Ho Notato Queste 7 Cose)")
- **Ordine di grandezza view:** più basso e più uniforme del canale precedente — punte a 4.600-6.800 view sui video più vecchi (4+ mesi), la maggioranza recente sotto le 1.000 view.
- **Cosa funziona meglio di noi:** angolo "tecnica/comando" più assertivo, meno lista-e-basta e più promessa di controllo diretto sulla situazione.
- **Cosa non funziona:** cadenza bassa = poca superficie di scoperta, coerente col vph più basso.

### 1.3 @DinamicheSocialiAcademy

- **Lingua reale:** ITALIANO confermato.
- **⚠️ Scoperta rilevante:** il canale **ha cambiato nome visualizzato**. L'handle è ancora `@DinamicheSocialiAcademy` ma il nome pubblico oggi è **"Relazioni in Focus"**. Nella cache del 26/08 non compariva ancora questo rebrand nei metadati salvati (solo handle). Va verificato se è un rebrand recente (ultimi giorni) o se semplicemente non era mai stato tracciato prima — comunque va aggiornato nei nostri riferimenti interni.
- **Iscritti:** NON VERIFICABILE oggi.
- **Frequenza di pubblicazione:** dalla cache (~91 video, arco fino a ~180 giorni), stima grezza **~3-4 video/settimana**, ma con rendimento per-video molto più basso della concorrenza (vedi sotto) — coerente col vph storico più basso indicato nel brief (0.16).
- **Pattern titolo/thumbnail ricorrenti:**
  - Taglio "critica sociale/crisi maschile" molto marcato, distinto dagli altri due: "Perché gli uomini stanno scomparendo", "Perché l'80% degli uomini è diventato INVISIBILE", "Solitudine Maschile"
  - Uso pesante di CAPS LOCK per 1-3 parole chiave nel titolo
  - Uso di emoji d'allarme (🛑 ⚠️ 🚫 🚪) invece di 🔥
  - Riferimenti espliciti all'anno corrente nel titolo ("Relazioni 2026", "La verità scioccante del 2026") — leva di attualità che noi non usiamo
- **Ordine di grandezza view:** i due video più vecchi/virali in cache arrivano a 7.800-10.000 view; il resto del catalogo scende rapidamente sotto le 500 view, con una lunga coda sotto le 100 — la dispersione più ampia dei 3 canali.
- **Cosa funziona meglio di noi:** framing "crisi sociale maschile" con urgenza e vittimismo del target maschile, leva dell'attualità (anno in titolo), CAPS per keyword.
- **Cosa non funziona:** il rendimento medio più basso dei 3 nonostante volume medio-alto — segnale che il taglio "allarme sociale" ha un tetto di attenzione più basso della lista di segnali pratici.

---

## 2. Confronto con il nostro canale (@Legamidiamore) — fatto verificato

Dalla cache `Legamidiamore.json` (fetch 2026-08-29, quindi anche questa datata di qualche giorno): su **28 video in cache, 25 sono in INGLESE** (titoli come "5 Body Language Signs That Make a MAN Irresistible", "7 Signs She Really Wants You Female Psychology") e solo **3 sono in italiano**, tutti concentrati tra i più recenti in cache (es. "Se Fa QUESTO... È Già Tua (Psicologia Femminile Svelata)").

**Implicazione per il confronto:** per mesi il nostro canale ha competuto in un mercato anglofono enorme e affollatissimo (migliaia di canali "female psychology" USA/UK/India), non nella nicchia italiana dei 3 competitor sopra. Il cambio recente verso titoli italiani ("7 SEGNALI che una DONNA...") ci sposta ora in un mercato molto più piccolo e diverso, dove i 3 competitor sopra sono i riferimenti diretti reali — ma il confronto storico vph tra noi e loro **non è comparabile 1:1** finché la maggioranza della cache è in inglese: stiamo confrontando fasi editoriali diverse dello stesso canale.

---

## 3. Nuovi competitor italiani individuati (non nella lista originale)

La ricerca via YouTube Search/Google ha restituito soprattutto canali "da coach" con volto in camera, non faceless come noi — lo dichiaro perché cambia il tipo di confronto possibile.

### 3.1 Giada Baccianella — Love Coach
- **Formato:** NON faceless — coach reale on-camera, personal brand.
- **Iscritti:** **115.000** (verificato live via fetch di una pagina video del canale).
- **Lingua:** italiano.
- **Contenuto:** stessa area tematica ("10 modi per capire se una donna è innamorata di te"), ma tono da coaching/autorevolezza personale, non slideshow a voce sintetica.
- **Cosa fa meglio di noi:** credibilità del volto reale + numeri già alti; format video "premiere"/live che genera community.
- **Cosa non è direttamente comparabile:** format completamente diverso dal nostro (non faceless), quindi non è un competitor 1:1 sul CTR/thumbnail, ma è un benchmark di autorità nella nicchia.

### 3.2 Riccia Capriccia
- **Formato:** titoli e struttura molto vicini al nostro stile (liste numerate, CAPS su parole chiave, taglio esplicito su desiderio/attrazione: "7 desideri SESSUALI segreti delle donne A LETTO", "Uomo MATURO: le donne PIÙ GIOVANI fanno QUESTO per FAR COLPO su di TE") — sembra il più vicino ai 3 competitor originali per tono.
- **Iscritti:** **23.700** (verificato live).
- **Lingua:** italiano.
- **Non verificato:** se il formato sia realmente faceless/voce sintetica o presenza on-camera parziale — non sono riuscito ad accedere alla pagina /videos per controllare le thumbnail (bloccata da consent wall). Da verificare manualmente aprendo il canale nel browser.
- **Cosa sembra fare meglio di noi:** titoli più diretti/espliciti sul desiderio sessuale femminile, leva CAPS aggressiva su 1-2 parole per titolo.

### 3.3 LA VERA LOGICA DELLE DONNE (@LAVERALOGICADELLEDONNE)
- **Formato:** NON VERIFICATO — il nome e il posizionamento nei risultati di ricerca suggeriscono un canale dello stesso tipo (segnali/psicologia femminile per uomini), ma ogni tentativo di leggere la pagina canale è stato bloccato (401/CAPTCHA sia diretto che via proxy).
- **Iscritti, cadenza, view:** NON VERIFICABILE con gli strumenti disponibili in questa sessione.
- Lo includo solo come **pista da verificare manualmente** da parte di Max/Gael aprendo il canale nel browser — non aggiungo dati inventati.

### 3.4 @codicedonna — già noto, campione ancora troppo piccolo
- Confermato dalla cache: solo 3 video, view bassissime (2, 8, 21). Resta uno scarto valido per campione insufficiente, non lo promuovo a competitor attivo.

---

## 4. Tabella comparativa finale

| Canale | Lingua | Iscritti | Frequenza pubblicazione | vph / ordine di grandezza view | Pattern che usano e noi no |
|---|---|---|---|---|---|
| **@Legamidiamore (noi)** | Italiano (dal recente switch; storicamente inglese) | N/D (nostro dashboard interno) | variabile, vedi dashboard interno | recente: decine-migliaia view/video | — |
| **@PsicologiaFemminile-f8c** | Italiano | NON VERIFICABILE oggi | ~5-7 video/sett. (proxy cache 26/08) | vph storico ~5.1 (fonte brief, coerente con calcolo su cache) — punte fino a 31.000 view | emoji 🔥 in apertura titolo, gamma tematica più spinta, volume molto alto |
| **@PsicologiadellAttrazionee** | Italiano | NON VERIFICABILE oggi | ~1 video/sett. (proxy cache 26/08) | vph storico ~0.46 — punte 4.600-6.800 view | taglio "tecnica/comando" assertivo, curiosity gap con "..." nel titolo |
| **@DinamicheSocialiAcademy** (oggi "Relazioni in Focus") | Italiano | NON VERIFICABILE oggi | ~3-4 video/sett. (proxy cache 26/08) | vph storico ~0.16 — punte 7.800-10.000 view, coda lunga sotto 100 | CAPS su parole chiave, emoji d'allarme ⚠️🛑, anno corrente nel titolo ("2026"), framing "crisi sociale maschile" |
| **Giada Baccianella Love Coach** (nuovo) | Italiano | 115.000 (live) | NON VERIFICATO | NON VERIFICATO in dettaglio | volto reale/autorità personale, format "premiere" |
| **Riccia Capriccia** (nuovo) | Italiano | 23.700 (live) | NON VERIFICATO | NON VERIFICATO in dettaglio | titoli più espliciti su desiderio sessuale, CAPS aggressivo su 1-2 parole |
| **LA VERA LOGICA DELLE DONNE** (nuovo, da verificare) | presunto italiano | NON VERIFICABILE | NON VERIFICABILE | NON VERIFICABILE | — |
| **@codicedonna** (già noto) | Italiano | NON VERIFICABILE | campione troppo piccolo (3 video) | view bassissime (2-21) | — |

---

## 5. Limiti dichiarati di questa ricerca

1. Nessun iscritto verificato live per i 3 competitor principali: YouTube ha bloccato ogni fetch diretto con consent wall GDPR; il proxy alternativo ha funzionato solo per leggere il nome canale, non le statistiche.
2. La frequenza di pubblicazione "ultime 2-4 settimane" richiesta nel brief non è stata misurata su dati di oggi, ma stimata dalla cache locale del 26/08/2026 (quindi con oltre una settimana di scarto) — dichiarato riga per riga sopra, da non spacciare per dato fresco.
3. Il vph storico riportato nel brief (5.1 / 0.46 / 0.16) è stato controllato per plausibilità ricalcolando views/age_hours su un campione della cache: i valori sono coerenti con l'ordine di grandezza dichiarato, ma non è un ricalcolo esatto sull'intero catalogo.
4. I 2 nuovi competitor con dati reali (Giada Baccianella, Riccia Capriccia) non sono faceless come noi — cambia il tipo di confronto possibile (autorità personale vs. voce sintetica anonima). Il terzo candidato (LA VERA LOGICA DELLE DONNE) resta da verificare manualmente.
5. Due file di cache locale citati nel brief come possibile punto di partenza (`ciraolone.json`, `linguaggiosegretodelcorpo-6589.json`) **non sono pertinenti alla nicchia**: il primo è un canale di tutorial AI/tech, il secondo un canale di tango/danza. Probabile scrape errato in una sessione precedente — segnalo per pulizia della cache.

## 6. Consigli (chiusura standard)

1. **Ripetere lo scrape con Playwright/browser reale** (come già fatto per la cache del 26/08) invece di WebFetch/proxy per ottenere iscritti e frequenza aggiornati — questo ambiente non riesce a superare il consent wall di YouTube in modo affidabile.
2. **Verificare manualmente nel browser** il canale "LA VERA LOGICA DELLE DONNE" e le thumbnail di "Riccia Capriccia" per confermare se sono davvero faceless/voce sintetica — sono i candidati più vicini al nostro formato tra quelli trovati.
3. **Pulire la cache** `memory/channel_videos/`: rimuovere o rietichettare `ciraolone.json` e `linguaggiosegretodelcorpo-6589.json`, non pertinenti alla nicchia Legami d'Amore.
4. **Aggiornare il riferimento interno** per l'handle `@DinamicheSocialiAcademy`: il nome pubblico oggi è "Relazioni in Focus" — se è un rebrand recente potrebbe segnalare un riposizionamento della loro strategia editoriale, da monitorare al prossimo scrape.
5. Nel report finale a Max, segnalare esplicitamente che **il confronto vph noi-vs-competitor è inquinato dallo switch inglese→italiano** del nostro canale: prima di trarre conclusioni sul confronto CTR/vph, isolare solo i video italiani recenti nostri contro i competitor italiani.
