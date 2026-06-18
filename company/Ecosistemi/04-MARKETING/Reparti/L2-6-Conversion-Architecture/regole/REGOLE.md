---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #conversion #funnel #cro #L2.6
Created: 2026-06-18
Last updated: 2026-06-18
---

# Regole Non Negoziabili — L2.6 Conversion Architecture

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Questo reparto NON scrive copy

Il copy di ogni stage del funnel, di ogni sezione della landing, di ogni variante di test
viene prodotto da L2.1 Copywriting tramite contratto §1.2 del dossier Marketing.

L2.6 produce brief copy (formato, awareness level, obiettivo, sezione APSOC, gate richiesto).
L2.1 produce il testo. Nessun agente di L2.6 scrive headline, body copy, CTA text o email.

**Perché esiste questa regola:** la qualità del copy è presidiata dal gate G1 di A8 (≥80/85).
Se L2.6 scrivesse copy internamente, il gate salterebbe e il sistema di qualità si romperebbe.

---

## R2 — Questo reparto NON implementa pagine

Le pagine, i form, le landing vengono costruite da 06-PLATFORM. L2.6 produce il brief tecnico
approvato. 06-PLATFORM implementa.

Nessun agente di L2.6 modifica HTML, CSS, layout CMS, configura form, o tocca il codice
della landing. Questo vale anche per modifiche "piccole" post-sprint: ogni modifica strutturale
passa dal brief tecnico approvato da CONV-LEAD.

**Perché esiste questa regola:** la responsabilità tecnica è di 06-PLATFORM. L2.6 che tocca
il codice crea conflitti di responsabilità e potenziali regressioni che nessuno presidia.

---

## R3 — Nessuna ottimizzazione senza verdetto A/B statisticamente valido

Una modifica alla landing è un'implementazione. Ogni implementazione richiede un verdetto
di AN3 (WF-AB-TEST) con p-value <0.05 e dimensione campione validata prima di avviare.

Questo vale per:
- Cambiamenti di headline.
- Cambiamenti di posizione CTA.
- Aggiunta/rimozione di sezioni.
- Cambiamenti di copy in sezioni esistenti.

Eccezione unica: fix tecnici critici (es. form rotto, CTA che non funziona su mobile) che
impediscono la conversione → si implementano senza test perché lo status quo è già fallimentare.
In questo caso CA-QA documenta il bypass con motivazione.

---

## R4 — CA-QA è bloccante su tutti gli output del reparto

Nessun funnel design, nessun brief tecnico a 06-PLATFORM, nessun report di audit esce
senza gate verde di CA-QA. Il gate CA-QA non ha deroga per urgenza.

Se il committente ha urgenza → CONV-LEAD può consegnare un output parziale con nota di rischio
esplicita SOLO con approvazione di MKT-Conductor. CA-QA documenta il bypass non autorizzato
se avviene senza questo iter.

---

## R5 — P prima di S in ogni funnel (Art.4.2 Mandato)

La sezione Problema deve precedere la sezione Soluzione in ogni funnel, in ogni landing,
in ogni sequenza email. Non esiste awareness level così alto da saltare il Problema.
Anche per "most-aware": il Problema può essere breve (1 frase), ma deve essere presente.

CA1 verifica nella mappa stage. CA-QA verifica nel gate finale. Violazione = FAIL automatico
senza analisi aggiuntiva.

---

## R6 — Nessun threshold di conversione senza dato reale

I KPI del reparto hanno campo [DM] (Da Misurare) ovunque non esista baseline storica.
Nessun agente dichiara "opt-in rate atteso 30%" o "conversione BoFu attesa 2%" senza dato
reale da misurazione precedente. I [DM] vengono riempiti al primo run reale.

Committente che chiede previsioni di conversione pre-lancio → risposta corretta: "la baseline
si stabilisce al primo funnel live. Possiamo dichiarare la struttura e i punti critici,
non i numeri." (Mandato Art.2: prove non promesse.)

---

## R7 — Nessuno sprint CRO su rumore statistico

Se il traffico sulla landing non è sufficiente per raggiungere la dimensione campione
necessaria per un verdetto statistico in un tempo ragionevole, lo sprint non si avvia.
AN3 (L2.4) è il giudice. Un verdetto "winner" su campione insufficiente è peggio di non
avere verdetto: porta a implementazioni basate su rumore.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ca-qa-conversion-verifier]] · `agenti/ca-qa-conversion-verifier.md` — esecutore del gate
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — confine L2.6 vs 06-PLATFORM in dettaglio
- [[04-ECOSISTEMA-MARKETING-V2]] · Mandato Art.4.2 + Art.2 come fonte di R5 e R6
