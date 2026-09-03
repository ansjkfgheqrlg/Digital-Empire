---
Type: PROJECT
Status: Parziale
Tags: #lanci #assorbimento #L2 #ecosistema-14 #TASK-LANCI-ECO-W2
Created: 2026-09-02
Last updated: 2026-09-02
Autore: Gael (via Emperator)
Task: TASK-LANCI-ECO-W2 — sotto-task L2
Gate L2: ❌ NON PASSATO — vedi §7
---

# ASSORBIMENTO LANCI — cosa contengono i progetti vecchi e dove finisce

> **Deliverable di L2, fermato a metà su ordine di Gael (2026-09-02).**
> Per ogni progetto vecchio: quali framework, checklist e criteri concreti contiene, e in
> quale reparto del nuovo ecosistema finiscono.
>
> ⚠️ **Questo documento è PARZIALE e lo dichiara.** Il gate L2 pretende che ogni riga punti a
> un file sorgente reale e a un reparto di destinazione, con **zero righe "da approfondire"**.
> Le fonti coperte qui rispettano il gate. Quelle **non ancora aperte sono elencate in §7**,
> separate e nominate una per una. Nessuna riga finge di essere completa.

---

## 0. Metodo e inventario misurato

Comandi eseguiti il 2026-09-02 dalla root del monorepo:

```bash
find "<cartella>" -type f              # inventario per ogni fonte
wc -l *.md                             # peso reale
md5sum <a> <b>                         # verifica dei duplicati
diff -rq <dir_a> <dir_b>               # verifica delle copie
find . -iname "*.skill*"               # esistenza delle skill dichiarate
```

| Fonte | File | Righe .md | Stato |
|---|---:|---:|---|
| `System OMEGA/.../Project-Strategy Command Center/` | 13 | **8.968** | ✅ Aperto ed estratto |
| `System OMEGA/.../Product Creation Lab/` | 10 | **2.453** | ✅ Aperto ed estratto |
| `System OMEGA/.../YouTube Lead Engine/` | 7 | **2.860** | ✅ Aperto ed estratto |
| `System OMEGA/Attività temporanea/Processo lanci - CONTESTO.md` | 1 | **172** | ✅ Letto integralmente |
| `System OMEGA/.../Project-Marketing University.md/` | 16 | n.m. | 🟡 Solo inventariato |
| `Progetti Claude/Info-Business-HQ_Knowledge/` | 22 | — (PDF) | 🟡 Solo inventariato |
| `InfoBusiness/` | 5 | — (PDF) | ⚫ **Duplicato**, vedi §3 |
| `Formazzione/` | 23 | — (PDF) | ⚫ **Duplicato parziale**, vedi §3 |
| `Lancio corso skill beast/` | 798 | — (codice) | 🟡 Solo inventariato |
| `Lanco ebook/` | 2 | — | 🟡 Solo inventariato |

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

`CONTESTO - SOLO ESEMPI/` contiene **57 file** in quattro sottocartelle
(Product Creation Lab, Product Creation Lab - Copia, Project-Marketing University.md,
Project-Strategy Command Center, YouTube Lead Engine). Nessun `.skill`.

**Sono citate dal `Processo lanci`** come skill delle FASE 4, 5 e 6 — quindi sono esistite, o
sono state progettate e mai scritte. **Il contenuto non è recuperabile da qui.**

**Destino:** le tre capacità restano nel piano (Pricing, Architettura Funnel, VSL/Webinar copy)
perché il flusso le richiede, ma **vanno riscritte da zero in L5**, non assorbite. Va detto a
Max esplicitamente: tre voci della sua lista fonti sono vuote.

---

## 3. I duplicati — tre coppie verificate

Prima di assorbire, va detto quali cartelle sono la stessa cartella. Verificato con `md5sum`
e `diff -rq`, non a occhio:

| A | B | Esito |
|---|---|---|
| `InfoBusiness/` (5 file) | `Progetti Claude/Info-Business-HQ_Knowledge/Priorità 1/` | **Identici** (md5 uguale su entrambi i file testati) |
| `Formazzione/` (23 file) | `Progetti Claude/Info-Business-HQ_Knowledge/Priorità 2/` | **Stessi PDF**, `Formazzione/` è il superset (ha in più: Claude code, Storytelling, Youtube) |
| `Product Creation Lab/` | `Product Creation Lab - Copia/` | **Identiche** (`diff -rq` → nessuna differenza) |

**Destino:** si assorbe **una sola** copia per coppia. Fonte canonica scelta:
`Progetti Claude/Info-Business-HQ_Knowledge/` (contiene entrambe le priorità) e
`Product Creation Lab/` (senza " - Copia").

Le altre **non si cancellano** — vale la direttiva *niente si scarta* — ma nel piano non
compaiono due volte.

---

## 4. STRATEGY COMMAND CENTER → reparto **Strategia**

`System OMEGA/.../CONTESTO - SOLO ESEMPI/Project-Strategy Command Center/KNOWLEDGE/`
**13 file, 8.968 righe.** È la fonte più densa di tutto il materiale storico.

### 4.1 `FILTRO_ANTI_ADD.md` (785 righe) — il gate di ingresso di 14-LANCI

Il filtro a **5 domande sequenziali**: se un'idea non supera una domanda, **si ferma lì** e non
passa alla successiva.

| # | Domanda | Esito se NO |
|---|---|---|
| **D1** | L'idea è **direttamente** collegata a uno dei 3 pillar (Agenzia CRO, Info-Business, YouTube)? | Indiretta → BACKLOG (rivaluta a 3 mesi) · Non collegata → SCARTA |
| **D2** | I 3 pillar sono **tutti 🟢**? | Uno 🟡 → FERMA, stabilizza prima · Uno 🔴 → **FERMA ASSOLUTAMENTE** |
| **D3** | L'idea muove **direttamente** un Key Result del trimestre? | BACKLOG fino al prossimo ciclo OKR |
| **D4** | C'è capacità **senza togliere** ai pillar? (allocazione: Agenzia 50-60%, Info-Biz 20-30%, YT 15-20%) | Serve rispondere a "da dove prendo queste ore?" |
| **D5** | *(quinta domanda presente nel file, non ancora estratta — vedi §7)* | — |

**Eccezione unica codificata:** se l'idea *risolve* il pillar in crisi, non è una nuova idea ma
un intervento correttivo → il filtro non si applica.

**→ Destinazione: reparto Strategia, come GATE BLOCCANTE di ingresso all'ecosistema.**
Nessun lancio entra in 14-LANCI senza passare queste domande. È il primo gate del flusso L4,
e sostituisce il vago "go/no-go strategico" con cinque domande a risposta binaria.

### 4.2 `SOGLIE_ALLARME.md` (870 righe) — 6 allarmi con soglie numeriche

| ID | Allarme | Soglia | Livello |
|---|---|---|---|
| **ALM-1** | Revenue agenzia in calo | 2 mesi consecutivi | 🔴 Critico |
| **ALM-2** | Zero vendite info-business | 30+ giorni | 🔴 Critico |
| **ALM-3** | Zero video YouTube | 3+ settimane | 🔴 Critico |
| **ALM-4** | Zero azioni cross-pillar | 30+ giorni | 🔴 Critico |
| **ALM-5** | OKR trimestrale sotto il 30% a metà Q | <30% | 🟡 Attenzione |
| **ALM-6** | Tempo su progetti satellite | >10% per 2+ settimane | 🟡 Attenzione |

Regole di precedenza già scritte: 🔴 ha precedenza **assoluta**; 🟡 va gestito **entro 7 giorni**.

