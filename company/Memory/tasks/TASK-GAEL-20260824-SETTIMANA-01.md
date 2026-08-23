---
Owner: Max (committente) · Esecutore: GAEL · Controllore: Claude (review + supporto diretto su TASK-CAROSELLI-W1)
Origine: richiesta esplicita Max 2026-08-23 — cadenza task passa da GIORNALIERA a SETTIMANALE
Governo: ADR-006 (ciclo 9 passi) + REGOLA ZERO memory-first
Emesso: 2026-08-23 · Settimana: W1 (lun 24 ago -> dom 30 ago 2026)
Riferimenti: company/Memory/STATO-EMPIRE.md (blocco 2026-08-23) · EmpireDesk/state/taskboard.json
---

# 📋 Task settimanali GAEL — Settimana 1 (24-30 agosto 2026)

## 0. Come funziona da ora in poi

Non più task giornaliere (G1, G2...). Ogni **domenica** arrivano qui le task della
settimana, ID stabili (`TASK-<AREA>-W<N>`), generali di proposito — non micro-step.
Gestisci tu i giorni: alcuni pieni, altri leggeri, quello che conta è il risultato a
fine settimana. Ogni task chiusa (o comunque ogni fine sessione) → checkpoint in
`company/Memory/checkpoints/` + `stato` aggiornato in `EmpireDesk/state/taskboard.json`.
Item minori che spuntano mentre lavori → `company/Memory/BACKLOG.md`, non fermano la
settimana.

3 task questa settimana. Le prime due sono le tue aree note (KDP, Caroselli — quest'ultima
ora **ufficiale**, non più fuori taskboard). La terza è pezzo di costruzione Impero che
serve davvero alle prime due, non costruzione fine a se stessa.

---

## 🟣 TASK-KDP-W1 — Chiudere il ciclo Workflow KDP end-to-end

**Dove**: `company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/`
(vedi `PIANO-KDP-V2-CLAUDE-CODE.md` e `SOP-SCRIVERE-UN-LIBRO.md` per lo stato attuale —
"The Quiet Hours" è stato prodotto con la SOP a 7 step manuale, LM Arena abbandonato per
il testo per via del captcha).

**Definizione di "finito"** (non prima): dai un comando/topic di avvio →
1. il flusso genera il libro (capitoli reali, non placeholder)
2. produce il prompt per la copertina (pronto da dare al generatore immagini)
3. scrive i copy Amazon (titolo, sottotitolo, descrizione, keyword/categorie — quello che
   serve per pubblicare la scheda)
4. mette tutto — manoscritto, prompt copertina, copy Amazon — dentro **una cartella per
   libro**, organizzata, senza pezzi sparsi tra sessioni/chat come è successo finora

Non serve l'upload automatico su KDP (resta manuale, come da regola generale "azioni
irreversibili verso l'esterno le fa un umano"). Serve che il flusso produca un pacchetto
completo pronto per l'upload, senza intervento manuale in mezzo.

**Dopo che funziona una volta pulita**: l'obiettivo di ritmo è **minimo 5 libri/settimana**,
target **10/settimana**. Non è il gate di questa settimana (prima deve girare bene una volta
end-to-end), ma tienilo come nord — se il flusso richiede passaggi manuali pesanti in mezzo,
quello è il primo posto dove intervenire prima di scalare.

**Gate TASK-KDP-W1**: un libro reale prodotto dall'avvio del flusso alla cartella finale,
senza copiaincolla manuale tra chat/sessioni per nessuno dei 3 output (testo/copertina/copy).
Incolla nel checkpoint: comando di avvio + path della cartella finale + contenuto (o link)
dei 3 artefatti.

---

## 🟠 TASK-CAROSELLI-W1 — Carousel Factory: comando unico, argomento in ingresso, output ordinato

**UFFICIALE DA OGGI** — prima non era nella tua taskboard, ora sì. Motore condiviso Arena
già esistente in `SKILL & Agenti/Workflow agency creative/caroselli - preventa/`
(`orchestrator_preventa.py`, `run_content_factory.py`, `confirm_and_download.py`), output
storico in `SKILL & Agenti/Workflow agency creative/Arsenale Caroselli/<Prodotto>/`.
Reparto formale collegato: `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/
CF-R5-Visual-Design-Caroselli/` (Ramo D, vedi CP-20260806-005 per lo stato — 3 rami A/B/C
ancora mai costruiti, gate CF-R6 non esiste).

