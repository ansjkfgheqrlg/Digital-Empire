# EMP-APPLAN1 — Piano chirurgico Andrei Pascu: P0 chiuso, P1 da rilanciare

- **Aperto:** 2026-09-09
- **Stato:** APERTA
- **Come si riprende:** dire `EMP-APPLAN1` in una chat nuova dentro Digital Empire.
- **Checkpoint di origine:** [CP-20260909-98ZG](../checkpoints/CP-20260909-98ZG.md)
- **Ordine di Max (testuale, 2026-09-09):** *«forse è il momento di fare un piano chirurgico…
  estremamente dettagliatissimo, che devi fare utilizzando un paio sicuramente di doom bot, forse
  anche qualche sentinella scagnozzo, e anche con fable, così che venga fatto benissimo il piano —
  il piano proprio per implementazione, aggiornamenti, miglioramenti da fare sull'azienda basati su
  tutti gli studi, su tutta la conoscenza e formazione acquisita.»*

**LA MISSIONE, in una riga:** trasformare tutto lo studio Andrei Pascu in un piano eseguibile che
**fa incassare Digital Empire** — non in altra documentazione.

---

## LA PRIMA COSA DA FARE ALLA RIPRESA

Misurare sul disco, non fidarsi di questa riga:
```
ls "competitor/Andrei Pascu/piano-implementazione/"
```
Attesi 2 file: `DRAFT-V1-A-lanci.md` e `DRAFT-V1-B-capacita.md`.

---

## DOVE SIAMO NEL PROCESSO

