# mirror-di-lancio

**Corsia A** | origine: `competitor/Andrei Pascu/site-study/SINTESI-METODO.md` §3 (misurato su
`armageddon.bsns.it` e le sue quattro figlie, 2026-09-09) e `company/Memory/decisions/ADR-024-canone-v2-primo-strato.md`
§3 (il badge, due usi: `capture/14-arma-outemail` [y=23953] · `capture/17-arma-outviral` [y=1290, y=9408])
| canone: `--u`, `--line-hair`, `--t-62`, `--t-76`, `--orange`, `--orange-bright`, `--ink-2`,
`--radius-sm`, `--measure-body`, `--leading-body`, `--t-base`, `--ease-land`, `.btn` / `.btn-orange`

## Quando
Quando si lancia un pacchetto fatto di prodotti che **esistono già** e hanno già una pagina che
vende. Il mirror prende quella pagina, la rispecchia dentro il lancio, e la ripunta: **un lancio non
richiede di scrivere pagine nuove, richiede di copiare, spogliare e ripuntare** (SINTESI-METODO §3).
È la ragione misurata per cui il concorrente può lanciare spesso — e la ragione per cui possiamo
farlo anche noi senza un cantiere da zero ogni volta.

Tre mosse, sempre le stesse:
1. **si spoglia** — via gli script della piattaforma, i widget, il carrello del negozio;
2. **si sostituisce** — il bottone-prezzo del prodotto singolo diventa il badge di inclusione;
3. **si ripunta** — tutte le figlie a **una sola** cassa, da **un solo** dato in pagina (§8).

## Quando NO
- **Se il prodotto non ha già una pagina che vende.** Il mirror rispecchia: senza originale non c'è
  niente da rispecchiare, e quella che si scrive non è un mirror, è una pagina di vendita nuova.
- **Se il prodotto resta acquistabile da solo al suo prezzo durante la finestra.** Allora il badge
  mente: dice «incluso» a chi può ancora comprarlo separatamente, e il lettore trova due prezzi per
  la stessa cosa. O si toglie il prodotto singolo dalla vendita per la durata del lancio, o non si
  usa questo pattern.
- **Se il pacchetto ha più di una cassa** (una per fascia, una per paese, un piano rateale). Qui
  «una sola cassa» non è una preferenza: è ciò che rende il mirror una freccia. Più casse sono una
  pagina di scelta, che è un altro pattern.
- **Se il lancio dura più della vita del contenuto.** Il mirror va **mantenuto** finché la finestra
  è aperta (vedi il difetto sotto): se la finestra è lunga come la vita del negozio, si sta
  duplicando il negozio, non lanciando.

## Le cose che si dimenticano sempre
1. **Il canonical.** Un mirror è una copia parola per parola di una pagina già indicizzata. Senza
   `<link rel="canonical">` verso l'originale, le due pagine competono fra loro nell'indice e
   vincono entrambe di meno. Il mirror serve a vendere dentro una finestra, non a posizionarsi:
   **questa è una scelta di Digital Empire**, non una misura presa da lui.
2. **Aggiornare solo la copia.** È il difetto misurato, ed è quello che uccide il metodo dall'interno:
   vedi sotto. La regola operativa è una sola — **si modifica l'originale, il mirror si rigenera**.
   Mai il contrario, mai «tanto è solo per tre settimane».
3. **Scrivere l'indirizzo della cassa in più di un posto.** Quattro figlie × tre bottoni = dodici
   punti in cui sbagliare un URL. Il pattern lo tiene in una riga sola: un indirizzo sbagliato resta
   sbagliato in un posto solo, e si vede su tutte e quattro le pagine insieme invece che su una.
4. **Lasciare il prezzo del prodotto singolo da qualche parte nel corpo** (nella FAQ, in una
   didascalia, nel testo «di solito costa X»). Il badge sostituisce **il bottone-prezzo**, ma se la
   cifra sopravvive più in basso il lettore ha di nuovo due numeri: §8, un dato solo.
5. **Ereditare gli script della piattaforma «per non rompere niente».** Sono esattamente il peso che
   il mirror esiste per togliere — e sono ciò che tiene la pagina fuori dal tetto di 250 KB della
   Corsia A (`canone.json`, gate `9_peso`).

