---
Type: PROJECT
Status: Active
Tags: #preventa #outreach #whatsapp #concessionari #metodo #gael
Created: 2026-07-30
Last updated: 2026-07-30
---

# Preventa — Logica Completa del Sistema (bozza del Metodo)

## Overview

**Preventa** (ex PreventivoForge) è un prodotto che vende ai concessionari auto:
incolli il link di un annuncio (anche estero, es. tedesco) e ottieni un **PDF
preventivo brandizzato** con prezzi bloccati dal titolare, pronto da mandare su
WhatsApp — invece di 20-30 minuti su Excel/gestionale mentre il cliente scrive
già ad altri 3. **Prezzo: €2.000 una tantum, nessun canone** (DEC-EST-005).

Questo documento descrive **tutta** la macchina che Gael ha costruito per
trovare concessionari, qualificarli e contattarli in automatico, fino
all'invio WhatsApp reale. È la base per trasformare la logica in **Metodo**
(operativo, ripetibile, sicuro) prima di scalarlo.

**Comando che accende tutto:** `/avvia-outreach-preventa` → esegue
`Outreach/preventa-maps-scraper/outreach_giornaliero.py`.

---

## Mappa dei pezzi (dove vive cosa)

```
Outreach/
├── preventa-maps-scraper/              motore di scraping + orchestratore giornaliero
│   ├── scraper.py                      entrypoint scraping singolo
│   ├── outreach_giornaliero.py         ⭐ il flusso completo (Fase 1 + Fase 2)
│   ├── 02-AUTOMAZIONI-E-SCRIPTS/
│   │   ├── run.py                      motore Playwright con agenti (Scraper/Qualifier/Areus/QA)
│   │   ├── checker.py                  qualità sito web + calcolo priorità lead
│   │   └── areus.py                    scrittura/lettura CRM Areus (JSON condiviso)
│   └── 05-TEMPLATES-E-KIT/cities.txt   pool di 55 città per la rotazione giornaliera
├── WhatsApp Automation/
│   ├── refresh_session.py              login QR una tantum → salva profilo Chromium
│   └── send_message.py                 invio reale di un messaggio WhatsApp
└── Outreach Workflow/campagne/concessionari-preventa/
    └── personalizza_messaggi.py        sceglie il "gancio" e scrive i testi per lead

EmpireDesk/state/preventa_leads.json    CRM Areus — un solo file JSON condiviso, letto
                                         anche da EmpireDesk/modules/preventa.py (pannello UI)
```

Nessun servizio esterno, nessuna API key, nessun Google Sheets: tutto locale,
un file JSON come CRM, un profilo Chrome come sessione WhatsApp.

---

## Il flusso, passo per passo

```
FASE 1 — SCRAPING (import-focus)          FASE 2 — INVIO WHATSAPP
──────────────────────────────            ─────────────────────────────
1. Pesca 6 città/giorno da cities.txt     6. Legge Areus: stage=NEW +
   (rotazione: giorno-dell'anno % 55)         telefono mobile + priorità ok
2. Per ognuna, cerca 3 query import:      7. Ordina ALTA → MEDIA → BASSA
   "concessionario auto import",          8. Per ogni lead:
   "... import Germania",                     a. genera messaggio (gancio)
   "auto import usate"                        b. apre WhatsApp Web nel
3. Playwright estrae 20 schede/query:              profilo persistente
   nome, indirizzo, telefono, sito,           c. scrive ed invia
   recensioni                                 d. aggiorna stage→CONTACTED
4. checker.py analizza il sito (pixel,             SOLO dopo invio reale
   GTM, vecchio/moderno, https) →           e. pausa random 45-120s
   calcola priorità ALTA/MEDIA/BASSA           (ritmo umano)
5. Push su Areus (dedup per telefono,      9. Si ferma SUBITO se rileva:
   stage=NEW)                                 - segnali di ban account
                                               - profilo Chrome già aperto
                                               - 5 fallimenti di fila
                                            10. Cap giornaliero: max 50/giorno
                                                (conta quanti già mandati oggi,
                                                 riprendibile in sicurezza)
```

### Fase 1 in dettaglio — Scraping

- **Query "import-focus"**: non filtra i lead per nome dopo lo scraping (un
  filtro su "import" nel nome scarterebbe troppi concessionari veri che
  importano senza scriverlo in ragione sociale). Il focus si ottiene **prima**,
  nella query di ricerca stessa.
