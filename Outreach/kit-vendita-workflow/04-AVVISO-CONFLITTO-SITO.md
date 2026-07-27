# 🚨 AVVISO — quattro affermazioni sul sito che oggi non puoi difendere in demo

> Trovate da Arena il 2026-07-27 mentre scrivevo il kit di vendita. Non le ho cercate: sono
> saltate fuori confrontando le sezioni commerciali del sito con le prove reali su disco.
> **Owner della decisione: Max.** Io segnalo, non modifico il sito.

## Perché ti riguarda adesso

Il kit che ti ho scritto è costruito su una regola: **si dice solo ciò che si può dimostrare.**
Il sito, in quattro punti, dice più di quello che possiamo dimostrare oggi.

Il problema non è etico in astratto — è **operativo**: se un imprenditore scettico ha letto il
sito prima della call e ti chiede *"fammi vedere questi numeri"*, tu non ce li hai. In quel momento
perdi la trattativa, e la perdi nel modo peggiore: sembrando uno che gonfia.

E c'è un dettaglio che rende la cosa più urgente: **la sezione PROVE del sito è stata scritta
con lo standard giusto** (*"qui dentro va SOLO ciò che è verificabile su disco… se aggiungi una
riga, deve avere una fonte"*), mentre altre sezioni no. **Il sito si contraddice da solo.**

---

## I quattro punti

### 1. «3-5 clienti nuovi nel primo mese, ticket medio 3.000 €»
**Dove:** `agency-empire/src/sections/15-objections.tsx`
**Testo:** *"Per la maggior parte dei nostri clienti, l'Outreach Workflow porta 3-5 clienti nuovi nel primo mese."*

**Il problema:** *"la maggior parte dei nostri clienti"* — al plurale. Sul disco c'è **un cliente
documentato**: Novacar. E Novacar è Preventa (preventivi auto), **non** l'Outreach Workflow.
Quel numero non ha una fonte in nessun file del repo.

**Se te lo chiedono in call, oggi non hai risposta.**

**Cosa farei:** riscrivere in *"Il sistema è progettato per portare un flusso costante di contatti
qualificati. Quanti diventino clienti dipende da voi e dal vostro mercato: non lo promettiamo."*
Perde smalto, regge a qualsiasi domanda.

---

### 2. «Il 90% di chi vede il sistema in live vuole iniziare la settimana dopo»
**Dove:** `agency-empire/src/sections/15-objections.tsx`

**Il problema:** il 90% **di quante demo?** Nel repo non c'è un registro demo. Il dossier 24
dice che l'outbound doveva ancora partire; il 25 segna il run reale come non completato.
Questo numero, oggi, **non ha un denominatore**.

È anche il più pericoloso dei quattro: basta che il cliente chieda *"su quante persone?"* e la
conversazione cambia di tono. Da venditore diventi uno che deve giustificarsi.

**Cosa farei:** toglierlo. Non sostituirlo — toglierlo. La demo si vende dicendo *"è gratis e
dura 30 minuti, se non ti convince non hai perso niente"*, che è vero e basta.

---

### 3. «In ogni demo ti mostriamo workflow attivi per clienti del tuo settore»
**Dove:** `agency-empire/src/sections/15-objections.tsx`
**Testo:** *"…quanti lead ha generato, quante email ha mandato, quale conversion rate sta ottenendo. Numeri reali, tracciati, verificabili."*

**Il problema:** è una promessa che **prendi in faccia in demo**. Se il cliente è un'azienda di
servizi e ti chiede il workflow attivo del suo settore con conversion rate, tu hai Novacar —
un concessionario, e per giunta con un prodotto diverso.

**Cosa farei:** *"In demo ti mostro un sistema vero che gira, con i numeri che abbiamo misurato.
Non è del tuo settore: è la prova che costruiamo macchine che funzionano davvero."* — che è
esattamente quello che ti ho messo nello script al minuto 12, e funziona meglio perché è disarmante.

---

### 4. «Un workflow da 7.000 € si ripaga al primo cliente»
**Dove:** citato nel dossier 23 §1 come claim del sito

**Il problema:** vero solo se il ticket medio del cliente è ≥7.000 €. Per un cliente con ticket
da 800 € è falso, e lui lo sa mentre lo legge. Un claim che è vero solo per alcuni, letto dagli
altri, **squalifica chi lo scrive**.

**Cosa farei:** girarlo in domanda — *"quanto vale un vostro cliente medio? Fate il conto di
quanti ve ne servono per ripagarlo."* Fa fare il calcolo a lui, e il numero che esce è suo.
(È già così nello script al minuto 3-12.)

---

## Il punto di fondo

Sul sito ci sono **due voci diverse**:

| | |
|---|---|
| **La sezione PROVE** | *"65 preventivi… i 65 comprendono i nostri collaudi… la testimonianza firmata non c'è ancora"* — **onestà chirurgica** |
| **La sezione OBIEZIONI** | *"3-5 clienti nel primo mese… il 90% vuole iniziare"* — **numeri senza fonte** |

La prima voce è quella che vi distingue: pochissime agenzie scrivono "cosa questa prova non dice".
**È il vostro vantaggio competitivo, ed è raro.** La seconda è quella che usano tutti, e che nessuno
si beve più.

La seconda **danneggia** la prima: se un cliente legge prima le obiezioni gonfiate e poi la sezione
prove, non pensa "che onesti" — pensa che l'onestà sia una tecnica di vendita anche quella.

---

## Cosa ti chiedo di decidere (5 minuti)

1. **Approvi la riscrittura dei 4 punti?** Se sì, è un task da mezz'ora per Gael su
   `15-objections.tsx` (+ `npm run build` verde). Prompt pronto, se lo vuoi te lo scrivo.
2. **Oppure vuoi tenerli** finché non hai numeri veri che li sostengono? È una scelta legittima
   — ma allora **non usare quelle frasi in call**, perché in call il numero te lo chiedono.
3. **Terza via, la migliore:** falli diventare veri. Dopo 10 demo hai il denominatore per il punto 2;
   dopo il primo cliente Outreach hai il punto 1. **Sono claim in attesa di prova, non bugie
   permanenti** — ma finché la prova non c'è, stanno online come se ci fosse.

---

*Nota di metodo: te lo segnalo perché il vostro Mandato all'Art.2 dice "prove non promesse, anche
verso noi stessi", e il dossier 23 usa la formula "onestà brutale". Ho applicato il vostro standard
al vostro sito. Se preferisci che questi controlli non li faccia, dimmelo e mi limito a quello che
chiedi — ma sarebbe uno spreco del mio ruolo di revisore indipendente.*
