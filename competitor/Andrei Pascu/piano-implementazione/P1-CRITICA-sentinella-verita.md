# P1 — CRITICA DELLA SENTINELLA DELLA VERITÀ

**Giro:** P1 (attacca i due DRAFT V1, non lo studio originale)
**Autore:** Sentinella (sonnet), angolo «il denaro e la verità»
**Data:** 2026-09-10
**Bersagli:** `DRAFT-V1-A-lanci.md` (27 azioni) e `DRAFT-V1-B-capacita.md` (4 verdetti)
**Nota:** la Sentinella gemella (angolo governo/coerenza/collisione) è stata persa con la chiusura
della chat — va rilanciata. Prompt in `company/Memory/riprese/EMP-APPLAN1.md`.

---

## LA CONTA

Contando ogni sotto-azione realmente distinta (non le etichette aggregate), il totale reale è **33**,
non «27+4=31». Primo difetto già qui: **Draft A dichiara «23 nuove» in Famiglia B ma i suoi stessi ID
(AP-034→044 = 11, AP-046b/047b/048b = 3, AP-050→060 = 11) sommano a 25.**

| Classe | N | % |
|---|---|---|
| **EURO DIRETTO** | **0** | **0%** |
| ABILITA UN EURO | 6 (di cui 3 dichiarate deboli/condizionali dagli stessi autori) | 18% |
| SOLO INFRASTRUTTURA | 17 | 52% |
| SOLO DOCUMENTO | 10 | 30% |