## La composizione
Il corpo della pagina **non si disegna**: è quello dell'originale. Il pattern disegna solo i tre
pezzi che il mirror aggiunge o sostituisce, e li tiene dentro la colonna `min(760px, 100%)` — la
stessa di `pagina-ponte`, perché il compito è lo stesso: portare, non convincere.

| Elemento | Origine | Misura reale | Frazione applicata |
|---|---|---|---|
| Badge di inclusione | `14-arma-outemail` [y=23953], `<p>` maiuscolo w700 | 15,2 px | `--u * 0.0105556` |
| Titolo del prodotto | stessa taglia di `pagina-ponte` (`/define`, `/asa`) | 60,8 px | `--u * 0.0422222` |
| Nastro d'origine e barra | scala di servizio del canone | 15 px | `--u * 0.0104167` |

**Il colore del badge.** Il suo è `#bc0807`, e la misura che conta non è il rosso: è che
**quell'hex compare nella pagina solo due volte, sul badge e sulla barra d'acquisto, e su
nient'altro** (ADR-024 §3). Il colore fa da filo fra «questo è incluso» e «compra qui». Qui il filo
è `--orange`: §1 dice che il canone vince sul gusto, e vince anche quando il gusto è quello del
concorrente studiato. §12 resta rispettato — un accento, **uno scopo**, due punti dello stesso
gesto.

**Il JavaScript è facoltativo per comprare.** Gli `href` statici restano scritti nell'HTML: se lo
script non gira, la barra è visibile e il link funziona. Lo script fa due cose sole — allineare
tutti i `[data-cassa]` a un dato solo, e far entrare la barra dal basso per chi non ha chiesto meno
movimento (§7).

## Lo standard di scrittura
**Originale** (badge, `14-arma-outemail`): *«INCLUSO NEL PACCHETTO ARMAGEDDON»* — maiuscolo, tre
parole più il nome, nessun verbo. Il meccanismo: non convince e non spiega, **riclassifica**. La
pagina che stavi leggendo come prodotto diventa, in una riga, un pezzo di qualcos'altro.

**Placeholder:** *«INCLUSO NEL PACCHETTO [NOME]»* — la struttura non si tocca. Cambia solo il nome
del pacchetto, e il nome del pacchetto è lo stesso identico che sta sulla pagina madre e sulla
cassa: tre nomi diversi per la stessa offerta sono tre offerte, per chi legge.

**Nastro d'origine — nostro, non suo.** *«Stai leggendo la scheda di uno dei corsi inclusi in
[PACCHETTO]. Il pacchetto si compra una volta sola, da un solo posto.»* Stessa forma della
riaffermazione di `pre-cassa` (*«Stai acquistando…»*): si dichiara **dove sei**, non si ricomincia a
vendere. La seconda frase è quella che previene la domanda che il badge apre da solo — *«e allora
quanto costa questo?»* — prima che il lettore la faccia.

## Il difetto da non copiare
**Il mirror non è congelato: è mantenuto — e viene mantenuto solo lui.** Misura del 2026-09-09
(SINTESI-METODO §3): la pagina prodotto originale sul negozio dice *«E adesso, nel **2025**…»*,
mentre la sua copia di lancio — catturata **lo stesso giorno** — dice *«nel **2026**»*. Qualcuno ha
aperto l'editor e ha aggiornato **solo la copia**. La pagina che vende tutto l'anno è rimasta
indietro di dodici mesi.

Il difetto non è la svista: è la **direzione**. Il mirror è più giovane dell'originale, quindi è più
comodo da toccare, quindi si tocca — e il negozio invecchia in silenzio mentre il lancio brilla.

Nella Fabbrica la direzione è invertita e non è affidata alla buona volontà:
1. **si modifica l'originale, il mirror si rigenera** — mai una modifica che nasce nel mirror;
2. **nessun anno scritto a mano** in una pagina che vende tutto l'anno (controllo `anno_a_mano` di
   `scripts/gate_siti.py`, che nasce esattamente da questa misura — ADR-024, controllo 5);
3. la finestra del lancio ha una fine, e alla fine il mirror **si spegne**: una pagina figlia che
   sopravvive alla finestra è un doppione del negozio con dentro un badge che non vale più.
