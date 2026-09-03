---
Type: PROJECT
Status: Active
Tags: #lanci #assorbimento #L2 #ecosistema-14 #TASK-LANCI-ECO-W2
Created: 2026-09-02
Last updated: 2026-09-03
Autore: Gael (via Emperator)
Task: TASK-LANCI-ECO-W2 — sotto-task L2
Gate L2: ✅ PASSATO — 10 fonti su 10 aperte, ogni riga con file sorgente e reparto
---

# ASSORBIMENTO LANCI — cosa contengono i progetti vecchi e dove finisce

> **Deliverable di L2, completo.**
> Per ogni progetto vecchio: quali framework, checklist e criteri concreti contiene, e in
> quale reparto del nuovo ecosistema finiscono.
>
> **Gate L2:** ogni riga punta a un **file sorgente reale** e a un **reparto di destinazione**.
> Zero righe "da approfondire". Dove una fonte è vuota o non pertinente, è **dichiarata tale
> con la prova** (§2, §12), non lasciata in sospeso.

---

## 0. Metodo e inventario

Comandi eseguiti il 2026-09-02/03 dalla root del monorepo:

```bash
find "<cartella>" -type f              # inventario per ogni fonte
wc -l *.md                             # peso reale
md5sum <a> <b> ; diff -rq <a> <b>      # verifica dei duplicati
find . -iname "*.skill*"               # esistenza delle skill dichiarate
python -c "from pypdf import PdfReader ..."   # estrazione testo dai PDF
```

| Fonte | File | Righe / pagine | Stato |
|---|---:|---:|---|
| `System OMEGA/.../Project-Marketing University.md/` | 16 | **11.853 righe** | ✅ Aperta |
| `System OMEGA/.../Project-Strategy Command Center/` | 13 | **8.968 righe** | ✅ Aperta |
| `System OMEGA/.../YouTube Lead Engine/` | 7 | **2.860 righe** | ✅ Aperta |
| `System OMEGA/.../Product Creation Lab/` | 10 | **2.453 righe** | ✅ Aperta |
| `System OMEGA/Attività temporanea/Processo lanci - CONTESTO.md` | 1 | **172 righe** | ✅ Letta integralmente |
| `Info-Business-HQ_Knowledge/Priorità 1/` | 5 | 32 righe + **40 pag PDF** | ✅ Aperta |
| `Lancio corso skill beast/` | 798 | **12 pag PDF** + codebase | ✅ Aperta |
| `Lanco ebook/` | 2 | **353 righe** | ✅ Aperta |
| `Info-Business-HQ_Knowledge/Priorità 2/` | 9 PDF | — | ✅ Valutata → **non è di 14-LANCI** (§12) |
| `Formazzione/` (extra) | 3 | 36 righe | ✅ Valutata → **code di ingestione** (§12) |

**Totale letto: ~26.300 righe + ~52 pagine PDF.**

---

## 1. LA SCOPERTA — il file che l'audit non aveva visto

**`System OMEGA - Creazione proggetti e skill per Claude/Attività temporanea/Processo lanci - CONTESTO.md`** — 172 righe.

La task diceva che la sostanza buona era *"la catena FASE 0→3 (Strategy Command Center →
Infobusiness HQ → Marketing University → Product Creation Lab)"*.

**Il file contiene FASE 0→10.** Non quattro fasi: **undici**, fino al post-lancio e
all'evergreen. Non è citato in nessun punto della task, e non è in nessuna delle cartelle
elencate come materiale da assorbire.

**È lo scheletro end-to-end che L4 deve produrre, già scritto.**

| Fase | Titolo | Progetto storico | Reparto di destinazione (L3) |
|---|---|---|---|
| **0** | Decisione strategica | P9 Strategy Command Center | **Strategia** |
| **1** | Validazione idea | P7 Infobusiness HQ | **Prodotto** |
| **2** | Ricerca target | P6 Marketing University | **Intelligence & Competitor** |
| **3** | Creazione prodotto | P8 Product Creation Lab | **Prodotto** |
| **4** | Pricing | *(skill mancante — §2)* | **Pricing & Offerta** |
| **5** | Architettura funnel | *(skill mancante — §2)* | **Siti & Funnel** |
| **6** | Copy funnel | P1 Agency Operations | **Copy** |
| **7** | Sequenze email | P1 Agency Operations | **Copy** |
| **8** | Contenuto pre-lancio | P2 YouTube Lead Engine | **Marketing & Traffico** |
| **9** | Esecuzione lancio | P4 Launch Command | **Esecuzione Lancio** |
| **10** | Post-lancio & evergreen | P7 + P9 | **Strategia** + **Prodotto** |

**Le fasi 6, 7 e 8 girano IN PARALLELO** — il file lo chiama *"Sprint produzione"*. È un
vincolo di orchestrazione, non un dettaglio: tre reparti che lavorano insieme con un solo
punto di sincronizzazione.

**Conseguenza per L3:** gli otto reparti nominati nella task **coprono tutte e undici le
fasi**. Nessun reparto va aggiunto, nessuno va tolto. La mappa qui sopra è la prova.

---

## 2. Le tre skill che NON esistono — dichiarato, non aggirato

La task elenca fra le fonti da assorbire:

