---
Type: PROJECT
Status: Proposta (in attesa di ok Max)
Tags: #lanci #ecosistema-14 #L3 #architettura #TASK-LANCI-ECO-W2
Created: 2026-09-03
Last updated: 2026-09-03
Autore: Gael (via Emperator)
Task: TASK-LANCI-ECO-W2 — sotto-task L3
Gate L3: ✅ PASSATO — §1-2 scritte, 8 reparti con missione/output/blocco
⚠️ Zero cartelle create. `company/Ecosistemi/14-LANCI/` NON esiste e non deve esistere
   finché Max non approva.
---

> ## ⚠️ 2026-09-05 — QUESTO DOCUMENTO È SUPERATO. VAI A `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/`
>
> Questo file resta come **L3 di Gael**, ed è la base da cui è nato tutto il resto: gli otto
> reparti, le etichette wrap/nuovo, i sette gate. Va letto per capire **da dove si è partiti**.
>
> **Ma due cose qui dentro sono cambiate e non vanno più usate:**
> 1. **Il numero è `15`, non `14`.** Il 14 è occupato da Tesoreria (collisione trovata il
>    2026-09-04). Riservato in `company/Ecosistemi/REGISTRO-NUMERI.md`.
> 2. **I reparti sono dodici, non otto.** I quattro aggiunti — offerta, editoriale, tesoro,
>    memoria — coprono cose che negli otto non avevano un proprietario.
>
> **Il piano completo di costruzione (L4, L5, L6 e oltre) è in
> `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/`**, undici dossier. Si comincia da `00-LEGGIMI-GAEL.md`.

# 🚀 14 — ECOSISTEMA LANCI *(superato: vedi il riquadro sopra)*

> **§1-2, deliverable di L3.** L'ecosistema e i suoi reparti.
> §3 (flusso end-to-end + comando) è L4. §4 (agenti e gate) è L5. L'ADR è L6.
>
> Basi misurate: [[RICOGNIZIONE-LANCI]] (L1) e [[ASSORBIMENTO-LANCI]] (L2).

---

## 0. Come è nato questo piano — tre giri, e cosa è cambiato

Regola dell'Impero: non si costruisce mai sulla prima idea. Tre giri, ognuno deve battere il
precedente **su un punto nominato**. Qui sotto solo cosa è cambiato, non i giri per intero.

### Giro 1 — "otto reparti nuovi in un ecosistema nuovo"

La lettura letterale della task: si crea `14-LANCI/` con gli otto reparti nominati da Max, si
scrivono le loro missioni, i loro agenti, i loro workflow.

### ❌ L'obiezione più forte contro il Giro 1

**Quattro degli otto reparti esistono già**, un livello sotto, dentro 02-INFO-BUSINESS.
Non come idea: come specifica scritta. Misurato il 2026-09-03:

| Area L2 esistente | File .md | Righe | Eseguibili | Schede agente |
|---|---:|---:|---:|---:|
| `IB-L2-PROD` Produzione Prodotti | 21 | 2.703 | **0** | 10 |
| `IB-L2-LANC` Lanci & Campagne | 19 | 2.377 | **0** | 9 |
| `IB-L2-VEND` Vendite & Funnel | 19 | 2.353 | **0** | 8 |
| `IB-L2-STRA` Strategia & Intelligence | 17 | 2.413 | **0** | 7 |
| `IB-L2-COMM` Community & Retention | 18 | 2.181 | **0** | 8 |
| **Totale 02-INFO-BUSINESS** | **94** | **12.027** | **0** | **42** |

E gli altri due (Copy, Marketing & Traffico) esistono in 04-MARKETING:

| Reparto L2 esistente | Righe | Eseguibili |
|---|---:|---:|
| `L2-1-Copywriting` | 2.934 | **0** |
| `L2-2-Advertising` | 2.906 | **0** |
| `L2-3-Email-Lifecycle` | 2.611 | **0** |
| `L2-4-Analytics` | 2.636 | **0** |
| `L2-5-Brand-Creative-Strategy` | 2.521 | **0** |
| `L2-6-Conversion-Architecture` | 2.618 | **0** |
| **Totale 04-MARKETING** | **16.226** | **0** |

```bash
$ ls .claude/agents/ | grep -icE "^ib-"
0        # 42 schede agente progettate, zero agenti ufficiali invocabili
```

