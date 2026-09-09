---
Type: PROJECT
Status: Active
Tags: #competitor #andrei-pascu #site-study #enumerazione
Created: 2026-09-07
Last updated: 2026-09-07
---

# ECOSISTEMA ANDREI PASCU — l'elenco vero

**Passo 0 del [dossier 33](../../../PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md).**
Non stimato: letto dalle sitemap vive, dalla navigazione e dai link interni delle 10 pagine già in
mano, il 2026-09-07.

---

## ⚠️ IL PIANO PARTIVA DA UN NUMERO SBAGLIATO

Tutto lo studio finora diceva *"l'ecosistema ha almeno 11 pagine"*. Il giro P6 del piano ha imposto
di verificarlo invece di crederci.

| | Si credeva | **È** |
|---|---|---|
| Pagine dell'ecosistema | ~11-12 | **187 URL** |
| Pagine commerciali (non blog) | ~11 | **76** |
| Articoli di blog | 0 conosciuti | ~~105~~ **37** (i 105 contavano gli indici tag/categoria — vedi correzione) |
| Domini | 4 | **7** |
| Pagine catturate | 10 | 10 — **il 13% del commerciale** |

**Avevamo studiato il 13% di ciò che credevamo fosse il 90%.** Se il Passo 0 non ci fosse stato,
avrei chiuso lo "studio totale" con 66 pagine commerciali mai aperte e non l'avrei saputo.

---

## I DOMINI — sette, non quattro

| Dominio | Cosa è | Pagine | Costruzione |
|---|---|---|---|
| `andrei-copy.com` | il negozio storico, l'hub | **165** (61 commerciali + 37 articoli + 67 indici tag/categoria) | **Squarespace** (`static1.squarespace.com`, `sqspcdn`) |
| `apsales.eu` | l'agenzia CRO | **8** | artigianale (design system vero) |
| `apsales.info` | **alias di `apsales.eu`** — stessa sitemap | — | idem |
| `claude-speedrun.com` | il corso su Claude, 249 € | **2** | artigianale, `#fb4604` + Onest |
| `armageddon.bsns.it` | il lancio, 199 € | **5** (home + 4 figlie) | artigianale, vanilla, **studiato** |
| `bsns.it` | **redirige** su `andrei-copy.com` | — | — |
| ~~`chiamata-formazione.netlify.app`~~ | **NON È SUA — È NOSTRA.** Vedi la correzione qui sotto | — | — |
| `linktr.ee/andrei.bsns` | il bio-link | 1 | Linktree stock, **studiato** |

---

## ⚠️ CORREZIONE — gli articoli del blog sono 37, non 105 *(2026-09-09)*

Il Passo 0 dichiarava **105 articoli di blog** e li chiamava *"il suo motore di posizionamento
organico"*. Preso l'elenco dalla sitemap viva e salvato (`capture/_corpus-blog/corpus.json`,
prodotto da `scripts/corpus_blog.py`): **165 URL totali, di cui 37 articoli veri**. Gli altri 67
`/blog/...` sono **pagine di tag e categoria** — indici senza contenuto proprio.

**Il primo giro dello script sbagliava anche lui**, contandoli come articoli: 104 invece di 37, un
errore del 64%. Corretto alla fonte, non solo nel rapporto. E le misure cambiano di segno:

| | prima (falso) | **vero** |
|---|---|---|
| Articoli | 104 | **37** |
| Titoli con un numero | 17% | **41%** |
| Parole per titolo | 3,4 | **7,8** |
| Parola più usata | «online» (21) | **«copywriting» (9)** |

**Cosa cambia per lo studio:** il blog **non è** un motore da 105 pezzi. Sono 37 articoli, con
titoli lunghi e quasi la metà costruiti su un numero. Il gonfiaggio veniva dalle pagine di indice
che Squarespace genera da solo — cioè da un conteggio automatico creduto sulla parola.

## ⚠️ CORREZIONE — una pagina censita nel suo ecosistema era NOSTRA *(2026-09-09)*

`chiamata-formazione.netlify.app` è stata contata per sette giorni come pagina di Andrei Pascu.
**Non lo è.** Catturata e letta: **zero occorrenze** della parola «Andrei» in tutta la pagina, e il
testo dice *«Digital Empire — la mia agenzia, appena nata — sta lanciando Claude Code Mastery»*
`[y=704]`, firmato Max. È **una nostra bozza di funnel** su un dominio Netlify di staging: una call
1:1 gratuita che porta al corso da **397 €**.

**Come c'è finita:** l'enumerazione del Passo 0 ha raccolto i domini dai link, e questo compariva
fra i nostri stessi appunti. Nessuno l'ha aperto: è entrato in elenco per il nome.