- **Rotazione città deterministica**: `indice = giorno_dell_anno % 55`, prende
  6 città consecutive dal pool. Pool esteso da 10 a 55 città (Lombardia,
  Piemonte, Veneto, Emilia-Romagna, Toscana, Liguria, Marche, Umbria) apposta
  per non esaurire lead freschi in pochi giorni.
- **Qualità del sito → priorità** (`checker.py`):
  | Condizione | Priorità |
  |---|---|
  | Nessun sito web | **ALTA** |
  | Sito vecchio/scarso (no https, Joomla, "in costruzione", pagina leggera) | **ALTA** |
  | Meno di 10 recensioni | **ALTA** |
  | Sito ok ma senza Pixel/GTM (probabile: no campagne ads attive) | **MEDIA** |
  | Meno di 25 recensioni o media <4.0 | **MEDIA** |
  | Sito moderno + tanti recensioni + tracking attivo | **BASSA** |
- **Anti-blocco Google Maps**: browser Playwright *headed* (visibile, non
  headless — fingerprint più credibile), flag `--disable-blink-features=
  AutomationControlled`, user-agent Windows/Chrome realistico, pause random
  (0.6-1.2s tra click, 1.2-2.8s tra lead, 3-6s tra città).
- **Push su Areus**: dedup per telefono normalizzato, scrive/legge un unico
  JSON (`EmpireDesk/state/preventa_leads.json`), stage iniziale `NEW`.

### Fase 2 in dettaglio — Invio WhatsApp

- **Chi è eligibile**: stage `NEW`, telefono tipo `mobile` (classificato per
  **lunghezza**, non per prefisso — un numero italiano locale a 10 cifre che
  comincia per 3xx diventa mobile; 39+10cifre resta invariato), non già
  contattato oggi. Per lead **import**: qualsiasi priorità va bene (vedi
  Gancio 4 sotto). Per lead non-import: solo ALTA/MEDIA (BASSA = già
  digitalizzato, il pitch non calza).
- **Scelta del gancio** (`personalizza_messaggi.py` → `scegli_gancio()`):
  | # | Nome | Quando | Idea del messaggio |
  |---|---|---|---|
  | 4 | Import/annunci esteri | categoria contiene "import" (ignora priorità) | "tradurre annunci tedeschi + preventivo italiano = doppio lavoro" |
  | 3 | PDF brutto/brand | ALTA, nessun sito o sito vecchio | "immagine curata online ma poi i preventivi escono storti" |
  | 2 | Cliente perso su WA | ALTA, poche recensioni | "se non rispondi con un PDF in 5 min, il cliente ha già scritto ad altri 3" |
  | 1 | Tempo perso (control) | tutti gli altri casi | "20-30 min a preventivo, il cliente scappa su WhatsApp" |
- **Invio reale**: `web.whatsapp.com/send?phone=...&text=...` dentro un
  **profilo Chromium persistente** dedicato (`whatsapp-profile/`, login QR
  una tantum via `refresh_session.py`). *Non* usa `storage_state` di
  Playwright: WhatsApp Web tiene le chiavi di sessione in IndexedDB, non nei
  cookie — `storage_state` non le cattura per come è fatto Playwright. Il
  profilo persistente invece sopravvive al riavvio.
- **Rilevatore di ban**: dopo l'apertura della chat e di nuovo dopo l'invio,
  legge il testo della pagina e cerca frasi tipo "account limitato",
  "temporarily banned", "hai raggiunto il limite" ecc. Se le trova → stop
  immediato dell'intero batch del giorno.
- **Ritmo umano**: pausa random 45-120s tra un invio e il prossimo (non
  istantaneo, non a intervalli fissi).
- **Stage aggiornato solo dopo invio vero** (Gate-CONTATTI: mai marcare
  CONTACTED senza invio reale confermato — niente numeri finti).
- **Cap giornaliero riprendibile**: conta quanti messaggi con
  `canale_contatto=whatsapp` sono già usciti *oggi* guardando `contattato_il`
  → puoi rilanciare lo script più volte nello stesso giorno senza superare il
  cap né duplicare invii.

### Follow-up (dopo il primo contatto)

Sequenza pensata (`personalizza_messaggi.py`, non ancora automatizzata come
la Fase 2):
1. **MSG1** (Fase 2 sopra) → aggancio.
2. Se risponde, o dopo G+1/+2 di silenzio → **MSG2**: spiega cos'è Preventa,
   offre esempio con un loro annuncio.