**Max lo sa: è un flusso complicato. Claude ti aiuta direttamente su questo, non sei solo
— chiedi supporto appena ti blocchi invece di perdere giorni.**

**Definizione di "finito" per questa settimana**: un comando, un argomento (il topic/brand
del carosello) → il flusso genera i caroselli e li salva per bene, per prodotto, dentro una
cartella (stesso pattern Arsenale Caroselli). Niente passaggi manuali nel mezzo per un
singolo run. Non serve ancora il collegamento alla pubblicazione (vedi TASK-PUBLISHER-W1 —
quello è il prossimo passo, dopo, quando questo gira liscio).

**Gate TASK-CAROSELLI-W1**: un comando con un solo argomento topic produce almeno un
carosello completo, salvato in `Arsenale Caroselli/<Prodotto>/<data_topic>/`, senza
intervento manuale a metà. Incolla comando + path output nel checkpoint.

---

## 🔵 TASK-PUBLISHER-W1 — Consolidare il workflow di pubblicazione multi-canale (serve a Caroselli E a tutto il resto)

**Perché questa e non un'altra**: non è "ricominciare a costruire l'Impero" — è finire un
pezzo che sblocca sia i Caroselli (TASK-CAROSELLI-W1, prossimo passo naturale) sia in
futuro KDP/YouTube (promozione libri, contenuti social dei video). Esiste già, va portato
a uno stato usabile da un comando, non ricostruito da zero.

**Dove**: `SKILL & Agenti/Workflow pubblicazione automatica/` — ha già `main_orchestrator.py`,
bot per Instagram/TikTok/LinkedIn, skill `social-publisher` (`check_ready.py`,
`push_social.py`). C'è anche un wrapper già testato in dry-run per Preventa:
`SKILL & Agenti/Workflow agency creative/caroselli - preventa/publish_instagram.py`
(wrappa `Instagram/instagram_publisher.py`, ADR-003 — non toccare il motore, solo wrappare).

**Definizione di "finito" per questa settimana**: verifica cosa di questo workflow è
realmente funzionante oggi (non aspirazionale — testalo) su almeno Instagram, poi rendilo
richiamabile con un comando semplice che prende una cartella di output (es. un prodotto
dell'Arsenale Caroselli) e la pubblica sul canale giusto. Se trovi pezzi rotti o mai finiti,
documenta onestamente cosa manca invece di far finta che funzioni (stessa regola di sempre:
niente PASS finti).

**Gate TASK-PUBLISHER-W1**: un comando che prende in input una cartella di caroselli già
pronti e pubblica (o fa dry-run verificato, se Max non ha ancora dato ok per il live) su
almeno un canale reale. Incolla comando + esito nel checkpoint.

---

## Regole valide per tutte e 3

1. **Prova, non dichiarazione** — comando + output reale incollato nel checkpoint per ogni gate.
2. **Task chiusa → checkpoint** in `company/Memory/checkpoints/CP-20260824-NNN.md` (primo
   numero libero quando parti) + `stato` aggiornato in `EmpireDesk/state/taskboard.json`
   per l'ID corrispondente (`TASK-KDP-W1`, `TASK-CAROSELLI-W1`, `TASK-PUBLISHER-W1`).
3. Su TASK-CAROSELLI-W1 e TASK-PUBLISHER-W1: se ti blocchi più di una sessione sullo stesso
   punto, scrivi il blocco in `STATO-EMPIRE.md` (blocco ⚠️ COORDINAMENTO) invece di
   insistere da solo — Claude interviene.
4. Item minori scoperti strada facendo → `company/Memory/BACKLOG.md`, non fermano la settimana.
5. Non serve finire tutte e 3 entro domenica per forza — se una è grossa più del previsto,
   dillo nel checkpoint di fine settimana con dove sei arrivato. Meglio un pezzo fatto bene
   di tre abbozzati.

---

## Definition of Done — Settimana 1

- [ ] TASK-KDP-W1: 1 libro reale, flusso unico avvio->cartella finale con 3 artefatti (testo/copertina-prompt/copy Amazon)
- [ ] TASK-CAROSELLI-W1: 1 comando+argomento -> caroselli reali salvati ordinati
- [ ] TASK-PUBLISHER-W1: 1 comando che pubblica (o dry-run verificato) un output caroselli su un canale reale
- [ ] checkpoint di fine settimana con stato reale delle 3 (fatto / parziale+dove sei / bloccato+perché)
