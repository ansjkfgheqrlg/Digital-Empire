> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.1 (Team L4) + sez. 4a (WF-CORSO step 2)

# T-CURRICULUM — Team Curriculum Design

> Funzione L4 · Reparto: IB-R1-PRODOTTO · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

Trasformare il Master Knowledge Document (MKD) in una **struttura di corso completa**:
moduli, lezioni, obiettivi di apprendimento misurabili, prerequisiti, esercizi, durata
dichiarata. Ogni lezione deve avere esattamente 1 outcome verificabile — niente lezioni
"informative" senza trasformazione misurabile.

---

## Agente proprietario

`ib-curriculum-architect` (worker, tier Sonnet)

---

## Input

- MKD validato da `T-MKD` (copertura 100% atomi)
- Brief prodotto: ICP, livello baseline studente, durata target corso, modalità delivery (video/testo)

---

## Output

- `curriculum-[prodotto].md` con:
  - Lista moduli (numerati) con titolo e descrizione
  - Per ogni modulo: lista lezioni con outcome verificabile, esercizio, durata stimata
  - Prerequisiti per modulo/lezione
  - Durata totale del corso dichiarata

---

## Gate di uscita obbligatorio

> "Ogni lezione ha 1 outcome verificabile; durata totale dichiarata."
> Verifica: revisione manuale del curriculum da parte di `ib-prodotto-coordinator`.

---

## Skill nuova richiesta

`course-architect` (da creare via 07-FORGE) — standardizza MKD → curriculum,
kernel ≤500 righe. Fino alla creazione: `ib-curriculum-architect` opera con istruzioni inline.

---

## Connessioni

- [[IB-R1-PRODOTTO]] — reparto di appartenenza
- [[T-MKD]] — fornitore dell'input (MKD)
- [[T-PIATTAFORMA]] — destinatario del curriculum strutturato
- [[WF-CORSO]] — workflow che include questa funzione come step 2
