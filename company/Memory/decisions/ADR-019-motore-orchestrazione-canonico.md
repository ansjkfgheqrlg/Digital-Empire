# ADR-019 — Il motore di orchestrazione canonico è `orchestration-layer`

- **Stato:** ATTIVO
- **Data:** 2026-09-03
- **Deciso da:** Emperator, per delega esplicita di Max (*"la prima domanda risolvi tu da solo"*)
- **Chiude:** la voce B-047 e la decisione lasciata aperta in ADR-018 §4
- **Supera, limitatamente al motore:** la clausola di ADR-010 e ADR-011 che designava
  `11-APEX-7-CORE/orchestrator` come unico motore canonico
- **Non tocca:** tutto il resto di ADR-010 e ADR-011, che restano attivi

---

## 1. La domanda era mal posta, e i numeri lo dimostrano

ADR-018 aveva registrato il guasto: due decisioni con lo stesso numero 012, e due motori
di orchestrazione entrambi dichiarati canonici, con la migrazione mai iniziata. Sembrava
una guerra fra due linee rivali.

**Prima misurazione vera, fatta oggi. Quattro fatti, nessuno dei quali era noto:**

| | `11-APEX-7-CORE` (il vecchio canonico) | `orchestration-layer` (di Neri) |
|---|---|---|
| File di codice | **28** | **133** |
| Test | **3** | **24** |
| Ultima modifica reale | **13 agosto** (21 giorni fa) | 26 agosto (8 giorni fa) |
| Dove sta | `11-APEX-7-CORE/orchestrator` | **dentro `11-APEX-7-CORE/`** |

**Il quarto fatto smonta l'accusa principale.** ADR-011 vietava *«nuove linee divergenti
fuori da quella cartella»*. Il lavoro di Neri **non è fuori: è dentro**. Non ha violato il
recinto — è stato innestato esattamente dove il canone diceva di stare. La violazione
formale che ADR-018 aveva registrato **non c'è**, o comunque non è quella.

## 2. Il fatto che chiude la questione

> **Nessuno script di Digital Empire chiama nessuno dei due motori.**

Verificato oggi cercando in `scripts/`, `.claude/skills/`, `.claude/agents/`: le uniche
citazioni di entrambi stanno nei documenti di memoria — checkpoint, ADR, indici. **Mai
nel codice che lavora.**

Quindi:

- la «Fase 2 — migrazione consumatori» che ADR-012 dichiarava «NON iniziata» riguarda
  **zero consumatori**. Non era in ritardo: non aveva niente da migrare.
- i due canoni non si contendevano il lavoro dell'azienda. **Si contendevano un trono su
  cui non si è mai seduto nessuno.**
- il conflitto è durato otto giorni senza conseguenze operative perché non c'erano
  operazioni da danneggiare.

**Questo non rende il guasto meno grave: lo rende più istruttivo.** L'azienda ha prodotto
sette linee di orchestrazione, due ADR contraddittori e un numero duplicato **per un
componente che nessuno ha mai chiamato**. Il problema non era scegliere il motore
sbagliato: era costruirne sette senza che uno solo servisse un lavoro vero.

---

## 3. La decisione

**`company/Ecosistemi/11-APEX-7-CORE/orchestration-layer/` è il motore di orchestrazione
canonico di Digital Empire.**

Ragioni, tutte misurate oggi e nessuna di gusto:

1. **Cinque volte più codice** (133 file contro 28)
2. **Otto volte più test** (24 contro 3)
3. **Sta già dentro l'ecosistema canonico**: nessuna violazione territoriale da sanare
4. **È il più recente**, e l'unico dei due con contratti, politiche di accesso, ripristino
   e documentazione operativa scritti

`11-APEX-7-CORE/orchestrator` e `11-APEX-7-CORE/orchestration` **restano dove sono, come
archivio storico**. Non si cancellano: contengono il lavoro di censimento di ADR-010 e
ADR-011, che è la ragione per cui oggi sappiamo che le linee erano sette.
**Ma non sono più il canone, e nessun lavoro nuovo parte da lì.**

### La Fase 2 è dichiarata conclusa
Non perché sia stata eseguita, ma perché **non aveva oggetto**: zero consumatori da
migrare, verificato. Lasciarla aperta come debito sarebbe tenere in vita un compito
immaginario.

---

## 4. LA CONDIZIONE — e questa vale più della scelta

Il motore vince oggi su 133 file e 24 test. **Ma 133 file che nessuno chiama non sono un
motore: sono un progetto.**

> **Entro il primo lavoro reale di Digital Empire che ha bisogno di orchestrazione, il
> motore canonico deve servirlo davvero.** Se quel lavoro arriva e viene fatto a mano, o
> con un altro strumento, o non arriva affatto entro tre mesi, questo ADR va riaperto —
> e la domanda diventa un'altra: *l'Impero ha davvero bisogno di un motore di
> orchestrazione, o ne ha costruiti sette perché era più divertente che pubblicare?*

Non è una provocazione. È la stessa legge di ADR-016 applicata al codice:
**un componente non è "fatto" finché non serve qualcosa.**

---

## 5. Cosa va detto a Neri — e come

Il lavoro di Neri **vince**, e vince sui numeri, non per cortesia. Va detto così, perché è
vero e perché è la prima volta che un suo lavoro diventa il canone dell'Impero.

Vanno dette anche le due cose vere che lo accompagnano, senza ammorbidirle:

1. **L'ADR che ha scritto dichiarava da sé di contraddire i due precedenti.** Quella
   onestà è esattamente il comportamento che vogliamo — ha lasciato la prova del conflitto
   nel testo invece di nasconderla. **Il difetto non è suo: è dell'Impero, che non aveva
   nessun organo capace di accorgersene.** `sentinel-drift` esisteva ed era un file da 39
   righe senza dentro l'elenco degli ADR da far rispettare. Se n'è accorto solo il giorno
   in cui gli è stato dato il regolamento da leggere.
2. **Il numero duplicato va sanato** (voce B-046), a mano, un puntatore alla volta.

---

## 6. Conseguenze

**Buone**
- un solo canone, scritto, con la ragione misurata accanto
- il debito immaginario della Fase 2 sparisce
- il lavoro migliore vince, e il criterio è pubblico: codice e test, non anzianità
- l'archivio storico resta consultabile

**Costi e rischi**
- **ADR-010 e ADR-011 vanno letti insieme a questo**: la loro clausola sul motore è
  superata, il resto no. Chi legge solo quelli prende una decisione vecchia.
- **Il rischio vero non è tecnico**: è che l'Impero continui a costruire motori che
  nessuno chiama. La condizione del §4 esiste per questo.
- **Nessuno dei due motori è mai stato messo alla prova su un lavoro vero.** La scelta è
  fatta sui migliori dati disponibili, che non sono dati di esercizio.

---

## 7. Il principio, oltre questo caso

> **Un canone senza consumatori non è un canone: è un'opinione con un numero d'ordine.**

Prima di dichiarare qualcosa «ufficiale» in Digital Empire, va chiesto **chi lo chiamerà
lunedì**. Se la risposta è nessuno, non serve un ADR: serve un consumatore, o serve
smettere.

---

*Legami: [[ADR-010]] · [[ADR-011]] · `ADR-012-orchestration-layer-canonico` ·
[[ADR-016]] · [[ADR-017]] · [[ADR-018]] · `company/Memory/BACKLOG.md` voci B-046, B-047*