```
System OMEGA/.../CONTESTO - SOLO ESEMPI/Product Pricing Strategist.skill
System OMEGA/.../CONTESTO - SOLO ESEMPI/VSL Script Builder.skill
System OMEGA/.../CONTESTO - SOLO ESEMPI/Webinar Script Master.skill
```

**Nessuna delle tre esiste.** Prova:

```bash
$ find . -iname "*.skill*" -not -path "./node_modules/*"
       # nessun risultato in tutto il repo
$ find . -iname "*Pricing Strategist*" -o -iname "*VSL Script*" -o -iname "*Webinar Script*"
       # nessun risultato
```

`CONTESTO - SOLO ESEMPI/` contiene **57 file** in cinque sottocartelle. Nessun `.skill`.

Sono citate dal `Processo lanci` come skill delle FASE 4, 5 e 6 — quindi sono esistite o sono
state progettate e mai scritte. **Il contenuto non è recuperabile da qui.**

**Destino:** le tre capacità restano nel piano perché il flusso le richiede, ma **vanno
riscritte da zero in L5**, non assorbite. Va detto a Max: tre voci della sua lista fonti sono
vuote.

⚠️ **Attenuante importante trovata dopo:** per **Webinar Script Master** la sostanza c'è
comunque, nei PDF `WEBINAR_EVENTO` (§9). Per **Product Pricing Strategist** c'è il
`PRODUCT_LADDER.md` (§4.3). Solo **VSL Script Builder** resta senza nessuna fonte.

---

## 3. I duplicati — tre coppie verificate

| A | B | Esito |
|---|---|---|
| `InfoBusiness/` (5 file) | `Info-Business-HQ_Knowledge/Priorità 1/` | **Identici** (md5 uguale sui file testati) |
| `Formazzione/` (23 file) | `Info-Business-HQ_Knowledge/Priorità 2/` | **Stessi PDF**, `Formazzione/` è il superset |
| `Product Creation Lab/` | `Product Creation Lab - Copia/` | **Identiche** (`diff -rq` → nessuna differenza) |

**Destino:** si assorbe **una sola** copia per coppia. Fonte canonica:
`Progetti Claude/Info-Business-HQ_Knowledge/` e `Product Creation Lab/` (senza " - Copia").
Le altre **non si cancellano** — vale *niente si scarta* — ma nel piano non compaiono due volte.

---

## 4. STRATEGY COMMAND CENTER → reparto **Strategia**

`System OMEGA/.../Project-Strategy Command Center/KNOWLEDGE/` — **13 file, 8.968 righe.**

### 4.1 `FILTRO_ANTI_ADD.md` (785 righe) — il gate di ingresso di 14-LANCI

Il filtro a **5 domande sequenziali**: se un'idea non supera una domanda, **si ferma lì** e non
passa alla successiva.

| # | Domanda | Esito se NO |
|---|---|---|
| **D1** | L'idea è **direttamente** collegata a uno dei 3 pillar (Agenzia CRO, Info-Business, YouTube)? | Indiretta → BACKLOG (3 mesi) · Non collegata → SCARTA |
| **D2** | I 3 pillar sono **tutti 🟢**? | Uno 🟡 → FERMA, stabilizza prima · Uno 🔴 → **FERMA ASSOLUTAMENTE** |
| **D3** | L'idea muove **direttamente** un Key Result del trimestre? | BACKLOG fino al prossimo ciclo OKR |
| **D4** | C'è capacità **senza togliere** ai pillar? (Agenzia 50-60%, Info-Biz 20-30%, YT 15-20%) | Serve rispondere a *"da dove prendo queste ore?"* |
| **D5** | **Test della scomparsa**: se sparisse domani, il business ne soffrirebbe **concretamente**? | NO → **DISTRAZIONE**, scarta o backlog lungo |

**D5 è la più tagliente** e va citata per intero nel piano, perché è quella che smaschera i
lanci fatti per noia: *"Immagina di essere 6 mesi nel futuro. Hai fatto tutto il resto ma NON
questa cosa. Come stai? Se la risposta è 'uguale o meglio' → non è una priorità."*
Chiude con: *"Non tutto ciò che è interessante è importante."*

**Eccezione unica codificata:** se l'idea *risolve* il pillar in crisi, non è una nuova idea ma
un intervento correttivo → il filtro non si applica.

**→ Destinazione: reparto Strategia, come GATE BLOCCANTE di ingresso.** Nessun lancio entra in
14-LANCI senza passare le cinque domande. È il primo gate del flusso L4 e sostituisce il vago
"go/no-go strategico" con cinque domande a risposta binaria.

### 4.2 `SOGLIE_ALLARME.md` (870 righe) — 6 allarmi con soglie numeriche

| ID | Allarme | Soglia | Livello |
|---|---|---|---|
| **ALM-1** | Revenue agenzia in calo | 2 mesi consecutivi | 🔴 Critico |
| **ALM-2** | Zero vendite info-business | 30+ giorni | 🔴 Critico |
| **ALM-3** | Zero video YouTube | 3+ settimane | 🔴 Critico |
| **ALM-4** | Zero azioni cross-pillar | 30+ giorni | 🔴 Critico |
| **ALM-5** | OKR trimestrale a metà Q | <30% | 🟡 Attenzione |
| **ALM-6** | Tempo su progetti satellite | >10% per 2+ settimane | 🟡 Attenzione |

