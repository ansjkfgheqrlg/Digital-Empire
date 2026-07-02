# ⛔ REGOLE SACRE — Preventivo PDF (INVIOLABILI)

> Queste regole NON si possono MAI infrangere. Vanno **verificate a OGNI preventivo generato**,
> una per una, senza dimenticarne nemmeno una. Sono la legge del formato PDF.
> Modello di riferimento: `Preventivo BMW Z4 2003 FR 3.0i.pdf` (concessionaria Novacar srl).
> Ogni PDF prodotto deve essere **indistinguibile per struttura** dal modello (contenuto diverso, struttura identica).
> Controllore automatico: agente `qa-regole-checker` (Gate R) + `qa-immagini` (Gate IMG). Se anche UNA regola è rossa → il PDF NON si consegna.

---

## R-01 — PRIMA PAGINA = SOLO LOGO
La prima pagina contiene **esclusivamente il logo della concessionaria**, centrato, grande, su
sfondo bianco. Nient'altro (no testo, no auto, no prezzo).

## R-02 — LOGO IN OGNI PAGINA (in alto a sinistra)
Su **tutte** le pagine di contenuto (scheda, equipaggiamento, prezzo, foto) il logo della
concessionaria è presente **in alto a sinistra**, piccolo e pulito.

## R-03 — DATI AZIENDA (seconda pagina, in alto a destra)
Nella seconda pagina, accanto al logo, ci sono SEMPRE i dati completi dell'azienda:
**ragione sociale, P. IVA, Sede Legale, cell., e-mail, PEC** (dal config della concessionaria).
Formato come nel modello (blocco corsivo/grassetto).

## R-04 — TITOLO VETTURA
Sotto l'header, il **titolo grande** dell'auto (marca + modello + versione). Es. "BMW Z4 ROADSTER (E85) 3.0i".

## R-05 — SCHEDA TECNICA (tabella come nel modello)
Tabella "Scheda tecnica autovettura" con **barra header scura** e righe alternate chiaro/grigio.
Campi minimi (ordine del modello): Prima immatricolazione · Provenienza veicolo · Porte · Carburante ·
Potenza · Tipo cambio · Colore esterno · Colore e tipo interni · Chilometraggio · Numero posti ·
Classe emissioni · Tipo trazione. Font e tabella si possono **migliorare** (più eleganti) ma la
struttura resta questa.

## R-06 — EQUIPAGGIAMENTO PRINCIPALE
Sezione "Equipaggiamento principale" (barra scura) con elenco puntato delle dotazioni.

## R-07 — CONDIZIONI DI GARANZIA
Sezione "Condizioni di garanzia" (barra scura) con elenco (es. Tagliandi certificati, Chilometri certificati).

## R-08 — PREZZO "TOTALE IN STRADA (IVA INCLUSA)"
Blocco prezzo in stile modello: riga grande **"Totale in strada (Iva inclusa) € <finale>"** +
righe di dettaglio del calcolo. Nota a piè: "Offerta valida salvo disponibilità del fornitore".

## R-09 — IMMAGINI: TUTTE, COMPLETE, PERFETTE (regola critica)
- **TUTTE** le foto dell'annuncio devono essere nel PDF. Nessuna esclusa.
- Le immagini **NON devono mai essere tagliate/croppate**: si vede l'auto per intero (fit completo, mai `cover`).
- Grandezza **perfetta e uniforme**, ben visibili, alta qualità, proporzioni originali rispettate.
- Impaginazione ordinata (nel modello: 2 foto grandi per pagina).
- Verifica: `qa-immagini` controlla `numero foto nel PDF == numero foto annuncio` e che nessuna sia ritagliata.

## R-10 — ULTIMA PAGINA = SOLO LOGO
L'ultima pagina contiene di nuovo **solo il logo** della concessionaria, centrato (chiusura).

## R-11 — NESSUN RESIDUO TEDESCO / NESSUN DATO INVENTATO
Tutto il testo è in **italiano corretto**. Zero parole tedesche. Nessun optional/dato inventato
(tutto deriva dai dati reali dell'annuncio). (Vale anche Gate B.)

## R-12 — DATI CORRETTI E PREZZO VERIFICATO
Prezzo finale ricalcolato in modo indipendente (Gate C). Marca/modello/km/anno coerenti coi dati reali.

## R-13 — COERENZA MULTI-CONCESSIONARIA
Logo, dati azienda, colori e note vengono SEMPRE dal config della concessionaria
(`concessionarie/<id>/config.json`). Mai valori hardcoded di un dealer nel PDF.

## R-14 — MIGLIORAMENTI SÌ, RIMOZIONI NO
Si possono **migliorare** font, spaziature, eleganza, organizzazione. Ma **nessuno** degli
elementi sopra (R-01…R-13) può mai mancare o essere semplificato via.

---

## Come si applica
1. Ad ogni run, dopo S5 (PDF), l'agente **`qa-regole-checker`** scorre R-01…R-14 e produce un
   report `regole-check.json` con PASS/FAIL per ogni regola.
2. L'agente **`qa-immagini`** verifica R-09 in dettaglio (conteggio + nessun crop + qualità).
3. Se anche una sola regola è FAIL → **Gate rosso**, il PDF non si consegna, si corregge.
4. Questo file va letto/rispettato **ad ogni generazione**: è citato in `CLAUDE.md`, nel conductor e negli agenti PDF/QA.
