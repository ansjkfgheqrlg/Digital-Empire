---
Type: SOURCE
Status: Active
Tags: #cfo-ai #tesoreria #quickbooks #claude-skills #determinismo #anti-allucinazione #finance #giovanni-beggiato #max17
Created: 2026-09-03
Last updated: 2026-09-03
---

# Source: Giovanni Beggiato — "Ho creato un CFO AI che controlla l'azienda H24 con Claude"

## Overview
Tutorial di 34m52s in cui Giovanni Beggiato (agenzia AI "Gente Sei", community Skool "Avanguardia Plus") costruisce da zero, in diretta, un "AI CFO": un sistema a tre fasi nettamente separate — estrazione dati grezzi da QuickBooks via API, calcolo deterministico in Python (mai l'AI), interpretazione finale affidata a due skill Claude distinte (`analista-finanziario` che estrae/calcola e non interpreta, `ai-cfo` che interpreta e non ricalcola) — con un cancello anti-invenzione automatico (`verifica_dashboard.py`) che blocca la consegna del report se un solo numero della dashboard HTML finale non risale a un dato realmente calcolato. Video 15 del batch `max17`.

Il valore per Digital Empire non è "un altro tool finanziario" — DE ha appena costruito il proprio (Tesoreria, ADR-020, 2026-09-03, lo stesso giorno di questo ingest) — ma un **confronto diretto punto per punto** fra un sistema maturo (soglie di allerta in codice, scadenzario crediti, test di determinismo con bug reali trovati, cancello anti-invenzione) e un sistema appena nato per scelta esplicita da un registro vuoto. Vedi `confronto-tesoreria.md` nel run per l'analisi completa.

## Dati Tecnici

- **Video ID:** sno_IcNbYFM
- **Durata:** 34m52s (2092s)
- **Canale:** Giovanni Beggiato — "Joe", agenzia AI "Gente Sei", community Skool "Avanguardia Plus" · **Lingua:** IT
- **Formato:** Talking head + screen share app Claude (tab Code) + QuickBooks Online Sandbox + documento Notion con 6 prompt integrali
- **Frame:** 523 densi @4s → 226 unici sopra soglia | **Frame letti: 82/226 (36,3%)** | NO-FINTO: PASS con copertura parziale dichiarata (vedi `coverage.md`)
- **KA:** 40 (architettura a 3 fasi, 6 prompt integrali, numeri reali della demo, dettagli delle due skill)
- **Processing:** pipeline Empire Studio · Memory Empire C-H 2026-09-03
- **Run:** `empire-studio/runs/max17-v15`
- **Deliverable unico di questo run:** `confronto-tesoreria.md` — non esiste in nessun altro run del lotto max17

## Il Principio — Tre Fasi Mai Mescolate

```
1. ESTRAZIONE                2. CALCOLO DETERMINISTICO       3. INTERPRETAZIONE
   solo dati grezzi              motore Python (non l'AI)        skill "ai-cfo"
   su disco, zero calcoli        fa tutte le somme, i punteggi,  legge i numeri già
   (QuickBooks via OAuth)        gli scostamenti budget           fissi, li traduce in
                                                                   report per la direzione
        |                              |                                |
        v                              v                                v
  "se un numero non torna,      test di determinismo:           verifica_dashboard.py:
   apri il file grezzo"         stessa SHA-256 su 13             blocca la consegna se un
                                 funzioni, ha trovato 2 bug       numero non ha origine
```

Frase riassuntiva ripetuta due volte con parole quasi identiche: **"il codice fa i conti, l'AI li interpreta"** — non per stile ma per token (il codice non ne consuma per l'aritmetica) e per determinismo (un LLM indovina il token successivo con probabilità di errore diversa da zero, il codice no).

## I Sei Prompt — Riusabili, Recuperati dal Notion Pubblico

Tutti incollati da un documento Notion condiviso in descrizione ("AI CFO — tutti i prompt"), mai scritti a mano davanti alla telecamera:

```
Prompt 1 — Modello dati Python (libreria standard, 4 dataclass "non negotiable")
Prompt 2 — Collegare QuickBooks e scaricare (estrazione pura, niente calcoli)
Prompt 3 — Il motore delle metriche (determinismo bit-per-bit richiesto esplicitamente)
Prompt 4 — Allerte e Command Center (10 soglie nominate, 6 campi per alert)
Prompt 5 — La dashboard (un solo file HTML, si apre anche senza rete)
Prompt 6 — Il controllo antinvenzione ("il prompt più importante di tutti")
```

Le dieci soglie del Prompt 4, lette per intero a schermo: concentrazione singolo cliente 20%, esposizione singolo cliente 60.000€, crediti già scaduti 25%, crediti oltre 90gg 12%, giorni medi incasso 75, ciclo di cassa 60gg, calo margine lordo anno su anno 1,5 punti, EBITDA minimo 6%, copertura costi fissi 3 mesi, scostamento dal budget 10%.

## Il Test di Determinismo Ha Trovato un Bug Reale

Documentato per iscritto nel Notion, non solo dichiarato a voce: confrontando 12 mesi di budget contro 8 mesi di consuntivo usciva uno scostamento del -40,8% — "un risultato che non era un risultato, era un calendario". Corretto usando solo i mesi in comune (scostamento vero: -86.334€, -3,2%). Determinismo poi confermato con la **stessa impronta SHA-256 su tutte e 13 le funzioni**, prima e dopo le correzioni.

## Il Cancello Anti-Invenzione

`verifica_dashboard.py`: estrae ogni numero dal testo HTML (ignorando CSS/SVG/coordinate), costruisce l'insieme dei valori noti scavando ricorsivamente in `command_center.json`, lo espande con le combinazioni elementari che un CFO fa a mente (×100, differenze, somme fra KPI), confronta con tolleranza relativa 0,6%, **esce con codice 1 se resta anche un solo numero senza origine verificabile** — bloccando la pipeline, non solo segnalando.

## Key Quotes

> "Il codice fa i conti, l'AI li interpreta." [ripetuto due volte, principio centrale]

> "Un alert senza soglia scritta non è un alert, è un'opinione." [Prompt 4]

> "Un numero scritto dentro una formula diventa invisibile: chi legge il risultato non ha modo di sapere che una parte di quel risultato è una scelta e non una misura." [sulla variabile RECUPERO_ATTESO messa in cima al modulo]

> "La linea fra le due [skill] è il punto di tutto il sistema. Se una sconfina, o i numeri diventano opinioni, o le opinioni diventano numeri."

> "Il prompt più importante di tutti... è quello che ti permette di mettere la dashboard davanti a qualcuno senza doverla accompagnare con dei distinguo." [sul Prompt 6, anti-invenzione]

> "Non stiamo parlando di rimuovere persone o rimuovere i CFO... parliamo qui di AI enhancement e non di rimpiazzare lavori vari."

## Confronto con Digital Empire — deliverable dedicato

**`confronto-tesoreria.md`** (nel run `max17-v15`) confronta punto per punto questo CFO AI con la **Tesoreria** di Digital Empire (ADR-020, nata lo stesso giorno di questo ingest, 2026-09-03, ancora a registro vuoto). Sintesi:

**Cosa fa il video che la Tesoreria non fa ancora:** connessione diretta al gestionale (QuickBooks via OAuth, la Tesoreria è 100% manuale), un motore di allerta con soglie in codice (la Tesoreria ha le stesse regole scritte solo come prosa negli agenti, non calcolate), uno scadenzario crediti per cliente (manca un campo data-scadenza in `tesoreria.py`), un cancello anti-invenzione automatico sull'output interpretato (la Tesoreria ha lo stesso principio come "Legge 2" ma nessun controllo automatico), un test di determinismo/regressione, un livello esplicito di "parametri esterni" (budget, fido, margini di listino) come input di prima classe.

**Cosa fa già la Tesoreria che il video non tratta:** è pensata per due soci che lavorano in parallelo (JSONL ad accodamento, mergiabile — il video è un flusso a operatore singolo), correzione per rettifica mai per cancellazione (già collaudata con 5 movimenti di prova), la distinzione previsto/fatturato/incassato/perso (stessa disciplina del video ma codificata indipendentemente), 5 agenti con confini di responsabilità scritti e supervisione C-suite (`cfo-empire`), la regola del passato vuoto dichiarata come legge attiva anche in assenza di dati.

**5 consigli concreti** (dettagliati nel deliverable): dizionario di soglie commentate in `tesoreria.py` sul modello del Prompt 4; campo `--scadenza` sulle entrate fatturate per uno scadenzario reale; `verifica_report.py` leggero per le risposte in prosa degli agenti Tesoreria; test di determinismo/regressione su `calcola()`; un terzo tipo di dato "parametro esterno" (budget/fido/margini) accanto a entrate e spese.

## Nota di trasparenza — limiti della fonte

Copertura parziale dichiarata: 82/226 frame unici guardati (36,3%), tutti i 6 prompt e le sezioni chiave del report letti per intero, ma il codice sorgente negli editor (`metriche.py`, `costruisci_command_center.py`, `verifica_dashboard.py`) non è stato ingrandito riga per riga — solo ciò che i prompt/il Notion dichiarano sul codice è riportato, mai il codice stesso come se fosse stato letto per intero. I sette documenti di riferimento citati per ogni skill (glossario metriche, formule coi limiti, ecc.) non sono mai aperti a schermo, solo nominati. Vedi `coverage.md` nel run per il dettaglio completo, capitolo per capitolo.

## Connessioni

- [[Tool_Tesoreria_Digital_Empire]] — la Tesoreria di DE (ADR-020), oggetto del confronto punto per punto in `confronto-tesoreria.md`; nata lo stesso giorno di questo ingest.
- [[Source_Artem_Novitckii_Caroselli_ChatGPT]] — stesso batch `max17`, stesso pattern di sessione (pipeline Empire Studio completa, video guardato per davvero frame per frame, poi confronto con un sistema DE esistente).
- [[Tool_Memory_Wiki_Bridge]] — il ponte per cui questa ingestione esiste come pagina wiki invece di restare solo in `empire-studio/knowledge/`.
- [[Tool_Conoscenza_Empire_Agente]] — gerarchia C-suite sotto cui vive `cfo-empire`, il supervisore dichiarato della Tesoreria oggetto del confronto.
