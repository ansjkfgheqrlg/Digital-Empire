# Preventa — Architettura completa del flusso (outreach + produzione contenuti)

**Scopo di questo documento**: spiegare passo-passo, senza saltare pezzi, tutto
quello che è stato costruito per Preventa — dal comando che accende lo scraping
fino al messaggio che arriva davvero su WhatsApp a un concessionario, e dal
comando che genera un carosello fino al PNG (quando lanciato). Scritto perché
Max ha chiesto di poter verificare, punto per punto, che sia stato fatto quello
che ha chiesto.

**Data**: 2026-08-03. **Stato**: outreach WhatsApp operativo e verificato su
invii reali. Produzione caroselli: scaffold completo, non ancora lanciata dal
vivo (richiede conferma esplicita, vedi §7).

---

## 1. Vista d'insieme — i due flussi

```
                         ┌─────────────────────────────┐
                         │   /avvia-outreach-preventa   │
                         └──────────────┬────────────────┘
                                        │
              ┌─────────────────────────┴─────────────────────────┐
              │                                                     │
              ▼                                                     ▼
     FLUSSO A — OUTREACH                                 FLUSSO B — PRODUZIONE
     (operativo, testato)                                (scaffold pronto,
                                                            non ancora lanciato)
   Scraping → Qualifica → Areus                          Copy Preventa (scritto)
        → Filtro solo-import (NUOVO)                          → Arena/Playwright
        → Genera messaggio (4 ganci)                           (motore condiviso
        → Gate Bibbia dei Messaggi                              con Agency, non
        → Invio WhatsApp reale                                  ancora lanciato)
        → Report
```

I due flussi sono **indipendenti** oggi: l'outreach manda messaggi WhatsApp,
la produzione genera immagini per post Instagram. Condividono solo il
posizionamento/prezzo del prodotto (€2.000 una tantum, target concessionari
import) — non condividono codice.

---

## 2. FLUSSO A — Outreach WhatsApp giornaliero

### 2.1 Comando che accende tutto
```
/avvia-outreach-preventa
```
Apre una finestra CMD visibile ed esegue:
```
python Outreach/preventa-maps-scraper/outreach_giornaliero.py
```
File skill: `~/.claude/skills/avvia-outreach-preventa/SKILL.md`.

### 2.2 Fase 1 — Scraping (Google Maps, focus import)
File: `outreach_giornaliero.py::fase1_scraping()`.

1. `citta_di_oggi()` sceglie 6 città dal pool di 55 città italiane
   (`05-TEMPLATES-E-KIT/cities.txt`), a rotazione deterministica basata sul
   giorno dell'anno (giorni diversi = città diverse, nessuna ripetizione
   ravvicinata).
2. Per ognuna delle 6 città, cerca su Google Maps con 3 query import-focus
   (`IMPORT_QUERIES`): *"concessionario auto import"*, *"concessionario auto
   import Germania"*, *"auto import usate"*.
3. Chiama `scraper.py` (wrapper di `02-AUTOMAZIONI-E-SCRIPTS/run.py`), limite
   20 risultati per combinazione città×query.
4. Ogni risultato viene **qualificato** (`checker.py::calcola_priorita()`):
   controlla se ha sito, se il sito è vecchio/lento, quante recensioni ha, se
   ha pixel/tracking pubblicitario attivo → assegna `priorita_lead`
   (ALTA/MEDIA/BASSA) e scrive il motivo in `note_qualifica`.
5. Ogni lead qualificato viene caricato su **Areus** (il CRM interno,
   `EmpireDesk/platform/`) in stage `NEW` — non più Google Sheets (migrazione
   fatta il 2026-07-28, vedi CP-20260728-002).

**Verificabile da te**: apri EmpireDesk → pannello "Preventa — Outreach
Freddo" → vedi i lead nuovi con città, priorità, telefono, categoria.

### 2.3 Fase 2 — Filtro SOLO-import reale (🆕 costruito oggi, CP-20260803-005)

