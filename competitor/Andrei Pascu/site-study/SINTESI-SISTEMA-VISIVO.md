---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #sistema-visivo #sintesi #onda-g
Created: 2026-09-09
Last updated: 2026-09-09
---

# SINTESI DEL SISTEMA VISIVO — 52 pagine, contate a macchina

**Primo documento dell'onda G.** Costruito come impone il Passo 4 del dossier 33: **dai
`scheda.json`, non rileggendo le prose.** Il calcolo sta in `scripts/sintesi_visiva.py` e si
rifà a comando — questo documento è la lettura, non la fonte.

---

## 1. DUE MONDI, NON UNO

| Costruzione | Pagine | Altezza media | Keyframes medi | **Media per 1.000 px** |
|---|---|---|---|---|
| **Squarespace** — il negozio | **44** | 9.081 px | 28,3 | **4,8** |
| **Artigianale** — lanci e agenzia | **7** | 14.118 px | 15,6 | **1,2** |

**Il numero che conta è l'ultimo: quattro volte meno immagini per pagina.** Dove costruisce a mano,
riempie con **il testo e la composizione**; dove sta sulla piattaforma, riempie con **le immagini**.
E lo fa su pagine più alte del 55%, con **la metà delle animazioni** — perché Squarespace ne porta
63 di serie che lui le usi o no, mentre a mano ne sceglie 9, 34, 39.

> La disciplina non è una qualità del suo gusto: è una conseguenza di dove costruisce.
> Sulla piattaforma il costo di aggiungere un'immagine è zero, e infatti ne aggiunge quattro volte
> tante.

---

## 2. COSA FA SEMPRE

| Tratto | Misura |
|---|---|
| Fondo di pagina | `#a8a8a8` su **35 pagine su 52** |
| Colore del testo | `#fafafa` su **42**, secondo tono `#ebe9e0` su **41** |
| Scuro di appoggio | `#1b1b1d` su **25** |
| Carattere dichiarato | **`sans-serif` su 38 pagine su 52** |

**L'ultima riga è la scoperta di questa sintesi.** Su tre quarti dell'ecosistema **non dichiara un
caratteredel tutto**: prende quello che passa il browser. Un copywriter che vende corsi di scrittura
non ha un'identità tipografica sul proprio negozio.

Dove invece costruisce a mano, il carattere c'è ed è scelto: `Elza, Inter, ui-sans-serif` su 5
pagine, `Inter` su 3. **Cinque pagine su cinquantadue hanno una voce tipografica.** Sono le sue.

---

## 3. COSA NON FA MAI

- **Non dichiara un carattere proprio sul negozio** (38/52 a `sans-serif`).
- **Non usa più di due neutri**: fondo grigio, testo quasi bianco, secondo tono osso. Il resto è
  accento.
- **Non anima le pagine che vende a mano oltre l'indispensabile**: 15,6 keyframes medi contro 28,3.
- **Non cambia guscio fra le pagine di uno stesso sito**: cambia solo l'accento, e cambia per
  prodotto.

---

## 4. IL PREZZO NON GOVERNA LA PAGINA — correzione a una nostra affermazione

Un rapporto precedente, misurato su **tre** pagine, concludeva che salendo di prezzo la pagina si
carica (densità 2,9 → 3,6 → 7,6). Con **dieci** pagine a prezzo noto, la relazione **non regge**:

| Pagina | Prezzo | Altezza | Sezioni | Blocchi | Media/1.000px |
|---|---|---|---|---|---|
| `04-outfunnel` | 98 € | 26.993 px | 24 | 215 | 4,1 |
| `03-outheadline` | 98 € | 21.119 px | 19 | 315 | 3,7 |
| `21-outemail` | 139 € | 26.032 px | 24 | 259 | 3,8 |
| `11-armageddon` | 199 € | 5.103 px | 4 | 53 | 1,6 |
| `12-claude-speedrun` | 249 € | **33.756 px** | 34 | 473 | 1,9 |
| `23-vendita` | 400 € | 14.905 px | 18 | 185 | 5,3 |
| `02-funnel-operator` | 434 € | 24.019 px | 28 | 340 | 3,6 |
| `05-copy` | 999 € | 26.952 px | 28 | 470 | 6,8 |

