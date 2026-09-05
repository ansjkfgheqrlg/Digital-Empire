# EMP-MCC4 — COMPLETAMENTO IMPERO (dossier 30, scaglioni S1..S7)

- **Aperto:** 2026-09-05 · **Stato:** APERTO
- **Ordine di Max:** *«la costruzione di Digital Empire non era finita al 100% — recap,
  analisi, cosa ho davanti, in che ordine, con che priorità, e un piano per fare tutto.»*

## Dove si riprende

**Leggi per primo:** `PIANO-MAESTRO/30-PIANO-COMPLETAMENTO-IMPERO.md`.
È il piano intero, con i gate eseguibili. Questo file dice solo dove si è arrivati.

## Stato al momento della scrittura

- **Analisi e piano: FATTI.** Tutti i numeri misurati coi comandi il 2026-09-05.
- **Costruzione: NON INIZIATA.** Il piano è PROPOSTO e aspetta il via di Max.
- **Impero: 92% sulla carta, 18% vivo** (calcolo in dossier 30 §3).

## Il prossimo passo, esatto

**S1.** Quattro atti che solo Max può fare, in quest'ordine (l'ordine conta):
1. revocare/rigenerare chiave Brevo (B-020);
2. cambiare password Arena + chiave OpenRouter (B-021) — la OpenRouter è viva adesso;
3. cambiare password Instagram (B-023) **poi** rifare il login IG (se si inverte, la sessione
   nuova nasce morta);
4. creare 2 Payment Link Stripe (+ login LinkedIn, 1 minuto).

**In parallelo, lavoro mio (4-6 h), già identificato riga per riga:**
- link morto `WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/preventivo-template.md:10` →
  `Clienti/Prof Autocad/preventivo-forge/templates/preventivo.html` non esiste;
- `company/Ecosistemi/08-STREAM-S7-BOT/` è una cartella quasi vuota che duplica
  `12-STREAM-S7-BOT` e viola ADR-001 (due `08`): fondere, non cancellare;
- `company/Memory/BACKLOG.md`: il blocco `B-001..B-012` compare **2 volte** (artefatto di merge);
- `company/skills-map.yaml`: mancano `tesoreria` e `ultimo-metro`;
- `registro-agenti.yaml`: mancano `conoscenza-empire` e i 5 `tesoreria-*`.

Chiusi questi, `empire doctor` va a 0 bloccanti e i due `verify-*` tornano verdi.

## Poi

**S2 — la fetta verticale.** `WF-S1-CONCESSIONARI` da `start` a `done`, 5 step, contratto C4
solo per i ~10 agenti che tocca, tracce automatiche, avviato da EMPERATOR. Chiude il terzo
gate dello STRUMENTO ZERO, aperto dal 31 agosto.
**Prima di tutto, in S2: riaprire la finestra di `empire flow`** — è scaduta il 26 luglio ed
è il vero motivo per cui nessuno step si chiude.

## Trappole trovate, da non ricalpestare

1. **`empire forge scan` conta 439 agenti, `empire registry census` ne conta 69.** Uno dei due
   mente. Va deciso **prima** di S3, o si scrivono 314 contratti dentro un censimento falso.
2. **Non invertire l'ordine credenziali → login.** Cambiare la password Instagram dopo aver
   rifatto la sessione la invalida: si rifà due volte.
3. **Collisioni di numerazione con le sessioni parallele.** Il 5 settembre sono già collisi
   ADR-022 e CP-018 nello stesso giorno. Verificare il numero libero **nel momento in cui si
   scrive**, mai a memoria. I CP si coniano con `python scripts/checkpoint.py cp`.
4. **La tentazione ricorrente:** aprire un lavoro di carta (studio, dossier, PDF) al posto di
   uno scaglione. È esattamente ciò che ha tenuto ferme nove misure su undici per cinque
   giorni.

## Riferimenti

- Piano: `PIANO-MAESTRO/30-PIANO-COMPLETAMENTO-IMPERO.md`
- Task madre: `company/Memory/tasks/TASK-MAX-20260831-IMPERO-OPERATIVO.md`
- Checkpoint: `company/Memory/checkpoints/CP-20260905-NUJJ.md`
- Audit d'origine: `company/Memory/audit/AUD-20260831-001.md`
- LANCI (non parte prima di S2): `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI.md`