**Il problema che c'era prima**: la query di ricerca (`categoria`, es.
"concessionario auto import Germania") veniva usata come "prova" che il lead
fosse un vero importatore. Ma **tutte** le query contengono la parola
"import" — quindi quel controllo era sempre vero, per ogni lead, a
prescindere da chi importasse davvero. Non filtrava nulla.

**Cosa fa ora** (`outreach_giornaliero.py::sembra_import_reale()`): prima di
contattare un lead, cerca keyword reali (`import`, `estero`, `tedesche`,
`francesi`, `belgio`, `olanda`, `svizzera`, `austria`, `europa`, `km0`,
`reimport`, ecc.) dentro **nome dell'attività + note di qualifica**. Solo se
trova un segnale reale, il lead entra nella lista da contattare.

**Verificato su dati reali** (228 lead in Areus): su 29 lead NEW con telefono
mobile valido, solo **8** superano il filtro. Esempi che passano: "German
Auto", "Sally auto Import export srl", "Autotedesche.it". Esempi che NON
passano (scartati, restano in Areus ma non vengono contattati oggi): "Kaufmann
S.a.s", "Eurocar Brescia" — nomi che *sembrano* import ma senza una keyword
riconoscibile nel nome/note. Il funnel si restringe (~72%) ma non si azzera.

Questo conteggio (`scartati_no_import`) è **sempre loggato**, mai silenzioso —
lo vedi nel report giornaliero e nel riepilogo a fine run.

### 2.4 Fase 3 — Generazione del messaggio (4 ganci)
File: `personalizza_messaggi.py::scegli_gancio()` (2 copie sincronizzate a
mano, una in `Outreach Workflow/campagne/concessionari-preventa/`, una nella
sua sottocartella `02-AUTOMAZIONI-E-SCRIPTS/`).

Ogni lead che supera il filtro riceve UNO dei 4 ganci, in ordine di priorità:

| # | Gancio | Quando scatta | Esempio apertura |
|---|--------|----------------|-------------------|
| 4 | **Import / annunci esteri** | Segnale import reale trovato (§2.3) — ha priorità su tutto il resto | "fate anche auto di importazione... con gli annunci esteri il preventivo richiede doppio lavoro" |
| 3 | PDF brutto / brand | Priorità ALTA + nessun sito o sito vecchio | leva l'immagine curata online vs preventivi che escono storti |
| 2 | Cliente perso su WhatsApp | Priorità ALTA + poche recensioni | attività poco digitalizzata |
| 1 | Tempo perso (control) | Nessuno dei precedenti | dolore universale, gancio di base |

Dato che oggi il filtro import scarta già tutto ciò che non ha segnale reale
(§2.3), **quasi tutti i lead che arrivano a questo punto prendono il Gancio
4** — coerente con l'ordine di Max ("focus totale sui concessionari import").

### 2.5 Fase 4 — Gate "Bibbia dei Messaggi" (Rule Keeper)
File: `Outreach/agents/outreach-message-team/rule_keeper_lint.py`.

Prima di mandare qualsiasi messaggio, viene passato attraverso un controllo
deterministico (no chiamata AI, veloce, gratis) sui **5 Pilastri** stabiliti
da Max il 2026-07-30 (framework Barnum/Rainbow + 5 Pilastri, vedi
`Outreach/knowledge/bibbia-messaggi-outreach.md`):

1. Personalizzazione presente (nome attività citato)
2. Mittente chiaro entro 150 caratteri
3. Niente prezzo nel primo messaggio
4. CTA che chiude con una domanda, non un comando ad alto impegno
5. Lunghezza sotto soglia WhatsApp

Se un messaggio viola una regola → **`RESPINTO`, non viene mai inviato**,
loggato come `bocciato_bibbia`, si passa al lead successivo. Bug reale trovato
e corretto in un run di test: il controllo leggeva anche il nome
dell'attività ripetuto nel messaggio, quindi "Compravendita" faceva scattare
il divieto sulla parola "compra" — corretto escludendo il nome
dall'analisi e usando confini di parola precisi.

### 2.6 Fase 5 — Invio WhatsApp reale
File: `Outreach/WhatsApp Automation/send_message.py`.