Precedenza già codificata: 🔴 ha priorità **assoluta**; 🟡 va gestito **entro 7 giorni**.

Soglie diagnostiche di funnel, valide durante un lancio:
opt-in **<20% = problema serio** · open rate **<20% = subject line** ·
click rate **<1% = contenuto email**.

**→ Destinazione: Strategia** (ALM-1…6, alimentano D2) + **Esecuzione Lancio** (soglie funnel).

### 4.3 `PRODUCT_LADDER.md` (577 righe) — 5 livelli di prezzo

| Livello | Fascia | Cosa | Nota operativa |
|---|---|---|---|
| **0** | €0 | Lead magnet | — |
| **1** | €7-47 | Mini-corsi | €7-17 "impulse buy" · €27-37 "no-brainer" · €47 limite entry |
| **2** | €97-297 | Corsi completi | €97 singolo topic · €147-197 con template e bonus · €297 premium |
| **3** | €497-997 | Percorsi trasformativi | €497 senza coaching · €697 gruppo · €997 all-inclusive |
| **4** | €2.000+ | Agenzia CRO high-ticket | — |

**Regola non negoziabile:** *"non saltare da €27 a €2.000 senza passaggi"*.

Contiene 5 percorsi di scala con revenue calcolata, fra cui il ponte **KDP → info-business**:
`Libro KDP €9.99 → link nel libro → PDF gratuito → €27-197`.

**→ Destinazione: Pricing & Offerta** (le fasce) + **Strategia** (la scala).
**È anche la fonte sostitutiva della `Product Pricing Strategist.skill` che non esiste.**
Il percorso KDP collega 14-LANCI al workflow libri già operativo.

### 4.4 Il resto dello Strategy Command Center

| File | Righe | → Reparto |
|---|---:|---|
| `WORKFLOW_CADENZE.md` | 1.038 | **Esecuzione Lancio** — cadenze e ritmo |
| `CROSS_POLLINATION_ENGINE.md` | 1.032 | **Strategia** — FASE 10, casi studio → YouTube, studenti → agenzia |
| `OKR_SYSTEM.md` | 922 | **Strategia** — alimenta D3 |
| `DECISION_FRAMEWORK.md` | 779 | **Strategia** — KEEP/UPDATE/RELAUNCH/RETIRE della FASE 10 |
| `OUTPUT_TEMPLATES.md` | 744 | **tutti** — formati di consegna standard |
| `DASHBOARD_ENGINE.md` | 675 | **Strategia** — stato 🟢🟡🔴 che D2 legge |
| `RETROSPETTIVA_ENGINE.md` | 503 | **Esecuzione Lancio** — debrief post-lancio |
| `REVENUE_TRACKER.md` | 487 | **Strategia** — revenue per pillar |
| `GERARCHIA_PILLAR.md` | 390 | **Strategia** — i 3 pillar, letti da D1 |
| `PROJECT_MAP.md` | 166 | — navigazione, non si assorbe |

---

## 5. PRODUCT CREATION LAB → reparto **Prodotto**

`System OMEGA/.../Product Creation Lab/KNOWLEDGE_BASE/` — **8 file KB, 2.453 righe.**

### 5.1 `KB_01_PRODUCT_PIPELINE.md` (401) — l'input obbligatorio

Il brief che entra in produzione **deve** contenere:

- Idea con **score ≥60/100**
- Validazione MVP: **almeno 5 persone** hanno detto "sì, lo comprerei"
- Target definito — *non "chiunque voglia imparare X"*
- Formato scelto (PDF / Ebook / Mini-corso / Corso / Percorso)
- Fascia prezzo ipotizzata

**→ Destinazione: reparto Prodotto, gate di ingresso.** È l'equivalente per i lanci del
`KDP-GATE` che nel workflow libri blocca prima che qualcuno esegua.

### 5.2 `KB_02_RICERCA_PRE_PRODUZIONE.md` (306) — la ricerca che blocca

**Regola testuale:** *"Non si procede al Step 1.2 senza aver completato questo step."*

- **≥15 frasi esatte** del target, **con URL della fonte**
- **≥5 pain point** distinti
- **≥3 competitor** analizzati (review negative 1-2 stelle su Amazon/Udemy)
- **≥3 gap** non coperti dai competitor
- Saper rispondere a *"perché il nostro prodotto è chiaramente migliore/diverso?"*

**→ Destinazione: Intelligence & Competitor.** Copre la FASE 2 del `Processo lanci`
(pain point map I×F×A, obiezioni top 10 F×I, TOV 20-30 frasi).

### 5.3 `KB_03_LEARNING_PATH_ENGINE.md` (410)

PRIMA→DOPO, **massimo 7 moduli, ideale 5**, **1 modulo = 1 trasformazione**, ogni modulo
produce un output pratico. **Regola:** se non sai formulare *"Da [prima] a [dopo]"* per un
modulo, quel modulo non è pronto. **→ Prodotto.**

### 5.4 `KB_05_QUALITY_SYSTEM.md` (255) — i 6 red flag assoluti