**Costruire il Giro 1 significherebbe: 28.253 righe di specifica orfane, due proprietari per lo
stesso lavoro (chi lancia? `IB-L2-LANC` o `14-LANCI/Esecuzione`?), e una terza generazione di
carta sopra due che già non eseguono.** Viola ADR-003 (wrap, mai riscrittura), ADR-008 (nessun
artefatto orfano) e la direttiva *niente si scarta*.

### Giro 2 — "14-LANCI non è un ecosistema, è un orchestratore trasversale"

Nessun reparto proprio: solo un flusso che chiama reparti che vivono altrove.

### ❌ L'obiezione più forte contro il Giro 2

Due cose lo rompono. **Primo:** un orchestratore senza reparti è un livello di indirezione in
più su una pila che già non esegue — non toglie carta, ne aggiunge. **Secondo, e decisivo:**
Max ha chiesto un ecosistema con dei reparti, e per nome ha chiesto **il sotto-ecosistema
Siti**. Contraddire un ordine in silenzio è vietato: si propone, non si decide da soli.

### ✅ Giro 3 — quello che si costruisce

**14-LANCI esiste come ecosistema, e ogni suo reparto porta un'etichetta dichiarata: NUOVO o
WRAP.**

- **NUOVO** = non esiste da nessuna parte nell'Impero. Si costruisce.
- **WRAP** = esiste già altrove. 14-LANCI **lo usa via handoff, non lo riscrive** (ADR-003).
  Il reparto di 14-LANCI è il *contratto* con quel reparto, non una sua copia.

**Cosa ha vinto il Giro 3 sul Giro 1:** zero righe orfane, zero doppi proprietari, ordine di
Max rispettato.
**Cosa ha vinto sul Giro 2:** l'ecosistema esiste davvero, con un reparto proprio e il
sotto-ecosistema Siti che Max ha chiesto.

**E il conto finale è questo: su otto reparti, uno solo è NUOVO.**
Il che dice, in una riga, dove sta davvero il valore di 14-LANCI: **non nelle capacità — nel
flusso eseguibile e nei gate che oggi non esistono.**

---

## 1. L'ECOSISTEMA

### 1.1 Missione

> **14-LANCI porta un prodotto finito sul mercato e ne misura l'esito.**
> Non lo crea, non lo scrive, non lo disegna: lo **lancia**. È l'organo che trasforma
> "è pronto" in "è in vendita, e so quanto ha reso".

### 1.2 DONE WHEN — quando l'ecosistema ha fatto il suo lavoro

Un lancio è chiuso quando **tutte e cinque** sono vere:

1. Il prodotto ha **un prezzo deciso e una data decisa**, scritti in un file, non in una testa.
2. Le pagine del funnel sono **online e misurate** — non "fatte": misurate (§2.6).
3. Il carrello si è aperto e si è chiuso alle date del calendario.
4. Le metriche reali sono a confronto con i benchmark, e **ogni scarto ≥10% ha una causa
   scritta**.
5. Il debrief è in Memory e almeno **3 pattern** sono distillati per il lancio successivo.

### 1.3 Il motivo per cui questo ecosistema deve esistere

Non è teorico. È un prodotto fermo, misurato in L2:

Il **Manuale Claude Code — Da zero a Senior** è **"Pronto"** dal **07/03/2026**, 203 pagine.
Ha il lead magnet finito (Framework I.C.R.O., 12 pagine), la landing costruita (299 righe), il
design system che l'ha generata, una libreria di ~30 componenti, la struttura del funnel, il
framework di copy, lo script webinar e le sequenze email.

**Prezzo: "€ NON LO SO". Data: "Presto spero". Metriche: 0.**

