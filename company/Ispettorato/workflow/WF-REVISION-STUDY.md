---
Type: WORKFLOW
Status: Active
Tags: #ispettorato #workflow #revisioni #primo-colpo-migliore #successi #isp
Created: 2026-07-20
Last updated: 2026-07-20
---

# WF-REVISION-STUDY — Studio dei Cicli di Correzione ("Primo Colpo Migliore")

- **ID**: `WF-REVISION-STUDY`
- **Trigger**: **dopo ogni ciclo di correzione** (direttiva Max 2026-07-20, dossier 15 §7 — 5° workflow)
- **Owner orchestratore**: `isp-conductor` · esecutore: `isp-revision-analyst`
- **Output**: voce `REV-*` (se N≥1 correzioni) o `SUC-*` (se 0 correzioni) + KPI `revisioni_medie_per_task` aggiornato

---

## Scopo

Direttiva Max: **"se ti richiedo 10 modifiche, studia TUTTE le modifiche — non solo l'ultima — per
fare il lavoro meglio al primo output la prossima volta."** Questo workflow trasforma ogni catena di
correzioni in una **regola generale** scritta, così che il ciclo si accorci nel tempo. E studia
anche i casi a **0 correzioni**: cosa è uscito bene al primo colpo, per ripeterlo di proposito.

L'obiettivo non è il fix del caso singolo: è estrarre ciò che, capito subito, avrebbe azzerato
l'intera catena — e renderlo riusabile per un task futuro diverso ma della stessa classe.

---

## Precondizioni

- Un ciclo di correzione è CHIUSO: l'output umano-Claude è stato accettato (dopo N correzioni, o al
  primo colpo).
- La catena delle correzioni è ricostruibile (chat, commit, diff).
- I registri `REGISTRO-REVISIONI.md` e `REGISTRO-SUCCESSI.md` sono leggibili (formato + anti-duplicati).

---

## Passi

1. **Trigger → `isp-conductor`** apre lo studio a fine ciclo e passa il riferimento del task.
2. **`isp-revision-analyst` ricostruisce la catena COMPLETA**: elenca OGNI correzione — cosa è
   cambiato e perché — non solo l'ultima.
3. **Estrae il pattern**: cosa mancava dal primo output che, capito subito, avrebbe evitato tutte le
   correzioni. Isola la causa comune, non i sintomi.
4. **Scrive la voce** nel formato esatto dei registri esistenti:
   - **N ≥ 1 correzioni** → `REV-YYYYMMDD-NNN` in `registro/REGISTRO-REVISIONI.md` (Task · Correzioni
     ricevute · Catena studiata · Pattern estratto · Regola generale write-once · Collegato a ERR-*).
   - **0 correzioni** → `SUC-YYYYMMDD-NNN` in `registro/REGISTRO-SUCCESSI.md` (Cosa è successo · Perché
     ha funzionato · Pattern da ripetere).
5. **Propaga il feedback**: se il pattern riguarda il modo di lavorare con Max (non solo l'artefatto
   tecnico), lo segnala per `MEMORY.md`.
6. **`isp-kpi-analyst` aggiorna `revisioni_medie_per_task`**: il KPI trend che deve calare nel tempo.
   Se i task non bastano per una media affidabile → "dato insufficiente" (Gate 4).

---

## Gate (bloccanti)

- **G-R1** — La catena COMPLETA, non l'ultima correzione: una `REV-*` che studia solo il fix finale
  è incompleta e va rifatta.
- **G-R2** — Zero correzioni non si ignora: genera sempre una `SUC-*` (studiare anche i successi).
- **G-R3** — Regola GENERALE, non fix locale: il campo "regola generale" deve valere per un task
  futuro diverso della stessa classe. Se vale solo per quel caso, non è ancora una regola.
- **G-R4** — Append-only (Gate 3 ARCHITETTURA): non riscrive voci esistenti, numera in sequenza.
- **G-R5** — Zero numeri inventati (Gate 4): `revisioni_medie_per_task` sui dati reali o "dato
  insufficiente".

---

## DONE WHEN

- Esiste la voce corretta: `REV-*` (N≥1) o `SUC-*` (0 correzioni), nel formato dei registri esistenti.
- **La regola generale estratta è scritta in modo che un futuro task simile la eviti dal primo colpo**
  — non descrive il caso, previene la classe.
- `revisioni_medie_per_task` è aggiornato in `ispettorato/kpi` (o marcato "dato insufficiente").
- Se pertinente, il pattern di lavoro con Max è propagato a `MEMORY.md`.

---

## Connessioni

- [[REGISTRO-REVISIONI]] · `../registro/REGISTRO-REVISIONI.md` — formato REV-* (voci 20260720-001/002)
- [[REGISTRO-SUCCESSI]] · `../registro/REGISTRO-SUCCESSI.md` — formato SUC-* (voci 20260711/20260719)
- [[ARCHITETTURA]] · missione (quarta garanzia: cicli di correzione + successi) · Gate 3/4
- [[15-DOSSIER-ISPETTORATO]] · §7 (trigger "DOPO OGNI CICLO DI CORREZIONE")
- `isp-conductor` · `isp-kpi-analyst` (batch gemello) · `isp-revision-analyst` (esecutore)
- [[REGISTRO-ERRORI]] · collegamento REV-*↔ERR-* · `MEMORY.md` (feedback modo di lavorare)
