# ADR-028 - Niente blocca tutto - un impedimento ferma solo se stesso, mai il resto del lavoro

- **Stato:** ATTIVA — LEGGE PERMANENTE, non una decisione di progetto
- **Data:** 2026-09-09
- **Ordinato da:** Max, testuale: *"se ci sono cose che bloccano non devono bloccare. Mai, non
  ci deve mai essere niente che blocca un qualcosa. [...] semplicemente non devono bloccare il
  lavoro, si tengono da parte e intanto si continua con il lavoro, sempre non ci deve mai
  essere un qualcosa che mi blocca tutto, a meno che non sia proprio infattibile. [...] questa
  mettila come legge, sia per te una legge tua Emperator, sia come legge dell'azienda."*
- **Nasce da:** ADR-027 (coniato un'ora prima, stesso filone) — lì ho corretto UN caso
  (S0/LANCI). Max ha chiesto di smettere di correggere caso per caso e fissare il principio
  generale una volta per tutte.
- **Tocca:** ogni ADR, task, gate o regola futura di tutta la holding — Emperator, Gael, Neri,
  qualunque agente, qualunque ecosistema. Non è un ADR di dominio, è una legge trasversale.

---

## Contesto

Tre volte nello stesso filone ho scritto o applicato una regola che fermava PIÙ del necessario:
1. ADR-025 decisione 6 diceva "se S0 non chiude, non si costruisce nient'altro dell'ecosistema"
   — un blocco totale scritto per dare priorità all'incasso, ma letto (da me) come motivo per
   fermare 9 micro-task che non c'entravano nulla con l'incasso.
2. L'ho applicato alla lettera in CP-20260909-DA2P: ho detto a Gael che la task 1️⃣ intera era
   "formalmente ferma" per 3 gesti che solo Max può fare.
3. Max ha dovuto correggermi due volte in un'ora (prima ADR-027 sul caso specifico, ora questa
   legge sul principio) — lo stesso errore, a scala crescente.

**Il pattern sotto i tre casi:** un impedimento reale (manca una firma, manca una credenziale,
manca un gesto umano, manca un componente, manca una decisione su cosa fare) veniva trattato
come se paralizzasse tutto ciò che gli sta vicino, invece che SOLO la cosa che dipende
letteralmente da lui. Questo vale anche per gli impedimenti "importanti" — non solo per quelli
minori già coperti da ADR-005.

---

## Decisione

**Nessun impedimento ferma mai più del suo perimetro esatto.** Regola unica, senza eccezioni
salvo una:

**1. Un impedimento blocca SOLO ciò che dipende letteralmente da lui — mai il lavoro intorno.**
Prima di dichiarare qualcosa "fermo", si chiede sempre: *"cosa, esattamente, non posso fare
senza questo? E cosa invece posso fare benissimo lo stesso?"* La seconda lista è quasi sempre
più lunga della prima, ed è quella su cui si continua a lavorare.