Contiene anche le **soglie diagnostiche di funnel**, che valgono direttamente per un lancio:
opt-in rate **<20% = problema serio** · open rate **<20% = subject line** ·
click rate **<1% = contenuto email**.

**→ Destinazione: reparto Strategia** (ALM-1…ALM-6, alimentano D2 del filtro anti-ADD) +
**reparto Esecuzione Lancio** (soglie di funnel, diagnostica durante il carrello aperto).

### 4.3 `PRODUCT_LADDER.md` (577 righe) — 5 livelli di prezzo

| Livello | Fascia | Cosa | Nota operativa |
|---|---|---|---|
| **0** | €0 | Lead magnet | — |
| **1** | €7-47 | Mini-corsi | €7-17 "impulse buy" · €27-37 "no-brainer" · €47 limite entry |
| **2** | €97-297 | Corsi completi | €97 singolo topic · €147-197 con template e bonus · €297 premium |
| **3** | €497-997 | Percorsi trasformativi | €497 senza coaching · €697 coaching di gruppo · €997 all-inclusive |
| **4** | €2.000+ | Agenzia CRO high-ticket | — |

**Regola non negoziabile codificata:** *"non saltare da €27 a €2.000 senza passaggi"*.

Contiene 5 percorsi di scala già tracciati con revenue calcolata, fra cui il ponte
**KDP → info-business**: `Libro KDP €9.99 → link nel libro → PDF gratuito → €27-197`.

**→ Destinazione: reparto Pricing & Offerta** (le fasce) + **reparto Strategia** (la scala e i
percorsi). Il percorso KDP è un collegamento diretto col workflow libri già operativo.

### 4.4 Il resto dello Strategy Command Center

| File | Righe | → Reparto |
|---|---:|---|
| `WORKFLOW_CADENZE.md` | 1.038 | **Esecuzione Lancio** — cadenze e ritmo operativo |
| `CROSS_POLLINATION_ENGINE.md` | 1.032 | **Strategia** — FASE 10, casi studio → YouTube, studenti → agenzia |
| `OKR_SYSTEM.md` | 922 | **Strategia** — alimenta D3 del filtro anti-ADD |
| `DECISION_FRAMEWORK.md` | 779 | **Strategia** — decisione KEEP/UPDATE/RELAUNCH/RETIRE della FASE 10 |
| `OUTPUT_TEMPLATES.md` | 744 | **tutti** — formati di consegna standard |
| `DASHBOARD_ENGINE.md` | 675 | **Strategia** — stato 🟢🟡🔴 che D2 legge |
| `RETROSPETTIVA_ENGINE.md` | 503 | **Esecuzione Lancio** — debrief post-lancio |
| `REVENUE_TRACKER.md` | 487 | **Strategia** — tracking revenue per pillar |
| `GERARCHIA_PILLAR.md` | 390 | **Strategia** — definizione dei 3 pillar, letta da D1 |
| `PROJECT_MAP.md` | 166 | — mappa di navigazione, non si assorbe |

---

## 5. PRODUCT CREATION LAB → reparto **Prodotto**

`System OMEGA/.../CONTESTO - SOLO ESEMPI/Product Creation Lab/KNOWLEDGE_BASE/`
**8 file KB, 2.453 righe** (+ `CUSTOM_INSTRUCTIONS.md` e `PROJECT_MAP.md`).

### 5.1 `KB_01_PRODUCT_PIPELINE.md` (401 righe) — l'input obbligatorio

Il brief che entra in produzione **deve** contenere, altrimenti la pipeline non parte:

- Idea con **score ≥60/100**
- Validazione MVP positiva: **almeno 5 persone** hanno detto "sì, lo comprerei"
- Target definito — e il file specifica: *non "chiunque voglia imparare X"*
- Formato scelto (PDF / Ebook / Mini-corso / Corso / Percorso)
- Fascia prezzo ipotizzata