**Cosa insegna, e vale più della correzione:** anche l'elenco «misurato» del Passo 0 conteneva un
falso, e il falso è sopravvissuto perché *sembrava plausibile*. **Un URL non è un fatto finché la
pagina non è aperta.** L'errore si è chiuso da solo solo perché l'onda D l'ha catturata davvero.

**Effetto collaterale utile:** quella pagina è comunque materiale prezioso — è la nostra offerta a
impegno alto, mai finita e mai lanciata. Il rapporto
[`reports/40-43-44-pagine-anomale.md`](reports/40-43-44-pagine-anomale.md) la studia lo stesso, e va
girata all'ecosistema **LANCI**: è già un pezzo di funnel scritto, fermo su uno staging.

---

## LA TRIAGE — cinque livelli, perché 187 studi surgical non si fanno

Il piano (P3-A1) impone di ordinare per valore. Ecco l'ordinamento, e la profondità che ognuno riceve.

### T1 — ARTIGIANALI: studio pieno, CSS e JS letti *(10 pagine)*
Qui vive **lo strato 4**: il metodo di costruzione. È dove armageddon ha dato la scoperta più
preziosa dell'intero studio.

| Pagina | Stato |
|---|---|
| `armageddon.bsns.it` | ✅ **studiata a fondo** (rapporto + atlante) |
| `armageddon.bsns.it/outemail` · `/outfunnel` · `/outheadline` · `/outviral` | ⬜ mai viste — **tutte e 4 rispondono 200** |
| `claude-speedrun.com` | 🟡 rapporto vecchio, **CSS/JS mai letti** |
| `apsales.eu` | 🟡 rapporto vecchio, **CSS/JS mai letti** |
| `apsales.eu/servizi` · `/landing-page` · `/consulenza` | ✅ catturate 2026-09-07 (rapporto + teardown di copy) |

### T2 — PAGINE CHE VENDONO su Squarespace: studio pieno meno il CSS di framework *(~9 pagine)*
Il loro CSS è Squarespace: ventimila righe che non insegnano niente. Ma lo **schema**, il **copy**,
la **palette** e gli **effetti scritti a mano** (custom.css) sì.

`/copy` ✅ · `/funnel-operator` ✅ · `/outheadline` ✅ · `/outfunnel` ✅ · `/manuale-del-copywriter` ✅
· `/outemail` 🟡 catturata · `/outviral` 🟡 catturata · `/vendita` 🟡 catturata · `/mpo2` 🟡 catturata

> **⚠️ CORREZIONE DELLA TRIAGE — 2026-09-07, misurata dopo l'Onda B.**
> Quattro pagine che stavano qui **non vendono niente** e sono state spostate in T3:
> `/asa` · `/define` · `/armadeggon-strp` · `/outfunnel-1`.
> Misura: altezza media **1.750 px contro 15.653 px** delle T2 vere, **1 sola sezione**, 28-40
> blocchi di testo contro 132-259. Erano state classificate leggendo i **nomi**, e i nomi mentono
> (`/outfunnel-1` sembra la pagina del prodotto outFunnel: è la sua cassa).
> Rapporto: [`reports/24-25-27-28-macchina-del-funnel.md`](reports/24-25-27-28-macchina-del-funnel.md).

> `custom.css` di Squarespace è pubblico e **scritto da lui**:
> `static1.squarespace.com/static/custom-css/602126db7a4e4c01fd9babb6/...`
> **Quello va letto**: è l'unica parte di questi siti che è sua.

### T3 — LA MACCHINA DEL FUNNEL: schema e copy, niente atlante visivo *(19 pagine)*
Sono i gradini fra una pagina e il pagamento. Il loro valore è **la sequenza**, non l'aspetto.

`/pre-copy` · `/pre-checkout-cm` · `/pre-checkout-cmb` · `/outemail-pre` · `/outheadline-pre` ·
`/vendita101-pre` · `/pre-outviral-shop` · `/stripe-claude-speedrun` · `/presto-disponibile` ·
`/ricevi-email-di-andrei-pascu` · `/ecco-i-fatti-copywriting` · `/aps-assistenza` ·
`chiamata-formazione.netlify.app` · `apsales.eu/promozione`
**+ arrivate da T2 e già catturate:** `/asa` ✅ · `/define` ✅ · `/armadeggon-strp` ✅ · `/outfunnel-1` ✅
**+ trovata studiando:** `/acquista-v101` ⬜ (ci porta `/vendita` a `[y=3219]`, non era in elenco)

> **Scoperta già visibile dai soli nomi:** ogni prodotto ha una pagina `-pre` prima della cassa.
> È un gradino di funnel sistematico che non avevamo mai visto, perché non avevamo mai guardato
> l'elenco delle pagine.
>
> **Confermata sul campo il 2026-09-07** (rapporto `24-25-27-28-macchina-del-funnel.md`): la
> pre-cassa esiste davvero, ha una forma fissa — occhiello «Stai acquistando…», nome del prodotto,
> cifra isolata, «Una tantum», bottone — e **il codice sconto vive lì, non nella pagina di vendita**.
> L'elenco delle pagine `-pre` **non è chiuso**: un solo campione ne ha rivelata una nuova.