E non è una scoperta nuova: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md` lo dichiara
**BLOCCANTE (B1)** dall'**11 giugno**, con le parole *"prezzo NON LO SO e doppio ruolo
contraddittorio (gratuito vs pagamento)"*.

**Un blocco dichiarato tre mesi fa, con tutto il resto pronto attorno, e mai risolto.**
Questo è il buco che 14-LANCI chiude. Non "fare lanci meglio": **far uscire ciò che è già
pronto.**

### 1.4 Confini — cosa 14-LANCI NON fa

| Non fa | Chi lo fa |
|---|---|
| Creare il prodotto | `IB-L2-PROD` (02-INFO-BUSINESS) |
| Scrivere il copy da zero | `L2-1-Copywriting` (04-MARKETING) |
| Acquisire clienti per l'agenzia | 01-AGENCY |
| Gestire la community post-acquisto | `IB-L2-COMM` (02-INFO-BUSINESS) |
| Studiare video e corsi | Empire Studio |

**La linea:** se un'attività continua **dopo** la chiusura del carrello, non è di 14-LANCI.

### 1.5 Regola di composizione — l'invariante dell'ecosistema

> **Nessun reparto di 14-LANCI duplica un reparto esistente.**
> Un reparto è NUOVO solo se, cercato nell'Impero, non esiste. Altrimenti è un WRAP: un
> contratto di handoff verso il proprietario reale, che resta l'unico a possedere quel lavoro.

Conseguenza operativa vincolante per L5: **un reparto WRAP non può avere agenti propri che
rifanno il lavoro del proprietario.** Può avere solo agenti di *interfaccia* (prepara l'input,
verifica l'output, gestisce il gate).

### 1.6 Numerazione e posizione

```bash
$ ls company/Ecosistemi/
01-AGENCY  02-INFO-BUSINESS  03-CONTENT-FACTORY  04-MARKETING  05-MULTI-BUSINESS
06-PLATFORM  07-FORGE  08-INTELLIGENCE  09-OPERATIONS  10-MEMORY
11-APEX-7-CORE  12-STREAM-S7-BOT  13-ARENA-APEX
```

**`14-LANCI` — primo numero libero.** Livello L1, pari agli altri ecosistemi.
⚠️ **La cartella non esiste e non va creata fino all'ok di Max.**

### 1.7 Collegamento al Corporate Backbone

**BUS — handoff in INGRESSO**

| Da | Cosa arriva | Criterio di accettazione |
|---|---|---|
| `IB-L2-PROD` | Prodotto finito + handoff di packaging | 6 red flag a zero; beta test fatto se ≥€97 |
| `IB-L2-STRA` | Idea validata | score ≥60/100 + MVP confermato da ≥5 persone |
| `04-MARKETING/L2-1` | Copy finita | gate APSOC ≥80/100 |
| `08-INTELLIGENCE` | Dossier competitor e trend | fonti citate, nessun dato stimato |
| `09-OPERATIONS` | Budget approvato | importo firmato, non ipotizzato |

**BUS — handoff in USCITA**

| A | Cosa parte |
|---|---|
| `IB-L2-COMM` | Lista acquirenti + onboarding, alla chiusura del carrello |
| `03-CONTENT-FACTORY` | Brief asset (video, caroselli, short) per la FASE 8 |
| `10-MEMORY` | Debrief + ≥3 pattern distillati |
| `Tesoreria` | Revenue reale del lancio, per motore di business |
| `01-AGENCY` | Lead high-ticket emersi dal lancio (cross-pollination) |

**BRAIN — namespace**

```
lanci/{lancio-id}/          calendario, gate, dry-run, tracking, debrief
lanci/catalogo/             prezzo e data per prodotto — la fonte di verità di §1.3
lanci/benchmark/            soglie attese vs misurate, storico per lancio
lanci/reasoningbank/        pattern distillati (≥3 per lancio)
```

> ⚠️ **Nota di migrazione.** `IB-L2-LANC` aveva progettato `infobusiness/lanci/*`, mai creato
> (L1: zero cartelle, zero lanci tracciati). Non c'è nulla da migrare: si nasce su `lanci/*`.
> Va deciso in L6 se `infobusiness/lanci/*` resta come alias o si dichiara chiuso.

**GOVERNANCE — i gate bloccanti, tutti già scritti e assorbiti in L2**

| Gate | Soglia | Fonte |
|---|---|---|
| **G1 — Filtro anti-ADD** | 5 domande sequenziali, una sola bocciatura ferma tutto | `FILTRO_ANTI_ADD.md` |
| **G2 — Brief di prodotto** | score ≥60/100 + MVP ≥5 persone | `KB_01_PRODUCT_PIPELINE.md` |
| **G3 — 6 red flag** | uno solo presente → non si consegna | `KB_05_QUALITY_SYSTEM.md` |
| **G4 — Prezzo e data** | entrambi presenti e non vuoti | **nuovo — §2.4** |
| **G5 — Copy APSOC** | ≥80/100 | standard dell'Impero, owner CMO |
| **G6 — Dry-run costi** | delta vs budget >10% → BLOCK | `REGOLE.md` R6 di `IB-L2-LANC` |
| **G7 — Pagine online** | ogni pagina risponde e traccia | **nuovo — §2.6** |

Cinque su sette esistono già. **G4 e G7 sono nuovi, e sono esattamente i due che avrebbero
impedito al Manuale Claude Code di restare fermo sei mesi.**

**COORDINATION** — topologia swarm: **pipeline** per il calendario T-30→T+7, con un
**punto di sincronizzazione unico** allo Sprint Produzione, dove le FASI 6-7-8 girano in
parallelo (L2 §1).

---

## 2. I REPARTI L2

Otto reparti. Per ognuno: **missione in una frase**, **cosa produce** (output verificabile),
**cosa lo blocca**, **etichetta NUOVO/WRAP** e **la fonte assorbita** in L2.

> Il gate L3 dice: *"se un reparto non ha un output verificabile, non è un reparto — è un
> capitolo"*. Ogni output qui sotto è un file o uno stato, mai un concetto.

---

### 2.1 · LAN-STRATEGIA — 🔵 WRAP

**Missione.** Decide se questo lancio si fa adesso, o non si fa.

| | |
|---|---|
| **Produce** | `decisione.json` — verdetto GO/BACKLOG/SCARTA con la risposta a ciascuna delle 5 domande e il KR agganciato |
| **Lo blocca** | **G1**: una sola domanda bocciata ferma tutto. Un pillar 🔴 blocca in modo assoluto |
| **Wrappa** | `IB-L2-STRA` (2.413 righe, 7 agenti progettati) + Board CEO |
| **Fonte L2** | `FILTRO_ANTI_ADD.md` (785) · `SOGLIE_ALLARME.md` (870) · `OKR_SYSTEM.md` (922) · `DECISION_FRAMEWORK.md` (779) · `GERARCHIA_PILLAR.md` (390) |

**Perché è un reparto e non un capitolo:** produce un verdetto binario che ferma o lascia
passare denaro. Le 5 domande sono a risposta chiusa — D5, il *test della scomparsa*, è quella
che smaschera i lanci fatti per noia: *"se sparisse domani, il business ne soffrirebbe
concretamente?"*

---

### 2.2 · LAN-INTELLIGENCE — 🔵 WRAP

**Missione.** Porta al lancio le parole vere del target e i buchi veri dei concorrenti.

| | |
|---|---|
| **Produce** | `ricerca.json` — ≥15 frasi esatte **con URL**, ≥5 pain point, ≥3 competitor analizzati, ≥3 gap scoperti |
| **Lo blocca** | Regola testuale: *"non si procede senza aver completato questo step"*. Nessuna frase senza URL |
| **Wrappa** | `IB-L2-STRA` (agenti INTEL, COMP, ICP) + ecosistema `08-INTELLIGENCE` |
| **Fonte L2** | `KB_02_RICERCA_PRE_PRODUZIONE.md` (306) · Marketing University (**11.853 righe**, la fonte più grande) |

**Perché è un reparto:** l'output è contabile — 15, 5, 3, 3. O ci sono, o il reparto non ha
finito.

⚠️ **Da risolvere in L6.** `KB_08_FRAMEWORKS_REGISTRY` è uno schema dati vero (ID stabili mai
riassegnati, deduplicazione, campo `contraddizioni`) e si sovrappone all'agente
`conoscenza-empire`, fornitore unico di conoscenza dell'Impero. **O il registro diventa il suo
formato dati per l'area lanci, o nascono due biblioteche.**

---

### 2.3 · LAN-PRODOTTO — 🔵 WRAP

**Missione.** Certifica che il prodotto è davvero pronto a essere venduto.

| | |
|---|---|
| **Produce** | `certificato-prodotto.json` — 6 red flag tutti a zero, beta test allegato se ≥€97, handoff di packaging firmato |
| **Lo blocca** | **G3**: un solo red flag presente → non si consegna. **G2** in ingresso: score <60/100 o MVP <5 persone → non entra |
| **Wrappa** | `IB-L2-PROD` (2.703 righe, 10 agenti progettati) |
| **Fonte L2** | `KB_05_QUALITY_SYSTEM.md` (255) · `KB_01_PRODUCT_PIPELINE.md` (401) · `KB_03_LEARNING_PATH_ENGINE.md` (410) · `KB_06_PACKAGING_HANDOFF.md` (278) |

**Perché è un reparto:** i 6 red flag hanno ognuno **il proprio test già scritto**. Es. #5:
*"testa ogni link in modalità incognito, come lo studente non loggato come te"*. È un gate
eseguibile, non un'opinione.

---

### 2.4 · LAN-PRICING — 🟢 **NUOVO — l'unico**

**Missione.** Decide il prezzo e la data, e non lascia passare il lancio senza entrambi.

| | |
|---|---|
| **Produce** | `offerta.json` — **prezzo**, **data di apertura carrello**, **durata**, stack di valore (rapporto ≥3×), anchor, bonus, garanzia, e il livello del Product Ladder |
| **Lo blocca** | **G4**: `prezzo` o `data` vuoti, nulli, o uguali a stringhe come *"NON LO SO"* / *"presto"* → **BLOCK**. Salto di più di un livello del ladder → BLOCK |
| **Perché NUOVO** | Verificato: non esiste. Il `team-prezzi` è solo una promessa in ADR-005 (B-003), e `Product Pricing Strategist.skill` non esiste in tutto il repo |
| **Fonte L2** | `PRODUCT_LADDER.md` (577) — 5 livelli: €0 / €7-47 / €97-297 / €497-997 / €2.000+, con la regola *"non saltare da €27 a €2.000 senza passaggi"* |

**Perché questo reparto è il cuore dell'ecosistema.** È l'unico NUOVO, e non per caso: è
esattamente il pezzo mancante che ha lasciato il Manuale Claude Code fermo dal 7 marzo. Tutti
gli altri sette reparti hanno un proprietario da qualche parte. **Il prezzo non ce l'ha
nessuno.**

⚠️ **Prima decisione che questo reparto deve prendere, e va presa da Max o Gael, non da un
agente:** il Manuale Claude Code ha un **doppio ruolo contraddittorio** dichiarato dall'11
giugno — nel catalogo è *"Ebook Premium"* a pagamento, e nella scheda del corso "Vendi la
Skill" è *"un forte lead magnet: Ebook Manuale Claude Code GRATUITO"*. **Le due cose non
possono essere vere insieme.** Finché non si sceglie, G4 non può passare.

---

### 2.5 · LAN-COPY — 🔵 WRAP

**Missione.** Consegna al lancio tutti i testi, nell'ordine in cui il funnel li usa.

| | |
|---|---|
| **Produce** | `copy/` — sales page, landing opt-in, VSL mini-corso (3-5 min), VSL evento (8-12 min), script webinar, thank you, checkout, e 4 sequenze email (pre-lancio, live, follow-up non acquirenti, onboarding acquirenti) |
| **Lo blocca** | **G5**: APSOC <80/100. Ordine di scrittura non rispettato (la sales page viene prima, sempre) |
| **Wrappa** | `04-MARKETING/L2-1-Copywriting` (2.934 righe) + `L2-3-Email-Lifecycle` (2.611) + skill `cro-copy-architect` + guild `guild-copy-apsoc` |
| **Fonte L2** | `KB_07_app-soc-framework.md` (379) · `KB_08_email-sequence-master.md` (522) · `KB_09_storytelling-guide.md` (455) · **3 PDF "Webinar Milionario"** (~40 pagine) |

**Il framework webinar è recuperato.** Il `Processo lanci` cita una `Webinar Script Master.skill`
che **non esiste**; la sostanza però è integra nei tre PDF: si parte da **una sola grande
promessa** — *"l'unica idea che, se il pubblico la crede raggiungibile, rende tutte le altre
obiezioni irrilevanti"* — e da lì discendono titolo, apertura, i tre segreti e il pitch. Non
sono quattro pezzi: sono quattro derivazioni della stessa frase.

⚠️ **Da risolvere prima di L5:** la fonte scrive **APP-SOC** (due P: Attention, Problem,
Promise, Solution, Offer, Close); lo standard dell'Impero è **APSOC**, con il CMO come owner e
una guild che lo sorveglia. **O sono lo stesso framework con due nomi, o sono due — e uno solo
può essere lo standard.**

---

### 2.6 · LAN-SITI — 🔵 WRAP + estensione · *il sotto-ecosistema che Max ha chiesto per nome*

**Missione.** Mette online le pagine del lancio e prova che funzionano, misurandole.

| | |
|---|---|
| **Produce** | `funnel.json` — per ogni pagina: URL pubblico, **codice di risposta HTTP**, tag installati e verificati, evento di conversione che spara davvero |
| **Lo blocca** | **G7**: una pagina che non risponde 200, o che non registra l'evento di conversione, **non è online** — anche se esiste |
| **Wrappa** | `IB-L2-VEND` (2.353 righe) + skill `site-build`, `site-copy`, `site-deploy`, `signup`, `empire-premium-style` |
| **Estende** | Nessun reparto esistente possiede il *funnel completo di un lancio*: `IB-L2-VEND` si ferma a sales page e checkout |

**Le pagine di un lancio, la lista chiusa:** bridge page opt-in · pagina lead magnet ·
upsell €15 · pagina webinar (registrazione) · pagina webinar (live/replay) · sales page ·
checkout · thank you · upsell/downsell post-acquisto.

**I benchmark che rendono una pagina "verificata"** — dalla fonte, non inventati:

| Pagina | Metrica | 🟢 | 🟡 |
|---|---|---|---|
| Bridge page | Opt-in rate | >35% | 20-35% |
| Upsell €15 | Conversion | >15% | 8-15% |
| VSL evento | Iscrizione webinar | >20% | 10-20% |
| Webinar | Show rate | >30% | 20-30% |
| Webinar | Conversion rate | >5% | 2-5% |
| Follow-up | Recupero | >15% | 8-15% |

**La risposta esatta alla domanda di Max** (*"non 'fatte' — online e funzionanti"*): una pagina
è verificata quando **misura**. Se non produce un numero, non è online: è solo pubblicata.

**Asset già esistenti che questo reparto eredita**, misurati in L2:
- `Lanco ebook/Sito- Leanding page/index.html` — landing costruita, 299 righe
- `Lanco ebook/Sito- Leanding page/Gemini.md` — 54 righe di design system inviolabile
- `Lancio corso skill beast/Leanding Page CCM/` — Next.js, ~30 sezioni, incluse **4 varianti
  di gestione obiezioni già in codice** (`ObjectionCPB_Checkout/Time/Website/WordOfMouth`)

⚠️ **Da risolvere in L5:** `Gemini.md` e la skill `empire-premium-style` descrivono lo stesso
tipo di pagina con due sistemi visivi diversi. Uno dei due è lo standard.

**Tre regole ereditate, non negoziabili:**
1. **Mai mischiare traffico** — bridge page organica separata da quella paid, altrimenti il
   confronto non è misurabile.
2. **L'upsell €15 non è opzionale** — è il finanziamento del funnel: anche al 10% genera €1,50
   per opt-in e abbassa il CAC.
3. **Il nurture non si interrompe** — cambia la frequenza, mai la lista.

---

### 2.7 · LAN-TRAFFICO — 🔵 WRAP

**Missione.** Porta persone dentro il funnel, per canale e con numeri separati per canale.

| | |
|---|---|
| **Produce** | `traffico.json` — per canale: volume, costo, opt-in generati, CAC. Più gli asset della FASE 8: 3 video (Anchor 70% / Shift 20% / Conversion 10%), 9+ short, il lead magnet |
| **Lo blocca** | Traffico mischiato fra organico e paid → il dato non è valido, si rifà. Spesa oltre il budget approvato → **G6** |
| **Wrappa** | `04-MARKETING/L2-2-Advertising` (2.906) + `L2-4-Analytics` (2.636) + skill `ads`, `ad-creative`, `launch`, `social` |
| **Fonte L2** | `KB_05_youtube-lead-engine-brief.md` (340) · **Framework I.C.R.O.** (12 pagine, lead magnet già finito e pubblicabile) |

**Perché è un reparto:** produce un CAC per canale. È un numero, e o c'è o non c'è.

---

### 2.8 · LAN-ESECUZIONE — 🔵 WRAP · *il reparto che si sposta, non si riscrive*

**Missione.** Fa partire il calendario, tiene i gate, apre e chiude il carrello, scrive il
debrief.

| | |
|---|---|
| **Produce** | `calendario.md` (T-30→T+7 con owner e dipendenze) · `state.json` (stato di ogni step) · `dry-run.md` · verbale go/no-go · tracking giornaliero · `debrief.md` con ≥3 pattern |
| **Lo blocca** | **G6**: delta costi vs budget >10% → BLOCK. Un gate a monte non passato → il calendario non avanza |
| **Wrappa** | `IB-L2-LANC` (19 file, 2.377 righe, 9 agenti progettati) — **ADR-003: si sposta e si avvolge, non si riscrive** |
| **Fonte L2** | `WF-LANCIO.md` (152) · `WF-WEBINAR.md` (144) · `REGOLE.md` (117) · `WORKFLOW_CADENZE.md` (1.038) · `RETROSPETTIVA_ENGINE.md` (503) · `KB_10_analytics-dashboard-template.md` (460) |

**Perché `WF-LANCIO` si salva quasi intero** (L1): ha già la forma giusta —
`Input JSON → Pipeline + owner → Gate → Output JSON → Handoff → Dry-run obbligatorio`. È la
stessa anatomia del flusso KDP che funziona. **Gli manca una cosa sola: il comando che lo
esegue.** Quello è L4.

**Le soglie diagnostiche durante il carrello aperto**, ereditate da `SOGLIE_ALLARME.md`:
opt-in **<20%** = problema serio · open rate **<20%** = subject line · click **<1%** = contenuto.

---

## 3. Il quadro degli otto reparti

| # | Reparto | Etichetta | Output verificabile | Gate che lo blocca |
|---|---|---|---|---|
| 2.1 | **LAN-STRATEGIA** | 🔵 WRAP | `decisione.json` | G1 |
| 2.2 | **LAN-INTELLIGENCE** | 🔵 WRAP | `ricerca.json` (15/5/3/3) | ricerca incompleta |
| 2.3 | **LAN-PRODOTTO** | 🔵 WRAP | `certificato-prodotto.json` | G2, G3 |
| 2.4 | **LAN-PRICING** | 🟢 **NUOVO** | `offerta.json` | **G4** |
| 2.5 | **LAN-COPY** | 🔵 WRAP | `copy/` | G5 |
| 2.6 | **LAN-SITI** | 🔵 WRAP + est. | `funnel.json` | **G7** |
| 2.7 | **LAN-TRAFFICO** | 🔵 WRAP | `traffico.json` | G6 |
| 2.8 | **LAN-ESECUZIONE** | 🔵 WRAP | `calendario.md` + `state.json` + `debrief.md` | G6 |

**Otto reparti, otto output che sono file. Sette gate, di cui cinque già scritti altrove e due
nuovi — G4 e G7 — che sono precisamente i due che mancavano.**

---

## 4. Le tre decisioni che 14-LANCI non può prendere da solo

Non sono blocchi tecnici: sono scelte che appartengono a una persona.

1. **Il Manuale Claude Code è a pagamento o è un lead magnet gratuito?** Le due fonti si
   contraddicono e il conflitto è aperto dall'11 giugno. Finché non si sceglie, G4 non passa e
   il primo lancio non parte. **Decide Max.**
2. **APP-SOC o APSOC?** Uno solo può essere lo standard di copy dell'Impero. **Decide il CMO.**
3. **`Gemini.md` o `empire-premium-style`?** Uno solo può essere il sistema visivo delle pagine
   di lancio. **Decide la guild Design.**

---

## 5. Cosa arriva dopo (non è in §1-2)

| Sotto-task | Cosa produce | Stato |
|---|---|---|
| **L4** | §3 — il flusso end-to-end di UN lancio + il comando ufficiale che lo esegue | Prossima |
| **L5** | §4 — agenti e gate per ogni reparto (con la regola §1.5: i WRAP hanno solo agenti di interfaccia) | Da fare |
| **L6** | ADR proposto + consegna a Max | Da fare |

**Costruzione: non questa settimana.** Il piano è il deliverable; la costruzione arriva dopo
l'ok di Max.

---

## Connessioni

- [[RICOGNIZIONE-LANCI]] — L1: il reparto Lanci è carta, misurato (CP-20260902-009)
- [[ASSORBIMENTO-LANCI]] — L2: 10 fonti, 58 framework mappati (CP-20260903-008)
- `PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS-V2.md` — le 5 aree L2 che 14-LANCI wrappa
- `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` — i reparti Copy e Advertising wrappati
- `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md` — l'invariante di §1.5
- `company/Memory/decisions/ADR-007-piano-v2-scala.md` — standard di scala dell'ecosistema
- `.claude/skills/ultimo-metro/` — trova il lavoro finito e mai uscito; 14-LANCI lo chiude