- Usa un **profilo Chromium persistente** (`whatsapp-profile/`, non
  committato in git — vedi `.gitignore`), la stessa sessione che hai
  autenticato tu scansionando il QR code. Non è WhatsApp Web "usa e getta":
  è il tuo WhatsApp vero, loggato una volta, riusato ad ogni run.
- Normalizza il numero (mobile italiano, gestisce prefissi correttamente).
- Apre la chat, gestisce il caso "numero non è su WhatsApp" (lo riconosce come
  scarto legittimo, non un errore tecnico), gestisce l'overlay "Inizio chat in
  corso".
- Ritmo umano: pausa casuale **45-120 secondi** tra un invio e il successivo
  (non un bot che spara messaggi a raffica).
- **Rilevamento ban**: se WhatsApp mostra segnali di blocco account, l'invio
  si ferma **immediatamente**, non insiste.
- **Circuit breaker**: se **5 invii falliscono di fila** per motivi tecnici
  (non scarti legittimi), il run si ferma da solo — probabile segno che
  qualcosa è cambiato in WhatsApp Web o il profilo è rotto, meglio fermarsi
  che continuare a fallire in silenzio.

Dopo un invio riuscito: `areus.mark_contacted()` sposta il lead a stage
`CONTACTED` su Areus, così non viene ricontattato.

### 2.7 Fase 6 — Cap giornaliero e report
- Cap di default: **50 messaggi/giorno** (`--daily-cap`, personalizzabile).
- Il cap conta gli invii **REALI** già fatti oggi, non gli tenta — se rilanci
  lo script due volte nello stesso giorno, non sfonda il limite.
- A fine run: `scrivi_report()` scrive un log in
  `Outreach/preventa-maps-scraper/logs/outreach_YYYY-MM-DD.log` con inviati,
  falliti, scartati (numero non valido), scartati (no segnale import),
  bocciati dalla Bibbia — tutto tracciato, niente nascosto.

### 2.8 Scenari concreti (come chiesto da Max — "nelle varie situazioni")

| Situazione | Cosa succede |
|---|---|
| Lead nuovo, nome "Autotedesche.it", mobile, ALTA priorità | Passa il filtro import → Gancio 4 → passa la Bibbia → inviato, stage→CONTACTED |
| Lead nuovo, nome "Auto Bianchi Srl", trovato dalla query import ma senza keyword | **Scartato dal filtro import** (§2.3) — resta in Areus stage NEW, non contattato oggi, contato in `scartati_no_import` |
| Messaggio generato contiene il prezzo nel primo contatto | **Bocciato dalla Bibbia** prima di partire, mai inviato, loggato `bocciato_bibbia` |
| Numero non registrato su WhatsApp | WhatsApp mostra il popup "non è su WhatsApp" → riconosciuto, scartato come `numero_non_su_whatsapp`, NON conta come errore tecnico |
| 5 invii di fila falliscono per motivi tecnici | Circuit breaker: il run si **ferma da solo**, log chiaro sul motivo |
| WhatsApp segnala limitazione account | Stop immediato, nessun altro tentativo in quel run |
| Cap giornaliero (50) già raggiunto oggi | Il run parte, controlla quanti ne mancano, si ferma appena tocca il cap reale |

### 2.9 Cosa è VERO oggi (non teoria)
- ✅ Scraping reale verificato (228 lead reali in Areus da run passati).
- ✅ Invio WhatsApp reale verificato (messaggi consegnati per davvero, testato
  con cap piccoli prima di scalare).