### T4 — PROVA, STORIA E NEGOZIO: campione, non tutte *(19 + 6 pagine)*
`/recensioni-andrei-pascu` · `/recensioni-copywriting-mentorship` · `/story` · `/storyvideo` ·
`/risorse` · `/attrezzatura-e-software` · `/negozio` · `/store` · `/store-ap-sales` ·
`/store/aps-store` · `/store/copyexe` · 19 schede `/store/p/*`

Le 19 schede prodotto non si studiano una per una: si studia **il modello di scheda** su tre campioni
(prezzo basso, medio, alto) e si registra la variazione.

### T5 — IL CORPUS DI COPY: 105 articoli, analisi in blocco *(105 pagine)*
Non si fa un atlante visivo di un articolo. Si fa **un'analisi di corpus**: titoli, aperture, formule
ricorrenti, lunghezze, chiusure, e quali articoli portano a quali prodotti.

> Il blog è **il suo motore di posizionamento organico** e non era nemmeno nel nostro elenco.
> `/blog/headline-copywriting-91-tecniche-infallibili-per-il-titolo-perfetto` è, da solo, un
> documento da studiare.

### FUORI — legale e tecnico *(6 pagine)*
`/privacy-dati-cookie-simili` · `/terms-of-service` · `/ai-policy` · `apsales.eu/tos` ·
`claude-speedrun.com/cookie-policy` · `/cart`
Non si studiano per lo stile. **`/ai-policy` sì, ma come contenuto**: è una posizione pubblica
sull'AI da parte di un concorrente diretto su un corso di AI.

### DA CAPIRE — nomi che non si spiegano *(6 pagine)*
`/pagina-gaia-1` · `/pagina-gaia-4` · `/pagina-gaia-5` · `/pagina-per-stupri` ·
`/ouerwigjbopkn4etwbvadsguhjl234qtewqgubio9` · `/home` (doppione di `/`)
Pagine di prova o di lavoro rimaste pubbliche. Si aprono una volta: o sono rumore, o sono un pezzo
di funnel che non capiamo ancora.

---

## IL CONTO DEL LAVORO

| Livello | Pagine | Profondità | Costo relativo |
|---|---|---|---|
| T1 | 10 | piena, con CSS e JS | alto |
| T2 | ~~13~~ **9** | piena meno il framework | medio-alto |
| T3 | ~~14~~ **19** (+4 da T2, +1 trovata) | schema + copy | medio |
| T4 | 25 → **9 studiate** (campionate) | modello + campioni | basso |
| T5 | 105 → **1 analisi di corpus** | corpus | medio |
| Fuori | 6 → **1** (`/ai-policy`) | contenuto | minimo |
| Da capire | 6 | un'apertura ciascuna | minimo |

**Pagine da aprire davvero: ~58.** Di queste, **10 già catturate** e **1 già studiata a fondo**.

---

## L'ORDINE DELLE ONDE — aggiornato ai fatti

| Onda | Cosa | Pagine |
|---|---|---|
| **A** | T1 artigianali: `claude-speedrun`, `apsales.eu` + 3 pagine, le 4 figlie di armageddon | 9 |
| **B** | T2 mai viste: `/outemail`, `/outviral`, `/vendita`, `/asa`, `/define`, `/mpo2`, `/armadeggon-strp`, `/outfunnel-1` | 8 |
| **C** | T2 già catturate: integrazione (sezioni + effetti + schema + copy) sulle 7 vecchie | 7 |
| **D** | T3 la macchina del funnel — **la sequenza, che è la scoperta grossa** | 14 |
| **E** | T4 campioni di prova e negozio | 9 |
| **F** | T5 corpus del blog | 105 → 1 documento |
| **G** | le tre sintesi + la fusione di `empire-premium-style` | — |

---

## STATO — contato sul disco da `scripts/stato_onde.py`

> Non si scrive a mano. Una pagina e' **chiusa** solo con `scheda.json` + rapporto + ATLANTE + COPY.

| Onda | Catturate | Chiuse (4 file) | Attese |
|---|---|---|---|
| Onda A | 9 | 9 | 9 |
| Onda B | 8 | 8 | 8 |
| Onda C | 7 | 7 | 7 |
| Onda D | 15 | 15 | 15 |
| Onda E | 9 | 9 | 9 |
| Onda F | 4 | 4 | 4 |
| Onda G | 4 | 4 | 4 |

## Connessioni
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — il piano, con i sette giri di critica
- `README.md` — lo stato dei rapporti già scritti
- `reports/11-armageddon.md` — il modello di profondità a cui tutte le T1 devono arrivare
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` — dove tutto questo deve finire