**2. Quello che non si può o non si vuole fare ORA si tiene da parte, non si cancella e non
ferma il resto.** Tre forme, secondo il motivo:
   - **Manca un gesto/decisione solo di Max** (firma, credenziale, gesto fisico) → ADR-026: si
     porta a lui attivamente, in cima a `STATO-EMPIRE.md`, e si continua a lavorare intorno.
   - **È minore o rimandabile** → ADR-005: `BACKLOG.md`, non ferma la costruzione.
   - **È importante ma Max o Gael scelgono di non farlo ORA** (non "non si può", ma "non lo
     vogliamo adesso") → stessa cosa: si segna dove va segnato (BACKLOG, task, nota nel piano)
     e si continua con il resto. Non farlo ora non è un blocco, è una priorità — e una priorità
     non ferma nient'altro.

**3. L'unica eccezione è l'infattibilità vera: qualcosa tecnicamente o fisicamente impossibile
in questo momento**, non "scomodo", non "richiede un'altra persona", non "non l'abbiamo ancora
deciso". Esempio reale che RESTA bloccante: non si può dichiarare "il pagamento vero è
avvenuto" se nessun pagamento vero è avvenuto — non è un'opinione, è un fatto che non esiste
finché non esiste (§3 emperator.md, prova non dichiarazione). Quello che NON è infattibilità:
"serve una firma di Max" (si chiede), "serve un conto su un fornitore" (si apre quando si apre,
nel frattempo si scrive il codice che lo userà), "non sappiamo ancora il prezzo" (si costruisce
tutto il resto e si inserisce il prezzo quando arriva).

**4. Chi scrive un nuovo gate, ADR o regola con parole tipo "non negoziabile", "blocca tutto",
"non si procede finché" deve scrivere ESATTAMENTE cosa blocca — mai lasciarlo implicito.** Una
frase come "se X non chiude, non si costruisce nient'altro" è vietata da ora: si scrive "se X
non chiude, non passa SOLO il gate Y" — nominando il gate, non "tutto". Vale per me che scrivo
ADR, vale per chiunque altro nella holding scriva una regola di governo.

**5. Questa legge non abolisce i gate che esistono per un buon motivo** (ADR-009 sui nuovi
ecosistemi, `lan-gate` senza scrittura, la prova reale di un pagamento). Non toglie NESSUN
controllo. Restringe solo il RAGGIO di ogni controllo al minimo che serve per fare il suo
lavoro — mai un raggio più largo "per sicurezza" o per pigrizia di scriverlo preciso.

---

## Conseguenze

**Diventa vero, da ora, sempre:**
- Ogni volta che scrivo "bloccato", "fermo", "non si può procedere" — devo poter rispondere
  subito alla domanda "bloccato ESATTAMENTE su cosa, e cos'altro invece si può fare?". Se non
  so rispondere, non ho ancora finito l'analisi, e non lo scrivo come blocco.
- Ogni checkpoint che segnala un impedimento elenca in modo esplicito cosa NON è impedito
  (stesso principio già applicato in CP-20260909-DA2P/HV8Q, ora obbligatorio sempre, non solo
  quando me ne ricordo).
- ADR-025 decisione 6 (già corretta da ADR-027) è il primo esempio applicato; ogni futuro
  "gesto zero"/"prerequisito non negoziabile" in un nuovo ecosistema si scrive da subito nella
  forma stretta del punto 4, non nella forma larga che ho usato per LANCI.

**Resta vero, immutato:**
- ADR-002 (memory-first), ADR-003 (wrap non riscrittura), ADR-006 (ciclo 9 passi), ADR-009
  (gate nuovi ecosistemi), ADR-013 (niente blob pesanti) restano gate veri — restano, solo
  scoping più stretto se in futuro si scoprisse che bloccano più del necessario.
- La Legge Suprema (§3 emperator.md, prova non dichiarazione) resta sopra a tutto: non si
  dichiara chiuso un gate che non lo è per aggirare questa legge. "Niente blocca tutto" non
  vuol dire "si finge che sia fatto" — vuol dire "si lavora su tutto il resto mentre quella
  cosa specifica resta onestamente aperta".

**Costa:**
- Un controllo in più ogni volta che scrivo o applico una regola di blocco: verificarne il
  perimetro esatto prima di dichiararlo, non dopo che qualcuno lo scopre troppo largo.

---

## Come si verifica che questa legge sia rispettata

Non è uno schema dati, è un comportamento — verifica a posteriori, come ADR-026: se un
checkpoint o una task futura dichiara qualcosa "bloccato"/"fermo" senza elencare cosa NON lo è,
o se un nuovo ADR/gate usa "non negoziabile"/"blocca tutto" senza nominare il perimetro esatto,
è una violazione di questa legge e va corretta nel prossimo checkpoint che la trova — stessa
disciplina di ADR-026.

---

## Rapporto con gli ADR esistenti

- **ADR-005 (backlog non blocca)** — questa legge ne generalizza il principio da "blocchi
  minori" a "ogni impedimento, anche importante, salvo vera infattibilità".
- **ADR-026 (blocchi mai silenziosi)** — resta la regola su COME si comunica un blocco reale
  (attivamente, in cima); questa legge aggiunge il QUANTO deve fermare (solo se stesso).
- **ADR-027 (S0 non blocca LANCI)** — primo caso applicato, nato un'ora prima di questa legge
  che lo generalizza.
- **Direttiva Max 2026-08-31 (niente si scarta)** — stessa famiglia di principio dal lato
  opposto: lì niente si cancella, qui niente ferma tutto. Insieme: il lavoro si tiene tutto e
  procede sempre, si può solo riordinare, mai fermare o buttare.

---

*Legami: [[ADR-005]] · [[ADR-026]] · [[ADR-027]] · [[ADR-009]] ·
`.claude/agents/emperator.md` §7 · `company/Memory/BACKLOG.md`*