Le 6 «abilita un euro»: AP-004 (ancoraggio), AP-005 (countdown, il draft stesso lo dice «prima della
firma è aria»), AP-046b e AP-047b (condizionali), AP-051 (ancora prima del prezzo), AP-054
(l'obiezione mai nominata).

**Zero azioni su 33 producono un euro da sole.** Oltre l'80% del piano combinato (28-46h + 3h20-4h20)
è infrastruttura o documentazione che non tocca l'unica transazione che l'azienda deve ancora fare
per la prima volta nella sua storia.

---

## IL PIANO HA LO STESSO MALE CHE DENUNCIA? — SÌ

Entrambi i draft citano ULTIMO METRO per **bocciare le idee altrui**:
- Draft B §3.3, contro AP-006: *«È ULTIMO METRO travestito da progresso: fabbricare il pezzo 26 mentre 25 marciscono.»*
- Draft B §5.3, contro AP-018: *«Aggiungere il pezzo 26… è il fallimento documentato dall'ADR-016, ripetuto con più stile.»*

Nessuno dei due applica lo stesso esame alla propria produzione. Il rango 1 di Draft A (AP-034) è
**uno script nuovo** — esattamente la categoria che ULTIMO METRO dichiara non essere il collo di
bottiglia (*«la macchina produce benissimo… il problema è che nessuno guardava»*). Il 52% del piano è
infrastruttura: roba che si aggiunge al mucchio delle cose costruite, non a quello delle cose vendute.

Il Manuale Claude Code è fermo dal **07/03/2026** (verificato: `ADR-025-ecosistema-lanci.md:23`,
*«È fermo, senza essere venduto, da: il 07/03/2026 — sei mesi»*). **È di fatto il pezzo numero 26.**
Un piano di 31-50 ore che gli costruisce attorno tredici artefatti di governo e non gli costruisce un
bottone di pagamento è la stessa malattia con un vestito più elegante.

Nota: ULTIMO METRO fu misurato il 2026-09-03 (25 pezzi, il più vecchio da 135 giorni). Oggi sono
**142+ giorni**, non 135.

---

## LE STIME SMONTATE

**AP-034 (`catena.py`), dichiarato 4-8h → realistico 8-16h.**
Confronto sul disco: `canone_sync.py` = 96 righe, `galleria.py` = 226, `valida_registro.py` (832
controlli) = 569. `catena.py` deve fare 8 controlli eterogenei, due dei quali (7: prezzo vs testo di
servizio; 2: soglia accento) richiedono **Playwright che legge stili calcolati** — decidere
programmaticamente quale elemento del DOM è «il corpo del prezzo» su markup variabile è
risoluzione-ambiguità, non scrittura di codice.
Il draft stesso (§10 punto 4) ammette che serve una **taratura anti-falsi-positivi sulle 52 pagine
già catturate prima di collegarlo al gate** — e quelle ore **non sono assegnate da nessuna parte**.
Stima ottimistica di circa il 100%, con il motivo già scritto dall'autore.

**AP-008 (7 fattori):** §10 punto 2 ammette il rischio «se compilare `transizioni[]` supera 30 minuti
va reso opzionale» — zero ore assegnate, annegato nel generico 10-16h di S3.

**Draft B, 3h20-4h20:** tre buchi auto-dichiarati e non sottratti dal totale — (1) due file di
convenzioni mai letti per intero, ma leggerli è precondizione per decidere dove scrivere le patch;
(2) **zero minuti per verificare che le patch funzionino** (sono istruzioni per agenti LLM, non
codice deterministico: scriverle non è confermare che un agente rifiuti davvero un brief incompleto);
(3) la Lezione 12 di cs2online non ingerita potrebbe ribaltare il NO-GO su AP-006, e chiudere quel
buco non è nel conto.

**Il pattern comune:** entrambi contano il tempo di scrittura, non quello di verifica.

---

## I NUMERI NON DICHIARATI

### 1. La fascia 27-47 € del Manuale (Draft A §3.2) — il ritrovamento più grave

Verificato con grep su tutto `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/`: «27» e «47» insieme compaiono
**solo** in `_v3-superata/04-WF-OFFERTA.md:146-169` — **un documento che il governo stesso ha
dichiarato superato**. Draft A riprende quei due numeri senza citare la fonte e senza dire che viene
da un piano demolito.

E soprattutto: **esiste già una decisione firmata che nessuno dei due draft cita.**
`DIGITAL-EMPIRE/00-MEMORY/decisions/DEC-EST-001-b-003-prezzo-manuale-claude-code-sblocco.md`
(2026-07-21, passata per silenzio-assenso) fissa **67 € lancio / 97 € listino**. Ed è **già live nel
codice**: `Crea siti/Siti CCM/checkout.config.json` → `"prezzo_lancio_eur": 67`,
`"prezzo_listino_eur": 97`, `"bump_eur": 27`. È il prezzo che la pagina di vendita reale
(`pagamento.html`) mostrerebbe oggi a un visitatore vero.

Quindi i prezzi in circolo non sono quattro come dice ADR-025: sono **almeno cinque** (catalogo «NON
LO SO», wiki 297-497, v3 superata 47/27, DEC-EST-001 67/97, listino), e Draft A ne aggiunge
silenziosamente una sesta pescata dal documento bocciato — proprio nella sezione che si vanta di
costare «zero amendment». Viola la regola scritta nello schema su cui scrive
(`offerta.schema.json:26`): *«Un prezzo proposto senza guardare i prezzi che l'azienda si è già data
non è istruito: è inventato con più pagine.»*

### 2. Il valore 100 € dell'opzione futura (AP-033)
Nessuna fonte, nessuna derivazione, nessun flag — e la stessa azione è ossessionata dal non far
entrare bonus inventati nel valore dichiarato.

### 3. Le soglie 150/400 € (AP-041)
I dati misurati sono tre punti: 98€→0 fonti, 400€→2, 999€→5. **150 non coincide con nessun punto
misurato** e non ha derivazione mostrata — eppure fa un lavoro concreto: decide che il Manuale non ha
bisogno di prove esterne.

### 4. Il tetto di 3 rami per sequenza (Draft B §4.4)
Attribuito a KA-07, ma la descrizione originale di KA-07 nella stessa tabella non contiene **nessun
numero**. Draft B ha un proprio marcatore per le aggiunte non-in-fonte (`➕`, usato correttamente due
righe sopra) e qui non lo applica: viola il proprio standard dichiarato.

---

## IL BUCO — quello che nessuno dei due draft ha guardato

**Digital Empire ha già sul disco, funzionante, il pezzo di incasso più vicino a partire — e nessuna
delle 33 azioni lo tocca.**

`PIANO-MAESTRO/29-ECOSISTEMA-LANCI/_critica-v3/INCASSO.md` (esiste, non citato in nessuno dei due
draft) conclude: *«Digital Empire può oggi, al massimo, ricevere un ordine per email e consegnarlo a
mano — non esiste un solo percorso automatico, collaudato e misurato che porti da "qualcuno vede una
pagina" a "un euro è arrivato".»*

Ma trova anche **due pezzi già costruiti e mai collegati**:

1. **`empire/tools/checkout.py`** — 375 righe di codice reale, legge
   `Crea siti/Siti CCM/checkout.config.json`: prezzo già impostato (67/97 €), quattro rail di
   pagamento già previsti (`stripe_base`, `stripe_bump`, `paypal_me`, `bonifico`), tutti
   `"attivo": false` tranne il fallback email. Il campo dice letteralmente
   `"richiede": "MAX: crea Payment Link su Stripe"` — **un'azione umana da dieci minuti, non una build.**
2. **`KDP - prodottti digitali/Leanding Page/email-agent/main.py`** — 81 righe, webhook FastAPI
   **reale e funzionante**: verifica la firma Stripe e su `checkout.session.completed` consegna un PDF
   via Gmail SMTP. Ha già una `STRIPE_SECRET_KEY` **live** nel `.env` (per un ebook diverso). È
   esattamente il pattern Stripe→consegna-automatica che AP-034/AP-057 provano a *garantire con un
   gate*, già scritto per un fratello del Manuale.

Collegarli (puntare `checkout.py` a un Payment Link vero, adattare `main.py` per consegnare il
Manuale) è lavoro di **poche ore**, non 28-46. ADR-003 («wrap, mai riscrittura») viene applicato da
Draft A al funnel morto di Mastery (AP-056) ma non al pattern di incasso già vivo.

**E si aggancia a una lezione dello studio che nessuno ha elevato a livello strategico:**
`SINTESI-METODO.md` §1/§7 — il negozio di Andrei (44 pagine, permanente, *«non si tocca… resta in
vendita per anni»*) è il motore vero; il lancio è un evento periodico **sopra un negozio già acceso**.
Digital Empire sta facendo il contrario: costruisce l'apparato del lancio (13 artefatti, 15 agenti,
un validatore da 832 controlli) **prima** di avere un negozio minimo sempre acceso.