Il piano si critica tre volte (dottrina Max: ogni giro attacca il giro prima, non l'originale).

| Giro | Cosa | Chi | Stato |
|---|---|---|---|
| **P0** | I due draft V1 | 2 Doom Bot (opus), in parallelo | ✅ **FATTO**, su disco |
| **P1** | Critica dei due draft | 2 Sentinelle (sonnet) | ⬜ **lanciato e perso con la chat — DA RIFARE** |
| **P2** | Critica della critica | Fable | ⬜ non iniziato |
| **Assemblaggio** | Documento unico | 1 Scagnozzo (haiku) | ⬜ non iniziato |
| **P3** | Esecutivo finale + PDF | Emperator, non delegato | ⬜ non iniziato |

---

## COSA C'È GIÀ (non rifare)

### Fasi chiuse prima di questa
- **EMP-APDOC1** (CP-20260909-2N8Q): 4 documenti ufficiali su Andrei Pascu, completi con PDF e
  doppioni in `documentazione Empire/competitor/Andrei Pascu/`.
- **EMP-APIMPL1** (CP-20260909-4RZV): 12 candidati applicati su 13 file `SKILL.md`
  (cro-copy-architect, popups, lead-magnets, ads, ad-creative, emails, cold-email,
  sales-enablement, discovery-call-brief, proposal-gate, preventivo-auto, revops, beast-preventivi).
  **Non ri-proporli**: la lista esatta è nella tabella 🟢 di `MIGLIORAMENTI-DIGITAL-EMPIRE.md`.

### I due draft V1 — cosa contengono in sintesi
- **DRAFT-V1-A-lanci.md** — 27 azioni. Ritrovamento portante: **gli 8 controlli di ADR-024 non
  esistono come codice**, quindi il «primo gate obbligatorio dell'ecosistema LANCI» oggi è solo una
  frase (azione AP-034, `catena.py`, rango 1). Divide tutto in **corsia C1** (libera, 17 azioni,
  zero collisione con Gael) e **corsia C2** (riservata a Gael dentro le sue micro-task).
  Propone ADR-029 per due articoli nuovi di `CLAUDE-SITI.md` (§13 e §14).
- **DRAFT-V1-B-capacita.md** — 4 verdetti: AP-006 **NO-GO** sull'automazione preventivi (il
  processo gira ~0 volte al mese) ma GO su 2 micro-patch; AP-012 **GO ristretto**; AP-018 **NO-GO
  netto** (anti-posizionato rispetto a «l'agenzia progettata per essere licenziata»); AP-019/020
  **GO chirurgici**. Più 4 scoperte collaterali verificate sul disco (content-forge duplicato,
  contraddizione interna in revops, tesoreria a zero righe, puntatore a `skill-forge` inesistente).

Entrambi i draft **dichiarano da soli i propri punti deboli** in fondo (§10): il giro P1 parte da lì.

---

## COME SI RILANCIA IL GIRO P1 (2 Sentinelle, sonnet, in parallelo, background)

**Sentinella 1 — angolo GOVERNO/COERENZA/COLLISIONE.** Deve leggere entrambi i draft e:
1. verificare sul disco almeno 8 fatti portanti dichiarati nei draft (esistenza di `catena.py`,
   contenuto reale di ADR-024 §4/§6, decisioni 2/3/4 di ADR-025, campi degli schemi in
   `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/schemi/*.json`, i «sei rossi su sei» di `MT-4GNU`,
   engagement scoring in `revops/SKILL.md`, diff `content-forge`/`content-forge2.0`,
   `tesoreria/entrate.jsonl` vuoto);
2. attaccare la divisione C1/C2 cercando azioni mal classificate;
3. cercare contraddizioni non dichiarate con ADR-003/005/016/019/023/024/025/026/028;
4. trovare **tutte** le sovrapposizioni fra draft A e draft B;
5. verificare il conteggio dei candidati verdi e i buchi nella numerazione AP-034..060.
Output: verifica fatti (tabella VERO/FALSO/GONFIATO), colpi ordinati per gravità con riparazione,
azioni da uccidere, azioni da fondere, **la sua obiezione più forte**.

**Sentinella 2 — angolo DENARO E VERITÀ.** Deve leggere entrambi i draft e:
1. classificare ogni azione: **EURO DIRETTO / ABILITA UN EURO / SOLO INFRASTRUTTURA / SOLO
   DOCUMENTO**, con i totali;
2. rispondere sì/no a: *il piano stesso è il pezzo 26 di ULTIMO METRO?*;
3. smontare le stime di effort (`catena.py` in 4-8h è credibile con taratura e falsi positivi?);
4. trovare i numeri inventati **non dichiarati** (fascia 27-47 €, valore 100 € dell'opzione futura,
   soglie 150/400 €, tetto di 3 rami);
5. trovare **il buco**: una lezione grossa dello studio che nessuno dei due draft ha convertito in
   azione (rileggere `ANDREI-PASCU-DOSSIER-COMPLETO.md` e `site-study/SINTESI-METODO.md`);
6. contestare l'ordine: `catena.py` al rango 1 è davvero la cosa giusta per un'azienda che non ha
   ancora venduto niente? Proporre la sequenza che porta a incassare prima.

**Regola per entrambe:** verifica sul disco, mai a memoria; «non verificabile da qui» invece di
assumere; ogni colpo con una prova, non un'impressione.

---

## POI (dopo che P1 rientra)

- **P2 — Fable** (model `fable`): riceve i due draft **e** le due critiche. Attacca la critica, non
  l'originale. Cerca cosa hanno sbagliato le Sentinelle, cosa hanno ucciso che andava salvato, e
  cosa nessuno dei quattro ha visto.
- **Assemblaggio — Scagnozzo** (haiku): fonde tutto in un documento unico, struttura data da
  Emperator, nessuna decisione propria.
- **P3 — Emperator**: sintesi esecutiva, decisioni finali, priorità, e **PDF standard-oro**
  (motore `PIANO-MAESTRO/scripts/pdf_engine_empire.py`, modelli già pronti in
  `competitor/Andrei Pascu/build_*.py`) + doppione in `documentazione Empire/`.

**Nome file pianificato per il documento finale:**
`competitor/Andrei Pascu/piano-implementazione/PIANO-IMPLEMENTAZIONE-ANDREI-PASCU.md` + `.pdf`.

---

## VINCOLI DA NON DIMENTICARE

- **ADR-028** (legge permanente, appena scritta): niente blocca tutto. Ogni azione del piano deve
  dichiarare **esattamente** cosa blocca — e nessuna azione può diventare precondizione di una
  micro-task di Gael.
- **Gael sta costruendo LANCI adesso** (`TASK-LANCI-BUILD-W3`): la corsia C2 non si esegue da
  un'altra sessione, si consegna a lui.
- **REGOLA PUNTATORI:** le voci nuove di `STATO-EMPIRE.md` vanno **in cima** (l'hook legge solo la
  prima riga e i primi 30.000 caratteri).
- Il blocco ⚠️ ATTIVAZIONE FORZE (ADR-015) per questo lavoro è già scritto in cima a
  `STATO-EMPIRE.md`: quando il piano chiude, va tolto.