3. Se dice sì, o dopo G+5 di silenzio dal MSG1 → **MSG3**: propone demo 15
   minuti, prezzo €2.000 una tantum, 2 slot orari a scelta.
4. In parallelo esiste una sequenza email equivalente (email1/2/3) per i lead
   senza telefono mobile o come canale secondario.

---

## Regole/gate che governano il sistema

- **Gate-CONTATTI**: uno stage CONTACTED in Areus significa SEMPRE che un
  messaggio è stato davvero mandato. Mai fake, mai anticipato.
- **ADR-003 (wrap, mai riscrittura)**: `personalizza_messaggi.py` non tocca
  script esistenti (es. `empire_auto_v3.py`), li avvolge.
- **--no-areus / --areus-push-alta**: lo scraping può girare senza toccare il
  CRM condiviso, o pushare solo i lead ALTA per non sporcarlo.
- **--test**: run di prova con 1 città, limit 5, invio in dry-run (apre la
  chat, precompila, non preme invio) — usato prima di ogni run reale nuova.

---

## Rischi (dichiarati, non nascosti)

1. **Ban WhatsApp — il rischio più concreto.** 50 messaggi/giorno da un
   numero personale è un volume che WhatsApp può rilevare come spam e
   bloccare. Mitigazioni in campo: ritmo umano, rilevatore di ban (stop
   immediato), stop dopo 5 fallimenti di fila, stop se il profilo Chrome
   risulta già in uso. **Il rischio non è a zero.** Raccomandazione già
   lasciata a Max: partire con `--daily-cap` basso (es. 10) per 1-2 giorni
   prima di salire al cap pieno.
2. **Single point of failure**: un solo numero WhatsApp personale, un solo
   profilo Chrome. Se si blocca, la Fase 2 si ferma del tutto finché non si
   risolve (nessun numero di riserva).
3. **Blocco IP / Captcha su Google Maps**: se lo scraper produce screenshot
   vuoti o captcha, va fermato subito (non ritentare a raffica) e ripreso
   dopo 30-60 min, possibilmente cambiando IP.
4. **Fragilità del DOM WhatsApp Web**: WhatsApp cambia spesso i selettori
   della UI. Lo script prova più selettori a cascata per il campo di testo,
   ma se cambiano tutti insieme lo script si blocca (esito
   `chat_non_caricata`, con screenshot di debug).
5. **Telefono fisso = buco nel funnel**: i lead con numero fisso (prefisso
   0...) non sono raggiungibili via WhatsApp. Restano fuori dall'automazione,
   servono chiamata manuale (o email, se trovata sul sito).
6. **Score di priorità pensato per "sito vecchio", non per "import"**: bug
   reale già trovato e corretto — i concessionari import veri hanno spesso
   siti curati (priorità BASSA), quindi il filtro originale li escludeva
   quasi tutti. Risolto col Gancio 4 (ignora priorita_lead per i lead
   import), ma è un promemoria che **lo score di qualificazione non è
   universale**: va ricontrollato ogni volta che cambia il tipo di lead
   cercato.
7. **Nessuna misura di risposta reale ancora**: il sistema sa quanti
   messaggi ha mandato, non ancora quanti hanno risposto/convertito. Il
   circuito si ferma a "invio confermato", il tracking delle risposte è
   manuale in Areus per ora.

---

## Cosa serve perché la logica diventi "Metodo" (prossimi passi)

- Osservare 1-2 run reali al cap basso per capire la soglia di sicurezza
  WhatsApp prima di salire a 50/giorno.
- Decidere un piano B se il numero si blocca (numero di riserva? WhatsApp
  Business API ufficiale invece del profilo browser?).
- Automatizzare anche il follow-up (MSG2/MSG3) con lo stesso pattern
  gate-and-stop della Fase 2, oggi manuale.
- Tracciare risposta/conversione per lead e per gancio (1/2/3/4), per capire
  quale aggancio converte di più — oggi si sa solo quanti sono partiti.
- Gestire i lead a telefono fisso con un canale (email o coda per chiamata
  manuale) invece di lasciarli fuori.

---

## Connessioni
- [[project_preventivoforge_fabbrica]] — architettura fabbrica concessionari (motore N-app)
- [[project_outreach_system]] — sistema outreach più ampio (email, Instagram, LinkedIn)
- [[project_empire_desk_app]] — EmpireDesk/Areus, il CRM che riceve questi lead
