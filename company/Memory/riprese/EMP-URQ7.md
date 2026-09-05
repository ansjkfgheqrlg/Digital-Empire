# EMP-URQ7 — Piano ecosistema LANCI: versione 4 completa e consegnata

- **Aperto:** 2026-09-05 · **Task:** TASK-LANCI-ECO-W2 · **Stato:** ✅ **CHIUSO** — versione 4 consegnata per intero
- **Checkpoint di chiusura:** [CP-20260905-017](../checkpoints/CP-20260905-017.md)
- **Continua:** [EMP-ECGA](EMP-ECGA.md) — che dichiarava il piano chiuso. **Non lo è più:**
  Max ha ordinato revisione totale e riscrittura ultra-architettata.

---

## L'ordine di Max, esatto

> *"Il piano secondo me va veramente migliorato, previsionato […] criticalo, guardalo,
> analizzalo e poi per una versione ultra migliorata […] l'architettura deve essere molto più
> architettata, molto molto di più […] a livello chirurgico."*

E, dalla ricognizione delle origini, **era già stato chiesto il 2026-09-04**: *"Deve essere
tutto ancora più architettato"*. È la seconda volta: la v3 non aveva soddisfatto la richiesta.

## Cosa è FATTO — verificato sul disco

### La critica (completa, 7 forze schierate, 6 rientrate)
Tutti i rapporti sono in
`C:\Users\Utente\AppData\Local\Temp\claude\c--Users-Utente-Desktop-qui-tutto-Digital-Empire\84927332-f056-487f-bf27-9e03c5796847\scratchpad\critica-lanci\`
**✅ COPIATI NEL REPO** in `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/_critica-v3/` (300 KB): non spariscono più.

| File | Contenuto |
|---|---|
| `CRITICA-A.md` (58 KB) | dossier 01-02-03: **19 difetti gravi** |
| `CRITICA-B.md` (47 KB) | dossier 04-05-06: **22 difetti gravi** |
| `CRITICA-D.md` | dossier 07-08-10 — **rientrata, completa (8 sezioni)**. Rilievi chiave: le formule dello scarto di budget non hanno tetto e possono rendere non-bloccante GATE-TSR-2; i conti dei reparti/agenti/gate non tornano fra dossier 01 e 08 (11 vs 10, 30 vs 29, 13 vs 14 gate); GATE-TSR-3 e GATE-MEM-1 si sovrappongono sulla stessa transizione, mai cablata; più agenti sono pura aritmetica travestita da modello; nessuna stima numerica del costo per lancio; **due affermazioni di fatto del piano erano già false mentre venivano scritte** — il registro numeri dava il 15 già riservato e `empire conform` restituisce 1 blocco, non 2 |
| `CRITICA-EMPERATOR.md` (17 KB) | i miei 13 rilievi, con ADR alla mano |
| `ORIGINE.md` (39 KB) | cosa era stato chiesto davvero (13 vincoli V-01..V-13) |
| `PONTE-AGENTI.md` (17 KB) | il ponte codice→agente: esiste, funziona, nessuno lo usa |
| `MOTORE.md` | il motore canonico non regge un flusso a 10 fasi |
| `INCASSO.md` | l'infrastruttura commerciale reale: quasi tutta assente |

### La versione 4 (scritta e funzionante)
Dentro `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/`:

- [x] `dati/registro.yaml` — **la fonte di verità unica**: 13 artefatti, 14 gate, 15 agenti,
      12 stati, 17 transizioni, 6 punti umani, 10 invarianti
- [x] `dati/valida_registro.py` — **gira davvero**: 253 controlli, esce 0
- [x] `dati/schemi/*.json` — **13 schemi, tutti JSON valido**
- [x] `00-LEGGIMI.md` — apertura, tesi, primo giorno, decisioni, quando si smette
- [x] `01-ARCHITETTURA.md` — catena, `avanza`, stati, ponte, motore, errori, osservabilità,
      sicurezza e obblighi di legge, confini

## Cosa è STATO COMPLETATO dopo la pausa

Tutti e quattro i documenti mancanti sono scritti, più le tre operazioni di chiusura:

- [x] `02-PREVISIONE-E-DENARO.md` (354 righe) — **il costo macchina è calcolato**: 48-79 invocazioni
      per lancio, 3,84-8,69 $ di sola tassa. Il tetto di 15 $ regge il lancio pulito, non regge molte
      riprove: dichiarato apertamente
- [x] `03-FLUSSO-OFFERTA.md` (371 righe) — sei fasi O1-O6, la firma come oggetto con impronta
- [x] `04-COSTRUZIONE.md` (320 righe) — 6 scaglioni, pre-mortem a 10 voci, 5 condizioni d'uscita
- [x] `05-ADR-023.md` (261 righe) — **rinumerato da 022**: quel numero è stato occupato da un'altra
      sessione alle 19:30 (studio AI TUBE PRO, già ACCETTATA)
- [x] `06-CRITICA-E-GIRI.md` (1.613 righe) — 12 fatali, 45 gravi, 8 respinti, 26 tenuti
- [x] I nove rapporti della critica **salvati nel repo** in `_critica-v3/` (300 KB)
- [x] La v3 archiviata in `_v3-superata/` con la propria nota, integrale
- [x] Puntatori aggiornati nello stesso turno: registro numeri, task di Gael, stato, wiki
- [x] Validatore rieseguito: **253 controlli, esce 0**; 137 sigle verificate, zero ignote

## Decisioni già prese — non rimetterle in discussione

| # | Decisione | Perché |
|---|---|---|
| 1 | **Il centro è l'artefatto, non il reparto** | i difetti della v3 sono quasi tutti errori di copia fra 11 documenti: la prosa non resta coerente con sé stessa |
| 2 | **La fonte di verità è `registro.yaml`, validato da un programma** | se un documento contraddice il registro, ha torto il documento |
| 3 | **Nascono 3 artefatti nuovi**: `pubblico.json`, `previsione.json`, `consuntivo.json` | rispettivamente: canale morto non rilevato, mai la domanda "quanto incassiamo", consuntivo che era un testo |
| 4 | **Il primo giorno è la catena dell'incasso**, non la cartella | l'azienda non può incassare un euro: misurato |
| 5 | **15 agenti, non 41-50** | tassa fissa di 0,08-0,11 $ per invocazione (ADR-014): tanti agenti = moltiplicatore di costo |
| 6 | **LANCI non costruisce un motore di orchestrazione** | misurato: non ne ha bisogno. È la risposta alla domanda aperta di ADR-019 §4 |
| 7 | **Il giudice (`lan-gate`) non ha Write né Edit** | invariante INV-09, verificato dal validatore |
| 8 | La v4 sostituisce in loco dentro `29-ECOSISTEMA-LANCI/`, la v3 si archivia | un solo puntatore, mai due piani concorrenti |

## Trappole — ogni riga vale un'ora

1. **`registro.yaml`: niente `;` come separatore.** Non è YAML valido. Per le mappe compatte
   si usa `{chiave: valore, chiave: valore}`. Ci sono già cascato una volta.
2. **Il validatore va rieseguito dopo OGNI modifica al registro**, e deve uscire 0:
   `cd PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati && PYTHONIOENCODING=utf-8 python valida_registro.py`
3. **Il validatore ha già bocciato me**: avevo dato Write al giudice del debrief. Non è teorico.
4. **Il servizio dei subagenti è instabile**: un DOOM BOT è morto per errore server a metà lavoro.
   Antidoto che ha funzionato: far creare il file d'uscita SUBITO con le sezioni vuote e farlo
   risalvare a ogni sezione. Chi muore lascia comunque il lavoro fatto.
5. **I rapporti della critica sono ora nel repo**, in `_critica-v3/`.
7. **La console è cp1252:** ogni script che stampa emoji va lanciato con `PYTHONIOENCODING=utf-8`.
8. **`sed` con `|` come delimitatore rompe** sulle righe di tabella markdown: usare Python.
9. **ADR-022 non è più libero**: occupato il 05/09 alle 19:30 da un'altra sessione. Il nostro è il **023**.
6. **⚠️ SICUREZZA, da dire a Max ogni volta finché non è fatto:** la chiave del servizio di posta
   (Brevo) è pubblica da mesi e mai sostituita. Va cambiata **sul servizio**: la storia git
   pubblica resta leggibile. È B-020.

## I fatti nuovi trovati, che il piano v3 non conosceva

1. **Il canale YouTube del Manuale è "funnel morto" dal 29/07/2026**, dirottato su @dosementale
   (`second-brain-vault/wiki/log.md:1054-1063`). Nessun documento di settembre lo sa.
2. **Quattro prezzi diversi** per lo stesso prodotto, mai riconciliati: "NON LO SO" (catalogo
   07/03), "€297-€497" (wiki 29/04), le fasce del listino, i 47 € del piano v3.
3. **Esisteva già un piano di lancio** per il Manuale, con obiettivo 30/05/2026: mancato da tre
   mesi, mai registrato da nessuna parte.
4. **Non esiste un modo automatico di incassare**, né misura installata, né pagine di vendita
   online. Il prodotto invece esiste davvero: 203 pagine verificate.

## Il prossimo passo esatto

**Nessuno sul piano: è chiuso.** Il lavoro riprende solo se Max decide qualcosa fra le quattro
voci qui sotto, oppure quando Gael comincia a costruire da
`PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI.md` → `04-COSTRUZIONE.md` §3, scaglione S0.

## Cosa aspetta MAX — quattro decisioni, le prime due chiudibili in dieci minuti

1. **Il Manuale si vende o è un regalo?** (ora ha default reversibile "vendita" a 7 giorni)
2. **Sostituire la chiave di posta esposta** (cresce ogni giorno — B-020)
3. Approvare l'**ADR-023** (era il 022: quel numero è stato occupato da un'altra decisione)
4. Riaprire o no **ADR-019** sul motore di orchestrazione
