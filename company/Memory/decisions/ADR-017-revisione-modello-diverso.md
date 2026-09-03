# ADR-017 — Il lavoro ad alto rischio lo rilegge un motore di famiglia diversa

- **Stato:** ATTIVO (in **pilota**, perimetro stretto — vedi §4)
- **Data:** 2026-09-03
- **Approvato da:** Max, 2026-09-03 (*"qualsiasi tuo consiglio io lo approvo"*)
- **Sostituisce:** `ADR-PROPOSTA-cross-model-review.md` (2026-09-02), che resta agli atti come
  istruttoria completa
- **Estende:** ADR-006 (ciclo di fase a 9 passi), passo 5 — REVIEW indipendente
- **Origine della prova:** video `T7PPX5M6Puo` — Riccardo Belli Contarini, Martes AI

---

## 1. Il problema in una frase

**Chi controlla il nostro lavoro è parente di chi lo fa.**

Il ciclo di fase a 9 passi (ADR-006) prevede una REVIEW indipendente, e i revisori sono davvero
agenti diversi dal costruttore, con prompt e ruoli distinti. Ma **girano tutti sulla stessa
famiglia di modello di chi ha scritto il lavoro**. È come far correggere il compito al fratello
gemello: gli errori che uno non vede per formazione, non li vede nemmeno l'altro.

Non è una questione di quale motore sia più bravo. È che due giudici addestrati insieme
**condividono i punti ciechi**.

---

## 2. La prova — tre casi su tre, non teoria

| Caso | Cosa aveva detto il primo giudice | Cosa ha trovato il motore di famiglia diversa |
|---|---|---|
| **MaReply** (gestisce account Instagram di clienti) | «pronta per la produzione» | **2 falle gravi**: account dirottabile via invito (nessuna verifica email); messaggi diretti duplicati per assenza di lock atomico — spam, doppio consumo di budget, rischio reputazionale |
| **Form candidature** (dati personali di candidati) | nessun rilievo | **4 falle gravi**: endpoint pubblico senza freno né captcha, caricamento file fidato ciecamente lato server, nessun limite alla dimensione dei campi, librerie esterne senza controllo di integrità. Più 10 medie. |
| **Piano "clone Bitly"** (ancora prima di scrivere codice) | piano approvato | **1 falla critica**: chiunque poteva cancellare i link altrui, nessun controllo di proprietà. Più 2 gravi. Rimesso davanti alle obiezioni, il primo giudice ne ha confermate **4 su 5** — incluso un errore che Bitly aveva corretto nel 2016. |

**In tutti e tre i casi il primo giudice aveva già dato il via libera.**

---

## 3. La decisione

Per i lavori **ad alto rischio su dati e credenziali**, la REVIEW indipendente del passo 5 di
ADR-006 include **un secondo passaggio con un motore di famiglia diversa**.

Regole:

1. **Si aggiunge, non sostituisce.** I revisori attuali restano e girano per primi. Il secondo
   motore legge dopo di loro.
2. **Stessa scala di gravità** già in uso (critico / alto / medio / basso / informativo), così
   i due giudizi sono confrontabili.
3. **L'uomo resta in mezzo.** I rilievi del secondo giudice si leggono e si filtrano, non si
   applicano alla cieca. Nel caso studiato, l'autore ha scartato uno dei rilievi come falso
   problema, e aveva ragione.
4. **Il disaccordo si dichiara, non si appiana.** Se i due giudici dissentono, il rapporto
   riporta entrambe le posizioni e la decisione la prende Max.

---

## 4. IL PERIMETRO — stretto per scelta, e perché

Max ha approvato tutto. **Io lo attivo lo stesso in pilota su un sistema solo**, e dico perché,
perché nascondere la ragione sarebbe peggio che non attivarlo.