---

## L'ORDINE GIUSTO — `catena.py` al rango 1 è sbagliato

Il governo lo dice più chiaramente del piano stesso.
`TASK-GAEL-20260908-SETTIMANA-03.md:74-78`: *«**Ordine non negoziabile (decisione 6 di ADR-025)**: il
primo giorno è la catena dell'incasso, non la cartella. Prima di scrivere un agente: sostituire la
chiave di posta esposta (B-020), collegare una cassa vera, incassare un pagamento di prova con una
carta vera, farsi consegnare il prodotto senza intervento umano, rimborsare, e vedere l'evento in un
pannello.»*

Un gate che verifica che i link non portino a un 404 protegge un percorso di incasso che **non esiste
ancora**. Verificare l'ultimo miglio di un viaggio mai partito è precisione sprecata sul problema
sbagliato.

**Rischio attivo non nominato da nessuno dei due draft:** `BACKLOG.md` righe 42-45 — **B-020, la
chiave Brevo in chiaro su repo pubblico, non ruotata da mesi**, marcata «🔴 subito» e riconfermata la
più urgente nella TASK-GAEL di oggi. Nessuna delle 33 azioni la tocca.

### La sequenza proposta

1. **Rotazione chiave Brevo (B-020)** — rischio di sicurezza attivo, cresce ogni giorno.
2. **Payment Link Stripe reale + adattare `email-agent/main.py` per il Manuale** — usa codice già
   scritto e funzionante. Poche ore. Non presente in nessuna delle 33 azioni.
3. **Chiudere per davvero PU-PREZZO** — non «27-47 €» pescato da un piano morto, ma riconciliazione
   vera delle almeno cinque cifre in circolo, con Max che firma UN numero.
4. **AP-054** (l'obiezione «è gratis nella documentazione») — economico, reale, misurato su un
   concorrente diretto.
5. **AP-004**, limitato al testo di ancoraggio (il numero è già coperto al punto 3).
6. **Solo ora AP-034/`catena.py`** — a quel punto c'è davvero un percorso di incasso da proteggere.
7. **Tutto il resto** in `BACKLOG.md`, dove ADR-005 dice che deve stare.

---

## L'OBIEZIONE PIÙ FORTE

> Due Doom Bot hanno prodotto 861+493 righe, 33 sotto-azioni e una stima combinata di 31-50 ore per
> costruire gate, schemi e articoli di legge attorno a un lancio che ancora non può accadere —
> mentre a due cartelle di distanza un audit già scritto (`INCASSO.md`) e due file di codice già
> funzionanti (`checkout.py`, `email-agent/main.py`, con chiave Stripe **live**) mostrano che il modo
> più veloce per far incassare a Digital Empire il suo primo euro di sempre è **collegare due pezzi
> che esistono già**, in ore, non in 28-46. Nessuno dei due draft li cita. Un piano che si chiama
> «chirurgico» e «verificato sul disco» e non trova, sullo stesso disco, il pattern di incasso più
> vicino a funzionare che l'azienda possiede, non ha guardato abbastanza a fondo prima di scrivere
> 27 azioni su tutt'altro.