**Il prodotto da 98 € e quello da 999 € hanno praticamente la stessa altezza** (26.993 contro
26.952 px), e la densità del 98 € (4,1) supera quella del 434 € (3,6). **Quello che sale col prezzo
non è la lunghezza: è la densità di prova** — e infatti il 999 € è il più denso di immagini (6,8) e
l'unico con listino a due livelli.

**La pagina più grande dell'ecosistema non è la più cara**: è `claude-speedrun.com` a 249 € —
33.756 px, 34 sezioni, 473 blocchi, **40 CTA**. È anche l'unica sua pagina che compete direttamente
col nostro Manuale Claude Code, ed è quella su cui ha speso più lavoro di tutte.

---

## 5. LA TEMPERATURA DEL TRAFFICO GOVERNA TUTTO IL RESTO

| | Pagine | Altezza media | Blocchi medi | CTA medie |
|---|---|---|---|---|
| **Gradini** (≤ 2.200 px) | 17 | **1.593 px** | 36 | 4,9 |
| **Pagine di vendita** (≥ 9.000 px) | 25 | **17.531 px** | 252 | 16,2 |

**Undici volte l'altezza, sette volte i blocchi, tre volte le CTA.** Questa — non il prezzo — è la
variabile che decide la forma di una sua pagina: *a che punto del percorso sta il lettore*.

Chi non ha ancora deciso riceve **una sola decisione per pagina** (4,9 CTA, di cui quasi tutte sono
navigazione: la scelta vera è una). Chi sta valutando riceve **sedici occasioni** di dire sì.

---

## 6. LA REGOLA DELL'ACCENTO — vera sul 60%, non su tutto

Misurata su tutte e 52, contando i colori di testo che compaiono **una volta sola** al netto dei
neutri:

| | Pagine |
|---|---|
| Almeno un accento speso **una volta sola** | **31** |
| Nessun accento oltre i neutri | 7 |
| Ogni accento usato più volte | 14 |

La regola scritta in ADR-024 §12 nasce da quattro pagine ed è confermata su **31 su 52**. Le 14
eccezioni sono concentrate dove ci si aspetterebbe: la home, le pagine di negozio, `40-ecco-i-fatti`,
`44-apsales-promozione`. **La disciplina cede dove la pagina serve a navigare, non a decidere.**

Questo non indebolisce §12: la conferma **come regola delle pagine che decidono**, che è esattamente
dove la vogliamo noi.

---

## DELTA ALLA FABBRICA

**CANONE.** Un articolo nuovo da §5: *la forma di una pagina si decide dalla temperatura del
traffico, non dal prezzo del prodotto.* Freddo → una sezione, una decisione, sotto i 2.000 px.
Caldo → lungo quanto serve, con una CTA ogni ~1.100 px (17.531 ÷ 16,2, misurato).
E da §2: **il carattere si dichiara sempre** — un `sans-serif` implicito è un'identità regalata al
browser, e il nostro canone ha già Onest.

**PATTERN.** Niente di nuovo: i pattern estratti (`pre-cassa`, `pagina-ponte`) sono esattamente i
due poli di §5, e questa sintesi li conferma sui numeri di 42 pagine invece che di 4.

**GATE.** Un controllo nuovo, dai dati di §1: **densità di immagini per 1.000 px**. Sopra 5,0 la
pagina si sta riempiendo di figure invece che di argomenti → WARN. Le sue pagine peggiori per
verificabilità (`51-recensioni-mentorship`, 8,1 — 42 screenshot muti) sono anche le più dense.

---

## LE TRE COSE DA RUBARE SUBITO

1. **Un guscio, tanti accenti.** Fondo, testo e secondo tono non cambiano mai in un sito; cambia
   l'accento, e cambia per prodotto.
2. **La pagina fredda è una decisione sola.** 1.593 px, 36 blocchi, un bottone vero.
3. **Una CTA ogni ~1.100 px sulle pagine calde.** Non a occhio: è la sua misura media.

---

## Connessioni
- [[SINTESI-METODO]] · [[SINTESI-SISTEMA-COPY]] — gli altri due documenti dell'onda G
- `scripts/sintesi_visiva.py` — il calcolo, rifacibile a comando
- `company/Memory/decisions/ADR-024-canone-v2-primo-strato.md` — §12 e gli otto controlli