- ✅ Filtro import reale verificato sui dati veri (8/29 passano).
- ✅ Gate Bibbia verificato contro i 3 ganci reali di produzione.
- ✅ Circuit breaker e rilevamento ban implementati (non ancora innescati da
  un vero blocco account, perché non se n'è mai verificato uno finora).

---

## 3. FLUSSO B — Reparto Produzione: Progetto Preventa (caroselli Instagram)

### 3.1 Cosa aveva chiesto Max
"L'azienda deve avere un reparto produzione con progetti e categorie...
creare ORA il progetto Preventa con caroselli Instagram promozionali, riusando
lo stile perfetto già costruito per altri prodotti, collegato con Arena
attraverso Playwright — non ripartire da zero."

### 3.2 Cosa c'era davvero sul disco (verificato oggi, non assunto)
Prima di scrivere una riga di codice, sono stati trovati **3 sistemi
caroselli indipendenti** — facile confonderli perché fanno tutti "caroselli
Instagram":

1. **ArenaAI** (`SKILL & Agenti/Workflow agency creative/caroselli - agency/`)
   — automazione **reale** via Playwright su Arena.ai: apre un browser vero,
   con un profilo autenticato persistente, seleziona modalità Direct e
   modello immagine, gestisce captcha automaticamente, genera 3 slide in
   sequenza (la seconda usa la prima come riferimento, la terza usa la
   seconda — così lo stile resta coerente). Ha anche un motore di copy via AI
   (Groq/OpenRouter) e una dashboard Next.js.
2. **carousel-factory** (`Workfolw crea caroselli à/carousel-factory/`) —
   Puppeteer (non Playwright), le foto si generano **a mano** su Gemini
   (nessuna automazione browser, nessuna chiave API immagini configurata). Un
   altro progetto Claude ci sta già lavorando sopra per un brand diverso
   (mentalità-brutale) — **non toccato**.
3. **carousel-empire** (skill Claude installata) — genera PNG senza passare
   da Arena o da un browser, sistema completamente diverso.

**Ho chiesto a Max quale intendesse** (rischio concreto: costruire su quello
sbagliato = lavoro buttato) → **confermato: ArenaAI**, il primo.

### 3.3 Cosa è stato costruito
Nuova cartella **sibling**, `caroselli - preventa/`, accanto a `caroselli -
agency/` (che NON è stata toccata — solo letta):

```
caroselli - preventa/
├── REGOLE.md                              (contesto Preventa, colori brand)
├── config_preventa.py                     (isola output/reference da Agency)
├── Agents/copywriter_agent_preventa.py    (copy Preventa, CTA diversa da Agency)
├── orchestrator_preventa.py               (collega copy + motore Arena condiviso)
└── output_preventa/esempio-01-tempo-perso/carousel_plan.json  (primo copy scritto)
```

Il motore vero e proprio (`ArenaAI/arena_generator.py`, browser automation)
**non è duplicato** — viene importato direttamente da `caroselli - agency/`.
Questo rispetta la regola "wrap, mai riscrittura" (ADR-003): un solo motore,
riusato da più progetti.

**Colori brand reali usati** (non inventati, presi da `Crea siti/Preventa/
index.html`, il sito già live): blu `#101E3E` (fiducia, automotive premium),
arancione `#FF4D00` **solo** per CTA/accenti (mai oltre il 10% della slide).

**Differenza importante dal progetto Agency**: Agency vende tramite DM
Instagram ("scrivimi X in DM per una call") — Preventa vende tramite outreach
WhatsApp diretto (Flusso A sopra), NON tramite DM. Quindi il copywriter
Preventa scrive CTA di *brand awareness* (segui/scopri di più), mai una
vendita diretta nella slide — sarebbe un canale sbagliato per il prodotto.

**Primo esempio di carosello (copy pronto, scritto a mano, stesso schema che
userebbe l'AI)**:
1. Hook: *"20 minuti su excel mentre il cliente scrive già ad altri 3"*
2. Soluzione: *"incolli il link dell'annuncio, esce il pdf pronto in
   italiano"*
3. CTA: *"preventa. il preventivo pronto prima che il cliente cambi idea"*

### 3.4 Un bug trovato e corretto durante la costruzione
La prima bozza pensava che servisse una "chat Arena dedicata" per non
mischiare lo stile Preventa con quello Agency. **Falso** — letto il codice
sorgente vero (`arena_generator.py`): il motore riapre `arena.ai` da zero per
ogni singola slide, non tiene mai una chat aperta. La coerenza visiva viene
dal ricaricare l'immagine della slide appena fatta come allegato per la
successiva. Quello che isola davvero Preventa da Agency è **dove finiscono i
file e quali immagini di riferimento vengono usate** — sistemato in
`config_preventa.py`.

### 3.5 Cosa MANCA (onestamente, non nascosto)
- **Nessun visual è ancora stato generato**. Il copy è pronto, il codice è
  collegato e compila senza errori, ma nessuno ha ancora premuto "genera
  davvero" — perché farlo apre un browser vero sull'account Arena vero di
  Max e consuma un ciclo di generazione reale (rischio captcha/errori/tempo).
  **Serve un tuo via libera esplicito** (vedi §7) — stesso principio già
  seguito per l'invio WhatsApp: prima si costruisce e si verifica che
  funzioni, poi si lancia davvero, non il contrario.
- Il primo run non avrà immagini di riferimento (nessun carosello Preventa
  esiste ancora) — lo stile verrà descritto solo a parole nel prompt. La
  prima slide generata diventerà poi il riferimento per i caroselli
  successivi.

---

## 4. ⚠️ Problema di sicurezza trovato (non risolto, decisione tua)

Mentre leggevo `caroselli - agency/config.py` per capire come riusarlo, ho
trovato che contiene **la tua email e password reali di Arena.ai**, più le
chiavi API di Groq e OpenRouter, **scritte in chiaro**. Questo file è
committato in git dal primo commit del monorepo ed è già stato pushato sul
repository GitHub (`ansjkfgheqrlg/Digital-Empire`).

Non è un problema che ho creato io, e non l'ho toccato — spostare credenziali
e riscrivere la storia di git sono operazioni che possono avere effetti
collaterali seri, quindi non le faccio senza il tuo ok esplicito. Le opzioni
sono, in ordine di solidità:

1. Spostare le credenziali in un file `.env` locale (aggiunto a `.gitignore`,
   come già fatto per i profili Chromium/WhatsApp) + **ruotare** (cambiare)
   la password Arena e rigenerare le due chiavi API, perché sono già visibili
   nella storia di git anche se le sposto adesso.
2. Solo spostarle in `.env` senza ruotarle (più veloce, ma chiunque abbia mai
   avuto accesso al repository le ha già viste).
3. Lasciare così (sconsigliato — è una password vera del tuo account).

---

## 5. Come lanciare tutto (comandi reali)

**Outreach WhatsApp (operativo oggi)**:
```
/avvia-outreach-preventa
```
oppure manualmente, con un cap ridotto per test:
```
python Outreach/preventa-maps-scraper/outreach_giornaliero.py --daily-cap 10
```

**Produzione carosello Preventa (pronto, in attesa di via libera)**:
```
cd "SKILL & Agenti/Workflow agency creative/caroselli - preventa"
python orchestrator_preventa.py
```
Genera copy nuovo via AI. Per usare il copy già scritto a mano
(`output_preventa/esempio-01-tempo-perso/carousel_plan.json`) invece di farne
generare uno nuovo, va passato direttamente a `generate_carousel_visuals()` —
un collegamento di 2 righe, non ancora fatto perché non ha senso finché non
c'è il via libera per il run reale.

---

## 6. Checklist — cosa ho fatto rispetto a quello che hai chiesto

- [x] Fase 1 — filtro solo-import reale (non più query-bias vacuo)
- [x] Fase 2 — IG/LinkedIn: **non toccato**, resta bloccato come richiesto
- [x] Fase 3 — Reparto Produzione + Progetto Preventa: scaffold completo,
      motore corretto identificato e confermato con te, nessuna collisione
      con il lavoro dell'altra sessione su carousel-factory
- [x] Tutto salvato: checkpoint, STATO-EMPIRE, wiki, commit, push — niente
      solo "in memoria della chat"
- [ ] Run live del carosello Preventa — **in attesa del tuo via libera**
- [ ] Decisione sicurezza credenziali Arena/API — **in attesa della tua scelta**

---

## 7. Le due cose che servono da te per "partire in sesta" per davvero

1. **Via libera per generare il primo carosello Preventa dal vivo** (apre un
   browser reale sul tuo account Arena, ~3-5 minuti, può incontrare captcha).
2. **Decisione sulle credenziali esposte** (§4) — anche solo "sposta in .env,
   rotazione la faccio dopo" va bene, ma voglio la tua parola prima di
   toccare quel file.

Con questi due via liberi, entrambi i flussi sono operativi end-to-end.
