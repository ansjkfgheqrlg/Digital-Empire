---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #site-study #lanci #post-acquisto #member-area #copy-teardown
Created: 2026-09-09
Last updated: 2026-09-09
---

# STUDIO SITO 59 — armageddon-dashboard (cosa vede chi ha già pagato)

**URL:** https://www.andrei-copy.com/armageddon-dashboard
**Titolo:** `AP Formazione` · **lang:** non dichiarato
**Meta:** nessuna description, `og_title: "AP Formazione"` (generico, non specifico del pacchetto)
**Altezza:** 1.918px desktop · **Blocchi:** 39 · **CTA:** 5 · **Media:** 10
**Costruzione:** **Squarespace nativo** (Member Areas) — diverso da `armageddon.bsns.it`, che è artigianale
**Catturato:** 2026-09-09 — cattura fuori onda, arrivata dopo la chiusura 56/56 dello studio
**Fonti grezze:** `capture/59-armageddon-dashboard/`

> **È la pagina che lo studio non aveva mai visto: cosa succede DOPO il clic sul link Stripe.**
> Le 56 pagine chiuse coprivano il funnel fino alla cassa. Questa è la prima e unica cattura del
> lato consegna — e usa un meccanismo completamente diverso (Squarespace nativo, non il mirror
> artigianale) da tutto il resto del lancio.

---

## 1. COSA C'È IN PAGINA — un paywall nativo di Squarespace, non un mirror

A differenza delle cinque pagine di `armageddon.bsns.it` (artigianali, vanilla, zero piattaforma),
questa vive su `andrei-copy.com` — il negozio storico — e usa il blocco **Member Areas** di
Squarespace: stesso meccanismo con cui probabilmente consegna tutti i suoi prodotti digitali.

| # | Elemento | Misura |
|---|---|---|
| 1 | Titolo | «Ti diamo il benvenuto su Armageddon Bundle» — 48px/700 |
| 2 | Sottotitolo | «Questa pagina è disponibile solo per i membri.» |
| 3 | Nome prodotto nella card | «Armageddon Bundle» |
| 4 | Prezzo | **199,00 €** — 35,2px/300, identico al prezzo del lancio |
| 5 | Condizione | «Una tantum» — stesso pattern lessicale della pre-cassa (report ATLANTE 30-42) |
| 6 | Bottone primario | «Iscriviti» — bg `#1b1b1d`, testo `#a8a8a8` 16px/600 |
| 7 | Bottone secondario | «Accedi» (in header) — stesso stile |
| 8 | Riga di valore | «Accesso istantaneo a 4 corsi di Andrei Pascu. Sconto di €199 su Funnel Operator alla sua uscita.» |
| 9 | Checklist contenuti | ✓ outFunnel · ✓ outHeadline · ✓ outEmail · **✓ outViral 2** |

**«outViral 2»**, non «outViral»: prima conferma diretta che il prodotto ha una versione 2 in
consegna, misurata qui e da nessun'altra parte nello studio.

---

## 2. LA SCOPERTA CHE CHIUDE UN BUCO: lo sconto sul prodotto che non esiste ancora

> *«Accesso istantaneo a 4 corsi di Andrei Pascu. Sconto di €199 su Funnel Operator alla sua
> uscita.»*

**Funnel Operator non è uscito.** Chi compra Armageddon oggi non riceve solo quattro prodotti
finiti: riceve anche uno **sconto bloccato su un quinto prodotto futuro**, dello stesso valore del
pacchetto intero (199 €). È una leva che le 56 pagine del funnel pre-cassa non mostrano mai — vive
solo qui, nella pagina che il cliente vede a pagamento avvenuto.