**→ Destinazione: reparto Prodotto, come gate di ingresso.** Questo è l'equivalente esatto,
per i lanci, del `KDP-GATE` che nel workflow libri blocca prima che qualcuno esegua.

### 5.2 `KB_02_RICERCA_PRE_PRODUZIONE.md` (306 righe) — la ricerca che blocca

**Regola non negoziabile testuale:** *"Non si procede al Step 1.2 senza aver completato questo
step."* Completo significa, misurabile:

- **≥15 frasi esatte** del target, **con URL della fonte**
- **≥5 pain point** distinti
- **≥3 prodotti competitor** analizzati (review negative 1-2 stelle su Amazon/Udemy)
- **≥3 gap** che i competitor non coprono
- Saper rispondere a: *"Perché il nostro prodotto è chiaramente migliore/diverso?"*

**→ Destinazione: reparto Intelligence & Competitor.** Copre esattamente la FASE 2 del
`Processo lanci` (pain point map I×F×A, obiezioni top 10 F×I, TOV 20-30 frasi).

### 5.3 `KB_03_LEARNING_PATH_ENGINE.md` (410 righe)

PRIMA→DOPO, **massimo 7 moduli, ideale 5**, **1 modulo = 1 trasformazione**, ogni modulo
produce un output pratico.
**Regola non negoziabile:** se non sai formulare *"Da [stato prima] a [stato dopo]"* per un
modulo, quel modulo non è pronto.

**→ Destinazione: reparto Prodotto.**

### 5.4 `KB_05_QUALITY_SYSTEM.md` (255 righe) — i 6 red flag assoluti

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

**Beta test obbligatorio per ogni prodotto ≥€97.** Criterio di uscita: *"correggi i problemi
segnalati da 2+ beta tester"*, *"tutti i red flag eliminati → prodotto approvato"*.

**→ Destinazione: reparto Prodotto, come GATE BLOCCANTE di uscita.** Sei controlli binari con
il proprio test: è la forma giusta di gate, la stessa di `KDP-GATE`.

### 5.5 `KB_08_METRICHE_KPI.md` (268 righe) — soglie post-vendita

| Metrica | Target | Soglia critica |
|---|---|---|
| Refund rate | **<5%** | **>10%** |
| Completion rate | **>40%** | **<20%** |
| Testimonial entro 30gg | **≥3** | 0 dopo 30gg |
| Prodotti in pipeline | **≥2 sempre** | — |
| Ricerca completata prima di iniziare | **100%** | *"Nessuna eccezione — processo rotto"* |
| Beta test per prodotti ≥€97 | **100%** | — |

**→ Destinazione: reparto Prodotto** (qualità) + **reparto Esecuzione Lancio** (FASE 10, il
debrief legge queste soglie).

### 5.6 Il resto

| File | Righe | → Reparto |
|---|---:|---|
| `KB_04_PRODUZIONE_CONTENUTI.md` | 322 | **Prodotto** |
| `KB_06_PACKAGING_HANDOFF.md` | 278 | **Prodotto** → handoff verso Esecuzione Lancio |
| `KB_07_STANDARD_PER_TIPO.md` | 213 | **Prodotto** — standard per PDF/ebook/corso/percorso |

---

## 6. YOUTUBE LEAD ENGINE → reparti **Siti & Funnel** + **Copy** + **Marketing & Traffico**

`System OMEGA/.../CONTESTO - SOLO ESEMPI/YouTube Lead Engine/KNOWLEDGE_BASE/`
**7 file, 2.860 righe.** **Non è nella lista fonti della task** — trovato durante la
ricognizione, ed è materiale di lancio a tutti gli effetti.

### 6.1 `KB_04_funnel-unico-perfetto.md` (359 righe) — la struttura, non il PDF

Esiste anche come `Funnel Unico Perfetto ... .pdf` in `InfoBusiness/`, ma **questo è il .md
già strutturato**: si assorbe questo, il PDF resta come sorgente originale.

