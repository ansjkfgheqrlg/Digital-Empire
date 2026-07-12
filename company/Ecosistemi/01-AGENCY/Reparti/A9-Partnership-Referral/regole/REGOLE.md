---
Type: REGOLE
Status: Active
Tags: #regole #bloccanti #partnership #referral #consenso #gdpr #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# REGOLE — A9 Partnership & Referral

> **Tutte le regole di questo file sono BLOCCANTI.** Non esistono deroghe, eccezioni "per questa
> volta", né bypass da parte di `AG-A9-COORD`. Una violazione è un **rework**, non un incidente
> da documentare e superare.
> Enforcement: `AG-A9-QA` (verifier del reparto). Escalation: `AG-DIR`.

---

## R1 — Nessun lead esce da A9 senza PASS di AG-A9-QA

Ogni lead instradato ad **A8-Closing** o **A2-Acquisizione** deve avere `gate_status = PASS` in
`agency/a9/referrals/{referral_id}`.

- Un handoff senza PASS è **nullo**: il reparto ricevente lo respinge.
- `AG-A9-COORD` **non ha potere di deroga**: coordina il routing, non il gate.
- Violazione ⇒ ritiro dell'handoff + rework del referral.

---

## R2 — Nessun lead da un partner senza accordo scritto firmato

Un partner in stato `candidato` **non può inviare lead**. Non si "testa" un partner con un lead
di prova, non si accetta un lead "mentre finalizziamo l'accordo".

Precondizioni per lo stato `attivo` (verificate da `AG-A9-QA`):
1. accordo referral **scritto e firmato**;
2. commissione **da catalogo** (R6);
3. **briefing ICP eseguito e datato** (`data_briefing` popolata).

Lead ricevuto da partner `candidato` ⇒ respinto, non registrato in pipeline.

---

## R3 — Consenso VERIFICATO su ogni lead (GDPR-light) — BLOCCANTE ASSOLUTA

Nessun lead — referral da partner, segnale da A7, o lead non-ICP risvegliato dal nurture —
può essere contattato o instradato senza **consenso verificato**:

```
consent: { flag: true, data: "YYYY-MM-DD", fonte: "<come è stato raccolto>" }
```

- Un consenso **dichiarato ma non documentato** dal partner è un **FAIL**.
- A9 **non raccoglie il consenso al posto del partner** e **non lo presume** da una relazione
  pregressa ("lo conosco bene", "sta aspettando la chiamata").
- Un lead senza consenso **non viene passato ad A2/A8 in nessun caso**, nemmeno come "solo un
  nome da guardare".
- `AG-A9-QUALIFY` **non contatta mai** i lead non-ICP in triage: il triage è documentale.

Violazione ⇒ lead respinto + richiamo del partner al briefing + `fail_count` incrementato.

---

## R4 — Zero PII negli schemi state

Nei namespace `agency/a9/*` si scrivono **riferimenti**, mai dati personali in chiaro.

- Ammesso: `lead_ref`, `partner_id`, `cliente_id`, azienda, ruolo, settore.
- **Vietato**: nome e cognome della persona, email, telefono, indirizzo, profili personali.
- Il consenso si registra come `{flag, data, fonte}` — **mai** come copia del dato personale.
- I report di `AG-A9-INTEL` sono aggregati su `partner_id` / `lead_ref`. Mai su persone.

Violazione ⇒ record da bonificare prima di qualsiasi altro avanzamento del workflow.

---

## R5 — Zero-Loss: ogni lead non-ICP ha un esito tracciato

Ogni lead ricevuto da A1-Ricerca (verdetto "scarta"/"nurture") deve avere **uno** degli esiti
`PARTNER_POTENZIALE` / `NURTURE` / `ARCHIVIO` scritto in `agency/a9/nonicp/{lead_ref}`, con motivo.

- Un batch con `lead_con_esito < lead_totali` resta **OPEN**: non è chiudibile.
- `AG-A9-INTEL` **non pubblica** i KPI del periodo con copertura < 100%.
- Caso **ambiguo** ⇒ `AG-A9-QUALIFY` **non archivia in autonomia**: escalation `AG-A9-COORD`.

---

## R6 — Commissioni: solo da catalogo, solo con contratto firmato

- La commissione è quella del **catalogo** (fonte di verità: A3-Preventivi). Qualsiasi scostamento
  proposto in trattativa ⇒ **escalation** `AG-A9-COORD` → `AG-DIR`, mai accettazione sul posto.
- Una commissione è `maturata` **solo** se: `contratto_firmato = true` **e** deal confermato in
  `agency/a8/deals`. Senza uno dei due ⇒ `hold`.
- Commissione richiesta da un partner **senza contratto firmato** ⇒ `AG-A9-MGMT` **rifiuta** +
  escalation `AG-DIR`. Nessun pagamento senza accordo.

---

## R7 — Zero metriche inventate

Nessun report, KPI o scorecard può contenere un numero non tracciabile a un namespace.

- Dato non ancora disponibile ⇒ si scrive **`[DM]`** (da misurare). Mai una stima, mai un
  "circa", mai una proiezione presentata come misura.
- Ogni metrica cita la **fonte** (namespace di origine).
- Violazione ⇒ report respinto da `AG-A9-QA`, non pubblicabile ad `AG-DIR`.

---

## R8 — Ownership del lead e recidiva del partner

**Ownership.** Prima del PASS, `AG-A9-QA` verifica che il lead non sia già in `agency/a2/pipeline`
o in `agency/clients`. Conflitto ⇒ escalation `AG-A9-COORD` + coordinatore A2; se non risolto,
`AG-DIR` decide. **Un lead ha un solo proprietario**: mai contattato da due reparti.

**Recidiva.** Partner con **≥2 FAIL su consenso** (R3) ⇒ `AG-A9-MGMT` propone **sospensione** ad
`AG-A9-COORD`. Partner sospeso: nessun lead accettato finché non ripete il briefing ICP e la
sospensione non è revocata per iscritto.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il perché dietro ogni regola
- [[ag-a9-qa]] · `agenti/ag-a9-qa.md` — enforcement di R1..R8
- [[ARCHITETTURA]] · `ARCHITETTURA.md` §6 — gate del reparto
- [[state/README]] · `state/README.md` — schema senza PII (R4)