L'istruttoria che ha prodotto questa regola **dichiara onestamente di non avere prove
sufficienti**: una sola fonte, tre casi, una sola agenzia, nessuna misura di quanto spesso il
secondo giudice trovi davvero qualcosa di nuovo, e nessun tasso di falsi allarmi. Approvarla su
tutto l'Impero sulla base di tre aneddoti significherebbe fare l'errore che questa regola stessa
esiste per impedire: **fidarsi di un giudizio senza averlo messo alla prova**.

**Pilota: `Preventa Outreach`.** È il candidato giusto perché custodisce credenziali di accesso
di terzi e dati di aziende clienti — il rischio è reale, non ipotetico — ed è un sistema che già
gira, quindi il pilota misura su cose vere.

**Gli altri due candidati restano in coda, non esclusi:** `Formazione Empire` (dati studenti,
accessi, pagamenti) e `PreventivoForge` (più clienti sullo stesso impianto, interruttore
abbonamento, dati concessionari).

**Come si esce dal pilota.** Dopo il primo audit sul pilota si scrive in questo stesso ADR:
quanti rilievi ha prodotto, quanti si sono rivelati veri, quanti falsi allarmi, quanto è costato.
Se i rilievi veri superano i falsi allarmi, si estende agli altri due. Se no, si chiude e si dice
perché — e la chiusura vale quanto l'estensione, perché avremo comunque imparato un fatto vero
sul nostro modo di controllare.

---

## 5. Cosa NON cambia

- **Il flusso ordinario resta identico.** La grande maggioranza del lavoro di Digital Empire non
  tocca dati sensibili né credenziali, e continua con i revisori attuali. Chiedere un secondo
  motore ovunque sarebbe spreco travestito da rigore.
- **Nessun secondo abbonamento per tutta l'azienda.** Solo una chiamata mirata sui pochi lavori
  in perimetro.
- **ADR-006 non viene riscritto.** Riceve una clausola in più nel passo 5, valida solo dentro
  questo perimetro.

---

## 6. I costi, dichiarati

- **Una credenziale in più da custodire.** Un secondo fornitore significa una seconda chiave da
  proteggere e ruotare — la stessa superficie di rischio che Digital Empire ha già dovuto
  correggere più volte (voci B-020, B-021, B-023 del backlog). Il costo in denaro è basso
  (~$20 al mese); il costo in attenzione non è zero.
- **Un secondo posto dove qualcosa può rompersi in silenzio.**
- **Beneficio dimostrato solo su sicurezza e dati.** Non c'è prova che serva su testi, contenuti
  o pagine: lì i revisori attuali bastano, ed estenderlo sarebbe ingiustificato.

---

## 7. Il principio, oltre questo caso

> **Un controllo vale quanto la sua indipendenza dal controllato.**
> Non basta che il giudice sia un altro agente: deve poter sbagliare in modo *diverso*.
> Due giudici che sbagliano insieme non sono due controlli — sono un controllo solo, contato due
> volte, con l'aggravante che sembra doppio.

Questo principio va oltre i modelli: vale ogni volta che Digital Empire mette un controllo su sé
stessa. Se il controllore condivide l'origine, il metodo e gli incentivi del controllato, il
controllo è decorativo.

---

## 8. Verifica del non-conflitto

Non contraddice ADR-006 (lo estende con una clausola limitata). Non contraddice ADR-008 (il nuovo
passo ha proprietario, controllore, origine e governo come ogni altro artefatto). Nessun conflitto
con gli ADR attivi da 001 a 016.

---

*Legami: [[ADR-006]] · [[ADR-008]] · [[ADR-016]] · `company/Memory/BACKLOG.md` voce B-042 ·
`memory-empire/knowledge/T7PPX5M6Puo/` (fonte integrale) ·
`second-brain-vault/wiki/sources/Source_Riccardo_Belli_Claude_Codex_Setup.md` ·
`company/Memory/decisions/ADR-PROPOSTA-cross-model-review.md` (istruttoria)*
