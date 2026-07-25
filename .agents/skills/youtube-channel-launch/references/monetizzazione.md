# Reference — Monetizzazione di un canale YouTube Automation

> I valori dei requisiti YPP e gli RPM cambiano nel tempo e per mercato. Qui c'è la **struttura del
> ragionamento economico**; i numeri correnti vanno sempre verificati su YouTube Studio e sulle
> pagine ufficiali. Nessun numero di questa pagina va usato come dato certo.

---

## 1. Requisiti di accesso al YPP

Storicamente richiesti (verificare i valori correnti):
- **1.000 iscritti**, **e**
- **4.000 ore** di visualizzazione pubblica negli ultimi 12 mesi **oppure** 10M di visualizzazioni
  di Short negli ultimi 90 giorni;
- rispetto delle policy, nessuno strike attivo, account AdSense, verifica in 2 passaggi.

Esiste anche una soglia d'ingresso ridotta per funzioni non pubblicitarie (es. abbonamenti al
canale) in alcuni mercati: utile saperlo, ma il grosso dei ricavi automation resta AdSense.

---

## 2. La matematica che decide il format

> **ORE = view × durata media VISTA**
> (non la durata del video: quella che conta è quanto viene effettivamente guardato)

Esempio a parità di view (12 video/mese × 1.800 view):

| Durata video | Retention 45% | Durata vista | Ore/mese | Mesi per 4.000h* |
|---|---|---|---|---|
| 3 min | 45% | 1,35 min | ~486 | ~6,5 |
| 10 min | 45% | 4,5 min | ~1.620 | ~1,9 |

*a partire da 850 ore già accumulate. Calcolo verificabile con `scripts/monetization_check.py`.

**Conseguenza operativa:** la **durata del format è una decisione economica**, non estetica. Un
format troppo corto richiede un volume di view molto più alto per lo stesso risultato.

**Ma attenzione al rovescio:** allungare un video senza contenuto **abbassa la retention**, e la
retention entra nella stessa formula. Allungare ha senso solo se il contenuto regge. Prima la
retention, poi la durata.

---

## 3. RPM: da cosa dipende

L'**RPM** (ricavo per 1.000 visualizzazioni) varia molto per:
- **Nicchia**: finanza, business, tecnologia, assicurazioni → alti. Intrattenimento, gossip,
  compilation → bassi.
- **Mercato linguistico**: i mercati anglofoni e nordeuropei pagano più di quelli piccoli.
- **Stagionalità**: il Q4 (Natale) paga sensibilmente più di gennaio.
- **Adatto agli inserzionisti**: temi delicati riducono o azzerano gli annunci.

> **Non usare mai un RPM "da internet" come se fosse il tuo.** Il tuo RPM reale si legge in YouTube
> Studio dopo l'ingresso nel YPP. Prima di allora è una **stima con intervallo**, e va dichiarata
> come tale (è quello che fa `monetization_check.py`).

---

## 4. Scelta della nicchia in ottica ricavi

Il compromesso tipico:
| | Nicchia ad alto RPM (finanza, business) | Nicchia a basso RPM (intrattenimento) |
|---|---|---|
| Ricavo per view | alto | basso |
| Difficoltà/concorrenza | alta | più bassa |
| Rischio policy | alto (disclaimer, YMYL) | variabile |
| Volume raggiungibile | minore | maggiore |

Non esiste la scelta giusta in assoluto: esiste quella coerente col tuo format e col tuo volume
sostenibile. Il `monetization-planner` lo mette per iscritto con uno scenario pessimista.

---

## 5. Ricavi non-AdSense (da considerare prima del YPP)

Utili perché **non richiedono i 1.000 iscritti**:
- Affiliazione (link in descrizione, coerenti con la nicchia).
- Prodotto proprio (ebook, corso) — collegabile all'ecosistema Digital Empire.
- Sponsorizzazioni (arrivano con un pubblico definito, anche piccolo, se la nicchia è chiara).

> Una nicchia **ben certificata e stretta** vale più per uno sponsor di un canale generalista
> grande: è lo stesso principio della coerenza che serve all'algoritmo.

---

## 6. Costi da mettere nel conto
Abbonamento Fliki (o simili), eventuale voce/musica premium, grafica miniature, tempo di
produzione (il costo più sottovalutato). Il break-even è: *quante view/mese servono per coprirli*
— calcolato da `monetization_check.py` con `--costi-mese`.

## Connessioni
- [[monetization-planner]] — costruisce il piano
- [[launch-gate]] — pretende lo scenario pessimista
- [[channel-health]] — decide se un canale va scalato o chiuso (scale-ops)