Struttura codificata: `Video YouTube → Bridge page (nome+email, 3 tag) → redirect →
Upsell €15 (VSL 3-5 min) → Sequenza email 3 giorni → VSL evento → Webinar → Follow-up 5 giorni`,
con nurture settimanale per chi non avanza.

**Benchmark target, numerici:**

| Step | Metrica | 🟢 Verde | 🟡 Giallo |
|---|---|---|---|
| Bridge page | Opt-in rate | **>35%** | 20-35% |
| Upsell €15 | Conversion | **>15%** | 8-15% |
| VSL evento | Iscrizione webinar | **>20%** | 10-20% |
| Webinar | Show rate | **>30%** | 20-30% |
| Webinar | Conversion rate | **>5%** | 2-5% |
| Follow-up | Recupero post-webinar | **>15%** | 8-15% |

Tre avvertenze operative già scritte, tutte da portare nel piano:
- **Mai mischiare traffico**: bridge page YouTube separata da quella paid, altrimenti il
  confronto organico vs paid non è misurabile.
- **L'upsell €15 non è opzionale**: è il finanziamento del funnel — anche al 10% genera €1,50
  per opt-in e abbassa il CAC.
- **Il nurture non si interrompe**: un lead a 6 mesi converte al lancio successivo; cambia la
  frequenza, non la lista.

**→ Destinazione: reparto Siti & Funnel** (struttura pagine, tag, routing) +
**reparto Esecuzione Lancio** (i benchmark diventano le soglie del tracking giornaliero).

> **Nota per L3, importante.** La task chiede *"come si verifica che le pagine siano online e
> funzionanti — non 'fatte', online e funzionanti"*. Questi sei benchmark sono la risposta:
> una pagina è verificata quando **misura**, non quando esiste.

### 6.2 `KB_07_app-soc-framework.md` (379 righe) — APP-SOC, il framework di copy

**A**ttention (aggancio) · **P**roblem (amplificazione) · **P**romise (trasformazione) ·
**S**olution (meccanismo unico) · **O**ffer (dettaglio) · **C**lose (chiusura con Reason Now).

Ogni lettera ha la sua sezione di dettaglio, più tre declinazioni per contesto: lead magnet
(brevissimo), VSL upsell €15 (3-5 min), email Day 4 (case study).

**→ Destinazione: reparto Copy.** ⚠️ **Da riconciliare con lo standard APSOC dell'Impero**, di
cui il CMO è owner e su cui vigila la guild `guild-copy-apsoc`: qui è chiamato **APP-SOC** (due
P). Vanno confrontati prima di scrivere L5 — o sono lo stesso framework con due nomi, o sono
due, e in quel caso uno solo può essere lo standard.

### 6.3 Il resto

| File | Righe | → Reparto |
|---|---:|---|
| `KB_08_email-sequence-master.md` | 522 | **Copy** — FASE 7, le 4 sequenze |
| `KB_10_analytics-dashboard-template.md` | 460 | **Esecuzione Lancio** — report metriche giornaliero |
| `KB_09_storytelling-guide.md` | 455 | **Copy** |
| `KB_06_brand-voice.md` | 345 | **Copy** — da riconciliare con la brand voice presidiata dal CMO |
| `KB_05_youtube-lead-engine-brief.md` | 340 | **Marketing & Traffico** — FASE 8 |

---

## 7. ⛔ DOVE MI SONO FERMATO — fonti non ancora aperte

**Fermato su ordine di Gael, 2026-09-02.** Queste fonti sono **inventariate ma non lette**.
Nessuna riga di questo documento pretende il contrario, ed è il motivo per cui il **gate L2 è
dichiarato NON PASSATO**.

