# TASK-LANCI-20260908 — ANATOMIA DEI LANCI DI ANDREI PASCU → consegna a chi costruisce LANCI

- **Aperto:** 2026-09-08
- **Da:** Emperator (sessione dello studio totale, ripresa `EMP-J8X2`)
- **A:** la sessione/task che costruisce **l'infrastruttura dei lanci** — ecosistema 15-LANCI,
  [ADR-025](../decisions/ADR-025-ecosistema-lanci.md), piano `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/`
- **Ordinato da:** Max, 2026-09-08, a voce
- **Stato:** 🟡 APERTA — il lavoro non è iniziato: prima si chiude lo studio dei siti

---

## L'ordine, in una riga

Andrei Pascu **sa fare i lanci, li fa spesso, e ne ha uno aperto adesso**. Lo stiamo già studiando
nel dettaglio più piccolo. Quindi si smonta anche **come lancia**, e il risultato non resta nello
studio: **si consegna a chi sta costruendo l'infrastruttura dei lanci**.

## Cosa arriverà, esattamente

| Forma | File | A cosa serve a LANCI |
|---|---|---|
| Markdown | `competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md` | la fonte leggibile: fasi, funnel, offerta, ricorrenze |
| Python | `competitor/Andrei Pascu/anatomia_lanci.py` | i dati in struttura interrogabile: LANCI ci chiama dentro invece di rileggere una prosa |
| PDF | `documentazione Empire/` | la forma ufficiale da consegnare e mostrare |

## Le sei domande a cui risponderà

1. Come struttura un lancio — fasi, ordine, tempi.
2. Come fa il funnel — ogni gradino, dall'ignaro alla cassa.
3. Come costruisce l'offerta — bundle, voucher, prezzo barrato, scarsità.
4. Cosa hanno in comune i suoi lanci — il modello ripetibile.
5. Come ragiona — il metodo, non l'estetica.
6. Cosa non fa mai — le assenze pesano quanto le presenze.

## Su cosa si fonda — prove già sul disco, non da raccogliere

- **Un lancio vivo, catturato:** `armageddon.bsns.it` + le 4 pagine figlie (mirror statico di un
  lancio in corso, ripulito a mano da ogni script della piattaforma, tutte verso **un solo link
  Stripe**).
- **L'offerta misurata:** 585 € di listino + 199 € di voucher, venduti a **199 €**.
- **La macchina del funnel:** catene `/define → /asa → /copy-base`, pre-casse `/outfunnel-1`,
  `/armadeggon-strp`, `/acquista-v101`. Misurato: **86 parole** portano dall'apertura al clic
  d'acquisto.
- **La scala dei prezzi:** 98 € → 434 € → 999 €. Misurato: **più prezzo non porta più obiezioni,
  porta più fonti esterne** (0 → 2 → 5); prova sociale vera solo sopra i 349 €.
- **~40.000 parole di teardown** già scritte in `competitor/Andrei Pascu/site-study/reports/`.
- **29 video del suo ecosistema** già ingeriti (reparto Competitor Research, ecosistema 1).

## Precondizione — non negoziabile

**Prima si chiude lo studio dei siti** (onde A→G, dossier 33 PARTE V). Stato contato dal disco:

```
python "competitor/Andrei Pascu/site-study/scripts/stato_onde.py"
```

Concludere sui lanci con metà ecosistema mai aperto significherebbe concludere su metà delle prove.

## Quando è "fatta"

Non quando il PDF esiste: **quando la sessione LANCI l'ha ricevuta e può usarla** (ADR-016,
l'Ultimo Metro). Chi chiude questa task scrive qui sotto la data e chi ha ricevuto.

- [ ] Markdown scritto
- [ ] Python scritto e funzionante
- [ ] PDF generato + doppione in `documentazione Empire/`
- [ ] **Consegnato a LANCI** — data: ______ · ricevuto da: ______

---

## Connessioni
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` — PARTE VI, il secondo scopo
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/` — il piano che riceve
- `company/Memory/riprese/EMP-J8X2.md` — la sessione che produce
- `company/Memory/decisions/ADR-025-ecosistema-lanci.md` · `ADR-016` (Ultimo Metro)
