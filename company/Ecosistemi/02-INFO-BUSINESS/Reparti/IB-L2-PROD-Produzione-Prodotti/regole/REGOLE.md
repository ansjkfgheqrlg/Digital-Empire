---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #infobusiness #prodotto #produzione #IB-L2-PROD
Created: 2026-06-21
Last updated: 2026-06-21
---

# Regole Non Negoziabili — IB-L2-PROD Produzione Prodotti

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Nessuna produzione senza WF-VALIDAZIONE PASS

Nessun prodotto entra in WF-CORSO o WF-EBOOK senza brief validato: score ≥60/100 da IB-PROD-VALID
**e** MVP test 7gg superato (5 "sì, lo comprerei" reali da persone ICP).

IB-PROD-VALID è il gate d'ingresso bloccante dell'intera area. Idea che non passa → BACKLOG
(ADR-005), mai in produzione, con motivo registrato in `infobusiness/prod/validazione/state.json`.

**Perché esiste questa regola:** produrre su intuizione brucia il raw più prezioso e il tempo
del team. Il gate quantitativo è ciò che separa un prodotto che vende da un prodotto che esiste.

---

## R2 — Il MKD copre il 100% degli atomi della fonte

Il MKD prodotto da IB-PROD-MKD copre tutti gli atomi informativi della fonte. IB-PROD-QA verifica
con checklist quantitativa (n. atomi MKD vs n. atomi fonte). Copertura sotto il 100% = FAIL.

Il rapporto lunghezza MKD / lunghezza fonte deve essere ≥1: la trasformazione è espansione, mai
sintesi. Un MKD più corto della fonte è una violazione, non un'ottimizzazione.

**Perché esiste questa regola:** il valore dell'area è il raw posseduto. Perdere atomi nella
trasformazione significa buttare il capitale informativo che giustifica l'intero prodotto.

---

## R3 — IB-L2-PROD non monta video e non scrive codice di piattaforma

Il montaggio video è di 03-CONTENT-FACTORY (handoff `HC-CF-IB-01`). La costruzione del corso su
Supabase+Next.js è degli agenti `formazione-*` coordinati via `HC-PL-IB-01`. Nessun agente di
IB-L2-PROD monta MP4, tocca il codice della piattaforma, configura Supabase o modifica la UI corso.

IB-PROD-WRITER produce lo script; 03-CF lo trasforma in video. IB-PROD-PLATFORM coordina e verifica
il deploy; non lo scrive a mano. Ogni modifica passa dall'handoff contract con i suoi acceptance criteria.

**Perché esiste questa regola:** la responsabilità tecnica del video e della piattaforma è di altri
reparti. IB-L2-PROD che le invade crea conflitti di responsabilità e regressioni che nessuno presidia.

---

## R4 — IB-PROD-QA è bloccante su ogni gate del workflow

Nessun MKD, nessun curriculum, nessuno script, nessun deploy, nessun asset esce senza gate verde
di IB-PROD-QA. Il gate non ha deroga per urgenza. IB-PROD-QA blocca, non suggerisce.

Se il gate QA fallisce 2 volte consecutive sullo stesso prodotto, IB-PROD-QA non itera all'infinito:
segnala a IB-COORD-PRODOTTO che riesamina brief/curriculum a monte. L'urgenza del committente non
abilita un bypass: solo IB-COORD-PRODOTTO può autorizzare una consegna parziale con nota di rischio.

---

## R5 — Ogni lezione ha 1 outcome verificabile + esercizio

Ogni lezione del curriculum dichiara 1 outcome misurabile e contiene un esercizio pratico che lo
produce. Nessuna lezione teorica senza esercizio. "Capire" / "conoscere" non sono outcome
verificabili; "produrre / configurare / mostrare che funziona" lo sono.

IB-PROD-CURRIC dichiara l'outcome nella mappa lezioni. IB-PROD-QA verifica nel gate. Lezione senza
outcome misurabile = FAIL automatico senza analisi aggiuntiva.

---

## R6 — Nessun placeholder e nessun lancio di ombre

Nessun asset (copertina, workbook, certificato, ebook, slide) esce con placeholder, lorem ipsum,
immagine segnaposto o link rotto. Nessun corso si consegna a IB-L2-VEND prima di esistere sulla
piattaforma reale con smoke test "studente fantasma" verde sul modulo 1.

IB-PROD-DESIGN verifica zero placeholder; IB-PROD-PLATFORM verifica l'esistenza reale; IB-PROD-QA
conferma con smoke test. Un prodotto annunciato e non apribile è una violazione del posizionamento DE.

---

## R7 — Nessun claim senza prova nel prodotto

Nessuno script di lezione e nessun capitolo di ebook dichiara un risultato ("ottieni X", "in Y
giorni", "il 90% di chi...") senza prova o motivazione esplicita. Il Mandato Art.2 (prove non
promesse) vale dentro il prodotto, non solo nel marketing.

Committente o brief che chiede claim aggressivi senza dato → risposta corretta: "dichiariamo cosa
il prodotto produce e mostriamo l'esercizio che lo dimostra; il numero senza misurazione resta [DM]."
IB-PROD-QA verifica nel gate brand voice. Claim non motivato = FAIL.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ib-prod-qa]] · `agenti/ib-prod-qa.md` — esecutore dei gate bloccanti
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — confini IB-L2-PROD vs 03-CF vs PLATFORM in dettaglio
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` — Art.2 come fonte di R7 e R6