| Fonte | Cosa manca | Perché serve |
|---|---|---|
| `FILTRO_ANTI_ADD.md` — **D5** | La quinta domanda del filtro | Il gate di ingresso è incompleto senza |
| `Project-Marketing University.md/` (16 file) | Tutto: `KB_08_FRAMEWORKS_REGISTRY`, `KB_14_PRELOADED_FRAMEWORKS`, `KB_02_EXTRACTION_ENGINE`, `KB_09_STUDY_PRIORITY_ENGINE`, `KB_10_QUALITY_VALIDATION` | È la FASE 2 (ricerca target) del Processo lanci |
| `Info-Business-HQ_Knowledge/Priorità 1/` | 3 PDF Webinar + `Funnel Unico Perfetto.pdf` + `CATALOGO PRODOTTI ATTUALE.md` | Il catalogo prodotti è l'input della FASE 1 |
| `Info-Business-HQ_Knowledge/Priorità 2/` | 9 PDF (Agency Scalping, Outreach, Funnel acquisizione, Freelancing) | Materiale agenzia: da valutare se è di 14-LANCI o di 01-AGENCY |
| `Formazzione/` | Superset dei precedenti + Claude code, Storytelling, `Rebdere YOUTUBE un Lead magnet.txt` | — |
| `Lancio corso skill beast/` (798 file) | `Framework_ICRO_Digital_Empire.pdf` + la landing CCM premium in React | **Il codebase è un asset reale per Siti & Funnel**: una landing di lancio già costruita |
| `Lanco ebook/` (2 file) | `Gemini.md` + `index.html` | Landing di lancio ebook |

**Nessuna di queste voci è "da approfondire" in senso vago:** ognuna ha il file, il motivo e il
reparto candidato. Vanno aperte, non cercate.

---

## 8. Bilancio di quanto è stato assorbito

| | Valore |
|---|---|
| Fonti aperte ed estratte | **4 su 10** |
| Righe di conoscenza lette | **~14.450** |
| Framework concreti mappati a un reparto | **26** |
| Gate bloccanti individuati | **3** (filtro anti-ADD, brief ≥60/100 + MVP 5 persone, 6 red flag) |
| Soglie numeriche recuperate | **20+** (6 allarmi, 6 benchmark funnel, 6 KPI prodotto, 3 soglie funnel) |
| Duplicati verificati e neutralizzati | **3 coppie** |
| Fonti dichiarate vuote | **3** (le `.skill` che non esistono) |
| Scoperte fuori dalla lista della task | **2** (`Processo lanci` FASE 0→10, `YouTube Lead Engine`) |

---

## 9. Cosa passa a L3 (già solido, non cambia se L2 si completa)

1. **Gli 8 reparti della task coprono le 11 fasi.** La mappa §1 lo dimostra. Non aggiungere
   reparti in L3.
2. **Tre gate bloccanti esistono già scritti** e vanno messi in fila: filtro anti-ADD in
   ingresso (Strategia) → brief ≥60/100 + MVP 5 persone (Prodotto) → 6 red flag in uscita
   (Prodotto). Nessuno dei tre va inventato.
3. **Le FASI 6-7-8 girano in parallelo.** L4 deve avere un punto di sincronizzazione, non una
   sequenza lineare.
4. **Le soglie numeriche ci sono tutte.** Un lancio è misurabile dal primo giorno: opt-in >35%,
   upsell >15%, show rate >30%, CR webinar >5%. L4 non deve inventare KPI.
5. **APP-SOC vs APSOC va risolto prima di L5** — vedi §6.2.
6. **Le tre `.skill` mancanti vanno riscritte, non assorbite** — e Max va avvisato.

---

## Connessioni

- [[RICOGNIZIONE-LANCI]] — L1, chiusa (CP-20260902-009)
- [[26-ECOSISTEMA-LANCI]] — L3/L4/L5, da scrivere
- `company/Memory/tasks/TASK-GAEL-20260831-SETTIMANA-02.md` — la task madre
- `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/workflow/WF-LANCIO.md` — si avvolge (ADR-003)