**Perché è rilevante per LANCI:** è un meccanismo diverso dal voucher-specchio (Parte IV
dell'anatomia, «il regalo vale quanto il prezzo»). Qui il regalo non è un buono spendibile subito,
è **uno sconto opzionato su un lancio che ancora non esiste** — costo zero per lui oggi, e un
motivo concreto per restare sulla sua lista finché quel prodotto non nasce. Un secondo modello di
regalo, da aggiungere accanto al voucher nel nostro catalogo di leve.

---

## 3. IL DIFETTO CHE UNO STUDIO DI PIXEL PUÒ VEDERE E UN CLIENTE NO

Sopra la card prezzo, in basso a sinistra, un banner realmente in produzione:

> **«Stiamo aggiornando il brand»** — «Potresti trovare colori strani, font sbagliati, o simili.» —
> bottone **«Capito»**, unico elemento della pagina nel blu di brand `#0062ff`.

**Un cliente che ha già pagato 199 € apre la pagina di consegna e la prima cosa che legge è un
avviso di manutenzione del brand**, non un benvenuto. Ed è proprio qui — non nella card prodotto —
che compare l'unico uso del colore `#0062ff` di tutta la pagina: **il colore di brand è speso per
scusarsi del brand**, non per vendere o per accogliere. È l'inverso esatto della gerarchia
tipografica già misurata nel lancio (Parte IV, controllo 7: la cifra pagata è il testo più
piccolo) — qui è l'accento più curato ad andare al messaggio meno importante della pagina.

Il bottone «Iscriviti», quello che davvero converte, è grigio su nero (`#a8a8a8` su `#1b1b1d`):
**zero contrasto di brand sulla sola azione che conta in questa pagina.**

---

## 4. DIFETTI REALI

1. **Il messaggio di sistema (aggiornamento brand) sovrasta il messaggio commerciale** nella
   gerarchia cromatica — unico uso del blu di brand è su "Capito", non su "Iscriviti".
2. **`og:title` generico** («AP Formazione»): chi condivide il link di consegna non vede il nome
   del pacchetto comprato.
3. **Nessuna `meta description`**: stesso buco già misurato altrove nell'ecosistema.
4. **Il link "Recensioni" nel piede punta ancora a `/presto-disponibile`** — lo stesso dead-end
   già trovato nelle quattro pagine-ponte (report macchina-del-funnel): qui è confermato che il
   dead-end non è un incidente locale, è nel **footer standard del sito**, quindi si propaga
   ovunque quel footer sia incluso.
5. **Segmentazione a 1 sola sezione**: la pagina è un contenitore Squarespace unico, coerente con
   un blocco nativo (Member Area), non con una pagina costruita a sezioni come il resto del sito.

---

## 5. COSA NE FACCIAMO IN DIGITAL EMPIRE

1. **Il pattern `pre-cassa` (dodici passi, Parte IX dell'anatomia) copre fino al pagamento. Manca
   ancora il gradino successivo**: la pagina di consegna/accesso. Questa cattura dice cosa NON
   fare lì — messaggi di sistema mai sopra il messaggio di benvenuto, CTA di consegna sempre nel
   colore di brand, mai nel grigio neutro.
2. **Lo sconto-su-prodotto-futuro è una leva aggiuntiva da mettere nel catalogo**, distinta dal
   voucher-specchio: costo marginale zero, tiene il cliente in attesa del prossimo lancio.
3. **Verificare footer condivisi prima di ogni lancio** (controllo 8 del gate, esteso): un link
   morto nel footer standard si propaga a ogni pagina che lo include, consegna compresa — non
   basta controllare le pagine del funnel, va controllato il footer una volta sola alla fonte.

---

## Connessioni

- [30-44-macchina-della-cassa-ATLANTE.md](30-44-macchina-della-cassa-ATLANTE.md) — lo stampo di
  pre-cassa che precede questa pagina
- `../ANATOMIA-DEI-LANCI.md` — Parte IV (leve dell'offerta) e Parte X (cosa consegniamo a LANCI):
  questa cattura riempie il gradino "dopo il pagamento" che il documento dichiarava non coperto
- `../anatomia_lanci.py` — `CONSEGNA_A_LANCI` aggiornata con questo pattern
- [40-43-44-pagine-anomale.md](40-43-44-pagine-anomale.md) — altri dead-end dello stesso footer
