---
Type: PROJECT
Status: Active
Tags: #competitor #andrei-pascu #site-study #pre-mortem #god-emperor-doom
Created: 2026-09-07
Last updated: 2026-09-07
---

# PRE-MORTEM DELL'ESECUZIONE — studio totale Andrei Pascu

**Obbligo 5 di GOD EMPEROR DOOM, rimasto aperto alla chiusura del 2026-09-07 mattina.**
Il piano ([dossier 33](../../../PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md)) ha già la sua
PARTE IV — «come questo piano può rompersi». Questo documento è un'altra cosa: **il piano è scritto
bene e l'esecuzione sta già andando storta in tre punti misurabili oggi**. Non è previsione: è
un'autopsia fatta da vivo, con i numeri contati sul disco il 2026-09-07.

> **Il metodo:** si finge che fra due settimane lo studio sia dichiarato «chiuso» e sia un fallimento.
> Poi si scrive perché. Solo le cause che hanno **già un segno visibile oggi** entrano qui.

---

## LE TRE CAUSE CHE HANNO GIÀ UN SEGNO OGGI

### 1. Alla fine avremo atlanti visivi e zero teardown di copy — il prodotto che lui vende davvero

**Il segno, misurato:** il Passo 3 del piano pretende **tre** artefatti per sito — `NN-<slug>.md`,
`NN-<slug>-ATLANTE.md`, `NN-<slug>-COPY.md`. In `reports/` ci sono **16 file e zero `-COPY.md`**
(i tre che `grep -i copy` trova sono nomi di pagina: `01-andrei-copy-home`, `05-copy-mentorship`,
`06-manuale-del-copywriter`). Onda A è a 6 pagine catturate su 9 e **non ha prodotto un solo
teardown di copy**.

**Perché è la causa più grave:** il piano stesso (P4-A2) dice che *«il copy è il prodotto che lui
vende davvero»*. Uno studio che torna con la palette e la scala tipografica di un copywriter, e non
con le sue formule, ha studiato la vetrina e saltato la merce. La Fabbrica Siti sa già fare pagine
belle; quello che non sa fare è **scriverle**.

**Perché sta succedendo:** l'atlante visivo è più facile — le immagini ci sono già, il lavoro è
descrittivo. Il teardown di copy chiede di leggere 4.000 parole e di estrarne una regola. Quando la
sessione si accorcia, cade sempre il pezzo più caro. **È una deriva verso il facile, non una
dimenticanza.**

**Rimedio, e non è un promemoria:** la chiusura di un'onda non la dichiaro io. La conta uno script
sul disco (`stato_onde.py`, vedi causa 3) che pretende i tre file. Un'onda con zero `-COPY.md` è
**rossa**, e resta rossa anche se i rapporti sono bellissimi.

---

### 2. I rapporti crescono, la Fabbrica no

**Il segno, misurato:** `reports/` ha **16 documenti** e ~2.400 righe di prosa. In
`.claude/skills/fabbrica-siti/CLAUDE-SITI.md` i riferimenti a tutto l'ecosistema studiato
(`andrei|apsales|armageddon|speedrun`) sono **5 righe in tutto**. Il rapporto fra ciò che sappiamo
e ciò che la Fabbrica ha incassato è di circa **1 a 400**.

**Perché è grave:** è esattamente il modo di rottura che il piano si era già scritto da solo
(«torno a trattare il tutto come dodici documenti»). Il piano lo aveva previsto e **sta accadendo lo
stesso** — che è la definizione di un rischio non presidiato: previsto a parole, senza un gate.
È anche la stessa malattia dell'[Ultimo Metro](../../../company/Memory/BACKLOG.md): roba finita che
non esce.

**Rimedio:** il delta alla Fabbrica smette di essere l'ultima spunta di una lista e diventa **la
prima riga di ogni rapporto**, in un blocco fisso a tre voci — `CANONE:` / `PATTERN:` / `GATE:` —
dove è ammesso scrivere `niente, e il perché`. Un rapporto senza quel blocco non è finito.
Alla fine di ogni onda, i delta si travasano in `CLAUDE-SITI.md` **prima** di aprire l'onda dopo.

---

### 3. Lo stato è scritto a mano, quindi mente

**Il segno, misurato:** la tabella STATO di `ECOSISTEMA.md` dichiara **Onda A: 0 su 9**. Sul disco
ci sono **6 cartelle di cattura di Onda A complete di `scheda.json`** (`12-claude-speedrun-v2`,
`13-apsales-v2`, `14`-`17-arma-*`). Lo stato era vecchio di un giorno ed era già falso di sei
pagine, cioè del 67% dell'onda.

**Perché è grave:** questo studio dura giorni e attraversa chat che muoiono col contesto pieno.
L'unico ponte fra una sessione e l'altra è lo stato scritto. **Un ponte che mente manda a sbattere**
— è la stessa legge dei puntatori stale già scritta in `CLAUDE.md`. Il rischio concreto non è
perdere lavoro: è **rifarlo**, o peggio dichiarare chiuso ciò che è a metà.

**Rimedio:** lo stato delle onde non si scrive più a mano. Lo conta uno script che guarda il disco —
cartelle con `scheda.json`, rapporti presenti per slug — e riscrive la tabella. Chi vuole sapere a
che punto siamo esegue lo script, non legge una riga di prosa.

---

## LE DUE CAUSE SENZA SEGNO, TENUTE D'OCCHIO

| Causa | Segno da sorvegliare | Cosa si fa quando appare |
|---|---|---|
| **Il `custom.css` di Squarespace annega nel framework.** Il valore delle 8 pagine di Onda B è il CSS scritto da lui; `src/` scarica anche ventimila righe di framework | in `src/` di una pagina T2 non compare nessun file `custom-css` | si va a prenderlo dritto all'URL pubblico `static1.squarespace.com/static/custom-css/602126db7a4e4c01fd9babb6/...` e lo si salva a parte, dichiarandolo |
| **Il limite di spesa colpisce a metà onda** (già successo due volte in 24 h sul run dei video, sempre dentro batch paralleli) | — | la coda delle catture è **sequenziale**, non parallela; ogni cattura è idempotente (`scheda.json` esiste → salta); si riparte misurando il disco |

---

## LA CONTROMISURA UNICA, IN UNA RIGA

Le tre cause vive hanno la stessa radice: **il giudizio ha sostituito la misura**. Tre volte su tre
il rimedio è lo stesso — *ciò che dichiara "fatto" deve essere una macchina che guarda il disco, non
una frase che ho scritto io*. Da qui nasce `scripts/stato_onde.py`.

---

## Connessioni
- [[33-PIANO-STUDIO-TOTALE-ANDREI-PASCU]] — il piano e i suoi sette giri di critica
- [[ECOSISTEMA]] — l'elenco vero e lo stato delle onde
- [[32-DOSSIER-FABBRICA-SITI]] — dove i delta devono finire
- `CP-20260907-ECX7` — il checkpoint che ha lasciato aperto l'obbligo 5
