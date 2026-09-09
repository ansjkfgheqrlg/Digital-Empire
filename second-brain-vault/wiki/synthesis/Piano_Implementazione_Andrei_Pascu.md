---
Type: SYNTHESIS
Status: Shipped
Tags: #competitor #implementazione #lanci #info-business #ultimo-metro
Created: 2026-09-10
Last updated: 2026-09-10
---

# Piano di Implementazione — Andrei Pascu

## Overview
Il documento che chiude lo studio del competitor Andrei Pascu trasformandolo in azioni eseguibili
per Digital Empire. Costruito col metodo dei tre giri di critica (ogni giro attacca il giro prima,
mai l'originale) e chiuso da Emperator il 2026-09-10 — checkpoint `CP-20260910-K6C2`, ripresa
`EMP-APPLAN1`. Documento e PDF standard-oro in
`competitor/Andrei Pascu/piano-implementazione/PIANO-IMPLEMENTAZIONE-ANDREI-PASCU.md|.pdf`, doppione
in `documentazione Empire/competitor/Andrei Pascu/`.

## Il ritrovamento portante
**Digital Empire possiede già il codice per incassare e non l'ha mai acceso.** Verificato sul disco:
- `empire/tools/checkout.py` (13.819 byte) legge `Crea siti/Siti CCM/checkout.config.json`
- quel file ha già il prezzo del Manuale — **67 € lancio / 97 listino / 27 bump** — fissato da
  `DEC-EST-001` il 21/07/2026 per silenzio-assenso, e mai eseguito
- tutti i rail di pagamento sono spenti tranne l'ordine via email; il primo dice testualmente
  `"richiede": "MAX: crea Payment Link su Stripe"`, e `scadenza_lancio` è ferma al 31/07/2026
- `KDP - prodottti digitali/Leanding Page/email-agent/main.py` è un webhook Stripe→PDF via Gmail
  già funzionante per un altro ebook

Nessuna delle 34 azioni scritte dai due draft toccava questo. Manca un gesto da dieci minuti, non una
build da quaranta ore.

## Le sette decisioni chiuse (P3)
| # | Decisione |
|---|---|
| D1 | Le azioni sono **34**, contate per ID distinto |
| D2 | AP-046b/047b sono **ABILITA UN EURO**, non infrastruttura |
| D3 | Prezzo Manuale **67/97/27** (`DEC-EST-001`); la fascia 27-47 € dei draft muore (veniva da un piano `_v3-superata`) |
| D4 | Scala prezzi **98→400→999**, soglia prova sociale **349**; il **434** della TASK-GAEL settimana 3 va corretto prima che diventi codice |
| D5 | AP-038 = C2 (cartella) + C1 (contenuto), come AP-037 |
| D6 | AP-041 usa un campo nuovo `soglia_fonti_esterne_minima` |
| D7 | `catena.py` **scende dal rango 1**: versione minima, e solo nello stesso commit della riga che la collega a `GATE-FNL-1` |

## Le lezioni di metodo, riusabili altrove
- **Uno strumento non chiude un gate finché nessuna riga li collega.** Costruire ≠ rendere obbligatorio.
- **Nessuna azione è fatta finché non nomina chi la consuma** — altrimenti è un pezzo per ULTIMO METRO.
- **Nessun numero senza fonte**: tre cifre del piano erano inventate, una quarta ne sostituiva
  silenziosamente un'altra realmente misurata.
- **Una critica sola non basta**: due Sentinelle sullo stesso angolo, che non si conoscevano, hanno
  prodotto conteggi e classificazioni divergenti. La divergenza va portata fino alla decisione,
  mai nascosta nell'assemblaggio.
- **Il mirror-di-lancio** (non si scrivono pagine nuove: si specchia e si rilancia) è lo strumento
  esatto per il magazzino dei 25 pezzi finiti e mai pubblicati.

## Connessioni
- [[Source_Andrei_Pascu_Armageddon_Landing_Lancio]]
- [[Source_Andrei_Pascu_Ordine_Funnel]]
- [[Source_Andrei_Pascu_Importanza_Landing]]
- [[Source_Andrei_Pascu_Preventivo_Non_Venderai]]
