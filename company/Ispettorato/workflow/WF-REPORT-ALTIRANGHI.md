---
Type: WORKFLOW
Status: Active
Tags: #ispettorato #workflow #altiranghi #board #maximilian #decisioni #isp
Created: 2026-07-20
Last updated: 2026-07-20
---

# WF-REPORT-ALTIRANGHI — Report verso gli Alti Ranghi

- **ID**: `WF-REPORT-ALTIRANGHI`
- **Trigger**: **verso Board / MAXIMILIAN / Max** (direttiva Max, dossier 15 §7 — uno dei 4 cicli)
- **Owner orchestratore**: `isp-conductor` · esecutore: `isp-liaison-altiranghi`
- **Output**: pacchetto report+KPI+errori-aperti instradato + decisione di ritorno tracciata e verificata

---

## Scopo

Portare davanti a chi decide un pacchetto completo e onesto — report, KPI, errori ancora aperti —
instradato per materia, e **chiudere il cerchio**: la decisione che torna viene tracciata e la sua
attuazione verificata. Un report che sale senza che la decisione di ritorno venga eseguita è lavoro
sprecato; questo workflow esiste per impedirlo.

**Instradamento per materia** (dossier 15 §Handoff): KPI e guasti tecnici → **Board C-Suite**; dati
per il 5-bis e metodo → **MAXIMILIAN**; indirizzo, priorità, bocciature/approvazioni → **Max**.

---

## Precondizioni

- I report da instradare esistono (`report/run|daily|escalation/`), prodotti da `isp-report-forger`.
- L'elenco errori APERTI è aggiornato (`isp-error-registrar`), niente voci già chiuse ri-sottoposte.
- I KPI da allegare sono calcolati (`isp-kpi-analyst`).

---

## Passi

1. **Trigger → `isp-conductor`** stabilisce cosa sale e a chi (materia → destinatario).
2. **`isp-liaison-altiranghi` impacchetta**: report + KPI aggregati + lista errori APERTI in un
   unico pacchetto, con la sintesi in testa (cosa serve decidere).
3. **Instrada** il pacchetto al destinatario giusto (Board / MAXIMILIAN / Max). Se la materia è
   ambigua, non indovina: torna a `isp-conductor` (Gate `isp-liaison-altiranghi`).
4. **Traccia la decisione di ritorno** come voce `DEC-YYYYMMDD-NNN` in
   `registro/REGISTRO-DECISIONI-ALTIRANGHI.md`: testo integrale, owner, scadenza, stato APERTA.
5. **`isp-improvement-dispatcher`** converte la decisione in azioni assegnate (se genera lavoro).
6. **`isp-verifier` verifica l'applicazione**: la decisione è stata portata a terra davvero? Con
   evidenza citata → la voce `DEC-*` passa a CHIUSA; altrimenti resta APERTA / IN ATTUAZIONE.

---

## Gate (bloccanti)

- **G-A1** — Nessuna decisione di ritorno persa: ogni ritorno diventa una `DEC-*` PRIMA di essere
  inoltrato a valle (Gate `isp-liaison-altiranghi`).
- **G-A2** — Append-only: una `DEC-*` chiusa non si riscrive; una revisione apre una nuova voce che
  cita la precedente (Gate 3 ARCHITETTURA).
- **G-A3** — Nessuna `DEC-*` dichiarata CHIUSA senza verifica indipendente di `isp-verifier` con
  evidenza citata (Gate 5 ARCHITETTURA — l'Ispettorato assegna e verifica, non si autocertifica).
- **G-A4** — Instradamento per materia corretto: un report sul tavolo sbagliato è un report perso.

---

## DONE WHEN

- Il pacchetto (report + KPI + errori aperti) è stato instradato al destinatario corretto.
- La decisione di ritorno è tracciata come `DEC-*` in `REGISTRO-DECISIONI-ALTIRANGHI.md`.
- Le eventuali azioni derivate sono assegnate (via `isp-improvement-dispatcher`).
- `isp-verifier` ha verificato l'applicazione: la `DEC-*` è CHIUSA con evidenza, o resta aperta con
  motivo esplicito.

---

## Connessioni

- [[ARCHITETTURA]] · `../ARCHITETTURA.md` — Handoff OUT (MAXIMILIAN/Board) · Gate 3/5
- [[15-DOSSIER-ISPETTORATO]] · §7 (trigger "VERSO GLI ALTI RANGHI")
- `company/MAXIMILIAN/ECOSISTEMA.md` · `company/Board-CSuite/` — i destinatari
- `isp-conductor` (batch gemello) · `isp-liaison-altiranghi` · `isp-verifier` · `isp-improvement-dispatcher`
- `isp-report-forger` · `isp-kpi-analyst` · `isp-error-registrar` — le fonti del pacchetto
- `registro/REGISTRO-DECISIONI-ALTIRANGHI.md` — dove vivono le `DEC-*`
