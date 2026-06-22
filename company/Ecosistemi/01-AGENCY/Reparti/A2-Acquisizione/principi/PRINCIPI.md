---
Type: PRINCIPI
Status: Active
Tags: #principi #agency #acquisizione #outreach #apsoc #A2
Created: 2026-06-22
Last updated: 2026-06-22
---

# Principi — A2 Acquisizione / Outreach

> Principi operativi del reparto. Guidano le decisioni quando le regole non bastano.
> Le regole non negoziabili (più stringenti) vivono in `regole/REGOLE.md`.

---

## P1 — Si wrappa il runtime, non si riscrive (ADR-003)

La pipeline di outreach gira in produzione e funziona. A2 la avvolge: la registra,
la governa, ne misura gli esiti, ne formalizza il gate. Non riscrive `writer.py`,
non rifà `bibbia_team.py`, non sostituisce gli script LinkedIn. Quando un motore sembra
da cambiare, la risposta è un ADR — non una riscrittura silenziosa. Il motore esegue;
il reparto governa e contabilizza.

---

## P2 — Il gate Bibbia viene prima dell'invio, sempre

Nessun messaggio raggiunge un lead senza essere passato per i 3 check sequenziali della
Bibbia. Il gate non è un consiglio post-hoc: è una barriera pre-invio. Un messaggio che
non passa torna al writer con note precise; non parte "in attesa di fix". La qualità del
copy in uscita è il bene più prezioso del reparto perché protegge sia la deliverability
sia la reputazione dell'agenzia.

---

## P3 — I cap reali proteggono gli account, non rallentano il reparto

500 email/gg con cap 100/h, 20+20+30/gg su LinkedIn, 30 DM/gg su Instagram non sono
obiettivi da spingere: sono limiti di sicurezza. Superarli brucia domini, account e
sessioni — il danno è permanente, il vantaggio è momentaneo. Il reparto preferisce
inviare meno e durare nel tempo. I cap non si alzano senza dati e senza ADR.

---

## P4 — Una variante, un'ipotesi: si impara dai dati reali

I template si fanno evolvere su segnale di reply rate, non su opinione. Un template in
calo per 2 cicli viene segnalato per refresh, non sostituito d'impulso. Ogni variante che
funziona si registra in `agency/outreach` con la sua performance. La conoscenza reale
(quale angolo APSOC converte per quale ICP) vale più di qualsiasi ottimizzazione a sensazione.

---

## P5 — L'agenzia progettata per essere licenziata anche nell'outreach

Il posizionamento di Digital Empire — autonomia del cliente, non dipendenza — vive anche
nel cold outreach. I messaggi non usano dependency-language ("senza di noi non ce la fate").
Il check 3 della Bibbia esiste per questo. Vendiamo un risultato e un percorso, non una
dipendenza. Questo è coerente con l'identità della holding, non un dettaglio di tono.

---

## P6 — Mai rispondere a un "no", mai forzare un sì

Il triage classifica le risposte e un "no" definitivo chiude la conversazione: nessun
follow-up, nessuna insistenza. Forzare un lead già contrario brucia reputazione e non
produce call. Il follow-up multi-touch serve chi non ha ancora risposto o ha obiezioni
aperte — non chi ha detto no. Il rispetto del "no" è parte della deliverability di lungo
periodo del brand.

---

## P7 — Nessuna PII nello schema, prove non promesse nei numeri

I thread di risposta passano il PII-scan prima di ogni store; lo schema di state contiene
solo riferimenti interni e contatori. I KPI senza misurazione restano `[DM]` — non si
inventa un reply rate atteso per rassicurare. Le baseline si stabiliscono al primo ciclo
reale (Mandato Art.2: prove non promesse).

---

## Connessioni

- [[REGOLE]] · `regole/REGOLE.md` — le regole non negoziabili che derivano da questi principi
- [[ARCHITETTURA]] · `ARCHITETTURA.md §3` — il gate Bibbia in dettaglio
- [[ADR-003]] · `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md`