> *"Se anche UNO SOLO è presente → NON consegnare. Fix obbligatorio."*

| # | Red flag | Perché blocca |
|---|---|---|
| 1 | Lezione senza output pratico | Nessun risultato → refund garantito |
| 2 | Template senza esempio compilato | Lo studente non sa compilarlo → abbandona |
| 3 | Concetto chiave non spiegato | La base del modulo manca |
| 4 | Audio/video incomprensibile | Completion rate → 0 |
| 5 | Link o file non funzionante | Frustrazione immediata |
| 6 | Salto logico tra moduli | Lo studente si perde |

Ogni red flag ha **il suo test di verifica** già scritto (es. #5: *"testa ogni link in modalità
incognito, come lo studente non loggato come te"*).

**Beta test obbligatorio per ogni prodotto ≥€97.** Uscita: *"correggi i problemi segnalati da
2+ beta tester"*, *"tutti i red flag eliminati → prodotto approvato"*.

**→ Destinazione: Prodotto, GATE BLOCCANTE di uscita.** Sei controlli binari con il proprio
test: è la forma giusta di gate, la stessa di `KDP-GATE`.

### 5.5 `KB_08_METRICHE_KPI.md` (268) — soglie post-vendita

| Metrica | Target | Soglia critica |
|---|---|---|
| Refund rate | **<5%** | **>10%** |
| Completion rate | **>40%** | **<20%** |
| Testimonial entro 30gg | **≥3** | 0 dopo 30gg |
| Prodotti in pipeline | **≥2 sempre** | — |
| Ricerca completata prima di iniziare | **100%** | *"Nessuna eccezione — processo rotto"* |
| Beta test per ≥€97 | **100%** | — |

**→ Prodotto** (qualità) + **Esecuzione Lancio** (FASE 10, il debrief legge queste soglie).

### 5.6 Il resto

| File | Righe | → Reparto |
|---|---:|---|
| `KB_04_PRODUZIONE_CONTENUTI.md` | 322 | **Prodotto** |
| `KB_06_PACKAGING_HANDOFF.md` | 278 | **Prodotto** → handoff verso Esecuzione Lancio |
| `KB_07_STANDARD_PER_TIPO.md` | 213 | **Prodotto** — standard per PDF/ebook/corso/percorso |

---

## 6. YOUTUBE LEAD ENGINE → **Siti & Funnel** + **Copy** + **Marketing & Traffico**

`System OMEGA/.../YouTube Lead Engine/KNOWLEDGE_BASE/` — **7 file, 2.860 righe.**
**Non è nella lista fonti della task** — trovato in ricognizione, ed è materiale di lancio a
tutti gli effetti.

### 6.1 `KB_04_funnel-unico-perfetto.md` (359) — la struttura, non il PDF

Esiste anche come `Funnel Unico Perfetto ... .pdf` in `Priorità 1/`, ma **questo è il .md già
strutturato**: si assorbe questo, il PDF resta come sorgente originale.

Struttura: `Video YouTube → Bridge page (nome+email, 3 tag) → redirect → Upsell €15 (VSL 3-5
min) → Sequenza email 3 giorni → VSL evento → Webinar → Follow-up 5 giorni`, con nurture
settimanale per chi non avanza.

**Benchmark target, numerici:**

| Step | Metrica | 🟢 Verde | 🟡 Giallo |
|---|---|---|---|
| Bridge page | Opt-in rate | **>35%** | 20-35% |
| Upsell €15 | Conversion | **>15%** | 8-15% |
| VSL evento | Iscrizione webinar | **>20%** | 10-20% |
| Webinar | Show rate | **>30%** | 20-30% |
| Webinar | Conversion rate | **>5%** | 2-5% |
| Follow-up | Recupero post-webinar | **>15%** | 8-15% |

Tre avvertenze operative già scritte, da portare nel piano:
- **Mai mischiare traffico**: bridge page YouTube separata da quella paid, altrimenti il
  confronto organico vs paid non è misurabile.
- **L'upsell €15 non è opzionale**: è il finanziamento del funnel — anche al 10% genera €1,50
  per opt-in e abbassa il CAC.
- **Il nurture non si interrompe**: un lead a 6 mesi converte al lancio successivo; cambia la
  frequenza, non la lista.

**→ Siti & Funnel** (struttura, tag, routing) + **Esecuzione Lancio** (benchmark → soglie del
tracking giornaliero).

> **Nota per L3.** La task chiede *"come si verifica che le pagine siano online e funzionanti —
> non 'fatte', online e funzionanti"*. Questi sei benchmark sono la risposta: una pagina è
> verificata quando **misura**, non quando esiste.

### 6.2 `KB_07_app-soc-framework.md` (379) — APP-SOC

**A**ttention (aggancio) · **P**roblem (amplificazione) · **P**romise (trasformazione) ·
**S**olution (meccanismo unico) · **O**ffer (dettaglio) · **C**lose (chiusura con Reason Now).

Ogni lettera ha la sua sezione, più tre declinazioni: lead magnet (brevissimo), VSL upsell €15
(3-5 min), email Day 4 (case study).

**→ Copy.** ⚠️ **Da riconciliare con lo standard APSOC dell'Impero**, di cui il CMO è owner e su
cui vigila `guild-copy-apsoc`: qui è **APP-SOC** (due P). O sono lo stesso framework con due
nomi, o sono due — e in quel caso uno solo può essere lo standard. **Va risolto prima di L5.**

### 6.3 Il resto

| File | Righe | → Reparto |
|---|---:|---|
| `KB_08_email-sequence-master.md` | 522 | **Copy** — FASE 7, le 4 sequenze |
| `KB_10_analytics-dashboard-template.md` | 460 | **Esecuzione Lancio** — report giornaliero |
| `KB_09_storytelling-guide.md` | 455 | **Copy** |
| `KB_06_brand-voice.md` | 345 | **Copy** — da riconciliare con la brand voice del CMO |
| `KB_05_youtube-lead-engine-brief.md` | 340 | **Marketing & Traffico** — FASE 8 |

---

## 7. MARKETING UNIVERSITY → reparto **Intelligence & Competitor**

`System OMEGA/.../Project-Marketing University.md/` — **16 file, 11.853 righe.**
**È la fonte più grande di tutto il materiale storico.** Copre la FASE 2 del `Processo lanci`.

Non è un archivio di contenuti: è **una macchina per estrarre e catalogare framework** da
qualunque materiale formativo.

| File | Righe | Cosa contiene | → Destinazione |
|---|---:|---|---|
| `KB_14_PRELOADED_FRAMEWORKS.md` | 1.146 | Framework già caricati, pronti | **Intelligence & Competitor** + **Copy** |
| `KB_11_SYSTEM_RULES_AND_EDGE_CASES.md` | 929 | Regole di sistema e casi limite | **Intelligence & Competitor** |
| `KB_06_RESPONSE_TEMPLATES.md` | 909 | Template di risposta strutturata | **tutti** |
| `KB_04_STUDY_METHOD_PIPELINE.md` | 893 | Pipeline del metodo di studio | **Intelligence & Competitor** |
| `KB_08_FRAMEWORKS_REGISTRY.md` | 871 | **Registro centralizzato dei framework** | **Intelligence & Competitor** |
| `KB_10_QUALITY_VALIDATION.md` | 802 | Validazione qualità dell'estrazione | **gate** del reparto |
| `KB_09_STUDY_PRIORITY_ENGINE.md` | 802 | Priorità di studio | **Intelligence & Competitor** |
| `KB_02_EXTRACTION_ENGINE.md` | 770 | Motore di estrazione dei framework | **Intelligence & Competitor** |
| `KB_05_WEEKLY_MONTHLY_ROUTINE.md` | 757 | Routine settimanale/mensile | **Strategia** — cadenze |
| `KB_12_SETUP_AND_ONBOARDING.md` | 754 | Setup e onboarding | — non si assorbe |
| `KB_01_LIBRARY_ARCHITECTURE.md` | 740 | Architettura della libreria | **Intelligence & Competitor** |
| `CUSTOM_INSTRUCTIONS.md` | 698 | Istruzioni operative del progetto | **Intelligence & Competitor** |
| `KB_07_QUICK_REFERENCE_PROTOCOL.md` | 674 | Protocollo di consultazione rapida | **tutti** |
| `s KB_03_PROJECT_CONNECTION_MATRIX.md` | 603 | Matrice di collegamento fra progetti | **Strategia** |
| `KB_13_DOMAIN_GLOSSARY.md` | 319 | Glossario di dominio | **tutti** |
| `KNOWLEDGE/PROJECT_MAP.md` | 186 | Navigazione | — non si assorbe |

### 7.1 Il pezzo che vale di più: `KB_08_FRAMEWORKS_REGISTRY.md`

Non è una lista: è **uno schema dati**. Ogni framework estratto genera un record con campi
tipizzati (`nome`, `num_step`, `derivato`, `contraddizioni`…), un **ID stabile** con
convenzione di naming (`A1_A_01_250615` = Area 1, Sottoarea A, primo framework, data), e
quattro regole di integrità già scritte:

1. Un ID non viene **mai** riassegnato, anche se il framework è scartato.
2. Un framework aggiornato **mantiene** lo stesso ID.
3. La **deduplicazione** è un passo esplicito del workflow (W1 Step 8).
4. Esiste il campo `contraddizioni`: un framework può **dichiarare** quali altri contraddice.

**→ Destinazione: Intelligence & Competitor, come schema di stato del reparto.**

Questo risolve un problema che il reparto Lanci di oggi non ha nemmeno posto: **dove finisce
ciò che si impara studiando i competitor**. Oggi finisce in un PDF. Con questo schema finisce
in un registro interrogabile, deduplicato, con le contraddizioni esplicite.

⚠️ **Collegamento da fare in L3:** questo registro **si sovrappone** all'agente
`conoscenza-empire`, che è il fornitore unico di conoscenza dell'Impero. O il registro diventa
il formato dati di `conoscenza-empire` per l'area lanci, o si duplicano due biblioteche.
**Decisione da mettere nell'ADR di L6.**

---

## 8. ⚠️ LA SCOPERTA PIÙ IMPORTANTE — il lancio esiste già, tranne il lancio

Fonte: `Info-Business-HQ_Knowledge/Priorità 1/CATALOGO PRODOTTI ATTUALE — Info-Bu.md`
(32 righe, ultimo aggiornamento **07/03/2026**).

### 8.1 Cosa dice il catalogo, testualmente

**Prodotto attivo — "Manuale Claude Code - Da zero a Senior"**

| Campo | Valore nel file |
|---|---|
| Status | **"Pronto"** |
| Tipo | Ebook Premium |
| Formato | **203 pagine** |
| Prezzo | **"€ NON LO SO"** |
| Data lancio | **"Presto spero"** |
| Metriche | **0** |
| Lead magnet collegato | Community WhatsApp *(da fare)* |
| Funnel tipo | Social → community → sales page → acquisto |

**Prodotto in idea** — *"Vendi la Skill n.1: Crea e vendi Agenti AI"*, corso video.
Nota nel file: *"ho un forte lead magnet: Ebook Manuale Claude Code GRATUITO"*.

**Gap dichiarato dal file stesso:** *"DEVE ANCORA ESSERE TUTTO MIGLIORATO TUTTO."*

### 8.2 Cosa ho trovato attorno a quel prodotto, altrove

Incrociando le altre fonti, per questo singolo lancio **esiste già quasi tutto**:

| Pezzo del lancio | Esiste? | Dove |
|---|---|---|
| **Prodotto** | ✅ 203 pagine, "Pronto" da marzo | catalogo |
| **Lead magnet** | ✅ **Framework I.C.R.O.**, 12 pagine finite | `Lancio corso skill beast/Framework_ICRO_Digital_Empire.pdf` |
| **Landing page** | ✅ costruita, 299 righe | `Lanco ebook/Sito- Leanding page/index.html` |
| **Design system della landing** | ✅ 54 righe di regole inviolabili | `Lanco ebook/Sito- Leanding page/Gemini.md` |
| **Libreria componenti** | ✅ Next.js, ~30 sezioni | `Lancio corso skill beast/Leanding Page CCM/` |
| **Struttura funnel** | ✅ | `KB_04_funnel-unico-perfetto.md` |
| **Framework copy** | ✅ | `KB_07_app-soc-framework.md` |
| **Script webinar** | ✅ | `WEBINAR_EVENTO.pdf` (§9) |
| **Sequenze email** | ✅ | `KB_08_email-sequence-master.md` |
| **Prezzo** | ❌ | *"NON LO SO"* |
| **Data** | ❌ | *"Presto spero"* |
| **Lancio** | ❌ | **mai avvenuto** |

### 8.3 Perché questo cambia il piano

**È la stessa malattia di FIX-1 nel workflow libri:** quattro libri scritti, zero pubblicati.
Qui: un ebook da 203 pagine pronto **da marzo**, con lead magnet, landing e funnel già fatti —
e **zero euro**, perché nessuno ha deciso un prezzo e una data.

Il reparto Lanci di oggi non ha un buco di *capacità*. Ha un buco di **decisione e esecuzione**,
e la prova non è teorica: è un prodotto fermo da sei mesi con tutto il resto pronto attorno.

**→ Conseguenza per L3/L4, da mettere nel piano:**

1. **Il primo cliente di 14-LANCI è il Manuale Claude Code.** Non un lancio ipotetico: quello.
   Il flusso di L4 va progettato in modo che *questo* lancio ci passi dentro per primo.
2. **Il flusso deve produrre due output obbligatori prima di qualunque altra cosa: un PREZZO e
   una DATA.** Sono i due campi che mancano, e sono esattamente i due che nessun documento
   attuale obbliga a compilare.
3. Il ponte con `ultimo-metro` (la skill che trova il lavoro finito e mai uscito) va dichiarato
   in L5: 14-LANCI è il reparto che *chiude* quello che `ultimo-metro` *trova*.

---

## 9. WEBINAR MILIONARIO → **Copy** + **Esecuzione Lancio**

`Info-Business-HQ_Knowledge/Priorità 1/Webinar/` — **3 PDF, ~40 pagine, ~58.000 caratteri.**

Il `Processo lanci` FASE 6 cita *"framework Webinar Milionario System"* come skill richiesta.
**La fonte è qui**, ed è integra:

| File | Pagine | Cosa contiene |
|---|---:|---|
| `WEBINAR_EVENTO.pdf` | 14 | **Script completo del framework**, versione generica |
| `WEBINAR_EVENTO (1).pdf` | 24 | **Versione applicata** — "Pagine Tema Instagram + AI" |
| `WEBINAR – Esempio di apertura con storytelling (prima parte).pdf` | 2 | Script dei primi 10-15 minuti |

### 9.1 La struttura del framework, estratta

Il metodo parte da **una sola domanda**, ed è la stessa in entrambe le versioni:

> *"Qual è la grande promessa che voglio fargli credere? Cioè: qual è quell'unica idea che, se
> il pubblico la percepisce come raggiungibile e reale, rende tutte le altre obiezioni quasi
> irrilevanti."*

Da quella promessa discendono, in cascata: **il titolo** → **l'apertura** → **il filo
conduttore dei 3 "segreti"** → **il pitch finale del percorso**. Non sono quattro pezzi
separati: sono quattro derivazioni della stessa frase.

L'esempio dell'apertura con storytelling è un modello di struttura riutilizzabile: caso reale
di una persona → la domanda scomoda (*"se da domani non potessi più lavorarci, quanto andrebbe
avanti da solo?"*) → la verità che riformula il problema (*"finché dipende da te non hai un
business, hai un hobby faticoso"*).

**→ Destinazione: Copy** (il framework e gli script) + **Esecuzione Lancio** (il webinar è il
Giorno W del calendario T-30→T+7).
**È la fonte sostitutiva della `Webinar Script Master.skill` che non esiste** (§2).

---

## 10. FRAMEWORK I.C.R.O. → **Prodotto** + **Marketing & Traffico**

`Lancio corso skill beast/Framework_ICRO_Digital_Empire.pdf` — **12 pagine.**

**È un lead magnet finito e pubblicabile**, non materiale grezzo. Si autodefinisce
*"Companion gratuito di Cloud Code Mastery"*: `12 pagine · 1 framework · 1 template pronto ·
10 minuti`.

Il framework **I.C.R.O.** — quattro sezioni di un `CLAUDE.md` ben scritto:

| | Sezione | Domanda a cui risponde |
|---|---|---|
| **I** | Identità | Chi è Claude Code per questo progetto? Quale ruolo, quale expertise? |
| **C** | Contesto | Cosa sa del business? Settore, target, prodotto, situazione? |
| **R** | Regole | Come si comporta? Che tono? Cosa evita? Quali vincoli? |
| **O** | Output | Cosa produce? In che formato, con che struttura, quanto lungo? |

Principio chiave testuale: *"Un CLAUDE.md di 30 righe ben strutturato con I.C.R.O. batte un
prompt di 500 parole — ogni singola volta. Perché il prompt scompare. Il CLAUDE.md resta."*

Contiene anche una tabella **APPROCCIO CHATBOT vs APPROCCIO SISTEMA** e un confronto
PRIMA/DOPO con esempio reale — cioè la struttura di argomentazione già pronta per il copy.

**→ Destinazione: Marketing & Traffico** (è il lead magnet della FASE 8 del lancio Manuale
Claude Code) + **Prodotto** (è anche un pezzo di prodotto).

> ⚠️ **Nota di coerenza interna.** Il PDF insegna a scrivere un `CLAUDE.md` con I.C.R.O.
> Il `CLAUDE.md` di questo monorepo **non segue I.C.R.O.** Non è un difetto da correggere qui,
> ma è un dato: vendiamo un metodo che in casa non applichiamo con quel nome. Da segnalare al
> reparto Prodotto prima di rimettere in vendita il lead magnet.

---

## 11. GLI ASSET DI CODICE → reparto **Siti & Funnel**

### 11.1 `Lanco ebook/Sito- Leanding page/` — la landing di lancio già costruita

| File | Righe | Cosa |
|---|---:|---|
| `index.html` | 299 | **Landing page costruita** per l'ebook "Claude Code - La Skill del Futuro" |
| `Gemini.md` | 54 | **Il design system che l'ha generata**, come regole inviolabili |

`Gemini.md` non è un appunto: è una **specifica di design completa e riutilizzabile**, con
palette (`#050505` sfondo, accento Claude Coral `#FF5A26` *"solo per micro-accenti, mai come
fondo pieno"*), tipografia (Inter, heading con `tracking-tighter` e `leading-none`, body min
18px), effetti (ambient glow con `blur(80px)`, ombre multi-layer, backdrop blur), spaziatura
(*"whitespace is luxury"*, `py-32`/`py-40`), e **le 7 sezioni obbligatorie della pagina** —
hero, social proof, problema/agitazione, bento grid dei moduli, sneak peek terminale, pricing,
footer.

**→ Destinazione: Siti & Funnel, come template di sales page per info-prodotti.**
⚠️ **Da riconciliare con `empire-premium-style`**, la skill di stile già installata: sono due
sistemi visivi che descrivono lo stesso tipo di pagina. In L5 uno dei due è lo standard.

### 11.2 `Lancio corso skill beast/Leanding Page CCM/` — la libreria componenti

**798 file**, progetto Next.js con `AGENTS.md`, `CLAUDE.md`, `package.json`, `src/`, `public/`.
La cartella `components/home/` contiene ~30 sezioni già scritte e riutilizzabili:

`Hero` · `ObjectionFlow` · `ObjectionCPB` (+ 4 varianti: Checkout, Time, Website, WordOfMouth)
· `FunnelComparison` · `ScientificProofs` · `Philosophy` · `HowWeWork` · `Services` ·
`SocialFunnelSection` · `CroFunnelSection` · `AutomationSection` · `WhyUs` · `Trust` ·
`TeamDashboard` · `Newsletter` · `Contact` · `WebDesignShowcase` · `HopeSection` …

**Il gruppo `ObjectionCPB_*` è il pezzo più prezioso:** quattro componenti che gestiscono
quattro obiezioni distinte. È la gestione obiezioni della FASE 2 **già in codice**, non in un
documento.

**→ Destinazione: Siti & Funnel, come libreria componenti dell'ecosistema.**
Non si riscrive (ADR-003): si avvolge e si indicizza.

---

## 12. Cosa NON si assorbe — dichiarato con la ragione

Il gate pretende zero righe sospese. Queste fonti sono state aperte e **scartate da 14-LANCI
con motivazione**, non lasciate a metà.

| Fonte | Contenuto reale | Perché non è di 14-LANCI | Dove va |
|---|---|---|---|
| `Info-Business-HQ_Knowledge/Priorità 2/` (9 PDF) | Agency Scalping, SMMA da zero, Funnel di acquisizione clienti, Guida freelancing, 4 file Outreach (Framework, Loom, strategie) | È materiale di **acquisizione clienti per l'agenzia**, non di lancio prodotto. Confonderli significa rifare in 14-LANCI ciò che 01-AGENCY già fa | **01-AGENCY** (ecosistema esistente) |
| `Formazzione/Youtube/Rebdere YOUTUBE un Lead magnet.txt` | **7 URL YouTube**, nessun testo | Non è conoscenza: è una **coda di ingestione** | **Empire Studio** (pipeline di studio video) |
| `Formazzione/Storytelling/storytelling formazione.txt` | **9 URL YouTube**, nessun testo | Idem | **Empire Studio** |
| `Formazzione/Claude code/` (2 file) | Manuale Claude Code per il business + Engineering Blueprint | È **il prodotto stesso**, non materiale sul come lanciarlo | **Prodotto** (§8) |
| `Product Creation Lab - Copia/`, `InfoBusiness/` | Duplicati verificati | §3 | — |
| `PROJECT_MAP.md` (×3) | Navigazione interna dei progetti vecchi | La navigazione del nuovo ecosistema è diversa | — |

> Sui due `.txt` di link: **non sono da buttare**, sono da *processare*. Ma il processore è
> Empire Studio, non 14-LANCI. Metterli nel piano dei lanci significherebbe fingere di aver
> assorbito 16 video che nessuno ha guardato.

---

## 13. Bilancio dell'assorbimento

| | Valore |
|---|---|
| Fonti aperte | **10 su 10** |
| Righe di conoscenza lette | **~26.300** |
| Pagine PDF estratte | **~52** |
| Framework concreti mappati a un reparto | **58** |
| Gate bloccanti individuati | **4** (filtro anti-ADD, brief ≥60/100 + MVP 5 persone, 6 red flag, quality validation MU) |
| Soglie numeriche recuperate | **26** (6 allarmi, 6 benchmark funnel, 6 KPI prodotto, 3 soglie funnel, 5 fasce prezzo) |
| Duplicati verificati e neutralizzati | **3 coppie** |
| Fonti dichiarate vuote | **1** (`VSL Script Builder.skill` — le altre 2 hanno una fonte sostitutiva) |
| Fonti scartate con motivazione | **6** (§12) |
| Scoperte fuori dalla lista della task | **4** (`Processo lanci` FASE 0→10, YouTube Lead Engine, Framework I.C.R.O., catalogo prodotti) |

---

## 14. Cosa passa a L3 — le sette conclusioni

1. **Gli 8 reparti della task coprono le 11 fasi.** La mappa §1 lo dimostra. Non aggiungere
   reparti in L3, non toglierne.
2. **Quattro gate bloccanti esistono già scritti** e vanno messi in fila: filtro anti-ADD a 5
   domande (Strategia) → brief ≥60/100 + MVP 5 persone (Prodotto) → 6 red flag in uscita
   (Prodotto) → quality validation dell'estrazione (Intelligence). Nessuno va inventato.
3. **Le FASI 6-7-8 girano in parallelo.** L4 deve avere un punto di sincronizzazione, non una
   sequenza lineare.
4. **Le soglie numeriche ci sono tutte.** Un lancio è misurabile dal primo giorno: opt-in >35%,
   upsell >15%, show rate >30%, CR webinar >5%. L4 non deve inventare KPI.
5. **Il primo lancio non è ipotetico.** Il Manuale Claude Code è pronto da marzo con lead
   magnet, landing e funnel già fatti, e manca solo **prezzo + data**. Il flusso di L4 va
   progettato attorno a questo caso, e deve **obbligare** a produrre quei due campi (§8).
6. **Tre conflitti da risolvere prima di L5**, tutti già nominati:
   **APP-SOC vs APSOC** (§6.2) · **`Gemini.md` vs `empire-premium-style`** (§11.1) ·
   **Framework Registry vs `conoscenza-empire`** (§7.1).
7. **Una sola skill va scritta davvero da zero:** `VSL Script Builder`. Pricing e Webinar hanno
   la fonte (§4.3, §9).

---

## Connessioni

- [[RICOGNIZIONE-LANCI]] — L1, chiusa (CP-20260902-009)
- [[26-ECOSISTEMA-LANCI]] — L3/L4/L5, prossimo passo
- `company/Memory/tasks/TASK-GAEL-20260831-SETTIMANA-02.md` — la task madre
- `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/workflow/WF-LANCIO.md` — si avvolge (ADR-003)
- `.claude/skills/ultimo-metro/` — trova il lavoro finito e mai uscito; 14-LANCI lo chiude (§8.3)
- `.claude/agents/conoscenza-empire.md` — da riconciliare col Framework Registry (§7.1)
